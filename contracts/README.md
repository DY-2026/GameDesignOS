# Skill Contracts

`contracts/` defines stable cross-skill artifact shapes for `GameDesignOS`.

The goal is interoperability: skills can pass structured artifacts to one another instead of producing isolated prose documents.

## Contract Flow

1. `contracts/router.yaml` chooses the smallest suitable skill entrypoint before long skill bodies compete for the same request.
2. `game-concept-architect` can export a `player-promise-contract`.
3. `game-design-proposal-writer` can consume concept, validation, evidence, ED, market/source, and production artifacts to assemble a commercial proposal, indie dossier, publisher pitch, decision memo, or vertical-slice document.
4. `game-experience-analyzer` can read a `player-promise-contract` and perform a promise fulfillment diagnosis against a prototype, video, screenshot set, or gameplay sample.
5. `game-experience-analyzer` can output `evidence-index`, `issue-card`, and `ed-handoff` artifacts.
6. `game-experience-density-optimizer` can consume `ed-handoff` and `issue-card` artifacts to produce weekly ED experiments without repeating the evidence pass.
7. `paranoia-ai-system-evolver` can read `validation-plan`, `issue-card`, `ed-handoff`, and eval results to decide whether a workflow upgrade is worth promoting.
8. `game-design-book-translator` and `game-design-source-curator` are knowledge input layers. They do not directly depend on these contracts, but they can enrich references used by the other skills.

## Project-Internal Collaboration Rules

This router coordinates only skills shipped inside this repository. Do not add external/global design-master skills to this graph.

The default production path is:

```text
game-concept-architect
  -> player-promise-contract / validation-plan
  -> game-experience-analyzer
  -> evidence-index / issue-card / ed-handoff
  -> game-experience-density-optimizer
  -> weekly ED experiment / instrumentation / dashboard / decision rules
  -> game-design-proposal-writer
  -> proposal / pitch / decision memo / vertical-slice document
```

Use these boundaries:

| Situation | Route To | Stable Output |
| --- | --- | --- |
| One-line idea, no core loop, no player promise | `game-concept-architect` | `player-promise-contract`, `validation-plan` |
| Screenshot, recording, PV, store page, prototype sample, or gameplay evidence request | `game-experience-analyzer` | `evidence-index`, `issue-card`, `ed-handoff` |
| Retention, pacing, feedback, embodiment, atmosphere, cognitive-load, Demo completion, return-session, or habituation experiment | `game-experience-density-optimizer` | weekly ED experiment, instrumentation, dashboard, decision rules |
| Existing concept/evidence/ED/source/production artifacts need a formal proposal | `game-design-proposal-writer` | proposal, pitch, decision memo, vertical-slice document |
| Skill, schema, eval, router, workflow, promotion, or rollback changes | `paranoia-ai-system-evolver` | evolution proposal, OODA/VOI state, eval plan |
| Design source ingestion or durable knowledge assets | `game-design-source-curator` | source notes, reference boundary, traceable knowledge entry |
| Design-book translation or polish | `game-design-book-translator` | translated/polished reference material |

`game-experience-density-optimizer` should not repeat the evidence pass when an `ed-handoff` exists. It should consume the handoff, declare its evidence gate, choose the smallest output mode, and compile the experiment artifact.

`game-design-proposal-writer` should not override upstream skills. If the user asks for a proposal but has no concept contract, evidence layer, ED experiment, source notes, or production constraints, it should first request or route to the smallest missing upstream artifact.

## Schemas

- [`player-promise-contract.schema.json`](./player-promise-contract.schema.json): promise layers exported from concept work.
- [`validation-plan.schema.json`](./validation-plan.schema.json): assumption-led validation plan.
- [`evidence-index.schema.json`](./evidence-index.schema.json): stable cross-skill interface for evidence indexes. The canonical detailed schema remains in [`../game-experience-analyzer/templates/evidence-index.schema.json`](../game-experience-analyzer/templates/evidence-index.schema.json).
- [`issue-card.schema.json`](./issue-card.schema.json): minimum assignable diagnosis issue card.
- [`ed-handoff.schema.json`](./ed-handoff.schema.json): evidence-linked issue cards prepared for ED experiment design.
- [`router.yaml`](./router.yaml): candidate routing contract for cross-skill selection.

Contracts must not contain real private project examples. Use schemas and generic descriptions only.
