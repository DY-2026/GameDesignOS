<p align="center">
  <img src="./assets/demo-game-experience-before-after.png" alt="60-second demo: Game Experience Analyzer turns PV input into an evidence-linked report" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  A Paranoia-method skill system for game-design and agent-workflow production.
  Turn play evidence, concept seeds, workflow mutations, translations, and sources into verifiable operating models.
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#60-second-demo">60-Second Demo</a> ·
  <a href="#easy-start">Easy Start</a> ·
  <a href="#current-skills">Current Skills</a> ·
  <a href="#showcase">Showcase</a> ·
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/Skills-5-2ea44f">
  <img alt="Domain" src="https://img.shields.io/badge/Domain-Game%20Design-blue">
  <img alt="Agent Ready" src="https://img.shields.io/badge/Agent--Ready-Codex%20%7C%20Claude%20Code%20%7C%20OpenCode-6f42c1">
  <img alt="Method" src="https://img.shields.io/badge/Method-Paranoia%20Method-f9a825">
</p>

> License: skill documents and tooling are released under the MIT License. The Paranoia name, logos, visual identity, and project branding are not licensed as trademarks.

> ParanoiaSkills treats skill packages as operating models: compact mechanisms with evidence ledgers, cost gates, validation surfaces, and rollback paths.

## 60-Second Demo

Start with one screenshot, gameplay recording, trailer/PV, or video link. Ask the skill for an evidence-linked report:

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, feature exposure/unlock/first-use ledger, Hook/Loop/Link/Surprise diagnosis, and actionable fixes.
```

The strongest current case is [`《生存33天》41 分钟试玩录屏前期体验复盘示例`](./game-experience-analyzer/examples/survival-33-days-gameplay-experience-report.md): a public gameplay recording becomes a timestamped report with visual evidence, feature ledger, early-loop diagnosis, UI/guide risks, and validation-ready fixes.

## What This Is

`ParanoiaSkills` is a game-design and AI-agent workflow system built around the Paranoia Method: compress messy creative work into small operating models that can be invoked, checked, revised, and moved across tools.

Each skill is not a prompt recipe. It is a packaged mechanism with a lightweight entrypoint, deeper references, reusable templates, deterministic validators, and eval or rollback surfaces where the work needs them.

```text
raw play evidence -> design diagnosis with an evidence ledger
idea fragment -> playable promise, verbs, loop, and validation gate
workflow mutation -> candidate rule with cost/trust/eval/rollback gates
design text or source -> reusable knowledge asset
```

## Why Star This

- **Open and portable:** each skill is a readable, copyable, auditable Markdown package that does not lock your workflow into one product.
- **Evidence ledger, not cautious prose:** important claims are separated into verified facts, tool observations, inference judgments, assumptions, and human-confirmation items.
- **Concept-to-validation:** a promising idea is not treated as a GDD; it becomes a seed, a player promise, a core loop, a scope gate, and a prototype test.
- **Operating model first:** useful behavior is compressed into `SKILL.md`, `references/`, `templates/`, validators, and eval gates, not left as one lucky answer.
- **Game-design native:** built for experience, mechanics, MDA, systems narrative, genre strategy, market windows, monetization, and production workflows.
- **Agent portable:** not tied to one tool; Codex, Claude Code, OpenCode, or any Markdown-skill-capable agent can adapt it.
- **Paranoia evolution:** system changes move through cost checks, missing-alternative checks, shadow-first rollout, evals, Human Gate, and rollback.

## Easy Start

The simplest path is three small moves: pick a skill, give the agent your material, and ask for a reviewable output.

### 1. Pick the right skill

| What you have | Use this skill | What you get |
| --- | --- | --- |
| Screenshot, recording, PV/trailer, or video link | `$game-experience-analyzer` | A game experience report with timestamps, evidence, issue priorities, game dissection, mechanic transfer boundaries, and validation plans |
| One-line game idea | `$game-concept-architect` | Concept seed, player verbs, action-goal alignment, player promise, core loop, scope gate, and validation plan |
| Prompt, workflow, schema, or agent rule | `$paranoia-ai-system-evolver` | A Paranoia Method evolution proposal with operating model, evidence ledger, cost delta, alternative check, shadow rollout, eval, and rollback |
| English game design chapter or essay | `$game-design-book-translator` | Professional Chinese design translation with reviewable terminology |
| Articles, videos, creators, or websites | `$game-design-source-curator` | Maintainable game design knowledge-base entries |

### 2. Copy a minimal prompt

Call a skill directly in an agent environment that supports skill loading:

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, design lenses, heat potential, foresight windows, Go/No-Go, and validation recommendations.
```

