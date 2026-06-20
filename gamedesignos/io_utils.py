"""Small, auditable filesystem helpers."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import unicodedata
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised in dependency-minimal clones.
    yaml = None

from .errors import UsageError


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(value: str, *, fallback: str = "untitled") -> str:
    raw = value.strip()
    ascii_value = (
        unicodedata.normalize("NFKD", raw).encode("ascii", "ignore").decode("ascii")
    )
    slug = _SLUG_RE.sub("-", ascii_value.lower()).strip("-")
    if not slug:
        if raw:
            digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:8]
            slug = f"{fallback}-{digest}"
        else:
            slug = fallback
    if not slug[0].isalnum():
        slug = f"p-{slug}"
    return slug[:64].rstrip("-")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise UsageError(f"Invalid JSON in {path}: {exc}") from exc


def read_yaml(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
        if yaml is not None:
            return yaml.safe_load(text)
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise UsageError(
                f"PyYAML is required to read this YAML file: {path}. "
                "Install with `python -m pip install -e .`."
            ) from exc
    except FileNotFoundError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise UsageError(f"Invalid YAML in {path}: {exc}") from exc


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def write_json(path: Path, data: Any) -> None:
    _atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def write_yaml(path: Path, data: Any) -> None:
    if yaml is not None:
        _atomic_write(path, yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
    else:
        _atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def write_text(path: Path, content: str) -> None:
    _atomic_write(path, content.rstrip() + "\n")


def ensure_relative_safe(root: Path, relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise UsageError(f"Unsafe workspace-relative path: {relative}")
    resolved_root = root.resolve()
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise UsageError(f"Path escapes workspace: {relative}") from exc
    return resolved


def is_nonempty_directory(path: Path) -> bool:
    return path.is_dir() and any(path.iterdir())
