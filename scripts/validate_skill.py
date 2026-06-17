#!/usr/bin/env python3
"""Validate one GameDesignOS skill folder."""

from __future__ import annotations

import argparse
import json
import re
import site
import sys
from pathlib import Path
from typing import Any

USER_SITE = site.getusersitepackages()
try:
    USER_SITE_EXISTS = bool(USER_SITE and Path(USER_SITE).exists())
except OSError:
    USER_SITE_EXISTS = False
if USER_SITE and USER_SITE not in sys.path and USER_SITE_EXISTS:
    sys.path.append(USER_SITE)

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - reported as a validation error.
    yaml = None


MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_ATTR_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.IGNORECASE)
INLINE_PATH_RE = re.compile(
    r"`((?:\.{1,2}/)?(?:SKILL\.md|README(?:\.[A-Za-z0-9_-]+)?\.md|quick_validate\.py|"
    r"agents/[^\s`'\"),]+|assets/[^\s`'\"),]+|evals/[^\s`'\"),]+|examples/[^\s`'\"),]+|"
    r"references/[^\s`'\"),]+|templates/[^\s`'\"),]+))`"
)
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
EXAMPLE_FRONTMATTER_REQUIRED = (
    "case_type",
    "source_status",
    "contains_private_project_info",
    "license_status",
    "intended_use",
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _parse_frontmatter(skill_md: Path, errors: list[str]) -> dict[str, Any]:
    text = _read(skill_md)
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"{skill_md}: missing YAML frontmatter")
        return {}

    raw = match.group(1)
    if yaml is None:
        return _parse_frontmatter_fallback(raw)

    try:
        data = yaml.safe_load(raw) or {}
    except Exception as exc:  # noqa: BLE001 - validator should report parser errors.
        errors.append(f"{skill_md}: invalid frontmatter YAML: {exc}")
        return {}

    if not isinstance(data, dict):
        errors.append(f"{skill_md}: frontmatter must be a mapping")
        return {}
    return data


def _parse_frontmatter_fallback(raw: str) -> dict[str, Any]:
    fields: dict[str, Any] = {}
    for line in raw.splitlines():
        if not (line and line.strip() and not line.lstrip().startswith("#")):
            continue
        match = re.match(r"^\s*([A-Za-z_][A-Za-z0-9_\\-]*)\s*:\s*(.*?)\s*$", line)
        if not match:
            continue
        key = match.group(1)
        value = match.group(2).strip().strip("'\"")
        if value.lower() in {"true", "false"}:
            fields[key] = value.lower() == "true"
        else:
            fields[key] = value
    return fields


def _parse_openai_yaml_fallback(text: str, errors: list[str], path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    interface: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(
            r"^\s*(interface:\s*)?([A-Za-z_][A-Za-z0-9_\\-]*)\s*:\s*(.*)$",
            line,
        )
        if not match:
            continue

        if match.group(1):
            continue

        if line.startswith(" ") and match.group(2) in {"display_name", "short_description", "default_prompt"}:
            value = match.group(3).strip().strip("'\"")
            if line.startswith("  "):  # interface child key
                interface[match.group(2)] = value
        elif match.group(2) in {"display_name", "short_description", "default_prompt"}:
            data[match.group(2)] = match.group(3).strip().strip("'\"")

    if interface:
        data["interface"] = interface
    for key in ("display_name", "short_description", "default_prompt"):
        if not data.get(key) and not interface.get(key):
            errors.append(f"{path}: missing non-empty {key}")
    return data


def _parse_yaml(path: Path, errors: list[str]) -> Any:
    if yaml is None:
        return {}
    try:
        return yaml.safe_load(_read(path))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path}: invalid YAML: {exc}")
        return None


def _parse_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(_read(path))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path}: invalid JSON: {exc}")
        return None


def _is_external_ref(ref: str) -> bool:
    ref = ref.strip()
    return (
        not ref
        or ref.startswith("#")
        or ref.startswith("http://")
        or ref.startswith("https://")
        or ref.startswith("mailto:")
        or ref.startswith("data:")
    )