```text
Use $game-experience-analyzer to dissect this game into player verbs, action-goal alignment, uncertainty sources, system dynamics, content flow, audience desire, transfer boundaries, and validation recommendations.
```

```text
Use $paranoia-ai-system-evolver to upgrade this prompt/workflow/schema through the Paranoia Method: map the operating model, compare total description cost, build an assertion evidence ledger, check missing alternatives, plan shadow-first rollout, evals, Human Gate, and rollback.
```

```text
Use $game-design-book-translator to translate and polish this game design chapter into professional Chinese, including terminology and figure captions.
```

```text
Use $game-design-source-curator to review these game design sources and turn accepted items into a maintainable local knowledge base.
```

```text
Use $game-concept-architect to turn this one-line game idea into a concept seed, player verbs, action-goal alignment, player promise, core loop, scope gate, production feasibility check, and prototype validation plan.
```

### 3. Install it in your own agent environment

If your tool supports local skills, copy the target folder into that tool's skill directory:

```text
game-experience-analyzer/
paranoia-ai-system-evolver/
game-design-book-translator/
game-design-source-curator/
game-concept-architect/
```

After installation, check that the `SKILL.md` frontmatter `name` matches the folder name, and that relative links inside `references/`, `templates/`, and `examples/` still resolve.

## Showcase

<table>
  <tr>
    <td width="20%">
      <img src="./assets/showcase-game-experience-analyzer.png" alt="Game Experience Analyzer showcase">
    </td>
    <td width="20%">
      <img src="./assets/showcase-voi-ooda.png" alt="Paranoia AI System Evolver showcase">
    </td>
    <td width="20%">
      <img src="./assets/showcase-book-translator.png" alt="Game Design Book Translator showcase">
    </td>
    <td width="20%">
      <img src="./assets/showcase-source-curator.png" alt="Game Design Source Curator showcase">
    </td>
    <td width="20%">
      <img src="./assets/showcase-game-concept-architect.png" alt="Game Concept Architect showcase">
    </td>
  </tr>
  <tr>
    <td><b>Analyze game experience</b><br>Convert screenshots, recordings, trailers, and video links into evidence-first diagnosis, game dissection, and mechanic-transfer judgment.</td>
    <td><b>Evolve workflows</b><br>Turn prompt, schema, memory, eval, and routing changes into candidate operating-model upgrades with cost, evidence, shadow, and rollback gates.</td>
    <td><b>Translate design knowledge</b><br>Transform serious game design books and chapters into professional Chinese design writing.</td>
    <td><b>Curate sources</b><br>Turn scattered articles, videos, creators, columns, and websites into a durable game design knowledge base.</td>
    <td><b>Architect game concepts</b><br>Turn a one-line idea into a seed, player verbs, action-goal alignment, player promise, core loop, scope gate, and validation plan.</td>
  </tr>
</table>

## Skill Architecture

`ParanoiaSkills` is organized into three operating layers. Public repository contains base skills. Private overlays should live outside this repository.

- **Design Production Layer**
  - [`game-concept-architect/`](./game-concept-architect/): one-line idea -> verifiable design blueprint.
  - [`game-experience-analyzer/`](./game-experience-analyzer/): media/sample -> evidence-linked diagnosis.
- **Workflow Governance Layer**
  - [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/): system changes -> Paranoia Method evolution gates.
- **Knowledge Asset Layer**
  - [`game-design-book-translator/`](./game-design-book-translator/): design texts -> professional Chinese design writing.
  - [`game-design-source-curator/`](./game-design-source-curator/): scattered sources -> durable knowledge base.

Users may still use these skills with real projects, private projects, client work, or synthetic cases in their own environment. The public-case rules apply only to content committed back to this repository.

## Current Skills

