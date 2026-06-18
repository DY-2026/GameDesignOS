#!/usr/bin/env python3
"""Validate the public GameDesignOS repository, Runtime Foundation, and VOI Decision Gate."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from validate_skill import _parse_json, _parse_yaml, validate_skill


REQUIRED_SKILLS = [
    "game-experience-analyzer",
    "game-concept-architect",
    "paranoia-ai-system-evolver",
    "game-design-book-translator",
    "game-design-source-curator",
    "game-experience-density-optimizer",
    "game-design-proposal-writer",
]

REQUIRED_PATHS = [
    ".gitignore",
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "adapters/README.md",
    "contracts/README.md",
    "contracts/router.yaml",
    "contracts/ed-handoff.schema.json",
    "contracts/project-workspace.schema.json",
    "contracts/design-asset-index.schema.json",
    "contracts/decision-log.schema.json",
    "contracts/information-value-assessment.schema.json",
    "docs/product/README.md",
    "docs/product/vision.md",
    "docs/product/architecture.md",
    "docs/product/mvp-definition.md",
    "docs/product/roadmap.md",
    "docs/workflows/README.md",
    "docs/workflows/decision-to-information.md",
    "docs/workflows/idea-to-validation.md",
    "docs/workflows/media-to-diagnosis.md",
    "docs/workflows/weekly-ed-experiment.md",
    "docs/workflows/evidence-to-proposal.md",
    "runtime/README.md",
    "runtime/cli/README.md",
    "runtime/cli/commands.md",
    "runtime/workspace-template/README.md",
    "runtime/workspace-template/game.designos.yaml",
    "runtime/workspace-template/design-asset-index.example.json",
    "runtime/workspace-template/06-decisions/decision-brief.template.md",
    "runtime/workspace-template/06-decisions/decision-log.example.json",
    "runtime/workspace-template/06-decisions/information-value-assessment.example.json",
    "paranoia-ai-system-evolver/references/value-of-information-playbook.md",
    "paranoia-ai-system-evolver/references/value-of-information-playbook.zh-CN.md",
    "paranoia-ai-system-evolver/references/value-of-information-playbook.en.md",
    "paranoia-ai-system-evolver/templates/voi_decision_gate.md",
    "paranoia-ai-system-evolver/templates/voi_decision_gate.zh-CN.md",
    "paranoia-ai-system-evolver/templates/voi_decision_gate.en.md",
    "paranoia-ai-system-evolver/evals/voi-decision-gate-cases.md",
    "paranoia-ai-system-evolver/evals/voi-decision-gate-cases.en.md",
    "releases/v0.8.0.md",
    ".github/workflows/validate.yml",
    "scripts/run_behavior_evals.py",
]

WORKSPACE_TEMPLATE_DIRS = {
    "inbox_dir": "00-inbox",
    "concept_dir": "01-concept",
    "evidence_dir": "02-evidence",
    "analysis_dir": "03-analysis",
    "proposals_dir": "04-proposals",
    "experiments_dir": "05-experiments",
    "decisions_dir": "06-decisions",
    "retrospectives_dir": "07-retrospectives",
}

WORKSPACE_REQUIRED_RULES = {
    "evidence_before_opinion",
    "feasibility_before_scope",
    "workflow_before_one_off_prompts",
    "voi_before_research",
    "eval_before_promotion",
    "rollback_before_confidence",
    "human_gate_for_commitments",
    "decision_before_information",
    "action_change_before_research",
    "sample_before_scale",
    "stop_when_marginal_voi_nonpositive",
    "preserve_local_negative_evidence",
}

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "_private_translations",
    ".venv",
    "venv",
    "node_modules",
}

PRIVATE_IGNORE_RULES = {"_private_translations/"}


def _iter_data_files(repo_root: Path):
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(repo_root).parts):
            continue
        if path.suffix == ".json" or path.suffix in {".yaml", ".yml"}:
            yield path


def _check_required_paths(repo_root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_PATHS:
        if not (repo_root / relative).exists():
            errors.append(f"{relative}: required path missing")


def _check_private_ignore_rules(repo_root: Path, errors: list[str]) -> None:
    gitignore = repo_root / ".gitignore"
    if not gitignore.exists():
        return
    rules = {
        line.strip()
        for line in gitignore.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    for required in sorted(PRIVATE_IGNORE_RULES):
        accepted = {
            required,
            required.rstrip("/"),
            f"/{required}",
            f"/{required.rstrip('/')}",
        }
        if rules.isdisjoint(accepted):
            errors.append(f".gitignore: missing required private ignore rule {required}")


def _check_repo_data_files(repo_root: Path, errors: list[str]) -> None:
    for path in _iter_data_files(repo_root):
        if path.suffix == ".json":
            data = _parse_json(path, errors)
            if path.name.endswith(".schema.json"):
                if not isinstance(data, dict):
                    errors.append(f"{path}: schema file must be a JSON object")
                elif "$schema" not in data:
                    errors.append(f"{path}: *.schema.json must contain $schema")
        else:
            _parse_yaml(path, errors)


def _require_mapping(data: Any, path: Path, label: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(data, dict):
        errors.append(f"{path}: {label} must be a mapping")
        return {}
    return data


def _check_workspace_example(path: Path, errors: list[str]) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = _parse_json(path, errors)
    if not isinstance(data, dict):
        return {}
    if data.get("schema_version") != "0.8.0":
        errors.append(f"{path}: schema_version must be 0.8.0")
    workspace_id = data.get("workspace_id")
    if not isinstance(workspace_id, str) or not workspace_id.strip():
        errors.append(f"{path}: workspace_id must be non-empty")
    return data


def _check_workspace_template(repo_root: Path, errors: list[str]) -> None:
    workspace_root = repo_root / "runtime" / "workspace-template"
    manifest_path = workspace_root / "game.designos.yaml"

    for directory in WORKSPACE_TEMPLATE_DIRS.values():
        guide = workspace_root / directory / "README.md"
        if not guide.exists():
            errors.append(
                f"runtime/workspace-template/{directory}/README.md: "
                "required workspace guide missing"
            )

    if not manifest_path.exists():
        return

    manifest = _require_mapping(
        _parse_yaml(manifest_path, errors), manifest_path, "workspace manifest", errors
    )
    if not manifest:
        return

    if manifest.get("schema_version") != "0.8.0":
        errors.append(f"{manifest_path}: schema_version must be 0.8.0")
    if manifest.get("workspace_type") != "gamedesignos-project":
        errors.append(f"{manifest_path}: workspace_type must be gamedesignos-project")

    project = _require_mapping(manifest.get("project"), manifest_path, "project", errors)
    for field in ("id", "title", "codename", "status", "visibility", "owner"):
        value = project.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{manifest_path}: project.{field} must be non-empty")

    designos = _require_mapping(manifest.get("designos"), manifest_path, "designos", errors)
    if designos.get("version") != "0.8.0":
        errors.append(f"{manifest_path}: designos.version must be 0.8.0")
    if designos.get("public_base_repo") != "DY-2026/GameDesignOS":
        errors.append(f"{manifest_path}: designos.public_base_repo must be DY-2026/GameDesignOS")
    if not isinstance(designos.get("private_overlay"), bool):
        errors.append(f"{manifest_path}: designos.private_overlay must be boolean")

    assets = _require_mapping(manifest.get("assets"), manifest_path, "assets", errors)
    if not isinstance(assets.get("index"), str) or not assets.get("index", "").strip():
        errors.append(f"{manifest_path}: assets.index must be non-empty")
    for field, expected_directory in WORKSPACE_TEMPLATE_DIRS.items():
        value = assets.get(field)
        if value != expected_directory:
            errors.append(f"{manifest_path}: assets.{field} must be {expected_directory}")
        elif not (workspace_root / value).is_dir():
            errors.append(f"{manifest_path}: assets.{field} points to missing directory {value}")

    rules = _require_mapping(manifest.get("rules"), manifest_path, "rules", errors)
    for field in sorted(WORKSPACE_REQUIRED_RULES):
        if rules.get(field) is not True:
            errors.append(f"{manifest_path}: rules.{field} must be true")

    asset_index = _check_workspace_example(
        workspace_root / "design-asset-index.example.json", errors
    )
    types = {
        item.get("asset_type")
        for item in asset_index.get("assets", [])
        if isinstance(item, dict)
    }
    if asset_index and "information-assessment" not in types:
        errors.append(
            f"{workspace_root / 'design-asset-index.example.json'}: "
            "must include an information-assessment asset"
        )

    decision_log = _check_workspace_example(
        workspace_root / "06-decisions" / "decision-log.example.json", errors
    )
    decisions = decision_log.get("decisions", []) if decision_log else []
    if decisions and not any(
        isinstance(item, dict)
        and item.get("decision_type") == "information"
        and item.get("current_default_action")
        and item.get("information_stop_reason")
        for item in decisions
    ):
        errors.append(
            f"{workspace_root / '06-decisions' / 'decision-log.example.json'}: "
            "must demonstrate an information decision with default action and stop reason"
        )

    voi_example = _check_workspace_example(
        workspace_root / "06-decisions" / "information-value-assessment.example.json",
        errors,
    )
    if voi_example:
        decision = voi_example.get("decision")
        if not isinstance(decision, dict) or not decision.get("current_default_action"):
            errors.append("information-value-assessment example lacks current_default_action")
        actions = voi_example.get("candidate_information_actions")
        if not isinstance(actions, list) or len(actions) > 3:
            errors.append("information-value-assessment example must contain at most 3 actions")
        stop_rule = voi_example.get("stop_rule")
        if not isinstance(stop_rule, dict) or not stop_rule.get("stop_when"):
            errors.append("information-value-assessment example lacks stop_rule.stop_when")


def _check_paranoia_voi(repo_root: Path, errors: list[str]) -> None:
    skill_root = repo_root / "paranoia-ai-system-evolver"
    if not skill_root.is_dir():
        return

    skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    for marker in (
        "Decision Object",
        "current_default_action",
        "EVPI",
        "EVSI",
        "candidate_information_actions",
        "references/value-of-information-playbook",
    ):
        if marker not in skill:
            errors.append(f"paranoia-ai-system-evolver/SKILL.md: missing VOI marker {marker}")

    playbook = (skill_root / "references" / "value-of-information-playbook.zh-CN.md")
    if playbook.exists():
        text = playbook.read_text(encoding="utf-8")
        for marker in ("信号—行动映射", "AI 疲劳 Gate", "反 AI 味 Gate", "EVPPI"):
            if marker not in text:
                errors.append(f"{playbook}: missing section marker {marker}")

    cases = skill_root / "evals" / "voi-decision-gate-cases.md"
    if cases.exists() and cases.read_text(encoding="utf-8").count("## Case") < 8:
        errors.append(f"{cases}: requires at least 8 VOI behavior cases")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    all_errors: list[str] = []

    _check_required_paths(repo_root, all_errors)
    _check_private_ignore_rules(repo_root, all_errors)
    _check_workspace_template(repo_root, all_errors)

    for skill_name in REQUIRED_SKILLS:
        skill_dir = repo_root / skill_name
        if not skill_dir.exists():
            all_errors.append(f"{skill_name}: required skill folder missing")
            continue
        all_errors.extend(validate_skill(skill_dir))

    _check_paranoia_voi(repo_root, all_errors)
    _check_repo_data_files(repo_root, all_errors)

    if all_errors:
        print("Repository validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("OK: repository")
    print("Validated Runtime Foundation:")
    print("- product docs")
    print("- workflow docs")
    print("- project workspace")
    print("- workspace contracts")
    print("Validated VOI Decision Gate:")
    print("- decision object and current default action")
    print("- EVPI / EVSI and signal-to-action mapping")
    print("- information-cost and stop-rule fields")
    print("- behavior-eval cases")
    print("Validated skills:")
    for skill_name in REQUIRED_SKILLS:
        print(f"- {skill_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
