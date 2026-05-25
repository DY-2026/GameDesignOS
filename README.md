<p align="center">
  <img src="./assets/voi-ooda-system-evolver-hero.png" alt="ParanoiaSkills skill library hero" width="100%">
</p>

# ParanoiaSkills

**Languages:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

ParanoiaSkills is @Paranoia's public skill library: a collection of reusable, installable skills for Codex-style agents and AI workflows.

ParanoiaSkills 是 @Paranoia 的公开技能库，用来整体管理可复用、可安装的 Codex / Agent skills。

## Skill Catalog

| Skill | Purpose | Package |
| --- | --- | --- |
| VOI-OODA AI System Evolver | Controlled AI system evolution with VOI, OODA, evals, Human Gate, versioning, and rollback | [`voi-ooda-ai-system-evolver/`](./voi-ooda-ai-system-evolver/) |

## Repository Model

```text
ParanoiaSkills/
├── README.md                 # library-level entry and management rules
├── README.zh-CN.md
├── README.en.md
├── assets/                   # repository-level visual assets
└── voi-ooda-ai-system-evolver/
    ├── SKILL.md              # agent entrypoint for this specific skill
    ├── README.*.md           # human docs for this specific skill
    ├── references/           # detailed methodology, loaded as needed
    └── templates/            # copy-paste working forms
```

## Management Rule

The root README explains the whole library. Each skill folder explains one specific skill. New skills should be added as peer folders and registered in the catalog above.

Copyright (c) 2026 @Paranoia. All rights reserved.
