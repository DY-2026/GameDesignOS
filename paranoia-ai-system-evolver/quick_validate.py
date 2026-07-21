#!/usr/bin/env python3
"""Lightweight package validation for paranoia-ai-system-evolver."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "agents/openai.yaml",
    "references/value-of-information-playbook.md",
    "references/value-of-information-playbook.zh-CN.md",
    "references/value-of-information-playbook.en.md",
    "references/intent-engineering-work-order.md",
    "references/intent-engineering-work-order.zh-CN.md",
    "references/intent-engineering-work-order.en.md",
    "references/project-workflow-governance.md",
    "references/project-workflow-governance.zh-CN.md",
    "references/project-workflow-governance.en.md",
    "references/evolution-loop-playbook.md",
    "references/evolution-loop-playbook.zh-CN.md",
    "references/evolution-loop-playbook.en.md",
    "references/uncertainty-ladder-protocol.md",
    "references/uncertainty-ladder-protocol.zh-CN.md",
    "references/uncertainty-ladder-protocol.en.md",
    "references/woop-harness-protocol.md",
    "references/woop-harness-protocol.zh-CN.md",
    "references/woop-harness-protocol.en.md",
    "references/model-compression-playbook.md",
    "references/model-compression-playbook.zh-CN.md",
    "references/model-compression-playbook.en.md",
    "references/eval-versioning-playbook.md",
    "references/eval-versioning-playbook.zh-CN.md",
    "references/eval-versioning-playbook.en.md",
    "templates/voi_decision_gate.md",
    "templates/voi_decision_gate.zh-CN.md",
    "templates/voi_decision_gate.en.md",
    "templates/intent_work_order.md",
    "templates/intent_work_order.zh-CN.md",
    "templates/intent_work_order.en.md",
    "templates/workflow_governance_review.md",
    "templates/workflow_governance_review.zh-CN.md",
    "templates/workflow_governance_review.en.md",
    "templates/evolution_proposal.md",
    "templates/evolution_proposal.zh-CN.md",
    "templates/evolution_proposal.en.md",
    "templates/ooda_voi_state.md",
    "templates/ooda_voi_state.zh-CN.md",
    "templates/ooda_voi_state.en.md",
    "templates/uncertainty_ladder_state.md",
    "templates/uncertainty_ladder_state.zh-CN.md",
    "templates/uncertainty_ladder_state.en.md",
    "evals/voi-decision-gate-cases.md",
    "evals/voi-decision-gate-cases.en.md",
    "evals/uncertainty-ladder-cases.md",
    "evals/uncertainty-ladder-cases.en.md",
    "examples/ul-state.example.json",
]

VOI_FIELDS = [
    "decision_question",
    "options",
    "current_default_action",
    "boundary_status",
    "candidate_information_actions",
    "expected_signals",
    "action_if_seen",
    "acquisition_cost",
    "latency_cost",
    "attention_cost",
    "stop_rule",
]

RJR_FIELDS = [
    "rjr_authority_gate",
    "delegation_matrix",
    "coupling",
    "authority_level",
    "residual_judgment",
]

UNCERTAINTY_LADDER_FIELDS = [
    "current_rung",
    "uncertainty_exposure",
    "released_this_round",
    "held_constant",
    "scaffolds_present",
    "consequence_budget",
    "attribution_gate",
    "graduation_evidence",
    "transfer_checks",
    "fallback_rung",
    "rollback",
    "stop_rule",
    "human_gate",
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
    require("references/value-of-information-playbook" in skill, "SKILL.md does not route to VOI playbook", failures)
    require("references/intent-engineering-work-order" in skill, "SKILL.md does not route to intent work order playbook", failures)
    require("references/project-workflow-governance" in skill, "SKILL.md does not route to workflow governance playbook", failures)
    require("references/model-compression-playbook" in skill, "SKILL.md does not route to model compression playbook", failures)
    require("Intent Work Order" in skill, "SKILL.md lacks Intent Work Order language", failures)
    require("workflow-run.governance" in skill, "SKILL.md lacks workflow governance language", failures)
    require("reality_to_change" in skill, "SKILL.md lacks intent reality-to-change field", failures)
    require("WOOP" in skill, "SKILL.md lacks WOOP language", failures)
    require("EVPI" in skill and "EVSI" in skill, "SKILL.md lacks EVPI/EVSI distinction", failures)
    require("current_default_action" in skill, "SKILL.md lacks current default action gate", failures)
    require("Scenario VOI Adapter" in skill, "SKILL.md lacks Scenario VOI Adapter routing", failures)
    require("RJR-AI" in skill, "SKILL.md lacks RJR-AI authority layer", failures)
    require("Uncertainty Ladder" in skill, "SKILL.md lacks Uncertainty Ladder control layer", failures)
    require("references/uncertainty-ladder-protocol" in skill, "SKILL.md does not route to uncertainty ladder protocol", failures)
    require("剩余判断权" in skill, "SKILL.md lacks residual judgment language", failures)
    require("停止" in skill or "stop" in skill.lower(), "SKILL.md lacks stop-rule language", failures)

    agent = read_text(root / "agents/openai.yaml")
    require("Paranoia AI System Evolver" in agent, "agents/openai.yaml display name mismatch", failures)
    require("current default action" in agent.lower(), "agents/openai.yaml lacks decision-default language", failures)
    require("EVPI/EVSI" in agent, "agents/openai.yaml lacks EVPI/EVSI", failures)
    require("不确定性阶梯" in agent, "agents/openai.yaml lacks uncertainty ladder language", failures)

    for rel in ["README.md", "README.zh-CN.md", "README.en.md"]:
        text = read_text(root / rel)
        require("value-of-information-playbook" in text, f"{rel} does not list VOI reference", failures)
        require("intent-engineering-work-order" in text, f"{rel} does not list intent-work-order reference", failures)
        require("project-workflow-governance" in text, f"{rel} does not list workflow governance reference", failures)
        require("voi_decision_gate" in text, f"{rel} does not list VOI template", failures)
        require("intent_work_order" in text, f"{rel} does not list intent-work-order template", failures)
        require("workflow_governance_review" in text, f"{rel} does not list workflow governance template", failures)
        require("model-compression-playbook" in text, f"{rel} does not list model-compression reference", failures)
        require("woop-harness-protocol" in text, f"{rel} does not list WOOP harness reference", failures)
        require("uncertainty-ladder-protocol" in text, f"{rel} does not list uncertainty ladder reference", failures)
        require("uncertainty_ladder_state" in text, f"{rel} does not list uncertainty ladder template", failures)

    for rel in [
        "templates/intent_work_order.md",
        "templates/intent_work_order.zh-CN.md",
        "templates/intent_work_order.en.md",
    ]:
        text = read_text(root / rel)
        for field in [
            "intent_work_order",
            "reality_to_change",
            "parent_project_goal",
            "desired_world_state",
            "verifier_role",
            "first_impression_must_understand",
            "must_not_sacrifice",
            "ai_can_freely_change",
            "ai_must_not_touch",
            "decision_principles_if_plan_breaks",
            "failure_signals_to_check_before_delivery",
            "retrospective_contract",
            "promotion_status",
        ]:
            require(field in text, f"{rel} lacks intent-work-order field: {field}", failures)

    for rel in [
        "templates/workflow_governance_review.md",
        "templates/workflow_governance_review.zh-CN.md",
        "templates/workflow_governance_review.en.md",
    ]:
        text = read_text(root / rel)
        for field in [
            "workflow_governance_review",
            "enforcement_mode",
            "intent_work_order_ref",
            "decision_ref",
            "voi_gate_ref",
            "rjr_authority_ref",
            "paranoia_review_ref",
            "human_gate_refs",
            "rollback_ref",
            "candidate_learning_refs",
            "promotion_status",
        ]:
            require(field in text, f"{rel} lacks workflow governance field: {field}", failures)

    for rel in [
        "templates/voi_decision_gate.md",
        "templates/voi_decision_gate.zh-CN.md",
        "templates/voi_decision_gate.en.md",
        "templates/ooda_voi_state.md",
        "templates/ooda_voi_state.zh-CN.md",
        "templates/ooda_voi_state.en.md",
        "templates/evolution_proposal.md",
        "templates/evolution_proposal.zh-CN.md",
        "templates/evolution_proposal.en.md",
    ]:
        text = read_text(root / rel)
        for field in VOI_FIELDS:
            require(field in text, f"{rel} lacks VOI field: {field}", failures)
        require("woop_task_card" in text or "woop:" in text or "voi_decision_gate" in text, f"{rel} lacks task/VOI control structure", failures)
        if rel.startswith("templates/evolution_proposal"):
            for field in RJR_FIELDS:
                require(field in text, f"{rel} lacks RJR field: {field}", failures)
            for field in UNCERTAINTY_LADDER_FIELDS:
                require(field in text, f"{rel} lacks uncertainty ladder field: {field}", failures)
        if rel.startswith("templates/voi_decision_gate"):
            for field in ["scenario_voi", "valid_evidence", "weak_evidence", "preferred_probe", "domain_stop_rule"]:
                require(field in text, f"{rel} lacks scenario VOI field: {field}", failures)

    voi_zh = read_text(root / "references/value-of-information-playbook.zh-CN.md")
    voi_en = read_text(root / "references/value-of-information-playbook.en.md")
    for token in ["EVPI", "EVPPI", "EVSI", "current_default_action", "signal", "stop"]:
        require(token.lower() in voi_zh.lower(), f"Chinese VOI playbook lacks {token}", failures)
        require(token.lower() in voi_en.lower(), f"English VOI playbook lacks {token}", failures)
    require("信息消费" in voi_zh, "Chinese VOI playbook lacks information-consumption classification", failures)
    require("AI 疲劳" in voi_zh, "Chinese VOI playbook lacks AI fatigue gate", failures)
    require("高结构" in voi_zh, "Chinese VOI playbook lacks high-structure/low-VOI gate", failures)
    require("场景 VOI Adapter" in voi_zh, "Chinese VOI playbook lacks scenario adapter", failures)
    require("Scenario VOI Adapter" in voi_en, "English VOI playbook lacks scenario adapter", failures)

    intent_zh = read_text(root / "references/intent-engineering-work-order.zh-CN.md")
    intent_en = read_text(root / "references/intent-engineering-work-order.en.md")
    for token in ["意图工程", "我要改变什么现实", "验收者第一眼", "ai_must_not_touch", "retrospective_contract"]:
        require(token in intent_zh, f"Chinese intent playbook lacks {token}", failures)
    for token in ["intent engineering", "What reality should change", "first glance", "retrospective"]:
        require(token.lower() in intent_en.lower(), f"English intent playbook lacks {token}", failures)

    governance_zh = read_text(root / "references/project-workflow-governance.zh-CN.md")
    governance_en = read_text(root / "references/project-workflow-governance.en.md")
    for token in [
        "workflow-run.governance",
        "enforcement_mode",
        "shadow",
        "warn",
        "enforce",
        "intent_work_order_ref",
        "voi_gate_ref",
        "rjr_authority_ref",
        "paranoia_review_ref",
        "human_gate_refs",
        "rollback_ref",
        "candidate_learning_refs",
    ]:
        require(token in governance_zh, f"Chinese workflow governance playbook lacks {token}", failures)
        require(token in governance_en, f"English workflow governance playbook lacks {token}", failures)

    evolution_zh = read_text(root / "references/evolution-loop-playbook.zh-CN.md")
    evolution_en = read_text(root / "references/evolution-loop-playbook.en.md")
    require("Decision Object" in evolution_zh, "Chinese evolution playbook lacks Decision Object", failures)
    require("Decision Object" in evolution_en, "English evolution playbook lacks Decision Object", failures)
    require("RJR-AI" in evolution_zh and "剩余判断权" in evolution_zh, "Chinese evolution playbook lacks RJR authority layer", failures)
    require("RJR-AI" in evolution_en and "residual judgment" in evolution_en.lower(), "English evolution playbook lacks RJR authority layer", failures)
    require("description_cost" in evolution_zh or "总描述成本" in evolution_zh, "Chinese evolution playbook lacks description cost", failures)
    require("total_description_cost" in evolution_en, "English evolution playbook lacks description cost", failures)
    require("不确定性阶梯" in evolution_zh and "confounded" in evolution_zh, "Chinese evolution playbook lacks uncertainty ladder attribution gate", failures)
    require("Uncertainty Ladder" in evolution_en and "confounded" in evolution_en, "English evolution playbook lacks uncertainty ladder attribution gate", failures)

    for rel in [
        "templates/uncertainty_ladder_state.md",
        "templates/uncertainty_ladder_state.zh-CN.md",
        "templates/uncertainty_ladder_state.en.md",
    ]:
        text = read_text(root / rel)
        for field in UNCERTAINTY_LADDER_FIELDS:
            require(field in text, f"{rel} lacks uncertainty ladder field: {field}", failures)
        for field in ("schema_version", "ul_id"):
            require(field in text, f"{rel} lacks UL identity field: {field}", failures)

    ladder_zh = read_text(root / "references/uncertainty-ladder-protocol.zh-CN.md")
    ladder_en = read_text(root / "references/uncertainty-ladder-protocol.en.md")
    for token in ["UL-L0", "UL-L3", "UL-L5", "ul_state", "released_this_round", "confounded", "Human Gate"]:
        require(token in ladder_zh, f"Chinese uncertainty ladder protocol lacks {token}", failures)
        require(token in ladder_en, f"English uncertainty ladder protocol lacks {token}", failures)

    try:
        ul_example = json.loads(read_text(root / "examples/ul-state.example.json"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"examples/ul-state.example.json is invalid JSON: {exc}")
        ul_example = {}
    for field in ("schema_version", "ul_id", "current_rung", "attribution_gate", "transfer_checks", "human_gate"):
        require(field in ul_example, f"UL example lacks field: {field}", failures)
    require(
        isinstance(ul_example.get("current_rung"), str) and ul_example["current_rung"].startswith("UL-L"),
        "UL example current_rung must use UL-L0..UL-L5",
        failures,
    )

    eval_zh = read_text(root / "evals/voi-decision-gate-cases.md")
    eval_en = read_text(root / "evals/voi-decision-gate-cases.en.md")
    for marker in ["FOMO", "决策边界", "负反馈", "分支爆炸", "不可逆"]:
        require(marker in eval_zh, f"Chinese VOI evals lack case marker: {marker}", failures)
    require(eval_zh.count("## Case") >= 9, "Chinese VOI evals need at least 9 cases", failures)
    require(eval_en.count("## ") >= 9, "English VOI evals need at least 9 cases", failures)
    require("场景 VOI 错配" in eval_zh, "Chinese VOI evals lack scenario mismatch case", failures)
    require("Scenario VOI mismatch" in eval_en, "English VOI evals lack scenario mismatch case", failures)
    require("RJR-AI" in eval_zh and "剩余判断权" in eval_zh, "Chinese VOI evals lack RJR authority case", failures)
    require("RJR-AI" in eval_en and "residual judgment" in eval_en.lower(), "English VOI evals lack RJR authority case", failures)
    require("workflow-run.governance" in eval_zh, "Chinese VOI evals lack workflow governance case", failures)
    require("workflow-run.governance" in eval_en, "English VOI evals lack workflow governance case", failures)

    ladder_eval_zh = read_text(root / "evals/uncertainty-ladder-cases.md")
    ladder_eval_en = read_text(root / "evals/uncertainty-ladder-cases.en.md")
    require(ladder_eval_zh.count("## Case") >= 6, "Chinese uncertainty ladder evals need at least 6 cases", failures)
    require(ladder_eval_en.count("## Case") >= 6, "English uncertainty ladder evals need at least 6 cases", failures)
    for token in ["confounded", "迁移", "Human Gate"]:
        require(token in ladder_eval_zh, f"Chinese uncertainty ladder evals lack {token}", failures)
    for token in ["confounded", "transfer", "Human Gate"]:
        require(token.lower() in ladder_eval_en.lower(), f"English uncertainty ladder evals lack {token}", failures)

    duplicate_keys = re.findall(
        r"^\s{4,}([a-zA-Z_]+):",
        read_text(root / "templates/evolution_proposal.en.md"),
        re.MULTILINE,
    )
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
