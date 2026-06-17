#!/usr/bin/env python3
"""Validate and sync a GameDesignOS package into the OpenCode global skill dir."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path


DEFAULT_SKILL = "paranoia-ai-system-evolver"
FRONTMATTER_NAME_RE = re.compile(r"^name:\s*([^\n]+)$", re.MULTILINE)
INLINE_SKILL_REF_RE = re.compile(
    r"`((?:references|templates|agents|assets|examples|evals)/[^`]+|README(?:\.[A-Za-z0-9_-]+)?\.md|quick_validate\.py)`"
)


def run_check(command: list[str], cwd: Path) -> None:
    printable = " ".join(command)
    print(f"$ {printable}")
    subprocess.run(command, cwd=cwd, check=True)


def validate_skill(repo_root: Path, skill_dir: Path) -> None:
    run_check([sys.executable, str(repo_root / "scripts" / "validate_skill.py"), str(skill_dir)], repo_root)
    quick_validate = skill_dir / "quick_validate.py"
    if quick_validate.exists():
        run_check([sys.executable, str(quick_validate), str(skill_dir)], skill_dir)


def validate_installed_skill(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        raise FileNotFoundError(f"missing installed SKILL.md: {skill_md}")

    skill_text = skill_md.read_text(encoding="utf-8")
    name_match = FRONTMATTER_NAME_RE.search(skill_text)
    if not name_match or name_match.group(1).strip().strip('"\'') != skill_dir.name:
        raise ValueError(f"installed SKILL.md name must equal folder name: {skill_dir.name}")

    for match in INLINE_SKILL_REF_RE.finditer(skill_text):
        ref = match.group(1).split("#", 1)[0]
        if not (skill_dir / ref).exists():
            raise FileNotFoundError(f"installed SKILL.md references missing path: {ref}")

    quick_validate = skill_dir / "quick_validate.py"
    if quick_validate.exists():
        run_check([sys.executable, str(quick_validate), str(skill_dir)], skill_dir)


def copy_skill(source: Path, target: Path, repo_root: Path) -> None:
    global_root = target.parent
    temp_parent = global_root / ".sync-tmp"
    temp_target = temp_parent / target.name
    backup_target = global_root / f".{target.name}.backup-{time.strftime('%Y%m%d%H%M%S')}"

    restored = False
    try:
        if temp_parent.exists():
            shutil.rmtree(temp_parent)
        temp_parent.mkdir(parents=True, exist_ok=True)

        print(f"copy: {source} -> {temp_target}")
        shutil.copytree(source, temp_target)
        validate_installed_skill(temp_target)

        if target.exists():
            print(f"backup: {target} -> {backup_target}")
            shutil.move(str(target), str(backup_target))
        print(f"install: {temp_target} -> {target}")
        shutil.move(str(temp_target), str(target))
        validate_installed_skill(target)
    except Exception:
        if backup_target.exists() and not target.exists():
            print(f"restore: {backup_target} -> {target}")
            shutil.move(str(backup_target), str(target))
            restored = True
        raise
    finally:
        if temp_parent.exists():
            shutil.rmtree(temp_parent)

    if backup_target.exists() and not restored:
        print(f"backup kept for rollback: {backup_target}")


def default_global_root() -> Path:
    home = Path(os.environ.get("USERPROFILE") or Path.home())
    return home / ".config" / "opencode" / "skills"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", nargs="?", default=DEFAULT_SKILL, help="Skill folder name to sync")
    parser.add_argument("--global-root", type=Path, default=default_global_root(), help="OpenCode global skills root")
    parser.add_argument("--dry-run", action="store_true", help="Validate only; do not copy")
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    source = repo_root / args.skill
    target = args.global_root.expanduser().resolve() / args.skill

    if not source.is_dir():
        print(f"missing source skill directory: {source}", file=sys.stderr)
        return 1
    if not args.global_root.expanduser().resolve().is_dir():
        print(f"missing global skills root: {args.global_root}", file=sys.stderr)
        return 1

    print(f"source: {source}")
    print(f"target: {target}")
    validate_skill(repo_root, source)

    if args.dry_run:
        print("dry-run passed; no files copied")
        return 0

    copy_skill(source, target, repo_root)
    print(f"sync passed: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
