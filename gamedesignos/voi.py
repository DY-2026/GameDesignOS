"""Decision-first information gate for creating and reviewing VOI assessments."""

from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from .errors import UsageError
from .io_utils import ensure_relative_safe, read_json, slugify, write_json
from .templates import information_assessment_skeleton
from .workspace import Workspace


_COST_WORDS = {"none": 0, "negligible": 0, "low": 1, "medium": 2, "high": 3, "critical": 5}


def _cost_rank(costs: Any) -> int:
    if not isinstance(costs, dict):
        return 99
    total = 0
    unknown = False
    for value in costs.values():
        text = str(value).lower()
        matched = next((score for word, score in _COST_WORDS.items() if word in text), None)
        if matched is None:
            unknown = True
        else:
            total += matched
    return total + (20 if unknown else 0)


def create_assessment(
    workspace: Workspace,
    *,
    decision_id: str,
    decision_question: str,
    options: list[str],
    current_default_action: str,
    owner: str,
    stakes: str,
    reversibility: str,
    boundary: str,
    candidate_information_actions: list[str],
    stop_when: list[str] | None,
    deadline: str | None = None,
    output: Path | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    if not re.fullmatch(r"DEC-[A-Z0-9-]{3,}", decision_id):
        raise UsageError("decision_id must match DEC-[A-Z0-9-]{3,}")
    if len(candidate_information_actions) > 3:
        raise UsageError("VOI gate accepts at most three candidate information actions per round")
    clean_options = [item.strip() for item in options if item.strip()]
    if len(clean_options) < 2:
        raise UsageError("At least two real options are required")
    if len(set(clean_options)) != len(clean_options):
        raise UsageError("Decision options must be distinct")
    options = clean_options
    if current_default_action not in options:
        raise UsageError("--default-action must exactly match one of the --option values")
    if boundary not in {"undefined", "far", "near", "locked"}:
        raise UsageError(f"Invalid decision boundary: {boundary}")
    if stakes not in {"low", "medium", "high", "critical"}:
        raise UsageError(f"Invalid stakes: {stakes}")
    if reversibility not in {"reversible", "costly_to_reverse", "irreversible"}:
        raise UsageError(f"Invalid reversibility: {reversibility}")

    asset_id = workspace.next_asset_id("VOI")
    assessment_id = asset_id.replace("ASSET-VOI-", "VOI-")
    data = information_assessment_skeleton(
        assessment_id=assessment_id,
        decision_id=decision_id,
        workspace_id=workspace.workspace_id,
        owner=owner,
        decision_question=decision_question,
        options=options,
        current_default_action=current_default_action,
        stakes=stakes,
        reversibility=reversibility,
        boundary=boundary,
        candidate_information_actions=candidate_information_actions,
        stop_when=stop_when,
        deadline=deadline,
    )

    decisions_dir = workspace.lifecycle_path("decisions_dir")
    if output is None:
        relative = decisions_dir.relative_to(workspace.root) / f"information-value-assessment-{slugify(decision_id.lower())}.json"
        output = workspace.root / relative
    else:
        output = output.expanduser()
        if not output.is_absolute():
            output = workspace.root / output
        output = output.resolve()
        try:
            relative = output.relative_to(workspace.root)
        except ValueError as exc:
            raise UsageError("VOI assessment output must remain inside the workspace") from exc
    ensure_relative_safe(workspace.root, relative.as_posix())
    if output.exists():
        raise UsageError(f"Refusing to overwrite existing assessment: {relative}")

    entry = {
        "asset_id": asset_id,
        "asset_type": "information-assessment",
        "title": f"VOI Assessment — {decision_id}",
        "path": relative.as_posix(),
        "format": "json",
        "created_by": "human-agent",
        "source_status": {"private": "private", "public-synthetic": "synthetic", "public-cleared": "cleared"}.get(workspace.visibility, "needs_review"),
        "review_status": "draft",
        "upstream_assets": [],
        "downstream_assets": [],
        "source_skill": "paranoia-ai-system-evolver",
        "notes": "Qualitative runtime scaffold. Edit signal-to-action mappings and costs, then review before treating a probe as selected.",
    }
    if not dry_run:
        write_json(output, data)
    workspace.register_asset(entry, dry_run=dry_run)
    return {
        "assessment": data,
        "asset": entry,
        "path": str(output),
        "dry_run": dry_run,
        "next_action": "Review signal-to-action mappings; the scaffold makes no numeric EV claim.",
    }


def review_assessment(path: Path, *, write: bool = False) -> dict[str, Any]:
    path = path.expanduser().resolve()
    data = read_json(path)
    if not isinstance(data, dict):
        raise UsageError("VOI assessment must be a JSON object")

    errors: list[str] = []
    warnings: list[str] = []
    recommendations: list[str] = []
    decision = data.get("decision")
    if not isinstance(decision, dict):
        errors.append("decision must be an object")
        decision = {}
    boundary = decision.get("boundary_status")
    options = decision.get("options") if isinstance(decision.get("options"), list) else []
    default_action = decision.get("current_default_action")
    if boundary not in {"undefined", "far", "near", "locked"}:
        errors.append("decision.boundary_status is missing or invalid")
    if not default_action:
        errors.append("decision.current_default_action is required")
    option_actions = {str(item.get("action")) for item in options if isinstance(item, dict) and item.get("action")}
    if len(option_actions) < 2:
        errors.append("decision.options must contain at least two distinct actions")
    if default_action and default_action not in option_actions:
        errors.append("decision.current_default_action must match one option action")

    uncertainty_items = data.get("uncertainty_map")
    if not isinstance(uncertainty_items, list):
        errors.append("uncertainty_map must be a list")
        uncertainty_items = []
    uncertainty_ids = {str(item.get("uncertainty_id")) for item in uncertainty_items if isinstance(item, dict) and item.get("uncertainty_id")}

    actions = data.get("candidate_information_actions")
    if not isinstance(actions, list):
        errors.append("candidate_information_actions must be a list")
        actions = []
    if len(actions) > 3:
        errors.append("candidate_information_actions exceeds the maximum of three")

    ranked: list[tuple[int, int, dict[str, Any], str]] = []
    for index, action in enumerate(actions):
        if not isinstance(action, dict):
            errors.append(f"candidate_information_actions[{index}] must be an object")
            continue
        action_id = str(action.get("action_id") or f"INFO-{index + 1:03d}")
        if action.get("target_uncertainty") not in uncertainty_ids:
            errors.append(f"{action_id}: target_uncertainty must reference uncertainty_map")
        signals = action.get("expected_signals")
        if not isinstance(signals, list) or not signals:
            errors.append(f"{action_id}: expected_signals must be a non-empty list")
            continue
        mapped_actions = {str(signal.get("action_if_seen")) for signal in signals if isinstance(signal, dict) and signal.get("action_if_seen")}
        invalid = sorted(mapped_actions - option_actions)
        if invalid:
            errors.append(f"{action_id}: signal actions are not decision options: {', '.join(invalid)}")
        could_change = action.get("could_change_action") is True and len(mapped_actions) >= 2 and not invalid
        if len(mapped_actions) < 2:
            conclusion = "skip"
            warnings.append(f"{action_id}: all plausible signals map to the same action; current decision VOI is approximately zero.")
        elif boundary == "undefined":
            conclusion = "ask_human"
        elif boundary == "locked":
            conclusion = "skip"
        elif boundary == "far":
            conclusion = "timebox_learning" if could_change else "skip"
        else:
            conclusion = "do" if could_change else "ask_human"
        action["conclusion"] = conclusion
        if conclusion == "do":
            ranked.append((_cost_rank(action.get("costs")), index, action, action_id))

    selected = None
    if ranked:
        ranked.sort(key=lambda item: (item[0], item[1]))
        _, _, action, action_id = ranked[0]
        selected = {
            "action_id": action_id,
            "why_smallest_high_value_probe": "It can map plausible signals to different actions and has the lowest stated cost among current do candidates.",
            "sample_or_evidence_gate": "TODO: define the minimum sample/evidence gate before execution.",
            "owner": str(decision.get("owner") or "TODO"),
        }
        data["selected_probe"] = selected
        recommendations.append(f"Select {action_id} only after replacing TODO cost and evidence-gate fields.")
    else:
        data["selected_probe"] = None
        if boundary == "undefined":
            recommendations.append("Define the Decision Object and real options before acquiring more information.")
        elif boundary == "locked":
            recommendations.append("Stop researching the locked choice; execute or start a retrospective.")
        elif not actions:
            recommendations.append("No information action is justified. Act with the current default or define one bounded probe.")
        else:
            recommendations.append("No positive-net-VOI probe is demonstrated. Use the fallback action in the stop rule.")

    stop_rule = data.get("stop_rule")
    if not isinstance(stop_rule, dict) or not stop_rule.get("stop_when"):
        errors.append("stop_rule.stop_when is required")
    if not isinstance(stop_rule, dict) or not stop_rule.get("fallback_action"):
        errors.append("stop_rule.fallback_action is required")
    if write and not errors:
        write_json(path, data)
    return {
        "ok": not errors,
        "path": str(path),
        "errors": errors,
        "warnings": warnings,
        "recommendations": recommendations,
        "selected_probe": selected,
        "written": bool(write and not errors),
        "assessment": data,
    }
