"""Stable runtime constants and conservative default mappings."""

from __future__ import annotations

from dataclasses import dataclass

RUNTIME_VERSION = "1.3.0.dev0"
WORKSPACE_SCHEMA_VERSION = "0.8.0"
PROJECT_READY_WORKSPACE_SCHEMA_VERSION = "1.0.0"
SUPPORTED_WORKSPACE_SCHEMAS = {"0.8.0", "1.0.0"}
SUPPORTED_RUNTIME_VERSIONS = {"0.8.0", "0.9.0", "1.0.0", "1.1.0", "1.2.0", "1.3.0.dev0"}
PUBLIC_BASE_REPO = "DY-2026/GameDesignOS"
WORKSPACE_TYPE = "gamedesignos-project"

LIFECYCLE_DIRS = {
    "inbox_dir": "00-inbox",
    "concept_dir": "01-concept",
    "evidence_dir": "02-evidence",
    "analysis_dir": "03-analysis",
    "proposals_dir": "04-proposals",
    "experiments_dir": "05-experiments",
    "decisions_dir": "06-decisions",
    "retrospectives_dir": "07-retrospectives",
}

PROJECT_READY_LIFECYCLE_DIRS = {
    "inbox_dir": "00-inbox",
    "decisions_dir": "01-decisions",
    "assumptions_dir": "02-assumptions",
    "evidence_dir": "03-evidence",
    "experiments_dir": "04-experiments",
    "design_assets_dir": "05-design-assets",
    "workflows_dir": "06-workflows",
    "learning_dir": "07-learning",
    "exports_dir": "08-exports",
}

REQUIRED_RULES = {
    "evidence_before_opinion": True,
    "feasibility_before_scope": True,
    "workflow_before_one_off_prompts": True,
    "voi_before_research": True,
    "eval_before_promotion": True,
    "rollback_before_confidence": True,
    "human_gate_for_commitments": True,
    "decision_before_information": True,
    "action_change_before_research": True,
    "sample_before_scale": True,
    "stop_when_marginal_voi_nonpositive": True,
    "preserve_local_negative_evidence": True,
}

VALID_PROJECT_STATUSES = {"concept", "prototype", "demo", "vertical-slice", "production", "paused", "archived"}
VALID_VISIBILITIES = {"private", "public-synthetic", "public-cleared"}
VALID_SOURCE_STATUSES = {"private", "synthetic", "public", "cleared", "needs_review"}
VALID_ASSET_TYPES = {"inbox", "concept", "validation", "evidence", "analysis", "proposal", "experiment", "information-assessment", "decision", "retrospective", "knowledge"}
VALID_ASSET_TYPES = VALID_ASSET_TYPES | {"assumption", "learning", "gate-result", "workflow-run"}
VALID_ASSET_FORMATS = {"markdown", "json", "yaml", "csv", "image", "video", "audio", "binary", "external-link"}
VALID_CREATED_BY = {"human", "agent", "human-agent", "import"}
VALID_DECISION_TYPES = {"prototype_direction", "concept_gate", "scope_gate", "validation", "experiment", "milestone", "proposal", "release", "workflow", "information"}
VALID_DECISION_STATUSES = {"proposed", "accepted", "rejected", "reversed", "superseded"}
VALID_REVIEW_STATUSES = {"draft", "needs_review", "reviewed", "accepted", "rejected", "superseded"}


@dataclass(frozen=True)
class AssetSpec:
    command_name: str
    index_type: str
    directory_key: str
    extension: str
    id_prefix: str
    source_skill: str | None
    default_title: str


ASSET_SPECS = {
    "concept": AssetSpec("concept", "concept", "concept_dir", "md", "CONCEPT", "game-concept-architect", "Concept Seed"),
    "evidence-index": AssetSpec("evidence-index", "evidence", "evidence_dir", "json", "EVIDENCE", "game-experience-analyzer", "Evidence Index"),
    "issue-card": AssetSpec("issue-card", "analysis", "analysis_dir", "json", "ISSUE", "game-experience-analyzer", "Issue Card"),
    "validation-plan": AssetSpec("validation-plan", "validation", "concept_dir", "json", "VALIDATION", "game-concept-architect", "Validation Plan"),
    "information-assessment": AssetSpec("information-assessment", "information-assessment", "decisions_dir", "json", "VOI", "paranoia-ai-system-evolver", "Information Value Assessment"),
    "ed-handoff": AssetSpec("ed-handoff", "experiment", "experiments_dir", "json", "EDH", "game-experience-analyzer", "ED Handoff"),
    "experiment": AssetSpec("experiment", "experiment", "experiments_dir", "md", "EXPERIMENT", "game-experience-density-optimizer", "Weekly Experiment Plan"),
    "proposal": AssetSpec("proposal", "proposal", "proposals_dir", "md", "PROPOSAL", "game-design-proposal-writer", "Decision-Ready Proposal"),
    "decision": AssetSpec("decision", "decision", "decisions_dir", "json", "DECISION", None, "Decision Record"),
    "retrospective": AssetSpec("retrospective", "retrospective", "retrospectives_dir", "md", "RETRO", "paranoia-ai-system-evolver", "Retrospective"),
}

PACK_ALLOWED_SOURCE_STATUSES = {
    "internal-review": VALID_SOURCE_STATUSES,
    "publisher": {"synthetic", "public", "cleared"},
    "public-synthetic": {"synthetic"},
}

SENSITIVE_BASENAMES = {".env", ".env.local", "credentials.json", "secrets.json", "host-config.json", "api-keys.json"}
SENSITIVE_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}

WORKSPACE_GUIDES = {
    "00-inbox": "Unreviewed intake only. Move accepted material into a durable asset before treating it as design truth.",
    "01-concept": "Concept seed, player promise, core loop, scope gate, and validation plans.",
    "02-evidence": "Source boundaries, timestamped observations, screenshots, and evidence indexes.",
    "03-analysis": "Interpretation, diagnosis, issue cards, and transfer boundaries.",
    "04-proposals": "Decision-facing memos, pitches, dossiers, and vertical-slice plans.",
    "05-experiments": "Sample-information plans, instrumentation, dashboards, results, and rollback rules.",
    "06-decisions": "Human authority, Decision Objects, VOI gates, accepted commitments, and reversals.",
    "07-retrospectives": "What changed, what failed, what is reusable, and what remains only a candidate rule.",
}

PROJECT_READY_WORKSPACE_GUIDES = {
    "00-inbox": "只放未经整理的输入。任何材料进入项目主线前，必须先连接到决策、证据或假设。",
    "01-decisions": "Decision Object、Human Gate、承诺记录、拒绝、反转和 supersede 链路。",
    "02-assumptions": "设计假设登记表。高风险假设必须写出测试方法、验证状态和 kill condition。",
    "03-evidence": "证据账本。每条证据都要写清来源类型、来源状态、支持范围和不能证明什么。",
    "04-experiments": "实验计划、实验结果和复盘。实验必须绑定 decision 或 assumption。",
    "05-design-assets": "概念、分析、提案和规格。只有证据边界明确后才进入这里。",
    "06-workflows": "工作流运行记录，说明当前卡点、缺失资产和下一步最小动作。",
    "07-learning": "复盘后的学习记录。默认先是 candidate，不直接变成长期规则。",
    "08-exports": "评审和发布导出包。公开导出不能包含 private 或 needs_review 证据。",
}
