<p align="center">
  <img src="./assets/paranoia-skills-overview-banner-v3.png" alt="ParanoiaSkills - interoperable game design agent operating system" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  A public base library of installable, verifiable, and portable agent skills for game-design production and AI workflow governance.
  Turn media evidence into diagnosis, concept seeds into validation contracts, experience-density problems into weekly experiments, and workflow changes into WOOP/VOI/OODA/eval-backed evolution.
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#what-this-is">What This Is</a> ·
  <a href="./docs/try-it-in-10-minutes.md">Try in 10 Minutes</a> ·
  <a href="#easy-start">Easy Start</a> ·
  <a href="#60-second-demo">60-Second Demo</a> ·
  <a href="#current-skills">Current Skills</a> ·
  <a href="#showcase">Showcase</a> ·
  <a href="#star-history">Star History</a> ·
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/Skills-6-2ea44f">
  <img alt="Domain" src="https://img.shields.io/badge/Domain-Game%20Design-blue">
  <img alt="Agent Ready" src="https://img.shields.io/badge/Agent--Ready-Codex%20%7C%20Claude%20Code%20%7C%20OpenCode-6f42c1">
  <img alt="Method" src="https://img.shields.io/badge/Method-Evidence%20%7C%20Contracts%20%7C%20Evals-f9a825">
</p>

> License: skill documents and tooling are released under the MIT License. The Paranoia name, logos, visual identity, and project branding are not licensed as trademarks.

> Think of it as a compact operating system for game designers and AI agents: not a prompt collection, but reusable evidence rules, cross-skill contracts, validation gates, rollback paths, and output templates packaged as skills.

## What This Is

`ParanoiaSkills` is a public base library for AI-assisted game design work. It turns game experience analysis, concept architecture, experience-density experiments, workflow evolution, professional translation, and source curation into reusable agent instructions, references, schemas, templates, examples, and evals.

It is not a prompt dump. It is closer to a compact operating system for serious game design work, with contracts that let skills hand work to each other instead of producing isolated prose:

```text
media evidence -> evidence index -> issue cards -> ED handoff -> weekly experiments
one-line idea -> player-promise contract -> validation plan -> later media diagnosis
workflow change -> WOOP Task Card -> VOI/OODA probe -> eval -> Human Gate -> rollback
books and sources -> structured knowledge assets -> better references for future work
```

## What Makes It Different

- **Evidence-first:** judgments point back to sources, screenshots, timestamps, sample evidence, or validation metrics.
- **Contract-driven:** concept briefs, evidence indexes, issue cards, ED handoffs, and validation plans can move across skills.
- **Concept-to-validation:** a promising idea becomes a seed, a player promise, a core loop, a scope gate, and a prototype test.
- **Workflow-governed:** useful behavior is written into `SKILL.md`, `references/`, `templates/`, evals, Human Gates, and rollback paths.
- **Agent portable:** Codex, Claude Code, OpenCode, or any Markdown-skill-capable agent can adapt the packages.
- **Public/private safe:** public examples stay synthetic, public, cleared, or marked `needs_review`; real projects stay in your own environment.

## Try It in 4 Prompts

```text
Use $game-experience-analyzer to diagnose this PV or gameplay recording into sample boundary, timestamped evidence, Hook/Loop/Link/Surprise diagnosis, issue cards, and validation recommendations.
```

```text
Use $game-concept-architect to turn this one-line game idea into concept seed extraction, design nucleus options, player promise contract, core loop, scope gate, and prototype validation plan.
```

```text
Use $paranoia-ai-system-evolver to upgrade this workflow with a WOOP Task Card, VOI, OODA, eval checks, Human Gate, and rollback.
```

```text
Use $game-experience-density-optimizer to turn this first-session retention, pacing, or experience density problem into an ED diagnosis, CLP/SF/EB/AR/MD-min levers, a weekly A/B plan, instrumentation, dashboard fields, decision rules, and rollback gates.
```

For the full onboarding path, see [Try It in 10 Minutes](./docs/try-it-in-10-minutes.md). Star this repo if you want more public game-analysis examples and portable agent-skill templates; more stars help prioritize better public demos, adapters, and reusable skill templates.

