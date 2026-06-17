# Contributing

`GameDesignOS` is a public game-design workflow system packaged as reusable skills. Contributions should improve the public base layer, not publish private project context.

## Runtime vs Repository Boundary

Skills in this repository may be used by users in their own environments with real projects, private projects, client work, public cases, or synthetic cases.

This contribution policy only governs material submitted to this public repository, including:

- `examples/`
- `assets/`
- showcases
- eval cases
- docs
- release notes
- fixtures and test prompts

It does not restrict how users use a skill privately.

## Allowed Repository Material

Repository examples, assets, showcases, and evals may use only:

| Source Type | Allowed When |
| --- | --- |
| `synthetic_case` | Created for this repository and not derived from private work |
| `public_material` | The public source boundary is clear and no private context is added |
| `cleared_material` | The contributor has explicit permission and the material is sanitized |

When unsure, use a synthetic case.

## Forbidden Repository Material

Do not submit:

- Real project codenames, internal project names, unreleased titles, or client identifiers.
- Unreleased theme/mechanic combinations that could identify a real project.
- Client materials, contractor materials, publisher materials, investor materials, roadmaps, budgets, schedules, pitch decks, or internal reviews.
- Private platform strategy, channel strategy, launch strategy, store strategy, monetization assumptions, economy assumptions, retention assumptions, KPI targets, or business-model assumptions.
- Local paths, private workspace layouts, raw logs, screenshots, recordings, manifests, spreadsheets, archives, transcripts, or tool output from private work.
- Any detail that lets a reader infer the real project, team, client, market target, launch plan, monetization plan, data source, roadmap, or private workflow.

## Contribution Metadata

For public-facing examples, eval cases, showcase assets, or docs that describe a case, include or be able to answer:

| Field | Allowed Values |
| --- | --- |
| `source_type` | `synthetic_case` / `public_material` / `cleared_material` |
| `output_destination` | `repo_example` / `showcase` / `eval_case` / `docs` |
| `clearance_status` | `not_needed_synthetic` / `public_source_checked` / `explicitly_cleared` |
| `redaction_required` | `true` / `false` |
| `private_inference_risk` | `low` / `medium` / `high` |

## Skill Package Conventions

Each skill folder should remain focused on one installable skill:

- Keep `SKILL.md` lightweight: trigger conditions, core workflow, boundaries, and read-as-needed paths.
- Put durable methodology, scoring rules, routers, and gates in `references/`.
- Put reusable working forms and output structures in `templates/`.
- Put public examples in `examples/` and regression prompts in `evals/`.
- Keep `SKILL.md` frontmatter `name`, the folder name, and `agents/openai.yaml` aligned.

For changes to `SKILL.md`, `references/`, `templates/`, schemas, routers, evals, or adapter prompts, include an evolution proposal based on `paranoia-ai-system-evolver/templates/evolution_proposal.md` or an equivalent PR note. It should state why the change is needed, which skills or contracts are affected, which evals/checks ran, what remains candidate, and how to roll back.

## Session Context Boundary

Commands, temporary Codex instructions, execution details, preference corrections, and one-off context from a working session are not repository documentation by default.

Only add them to this public repository when they have been rewritten into reusable, public, verifiable project rules or when the user explicitly asks to preserve them as public project material.

If you maintain an installed runtime copy of a skill, keep it synchronized with the repository source and validate both copies before release.

## Minimal Safe Example

```markdown
source_type: synthetic_case
output_destination: repo_example
clearance_status: not_needed_synthetic
redaction_required: false
private_inference_risk: low

Case: A fictional greenhouse strategy game where mechanical plants change form based on care order.
Why safe: The case was created for this repository and is not derived from a real project.
```

## Quality Gate

Before submitting, verify:

- The contribution is synthetic, public, or explicitly cleared.
- All private identifiers, paths, budgets, dates, strategy details, and roadmap details are removed.
- A reader cannot infer a real project, client, team, launch plan, or private workflow.
- Examples and evals test reusable behavior, not private facts.
- Behavior assertions are runnable where possible with `scripts/run_behavior_evals.py` against captured outputs, and script tests pass with `python -m unittest discover -s scripts/tests`.
- Any private overlay, client work, unreleased project, or author-specific context stays outside this repository.

If the answer is unclear, do not submit the material.
