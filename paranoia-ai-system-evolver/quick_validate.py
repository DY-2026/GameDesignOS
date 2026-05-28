#!/usr/bin/env python3
"""Lightweight package validation for paranoia-ai-system-evolver."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "agents/openai.yaml",
    "references/evolution-loop-playbook.md",
    "references/evolution-loop-playbook.zh-CN.md",
    "references/evolution-loop-playbook.en.md",
    "references/model-compression-playbook.md",
    "references/model-compression-playbook.zh-CN.md",
    "references/model-compression-playbook.en.md",
    "references/eval-versioning-playbook.md",
    "references/eval-versioning-playbook.zh-CN.md",
    "references/eval-versioning-playbook.en.md",
    "templates/evolution_proposal.md",
    "templates/evolution_proposal.zh-CN.md",
    "templates/evolution_proposal.en.md",
    "templates/ooda_voi_state.md",
    "templates/ooda_voi_state.zh-CN.md",
    "templates/ooda_voi_state.en.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    require(root.is_dir(), f"not a directory: {root}", failures)
    if failures:
        return failures

    for rel in REQUIRED_FILES:
        require((root / rel).is_file(), f"missing required file: {rel}", failures)

    if failures:
        return failures

    skill = read_text(root / "SKILL.md")
    require("name: paranoia-ai-system-evolver" in skill, "SKILL.md name mismatch", failures)
    require("references/model-compression-playbook" in skill, "SKILL.md does not route to model compression playbook", failures)
    require("model compression" in skill.lower(), "SKILL.md lacks model-compression language", failures)

    agent = read_text(root / "agents/openai.yaml")
    require("Paranoia AI System Evolver" in agent, "agents/openai.yaml display name mismatch", failures)

    for rel in ["README.md", "README.zh-CN.md", "README.en.md"]:
        text = read_text(root / rel)
        require("model-compression-playbook" in text, f"{rel} does not list model-compression references", failures)

    for rel in [
        "templates/evolution_proposal.md",
        "templates/evolution_proposal.zh-CN.md",
        "templates/evolution_proposal.en.md",
        "templates/ooda_voi_state.md",
        "templates/ooda_voi_state.zh-CN.md",
        "templates/ooda_voi_state.en.md",
    ]:
        text = read_text(root / rel)
        require("model_audit" in text or "operating_model" in text, f"{rel} lacks model audit fields", failures)

    for rel in [
        "references/evolution-loop-playbook.zh-CN.md",
        "references/evolution-loop-playbook.en.md",
        "references/model-compression-playbook.zh-CN.md",
        "references/model-compression-playbook.en.md",
    ]:
        text = read_text(root / rel)
        require("description_cost" in text or "总描述成本" in text, f"{rel} lacks description cost gate", failures)

    duplicate_keys = re.findall(r"^\s{4,}([a-zA-Z_]+):", read_text(root / "templates/evolution_proposal.en.md"), re.MULTILINE)
    require(
        duplicate_keys.count("failure_recovery_length") == 1,
        "templates/evolution_proposal.en.md has duplicate failure_recovery_length",
        failures,
    )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="skill package root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    failures = validate(root)
    if failures:
        print("quick_validate failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"quick_validate passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
