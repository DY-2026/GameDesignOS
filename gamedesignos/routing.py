"""Deterministic, explainable skill routing for the local prototype."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .workspace import Workspace, find_repo_root


@dataclass(frozen=True)
class RouteRule:
    skill: str
    signals: tuple[str, ...]
    reason: str
    primary_outputs: tuple[str, ...]
    required_all_upstream_types: tuple[str, ...] = ()
    required_any_upstream_types: tuple[str, ...] = ()


RULES: tuple[RouteRule, ...] = (
    RouteRule(
        "game-experience-analyzer",
        (
            "screenshot",
            "recording",
            "gameplay",
            "video",
            "trailer",
            "pv",
            "store page",
            "steam page",
            "截图",
            "录屏",
            "录像",
            "视频",
            "宣传片",
            "商店页",
            "试玩样本",
        ),
        "媒体或试玩样本要先建立证据边界和问题卡，再进入后续实验或策划判断。",
        ("evidence-index", "issue-card", "ed-handoff", "validation-plan"),
    ),
    RouteRule(
        "game-concept-architect",
        (
            "one line idea",
            "one-line idea",
            "game idea",
            "concept seed",
            "core loop",
            "creative premise",
            "一句话创意",
            "游戏创意",
            "我想做",
            "想做",
            "做一款",
            "做一个游戏",
            "游戏项目",
            "玩法方向",
            "立项方向",
            "概念种子",
            "核心循环",
            "玩法点子",
        ),
        "粗创意要先变成玩家承诺、核心循环、范围门和验证计划，再进入策划案或立项判断。",
        ("player-promise-contract", "validation-plan"),
    ),
    RouteRule(
        "game-design-proposal-writer",
        (
            "proposal",
            "publisher pitch",
            "investor pitch",
            "gdd",
            "vertical slice",
            "decision memo",
            "商业策划案",
            "立项案",
            "发行 pitch",
            "投资 pitch",
            "策划案",
            "垂直切片",
            "决策 memo",
        ),
        "面向决策的文档应整合已有概念、证据、验证和生产约束，而不是补编缺失上游。",
        ("proposal", "pitch", "decision-memo", "vertical-slice-document"),
        required_any_upstream_types=(
            "concept",
            "validation",
            "evidence",
            "analysis",
            "experiment",
            "knowledge",
        ),
    ),
    RouteRule(
        "game-experience-density-optimizer",
        (
            "retention",
            "first session",
            "pacing",
            "feedback strength",
            "cognitive load",
            "instrumentation",
            "dashboard",
            "ab test",
            "a/b test",
            "留存",
            "首局",
            "节奏",
            "反馈",
            "认知负荷",
            "埋点",
            "看板",
            "a/b",
            "体验浓度",
        ),
        "体验问题要先有证据或问题层，才能转成一周实验、埋点和回滚规则。",
        ("weekly-ed-experiment-plan", "instrumentation-dictionary", "dashboard-spec", "decision-rules"),
        required_any_upstream_types=("evidence", "analysis", "experiment"),
    ),
    RouteRule(
        "paranoia-ai-system-evolver",
        (
            "prompt change",
            "workflow change",
            "schema change",
            "eval change",
            "router change",
            "memory change",
            "skill change",
            "voi",
            "fomo",
            "research overload",
            "ai fatigue",
            "提示词改造",
            "工作流改造",
            "schema 改造",
            "评测改造",
            "路由改造",
            "记忆改造",
            "skill 改造",
            "信息价值",
            "信息焦虑",
            "ai 疲劳",
        ),
        "系统改动和信息获取要经过 VOI、eval、Human Gate 和 rollback，先保持 candidate。",
        ("evolution-proposal", "ooda-voi-state", "information-value-assessment"),
    ),
    RouteRule(
        "game-design-source-curator",
        (
            "curate sources",
            "knowledge base",
            "source ingest",
            "article collection",
            "资料策展",
            "知识库",
            "来源整理",
            "文章收集",
        ),
        "散落资料应沉淀成可追踪知识资产，而不是一次性摘要。",
        ("source-note", "reference-boundary", "knowledge-entry"),
    ),
    RouteRule(
        "game-design-book-translator",
        (
            "translate",
            "translation",
            "book chapter",
            "terminology table",
            "翻译",
            "译文",
            "书籍章节",
            "术语表",
        ),
        "设计资料翻译需要术语、图表、来源边界和编辑检查。",
        ("translated-reference", "terminology-table", "chapter-package"),
    ),
)

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

    scored: list[tuple[int, RouteRule, list[str]]] = []
    for rule in RULES:
        matches = [signal for signal in rule.signals if _normalized(signal) in normalized]
        if matches:
            score = sum(max(1, len(_normalized(signal).split())) for signal in matches)
            scored.append((score, rule, matches))

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

    scored.sort(key=lambda item: (-item[0], RULES.index(item[1])))
    _, rule, matches = scored[0]
    result = _result(rule, matches, available, explicit=False)

    # Missing-upstream behavior is intentional: route to the smallest prerequisite,
    # while preserving the user's eventual target.
    missing = set(result["missing_upstream"])
    if rule.skill == "game-experience-density-optimizer" and missing:
        result["target_skill"] = rule.skill
        result["selected_skill"] = "game-experience-analyzer"
        result["reason"] = (
            "这个 ED 实验请求缺少证据或问题层。先建立 sample_boundary、evidence-index 和 issue cards，"
            "再交给 game-experience-density-optimizer。"
        )
        result["primary_outputs"] = ["evidence-index", "issue-card", "ed-handoff"]
    elif rule.skill == "game-design-proposal-writer" and missing:
        result["target_skill"] = rule.skill
        result["selected_skill"] = "game-concept-architect"
        result["reason"] = (
            "策划案路线缺少概念或验证基础。先创建 player promise 和 validation plan，"
            "再进入 game-design-proposal-writer 成案。"
        )
        result["primary_outputs"] = ["player-promise-contract", "validation-plan"]

    return result


def _result(
    rule: RouteRule, matches: list[str], available: set[str], *, explicit: bool
) -> dict[str, Any]:
    missing = [item for item in rule.required_all_upstream_types if item not in available]
    if rule.required_any_upstream_types and not any(
        item in available for item in rule.required_any_upstream_types
    ):
        missing.append("one_of:" + "|".join(rule.required_any_upstream_types))
    confidence = "high" if explicit or len(matches) >= 2 else "medium"
    return {
        "selected_skill": rule.skill,
        "target_skill": rule.skill,
        "confidence": confidence,
        "reason": rule.reason,
        "matched_signals": matches,
        "available_asset_types": sorted(available),
        "missing_upstream": missing,
        "primary_outputs": list(rule.primary_outputs),
        "executed": False,
    }


def router_source(workspace: Workspace | None = None) -> str:
    root = find_repo_root(workspace.root if workspace else Path.cwd())
    if root and (root / "contracts" / "router.yaml").is_file():
        return str(root / "contracts" / "router.yaml")
    return "embedded-v0.9-route-rules"
