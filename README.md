<p align="center">
  <img src="./assets/voi-ooda-system-evolver-hero.png" alt="ParanoiaSkills game design workflow hero" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  Paranoia's game design skill library for Claude Code, Codex, OpenCode, and agent CLI workflows.
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#current-skills">Current Skills</a> ·
  <a href="#showcase">Showcase</a> ·
  <a href="#future-skills">Future Skills</a>
</p>

<p align="center">
  Copyright (c) 2026 @Paranoia. All rights reserved.
</p>

ParanoiaSkills is an open skill library that turns game design reading, translation, source curation, and AI workflow evolution into reusable operating methods.

It is not tied to one tool. The skills are written as portable agent instructions and working templates, so they can be adapted for Claude Code, Codex, OpenCode, or any agent CLI that can load Markdown-based skills, prompts, references, and templates.

Most AI workflows stop at a good answer. ParanoiaSkills is built for the harder second step: turning that answer into a repeatable skill, a maintainable knowledge asset, and a process that can improve without drifting out of control.

The ambition is straightforward: make this one of the most useful GitHub projects for game designers, design researchers, and AI-assisted creators who want durable methods instead of one-off prompts.

It is also designed to grow with the community. As the repository earns more attention, ParanoiaSkills will keep adding better, more mature game design skills, turning a personal method library into shared infrastructure for game design work.

## What This Is

This is Paranoia's game design library: a set of reusable skills for game design reading, translation, source curation, and AI-assisted workflows.

Each package is an installable skill with its own agent entrypoint, human documentation, method references, templates, and validation boundaries. The library is designed for people who care about game design as a craft: source quality, terminology, evidence, iteration, rollback, and practical reuse.

## Showcase

<table>
  <tr>
    <td width="33%">
      <img src="./assets/showcase-source-curator.png" alt="Game Design Source Curator showcase">
    </td>
    <td width="33%">
      <img src="./assets/showcase-book-translator.png" alt="Game Design Book Translator showcase">
    </td>
    <td width="33%">
      <img src="./assets/showcase-voi-ooda.png" alt="Paranoia AI System Evolver showcase">
    </td>
  </tr>
  <tr>
    <td><b>Curate sources</b><br>Turn scattered articles, videos, creators, columns, and websites into a durable game design knowledge base.</td>
    <td><b>Translate design knowledge</b><br>Transform serious game design books and chapters into professional Chinese design writing.</td>
    <td><b>Evolve workflows</b><br>Upgrade prompts, schemas, evals, memory, and tool routing through VOI, OODA, gates, and rollback.</td>
  </tr>
</table>

## Current Skills

| Skill | Why it matters | Package |
| --- | --- | --- |
| **Paranoia AI System Evolver** | Turns prompt, workflow, memory, schema, RAG, tool routing, and eval changes into controlled system evolution. It uses model compression and causal mediators to find control points, keeps the agent oriented with VOI/OODA, gates risky changes through humans, and makes upgrades reversible. | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | Produces professional Chinese game design translations that read like serious design writing, not machine translation. It handles terminology, chapters, figures, captions, tables, QA, and source-boundary checks. | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | Converts scattered articles, videos, creators, columns, and websites into a living game design knowledge base. It uses evidence gates, scoring, HTML archives, registries, update history, and design experiment cards. | [`game-design-source-curator/`](./game-design-source-curator/) |

Together, these skills cover a full loop:

```text
Find high-quality sources
-> translate and structure design knowledge
-> connect it to methods, projects, and experiments
-> upgrade the agent workflow that performs the work
-> validate, version, and rollback when needed
```

## Why Game Designers Might Care

Game design knowledge is messy. The best ideas are scattered across books, talks, postmortems, forums, internal notes, videos, and half-remembered production lessons. Ordinary AI summaries flatten that mess too quickly.

ParanoiaSkills is built for the slower, more valuable version of the work:

- **From links to knowledge:** sources are screened, scored, archived, and connected to concrete design use.
- **From translation to design literacy:** translated material keeps the argument, terminology, diagrams, and production context intact.
- **From prompt success to workflow memory:** useful agent behavior becomes a candidate method only after evidence, evals, and rollback paths exist.
- **From personal notes to reusable infrastructure:** templates, references, and package boundaries make the work portable.

## How It Works

Each skill keeps a lightweight `SKILL.md` as the agent-facing entrypoint. Long-form methods live in `references/`, reusable forms live in `templates/`, and tool-specific metadata lives in `agents/`.

```text
SKILL.md      -> when to use the skill, boundaries, and the quick workflow
references/  -> deeper methods, gates, scoring rules, and validation playbooks
templates/   -> copy-paste working forms for real projects
agents/      -> metadata for agent environments that support it
```

## Prompt Examples

```text
Use $game-design-source-curator to review these game design sources and turn accepted items into a maintainable local knowledge base.
```

```text
Use $game-design-book-translator to translate and polish this game design chapter into professional Chinese, including terminology and figure captions.
```

```text
Use $paranoia-ai-system-evolver to turn this AI workflow problem into a controlled evolution proposal with model compression, causal mediators, VOI, OODA, evals, Human Gate, and rollback.
```

## Future Skills

Depending on community feedback and skill maturity, future additions may include AI + indie game production packages such as:

- `indie-game-production-master`: a full-cycle indie production skill covering idea validation, GDD/Gates, prototyping, playtesting, AI asset pipelines, Steam/release strategy, and postmortem writeback.
- `godot-ai-game-production`: a Godot + AI production skill covering project scaffolding, design truth, data contracts, asset pipelines, headless/keyshot validation, Demo/Release Gates, and engineering retrospectives.

## Repository Model

```text
ParanoiaSkills/
|-- README.md
|-- README.zh-CN.md
|-- README.en.md
|-- assets/
|   |-- voi-ooda-system-evolver-hero.png
|   |-- showcase-source-curator.png
|   |-- showcase-book-translator.png
|   `-- showcase-voi-ooda.png
|-- game-design-book-translator/
|-- game-design-source-curator/
`-- paranoia-ai-system-evolver/
```

## Maintenance Rules

- Keep the root README focused on the whole `ParanoiaSkills` library.
- Keep each skill folder responsible for one installable skill.
- Keep `SKILL.md` lightweight: trigger conditions, core workflow, boundaries, and read-as-needed paths.
- Put durable methodology in `references/`.
- Put reusable working forms in `templates/`.
- Keep `SKILL.md` frontmatter `name`, folder name, and `agents/openai.yaml` aligned.
- If a runtime copy under `C:\Users\Admin\.codex\skills` changes later, sync it back to the matching project folder and validate both copies.

## Copyright

Copyright (c) 2026 @Paranoia. All rights reserved.
