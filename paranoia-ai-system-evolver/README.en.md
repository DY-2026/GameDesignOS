# Paranoia AI System Evolver

**Parent project:** [ParanoiaSkills](../README.en.md)

**Languages:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

This is one installable skill inside `ParanoiaSkills`. It owns the Paranoia Method system-evolution capability; it is not the whole project.

## What This Skill Does

It helps an agent improve AI systems by turning behavior changes into auditable operating-model proposals. The goal is not to add more caution words; it is to decide whether a system change has enough evidence, lower total description cost, controlled rollout, and rollback.

The skill applies the Paranoia Method through:

- Operating-model audit: make the implicit model, causal mediators, and control points explicit
- Total description cost: compare seven cost terms before and after a change instead of judging only the prompt
- Assertion evidence ledger: separate verified facts, tool observations, inference judgments, assumptions, and human-confirmation items
- Missing-alternative check: verify that important options and subagent findings were not compressed away
- Deterministic gates first: prefer schema, routing, validators, retry, and rollback before LLM judgment
- Shadow-first release: move behavior-changing gates through `off -> shadow -> warn -> enforce -> rollbackable`
- Human Gate and rollback: keep durable promotions approved and reversible

## Package Contents

```text
SKILL.md
agents/openai.yaml
references/evolution-loop-playbook.md
references/evolution-loop-playbook.zh-CN.md
references/evolution-loop-playbook.en.md
references/model-compression-playbook.md
references/model-compression-playbook.zh-CN.md
references/model-compression-playbook.en.md
references/eval-versioning-playbook.md
references/eval-versioning-playbook.zh-CN.md
references/eval-versioning-playbook.en.md
templates/evolution_proposal.md
templates/evolution_proposal.zh-CN.md
templates/evolution_proposal.en.md
templates/ooda_voi_state.md
templates/ooda_voi_state.zh-CN.md
templates/ooda_voi_state.en.md
quick_validate.py
```

## Suggested Prompt

```text
Use $paranoia-ai-system-evolver to turn this AI workflow problem into a Paranoia Method evolution proposal: operating model, total description cost, assertion evidence ledger, missing-alternative check, shadow-first rollout, evals, Human Gate, and rollback.
```

## Boundary Inside ParanoiaSkills

- The root README manages the whole `ParanoiaSkills` catalog, structure, and governance rules.
- This README explains only the `paranoia-ai-system-evolver` skill.
- `SKILL.md` is the lightweight agent entrypoint.
- `references/` contains methodology loaded as needed.
- `templates/` contains reusable working forms.

## Maintenance Rules

- Keep `SKILL.md` as the lightweight routing layer.
- Put durable methodology in `references/`.
- Put copy-paste working forms in `templates/`.
- After changes, run `python scripts/validate_skill.py paranoia-ai-system-evolver` from the repository root, then sync the runtime copy and verify both copies match.
- Keep the frontmatter `name`, folder name, `agents/openai.yaml`, and public README naming aligned.
- Treat global installation, long-term memory writes, and production-impacting changes as Human Gate actions.
