"""Resolve canonical resources in a source checkout or an installed wheel."""

from __future__ import annotations

import os
from pathlib import Path


def find_source_root(start: Path | None = None) -> Path | None:
    """Return a source checkout root when one is available."""

    candidates: list[Path] = []
    configured = os.getenv("GAMEDESIGNOS_HOME")
    if configured:
        candidates.append(Path(configured).expanduser())
    candidates.extend(Path(__file__).resolve().parents)
    current = (start or Path.cwd()).expanduser().resolve()
    if current.is_file():
        current = current.parent
    candidates.extend([current, *current.parents])
    seen: set[Path] = set()
    for candidate in candidates:
        candidate = candidate.resolve()
        if candidate in seen:
            continue
        seen.add(candidate)
        if (candidate / "contracts/router.yaml").is_file():
            return candidate
    return None


def packaged_data_root() -> Path:
    return Path(__file__).resolve().parent / "_data"


def contracts_dir(start: Path | None = None) -> Path:
    source = find_source_root(start)
    if source:
        return source / "contracts"
    packaged = packaged_data_root() / "contracts"
    if packaged.is_dir():
        return packaged
    raise FileNotFoundError(
        "GameDesignOS contracts are unavailable. Reinstall the wheel or set "
        "GAMEDESIGNOS_HOME to a valid source checkout."
    )


def workspace_template_dir(*, project_ready: bool = True, start: Path | None = None) -> Path:
    name = "workspace-template-v1" if project_ready else "workspace-template"
    source = find_source_root(start)
    if source:
        return source / "runtime" / name
    packaged = packaged_data_root() / name
    if packaged.is_dir():
        return packaged
    raise FileNotFoundError(
        f"GameDesignOS template {name!r} is unavailable. Reinstall the wheel or set "
        "GAMEDESIGNOS_HOME to a valid source checkout."
    )


def resource_mode(start: Path | None = None) -> str:
    return "source" if find_source_root(start) else "packaged"
