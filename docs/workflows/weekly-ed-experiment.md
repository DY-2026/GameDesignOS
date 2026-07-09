# Workflow: Weekly Experience-Density Experiment

## Purpose

Turn a bounded retention, pacing, feedback, embodiment, atmosphere, cognitive-load, demo-completion, or return-session problem into a small, instrumented, rollbackable experiment.

## Primary Skill

`$game-experience-density-optimizer`

## Required Upstream Boundary

Prefer one or more of:

- `ed-handoff`;
- issue cards;
- playtest notes;
- telemetry snapshot;
- a clearly labeled synthetic or text-only hypothesis.

When an `ed-handoff` exists, do not repeat the full media evidence pass.

## Workspace Reads

```text
02-evidence/
03-analysis/issue-cards.json
05-experiments/ed-handoff.json
06-decisions/
```

## Workspace Writes

```text
05-experiments/weekly-experiment-plan.md
05-experiments/instrumentation.md
05-experiments/dashboard-fields.md
05-experiments/decision-rules.md
05-experiments/rollback-rules.md
06-decisions/information-value-assessment.json
06-decisions/decision-log.json
07-retrospectives/experiment-retrospective.md
```

## VOI Decision Gate

The experiment is an EVSI instrument, not a ritual. Define the decision it will unlock: which lever to ship, revise, observe, rollback, or kill.

Compare candidate playtest, telemetry, and A/B designs by:

- probability that results change the chosen variant;
- consequence of choosing the wrong lever;
- sample and implementation cost;
- delay before the result is usable;
- confounder and data-quality risk;
- reversibility of the production decision.

Choose the smallest design with positive net sample value. Every result range must map to a pre-registered action. Stop when the option ranking is stable, the sample/evidence gate is reached, marginal VOI falls below cost, or the weekly decision deadline arrives.

## Paranoia Checkpoint

Use `$paranoia-ai-system-evolver` as a governance pass before launch and after result review.

Required checkpoint output:

- `intent_work_order_ref`: the real outcome the experiment should change, not just the feature to tweak;
- `voi_gate_ref`: why this sample has positive EVSI after implementation, delay, attention, and contamination costs;
- `rjr_authority_ref`: what the experiment can automate versus what remains human residual judgment;
- `rollback_ref`: the exact rollback or kill trigger attached to each result range;
- `retrospective_ref`: post-test decision delta, failure signals, and candidate workflow learning.

## Flow

```text
evidence gate
  -> metric horizon
  -> ED diagnosis
  -> choose smallest output mode
  -> one primary lever per variant
  -> instrumentation
  -> pre-registered decision rules
  -> rollback gate
  -> run
  -> review and decide
  -> retrospective
```

## Operating Rules

- Classify the evidence gate before making claims.
- Do not automatically interpret boredom as insufficient stimulation.
- Diagnose with the smallest relevant set of `CLP`, `SF`, `EB`, `AR`, and `MD/min`.
- Each variant receives one primary lever.
- Define data-quality checks and negative gates before success metrics.
- Pre-register amplify, iterate, observe, rollback, and kill conditions.
- Reject dark patterns, misleading rewards, false countdowns, anxiety red dots, and pure numerical inflation.

## Human Gates

Before launch:

```text
approve_test
revise_test
reject_test
```

After results:

```text
amplify
iterate
observe
rollback
kill
```

Both decisions belong in `06-decisions/`.

## Minimal Prompt

```text
Use $game-experience-density-optimizer to consume this issue card or ED handoff and compile the smallest useful weekly experiment.

Required outputs:
- evidence gate and allowed/forbidden claims;
- metric horizon;
- ED diagnosis;
- variant matrix with one primary lever each;
- instrumentation and dashboard fields;
- pre-registered decision and rollback rules;
- Human Gate.

Write the artifacts to 05-experiments/ and the decision record to 06-decisions/.
```

## Definition of Done

- the experiment can run within the declared time and production limit;
- each variant changes one primary lever;
- telemetry can distinguish the hypothesis from obvious confounders;
- rollback is operational, not rhetorical;
- a post-test decision and retrospective path exist.
