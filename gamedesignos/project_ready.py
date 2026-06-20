"""Project-ready decision graph, gate, and health primitives.

These helpers intentionally stay deterministic. They read local workspace
records, surface missing evidence, and never accept a commitment on behalf of a
human owner.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

from .constants import VALID_VISIBILITIES
from .errors import UsageError
from .io_utils import ensure_relative_safe, read_json, slugify, write_json
from .workspace import Workspace, find_repo_root


GATE_TYPES = {"voi", "evidence", "scope", "experiment", "commitment", "rollback"}
EDGE_TYPES = {
    "supports",
    "contradicts",
    "tests",
    "depends_on",
    "supersedes",
    "produces",
    "uses",
    "updates",
    "blocks",
}

WORKFLOWS: dict[str, dict[str, Any]] = {
    "idea-to-validation": {
        "workflow_id": "idea-to-validation",
        "version": "1.0.0",
        "title": "想法到验证",
        "nodes": [
            {"id": "decision_object", "type": "decision", "required_outputs": ["decision"]},
            {"id": "assumption_registry", "type": "assumption", "required_outputs": ["assumption"]},
            {"id": "voi_gate", "type": "gate", "gate_type": "voi"},
            {"id": "experiment_plan", "type": "experiment", "required_outputs": ["experiment_plan"]},
            {"id": "evidence_review", "type": "evidence", "required_outputs": ["evidence"]},
            {"id": "human_decision", "type": "gate", "gate_type": "commitment"},
        ],
        "edges": [
            {"from": "decision_object", "to": "assumption_registry"},
            {"from": "assumption_registry", "to": "voi_gate"},
            {"from": "voi_gate", "to": "experiment_plan"},
            {"from": "experiment_plan", "to": "evidence_review"},
            {"from": "evidence_review", "to": "human_decision"},
        ],
    }
}


def _relative_dir(workspace: Workspace, key: str, default: str) -> Path:
    value = str(workspace.assets_config.get(key) or default)
    return ensure_relative_safe(workspace.root, value)


def _json_files(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(path for path in directory.rglob("*.json") if path.is_file())


def _register_asset_if_possible(workspace: Workspace, entry: dict[str, Any]) -> None:
    index = workspace.load_asset_index()
    if any(item.get("asset_id") == entry["asset_id"] for item in index["assets"] if isinstance(item, dict)):
        return
    if any(item.get("path") == entry["path"] for item in index["assets"] if isinstance(item, dict)):
        return
    index["assets"].append(entry)
    write_json(workspace.asset_index_path, index)


def _next_id(existing: set[str], prefix: str) -> str:
    today = date.today().strftime("%Y%m%d")
    marker = f"{prefix}-{today}-"
    used = sorted(
        int(item[len(marker) :])
        for item in existing
        if item.startswith(marker) and item[len(marker) :].isdigit()
    )
    number = 1
    for candidate in used:
        if candidate == number:
            number += 1
    return f"{marker}{number:03d}"


def _relative_to_workspace(workspace: Workspace, path: Path) -> str:
    return path.resolve().relative_to(workspace.root).as_posix()


def _load_json_objects(paths: list[Path]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for path in paths:
        data = read_json(path)
        if isinstance(data, dict):
            data = dict(data)
            data.setdefault("_path", str(path))
            items.append(data)
    return items


def _normalize_options(value: Any) -> list[dict[str, str]]:
    if not isinstance(value, list):
        return []
    options: list[dict[str, str]] = []
    for index, item in enumerate(value, start=1):
        if isinstance(item, dict):
            action = item.get("action") or item.get("label") or item.get("name")
            option_id = item.get("option_id") or f"OPT-{index:03d}"
        else:
            action = str(item)
            option_id = f"OPT-{index:03d}"
        if action:
            options.append({"option_id": str(option_id), "action": str(action)})
    return options


def _decision_id(item: dict[str, Any]) -> str | None:
    value = item.get("decision_id") or item.get("id")
    return str(value) if value else None


def _assumption_id(item: dict[str, Any]) -> str | None:
    value = item.get("assumption_id") or item.get("id")
    return str(value) if value else None


def _evidence_id(item: dict[str, Any]) -> str | None:
    value = item.get("evidence_id") or item.get("id")
    return str(value) if value else None


def _experiment_id(item: dict[str, Any]) -> str | None:
    value = item.get("experiment_id") or item.get("id")
    return str(value) if value else None


def _learning_id(item: dict[str, Any]) -> str | None:
    value = item.get("learning_id") or item.get("id")
    return str(value) if value else None


def _normalize_decision(item: dict[str, Any]) -> dict[str, Any] | None:
    decision_id = _decision_id(item)
    if not decision_id:
        return None
    options = _normalize_options(item.get("options") or item.get("options_considered"))
    return {
        "decision_id": decision_id,
        "title": item.get("title") or item.get("decision") or item.get("decision_question") or decision_id,
        "decision_question": item.get("decision_question") or item.get("decision") or "",
        "owner": item.get("owner") or "TODO",
        "status": item.get("status") or "proposed",
        "decision_type": item.get("decision_type") or "unknown",
        "boundary_status": item.get("boundary_status") or item.get("decision_boundary") or "undefined",
        "stakes": item.get("stakes") or "medium",
        "reversibility": item.get("reversibility") or "reversible",
        "current_default_action": item.get("current_default_action") or "",
        "options": options,
        "evidence_refs": list(item.get("evidence_refs") or []),
        "assumption_refs": list(item.get("assumption_refs") or []),
        "experiment_refs": list(item.get("experiment_refs") or []),
        "gate_refs": list(item.get("gate_refs") or item.get("voi_assessment_refs") or []),
        "decision_result": item.get("decision_result"),
        "rollback_trigger": item.get("rollback_trigger") or "",
        "_path": item.get("_path"),
    }


def load_project_ready_state(workspace: Workspace) -> dict[str, Any]:
    """Load v0.9 and v1.0-style records into one conservative state map."""

    decisions: dict[str, dict[str, Any]] = {}
    try:
        for item in workspace.load_decision_log().get("decisions", []):
            if isinstance(item, dict):
                normalized = _normalize_decision(item)
                if normalized:
                    decisions[normalized["decision_id"]] = normalized
    except UsageError:
        raise

    decision_paths = [
        *_json_files(_relative_dir(workspace, "decisions_dir", "06-decisions")),
        *_json_files(workspace.root / "01-decisions"),
    ]
    for item in _load_json_objects(decision_paths):
        if item.get("decisions"):
            continue
        normalized = _normalize_decision(item)
        if normalized:
            decisions[normalized["decision_id"]] = {**decisions.get(normalized["decision_id"], {}), **normalized}

    assumption_items: list[dict[str, Any]] = []
    for item in _load_json_objects(_json_files(workspace.root / "02-assumptions")):
        if isinstance(item.get("assumptions"), list):
            assumption_items.extend(
                dict(child, _path=item.get("_path")) for child in item["assumptions"] if isinstance(child, dict)
            )
        elif _assumption_id(item):
            assumption_items.append(item)
    assumptions = {_assumption_id(item): item for item in assumption_items if _assumption_id(item)}

    evidence_items: list[dict[str, Any]] = []
    for directory in (_relative_dir(workspace, "evidence_dir", "02-evidence"), workspace.root / "03-evidence"):
        for item in _load_json_objects(_json_files(directory)):
            if isinstance(item.get("evidence"), list):
                evidence_items.extend(
                    dict(child, _path=item.get("_path")) for child in item["evidence"] if isinstance(child, dict)
                )
            elif isinstance(item.get("evidence_items"), list):
                evidence_items.extend(
                    dict(child, _path=item.get("_path")) for child in item["evidence_items"] if isinstance(child, dict)
                )
            elif _evidence_id(item):
                evidence_items.append(item)
    evidence = {_evidence_id(item): item for item in evidence_items if _evidence_id(item)}

    experiment_items: list[dict[str, Any]] = []
    for directory in (_relative_dir(workspace, "experiments_dir", "05-experiments"), workspace.root / "04-experiments"):
        for item in _load_json_objects(_json_files(directory)):
            if _experiment_id(item) and (
                item.get("target_decision") or item.get("target_assumptions") or item.get("hypothesis")
            ):
                experiment_items.append(item)
    experiments = {_experiment_id(item): item for item in experiment_items if _experiment_id(item)}

    learning_items: list[dict[str, Any]] = []
    for directory in (workspace.root / "07-learning", _relative_dir(workspace, "retrospectives_dir", "07-retrospectives")):
        for item in _load_json_objects(_json_files(directory)):
            if _learning_id(item):
                learning_items.append(item)
    learning = {_learning_id(item): item for item in learning_items if _learning_id(item)}

    return {
        "decisions": decisions,
        "assumptions": assumptions,
        "evidence": evidence,
        "experiments": experiments,
        "learning": learning,
    }


def create_decision(
    workspace: Workspace,
    *,
    title: str,
    question: str,
    options: list[str],
    default_action: str,
    owner: str,
    decision_type: str,
    boundary: str,
    stakes: str,
    reversibility: str,
    rollback_trigger: str,
) -> dict[str, Any]:
    clean_options = [item.strip() for item in options if item.strip()]
    if len(clean_options) < 2:
        raise UsageError("decision new requires at least two --option values")
    if default_action not in clean_options:
        raise UsageError("--default-action must exactly match one --option")
    state = load_project_ready_state(workspace)
    decision_id = _next_id(set(state["decisions"]), "DEC")
    data = {
        "schema_version": "1.0.0",
        "decision_id": decision_id,
        "title": title.strip() or question.strip(),
        "decision_question": question.strip(),
        "owner": owner.strip() or "designer",
        "status": "proposed",
        "decision_type": decision_type,
        "boundary_status": boundary,
        "stakes": stakes,
        "reversibility": reversibility,
        "current_default_action": default_action,
        "options": [
            {
                "option_id": f"OPT-{index:03d}",
                "action": action,
                "expected_benefit": "",
                "main_risk": "",
            }
            for index, action in enumerate(clean_options, start=1)
        ],
        "evidence_refs": [],
        "assumption_refs": [],
        "experiment_refs": [],
        "gate_refs": [],
        "decision_result": None,
        "rollback_trigger": rollback_trigger,
    }
    directory = workspace.lifecycle_path("decisions_dir")
    path = directory / f"{decision_id}.json"
    write_json(path, data)
    _register_asset_if_possible(
        workspace,
        {
            "asset_id": workspace.next_asset_id("DECISION"),
            "asset_type": "decision",
            "title": data["title"],
            "path": _relative_to_workspace(workspace, path),
            "format": "json",
            "created_by": "human-agent",
            "source_status": {"private": "private", "public-synthetic": "synthetic", "public-cleared": "cleared"}.get(workspace.visibility, "needs_review"),
            "review_status": "draft",
            "upstream_assets": [],
            "downstream_assets": [],
            "notes": "v1 Decision Object.",
        },
    )
    return {"decision": data, "path": str(path)}


def _record_path(record: dict[str, Any]) -> Path | None:
    value = record.get("_path")
    return Path(str(value)) if value else None


def list_decisions(workspace: Workspace) -> list[dict[str, Any]]:
    return sorted(load_project_ready_state(workspace)["decisions"].values(), key=lambda item: item["decision_id"])


def inspect_decision(workspace: Workspace, decision_id: str) -> dict[str, Any]:
    decision = load_project_ready_state(workspace)["decisions"].get(decision_id)
    if not decision:
        raise UsageError(f"Decision not found: {decision_id}")
    return decision


def update_decision_status(
    workspace: Workspace,
    decision_id: str,
    *,
    status: str,
    by: str,
    reason: str,
    supersedes: str | None = None,
) -> dict[str, Any]:
    if status == "accepted":
        gate = run_gate(workspace, "commitment", decision_id)
        if gate["status"] == "block":
            raise UsageError("Commitment gate blocked acceptance: " + gate["reason"])
    state = load_project_ready_state(workspace)
    decision = state["decisions"].get(decision_id)
    if not decision:
        raise UsageError(f"Decision not found: {decision_id}")
    path = _record_path(decision)
    if not path or not path.exists():
        raise UsageError(f"Decision is not stored as an editable v1 file: {decision_id}")
    data = read_json(path)
    data["status"] = status
    data["decision_result"] = {
        "status": status,
        "by": by,
        "reason": reason,
        "date": date.today().isoformat(),
    }
    if status == "accepted":
        data["accepted_by"] = by
        data["accepted_reason"] = reason
    if supersedes:
        data["supersedes"] = supersedes
    write_json(path, data)
    return {"decision": data, "path": str(path)}


def create_assumption(
    workspace: Workspace,
    *,
    decision_id: str,
    statement: str,
    assumption_type: str,
    risk_level: str,
    confidence: str,
    test_method: str,
    kill_condition: str,
) -> dict[str, Any]:
    if decision_id not in load_project_ready_state(workspace)["decisions"]:
        raise UsageError(f"Decision not found: {decision_id}")
    state = load_project_ready_state(workspace)
    assumption_id = _next_id(set(state["assumptions"]), "ASM")
    data = {
        "schema_version": "1.0.0",
        "assumption_id": assumption_id,
        "statement": statement,
        "type": assumption_type,
        "risk_level": risk_level,
        "confidence": confidence,
        "linked_decisions": [decision_id],
        "test_method": test_method,
        "validation_status": "untested",
        "kill_condition": kill_condition,
    }
    directory = workspace.lifecycle_path("assumptions_dir")
    path = directory / f"{assumption_id}.json"
    write_json(path, data)
    decision = inspect_decision(workspace, decision_id)
    decision_path = _record_path(decision)
    if decision_path and decision_path.exists():
        decision_data = read_json(decision_path)
        refs = list(dict.fromkeys([*decision_data.get("assumption_refs", []), assumption_id]))
        decision_data["assumption_refs"] = refs
        write_json(decision_path, decision_data)
    _register_asset_if_possible(
        workspace,
        {
            "asset_id": workspace.next_asset_id("ASM"),
            "asset_type": "assumption",
            "title": statement[:80],
            "path": _relative_to_workspace(workspace, path),
            "format": "json",
            "created_by": "human-agent",
            "source_status": "private" if workspace.visibility == "private" else "synthetic",
            "review_status": "draft",
            "upstream_assets": [],
            "downstream_assets": [],
            "notes": "v1 Assumption.",
        },
    )
    return {"assumption": data, "path": str(path)}


def list_assumptions(workspace: Workspace) -> list[dict[str, Any]]:
    return sorted(load_project_ready_state(workspace)["assumptions"].values(), key=lambda item: _assumption_id(item) or "")


def validate_assumption(workspace: Workspace, assumption_id: str, *, status: str, reason: str) -> dict[str, Any]:
    assumption = load_project_ready_state(workspace)["assumptions"].get(assumption_id)
    if not assumption:
        raise UsageError(f"Assumption not found: {assumption_id}")
    path = _record_path(assumption)
    if not path or not path.exists():
        raise UsageError(f"Assumption is not stored as an editable v1 file: {assumption_id}")
    data = read_json(path)
    data["validation_status"] = status
    data["validation_note"] = reason
    data["updated_at"] = date.today().isoformat()
    write_json(path, data)
    return {"assumption": data, "path": str(path)}


def add_evidence(
    workspace: Workspace,
    *,
    decision_id: str,
    summary: str,
    source_type: str,
    source_status: str,
    confidence: str,
    decision_impact: str,
    unsupported_claims: list[str],
) -> dict[str, Any]:
    if decision_id not in load_project_ready_state(workspace)["decisions"]:
        raise UsageError(f"Decision not found: {decision_id}")
    state = load_project_ready_state(workspace)
    evidence_id = _next_id(set(state["evidence"]), "EVD")
    data = {
        "schema_version": "1.0.0",
        "evidence_id": evidence_id,
        "source_type": source_type,
        "source_status": source_status,
        "summary": summary,
        "confidence": confidence,
        "decision_impact": decision_impact,
        "used_by_decisions": [decision_id],
        "used_by_assumptions": [],
        "unsupported_claims": unsupported_claims or ["没有声明可外推范围。"],
    }
    directory = workspace.lifecycle_path("evidence_dir")
    path = directory / f"{evidence_id}.json"
    write_json(path, data)
    decision = inspect_decision(workspace, decision_id)
    decision_path = _record_path(decision)
    if decision_path and decision_path.exists():
        decision_data = read_json(decision_path)
        refs = list(dict.fromkeys([*decision_data.get("evidence_refs", []), evidence_id]))
        decision_data["evidence_refs"] = refs
        write_json(decision_path, decision_data)
    _register_asset_if_possible(
        workspace,
        {
            "asset_id": workspace.next_asset_id("EVD"),
            "asset_type": "evidence",
            "title": summary[:80],
            "path": _relative_to_workspace(workspace, path),
            "format": "json",
            "created_by": "human-agent",
            "source_status": source_status,
            "review_status": "draft",
            "upstream_assets": [],
            "downstream_assets": [],
            "notes": "v1 Evidence.",
        },
    )
    return {"evidence": data, "path": str(path)}


def list_evidence(workspace: Workspace) -> list[dict[str, Any]]:
    return sorted(load_project_ready_state(workspace)["evidence"].values(), key=lambda item: _evidence_id(item) or "")


def inspect_evidence(workspace: Workspace, evidence_id: str) -> dict[str, Any]:
    evidence = load_project_ready_state(workspace)["evidence"].get(evidence_id)
    if not evidence:
        raise UsageError(f"Evidence not found: {evidence_id}")
    return evidence


def plan_experiment(
    workspace: Workspace,
    *,
    decision_id: str,
    assumption_ids: list[str],
    title: str,
    hypothesis: str,
    method: str,
    success_criteria: list[str],
    failure_criteria: list[str],
    sample_size: int | None,
) -> dict[str, Any]:
    state = load_project_ready_state(workspace)
    if decision_id not in state["decisions"]:
        raise UsageError(f"Decision not found: {decision_id}")
    missing = [item for item in assumption_ids if item not in state["assumptions"]]
    if missing:
        raise UsageError("Assumption not found: " + ", ".join(missing))
    experiment_id = _next_id(set(state["experiments"]), "EXP")
    data = {
        "schema_version": "1.0.0",
        "experiment_id": experiment_id,
        "title": title,
        "target_decision": decision_id,
        "target_assumptions": assumption_ids,
        "hypothesis": hypothesis,
        "method": method,
        "sample_size": sample_size,
        "success_criteria": success_criteria,
        "failure_criteria": failure_criteria,
        "result_status": "planned",
    }
    directory = workspace.lifecycle_path("experiments_dir") / experiment_id
    path = directory / "experiment-plan.json"
    write_json(path, data)
    decision = inspect_decision(workspace, decision_id)
    decision_path = _record_path(decision)
    if decision_path and decision_path.exists():
        decision_data = read_json(decision_path)
        refs = list(dict.fromkeys([*decision_data.get("experiment_refs", []), experiment_id]))
        decision_data["experiment_refs"] = refs
        write_json(decision_path, decision_data)
    _register_asset_if_possible(
        workspace,
        {
            "asset_id": workspace.next_asset_id("EXP"),
            "asset_type": "experiment",
            "title": title,
            "path": _relative_to_workspace(workspace, path),
            "format": "json",
            "created_by": "human-agent",
            "source_status": "private" if workspace.visibility == "private" else "synthetic",
            "review_status": "draft",
            "upstream_assets": [],
            "downstream_assets": [],
            "notes": "v1 Experiment Plan.",
        },
    )
    return {"experiment": data, "path": str(path)}


def add_experiment_result(
    workspace: Workspace,
    experiment_id: str,
    *,
    status: str,
    observations: list[str],
    evidence_refs: list[str],
    decision_delta: str,
) -> dict[str, Any]:
    experiment = load_project_ready_state(workspace)["experiments"].get(experiment_id)
    if not experiment:
        raise UsageError(f"Experiment not found: {experiment_id}")
    plan_path = _record_path(experiment)
    if not plan_path:
        raise UsageError(f"Experiment is not stored as an editable v1 file: {experiment_id}")
    data = {
        "schema_version": "1.0.0",
        "experiment_id": experiment_id,
        "status": status,
        "observations": observations,
        "evidence_refs": evidence_refs,
        "decision_delta": decision_delta,
        "review_status": "draft",
    }
    result_path = plan_path.parent / "experiment-result.json"
    write_json(result_path, data)
    plan = read_json(plan_path)
    plan["result_status"] = "completed"
    write_json(plan_path, plan)
    return {"result": data, "path": str(result_path)}


def review_experiment(workspace: Workspace, experiment_id: str, *, by: str, summary: str) -> dict[str, Any]:
    experiment = load_project_ready_state(workspace)["experiments"].get(experiment_id)
    if not experiment:
        raise UsageError(f"Experiment not found: {experiment_id}")
    plan_path = _record_path(experiment)
    if not plan_path:
        raise UsageError(f"Experiment is not stored as an editable v1 file: {experiment_id}")
    result_path = plan_path.parent / "experiment-result.json"
    if not result_path.exists():
        raise UsageError(f"Experiment result missing: {experiment_id}")
    result = read_json(result_path)
    result["review_status"] = "reviewed"
    result["reviewed_by"] = by
    result["review_summary"] = summary
    write_json(result_path, result)
    plan = read_json(plan_path)
    plan["result_status"] = "reviewed"
    plan["review_status"] = "reviewed"
    write_json(plan_path, plan)
    return {"result": result, "path": str(result_path)}


def list_workflows() -> list[dict[str, Any]]:
    return [
        {
            "workflow_id": item["workflow_id"],
            "version": item["version"],
            "title": item["title"],
            "nodes": [node["id"] for node in item["nodes"]],
        }
        for item in WORKFLOWS.values()
    ]


def _workflow_dir(workspace: Workspace) -> Path:
    path = workspace.root / ".gamedesignos" / "workflow-runs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _workflow_path(workspace: Workspace, run_id: str) -> Path:
    return _workflow_dir(workspace) / f"{run_id}.json"


def start_workflow(workspace: Workspace, workflow_id: str) -> dict[str, Any]:
    if workflow_id not in WORKFLOWS:
        raise UsageError(f"Unknown workflow: {workflow_id}")
    workflow = WORKFLOWS[workflow_id]
    existing = {path.stem.upper() for path in _workflow_dir(workspace).glob("WRUN-*.json")}
    run_id = _next_id(existing, "WRUN")
    nodes = []
    for index, node in enumerate(workflow["nodes"]):
        nodes.append(
            {
                "id": node["id"],
                "type": node["type"],
                "status": "ready" if index == 0 else "pending",
                **({"gate_type": node["gate_type"]} if node.get("gate_type") else {}),
                **({"required_outputs": node["required_outputs"]} if node.get("required_outputs") else {}),
            }
        )
    data = {
        "schema_version": "1.0.0",
        "workflow_id": workflow_id,
        "version": workflow["version"],
        "run_id": run_id,
        "status": "running",
        "current_node": nodes[0]["id"],
        "nodes": nodes,
        "edges": workflow["edges"],
    }
    path = _workflow_path(workspace, run_id)
    write_json(path, data)
    _register_asset_if_possible(
        workspace,
        {
            "asset_id": workspace.next_asset_id("WRUN"),
            "asset_type": "workflow-run",
            "title": f"{workflow['title']} {run_id}",
            "path": _relative_to_workspace(workspace, path),
            "format": "json",
            "created_by": "human-agent",
            "source_status": "private" if workspace.visibility == "private" else "synthetic",
            "review_status": "draft",
            "upstream_assets": [],
            "downstream_assets": [],
            "notes": "v1 Workflow Run.",
        },
    )
    return {"workflow_run": data, "path": str(path)}


def workflow_status(workspace: Workspace, run_id: str) -> dict[str, Any]:
    path = _workflow_path(workspace, run_id)
    if not path.exists():
        raise UsageError(f"Workflow run not found: {run_id}")
    return read_json(path)


def _node_recommendation(workspace: Workspace, node_id: str) -> dict[str, Any]:
    state = load_project_ready_state(workspace)
    if node_id == "decision_object":
        if state["decisions"]:
            return {"status": "done", "reason": "已经存在 Decision Object。"}
        return {"status": "ready", "reason": "先创建 Decision Object。", "hint": "gamedesignos decision new ..."}
    if node_id == "assumption_registry":
        if state["assumptions"]:
            return {"status": "done", "reason": "已经存在 Assumption。"}
        return {"status": "ready", "reason": "登记最高风险假设。", "hint": "gamedesignos assumption new ..."}
    if node_id == "voi_gate":
        near = [
            decision_id
            for decision_id, item in state["decisions"].items()
            if item.get("boundary_status") == "near"
        ]
        if not near:
            return {"status": "done", "reason": "当前没有 near-boundary decision。"}
        gate = run_gate(workspace, "voi", near[0])
        return {
            "status": "done" if gate["status"] in {"pass", "warn"} else "blocked",
            "reason": gate["reason"],
            "hint": f"gamedesignos gate run voi {near[0]}",
        }
    if node_id == "experiment_plan":
        if state["experiments"]:
            return {"status": "done", "reason": "已经存在 Experiment Plan。"}
        return {"status": "ready", "reason": "为最高风险假设创建实验。", "hint": "gamedesignos experiment plan ..."}
    if node_id == "evidence_review":
        if state["evidence"]:
            return {"status": "done", "reason": "已经存在 Evidence。"}
        return {"status": "ready", "reason": "记录实验或样本证据。", "hint": "gamedesignos evidence add ..."}
    if node_id == "human_decision":
        accepted = [item for item in state["decisions"].values() if item.get("status") == "accepted"]
        if accepted:
            return {"status": "done", "reason": "已有 accepted decision。"}
        if state["decisions"]:
            decision_id = sorted(state["decisions"])[0]
            gate = run_gate(workspace, "commitment", decision_id)
            return {
                "status": "ready" if gate["status"] == "ask_human" else "blocked",
                "reason": gate["reason"],
                "hint": f"gamedesignos decision accept {decision_id} --by OWNER --reason REASON",
            }
        return {"status": "blocked", "reason": "缺少 Decision Object。"}
    return {"status": "blocked", "reason": f"未知节点: {node_id}"}


def workflow_next(workspace: Workspace, run_id: str) -> dict[str, Any]:
    data = workflow_status(workspace, run_id)
    for node in data.get("nodes", []):
        if node.get("status") in {"done", "skipped"}:
            continue
        recommendation = _node_recommendation(workspace, node["id"])
        node["status"] = recommendation["status"]
        if recommendation["status"] != "done":
            data["current_node"] = node["id"]
            data["status"] = "blocked" if recommendation["status"] == "blocked" else "running"
            write_json(_workflow_path(workspace, run_id), data)
            return {"run": data, "node": node, "next": recommendation}
    data["status"] = "completed"
    data["current_node"] = None
    write_json(_workflow_path(workspace, run_id), data)
    return {"run": data, "node": None, "next": {"status": "done", "reason": "工作流已完成。"}}


def validate_workflow_run(workspace: Workspace, run_id: str) -> dict[str, Any]:
    data = workflow_status(workspace, run_id)
    errors: list[str] = []
    node_ids = {node.get("id") for node in data.get("nodes", []) if isinstance(node, dict)}
    for edge in data.get("edges", []):
        if edge.get("from") not in node_ids or edge.get("to") not in node_ids:
            errors.append(f"edge references unknown node: {edge}")
    if data.get("workflow_id") not in WORKFLOWS:
        errors.append("workflow_id is not registered")
    return {"ok": not errors, "errors": errors, "workflow_run": data}


def _gate_result(
    *,
    gate_type: str,
    target: str,
    status: str,
    reason: str,
    required_actions: list[str] | None = None,
    blocked_actions: list[str] | None = None,
    human_gate_required: bool = False,
) -> dict[str, Any]:
    today = date.today().strftime("%Y%m%d")
    slug = slugify(f"{gate_type}-{target}", fallback="gate")
    return {
        "schema_version": "1.0.0",
        "gate_id": f"GATE-{today}-{slug[:40].upper()}",
        "gate_type": gate_type,
        "target": target,
        "status": status,
        "reason": reason,
        "required_actions": required_actions or [],
        "blocked_actions": blocked_actions or [],
        "reviewer": "gamedesignos-runtime",
        "human_gate_required": human_gate_required,
    }


def _linked_assumptions(state: dict[str, Any], decision_id: str, decision: dict[str, Any]) -> list[dict[str, Any]]:
    refs = set(str(item) for item in decision.get("assumption_refs", []))
    linked = []
    for assumption_id, item in state["assumptions"].items():
        linked_decisions = set(str(ref) for ref in item.get("linked_decisions", []))
        if assumption_id in refs or decision_id in linked_decisions:
            linked.append(item)
    return linked


def _linked_experiments(state: dict[str, Any], decision_id: str, decision: dict[str, Any]) -> list[dict[str, Any]]:
    refs = set(str(item) for item in decision.get("experiment_refs", []))
    linked = []
    for experiment_id, item in state["experiments"].items():
        target = item.get("target_decision") or item.get("decision_id")
        if experiment_id in refs or target == decision_id:
            linked.append(item)
    return linked


def run_gate(workspace: Workspace, gate_type: str, target: str, *, write: bool = False) -> dict[str, Any]:
    """Run a deterministic Project-Ready gate for a local workspace target."""

    if gate_type not in GATE_TYPES:
        raise UsageError(f"Unknown gate type: {gate_type}")
    state = load_project_ready_state(workspace)
    decision = state["decisions"].get(target)

    if gate_type == "voi":
        if not decision:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="No Decision Object exists, so information gathering cannot be action-sensitive.",
                required_actions=["Create a Decision Object with options and current_default_action."],
                blocked_actions=["research", "trend_scan", "large_context_collection"],
            )
        elif decision["boundary_status"] == "locked":
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="The decision is locked; more research is not allowed unless the owner reopens it.",
                required_actions=["Execute the current default action or start a retrospective."],
                blocked_actions=["research"],
            )
        elif not decision["current_default_action"] or len(decision["options"]) < 2:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="VOI requires at least two real options and a current default action.",
                required_actions=["Fill options and current_default_action before collecting more information."],
            )
        elif decision["boundary_status"] == "near":
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="pass",
                reason="The decision is near-boundary, so a small probe can be justified if its signals map to different actions.",
                required_actions=["Create or review a qualitative VOI assessment before running the probe."],
            )
        else:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="warn",
                reason="The decision is not near-boundary; information should be timeboxed or skipped unless it can change action.",
                required_actions=["Record the stop rule and fallback action."],
            )

    elif gate_type == "commitment":
        if not decision:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="No Decision Object exists, so no commitment can be accepted.",
                required_actions=["Create a Decision Object first."],
            )
        else:
            linked_assumptions = _linked_assumptions(state, target, decision)
            untested_high = [
                item.get("assumption_id") or item.get("id")
                for item in linked_assumptions
                if item.get("risk_level") in {"high", "critical"}
                and item.get("validation_status") not in {"tested", "validated", "invalidated"}
            ]
            linked_experiments = _linked_experiments(state, target, decision)
            unreviewed_experiments = [
                item.get("experiment_id") or item.get("id")
                for item in linked_experiments
                if item.get("result_status") not in {"reviewed", "accepted", "failed", "inconclusive"}
                and item.get("review_status") not in {"reviewed", "accepted"}
            ]
            high_impact = decision["stakes"] in {"high", "critical"} or decision["reversibility"] in {
                "costly_to_reverse",
                "irreversible",
            }
            if high_impact and not decision["rollback_trigger"]:
                result = _gate_result(
                    gate_type=gate_type,
                    target=target,
                    status="block",
                    reason="High-impact commitments need an explicit rollback trigger.",
                    required_actions=["Add rollback_trigger before acceptance."],
                    blocked_actions=["decision_accept", "scope_lock", "publish_commitment"],
                    human_gate_required=True,
                )
            elif untested_high:
                result = _gate_result(
                    gate_type=gate_type,
                    target=target,
                    status="block",
                    reason="High-risk assumptions are still untested.",
                    required_actions=[f"Test or explicitly waive assumptions: {', '.join(map(str, untested_high))}"],
                    blocked_actions=["decision_accept"],
                    human_gate_required=True,
                )
            elif unreviewed_experiments:
                result = _gate_result(
                    gate_type=gate_type,
                    target=target,
                    status="block",
                    reason="Linked experiments have no reviewed result.",
                    required_actions=[f"Review experiments: {', '.join(map(str, unreviewed_experiments))}"],
                    blocked_actions=["decision_accept"],
                    human_gate_required=True,
                )
            else:
                result = _gate_result(
                    gate_type=gate_type,
                    target=target,
                    status="ask_human",
                    reason="Runtime checks passed, but accepting a commitment remains a Human Gate.",
                    required_actions=["Run decision accept with --by and --reason, or record rejection/supersession."],
                    human_gate_required=True,
                )

    elif gate_type == "rollback":
        if not decision:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="No Decision Object exists.",
                required_actions=["Create a Decision Object first."],
            )
        elif decision["stakes"] in {"high", "critical"} and not decision["rollback_trigger"]:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="High-stakes decisions need an observable rollback trigger.",
                required_actions=["Add rollback_trigger with a concrete condition."],
                blocked_actions=["commitment"],
                human_gate_required=True,
            )
        else:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="pass",
                reason="Rollback boundary is explicit enough for the current risk level.",
            )

    elif gate_type == "evidence":
        if not decision:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="Evidence cannot be evaluated without a target Decision Object.",
                required_actions=["Create or specify a Decision Object."],
            )
        elif not decision["evidence_refs"]:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="warn",
                reason="The decision has no evidence references; strong claims must stay marked as assumptions.",
                required_actions=["Register evidence or list unsupported claims before proposal work."],
            )
        else:
            unsupported = [
                ref
                for ref in decision["evidence_refs"]
                if (state["evidence"].get(ref) or {}).get("unsupported_claims")
            ]
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="warn" if unsupported else "pass",
                reason=(
                    "Some referenced evidence has explicit unsupported claims."
                    if unsupported
                    else "Referenced evidence has a recorded boundary."
                ),
                required_actions=[f"Do not use {', '.join(unsupported)} outside its support boundary."]
                if unsupported
                else [],
            )

    elif gate_type == "experiment":
        if target in state["experiments"]:
            experiment = state["experiments"][target]
            if not experiment.get("target_decision") and not experiment.get("target_assumptions"):
                result = _gate_result(
                    gate_type=gate_type,
                    target=target,
                    status="block",
                    reason="Experiment has no target decision or target assumptions.",
                    required_actions=["Bind the experiment to a decision or assumption before running it."],
                )
            elif not experiment.get("success_criteria") or not experiment.get("failure_criteria"):
                result = _gate_result(
                    gate_type=gate_type,
                    target=target,
                    status="block",
                    reason="Experiment lacks success or failure criteria.",
                    required_actions=["Add success_criteria and failure_criteria."],
                )
            else:
                result = _gate_result(
                    gate_type=gate_type,
                    target=target,
                    status="pass",
                    reason="Experiment can produce decision-relevant evidence if executed as written.",
                )
        else:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="Experiment record not found.",
                required_actions=["Create an experiment plan before running this gate."],
            )

    else:
        if not decision:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="block",
                reason="Scope cannot be evaluated without a Decision Object.",
                required_actions=["Create or specify a Decision Object."],
            )
        elif decision["stakes"] == "critical" and decision["reversibility"] == "irreversible":
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="ask_human",
                reason="Critical irreversible scope requires explicit owner review.",
                human_gate_required=True,
            )
        else:
            result = _gate_result(
                gate_type=gate_type,
                target=target,
                status="pass",
                reason="No deterministic scope blocker was found in the available record.",
            )

    if write:
        out_dir = workspace.root / ".gamedesignos" / "gate-results"
        out_dir.mkdir(parents=True, exist_ok=True)
        write_json(out_dir / f"{result['gate_id'].lower()}.json", result)
    return result


def _first_record(items: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    if not items:
        return None
    return items[sorted(items)[0]]


def _link_decision_reference(workspace: Workspace, decision_id: str, field: str, ref: str) -> None:
    decision = inspect_decision(workspace, decision_id)
    path = _record_path(decision)
    if not path or not path.exists():
        return
    data = read_json(path)
    refs = list(dict.fromkeys([*data.get(field, []), ref]))
    data[field] = refs
    write_json(path, data)


def _existing_experiment_for(
    state: dict[str, Any],
    *,
    decision_id: str,
    assumption_id: str | None,
) -> dict[str, Any] | None:
    for experiment_id in sorted(state["experiments"]):
        item = state["experiments"][experiment_id]
        target_decision = item.get("target_decision") or item.get("decision_id")
        target_assumptions = set(str(ref) for ref in item.get("target_assumptions", []))
        if target_decision == decision_id or (assumption_id and assumption_id in target_assumptions):
            return item
    return None


def _existing_workflow_run(workspace: Workspace, workflow_id: str) -> dict[str, Any] | None:
    for path in sorted(_workflow_dir(workspace).glob("WRUN-*.json")):
        data = read_json(path)
        if data.get("workflow_id") == workflow_id:
            return data
    return None


def _default_start_destination(project_name: str) -> Path:
    current = Path.cwd().resolve()
    repo = find_repo_root(current)
    base = current
    if repo:
        try:
            current.relative_to(repo.resolve())
            base = repo.resolve().parent
        except ValueError:
            base = current
    slug = slugify(project_name, fallback="game")
    if not slug.endswith("-designos"):
        slug = f"{slug}-designos"
    return base / slug


def start_project(
    *,
    project_name: str,
    destination: Path | None = None,
    owner: str = "designer",
    visibility: str = "private",
    question: str = "下一轮最应该验证什么，才能决定是否继续投入？",
    options: list[str] | None = None,
    default_action: str | None = None,
    assumption: str = "玩家能在三分钟内理解并感受到核心玩法的乐趣。",
    test_method: str = "三分钟核心循环原型 + 3-5 人观察。",
    success_criteria: list[str] | None = None,
    failure_criteria: list[str] | None = None,
    rollback_trigger: str = "一周内无法形成可试玩的三分钟核心循环。",
    sample_size: int = 5,
) -> dict[str, Any]:
    """Create or resume the smallest useful Project-Ready workspace path."""

    if visibility not in VALID_VISIBILITIES:
        raise UsageError(f"Invalid visibility: {visibility}")
    project_name = project_name.strip()
    if not project_name:
        raise UsageError("project_name must not be empty")

    target = (destination or _default_start_destination(project_name)).expanduser().resolve()
    created_workspace = False
    if (target / "game.designos.yaml").is_file():
        workspace = Workspace.open(target)
    else:
        from .workspace_init import init_workspace

        init_workspace(
            project_name=project_name,
            destination=target,
            codename=None,
            visibility=visibility,
            owner=owner,
        )
        workspace = Workspace.open(target)
        created_workspace = True

    clean_options = [item.strip() for item in (options or []) if item.strip()]
    if not clean_options:
        clean_options = ["做一个三分钟核心玩法原型", "先做资料和概念整理"]
    clean_default = (default_action or clean_options[0]).strip()
    if clean_default not in clean_options:
        clean_options.insert(0, clean_default)
    if len(clean_options) == 1:
        clean_options.append("暂停投入，重新定义方向")

    state = load_project_ready_state(workspace)
    existing_decision = _first_record(state["decisions"])
    if existing_decision:
        decision = existing_decision
        decision_created = False
        decision_path = decision.get("_path")
    else:
        decision_result = create_decision(
            workspace,
            title=f"{project_name}：第一轮验证方向",
            question=question,
            options=clean_options,
            default_action=clean_default,
            owner=owner,
            decision_type="prototype_direction",
            boundary="near",
            stakes="medium",
            reversibility="reversible",
            rollback_trigger=rollback_trigger,
        )
        decision = decision_result["decision"]
        decision_created = True
        decision_path = decision_result["path"]

    decision_id = str(decision["decision_id"])
    state = load_project_ready_state(workspace)
    linked_assumption = None
    for assumption_id in sorted(state["assumptions"]):
        item = state["assumptions"][assumption_id]
        if decision_id in set(str(ref) for ref in item.get("linked_decisions", [])):
            linked_assumption = item
            break
    if linked_assumption is None:
        linked_assumption = _first_record(state["assumptions"])

    if linked_assumption:
        assumption_record = linked_assumption
        assumption_created = False
        assumption_path = assumption_record.get("_path")
    else:
        assumption_result = create_assumption(
            workspace,
            decision_id=decision_id,
            statement=assumption,
            assumption_type="player_understanding",
            risk_level="medium",
            confidence="low",
            test_method=test_method,
            kill_condition="多数测试者无法说清目标、阻力或乐趣来源。",
        )
        assumption_record = assumption_result["assumption"]
        assumption_created = True
        assumption_path = assumption_result["path"]

    assumption_id = str(assumption_record["assumption_id"])
    state = load_project_ready_state(workspace)
    existing_experiment = _existing_experiment_for(
        state,
        decision_id=decision_id,
        assumption_id=assumption_id,
    )
    if existing_experiment:
        experiment = existing_experiment
        experiment_created = False
        experiment_path = experiment.get("_path")
    else:
        experiment_result = plan_experiment(
            workspace,
            decision_id=decision_id,
            assumption_ids=[assumption_id],
            title="三分钟核心循环验证",
            hypothesis="如果方向成立，测试者能在三分钟内说出目标、阻力和下一步想做什么。",
            method=test_method,
            success_criteria=success_criteria
            or [
                "3-5 人中多数能说出目标、阻力和下一步动作。",
                "测试后能决定下一轮默认动作是否继续保持。",
            ],
            failure_criteria=failure_criteria
            or [
                "多数测试者无法解释目标或乐趣来源。",
                "测试后仍无法判断下一轮要继续、调整还是暂停。",
            ],
            sample_size=sample_size,
        )
        experiment = experiment_result["experiment"]
        experiment_created = True
        experiment_path = experiment_result["path"]

    gate = run_gate(workspace, "voi", decision_id, write=True)
    if gate["status"] in {"pass", "warn", "ask_human"}:
        _link_decision_reference(workspace, decision_id, "gate_refs", gate["gate_id"])

    workflow_run = _existing_workflow_run(workspace, "idea-to-validation")
    workflow_created = False
    if workflow_run is None:
        workflow_result = start_workflow(workspace, "idea-to-validation")
        workflow_run = workflow_result["workflow_run"]
        workflow_created = True
    workflow_next_result = workflow_next(workspace, str(workflow_run["run_id"]))

    evidence_command = (
        f'gamedesignos evidence add --workspace "{workspace.root}" --decision {decision_id} '
        '--summary "三分钟验证：写下最关键的观察" --source-type playtest '
        '--source-status private --confidence medium --decision-impact "决定下一轮默认动作是否调整"'
    )
    next_step = "做一次 3-5 人/自测的三分钟验证，然后记录一条观察。"
    return {
        "workspace": str(workspace.root),
        "project_id": workspace.workspace_id,
        "created_workspace": created_workspace,
        "decision": decision,
        "decision_created": decision_created,
        "decision_path": str(decision_path) if decision_path else None,
        "assumption": assumption_record,
        "assumption_created": assumption_created,
        "assumption_path": str(assumption_path) if assumption_path else None,
        "experiment": experiment,
        "experiment_created": experiment_created,
        "experiment_path": str(experiment_path) if experiment_path else None,
        "gate": gate,
        "workflow_run": workflow_next_result["run"],
        "workflow_created": workflow_created,
        "workflow_next": workflow_next_result["next"],
        "next_step": next_step,
        "record_evidence_command": evidence_command,
    }


def health_scan(workspace: Workspace) -> dict[str, Any]:
    state = load_project_ready_state(workspace)
    high_risk_untested = []
    for assumption_id, item in state["assumptions"].items():
        if item.get("risk_level") in {"high", "critical"} and item.get("validation_status") not in {
            "tested",
            "validated",
            "invalidated",
        }:
            high_risk_untested.append(assumption_id)

    experiments_without_results = [
        experiment_id
        for experiment_id, item in state["experiments"].items()
        if item.get("result_status") in {None, "", "planned"} and item.get("review_status") not in {"reviewed", "accepted"}
    ]

    no_rollback = [
        decision_id
        for decision_id, item in state["decisions"].items()
        if (item.get("stakes") in {"high", "critical"} or item.get("reversibility") in {"costly_to_reverse", "irreversible"})
        and not item.get("rollback_trigger")
    ]

    near_without_gate = [
        decision_id
        for decision_id, item in state["decisions"].items()
        if item.get("boundary_status") == "near" and not item.get("gate_refs")
    ]

    return {
        "workspace": str(workspace.root),
        "decisions": len(state["decisions"]),
        "assumptions": len(state["assumptions"]),
        "evidence_items": len(state["evidence"]),
        "experiments": len(state["experiments"]),
        "learning_records": len(state["learning"]),
        "high_risk_untested_assumptions": high_risk_untested,
        "experiments_without_results": experiments_without_results,
        "high_impact_decisions_without_rollback": no_rollback,
        "near_decisions_without_gate": near_without_gate,
        "ok": not (high_risk_untested or no_rollback),
    }


def next_best_action(workspace: Workspace) -> dict[str, Any]:
    health = health_scan(workspace)
    if health["high_impact_decisions_without_rollback"]:
        target = health["high_impact_decisions_without_rollback"][0]
        return {
            "action": "define_rollback_trigger",
            "target": target,
            "reason": "A high-impact decision cannot move toward commitment without rollback.",
            "command_hint": f"gamedesignos gate run rollback {target}",
        }
    if health["high_risk_untested_assumptions"]:
        target = health["high_risk_untested_assumptions"][0]
        return {
            "action": "plan_experiment",
            "target": target,
            "reason": "A high-risk assumption is still untested.",
            "command_hint": "Create an experiment plan linked to this assumption.",
        }
    if health["near_decisions_without_gate"]:
        target = health["near_decisions_without_gate"][0]
        return {
            "action": "run_voi_gate",
            "target": target,
            "reason": "A near-boundary decision needs a VOI gate before more information work.",
            "command_hint": f"gamedesignos gate run voi {target}",
        }
    if health["experiments_without_results"]:
        target = health["experiments_without_results"][0]
        return {
            "action": "review_experiment",
            "target": target,
            "reason": "An experiment exists without a reviewed result.",
            "command_hint": f"gamedesignos gate run experiment {target}",
        }
    if health["decisions"] == 0:
        return {
            "action": "create_decision_object",
            "target": None,
            "reason": "Project-ready work starts from a Decision Object.",
            "command_hint": "gamedesignos new decision",
        }
    return {
        "action": "continue_current_workflow",
        "target": None,
        "reason": "No deterministic Project-Ready blocker was found.",
        "command_hint": "gamedesignos status",
    }


def graph_edges(workspace: Workspace) -> dict[str, Any]:
    state = load_project_ready_state(workspace)
    nodes: dict[str, dict[str, str]] = {}
    edges: list[dict[str, str]] = []

    for decision_id, decision in state["decisions"].items():
        nodes[decision_id] = {"id": decision_id, "type": "decision", "label": str(decision.get("title") or decision_id)}
        for ref in decision.get("evidence_refs", []):
            if ref in state["evidence"]:
                edges.append({"from": ref, "to": decision_id, "type": "supports"})
        for ref in decision.get("assumption_refs", []):
            if ref in state["assumptions"]:
                edges.append({"from": decision_id, "to": ref, "type": "depends_on"})
        for ref in decision.get("experiment_refs", []):
            if ref in state["experiments"]:
                edges.append({"from": ref, "to": decision_id, "type": "tests"})

    for assumption_id, assumption in state["assumptions"].items():
        nodes[assumption_id] = {"id": assumption_id, "type": "assumption", "label": str(assumption.get("statement") or assumption_id)}
        for decision_id in assumption.get("linked_decisions", []) or []:
            if decision_id in nodes:
                edges.append({"from": decision_id, "to": assumption_id, "type": "depends_on"})

    for evidence_id, evidence in state["evidence"].items():
        nodes[evidence_id] = {"id": evidence_id, "type": "evidence", "label": str(evidence.get("summary") or evidence_id)}
        for decision_id in evidence.get("used_by_decisions", []) or []:
            if decision_id in nodes:
                edges.append({"from": evidence_id, "to": decision_id, "type": "supports"})
        for assumption_id in evidence.get("used_by_assumptions", []) or []:
            if assumption_id in state["assumptions"]:
                edges.append({"from": evidence_id, "to": assumption_id, "type": "supports"})

    for experiment_id, experiment in state["experiments"].items():
        nodes[experiment_id] = {"id": experiment_id, "type": "experiment", "label": str(experiment.get("title") or experiment_id)}
        target_decision = experiment.get("target_decision")
        if target_decision in nodes:
            edges.append({"from": experiment_id, "to": target_decision, "type": "tests"})
        for assumption_id in experiment.get("target_assumptions", []) or []:
            if assumption_id in state["assumptions"]:
                edges.append({"from": experiment_id, "to": assumption_id, "type": "tests"})

    for learning_id, learning in state["learning"].items():
        nodes[learning_id] = {"id": learning_id, "type": "learning", "label": str(learning.get("statement") or learning_id)}
        source = learning.get("source")
        if source in nodes:
            edges.append({"from": source, "to": learning_id, "type": "produces"})

    unique_edges = []
    seen = set()
    for edge in edges:
        marker = (edge["from"], edge["to"], edge["type"])
        if marker not in seen:
            seen.add(marker)
            unique_edges.append(edge)
    return {"nodes": nodes, "edges": unique_edges}


def export_graph_mermaid(workspace: Workspace) -> str:
    graph = graph_edges(workspace)
    lines = ["graph TD"]
    for node_id, node in sorted(graph["nodes"].items()):
        safe_id = slugify(node_id, fallback="node").replace("-", "_").upper()
        label = f"{node['type']}: {node['label']}".replace('"', "'")
        lines.append(f'  {safe_id}["{label}"]')
    for edge in graph["edges"]:
        left = slugify(edge["from"], fallback="node").replace("-", "_").upper()
        right = slugify(edge["to"], fallback="node").replace("-", "_").upper()
        lines.append(f"  {left} -- {edge['type']} --> {right}")
    return "\n".join(lines) + "\n"


def inspect_graph(workspace: Workspace, target: str) -> dict[str, Any]:
    graph = graph_edges(workspace)
    if target not in graph["nodes"]:
        raise UsageError(f"Graph target not found: {target}")
    return {
        "target": graph["nodes"][target],
        "incoming": [edge for edge in graph["edges"] if edge["to"] == target],
        "outgoing": [edge for edge in graph["edges"] if edge["from"] == target],
    }
