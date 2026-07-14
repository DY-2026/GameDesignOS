"""Workspace structural and optional canonical-schema validation."""

from __future__ import annotations

import json
import re
from pathlib import Path

from .constants import (
    LIFECYCLE_DIRS,
    PROJECT_READY_LIFECYCLE_DIRS,
    PROJECT_READY_WORKSPACE_SCHEMA_VERSION,
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
from .resources import contracts_dir
from .workspace import ValidationReport, Workspace


def _sensitive(path: Path) -> bool:
    return path.name.lower() in SENSITIVE_BASENAMES or path.suffix.lower() in SENSITIVE_SUFFIXES


def validate_workspace(workspace: Workspace, *, repo_root: Path | None = None) -> ValidationReport:
    report = ValidationReport()
    manifest = workspace.manifest
    if manifest.get("schema_version") not in SUPPORTED_WORKSPACE_SCHEMAS:
        report.errors.append(f"Unsupported workspace schema_version {manifest.get('schema_version')!r}")
    schema_version = str(manifest.get("schema_version") or "")
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
    if schema_version == PROJECT_READY_WORKSPACE_SCHEMA_VERSION:
        for key in (
            "decision_first",
            "evidence_bound",
            "experiment_before_commitment",
            "human_gate_owns_commitment",
            "learning_must_persist",
            "rollback_before_confidence",
            "public_private_boundary",
        ):
            if rules.get(key) is not True:
                report.errors.append(f"rules.{key} must be true")
        lifecycle_dirs = PROJECT_READY_LIFECYCLE_DIRS
    else:
        for key, expected in REQUIRED_RULES.items():
            if rules.get(key) is not expected:
                report.errors.append(f"rules.{key} must be true")
        lifecycle_dirs = LIFECYCLE_DIRS
    for key, default_directory in lifecycle_dirs.items():
        try:
            if not workspace.lifecycle_path(key).is_dir():
                report.errors.append(f"Missing lifecycle directory: {default_directory}")
        except UsageError as exc:
            report.errors.append(str(exc))

    try:
        index = workspace.load_asset_index()
    except UsageError as exc:
        report.errors.append(str(exc))
        index = {"schema_version": schema_version or WORKSPACE_SCHEMA_VERSION, "workspace_id": workspace.workspace_id, "assets": []}
    if index.get("schema_version") != schema_version or index.get("workspace_id") != workspace.workspace_id:
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
        if log.get("schema_version") != schema_version or log.get("workspace_id") != workspace.workspace_id:
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

    if repo_root:
        canonical_contracts = repo_root / "contracts" if (repo_root / "contracts").is_dir() else repo_root
    else:
        try:
            canonical_contracts = contracts_dir(workspace.root)
        except FileNotFoundError:
            canonical_contracts = None
    if canonical_contracts:
        _validate_schemas(workspace, canonical_contracts, report)
    else:
        report.warnings.append("Canonical contracts were not found. Structural validation ran, but JSON Schema validation was skipped.")
    return report


def _project_ready_schema_targets(workspace: Workspace, contracts_root: Path) -> list[tuple[Path, Path]]:
    """Return v1 runtime object files and their canonical schemas.

    The patterns intentionally target runtime-owned v1 records. They avoid broad
    directory-level validation so unrelated skill asset JSON files can still live
    in the same lifecycle folders without being forced into the ledger schemas.
    """

    decisions_dir = workspace.lifecycle_path("decisions_dir")
    assumptions_dir = workspace.lifecycle_path("assumptions_dir")
    evidence_dir = workspace.lifecycle_path("evidence_dir")
    experiments_dir = workspace.lifecycle_path("experiments_dir")
    learning_dir = workspace.lifecycle_path("learning_dir")
    gate_results_dir = workspace.root / ".gamedesignos" / "gate-results"
    workflow_runs_dir = workspace.root / ".gamedesignos" / "workflow-runs"

    targets: list[tuple[Path, Path]] = []
    targets.extend((contracts_root / "decision.schema.json", path) for path in decisions_dir.glob("DEC-*.json"))
    targets.extend((contracts_root / "assumption-registry.schema.json", path) for path in assumptions_dir.glob("ASM-*.json"))
    targets.extend((contracts_root / "assumption-registry.schema.json", path) for path in assumptions_dir.glob("assumption-registry*.json"))
    targets.extend((contracts_root / "evidence-ledger.schema.json", path) for path in evidence_dir.glob("EVD-*.json"))
    targets.extend((contracts_root / "evidence-ledger.schema.json", path) for path in evidence_dir.glob("evidence-ledger*.json"))
    targets.extend((contracts_root / "experiment-plan.schema.json", path) for path in experiments_dir.glob("EXP-*/experiment-plan*.json"))
    targets.extend((contracts_root / "experiment-result.schema.json", path) for path in experiments_dir.glob("EXP-*/experiment-result*.json"))
    targets.extend((contracts_root / "learning-record.schema.json", path) for path in learning_dir.glob("LRN-*.json"))
    targets.extend((contracts_root / "learning-record.schema.json", path) for path in learning_dir.glob("learning-record*.json"))
    targets.extend((contracts_root / "gate-result.schema.json", path) for path in gate_results_dir.glob("*.json"))
    targets.extend((contracts_root / "workflow-run.schema.json", path) for path in workflow_runs_dir.glob("WRUN-*.json"))
    return targets


def _validate_schemas(workspace: Workspace, contracts_root: Path, report: ValidationReport) -> None:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        report.warnings.append("jsonschema is not installed; canonical schema validation skipped")
        return
    targets = [
        (contracts_root / "project-workspace.schema.json", workspace.manifest_path),
        (contracts_root / "design-asset-index.schema.json", workspace.asset_index_path),
        (contracts_root / "decision-log.schema.json", workspace.decision_log_path),
    ]
    voi_schema = contracts_root / "information-value-assessment.schema.json"
    targets.extend((voi_schema, path) for path in workspace.lifecycle_path("decisions_dir").glob("*information-value-assessment*.json"))
    if workspace.manifest.get("schema_version") == PROJECT_READY_WORKSPACE_SCHEMA_VERSION:
        targets.extend(_project_ready_schema_targets(workspace, contracts_root))
    for schema_path, data_path in targets:
        if not schema_path.is_file() or not data_path.is_file():
            continue
        schema = read_json(schema_path)
        data = read_yaml(data_path) if data_path.suffix in {".yaml", ".yml"} else read_json(data_path)
        for error in Draft202012Validator(schema).iter_errors(data):
            location = ".".join(str(part) for part in error.path) or "<root>"
            report.errors.append(f"{data_path.relative_to(workspace.root)}:{location}: {error.message}")
