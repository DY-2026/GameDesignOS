# Workflow: Evidence to Proposal

## Purpose

Assemble existing concept, evidence, validation, experiment, market/source, and production assets into a decision-ready proposal without fabricating missing upstream work.

## Primary Skill

`$game-design-proposal-writer`

## Inputs

Useful upstream assets:

- concept seed and player-promise contract;
- validation plan and scope gate;
- evidence index and issue cards;
- ED experiment or results;
- source notes and market references;
- production constraints;
- business goal and intended decision maker.

## Workspace Reads

```text
01-concept/
02-evidence/
03-analysis/
05-experiments/
06-decisions/
```

## Workspace Writes

Depending on requested mode:

```text
04-proposals/one-page-decision-memo.md
04-proposals/indie-design-dossier.md
04-proposals/publisher-pitch-outline.md
04-proposals/vertical-slice-plan.md
06-decisions/milestone-gate.md
06-decisions/information-value-assessment.json
06-decisions/decision-log.json
```

## VOI Decision Gate

A missing section is not automatically a reason for more research. First define the proposal decision: Go/No-Go, milestone approval, scope, budget, publisher interest, or a requested commitment.

For each missing upstream artifact, ask whether a plausible result would change the decision request, project scope, investment, or risk treatment. If not, label it as optional model learning and do not block the proposal.

Prioritize local production constraints, negative test results, unresolved kill conditions, and evidence that could reverse the recommendation. Stop when the proposal is decision-sufficient, not when it is encyclopedic.

## Paranoia Checkpoint

Use `$paranoia-ai-system-evolver` as a governance pass before proposal finalization, especially when the proposal asks for budget, scope, publishing, staffing, or milestone commitment.

Required checkpoint output:

- `intent_work_order_ref`: what outside-world decision or confidence state the proposal must change;
- `decision_ref`: the explicit decision request and current default action without the proposal;
- `rjr_authority_ref`: which recommendation remains human residual judgment rather than agent synthesis;
- `paranoia_review_ref`: missing upstream assets, unsupported claims, and evidence that could reverse the recommendation;
- `human_gate_refs`: approval, rejection, revise-scope, or request-more-evidence outcomes;
- `rollback_ref`: milestone, budget, or scope condition that reverses the recommendation.

## Flow

```text
decision request
  -> asset inventory
  -> missing-upstream check
  -> proposal mode selection
  -> proof of play
  -> scope and production feasibility
  -> commercial or platform assumptions
  -> risks and unknowns
  -> explicit decision request
  -> Human Gate
```

## Operating Rules

- Do not override upstream diagnosis or invent evidence.
- If a critical concept, evidence, validation, ED, source, or production asset is missing, identify the smallest missing upstream artifact.
- Separate verified facts, project assumptions, estimates, and unresolved questions.
- A pitch should make the decision easier, not hide uncertainty.
- Budget, schedule, retention, conversion, and revenue claims require provided data or explicit assumption labels.

## Human Gate

Possible outcomes:

```text
approve_next_milestone
approve_with_conditions
request_missing_evidence
revise_scope
reject
```

## Minimal Prompt

```text
Use $game-design-proposal-writer to assemble the available GameDesignOS workspace assets into a decision-ready proposal.

Decision audience:
Decision requested:
Available assets:
Production constraints:
Unknowns:

First identify missing upstream artifacts. Do not invent them. Write the selected proposal mode to 04-proposals/ and the resulting Human Gate to 06-decisions/.
```

## Definition of Done

- the document names its audience and requested decision;
- claims are traceable to assets or labeled assumptions;
- proof of play, scope, constraints, risks, and unknowns are visible;
- the next milestone has acceptance and stop conditions;
- the human decision is logged.
