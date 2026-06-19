# GameDesignOS Roadmap

This roadmap is capability-gated rather than date-promised. A stage advances only when the previous layer has reviewable cases, stable contracts, and regression coverage.

> 中文摘要：路线图按能力门推进，不承诺空泛日期。v0.8.0 先把 workspace 与 contract 打稳，v0.9.0 再做本地 Runtime，v1.0.0 才进入可长期管理真实项目的工作台形态。

## v0.8.0 — Runtime Foundation

**Theme:** From Skill Packages to Project Workspace.

Deliverables:

- product vision and system architecture;
- workspace template and manifest;
- decision-information and workspace-level contracts;
- a decision-to-information route plus four core production workflows;
- workspace-aware adapters;
- planned CLI surface;
- validation and release integration.

Exit gate:

- one synthetic project can be represented coherently as workspace assets;
- existing skills remain backward compatible;
- repository validation passes.

## v0.9.0 — Local Runtime Prototype

Delivered prototype capabilities:

```text
gamedesignos init <project>
gamedesignos status
gamedesignos voi <decision-id>
gamedesignos route <task>
gamedesignos new <asset-type>
gamedesignos validate
gamedesignos pack
gamedesignos doctor
```

Delivered behavior:

- initialize a workspace from the template;
- inspect manifest, asset index, accepted decisions, and current default actions;
- rank candidate information actions and enforce a research stop rule;
- recommend the smallest suitable skill;
- create contract-shaped artifact stubs;
- validate workspace structure and references;
- package a review-safe project snapshot.

Exit gate:

- commands are tested on at least two synthetic projects;
- routing failures and missing-upstream behavior are covered by evals;
- no credential or hosted-service responsibilities leak into the CLI.

Release bookkeeping:

- Runtime code and tests are on `main`;
- the public release should still be completed with the matching Git tag and GitHub Release after maintainer review.

## v1.0.0 — Project-Ready GameDesignOS

Candidate capabilities:

- local project dashboard;
- asset dependency graph;
- explicit Human Gate queue;
- project status and milestone view;
- private overlay guidance and migration;
- cross-skill end-to-end eval suite;
- validated concept-to-decision cases;
- exportable publisher, milestone, and retrospective packs.

Exit gate:

- a real private project can use GameDesignOS over multiple iterations without rebuilding context;
- accepted decisions, superseded assets, evidence boundaries, and rollback history remain traceable;
- public and private material boundaries are operationally clear.

## Later Exploration

Only after v1.0 foundations are stable:

- game-engine adapters;
- playtest and telemetry connectors;
- visual asset graph;
- multi-agent orchestration;
- team permissions and review roles;
- reusable studio overlays;
- optional local knowledge retrieval.

These are not commitments. They remain candidates until user evidence shows that they improve design decisions more than they increase system complexity.

## Prioritization Rule

Future work is prioritized by:

```text
positive net VOI
x decision value
x frequency of use
x reuse across projects
x evidence quality
÷ implementation and governance cost
```

New surface area should not be added merely because an agent can generate it.
