<p align="center">
  <img src="./assets/voi-ooda-system-evolver-hero.png" alt="ParanoiaSkills game design workflow hero" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  Reusable agent skills for game design, design research, and AI-assisted creative workflows.
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#current-skills">Current Skills</a> ·
  <a href="#showcase">Showcase</a> ·
  <a href="#governance">Governance</a>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/Skills-4-2ea44f">
  <img alt="Domain" src="https://img.shields.io/badge/Domain-Game%20Design-blue">
  <img alt="Agent Ready" src="https://img.shields.io/badge/Agent--Ready-Codex%20%7C%20Claude%20Code%20%7C%20OpenCode-6f42c1">
  <img alt="Method" src="https://img.shields.io/badge/Method-Evidence%20%7C%20VOI%20%7C%20OODA-f9a825">
</p>

> Copyright (c) 2026 @Paranoia. All rights reserved.

## What This Is

`ParanoiaSkills` is a game-design skill library that turns game experience analysis, AI workflow evolution, professional translation, and source curation into reusable agent instructions, references, templates, and examples.

It is not a prompt dump. It is closer to a compact operating system for serious game design work:

```text
Analyze screenshots, recordings, trailers, and video links
-> evolve the agent workflow that performs the work
-> translate and structure design knowledge
-> curate high-quality sources into reusable knowledge
```

## Why Star This

- **Evidence-first:** judgments should point back to sources, screenshots, timestamps, sample evidence, or validation metrics.
- **Workflow-first:** useful behavior is written into `SKILL.md`, `references/`, and `templates/`, not left as one lucky answer.
- **Game-design native:** built for experience, mechanics, MDA, systems narrative, genre strategy, market windows, monetization, and production workflows.
- **Agent portable:** not tied to one tool; Codex, Claude Code, OpenCode, or any Markdown-skill-capable agent can adapt it.
- **Controlled evolution:** VOI, OODA, evals, Human Gate, and rollback keep workflows from drifting out of control.

## Quick Start

