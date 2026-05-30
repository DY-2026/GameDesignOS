# Paranoia AI System Evolver

**Parent project:** [ParanoiaSkills](../README.en.md)

**Languages:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

This is one installable skill inside `ParanoiaSkills`. It owns the controlled AI system evolution capability; it is not the whole skill library.

## What This Skill Does

It helps an agent improve AI systems without turning one successful case into an uncontrolled permanent rule. It combines:

- Model compression: judge whether a prompt, skill, agent, workflow, or harness explains more real tasks with a shorter core model
- Causal mediators: break final outcomes into observable, intervenable, and verifiable intermediate links
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
Use $paranoia-ai-system-evolver to turn this AI workflow problem into a controlled evolution proposal with model compression, causal mediators, VOI, OODA, evals, Human Gate, and rollback.
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
