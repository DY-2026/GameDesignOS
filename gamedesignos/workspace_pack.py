"""Review-safe packaging for registered workspace assets."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path
from typing import Any

from .constants import PACK_ALLOWED_SOURCE_STATUSES, RUNTIME_VERSION
from .errors import UsageError
from .io_utils import ensure_relative_safe
from .workspace import Workspace


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pack_workspace(
    workspace: Workspace,
    *,
    mode: str,
    output: Path | None = None,
    dry_run: bool = False,
    force: bool = False,
) -> dict[str, Any]:
    if mode not in PACK_ALLOWED_SOURCE_STATUSES:
        raise UsageError(f"Unknown pack mode: {mode}")
    report = workspace.validate()
    if not report.ok:
        raise UsageError("Workspace validation failed; pack stopped:\n- " + "\n- ".join(report.errors))
    output = (output or (workspace.root.parent / f"{workspace.workspace_id}-{mode}.zip")).expanduser().resolve()
    if output.exists() and not force:
        raise UsageError(f"Refusing to overwrite existing pack: {output}")
    allowed = PACK_ALLOWED_SOURCE_STATUSES[mode]
    index = workspace.load_asset_index()
    included: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    for item in index["assets"]:
        if not isinstance(item, dict):
            continue
        if item.get("source_status") in allowed:
            included.append(item)
        else:
            excluded.append({"asset_id": item.get("asset_id"), "reason": f"source_status={item.get('source_status')} not allowed"})
    manifest = {
        "runtime_version": RUNTIME_VERSION,
        "workspace_id": workspace.workspace_id,
        "mode": mode,
        "included_assets": [{"asset_id": item.get("asset_id"), "path": item.get("path")} for item in included],
        "excluded_assets": excluded,
    }
    if dry_run:
        return {"output": str(output), "dry_run": True, **manifest}
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists() and force:
        output.unlink()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for item in included:
            relative = str(item["path"])
            archive.write(ensure_relative_safe(workspace.root, relative), arcname=relative)
        filtered_index = {"schema_version": index.get("schema_version"), "workspace_id": workspace.workspace_id, "assets": included}
        summary = {
            "workspace_id": workspace.workspace_id,
            "title": workspace.project.get("title"),
            "status": workspace.project.get("status"),
            "visibility": workspace.visibility,
            "asset_count": len(included),
        }
        archive.writestr("design-asset-index.json", json.dumps(filtered_index, ensure_ascii=False, indent=2) + "\n")
        archive.writestr("gamedesignos-workspace-summary.json", json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
        archive.writestr("gamedesignos-pack-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    manifest["sha256"] = _sha256(output)
    return {"output": str(output), "dry_run": False, **manifest}
