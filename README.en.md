<p align="center">
  <img src="./assets/voi-ooda-system-evolver-hero.png" alt="ParanoiaSkills skill library hero" width="100%">
</p>

# ParanoiaSkills

**Languages:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

ParanoiaSkills is @Paranoia's public skill library for managing reusable, installable Codex / agent skills as one coherent collection.

The goal is not to make one huge skill. The goal is to manage many focused skills with clear boundaries:

```text
Root README: explains the whole ParanoiaSkills library.
Each skill folder: explains one installable skill.
SKILL.md: lightweight agent entrypoint.
references/: detailed methodology and rules loaded as needed.
templates/: copy-paste working forms.
```

## Skill Catalog

| Skill | Purpose | Package |
| --- | --- | --- |
| VOI-OODA AI System Evolver | Controlled AI system evolution with VOI, OODA, evals, Human Gate, versioning, and rollback | [`voi-ooda-ai-system-evolver/`](./voi-ooda-ai-system-evolver/) |

## Current Structure

```text
ParanoiaSkills/
├── README.md
├── README.zh-CN.md
├── README.en.md
├── assets/
│   └── voi-ooda-system-evolver-hero.png
└── voi-ooda-ai-system-evolver/
    ├── SKILL.md
    ├── README.md
    ├── README.zh-CN.md
    ├── README.en.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── evolution-loop-playbook.md
    │   ├── evolution-loop-playbook.zh-CN.md
    │   ├── evolution-loop-playbook.en.md
    │   ├── eval-versioning-playbook.md
    │   ├── eval-versioning-playbook.zh-CN.md
    │   └── eval-versioning-playbook.en.md
    └── templates/
        ├── evolution_proposal.md
        ├── evolution_proposal.zh-CN.md
        ├── evolution_proposal.en.md
        ├── ooda_voi_state.md
        ├── ooda_voi_state.zh-CN.md
        └── ooda_voi_state.en.md
```

## Library Management Rules

- The root README describes `ParanoiaSkills` as a whole: positioning, catalog, structure, and governance.
- Each skill's description, install prompt, methodology entrypoints, and examples live inside that skill's folder.
- Each skill's `SKILL.md` stays lightweight: trigger conditions, core workflow, and read-as-needed paths only.
- Long-form methodology belongs in `references/`; reusable working forms belong in `templates/`.
- Every new skill must be added to the root Skill Catalog.
- Every public skill should keep `README.md`, `README.zh-CN.md`, and `README.en.md`.
- `SKILL.md` frontmatter `name`, folder name, and `agents/openai.yaml` default prompt must stay aligned.

## Current Skill

### VOI-OODA AI System Evolver

Package: [`voi-ooda-ai-system-evolver/`](./voi-ooda-ai-system-evolver/)

Use it to upgrade AI systems, agent workflows, Codex skills, prompts, memory, RAG, tool routing, schemas, eval sets, or feedback loops. It focuses on:

- VOI: which information is worth acquiring.
- OODA: how to keep the map calibrated during real work.
- Evals: which changes deserve to remain.
- Human Gate: which actions require human confirmation.
- Rollback: how to make system upgrades reversible.

## Copyright

Copyright (c) 2026 @Paranoia. All rights reserved.
