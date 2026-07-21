# Paranoia AI System Evolver

**Parent project:** [GameDesignOS by Paranoia](../README.en.md)

**Languages:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

This installable GameDesignOS skill upgrades AI work orders from action instructions to intent work orders. It also upgrades prompts, memory, RAG, tool routing, workflows, schemas, evals, and skills while using a VOI decision gate to prevent FOMO research, AI branch explosion, and high-structure/low-value output.

## What It Combines

- an Intent Work Order for the reality to change, verifier, first-glance acceptance, non-sacrifice boundaries, and AI autonomy boundary;
- WOOP harness protocol for intent, acceptance, Failure Patterns, and if-then recovery;
- a VOI decision gate that declares the decision, options, default action, and boundary before acquiring information;
- an RJR-AI residual judgment authority gate that makes AI, Workflow, Eval, automation, and human authority explicit;
- a Scenario VOI Adapter that defines valid evidence for skill evolution, game direction, experience diagnosis, source curation, content decisions, platform facts, high-risk actions, and AI branch management;
- EVPI, EVPPI, and EVSI distinctions for value ceilings, target uncertainty, and concrete sample/experiment value;
- model compression and causal mediators for shorter, intervenable, verifiable operating models;
- UL (Uncertainty Ladder) from UL-L0 to UL-L5 for controlled exposure, failure attribution, progressive complexity, and transfer;
- Orient-first OODA for reality-driven frame updates;
- evals, Human Gates, versioning, and rollback for controlled promotion.

## New VOI Hard Rules

```text
No decision object -> no open-ended research.
No current default action -> no action-change test.
All plausible signals lead to the same action -> current decision VOI is approximately zero.
EVPI is the value ceiling; EVSI is the value of a concrete sample or experiment.
After the generic VOI gate, define valid evidence, weak evidence, the smallest probe, and the domain stop rule for the concrete scenario.
Net VOI subtracts acquisition, delay, attention, privacy, and contamination costs.
Stop when the marginal information value no longer exceeds its cost.
```

## RJR-AI Authority Hard Rules

```text
AI expands possibilities; it does not own the final bet.
Workflow compresses chaos; it does not rewrite the human judgment layer.
Eval provides feedback; it does not replace high-coupling, low-reversibility decisions.
Low-risk reversible work can be automated.
High-coupling, low-reversibility, under-evidenced choices preserve residual_judgment and enter Human Gate.
```

## UL Hard Rules

```text
VOI chooses the uncertainty; UL controls exposure dose.
Release one major variable per round by default and declare held constants, scaffolds, and consequence budget.
If leading failure explanations cannot be separated, mark confounded and return to a controlled environment.
Fixture success is not transfer proof; test novel structure and negative transfer.
Task complexity never auto-promotes authority; real-world consequence still requires Human Gate.
```

## Package Contents

```text
SKILL.md
agents/openai.yaml
references/value-of-information-playbook.md
references/value-of-information-playbook.zh-CN.md
references/value-of-information-playbook.en.md
references/intent-engineering-work-order.md
references/intent-engineering-work-order.zh-CN.md
references/intent-engineering-work-order.en.md
references/project-workflow-governance.md
references/project-workflow-governance.zh-CN.md
references/project-workflow-governance.en.md
references/evolution-loop-playbook.md
references/evolution-loop-playbook.zh-CN.md
references/evolution-loop-playbook.en.md
references/uncertainty-ladder-protocol.md
references/uncertainty-ladder-protocol.zh-CN.md
references/uncertainty-ladder-protocol.en.md
references/woop-harness-protocol.md
references/woop-harness-protocol.zh-CN.md
references/woop-harness-protocol.en.md
references/model-compression-playbook.md
references/model-compression-playbook.zh-CN.md
references/model-compression-playbook.en.md
references/eval-versioning-playbook.md
references/eval-versioning-playbook.zh-CN.md
references/eval-versioning-playbook.en.md
templates/voi_decision_gate.md
templates/voi_decision_gate.zh-CN.md
templates/voi_decision_gate.en.md
templates/intent_work_order.md
templates/intent_work_order.zh-CN.md
templates/intent_work_order.en.md
templates/workflow_governance_review.md
templates/workflow_governance_review.zh-CN.md
templates/workflow_governance_review.en.md
templates/evolution_proposal.md
templates/evolution_proposal.zh-CN.md
templates/evolution_proposal.en.md
templates/ooda_voi_state.md
templates/ooda_voi_state.zh-CN.md
templates/ooda_voi_state.en.md
templates/uncertainty_ladder_state.md
templates/uncertainty_ladder_state.zh-CN.md
templates/uncertainty_ladder_state.en.md
evals/voi-decision-gate-cases.md
evals/voi-decision-gate-cases.en.md
evals/uncertainty-ladder-cases.md
evals/uncertainty-ladder-cases.en.md
examples/ul-state.example.json
quick_validate.py
```

## Suggested Prompt

```text
Use $paranoia-ai-system-evolver to upgrade this task from an instruction sheet into an Intent Work Order: define the reality to change, larger project goal, desired outside-world state, verifier, first-glance acceptance, non-sacrifice boundaries, what AI may freely change, what AI must not touch, principles for changing direction if the plan fails, and failure signals to check before delivery. Then declare the decision, options, current default action, and decision boundary; establish the RJR-AI authority gate; apply VOI/EVPI/EVSI; use UL to declare the UL-L0 to UL-L5 rung, released and held variables, scaffolds, attribution gate, transfer checks, and fallback; and package the system change as a candidate with WOOP, OODA, evals, Human Gate, rollback, and retrospective learning.
```

## Boundary

- Domain skills still own concept, diagnosis, ED experiments, and proposal work; this skill owns system mutation and explicit VOI audits.
- The Intent Work Order is not a parallel process; it is the task entry before WOOP/VOI/RJR-AI, designed to reduce human micromanagement without granting unbounded AI autonomy.
- VOI distinguishes `decision_information`, `model_learning`, and `information_consumption` rather than declaring all non-immediate learning useless.
- UL controls experimental exposure, not authority, and is not a fixed waterfall; RJR-AI still governs delegation.
- Qualitative scores are triage aids, not substitutes for quantified high-stakes decision models.
- Real project data remains in private workspaces.

## Maintenance

Run `python scripts/validate_skill.py paranoia-ai-system-evolver` and `python paranoia-ai-system-evolver/quick_validate.py paranoia-ai-system-evolver` after changes. Skill-level mutations require behavior regression, attributable failures, and transfer checks, and must remain candidate-gated until evidence, approval, and rollback exist.