## 60-Second Demo

Start with one screenshot, gameplay recording, trailer/PV, or video link. Ask the skill for an evidence-linked report:

<p align="center">
  <img src="./assets/demo-game-experience-before-after.png" alt="60-second demo: Game Experience Analyzer turns PV input into an evidence-linked report" width="100%">
</p>

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, feature exposure/unlock/first-use ledger, Hook/Loop/Link/Surprise diagnosis, and actionable fixes.
```

The strongest current example is [`《生存33天》41 分钟试玩录屏前期体验复盘示例`](./game-experience-analyzer/examples/survival-33-days-gameplay-experience-report.md): a gameplay recording sample becomes a timestamped report with visual evidence, feature ledger, early-loop diagnosis, UI/guide risks, and validation-ready fixes. Its source status is marked `needs_review` before public-material promotion.

## Easy Start

The simplest path is three small moves: pick a skill, give the agent your material, and ask for a reviewable output.

### 1. Pick the right skill

| What you have | Use this skill | What you get |
| --- | --- | --- |
| Screenshot, recording, PV/trailer, or video link | `$game-experience-analyzer` | A game experience report with timestamps, evidence, issue priorities, game dissection, mechanic transfer boundaries, and validation plans |
| One-line game idea | `$game-concept-architect` | Concept seed, player verbs, action-goal alignment, player promise, core loop, scope gate, and validation plan |
| Prompt, workflow, schema, or agent rule | `$paranoia-ai-system-evolver` | A WOOP/VOI/OODA/eval/Human Gate/rollback-backed evolution proposal |
| English game design chapter or essay | `$game-design-book-translator` | Professional Chinese design translation with reviewable terminology |
| Articles, videos, creators, or websites | `$game-design-source-curator` | Maintainable game design knowledge-base entries |
| Retention, pacing, feedback, embodiment, atmosphere, or cognitive-load problem | `$game-experience-density-optimizer` | ED diagnosis, weekly A/B variants, instrumentation, dashboard fields, and rollback gates |

### 2. Copy a minimal prompt

Call a skill directly in an agent environment that supports skill loading:

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, design lenses, heat potential, foresight windows, Go/No-Go, and validation recommendations.
```

```text
Use $game-experience-analyzer to dissect this game into player verbs, action-goal alignment, uncertainty sources, system dynamics, content flow, audience desire, transfer boundaries, and validation recommendations.
```

