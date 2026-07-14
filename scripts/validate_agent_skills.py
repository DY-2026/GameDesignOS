#!/usr/bin/env python3
"""Validate every public skill with the official Agent Skills reference CLI."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def main() -> int:
    executable = shutil.which("agentskills")
    if not executable:
        print("Agent Skills validation failed: `agentskills` is not installed; install .[dev]")
        return 1
    root = Path(__file__).resolve().parents[1]
    skills = sorted(path.parent for path in root.glob("*/SKILL.md"))
    if not skills:
        print("Agent Skills validation failed: no public skills found")
        return 1
    for skill in skills:
        result = subprocess.run([executable, "validate", str(skill)], check=False)
        if result.returncode:
            return result.returncode
    print(f"OK: {len(skills)} Agent Skills packages validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
