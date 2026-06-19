# Runtime Foundation and Local Prototype

The runtime layer describes how a project workspace, contracts, skills, adapters, local commands, and human review fit together.

## v0.9.0 Runtime Status

Available now:

- an executable local `gamedesignos` CLI;
- a copyable workspace template;
- workspace and skill-level contracts;
- Decision-to-Information and production workflow guides;
- deterministic initialization, status, routing, draft creation, validation, packing, and diagnostics.

Install from the repository root:

```bash
python -m pip install -e .
gamedesignos --version
```

Start a private workspace:

```bash
gamedesignos init "My Game" --destination ../my-game-designos
```

Then define the first Decision Object and run:

```bash
gamedesignos route "turn this one-line idea into a validation plan" --workspace ../my-game-designos
gamedesignos validate --workspace ../my-game-designos
```

The runtime performs no model or network call. API keys, model selection, disclosure previews, and tool permissions belong to the host agent or harness.

## Compatibility

The runtime implementation is `0.9.0`. The workspace schema remains `0.8.0`, because the manifest shape is unchanged. Existing v0.8 workspaces remain supported without destructive migration.

## Runtime Lifecycle

```text
create or open workspace
  -> inspect manifest, asset index, and decisions
  -> define Decision Object and default action
  -> run VOI gate before broad information acquisition
  -> route to the smallest suitable skill
  -> create or update a durable draft asset
  -> validate evidence, references, and source status
  -> stop at the research rule or Human Gate
  -> package an allowed review snapshot
```

## Non-Goals

The v0.9 prototype does not provide a hosted service, model gateway, API-key manager, automatic skill execution, autonomous search, GUI dashboard, or game-engine production adapter.

See [`cli/README.md`](./cli/README.md), [`cli/commands.md`](./cli/commands.md), and [`../docs/product/v0.9.0-definition.md`](../docs/product/v0.9.0-definition.md).
