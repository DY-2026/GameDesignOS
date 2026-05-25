---
name: voi-ooda-ai-system-evolver
description: Use when upgrading an AI system, agent workflow, Codex skill, prompt, memory, RAG, tool routing, schema, eval set, or feedback loop with VOI, OODA, evals, traces, human gates, versioning, and rollback. Use for controlled self-improving AI system design without uncontrolled model weight changes.
metadata:
  short-description: Controlled AI system evolution with VOI/OODA/evals
---

# VOI-OODA AI System Evolver

> Copyright (c) 2026 @Paranoia. All rights reserved.

## Core Stance

Treat AI system evolution as controlled system design, not mystical self-improvement.

```text
OODA keeps the agent moving through reality.
VOI decides what is worth learning, asking, searching, reading, or testing.
Evals decide which changes deserve to remain.
Human Gate prevents a useful one-off mutation from contaminating future systems.
Rollback keeps every promotion reversible.
```

OODA is not about reacting faster. The center of gravity is Orient: refresh the map, rewrite the frame, and test whether the old narrative has expired.

## When To Use

Use this skill for changes to:

- prompts, system instructions, memory, RAG, tool routing, workflows, schemas, eval sets, docs, or Codex skills
- agent feedback loops, trace formats, release gates, and rollback policies
- public skill packages that need lighter entrypoints, clearer references, validation, and versionable change discipline

Do not use it to justify uncontrolled model-weight changes, silent long-term memory writes, unapproved global skill installation, or production-impacting behavior without a Human Gate.

## Quick Workflow

1. Define the current task and the system layer being changed: `prompt`, `memory`, `RAG`, `tool routing`, `workflow`, `eval`, `schema`, `docs`, or `skill`.
2. Before gathering more information, pass a VOI gate. Search, ask, read memory, or run experiments only when the information could change a key decision or lower high-impact risk.
3. Maintain a compact OODA state:
   - Observe: goal, context, evidence, surprising signals.
   - Orient: current frame, user model, domain model, uncertainty map.
   - Decide: chosen action, rejected actions, VOI reason.
   - Act: artifact, tool call, probe, or test.
   - Evaluate: result check, process check, failure signals.
4. Separate task OODA from meta OODA. The task loop completes today's work; the meta loop proposes candidate changes for tomorrow's system.
5. Keep every evolution change as `candidate` until evidence, evals, required approval, and rollback are present.
6. When editing a skill, keep `SKILL.md` light. Put detailed methods in this skill's own `references/` and reusable forms in `templates/`.

## Read As Needed

- Full VOI/OODA workflow and scoring rules: `references/evolution-loop-playbook.en.md` or `references/evolution-loop-playbook.zh-CN.md`.
- Eval, trace, versioning, promotion, and rollback rules: `references/eval-versioning-playbook.en.md` or `references/eval-versioning-playbook.zh-CN.md`.
- Reusable working forms:
  - default: `templates/evolution_proposal.md` and `templates/ooda_voi_state.md`
  - Chinese: `templates/evolution_proposal.zh-CN.md` and `templates/ooda_voi_state.zh-CN.md`
  - English: `templates/evolution_proposal.en.md` and `templates/ooda_voi_state.en.md`

## Human Gate Defaults

Ask for human confirmation before:

- writing long-term memory
- installing or replacing a global skill
- changing production strategy, release behavior, real accounts, money, or user-visible systems
- promoting generated content or workflow mutations from `candidate` to current rule
- deleting, mirroring, bulk-moving, or overwriting project workspaces

## Output Contract

End by stating:

- what changed
- why the evidence is sufficient
- which evals or checks ran
- what remains `candidate`
- what needs Human Gate
- how to rollback
