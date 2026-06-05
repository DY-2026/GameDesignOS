# Skill Contracts

`contracts/` defines stable cross-skill artifact shapes for `ParanoiaSkills`.

The goal is interoperability: skills can pass structured artifacts to one another instead of producing isolated prose documents.

## Contract Flow

1. `contracts/router.yaml` chooses the smallest suitable skill entrypoint before long skill bodies compete for the same request.
2. `game-concept-architect` can export a `player-promise-contract`.
3. `game-experience-analyzer` can read a `player-promise-contract` and perform a promise fulfillment diagnosis against a prototype, video, screenshot set, or gameplay sample.
4. `game-experience-analyzer` can output `evidence-index`, `issue-card`, and `ed-handoff` artifacts.
5. `game-experience-density-optimizer` can consume `ed-handoff` and `issue-card` artifacts to produce weekly ED experiments without repeating the evidence pass.
6. `paranoia-ai-system-evolver` can read `validation-plan`, `issue-card`, `ed-handoff`, and eval results to decide whether a workflow upgrade is worth promoting.
7. `game-design-book-translator` and `game-design-source-curator` are knowledge input layers. They do not directly depend on these contracts, but they can enrich references used by the other skills.

## Schemas

- [`player-promise-contract.schema.json`](./player-promise-contract.schema.json): promise layers exported from concept work.
- [`validation-plan.schema.json`](./validation-plan.schema.json): assumption-led validation plan.
- [`evidence-index.schema.json`](./evidence-index.schema.json): stable cross-skill interface for evidence indexes. The canonical detailed schema remains in [`../game-experience-analyzer/templates/evidence-index.schema.json`](../game-experience-analyzer/templates/evidence-index.schema.json).
- [`issue-card.schema.json`](./issue-card.schema.json): minimum assignable diagnosis issue card.
- [`ed-handoff.schema.json`](./ed-handoff.schema.json): evidence-linked issue cards prepared for ED experiment design.
- [`router.yaml`](./router.yaml): candidate routing contract for cross-skill selection.

Contracts must not contain real private project examples. Use schemas and generic descriptions only.
