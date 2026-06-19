"""Workspace initialization and local runtime diagnostics."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

from .constants import LIFECYCLE_DIRS, RUNTIME_VERSION, VALID_VISIBILITIES, WORKSPACE_GUIDES
from .errors import UsageError, WorkspaceNotFoundError
from .io_utils import is_nonempty_directory, slugify, write_json, write_text, write_yaml
from .templates import decision_brief_markdown, empty_asset_index, empty_decision_log, workspace_manifest
from .workspace import Workspace, find_repo_root


def init_workspace(
    *,
    project_name: str,
    destination: Path,
    codename: str | None,
    visibility: str,
    owner: str,
    force: bool = False,
    dry_run: bool = False,
) -> dict[str, Any]:
    if visibility not in VALID_VISIBILITIES:
        raise UsageError(f"Invalid visibility: {visibility}")
    destination = destination.expanduser().resolve()
    if not project_name.strip():
        raise UsageError("project_name must not be empty")
    if destination.exists() and is_nonempty_directory(destination) and not force:
        raise UsageError(f"Refusing to overwrite non-empty directory {destination}. Use --force only after review.")
    if force and ((destination / "game.designos.yaml").exists() or (destination / "design-asset-index.json").exists()):
        raise UsageError("--force never overwrites an existing GameDesignOS workspace")
    project_id = slugify(codename or project_name)
    manifest = workspace_manifest(
        project_id=project_id,
        title=project_name.strip(),
        codename=slugify(codename or project_name),
        visibility=visibility,
        owner=owner.strip() or "designer",
    )
    planned = ["game.designos.yaml", "design-asset-index.json", *[f"{d}/README.md" for d in LIFECYCLE_DIRS.values()], "06-decisions/decision-log.json", "06-decisions/decision-brief.template.md"]
    if dry_run:
        return {"workspace": str(destination), "project_id": project_id, "dry_run": True, "planned_paths": planned}
    destination.mkdir(parents=True, exist_ok=True)
    write_yaml(destination / "game.designos.yaml", manifest)
    write_json(destination / "design-asset-index.json", empty_asset_index(project_id))
    for directory, guide in WORKSPACE_GUIDES.items():
        path = destination / directory
        path.mkdir(parents=True, exist_ok=True)
        readme = path / "README.md"
        if not readme.exists() or force:
            write_text(readme, f"# {directory}\n\n{guide}\n")
    write_json(destination / "06-decisions/decision-log.json", empty_decision_log(project_id))
    write_text(destination / "06-decisions/decision-brief.template.md", decision_brief_markdown(project_name.strip()))
    return {"workspace": str(destination), "project_id": project_id, "dry_run": False, "created_paths": planned}


def doctor(workspace_path: Path | None = None) -> dict[str, Any]:
    checks: list[dict[str, Any]] = [
        {"name": "python", "ok": sys.version_info >= (3, 11), "detail": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"},
    ]
    for name in ("yaml", "jsonschema"):
        try:
            __import__(name)
            checks.append({"name": name, "ok": True, "detail": "available"})
        except ImportError:
            checks.append({"name": name, "ok": False, "detail": "missing"})
    repo = find_repo_root(workspace_path)
    checks.append({"name": "canonical-repository", "ok": repo is not None, "detail": str(repo) if repo else "not found; set GAMEDESIGNOS_HOME for schema/router access"})
    try:
        workspace = Workspace.open(workspace_path)
        status = workspace.status()
        checks.extend(
            [
                {"name": "workspace", "ok": True, "detail": str(workspace.root)},
                {"name": "workspace-compatibility", "ok": status.compatible, "detail": f"schema={status.workspace_schema_version}, runtime={status.runtime_version_declared}"},
                {"name": "workspace-write-access", "ok": os.access(workspace.root, os.W_OK), "detail": str(os.access(workspace.root, os.W_OK))},
            ]
        )
    except WorkspaceNotFoundError as exc:
        checks.append({"name": "workspace", "ok": workspace_path is None, "detail": "optional: not currently inside a workspace" if workspace_path is None else str(exc)})
    required = [item for item in checks if item["name"] != "canonical-repository"]
    return {"ok": all(item["ok"] for item in required), "runtime_version": RUNTIME_VERSION, "checks": checks}
