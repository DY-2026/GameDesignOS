# GameDesignOS Contracts

`contracts/` defines stable artifact shapes and routing boundaries for GameDesignOS.

The goal is interoperability and decision continuity: skills pass structured artifacts to one another, a workspace preserves them as a connected record, and costly information actions are tied to a decision they may change.

## Three Contract Levels

### Skill-Level Contracts

Specialist workflows exchange player promises, validation plans, evidence indexes, issue cards, ED handoffs, and router selections.

### Decision / Information Contract

[`information-value-assessment.schema.json`](./information-value-assessment.schema.json) defines the cross-cutting VOI gate:

```text
Decision Object
-> current default action
-> boundary status
-> action-sensitive uncertainty
-> candidate information actions
-> signal-to-action mapping
-> EVPI / EVSI / total cost
-> selected smallest probe
-> stop rule
-> posterior and action update
```

This contract does not claim that every project can calculate exact monetary VOI. It requires the decision structure and cost boundary to be explicit so qualitative judgments remain reviewable.

### Workspace-Level Contracts

Workspace contracts organize specialist outputs inside a durable project:

- project manifest;
- design-asset index;
- information-value assessment;
- decision log.

They record where assets live, what they depend on, how they were created, whether a human accepted them, and when further information gathering should stop.

## Contract Flow

1. Read accepted project decisions and the current default action.
2. When more research, retrieval, memory, analysis, or experimentation is proposed, run the VOI gate.
3. If plausible signals cannot change action, act now, time-box model learning, or classify the activity as information consumption.
4. If net sample value is positive, select the smallest information probe and pre-register its signal-to-action mapping and stop rule.
5. `contracts/router.yaml` chooses the smallest suitable domain skill.
6. `game-concept-architect` exports a `player-promise-contract` and `validation-plan`.
7. `game-experience-analyzer` creates `evidence-index`, `issue-card`, and optional `ed-handoff` artifacts.
8. `game-experience-density-optimizer` consumes upstream evidence and compiles a bounded experiment without repeating the evidence pass.
9. `game-design-proposal-writer` assembles existing concept, validation, evidence, ED, source, market, and production assets.
10. A Human Gate records the commitment, reversal, or stop decision.
11. `paranoia-ai-system-evolver` audits system mutations and explicit VOI gates, then keeps changes candidate-gated until behavior eval, approval, and rollback exist.
12. Translation and source-curation skills remain knowledge-input layers.

## Default Production Path

```text
Decision Object
  -> VOI decision gate
  -> smallest probe or direct action
  -> game-concept-architect
  -> player-promise-contract / validation-plan
  -> game-experience-analyzer
  -> evidence-index / issue-card / ed-handoff
  -> game-experience-density-optimizer
  -> weekly experiment / instrumentation / decision rules
  -> game-design-proposal-writer
  -> proposal / pitch / decision memo / vertical-slice document
  -> Human Gate
  -> decision-log
  -> retrospective
```

The VOI gate is cross-cutting. It does not force every project through every skill.

## Routing Boundaries

| Situation | Route To | Stable Output |
| --- | --- | --- |
| Research impulse, FOMO, information overload, or uncertainty about what to test | explicit VOI audit, optionally via `paranoia-ai-system-evolver` | `information-value-assessment`, decision brief, stop rule |
| One-line idea, no core loop, no player promise | `game-concept-architect` | `player-promise-contract`, `validation-plan` |
| Screenshot, recording, PV, store page, prototype sample, or gameplay evidence request | `game-experience-analyzer` | `evidence-index`, `issue-card`, `ed-handoff` |
| Retention, pacing, feedback, embodiment, atmosphere, cognitive load, demo completion, return session, or habituation experiment | `game-experience-density-optimizer` | weekly ED experiment, instrumentation, dashboard, decision rules |
| Existing concept/evidence/ED/source/production artifacts need a formal proposal | `game-design-proposal-writer` | proposal, pitch, decision memo, vertical-slice document |
| Skill, schema, eval, router, workflow, promotion, rollback, or information-policy changes | `paranoia-ai-system-evolver` | evolution proposal, VOI decision gate, OODA state, eval plan |
| Design source ingestion or durable knowledge assets | `game-design-source-curator` | source notes, reference boundary, traceable knowledge entry |
| Design-book translation or polish | `game-design-book-translator` | translated or polished reference material |

`game-experience-density-optimizer` should not repeat the evidence pass when an `ed-handoff` exists.

`game-design-proposal-writer` should identify the smallest missing upstream artifact only when that artifact can change the proposal decision, scope, investment, or risk treatment. A missing section is not automatically high-VOI research.

## Workspace Collaboration Rules

A workspace-aware host should:

1. read `game.designos.yaml`;
2. inspect accepted decisions and their supersession chain;
3. declare the Decision Object and current default action before broad research;
4. classify the boundary as `undefined`, `far`, `near`, or `locked`;
5. generate no more than three candidate information actions per VOI round;
6. require signal-to-action mapping and an explicit stop rule;
7. resolve artifact paths through the design-asset index;
8. preserve local negative evidence and source boundaries;
9. save new artifacts to the documented lifecycle directory;
10. update upstream/downstream references, VOI outcome, and decision log;
11. stop at a Human Gate before changing project commitments.

The router coordinates only skills shipped inside this repository. Do not add external or global design-master skills to this graph.

## Schemas

### Skill-Level

- [`player-promise-contract.schema.json`](./player-promise-contract.schema.json)
- [`validation-plan.schema.json`](./validation-plan.schema.json)
- [`evidence-index.schema.json`](./evidence-index.schema.json)
- [`issue-card.schema.json`](./issue-card.schema.json)
- [`ed-handoff.schema.json`](./ed-handoff.schema.json)
- [`router.yaml`](./router.yaml)

### Decision / Information

- [`information-value-assessment.schema.json`](./information-value-assessment.schema.json): decision, default action, boundary, uncertainties, information actions, signal-to-action mapping, costs, selected probe, stop rule, and outcome.

### Workspace-Level

- [`project-workspace.schema.json`](./project-workspace.schema.json)
- [`design-asset-index.schema.json`](./design-asset-index.schema.json)
- [`decision-log.schema.json`](./decision-log.schema.json)

## Public/Private Boundary

Contracts must not contain real private project examples. Use schemas, generic descriptions, and synthetic or explicitly cleared fixtures only. VOI does not justify collecting sensitive data merely because the decision is important; privacy, contamination, consent, and publication risks belong in the information cost.
