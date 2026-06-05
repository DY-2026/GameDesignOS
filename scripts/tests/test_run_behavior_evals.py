#!/usr/bin/env python3
"""Tests for the behavior eval runner."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "scripts" / "run_behavior_evals.py"


class BehaviorEvalRunnerTest(unittest.TestCase):
    def run_runner(self, eval_payload: dict, output_payload: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            eval_file = tmp_path / "evals.json"
            output_file = tmp_path / "outputs.json"
            eval_file.write_text(json.dumps(eval_payload), encoding="utf-8")
            output_file.write_text(json.dumps(output_payload), encoding="utf-8")

            return subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--evals",
                    str(eval_file),
                    "--outputs",
                    str(output_file),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

    def test_passes_structured_case(self) -> None:
        result = self.run_runner(
            {
                "skill_name": "sample-skill",
                "evals": [
                    {
                        "id": "case_1",
                        "required_sections": ["sample_boundary"],
                        "must_include": ["uncertain"],
                        "must_not_include": ["guaranteed uplift"],
                    }
                ],
            },
            {
                "case_1": {
                    "sample_boundary": "Screenshots only.",
                    "answer": "The result is uncertain.",
                }
            },
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK: 1 behavior evals", result.stdout)

    def test_fails_when_must_include_is_missing(self) -> None:
        result = self.run_runner(
            {
                "evals": [
                    {
                        "id": "missing_include",
                        "must_include": ["rollback"],
                    }
                ],
            },
            {
                "missing_include": {
                    "answer": "No fallback plan provided.",
                }
            },
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing_include: missing required text: rollback", result.stdout)

    def test_fails_when_required_section_is_missing(self) -> None:
        result = self.run_runner(
            {
                "evals": [
                    {
                        "id": "missing_section",
                        "required_sections": ["evidence_index"],
                    }
                ],
            },
            {
                "missing_section": {
                    "answer": "Evidence exists in prose only.",
                }
            },
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing_section: missing required section: evidence_index", result.stdout)


if __name__ == "__main__":
    unittest.main()
