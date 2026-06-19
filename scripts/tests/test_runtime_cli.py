from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from gamedesignos.cli import main
from gamedesignos.errors import EXIT_OK, UsageError
from gamedesignos.routing import route_task
from gamedesignos.voi import create_assessment, review_assessment
from gamedesignos.workspace import Workspace, init_workspace


class RuntimeCliTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def workspace(self, name: str = "Clockwork Garden", visibility: str = "private") -> Workspace:
        target = self.root / name.replace(" ", "-").lower()
        init_workspace(project_name=name, destination=target, codename=None, visibility=visibility, owner="tester")
        return Workspace.open(target)

    def test_01_init_and_validate(self) -> None:
        ws = self.workspace()
        self.assertTrue(ws.validate().ok)
        self.assertEqual(ws.status().runtime_version_declared, "0.9.0")
        self.assertTrue(ws.decision_log_path.is_file())

    def test_02_init_refuses_nonempty(self) -> None:
        target = self.root / "occupied"
        target.mkdir()
        keep = target / "keep.txt"
        keep.write_text("keep", encoding="utf-8")
        self.assertNotEqual(main(["init", "Occupied", "--destination", str(target)]), EXIT_OK)
        self.assertEqual(keep.read_text(encoding="utf-8"), "keep")

    def test_03_chinese_name_gets_ascii_id(self) -> None:
        result = init_workspace(project_name="灯塔战术", destination=self.root / "cn", codename=None, visibility="private", owner="tester")
        self.assertRegex(result["project_id"], r"^untitled-[0-9a-f]{8}$")

    def test_04_explicit_missing_workspace_fails(self) -> None:
        self.assertNotEqual(main(["route", "analyze recording", "--workspace", str(self.root / "missing")]), EXIT_OK)

    def test_05_new_asset_registers_file(self) -> None:
        ws = self.workspace()
        result = ws.create_asset("concept", title="Repairing Lighthouse")
        self.assertTrue(Path(result["path"]).is_file())
        self.assertEqual(ws.load_asset_index()["assets"][0]["asset_type"], "concept")

    def test_06_media_routes_to_analyzer(self) -> None:
        result = route_task("请分析这段试玩录屏里的首局体验")
        self.assertEqual(result["selected_skill"], "game-experience-analyzer")
        self.assertFalse(result["executed"])

    def test_07_ed_missing_evidence_routes_upstream(self) -> None:
        result = route_task("设计首局留存和反馈强度的一周 A/B 测试", workspace=self.workspace())
        self.assertEqual(result["selected_skill"], "game-experience-analyzer")
        self.assertEqual(result["target_skill"], "game-experience-density-optimizer")

    def test_08_proposal_after_concept(self) -> None:
        ws = self.workspace()
        ws.create_asset("concept", title="Concept")
        ws.create_asset("validation-plan", title="Validation")
        result = route_task("assemble a publisher pitch proposal", workspace=ws)
        self.assertEqual(result["selected_skill"], "game-design-proposal-writer")
        self.assertEqual(result["missing_upstream"], [])

    def test_09_voi_near_selects_probe(self) -> None:
        ws = self.workspace()
        result = create_assessment(
            ws,
            decision_id="DEC-PROTOTYPE-001",
            decision_question="Which prototype receives the next week?",
            options=["Build combat prototype", "Build economy prototype"],
            current_default_action="Build combat prototype",
            owner="tester",
            stakes="high",
            reversibility="reversible",
            boundary="near",
            candidate_information_actions=["Run five-player paper test"],
            stop_when=["Five sessions complete"],
        )
        path = Path(result["path"])
        data = json.loads(path.read_text(encoding="utf-8"))
        data["candidate_information_actions"][0]["costs"] = {
            "acquisition": "low", "latency": "low", "attention": "low", "privacy_or_contamination": "none"
        }
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        reviewed = review_assessment(path, write=True)
        self.assertTrue(reviewed["ok"])
        self.assertEqual(reviewed["selected_probe"]["action_id"], "INFO-001")

    def test_10_voi_rejects_invalid_decision(self) -> None:
        with self.assertRaises(UsageError):
            create_assessment(
                self.workspace(), decision_id="bad", decision_question="What?", options=["A", "A"],
                current_default_action="A", owner="tester", stakes="medium", reversibility="reversible",
                boundary="near", candidate_information_actions=[], stop_when=None,
            )

    def test_11_locked_decision_stops_research(self) -> None:
        result = create_assessment(
            self.workspace(), decision_id="DEC-LOCKED-001", decision_question="Reopen scope?",
            options=["Execute", "Reopen"], current_default_action="Execute", owner="tester",
            stakes="medium", reversibility="costly_to_reverse", boundary="locked",
            candidate_information_actions=["Read another trend report"], stop_when=None,
        )
        reviewed = review_assessment(Path(result["path"]))
        self.assertTrue(reviewed["ok"])
        self.assertIsNone(reviewed["selected_probe"])

    def test_12_public_pack_filters(self) -> None:
        ws = self.workspace("Synthetic Lighthouse", "public-synthetic")
        ws.create_asset("concept", title="Synthetic Concept")
        output = self.root / "pack.zip"
        ws.pack(mode="public-synthetic", output=output)
        with zipfile.ZipFile(output) as archive:
            names = set(archive.namelist())
            index = json.loads(archive.read("design-asset-index.json"))
        self.assertIn("01-concept/synthetic-concept.md", names)
        self.assertNotIn("game.designos.yaml", names)
        self.assertEqual(len(index["assets"]), 1)

    def test_13_pack_overwrite_requires_force(self) -> None:
        ws = self.workspace("Pack Guard", "public-synthetic")
        ws.create_asset("concept", title="Synthetic Concept")
        output = self.root / "guard.zip"
        ws.pack(mode="public-synthetic", output=output)
        with self.assertRaises(UsageError):
            ws.pack(mode="public-synthetic", output=output)
        self.assertFalse(ws.pack(mode="public-synthetic", output=output, force=True)["dry_run"])

    def test_14_public_validation_rejects_private_asset(self) -> None:
        ws = self.workspace("Synthetic Broken", "public-synthetic")
        ws.create_asset("concept", title="Synthetic Concept")
        index = ws.load_asset_index()
        index["assets"][0]["source_status"] = "private"
        ws.asset_index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(any("non-synthetic" in item for item in ws.validate().errors))

    def test_15_cli_smoke_second_workspace(self) -> None:
        target = self.root / "lighthouse"
        self.assertEqual(main(["init", "Lighthouse Tactics", "--destination", str(target), "--visibility", "public-synthetic", "--owner", "fixture"]), EXIT_OK)
        self.assertEqual(main(["new", "decision", "--workspace", str(target), "--title", "Prototype Direction"]), EXIT_OK)
        self.assertEqual(main(["validate", "--workspace", str(target)]), EXIT_OK)


if __name__ == "__main__":
    unittest.main()
