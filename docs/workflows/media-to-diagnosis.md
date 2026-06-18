# Workflow: Media to Diagnosis

## Purpose

Turn screenshots, a store page, PV, trailer, gameplay recording, or prototype capture into an evidence-linked diagnosis with an explicit sample boundary.

## Primary Skill

`$game-experience-analyzer`

## Inputs

One or more of:

- screenshot set;
- gameplay recording;
- PV or trailer;
- public video link;
- store page;
- prototype capture;
- existing player-promise contract.

## Workspace Reads

```text
01-concept/player-promise-contract.json
01-concept/validation-plan.json
02-evidence/
06-decisions/
```

A player-promise contract is useful but not mandatory. When present, diagnose promise fulfillment rather than inventing a new product promise.

## Workspace Writes

```text
02-evidence/source-boundary.md
02-evidence/evidence-index.json
02-evidence/timestamp-ledger.md
03-analysis/experience-report.md
03-analysis/issue-cards.json
05-experiments/ed-handoff.json
06-decisions/information-value-assessment.json
```

Only write `ed-handoff.json` when the diagnosed issue is suitable for experience-density experimentation.

## VOI Decision Gate

Do not analyze media merely because it is available. Declare the decision that the evidence should influence, such as issue priority, a proposed fix, player-promise revision, or the next validation test.

For each requested evidence pass, state:

- the current default action without more analysis;
- the uncertainty the sample can reduce;
- what observed signal would change the action;
- what the sample cannot prove;
- the cost of more extraction versus acting now.

When additional timestamps, screenshots, or sources will not change issue priority or the next action, stop the evidence pass. Preserve surprising and negative local evidence even when it conflicts with the current product narrative.

## Flow

```text
source and sample boundary
  -> observation capture
  -> timestamp or screenshot evidence
  -> feature exposure / unlock / first-use ledger
  -> diagnosis route
  -> issue cards
  -> supported and unsupported claims
  -> validation recommendation
  -> optional ED handoff
```

## Evidence Rules

- An observed UI state is not proof of player comprehension.
- A trailer is not proof of actual game feel.
- One recording is not proof of retention, conversion, revenue, or market sentiment.
- Separate observation from interpretation.
- Every high-confidence issue needs an evidence reference.
- List what the sample cannot support.

## Human Gate

The designer decides:

```text
accept_diagnosis
request_more_evidence
route_to_ed_experiment
revise_player_promise
stop
```

## Minimal Prompt

```text
Use $game-experience-analyzer to turn this material into a GameDesignOS evidence package.

Required outputs:
- sample boundary and unsupported claims;
- evidence index with timestamps or screenshot references;
- experience report;
- assignable issue cards;
- validation recommendation;
- ED handoff only when justified.

Save the outputs to 02-evidence/, 03-analysis/, and optionally 05-experiments/.
```

## Definition of Done

- source status and sample boundary are explicit;
- strong claims link to evidence;
- unsupported judgment scope is listed;
- issue cards distinguish symptom, interpretation, confidence, and proposed test;
- the next route is clear.
