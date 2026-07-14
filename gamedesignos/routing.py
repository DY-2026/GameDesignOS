"""Deterministic, explainable routing compiled from contracts/router.yaml."""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from .io_utils import read_yaml
from .resources import contracts_dir, resource_mode
from .workspace import Workspace


@dataclass(frozen=True)
class RouteRule:
    rule_id: str
    skill: str
    signals: tuple[str, ...]
    reason: str
    primary_outputs: tuple[str, ...]
    required_all_upstream_types: tuple[str, ...] = ()
    required_any_upstream_types: tuple[str, ...] = ()


def _strings(value: Any, *, field: str, rule_id: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise ValueError(f"router rule {rule_id}: {field} must be a list of non-empty strings")
    return tuple(value)


@lru_cache(maxsize=1)
def load_rules() -> tuple[RouteRule, ...]:
    path = contracts_dir() / "router.yaml"
    payload = read_yaml(path)
    if not isinstance(payload, dict) or not isinstance(payload.get("default_rules"), list):
        raise ValueError(f"Invalid router contract: {path}")

    rules: list[RouteRule] = []
    for raw in payload["default_rules"]:
        if not isinstance(raw, dict):
            raise ValueError(f"Invalid router rule in {path}")
        rule_id = str(raw.get("id") or "")
        skill = str(raw.get("use") or "")
        runtime = raw.get("runtime")
        if not rule_id or not skill or not isinstance(runtime, dict):
            raise ValueError(f"router rule requires id, use, and runtime mapping: {raw!r}")
        rules.append(
            RouteRule(
                rule_id=rule_id,
                skill=skill,
                signals=_strings(runtime.get("signals"), field="runtime.signals", rule_id=rule_id),
                reason=str(runtime.get("reason_zh") or raw.get("reason") or ""),
                primary_outputs=_strings(raw.get("primary_outputs"), field="primary_outputs", rule_id=rule_id),
                required_all_upstream_types=_strings(
                    runtime.get("required_all_upstream_types"),
                    field="runtime.required_all_upstream_types",
                    rule_id=rule_id,
                ),
                required_any_upstream_types=_strings(
                    runtime.get("required_any_upstream_types"),
                    field="runtime.required_any_upstream_types",
                    rule_id=rule_id,
                ),
            )
        )
    if not rules or any(not rule.signals for rule in rules):
        raise ValueError(f"Every router rule must define runtime.signals: {path}")
    return tuple(rules)


RULES = load_rules()
EXPLICIT_SKILL_NAMES = {rule.skill: rule for rule in RULES}


def _normalized(text: str) -> str:
    text = text.lower().replace("_", " ").replace("-", " ")
    return re.sub(r"\s+", " ", text).strip()


def _available_asset_types(workspace: Workspace | None) -> set[str]:
    if workspace is None:
        return set()
    try:
        index = workspace.load_asset_index()
    except Exception:  # noqa: BLE001 - routing should remain available for diagnosis.
        return set()
    return {
        str(item.get("asset_type"))
        for item in index.get("assets", [])
        if isinstance(item, dict) and item.get("review_status") not in {"rejected", "superseded"}
    }


def route_task(task: str, *, workspace: Workspace | None = None) -> dict[str, Any]:
    normalized = _normalized(task)
    available = _available_asset_types(workspace)

    for skill_name, rule in EXPLICIT_SKILL_NAMES.items():
        if _normalized(skill_name) in normalized or f"${skill_name}" in task:
            return _result(rule, [skill_name], available, explicit=True)

    scored: list[tuple[int, int, RouteRule, list[str]]] = []
    for index, rule in enumerate(RULES):
        matches = [signal for signal in rule.signals if _normalized(signal) in normalized]
        if matches:
            score = sum(max(1, len(_normalized(signal).split())) for signal in matches)
            scored.append((score, index, rule, matches))

    if not scored:
        return {
            "selected_skill": None,
            "target_skill": None,
            "confidence": "low",
            "reason": "暂时没有稳定匹配路线。请补一句最终想产出的东西，或直接点名 skill。",
            "matched_signals": [],
            "available_asset_types": sorted(available),
            "missing_upstream": [],
            "primary_outputs": [],
            "executed": False,
        }

    _, _, rule, matches = sorted(scored, key=lambda item: (-item[0], item[1]))[0]
    result = _result(rule, matches, available, explicit=False)

    missing = set(result["missing_upstream"])
    if rule.skill == "game-experience-density-optimizer" and missing:
        result.update(
            selected_skill="game-experience-analyzer",
            target_skill=rule.skill,
            reason=(
                "这个 ED 实验请求缺少证据或问题层。先建立 sample_boundary、evidence-index 和 issue cards，"
                "再交给 game-experience-density-optimizer。"
            ),
            primary_outputs=["evidence-index", "issue-card", "ed-handoff"],
        )
    elif rule.skill == "game-design-proposal-writer" and missing:
        result.update(
            selected_skill="game-concept-architect",
            target_skill=rule.skill,
            reason=(
                "策划案路线缺少概念或验证基础。先创建 player promise 和 validation plan，"
                "再进入 game-design-proposal-writer 成案。"
            ),
            primary_outputs=["player-promise-contract", "validation-plan"],
        )
    return result


def _result(rule: RouteRule, matches: list[str], available: set[str], *, explicit: bool) -> dict[str, Any]:
    missing = [item for item in rule.required_all_upstream_types if item not in available]
    if rule.required_any_upstream_types and not any(
        item in available for item in rule.required_any_upstream_types
    ):
        missing.append("one_of:" + "|".join(rule.required_any_upstream_types))
    return {
        "selected_skill": rule.skill,
        "target_skill": rule.skill,
        "confidence": "high" if explicit or len(matches) >= 2 else "medium",
        "reason": rule.reason,
        "matched_signals": matches,
        "available_asset_types": sorted(available),
        "missing_upstream": missing,
        "primary_outputs": list(rule.primary_outputs),
        "executed": False,
    }


def router_source(workspace: Workspace | None = None) -> str:
    start = workspace.root if workspace else Path.cwd()
    return f"{contracts_dir(start) / 'router.yaml'} ({resource_mode(start)})"
