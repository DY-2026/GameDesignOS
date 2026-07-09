from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from gamedesignos.project_ready import (
    add_evidence,
    add_experiment_result,
    review_experiment,
    run_gate,
    start_project,
    update_decision_status,
    validate_assumption,
    validate_workflow_run,
    workflow_next,
)
from gamedesignos.workspace import Workspace


class ProjectReadySchemaValidationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_full_cycle_runtime_records_validate_against_contracts(self) -> None:
        project = start_project(
            project_name="Schema Golden",
            destination=self.root / "schema-golden",
            owner="tester",
            visibility="private",
            options=["Build a three-minute prototype", "Pause and redefine"],
            default_action="Build a three-minute prototype",
            rollback_trigger="The three-minute prototype cannot produce a readable loop.",
            sample_size=5,
        )
        workspace = Workspace.open(Path(project["workspace"]))
        decision_id = project["decision"]["decision_id"]
        assumption_id = project["assumption"]["assumption_id"]
        experiment_id = project["experiment"]["experiment_id"]
        run_id = project["workflow_run"]["run_id"]

        evidence = add_evidence(
            workspace,
            decision_id=decision_id,
            summary="Five-player synthetic test supports readability, not retention.",
            source_type="playtest",
            source_status="private",
            confidence="medium",
            decision_impact="Keep the prototype as the default action for this sprint.",
            unsupported_claims=["Cannot prove D1 retention or monetization."],
        )
        evidence_id = evidence["evidence"]["evidence_id"]

        add_experiment_result(
            workspace,
            experiment_id,
            status="passed",
            observations=["Four of five testers explained the goal and next action."],
            evidence_refs=[evidence_id],
            decision_delta="The default action remains unchanged.",
        )
        review_experiment(
            workspace,
            experiment_id,
            by="tester",
            summary="Reviewed as readability evidence only; no retention claim promoted.",
        )
        validate_assumption(
            workspace,
            assumption_id,
            status="tested",
            reason="Covered by the reviewed experiment result.",
        )
        run_gate(workspace, "evidence", decision_id, write=True)
        run_gate(workspace, "commitment", decision_id, write=True)
        update_decision_status(
            workspace,
            decision_id,
            status="accepted",
            by="tester",
            reason="Experiment reviewed, evidence boundary recorded, rollback trigger exists.",
        )
        workflow_next(workspace, run_id)

        workflow_report = validate_workflow_run(workspace, run_id)
        self.assertTrue(workflow_report["ok"], workflow_report["errors"])

        report = workspace.validate()
        self.assertTrue(report.ok, "\n".join(report.errors))


if __name__ == "__main__":
    unittest.main()