def _normalize_ref(ref: str) -> str:
    ref = ref.strip().strip("<>")
    if " " in ref and not ref.startswith("./") and not ref.startswith("../"):
        ref = ref.split(" ", 1)[0]
    ref = ref.split("#", 1)[0]
    return ref.rstrip(".,;:。；：，)")


def _check_relative_ref(base_file: Path, ref: str, errors: list[str]) -> None:
    if _is_external_ref(ref):
        return
    target = _normalize_ref(ref)
    if _is_external_ref(target):
        return
    path = (base_file.parent / target).resolve()
    if not path.exists():
        errors.append(f"{base_file}: referenced path does not exist: {ref}")


def _check_references(skill_dir: Path, errors: list[str]) -> None:
    for filename in ("README.md", "SKILL.md"):
        path = skill_dir / filename
        if not path.exists():
            continue
        text = _read(path)

        for match in MARKDOWN_LINK_RE.finditer(text):
            _check_relative_ref(path, match.group(1), errors)

        for match in HTML_ATTR_RE.finditer(text):
            _check_relative_ref(path, match.group(1), errors)

        for match in INLINE_PATH_RE.finditer(text):
            _check_relative_ref(path, match.group(1), errors)


def _check_openai_yaml(skill_dir: Path, errors: list[str]) -> None:
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        return

    if yaml is None:
        _parse_openai_yaml_fallback(_read(openai_yaml), errors, openai_yaml)
        return

    data = _parse_yaml(openai_yaml, errors)
    if not isinstance(data, dict):
        errors.append(f"{openai_yaml}: must be a YAML mapping")
        return

    interface = data.get("interface")
    if not isinstance(interface, dict):
        interface = {}

    for key in ("display_name", "short_description", "default_prompt"):
        value = data.get(key, interface.get(key))
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{openai_yaml}: missing non-empty {key}")


def _check_data_files(skill_dir: Path, errors: list[str]) -> None:
    for path in sorted(skill_dir.rglob("*.json")):
        data = _parse_json(path, errors)
        if path.name.endswith(".schema.json"):
            if not isinstance(data, dict):
                errors.append(f"{path}: schema file must be a JSON object")
            elif "$schema" not in data:
                errors.append(
                    f"{path}: *.schema.json must contain $schema; rename to "
                    "*.example.json or *.contract.json if it is not a schema"
                )

    for pattern in ("*.yaml", "*.yml"):
        for path in sorted(skill_dir.rglob(pattern)):
            _parse_yaml(path, errors)


def _check_example_frontmatter(skill_dir: Path, errors: list[str]) -> None:
    examples_dir = skill_dir / "examples"
    if not examples_dir.exists():
        return

    for path in sorted(examples_dir.glob("*.md")):
        data = _parse_frontmatter(path, errors)
        for key in EXAMPLE_FRONTMATTER_REQUIRED:
            if key not in data:
                errors.append(f"{path}: example frontmatter missing {key}")

        if data.get("contains_private_project_info") is not False:
            errors.append(f"{path}: contains_private_project_info must be false")


def validate_skill(skill_dir: Path) -> list[str]:
    skill_dir = skill_dir.resolve()
    errors: list[str] = []

    if not skill_dir.exists():
        return [f"{skill_dir}: skill folder does not exist"]
    if not skill_dir.is_dir():
        return [f"{skill_dir}: not a directory"]

    skill_md = skill_dir / "SKILL.md"
    readme_md = skill_dir / "README.md"

    if not skill_md.exists():
        errors.append(f"{skill_dir}: SKILL.md missing")
    if not readme_md.exists():
        errors.append(f"{skill_dir}: README.md missing")

    if skill_md.exists():
        frontmatter = _parse_frontmatter(skill_md, errors)
        name = frontmatter.get("name")
        if name != skill_dir.name:
            errors.append(f"{skill_md}: frontmatter name must equal folder name '{skill_dir.name}'")

    _check_openai_yaml(skill_dir, errors)
    _check_references(skill_dir, errors)
    _check_data_files(skill_dir, errors)
    _check_example_frontmatter(skill_dir, errors)

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate one GameDesignOS skill folder.")
    parser.add_argument("skill_folder", help="Skill folder path, for example game-experience-analyzer")
    args = parser.parse_args(argv)

    errors = validate_skill(Path(args.skill_folder))
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {Path(args.skill_folder)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
