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
    "game-experience-density-optimizer",
]

REQUIRED_PATHS = [
    ".gitignore",
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "contracts/README.md",
    "contracts/router.yaml",
    "contracts/ed-handoff.schema.json",
    "CONTRIBUTING.md",
    "LICENSE",
    "adapters/README.md",
    ".github/workflows/validate.yml",
    "scripts/run_behavior_evals.py",
]

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "_private_translations",
    ".venv",
    "venv",
    "node_modules",
}

PRIVATE_IGNORE_RULES = {
    "_private_translations/",
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


def _check_private_ignore_rules(repo_root: Path, errors: list[str]) -> None:
    gitignore = repo_root / ".gitignore"
    if not gitignore.exists():
        return

    rules = {
        line.strip()
        for line in gitignore.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    for required in sorted(PRIVATE_IGNORE_RULES):
        accepted = {
            required,
            required.rstrip("/"),
            f"/{required}",
            f"/{required.rstrip('/')}",
        }
        if rules.isdisjoint(accepted):
            errors.append(f".gitignore: missing required private ignore rule {required}")


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
    _check_private_ignore_rules(repo_root, all_errors)

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
