#!/usr/bin/env python3
"""Run static behavior eval assertions against captured skill outputs.

This runner does not call a model. It checks a saved output artifact against
repo-defined behavior expectations such as required sections, required text,
forbidden text, and hard-fail markers.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _eval_cases(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        cases = payload.get("evals", [])
    else:
        cases = payload
    if not isinstance(cases, list):
        raise ValueError("evals payload must be a list or an object with an evals list")
    return [case for case in cases if isinstance(case, dict)]


def _output_map(payload: Any) -> dict[str, Any]:
    if isinstance(payload, dict):
        return payload
    if isinstance(payload, list):
        mapped: dict[str, Any] = {}
        for item in payload:
            if isinstance(item, dict) and "id" in item:
                mapped[str(item["id"])] = item.get("output", item)
        return mapped
    raise ValueError("outputs payload must be an object or a list of objects with id")


def _flatten(value: Any) -> str:
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _has_section(output: Any, section: str) -> bool:
    if isinstance(output, dict):
        if section in output:
            return True
        sections = output.get("sections")
        if isinstance(sections, dict) and section in sections:
            return True
        if isinstance(sections, list) and section in {str(item) for item in sections}:
            return True
    return section.lower() in _flatten(output).lower()


def _contains(output_text: str, needle: str) -> bool:
    return needle.lower() in output_text.lower()


def evaluate_case(case: dict[str, Any], output: Any) -> list[str]:
    case_id = str(case.get("id", "<missing-id>"))
    output_text = _flatten(output)
    errors: list[str] = []

    for section in case.get("required_sections", []):
        section_text = str(section)
        if not _has_section(output, section_text):
            errors.append(f"{case_id}: missing required section: {section_text}")

    for text in case.get("must_include", []):
        required_text = str(text)
        if not _contains(output_text, required_text):
            errors.append(f"{case_id}: missing required text: {required_text}")

    for text in case.get("must_not_include", []):
        forbidden_text = str(text)
        if _contains(output_text, forbidden_text):
            errors.append(f"{case_id}: forbidden text present: {forbidden_text}")

    for marker in case.get("hard_fail_if", []):
        hard_fail_marker = str(marker)
        if _contains(output_text, hard_fail_marker):
            errors.append(f"{case_id}: hard fail marker present: {hard_fail_marker}")

    return errors


def evaluate(evals_payload: Any, outputs_payload: Any) -> list[str]:
    cases = _eval_cases(evals_payload)
    outputs = _output_map(outputs_payload)
    errors: list[str] = []

    for case in cases:
        case_id = str(case.get("id", ""))
        if not case_id:
            errors.append("<missing-id>: eval case missing id")
            continue
        if case_id not in outputs:
            errors.append(f"{case_id}: missing output")
            continue
        errors.extend(evaluate_case(case, outputs[case_id]))

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run static GameDesignOS behavior eval assertions.")
    parser.add_argument("--evals", required=True, help="Path to evals JSON.")
    parser.add_argument("--outputs", required=True, help="Path to captured outputs JSON.")
    args = parser.parse_args(argv)

    evals_path = Path(args.evals)
    outputs_path = Path(args.outputs)
    evals_payload = _read_json(evals_path)
    outputs_payload = _read_json(outputs_path)
    errors = evaluate(evals_payload, outputs_payload)

    if errors:
        print("Behavior evals failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(_eval_cases(evals_payload))} behavior evals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