```text
Use $paranoia-ai-system-evolver to upgrade this prompt/workflow/schema with a WOOP Task Card, VOI, OODA, evals, Human Gate, and rollback.
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

```text
Use $game-experience-density-optimizer to turn this first-session experience density problem into CLP/SF/EB/AR/MD-min diagnosis, rollbackable weekly variants, telemetry events, dashboard fields, and pre-registered decision rules.
```

### 3. Install it in your own agent environment

If your tool supports local skills, copy the target folder into that tool's skill directory:

```text
game-experience-analyzer/
paranoia-ai-system-evolver/
game-design-book-translator/
game-design-source-curator/
game-concept-architect/
game-experience-density-optimizer/
```

After installation, check that the `SKILL.md` frontmatter `name` matches the folder name, and that relative links inside `references/`, `templates/`, and `examples/` still resolve.

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
    <td><b>Analyze game experience</b><br>Convert screenshots, recordings, trailers, and video links into evidence-first diagnosis, game dissection, and mechanic-transfer judgment.</td>
    <td><b>Evolve workflows</b><br>Upgrade prompts, schemas, evals, memory, and tool routing through WOOP, VOI, OODA, gates, and rollback.</td>
    <td><b>Translate design knowledge</b><br>Transform serious game design books and chapters into professional Chinese design writing.</td>
    <td><b>Curate sources</b><br>Turn scattered articles, videos, creators, columns, and websites into a durable game design knowledge base.</td>
  </tr>
  <tr>
    <td width="25%">
      <img src="./assets/showcase-game-concept-architect.png" alt="Game Concept Architect showcase">
    </td>
    <td width="25%">
      <img src="./assets/showcase-game-experience-density-optimizer.png" alt="Game Experience Density Optimizer showcase">
    </td>
    <td width="25%"></td>
    <td width="25%"></td>
  </tr>
  <tr>
    <td><b>Architect game concepts</b><br>Turn a one-line idea into a seed, player verbs, action-goal alignment, player promise, core loop, scope gate, and validation plan.</td>
    <td><b>Optimize experience density</b><br>Turn retention, pacing, feedback, embodiment, atmosphere, and cognitive-load issues into weekly ED experiments.</td>
    <td></td>
    <td></td>
  </tr>
</table>

For the compact proof-path list, see the [showcase index](./docs/showcases/README.md).

## Skill Architecture

`ParanoiaSkills` is organized as a public base layer plus a contract layer. Private overlays, real project data, client examples, and local workflow rules should live outside this repository.

- **Design Production Layer**
  - [`game-concept-architect/`](./game-concept-architect/): one-line idea -> verifiable design blueprint.
  - [`game-experience-analyzer/`](./game-experience-analyzer/): media/sample -> evidence-linked diagnosis.
  - [`game-experience-density-optimizer/`](./game-experience-density-optimizer/): retention/pacing/feedback issue -> weekly ED experiment.
- **Workflow Governance Layer**
  - [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/): prompt/workflow/schema/eval changes -> controlled evolution.
- **Knowledge Asset Layer**
  - [`game-design-book-translator/`](./game-design-book-translator/): design texts -> professional Chinese design writing.
  - [`game-design-source-curator/`](./game-design-source-curator/): scattered sources -> durable knowledge base.
- **Contract Layer**
  - [`contracts/`](./contracts/): router rules and shared schemas for player promises, validation plans, evidence indexes, issue cards, and ED handoffs.

Users may still use these skills with real projects, private projects, client work, or synthetic cases in their own environment. The public-case rules apply only to content committed back to this repository.

## Current Skills

| Skill | One-line Use | Best For | Package |
| --- | --- | --- | --- |
| **Game Experience Analyzer** | Turns screenshots, gameplay recordings, trailers/PVs, and video links into evidence-first Chinese game design reports. | Early experience, mechanics, game dissection, mechanic transfer, holistic product analysis, MDA, systems-narrative fusion, single-player flow, genre strategy, heat prediction, foresight windows, monetization, UX. | [`game-experience-analyzer/`](./game-experience-analyzer/) |
| **Paranoia AI System Evolver** | Turns prompt, workflow, memory, schema, tool-routing, and eval changes into controlled system evolution. | WOOP Task Cards, VOI/OODA, model compression, causal mediators, Human Gate, rollback, validated upgrades. | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | Produces professional Chinese game design translations that read like serious design writing. | Terminology, chapters, figures, captions, tables, QA, source-boundary checks. | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | Converts scattered game design sources into a durable local knowledge base. | Source screening, scoring, HTML archives, registries, update history, design experiment cards. | [`game-design-source-curator/`](./game-design-source-curator/) |
| **Game Concept Architect** | Turns one-line game ideas into verifiable concept briefs with seed extraction, player verbs, action-goal alignment, player promises, core loops, scope gates, and prototype validation plans. | Indie game ideation, pitch shaping, external feasibility, platform/business fit, MVP/vertical slice planning, production constraints. | [`game-concept-architect/`](./game-concept-architect/) |
| **Game Experience Density Optimizer** | Turns experience density, retention, pacing, feedback, embodiment, atmosphere, and cognitive-load problems into weekly ED experiments. | First-session tuning, prototype feel, live-ops micro tests, A/B variants, telemetry dictionaries, dashboard specs, rollback gates. | [`game-experience-density-optimizer/`](./game-experience-density-optimizer/) |

## Use Cases

- **Competitor experience review:** turn a gameplay recording into a timeline, feature ledger, loop diagnosis, issue priority, and concrete fixes.
- **Game dissection and mechanic transfer:** break a sample into player verbs, goal layers, uncertainty, system dynamics, content flow, audience desire, playable theme, and transfer boundaries.
- **Trailer heat prediction:** evaluate first seconds, one-line value proposition, proof of play, channel fit, conversion path, and validation plan.
- **Foresight opportunity:** judge whether a genre, theme, or mechanic still has a window; casual/light defaults to 1-3 months, micro/midcore-heavy defaults to 3-6 months.
- **Source curation:** turn articles, videos, creators, columns, and websites into searchable, citable, experiment-ready design knowledge.
- **Professional translation:** translate game design books or essays while preserving terminology, argument structure, and figure context.
- **Workflow evolution:** promote useful agent behavior into candidate rules with evals, Human Gate, and rollback.
- **Cross-skill handoff:** move from concept promise to media diagnosis to ED experiment through shared contracts instead of rewriting context by hand.
- **Concept feasibility:** turn a one-line idea into concept seed extraction, player verbs, action-goal alignment, player promises, core loop design, scope gate, production feasibility, and prototype validation.
- **Experience density experiments:** turn first-session, pacing, feedback, embodiment, atmosphere, or cognitive-load issues into weekly ED experiments with metrics and rollback gates.

## Repository Layout

Read the repository as a set of installable skill packages plus supporting public infrastructure.

| Layer | Paths | Purpose |
| --- | --- | --- |
| Skill packages | `game-experience-analyzer/`, `game-concept-architect/`, `paranoia-ai-system-evolver/`, `game-design-book-translator/`, `game-design-source-curator/`, `game-experience-density-optimizer/` | Copyable agent skills. Each package carries its own runtime instructions, references, templates, examples, and evals. |
| Public onboarding | `README.md`, `README.zh-CN.md`, `README.en.md`, `docs/`, `releases/` | Explains what the project is, how to try it, showcase boundaries, release drafts, and public-facing docs. |
| Integration and contracts | `adapters/`, `contracts/`, `.github/`, `scripts/` | Adapter notes, shared schemas, router contracts, GitHub workflow/templates, behavior evals, and repository validation tools. |
| Governance and media | `CONTRIBUTING.md`, `LICENSE`, `assets/` | Contribution rules, license terms, and public README/showcase visuals. |

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
python scripts/validate_skill.py game-experience-density-optimizer
```

