from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from gamedesignos.constants import VALID_DECISION_TYPES


REPO_ROOT = Path(__file__).resolve().parents[2]


class TrustworthinessSurfaceTest(unittest.TestCase):
    def test_readme_contract_schema_counts_match_repository(self) -> None:
        expected_count = len(list((REPO_ROOT / "contracts").glob("*.schema.json")))
        self.assertGreater(expected_count, 0)

        patterns = {
            "README.md": r"\| Contract schemas \| (\d+) \|",
            "README.en.md": r"\| Contract schemas \| (\d+) \|",
            "README.zh-CN.md": r"\| Contract schema \| (\d+) \|",
        }
        for relative, pattern in patterns.items():
            text = (REPO_ROOT / relative).read_text(encoding="utf-8")
            match = re.search(pattern, text)
            self.assertIsNotNone(match, f"{relative} missing contract schema count row")
            self.assertEqual(
                int(match.group(1)),
                expected_count,
                f"{relative} contract schema count should match contracts/*.schema.json",
            )

    def test_runtime_decision_types_match_decision_schema(self) -> None:
        schema = json.loads((REPO_ROOT / "contracts" / "decision.schema.json").read_text(encoding="utf-8"))
        schema_types = set(schema["properties"]["decision_type"]["enum"])
        missing_from_runtime = schema_types - VALID_DECISION_TYPES
        missing_from_schema = VALID_DECISION_TYPES - schema_types
        self.assertEqual(missing_from_runtime, set())
        self.assertEqual(missing_from_schema, set())


if __name__ == "__main__":
    unittest.main()
