# GameDesignOS Project Workspace Template

Copy this directory outside the public repository to start a real or synthetic project.

```bash
cp -R runtime/workspace-template ../my-game-designos
cd ../my-game-designos
```

Edit `game.designos.yaml` before adding project material.

## Layout

| Directory | Purpose | Typical Assets |
| --- | --- | --- |
| `00-inbox/` | Unreviewed intake | notes, links, screenshots, questions, FOMO captures |
| `01-concept/` | Concept truth candidates | concept seed, player promise, core loop, scope gate, validation plan |
| `02-evidence/` | Source and observation layer | source boundary, evidence index, timestamps, screenshot cards |
| `03-analysis/` | Interpretation and diagnosis | experience report, issue cards, transfer boundaries |
| `04-proposals/` | Decision-facing documents | one-page memo, indie dossier, pitch, vertical-slice plan |
| `05-experiments/` | Sample information and results | ED handoff, variants, instrumentation, dashboard, rollback |
| `06-decisions/` | Human authority and VOI gate | decision brief, information-value assessment, decision log, milestone gates |
| `07-retrospectives/` | Learning and writeback | experiment review, project retrospective, workflow-upgrade notes |

## First Six Actions

1. Set project identity, status, visibility, and owner in `game.designos.yaml`.
2. Move raw material into `00-inbox/` without treating it as design truth.
3. Before searching or opening more AI branches, write `06-decisions/decision-brief.md`: decision, options, current default action, deadline, stakes, reversibility, and boundary status.
4. When more information may change the action, copy `06-decisions/information-value-assessment.example.json` and run the Decision-to-Information workflow.
5. Run the smallest relevant production workflow from `docs/workflows/` and register durable outputs in `design-asset-index.json`.
6. Record commitment-changing choices and information stop reasons in `06-decisions/decision-log.json`.

## Decision-First Information Rule

```text
undefined decision
  -> define decision and exploration budget
far from boundary
  -> act or run only a light check
near boundary
  -> acquire the smallest high-VOI sample
locked decision
  -> stop researching the old choice; execute or retrospect
```

Information enters the project as one of three modes:

- `decision_information`: may change action, priority, resource allocation, or a stop condition;
- `model_learning`: improves a reusable model but does not change the current action;
- `information_consumption`: provides curiosity, entertainment, identity, or social value and must not occupy the project decision thread.

Every decision-information action should name the uncertainty it targets, the signals it may reveal, the action for each signal, total cost, and a stop rule. If all plausible signals lead to the same action, stop the research or reclassify it.

## Design Truth Order

```text
accepted human decision
  > accepted reviewed asset
  > reviewed draft
  > unreviewed draft
  > inbox note
  > unstated agent assumption
```

## File Naming

Prefer stable, descriptive names:

```text
decision-brief.md
information-value-assessment.json
concept-seed.md
player-promise-contract.json
validation-plan.json
evidence-index.json
issue-cards.json
weekly-experiment-plan.md
one-page-decision-memo.md
decision-log.json
```

Add dates or sequence numbers only when multiple versions must coexist. Use review state and upstream references instead of ambiguous names such as `final-final-v2.md`.

## Asset Index

`design-asset-index.example.json` demonstrates the workspace-level contract. Copy it to `design-asset-index.json`, replace the synthetic entries, and keep paths relative to the workspace root. Information assessments are durable assets when they change or close a real project decision.

## Decision and VOI Files

- `06-decisions/decision-brief.template.md`: the minimal human-readable decision object.
- `06-decisions/information-value-assessment.example.json`: a machine-readable VOI gate with EVPI/EVSI, signal-to-action mapping, costs, selected probe, and stop rules.
- `06-decisions/decision-log.example.json`: the Human Gate record, including action before/after information and the reason research stopped.

## Privacy Boundary

The template is public; your project usually is not.

Do not commit real concepts, client work, internal metrics, credentials, private screenshots, unpublished roadmaps, budgets, or local host configuration to the public GameDesignOS repository. Use synthetic or explicitly cleared fixtures for public examples.
