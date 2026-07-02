# Paranoia AI System Evolver

**Parent project:** [GameDesignOS by Paranoia](../README.en.md)

**Languages:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

This installable GameDesignOS skill upgrades prompts, memory, RAG, tool routing, workflows, schemas, evals, and skills while using a VOI decision gate to prevent FOMO research, AI branch explosion, and high-structure/low-value output.

## What It Combines

- WOOP harness protocol for intent, acceptance, Failure Patterns, and if-then recovery;
- a VOI decision gate that declares the decision, options, default action, and boundary before acquiring information;
- an RJR-AI residual judgment authority gate that makes AI, Workflow, Eval, automation, and human authority explicit;
- a Scenario VOI Adapter that defines valid evidence for skill evolution, game direction, experience diagnosis, source curation, content decisions, platform facts, high-risk actions, and AI branch management;
- EVPI, EVPPI, and EVSI distinctions for value ceilings, target uncertainty, and concrete sample/experiment value;
- model compression and causal mediators for shorter, intervenable, verifiable operating models;
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

## Package Contents

```text
SKILL.md
agents/openai.yaml
references/value-of-information-playbook.md
references/value-of-information-playbook.zh-CN.md
references/value-of-information-playbook.en.md
references/evolution-loop-playbook.md
references/evolution-loop-playbook.zh-CN.md
references/evolution-loop-playbook.en.md
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
templates/evolution_proposal.md
templates/evolution_proposal.zh-CN.md
templates/evolution_proposal.en.md
templates/ooda_voi_state.md
templates/ooda_voi_state.zh-CN.md
templates/ooda_voi_state.en.md
evals/voi-decision-gate-cases.md
evals/voi-decision-gate-cases.en.md
quick_validate.py
```

## Suggested Prompt

```text
Use $paranoia-ai-system-evolver to declare the decision, options, current default action, and decision boundary first. Then establish the RJR-AI authority gate: coupling, reversibility, authority_level, delegation_matrix, and residual_judgment. Apply VOI/EVPI/EVSI to choose which searches, questions, logs, experiments, or AI branches are worth running, define valid evidence, weak evidence, the smallest probe, and the domain stop rule for the concrete scenario, then package the system change as a candidate with WOOP, OODA, evals, Human Gate, and rollback.
```

## Boundary

- Domain skills still own concept, diagnosis, ED experiments, and proposal work; this skill owns system mutation and explicit VOI audits.
- VOI distinguishes `decision_information`, `model_learning`, and `information_consumption` rather than declaring all non-immediate learning useless.
- Qualitative scores are triage aids, not substitutes for quantified high-stakes decision models.
- Real project data remains in private workspaces.

## Maintenance

Run `python scripts/validate_skill.py paranoia-ai-system-evolver` and `python paranoia-ai-system-evolver/quick_validate.py paranoia-ai-system-evolver` after changes. Skill-level mutations require behavior regression and must remain candidate-gated until evidence, approval, and rollback exist.
