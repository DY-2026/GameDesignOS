"""Deterministic workspace and artifact templates.

The runtime deliberately writes explicit placeholders instead of invented evidence.
"""

from __future__ import annotations

from datetime import date
from typing import Any

from .constants import (
    LIFECYCLE_DIRS,
    PUBLIC_BASE_REPO,
    REQUIRED_RULES,
    RUNTIME_VERSION,
    WORKSPACE_SCHEMA_VERSION,
    WORKSPACE_TYPE,
)


def workspace_manifest(
    *, project_id: str, title: str, codename: str, visibility: str, owner: str
) -> dict[str, Any]:
    return {
        "schema_version": WORKSPACE_SCHEMA_VERSION,
        "workspace_type": WORKSPACE_TYPE,
        "project": {
            "id": project_id,
            "title": title,
            "codename": codename,
            "status": "concept",
            "visibility": visibility,
            "owner": owner,
            "target_platforms": [],
            "tags": [],
        },
        "designos": {
            "version": RUNTIME_VERSION,
            "public_base_repo": PUBLIC_BASE_REPO,
            "private_overlay": visibility == "private",
        },
        "assets": {"index": "design-asset-index.json", **LIFECYCLE_DIRS},
        "rules": dict(REQUIRED_RULES),
    }


def empty_asset_index(workspace_id: str) -> dict[str, Any]:
    return {
        "schema_version": WORKSPACE_SCHEMA_VERSION,
        "workspace_id": workspace_id,
        "assets": [],
    }


def empty_decision_log(workspace_id: str) -> dict[str, Any]:
    return {
        "schema_version": WORKSPACE_SCHEMA_VERSION,
        "workspace_id": workspace_id,
        "decisions": [],
    }


def decision_brief_markdown(project_title: str) -> str:
    return f"""# Decision Brief — {project_title}

## Decision Object

- Decision ID: `DEC-001`
- Owner: TODO
- Deadline or gate: TODO
- Decision question: TODO
- Current default action: TODO
- Boundary status: `undefined | far | near | locked`
- Stakes: `low | medium | high | critical`
- Reversibility: `reversible | costly_to_reverse | irreversible`

## Real Options

1. TODO
2. TODO

## Action-Sensitive Uncertainty

Only list uncertainty that can change option ranking or a stop condition.

- TODO

## Candidate Information Actions

Use no more than three per round. For each action, name the possible signals and the action following each signal.

## Stop Rule

- Stop when: TODO
- Fallback action: TODO

## Human Gate

- Commitment-changing decision required: yes
- Decision owner: TODO
"""


def _markdown_stub(title: str, asset_id: str, sections: list[str]) -> str:
    lines = [
        f"# {title}",
        "",
        f"- Asset ID: `{asset_id}`",
        "- Review status: `draft`",
        "- Evidence status: `not supplied`",
        "",
        "> This is a runtime-generated stub. Replace TODO fields with project evidence or explicit assumptions.",
        "",
    ]
    for section in sections:
        lines.extend([f"## {section}", "", "TODO", ""])
    return "\n".join(lines).rstrip() + "\n"


def asset_body(command_name: str, *, asset_id: str, title: str, workspace_id: str) -> Any:
    today = date.today().isoformat()

    if command_name == "concept":
        return _markdown_stub(
            title,
            asset_id,
            ["Concept Seed", "Player Verbs", "Player Promise", "Core Loop", "Scope Gate", "Next Validation"],
        )

    if command_name == "evidence-index":
        return {
            "evidence_index_id": asset_id.replace("ASSET-", "EVIDENCE-"),
            "workspace_id": workspace_id,
            "sample_boundary": {
                "included": [],
                "excluded": [],
                "unsupported_claims": ["No evidence has been added yet."],
            },
            "sources": [],
            "evidence_items": [],
            "review_status": "draft",
        }

    if command_name == "issue-card":
        return {
            "issue_id": asset_id.replace("ASSET-", "ISSUE-"),
            "title": title,
            "symptom": "TODO: observed symptom",
            "evidence_refs": [],
            "interpretation": "TODO: interpretation, explicitly separated from observed fact",
            "severity": "needs_review",
            "confidence": 0,
            "unknowns": ["Evidence not supplied"],
            "recommended_probe": "TODO: smallest probe that could change the action",
        }

    if command_name == "validation-plan":
        return {
            "validation_id": asset_id.replace("ASSET-", "VALIDATION-"),
            "target_assumption": "TODO: assumption to test",
            "prototype_scope": "TODO: smallest testable scope",
            "test_method": "TODO: sample, playtest, interview, benchmark, or A/B method",
            "success_criteria": ["TODO: observable success criterion"],
            "failure_criteria": ["TODO: observable failure criterion"],
            "next_investment_condition": "TODO: condition for increasing investment",
            "kill_condition": "TODO: condition for stopping or changing direction",
            "evidence_required": ["TODO: minimum evidence required"],
        }

    if command_name == "information-assessment":
        return information_assessment_skeleton(
            assessment_id=asset_id.replace("ASSET-VOI-", "VOI-"),
            decision_id="DEC-001",
            workspace_id=workspace_id,
            owner="TODO",
            decision_question="TODO: decision question",
            options=["TODO: option A", "TODO: option B"],
            current_default_action="TODO: default action",
            stakes="medium",
            reversibility="reversible",
            boundary="undefined",
            candidate_information_actions=[],
        )

    if command_name == "ed-handoff":
        return {
            "handoff_id": "EDH001",
            "source_skill": "game-experience-analyzer",
            "target_skill": "game-experience-density-optimizer",
            "case_boundary": {
                "supported": [],
                "unsupported": ["No evidence has been added yet."],
            },
            "issue_cards_for_ed": [
                {
                    "issue_id": "ISSUE-TODO",
                    "evidence_refs": ["TODO-EVIDENCE-REF"],
                    "symptom": "TODO",
                    "ed_terms": [],
                    "suggested_primary_lever": "TODO",
                    "confidence": 0,
                    "unknowns": ["Evidence not supplied"],
                    "unsupported_by_sample": True,
                }
            ],
            "unsupported_judgment_scope": ["Retention, revenue, and player sentiment are unsupported."],
            "recommended_next_step": "Replace placeholder issue with an evidence-linked issue card.",
        }

    if command_name == "experiment":
        return _markdown_stub(
            title,
            asset_id,
            [
                "Evidence Gate",
                "Target Decision",
                "Primary Lever",
                "Variants",
                "Instrumentation",
                "Decision Rules",
                "Rollback Gate",
            ],
        )

    if command_name == "proposal":
        return _markdown_stub(
            title,
            asset_id,
            ["Decision Request", "Player Promise", "Proof of Play", "Scope", "Evidence", "Risks", "Milestone Gate"],
        )

    if command_name == "decision":
        return {
            "decision_id": asset_id.replace("ASSET-DECISION-", "DEC-"),
            "date": today,
            "decision_type": "information",
            "status": "proposed",
            "decision": "TODO: proposed decision",
            "context": "TODO: decision context",
            "options_considered": ["TODO: option A", "TODO: option B"],
            "evidence_refs": [],
            "assumptions": ["TODO: explicit assumption"],
            "risks": ["TODO: risk"],
            "owner": "TODO",
            "rollback_trigger": "TODO: observable rollback trigger",
            "current_default_action": "TODO: current default action",
            "decision_boundary": "undefined",
            "voi_assessment_refs": [],
            "action_before_information": "TODO",
            "action_after_information": "TODO",
            "information_stop_reason": "TODO: why research stopped",
        }

    if command_name == "retrospective":
        return _markdown_stub(
            title,
            asset_id,
            ["Expected Outcome", "Observed Outcome", "Decision Delta", "Failures", "Reusable Learning", "Candidate Workflow Change"],
        )

    raise KeyError(command_name)


