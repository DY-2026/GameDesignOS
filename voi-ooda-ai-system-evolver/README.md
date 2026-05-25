# VOI-OODA AI System Evolver Skill

> Copyright (c) 2026 @Paranoia. All rights reserved.

This folder is the installable Codex skill package. The repository root README is for humans; this package is for agents.

## What This Skill Does

It helps an agent improve AI systems without turning one successful case into an uncontrolled permanent rule. It combines:

- VOI: decide what information is worth acquiring
- OODA: keep a compact Observe / Orient / Decide / Act state
- Evals: test result quality, process quality, and evolution risk
- Human Gate: require approval for high-impact changes
- Rollback: keep every promoted change reversible

## Package Contents

```text
SKILL.md
agents/openai.yaml
references/evolution-loop-playbook.md
references/eval-versioning-playbook.md
templates/evolution_proposal.md
templates/ooda_voi_state.md
```

## Suggested Prompt

```text
使用 $voi-ooda-ai-system-evolver，把这个 AI workflow 问题整理成带 VOI、OODA、eval、Human Gate 和 rollback 的受控进化提案。
```

## Maintenance Rules

- Keep `SKILL.md` as the lightweight routing layer.
- Put durable methodology in `references/`.
- Put copy-paste working forms in `templates/`.
- Keep the frontmatter `name`, folder name, `agents/openai.yaml`, and public README naming aligned.
- Treat global installation, long-term memory writes, and production-impacting changes as Human Gate actions.