Call a skill directly in an agent environment that supports skill loading:

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, design lenses, heat potential, foresight windows, Go/No-Go, and validation recommendations.
```

```text
Use $paranoia-ai-system-evolver to upgrade this prompt/workflow/schema with VOI, OODA, evals, Human Gate, and rollback.
```

```text
Use $game-design-book-translator to translate and polish this game design chapter into professional Chinese, including terminology and figure captions.
```

```text
Use $game-design-source-curator to review these game design sources and turn accepted items into a maintainable local knowledge base.
```

## Showcase

<table>
  <tr>
    <td width="25%">
      <img src="./assets/showcase-game-experience-analyzer.png" alt="Game Experience Analyzer showcase">
    </td>
    <td width="25%">
      <img src="./assets/showcase-voi-ooda.png" alt="Paranoia AI System Evolver showcase">
    </td>
    <td width="25%">
      <img src="./assets/showcase-book-translator.png" alt="Game Design Book Translator showcase">
    </td>
    <td width="25%">
      <img src="./assets/showcase-source-curator.png" alt="Game Design Source Curator showcase">
    </td>
  </tr>
  <tr>
    <td><b>Analyze game experience</b><br>Convert screenshots, recordings, trailers, and video links into evidence-first game design reports.</td>
    <td><b>Evolve workflows</b><br>Upgrade prompts, schemas, evals, memory, and tool routing through VOI, OODA, gates, and rollback.</td>
    <td><b>Translate design knowledge</b><br>Transform serious game design books and chapters into professional Chinese design writing.</td>
    <td><b>Curate sources</b><br>Turn scattered articles, videos, creators, columns, and websites into a durable game design knowledge base.</td>
  </tr>
</table>

## Current Skills

| Skill | One-line Use | Best For | Package |
| --- | --- | --- | --- |
| **Game Experience Analyzer** | Turns screenshots, gameplay recordings, trailers/PVs, and video links into evidence-first Chinese game design reports. | Early experience, mechanics, holistic product analysis, MDA, systems-narrative fusion, single-player flow, genre strategy, heat prediction, foresight windows, monetization, UX. | [`game-experience-analyzer/`](./game-experience-analyzer/) |
| **Paranoia AI System Evolver** | Turns prompt, workflow, memory, schema, tool-routing, and eval changes into controlled system evolution. | VOI/OODA, model compression, causal mediators, Human Gate, rollback, validated upgrades. | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | Produces professional Chinese game design translations that read like serious design writing. | Terminology, chapters, figures, captions, tables, QA, source-boundary checks. | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | Converts scattered game design sources into a durable local knowledge base. | Source screening, scoring, HTML archives, registries, update history, design experiment cards. | [`game-design-source-curator/`](./game-design-source-curator/) |

## Use Cases

- **Competitor experience review:** turn a gameplay recording into a timeline, feature ledger, loop diagnosis, issue priority, and concrete fixes.
- **Trailer heat prediction:** evaluate first seconds, one-line value proposition, proof of play, channel fit, conversion path, and validation plan.
- **Foresight opportunity:** judge whether a genre, theme, or mechanic still has a window; casual/light defaults to 1-3 months, micro/midcore-heavy defaults to 3-6 months.
- **Source curation:** turn articles, videos, creators, columns, and websites into searchable, citable, experiment-ready design knowledge.
- **Professional translation:** translate game design books or essays while preserving terminology, argument structure, and figure context.
- **Workflow evolution:** promote useful agent behavior into candidate rules with evals, Human Gate, and rollback.

## Repository Layout

```text
ParanoiaSkills/
|-- README.md
|-- README.zh-CN.md
|-- README.en.md
|-- assets/
|   |-- voi-ooda-system-evolver-hero.png
|   |-- showcase-game-experience-analyzer.png
|   |-- showcase-voi-ooda.png
|   |-- showcase-book-translator.png
|   `-- showcase-source-curator.png
|-- game-experience-analyzer/
|-- paranoia-ai-system-evolver/
|-- game-design-book-translator/
`-- game-design-source-curator/
```

Most skills follow this structure:

```text
SKILL.md      -> agent entrypoint, triggers, workflow, boundaries
references/  -> methods, scoring rules, routers, gates, validation playbooks
templates/   -> reusable forms and output structures
examples/    -> reviewable example outputs
agents/      -> metadata for agent environments that support it
evals/       -> regression prompts and expected behavior
```

## Install And Use

These packages are portable skill folders. A typical setup:

1. Copy or sync a skill folder into your agent skill directory.
2. Confirm the `SKILL.md` frontmatter `name` matches the folder name.
3. Trigger the skill by `$skill-name` or natural language.
4. Validate JSON/YAML, reference paths, and examples according to the skill README or `SKILL.md`.

## Governance

- Keep the root README focused on the whole `ParanoiaSkills` library: positioning, packages, structure, use cases, and governance.
- Keep each skill folder responsible for one installable skill.
- Separate session commands from project rules: temporary Codex instructions, execution commands, preference corrections, and one-off context from a working conversation are not automatically written into this public project. Only reusable, public, verifiable rules, or content the user explicitly asks to preserve, should enter README, SKILL, references, templates, or examples.
- Keep `SKILL.md` lightweight: trigger conditions, core workflow, boundaries, and read-as-needed paths.
- Put durable methodology in `references/`.
- Put reusable working forms in `templates/`.
- Keep `SKILL.md` frontmatter `name`, folder name, and `agents/openai.yaml` aligned.
- If a runtime copy changes later, sync it back to the matching project folder and validate both copies.

## Design Principles

```text
Evidence before opinion.
Workflow before one-off prompts.
VOI before research.
Eval before promotion.
Rollback before confidence.
```

## Future Skills

Depending on feedback and maturity, future additions may include AI + indie game production packages such as:

- `indie-game-production-master`: full-cycle indie production from idea validation, GDD/Gates, prototyping, playtesting, AI asset pipelines, Steam/release strategy, and postmortem writeback.
- `godot-ai-game-production`: Godot + AI production covering project scaffolding, design truth, data contracts, asset pipelines, headless/keyshot validation, Demo/Release Gates, and engineering retrospectives.

## Copyright

Copyright (c) 2026 @Paranoia. All rights reserved.
