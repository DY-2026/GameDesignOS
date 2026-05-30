#!/usr/bin/env python3
"""Validate the public ParanoiaSkills repository."""

from __future__ import annotations

from pathlib import Path

from validate_skill import _parse_json, _parse_yaml, validate_skill


REQUIRED_SKILLS = [
    "game-experience-analyzer",
    "game-concept-architect",
    "paranoia-ai-system-evolver",
    "game-design-book-translator",
    "game-design-source-curator",
]

REQUIRED_PATHS = [
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "contracts/README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "adapters/README.md",
    ".github/workflows/validate.yml",
]

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "node_modules",
}


def _iter_data_files(repo_root: Path):
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(repo_root).parts):
            continue
        if path.suffix == ".json" or path.suffix in {".yaml", ".yml"}:
            yield path


def _check_required_paths(repo_root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_PATHS:
        path = repo_root / relative
        if not path.exists():
            errors.append(f"{relative}: required path missing")


def _check_repo_data_files(repo_root: Path, errors: list[str]) -> None:
    for path in _iter_data_files(repo_root):
        if path.suffix == ".json":
            data = _parse_json(path, errors)
            if path.name.endswith(".schema.json"):
                if not isinstance(data, dict):
                    errors.append(f"{path}: schema file must be a JSON object")
                elif "$schema" not in data:
                    errors.append(f"{path}: *.schema.json must contain $schema")
        else:
            _parse_yaml(path, errors)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    all_errors: list[str] = []

    _check_required_paths(repo_root, all_errors)

    for skill_name in REQUIRED_SKILLS:
        skill_dir = repo_root / skill_name
        if not skill_dir.exists():
            all_errors.append(f"{skill_name}: required skill folder missing")
            continue
        all_errors.extend(validate_skill(skill_dir))

    _check_repo_data_files(repo_root, all_errors)

    if all_errors:
        print("Repository validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("OK: repository")
    print("Validated skills:")
    for skill_name in REQUIRED_SKILLS:
        print(f"- {skill_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
