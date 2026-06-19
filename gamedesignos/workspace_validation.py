"""Workspace structural and optional canonical-schema validation."""

from __future__ import annotations

import json
import re
from pathlib import Path

from .constants import (
    LIFECYCLE_DIRS,
    PUBLIC_BASE_REPO,
    REQUIRED_RULES,
    RUNTIME_VERSION,
    SENSITIVE_BASENAMES,
    SENSITIVE_SUFFIXES,
    SUPPORTED_RUNTIME_VERSIONS,
    SUPPORTED_WORKSPACE_SCHEMAS,
    VALID_ASSET_FORMATS,
    VALID_ASSET_TYPES,
    VALID_CREATED_BY,
    VALID_DECISION_STATUSES,
    VALID_DECISION_TYPES,
    VALID_PROJECT_STATUSES,
    VALID_REVIEW_STATUSES,
    VALID_SOURCE_STATUSES,
    VALID_VISIBILITIES,
    WORKSPACE_SCHEMA_VERSION,
    WORKSPACE_TYPE,
)
from .errors import UsageError
from .io_utils import ensure_relative_safe, read_json, read_yaml
from .workspace import ValidationReport, Workspace, find_repo_root


def _sensitive(path: Path) -> bool:
    return path.name.lower() in SENSITIVE_BASENAMES or path.suffix.lower() in SENSITIVE_SUFFIXES


