# Workflow: Idea to Validation

## Purpose

Turn a rough game idea into a bounded, testable concept package without inflating it into a full GDD.

## Primary Skill

`$game-concept-architect`

## Inputs

Minimum input:

- one-line idea or rough concept seed.

Useful constraints:

- target player;
- intended platform;
- team size and available time;
- business model;
- must-have fantasy;
- known production risks.

## Workspace Reads

```text
00-inbox/
01-concept/
06-decisions/
```

Inspect existing concept notes and decisions before creating a parallel concept branch.

## Workspace Writes

```text
01-concept/concept-seed.md
01-concept/player-promise-contract.json
01-concept/core-loop.md
01-concept/scope-gate.md
01-concept/validation-plan.json
06-decisions/decision-brief.md
06-decisions/information-value-assessment.json
06-decisions/decision-log.json
```

## VOI Decision Gate

Before choosing what to prototype, write the decision:

```text
Which player promise, core-loop risk, or production assumption should receive the next prototype investment?
```

Record the current default action, real alternatives, deadline, stakes, and reversibility. Compare candidate information actions such as a paper prototype, concept test, focused interview, implementation spike, or reference check.

The selected validation must be the smallest sample that can change the prototype choice. A test that produces interesting feedback but cannot alter investment, scope, or kill criteria is model learning, not the primary decision probe.

Pre-register how supportive, contradictory, and ambiguous signals lead to `prototype`, `revise`, `hold`, or `reject`. Stop when the selected concept remains preferred across plausible signals, the evidence gate is reached, or the prototype deadline arrives.

## Paranoia Checkpoint

Use `$paranoia-ai-system-evolver` as a governance pass when the idea is vague, over-ambitious, or already drifting toward a full GDD.

Required checkpoint output:

- `intent_work_order_ref`: what reality the concept sprint should change, who verifies it, and what cannot be sacrificed;
- `voi_gate_ref`: the smallest concept or prototype signal that can change the next investment;
- `rjr_authority_ref`: which scope, budget, platform, or production calls remain human residual judgment;
- `rollback_ref`: the observable condition for shrinking, revising, or stopping the concept path;
- `candidate_learning_refs`: reusable rules learned from the concept pass, still marked candidate.

## Flow

```text
idea intake
  -> seed extraction
  -> player verbs
  -> action-goal alignment
  -> design nucleus options
  -> player promise
  -> core loop
  -> scope gate
  -> validation plan
  -> Human Gate
```

## Operating Rules

- Do not write a full GDD before the player promise and testable risk are clear.
- Mark facts, assumptions, preferences, and unresolved questions separately.
- The scope gate must describe what is deliberately excluded.
- The validation plan must target the highest-value uncertainty, not the easiest feature to prototype.
- A concept is not accepted merely because its prose is attractive.

## Human Gate

The designer decides one of:

```text
accept_for_prototype
revise_concept
hold_for_research
reject
```

Record the decision, evidence used, risks, and rollback or revisit trigger in `06-decisions/`.

## Minimal Prompt

```text
Use $game-concept-architect to turn this idea into a concept seed, design nucleus options, player-promise contract, core loop, scope gate, and prototype validation plan.

Project constraints:
- target player:
- platform:
- team/time:
- business model:
- non-negotiable fantasy:

Write the outputs as GameDesignOS workspace assets for 01-concept/ and end with a Human Gate for 06-decisions/.
```

## Definition of Done

- the player promise is explicit at external, first-session, and long-term levels;
- player verbs and goals align with the promise;
- the smallest prototype can falsify a named assumption;
- success, failure, next-investment, and kill conditions exist;
- the human decision is logged.