| Skill | One-line Use | Best For | Package |
| --- | --- | --- | --- |
| **Game Experience Analyzer** | Turns screenshots, gameplay recordings, trailers/PVs, and video links into evidence-first Chinese game design reports. | Early experience, mechanics, game dissection, mechanic transfer, holistic product analysis, MDA, systems-narrative fusion, single-player flow, genre strategy, heat prediction, foresight windows, monetization, UX. | [`game-experience-analyzer/`](./game-experience-analyzer/) |
| **Paranoia AI System Evolver** | Turns prompt, workflow, memory, schema, tool-routing, and eval changes into Paranoia Method evolution proposals. | Operating model audit, total description cost, evidence ledger, missing-alternative check, subagent loss audit, shadow-first release, Human Gate, rollback. | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | Produces professional Chinese game design translations that read like serious design writing. | Terminology, chapters, figures, captions, tables, QA, source-boundary checks. | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | Converts scattered game design sources into a durable local knowledge base. | Source screening, scoring, HTML archives, registries, update history, design experiment cards. | [`game-design-source-curator/`](./game-design-source-curator/) |
| **Game Concept Architect** | Turns one-line game ideas into verifiable concept briefs with seed extraction, player verbs, action-goal alignment, player promises, core loops, scope gates, and prototype validation plans. | Indie game ideation, pitch shaping, external feasibility, platform/business fit, MVP/vertical slice planning, production constraints. | [`game-concept-architect/`](./game-concept-architect/) |

## Use Cases

- **Competitor experience review:** turn a gameplay recording into a timeline, feature ledger, loop diagnosis, issue priority, and concrete fixes.
- **Game dissection and mechanic transfer:** break a sample into player verbs, goal layers, uncertainty, system dynamics, content flow, audience desire, playable theme, and transfer boundaries.
- **Trailer heat prediction:** evaluate first seconds, one-line value proposition, proof of play, channel fit, conversion path, and validation plan.
- **Foresight opportunity:** judge whether a genre, theme, or mechanic still has a window; casual/light defaults to 1-3 months, micro/midcore-heavy defaults to 3-6 months.
- **Source curation:** turn articles, videos, creators, columns, and websites into searchable, citable, experiment-ready design knowledge.
- **Professional translation:** translate game design books or essays while preserving terminology, argument structure, and figure context.
- **Workflow evolution:** promote useful agent behavior into candidate operating-model changes with evidence, cost delta, shadow rollout, evals, Human Gate, and rollback.
- **Concept feasibility:** turn a one-line idea into concept seed extraction, player verbs, action-goal alignment, player promises, core loop design, scope gate, production feasibility, and prototype validation.

## Repository Layout

```text
ParanoiaSkills/
|-- README.md
|-- README.zh-CN.md
|-- README.en.md
|-- LICENSE
|-- CONTRIBUTING.md
|-- adapters/
|-- contracts/
|-- docs/
|-- .github/
|-- releases/
|-- scripts/
|-- assets/
|   |-- demo-game-experience-before-after.png
|   |-- voi-ooda-system-evolver-hero.png
|   |-- showcase-game-experience-analyzer.png
|   |-- showcase-voi-ooda.png
|   |-- showcase-book-translator.png
|   |-- showcase-source-curator.png
|   `-- showcase-game-concept-architect.png
|-- game-experience-analyzer/
|-- paranoia-ai-system-evolver/
|-- game-design-book-translator/
|-- game-design-source-curator/
`-- game-concept-architect/
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

## Validation

Run these commands from the repository root:

```text
python scripts/validate_repo.py
python scripts/validate_skill.py game-experience-analyzer
python scripts/validate_skill.py game-concept-architect
```

## License

Skill documents and tooling in this repository are released under the [MIT License](./LICENSE).

The Paranoia name, logos, visual identity, and project branding are not licensed as trademarks. Examples may have their own `source_status`, `case_type`, or source metadata; check each example's frontmatter before reuse.

## Package Conventions

Each skill is an independently installable package. Keep `SKILL.md` as the runtime entrypoint, put durable methods in `references/`, reusable forms in `templates/`, examples in `examples/`, and regression checks in `evals/`.

## Contributing

Public examples, evals, assets, showcases, and release notes must use synthetic, public, or explicitly cleared material. See [CONTRIBUTING.md](./CONTRIBUTING.md) before submitting repository-facing content.

## Design Principles

```text
Evidence ledger before opinion.
Operating model before prompt.
Feasibility before scope.
Alternatives before recommendation.
Shadow before enforcement.
Eval before promotion.
Rollback before confidence.
```

## Future Skills

Depending on feedback and maturity, future additions may include AI + indie game production packages such as:

- `indie-game-production-master`: full-cycle indie production from idea validation, GDD/Gates, prototyping, playtesting, AI asset pipelines, Steam/release strategy, and postmortem writeback.
- `godot-ai-game-production`: Godot + AI production covering project scaffolding, design truth, data contracts, asset pipelines, headless/keyshot validation, Demo/Release Gates, and engineering retrospectives.