def validate_workspace(workspace: Workspace, *, repo_root: Path | None = None) -> ValidationReport:
    report = ValidationReport()
    manifest = workspace.manifest
    if manifest.get("schema_version") not in SUPPORTED_WORKSPACE_SCHEMAS:
        report.errors.append(f"Unsupported workspace schema_version {manifest.get('schema_version')!r}")
    if manifest.get("workspace_type") != WORKSPACE_TYPE:
        report.errors.append(f"workspace_type must be {WORKSPACE_TYPE}")
    for name in ("id", "title", "codename", "status", "visibility", "owner"):
        if not isinstance(workspace.project.get(name), str) or not str(workspace.project.get(name)).strip():
            report.errors.append(f"project.{name} must be a non-empty string")
    if isinstance(workspace.project.get("id"), str) and not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,63}", workspace.project["id"]):
        report.errors.append("project.id is invalid")
    if workspace.project.get("status") not in VALID_PROJECT_STATUSES:
        report.errors.append("project.status is invalid")
    if workspace.project.get("visibility") not in VALID_VISIBILITIES:
        report.errors.append("project.visibility is invalid")
    if workspace.designos.get("version") not in SUPPORTED_RUNTIME_VERSIONS:
        report.errors.append(f"designos.version {workspace.designos.get('version')!r} is incompatible with runtime {RUNTIME_VERSION}")
    if workspace.designos.get("public_base_repo") != PUBLIC_BASE_REPO:
        report.errors.append(f"designos.public_base_repo must be {PUBLIC_BASE_REPO}")
    rules = manifest.get("rules") if isinstance(manifest.get("rules"), dict) else {}
    for key, expected in REQUIRED_RULES.items():
        if rules.get(key) is not expected:
            report.errors.append(f"rules.{key} must be true")
    for key in LIFECYCLE_DIRS:
        try:
            if not workspace.lifecycle_path(key).is_dir():
                report.errors.append(f"Missing lifecycle directory: {LIFECYCLE_DIRS[key]}")
        except UsageError as exc:
            report.errors.append(str(exc))

    try:
        index = workspace.load_asset_index()
    except UsageError as exc:
        report.errors.append(str(exc))
        index = {"schema_version": WORKSPACE_SCHEMA_VERSION, "workspace_id": workspace.workspace_id, "assets": []}
    if index.get("schema_version") != WORKSPACE_SCHEMA_VERSION or index.get("workspace_id") != workspace.workspace_id:
        report.errors.append("asset index version/workspace_id mismatch")
    assets = [item for item in index.get("assets", []) if isinstance(item, dict)]
    ids = {str(item.get("asset_id")) for item in assets}
    seen_paths: set[str] = set()
    for item in assets:
        asset_id = str(item.get("asset_id") or "<unknown>")
        if not re.fullmatch(r"ASSET-[A-Z0-9-]{3,}", asset_id):
            report.errors.append(f"invalid asset_id: {asset_id}")
        if item.get("asset_type") not in VALID_ASSET_TYPES:
            report.errors.append(f"{asset_id}: invalid asset_type")
        if item.get("format") not in VALID_ASSET_FORMATS or item.get("created_by") not in VALID_CREATED_BY:
            report.errors.append(f"{asset_id}: invalid format/created_by")
        if item.get("source_status") not in VALID_SOURCE_STATUSES or item.get("review_status") not in VALID_REVIEW_STATUSES:
            report.errors.append(f"{asset_id}: invalid source/review status")
        relative = str(item.get("path") or "")
        if not relative or relative in seen_paths:
            report.errors.append(f"{asset_id}: missing or duplicate path")
        else:
            seen_paths.add(relative)
            try:
                target = ensure_relative_safe(workspace.root, relative)
                if not target.exists():
                    report.errors.append(f"Registered asset file is missing: {relative}")
                if _sensitive(target):
                    report.errors.append(f"Sensitive file registered: {relative}")
            except UsageError as exc:
                report.errors.append(str(exc))
        for field in ("upstream_assets", "downstream_assets", "supersedes"):
            for ref in item.get(field, []) or []:
                if ref not in ids:
                    report.errors.append(f"{asset_id}.{field} references unknown asset {ref}")
        if workspace.visibility == "public-synthetic" and item.get("source_status") != "synthetic":
            report.errors.append(f"public-synthetic workspace contains non-synthetic asset {asset_id}: {item.get('source_status')}")
        if workspace.visibility == "public-cleared" and item.get("source_status") in {"private", "needs_review"}:
            report.errors.append(f"public-cleared workspace contains unsafe asset {asset_id}")

    try:
        log = workspace.load_decision_log()
        if log.get("schema_version") != WORKSPACE_SCHEMA_VERSION or log.get("workspace_id") != workspace.workspace_id:
            report.errors.append("decision log version/workspace_id mismatch")
        for decision in log.get("decisions", []):
            if not isinstance(decision, dict):
                report.errors.append("decision entry must be an object")
            elif decision.get("decision_type") not in VALID_DECISION_TYPES or decision.get("status") not in VALID_DECISION_STATUSES:
                report.errors.append("decision type/status is invalid")
    except UsageError as exc:
        report.errors.append(str(exc))

    for path in workspace.root.rglob("*.json"):
        if _sensitive(path):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            report.errors.append(f"Invalid JSON {path.relative_to(workspace.root)}: {exc}")

    canonical = repo_root or find_repo_root(workspace.root)
    if canonical:
        _validate_schemas(workspace, canonical, report)
    else:
        report.warnings.append("Canonical contracts were not found. Structural validation ran, but JSON Schema validation was skipped.")
    return report


def _validate_schemas(workspace: Workspace, repo_root: Path, report: ValidationReport) -> None:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        report.warnings.append("jsonschema is not installed; canonical schema validation skipped")
        return
    targets = [
        (repo_root / "contracts/project-workspace.schema.json", workspace.manifest_path),
        (repo_root / "contracts/design-asset-index.schema.json", workspace.asset_index_path),
        (repo_root / "contracts/decision-log.schema.json", workspace.decision_log_path),
    ]
    voi_schema = repo_root / "contracts/information-value-assessment.schema.json"
    targets.extend((voi_schema, path) for path in workspace.lifecycle_path("decisions_dir").glob("*information-value-assessment*.json"))
    for schema_path, data_path in targets:
        if not schema_path.is_file() or not data_path.is_file():
            continue
        schema = read_json(schema_path)
        data = read_yaml(data_path) if data_path.suffix in {".yaml", ".yml"} else read_json(data_path)
        for error in Draft202012Validator(schema).iter_errors(data):
            location = ".".join(str(part) for part in error.path) or "<root>"
            report.errors.append(f"{data_path.relative_to(workspace.root)}:{location}: {error.message}")
