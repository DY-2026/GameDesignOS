# GameDesignOS Runtime Foundation

The runtime layer describes how a project workspace, contracts, skills, adapters, and human review fit together.

> 中文摘要：v0.8.0 的 Runtime 是 documentation-first foundation，不是托管 API。它提供可复制 workspace、资产约定、路由流程和未来 CLI 语义。

## v0.8.0 Runtime Status

Available now:

- [`workspace-template/`](./workspace-template/): a copyable project skeleton;
- [`../contracts/`](../contracts/): skill-level and workspace-level artifact contracts;
- [`../docs/workflows/`](../docs/workflows/): workspace-aware production routes;
- [`../adapters/`](../adapters/): host-agent integration guidance;
- [`cli/`](./cli/): planned local command surface.

Not shipped in v0.8.0:

- a hosted service;
- a model gateway;
- API-key management;
- a full CLI binary;
- a GUI dashboard;
- automatic game-engine production.

## Start a Private Workspace

From the repository root:

```bash
cp -R runtime/workspace-template ../my-game-designos
cd ../my-game-designos
```

On PowerShell:

```powershell
Copy-Item -Recurse runtime/workspace-template ../my-game-designos
Set-Location ../my-game-designos
```

Then edit `game.designos.yaml`.

Keep real projects outside this public repository unless the project is synthetic, public, or explicitly cleared for publication.

## Runtime Lifecycle

```text
create or open workspace
  -> read game.designos.yaml
  -> inspect existing design-asset index
  -> identify the Decision Object and current default action
  -> classify the decision boundary
  -> run the VOI gate when more information is proposed
  -> choose the smallest positive-net-VOI probe or act now
  -> route to the smallest suitable skill
  -> load only required references/templates
  -> create or update workspace assets
  -> validate structure and evidence boundary
  -> stop when the marginal VOI is non-positive or the evidence gate is reached
  -> Human Gate
  -> update the VOI assessment and decision log
  -> retrospective or next route
```

## Decision-First Information Contract

Before a host opens broad search, memory, RAG, or experimentation, it should know the decision, real options, current default action, owner, deadline, stakes, reversibility, and boundary status.

A candidate information action must identify the uncertainty it targets, plausible signals, the action following each signal, its EVPI ceiling or qualitative upper bound, realistic EVSI, and total cost. If all plausible signals lead to the same action, the current decision value is approximately zero. The host should act, time-box model learning, or classify the activity as consumption.

Use [`docs/workflows/decision-to-information.md`](../docs/workflows/decision-to-information.md) and [`contracts/information-value-assessment.schema.json`](../contracts/information-value-assessment.schema.json).

## Workspace-Aware Agent Contract

A host agent should:

1. read `game.designos.yaml`;
2. inspect `06-decisions/` before contradicting accepted decisions;
3. inspect upstream assets before asking the user to restate context;
4. read or create a decision brief before broad research;
5. use `contracts/information-value-assessment.schema.json` to test whether proposed information can change action;
6. use `contracts/router.yaml` to choose the smallest suitable skill;
7. load the selected `SKILL.md`;
8. save outputs to the documented lifecycle directory;
9. update the asset index and VOI outcome;
10. stop at the research stop rule or Human Gate when commitment or publication is required.

## Direct Skill Mode Remains Supported

A user may still copy and run one skill package without a workspace. v0.8.0 adds an optional project layer; it does not remove or break direct skill usage.

## Private Overlay Boundary

The public repository is the reusable base. A private workspace or overlay may add:

- studio terminology;
- real project concepts;
- client material;
- internal metrics and budgets;
- unpublished media;
- local tools and credentials;
- team-specific review rules.

Do not commit those materials back to the public base.

## Validation

Repository-level validation:

```bash
python scripts/validate_repo.py
```

The validator checks the runtime foundation, workspace template, schemas, YAML/JSON syntax, skill packages, and required public files.