def information_assessment_skeleton(
    *,
    assessment_id: str,
    decision_id: str,
    workspace_id: str,
    owner: str,
    decision_question: str,
    options: list[str],
    current_default_action: str,
    stakes: str,
    reversibility: str,
    boundary: str,
    candidate_information_actions: list[str],
    stop_when: list[str] | None = None,
    deadline: str | None = None,
) -> dict[str, Any]:
    option_items = [
        {"option_id": f"OPT-{index:02d}", "action": action}
        for index, action in enumerate(options, start=1)
    ]
    alternative = next((item for item in options if item != current_default_action), current_default_action)

    uncertainty_map = []
    actions = []
    for index, action in enumerate(candidate_information_actions, start=1):
        uncertainty_id = f"U-{index:03d}"
        action_id = f"INFO-{index:03d}"
        uncertainty_map.append(
            {
                "uncertainty_id": uncertainty_id,
                "uncertainty": f"TODO: uncertainty targeted by {action}",
                "current_belief_or_range": "TODO",
                "confidence": "low",
                "impact_if_wrong": stakes,
                "affected_options": [item["option_id"] for item in option_items],
                "could_change_option_ranking": boundary == "near",
                "observable": True,
                "controllable": False,
            }
        )
        conclusion = {
            "undefined": "ask_human",
            "far": "timebox_learning",
            "near": "ask_human",
            "locked": "skip",
        }[boundary]
        actions.append(
            {
                "action_id": action_id,
                "action": action,
                "target_uncertainty": uncertainty_id,
                "information_type": "sample",
                "expected_signals": [
                    {
                        "signal": "TODO: signal strong enough to change option ranking",
                        "posterior_update": "TODO",
                        "action_if_seen": alternative,
                    },
                    {
                        "signal": "TODO: signal insufficient to justify switching",
                        "posterior_update": "TODO",
                        "action_if_seen": current_default_action,
                    },
                ],
                "could_change_action": boundary == "near" and alternative != current_default_action,
                "reliability_and_bias": "TODO: reliability, blind spots, and contamination risk",
                "evpi_upper_bound": "qualitative upper bound not yet estimated",
                "evsi_estimate": "not yet estimated",
                "approximate_net_voi": "not yet estimated",
                "costs": {
                    "acquisition": "TODO",
                    "latency": "TODO",
                    "attention": "TODO",
                    "privacy_or_contamination": "TODO",
                },
                "conclusion": conclusion,
            }
        )

    return {
        "schema_version": WORKSPACE_SCHEMA_VERSION,
        "assessment_id": assessment_id,
        "workspace_id": workspace_id,
        "information_mode": "decision_information",
        "decision": {
            "decision_id": decision_id,
            "owner": owner,
            **({"deadline": deadline} if deadline else {}),
            "decision_question": decision_question,
            "options": option_items,
            "current_default_action": current_default_action,
            "stakes": stakes,
            "reversibility": reversibility,
            "boundary_status": boundary,
        },
        "utility_model": {
            "objective": "TODO: objective or value function",
            "decision_delta_if_wrong": "TODO: cost of taking the wrong action",
            "key_payoffs_or_losses": [],
            "assumptions": ["No numeric EV claim is made by this scaffold."],
        },
        "uncertainty_map": uncertainty_map,
        "candidate_information_actions": actions,
        "selected_probe": None,
        "stop_rule": {
            "stop_when": stop_when
            or [
                "All plausible signals map to the same action.",
                "The decision deadline is reached.",
                "Marginal VOI is non-positive.",
            ],
            "fallback_action": current_default_action,
        },
    }