## Star History

<a href="https://star-history.com/#DY-2026/ParanoiaSkills&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=DY-2026/ParanoiaSkills&type=Date&theme=dark">
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=DY-2026/ParanoiaSkills&type=Date">
    <img alt="Star History Chart for DY-2026/ParanoiaSkills" src="https://api.star-history.com/svg?repos=DY-2026/ParanoiaSkills&type=Date">
  </picture>
</a>

## License

Skill documents and tooling in this repository are released under the [MIT License](./LICENSE).

The Paranoia name, logos, visual identity, and project branding are not licensed as trademarks. Examples may have their own `source_status`, `case_type`, or source metadata; check each example's frontmatter before reuse.

## Package Conventions

Each skill is an independently installable package. Keep `SKILL.md` as the runtime entrypoint, put durable methods in `references/`, reusable forms in `templates/`, examples in `examples/`, and regression checks in `evals/`.

## Contributing

Public examples, evals, assets, showcases, and release notes must use synthetic, public, or explicitly cleared material. See [CONTRIBUTING.md](./CONTRIBUTING.md) before submitting repository-facing content.

## Design Principles

```text
Evidence before opinion.
Feasibility before scope.
Workflow before one-off prompts.
VOI before research.
Eval before promotion.
Rollback before confidence.
```

## Future Skills

Depending on feedback and maturity, future additions may include AI + indie game production packages such as:

- `indie-game-production-master`: full-cycle indie production from idea validation, GDD/Gates, prototyping, playtesting, AI asset pipelines, Steam/release strategy, and postmortem writeback.
- `godot-ai-game-production`: Godot + AI production covering project scaffolding, design truth, data contracts, asset pipelines, headless/keyshot validation, Demo/Release Gates, and engineering retrospectives.
