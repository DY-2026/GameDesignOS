# Try It in 10 Minutes

This guide helps a new user understand and test `ParanoiaSkills` without adding private material to the public repository.

## Who This Project Is For

- Game designers who want evidence-linked diagnosis from screenshots, PVs, trailers, or gameplay recordings.
- Indie developers who want to turn a one-line idea into a testable concept blueprint.
- Agent-workflow builders who want portable Markdown skills with validation gates, not one-off prompts.
- Teams that want to use real projects privately while keeping public examples synthetic, public, or cleared.

## Which Skill To Choose

| Your input | Choose this skill | Main output |
| --- | --- | --- |
| PV, trailer, gameplay recording, screenshot, or video link | `$game-experience-analyzer` | Evidence index, diagnosis route, issue cards, validation plan |
| One-line game idea | `$game-concept-architect` | Concept seed, player promise, core loop, scope gate, validation plan |
| Prompt, workflow, schema, eval, memory, or agent rule | `$paranoia-ai-system-evolver` | VOI/OODA evolution proposal with Human Gate and rollback |

## Which Folder To Copy

Copy only the skill folder you want to try into your agent's local skill directory:

```text
game-experience-analyzer/
game-concept-architect/
paranoia-ai-system-evolver/
```

For a first test, copy one folder only. After copying, confirm that `SKILL.md`, `references/`, `templates/`, and `examples/` are still in the same relative layout.

## How To Trigger `$game-experience-analyzer`

Use this when you have public, synthetic, or private-in-your-own-environment media. Do not submit private media back to this public repository.

```text
Use $game-experience-analyzer to analyze this gameplay recording or PV into timestamped evidence, sample boundary, diagnosis route, Hook/Loop/Link/Surprise diagnosis, issue cards, and validation recommendations.

Input material:
- Source: <public link, local private file, or synthetic sample>
- Sample type: PV / trailer / gameplay recording / screenshot set
- What I want to learn: <early hook, core loop clarity, UX risk, conversion risk, mechanic-transfer boundary>
```

## How To Trigger `$game-concept-architect`

Use this when you have a rough idea and need a verifiable design blueprint.

```text
Use $game-concept-architect to turn this one-line idea into concept seed extraction, design nucleus options, player promise contract, core loop, scope gate, production feasibility check, and prototype validation plan.

Idea:
A short tactics game about repairing a drifting lighthouse while storms change the map every night.
```

## Minimal Input Examples

### PV Or Recording Diagnosis

```text
Use $game-experience-analyzer on this public gameplay recording:
<link>

Please focus on the first 3 minutes, visible player verbs, feature exposure, UI density, and what claims are unsupported by this sample.
```

### One-Line Concept Architecture

```text
Use $game-concept-architect:
One-line idea: A cozy roguelite shop game where every item sold changes the town's future problems.
```

### Workflow Evolution

```text
Use $paranoia-ai-system-evolver to upgrade this agent workflow:
When asked for game analysis, first gather evidence, then write conclusions.

Please add VOI, OODA, eval checks, Human Gate, and rollback criteria.
```

## Expected Output Structure

`$game-experience-analyzer` should usually return:

- Sample boundary and unsupported judgment scope.
- Evidence index with timestamps, screenshots, observed facts, and confidence.
- Diagnosis route or diagnosis pack selection.
- Issue cards with severity, evidence, interpretation, and proposed fix.
- Validation plan that names what would prove or disprove the diagnosis.

`$game-concept-architect` should usually return:

- Concept seed extraction.
- Assumption ledger.
- Design nucleus options.
- Player promise contract.
- Core loop and player verbs.
- Scope or production feasibility gate.
- Prototype validation plan.

`$paranoia-ai-system-evolver` should usually return:

- Current workflow diagnosis.
- Proposed candidate change.
- VOI decision and OODA loop.
- Eval or regression checks.
- Human Gate requirements.
- Rollback plan.

## How To Check The Output Did Not Go Out Of Bounds

Ask these checks before trusting or publishing an output:

- Does every strong claim point to evidence, a timestamp, a screenshot, a source, or a named assumption?
- Does the output list what the sample cannot prove?
- Does it avoid claiming real retention, revenue, conversion, player sentiment, or market performance unless that data was provided?
- Does it label private, synthetic, public, and cleared material correctly?
- Does it avoid leaking local paths, client names, unreleased project plans, budgets, roadmaps, or private overlays?
- Does it include a validation plan instead of treating diagnosis as final truth?

## How To Run Repository Validation

From the repository root:

```text
python scripts/validate_repo.py
```

For targeted checks:

```text
python scripts/validate_skill.py game-experience-analyzer
python scripts/validate_skill.py game-concept-architect
python scripts/validate_skill.py paranoia-ai-system-evolver
```

## How To Avoid Publishing Private Overlay Or Real Project Cases

- Use real projects only in your own private environment.
- Keep private overlays outside this repository.
- Do not commit client work, unreleased roadmaps, internal strategy, local workspace outputs, private screenshots, private recordings, or private examples.
- Public repository examples must be `synthetic`, `public`, or `cleared`.
- If source status is unclear, mark it `needs_review` and do not publish it as a public example.
- Before opening a PR or issue, remove private identifiers, local paths, budgets, dates, launch plans, and any detail that lets readers infer the real project.
