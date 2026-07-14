#!/usr/bin/env python3
"""Create the public-synthetic Lighthouse golden path with one command."""

from __future__ import annotations

import argparse
from pathlib import Path

from gamedesignos.cli import main as cli_main


def invoke(args: list[str]) -> None:
    code = cli_main(args)
    if code:
        raise SystemExit(code)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    destination = args.destination.expanduser().resolve()

    invoke(
        [
            "start",
            "Synthetic Lighthouse Tactics",
            "--destination",
            str(destination),
            "--owner",
            "gamedesignos-golden-fixture",
            "--visibility",
            "public-synthetic",
            "--question",
            "Can players understand the repair-versus-defend tradeoff in three minutes?",
            "--option",
            "Repair-first route",
            "--option",
            "Defense-first route",
            "--default-action",
            "Repair-first route",
            "--assumption",
            "Four of five synthetic testers can explain the tradeoff after three minutes.",
            "--rollback-trigger",
            "Fewer than four of five can explain the tradeoff.",
        ]
    )

    decision_id = next(path.stem for path in (destination / "01-decisions").glob("DEC-*.json"))
    assumption_id = next(path.stem for path in (destination / "02-assumptions").glob("ASM-*.json"))
    experiment_id = next(path.name for path in (destination / "04-experiments").glob("EXP-*"))

    invoke(
        [
            "evidence",
            "add",
            "--workspace",
            str(destination),
            "--decision",
            decision_id,
            "--summary",
            "Synthetic fixture: four of five testers explained the tradeoff.",
            "--source-type",
            "playtest",
            "--source-status",
            "synthetic",
            "--confidence",
            "medium",
            "--decision-impact",
            "Keep repair-first as the next prototype default.",
            "--unsupported-claim",
            "Does not establish retention or commercial demand.",
        ]
    )
    evidence_id = next(path.stem for path in (destination / "03-evidence").glob("EVD-*.json"))
    invoke(
        [
            "experiment",
            "result",
            experiment_id,
            "--workspace",
            str(destination),
            "--status",
            "passed",
            "--observation",
            "Four of five synthetic testers explained the tradeoff.",
            "--evidence",
            evidence_id,
            "--decision-delta",
            "Repair-first remains the reversible default.",
        ]
    )
    invoke(["experiment", "review", experiment_id, "--workspace", str(destination), "--by", "fixture", "--summary", "Synthetic result reviewed; no retention claim allowed."])
    invoke(["assumption", "validate", assumption_id, "--workspace", str(destination), "--status", "tested", "--reason", "Covered by the reviewed synthetic experiment."])
    invoke(["decision", "accept", decision_id, "--workspace", str(destination), "--by", "fixture", "--reason", "Synthetic experiment passed and rollback remains explicit."])
    invoke(["validate", "--workspace", str(destination)])
    print(f"OK: golden project created at {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
