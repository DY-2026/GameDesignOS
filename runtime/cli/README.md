# Planned GameDesignOS CLI

This directory defines the intended local command surface for a future GameDesignOS runtime.

> v0.8.0 does **not** ship a complete CLI binary. These documents freeze command semantics before implementation so the workspace and contracts do not drift around ad hoc scripts.

See [commands.md](./commands.md) for command contracts.

## Design Goals

A future CLI should be:

- local-first;
- workspace-aware;
- model-provider neutral;
- safe around private material;
- explicit about Human Gates;
- deterministic for initialization and validation;
- replaceable by another host or harness.

## Non-Goals

The CLI should not:

- store API keys;
- become a hosted proxy;
- silently upload project files;
- choose irreversible project decisions;
- execute production changes without an explicit host permission model;
- hide missing evidence behind generated prose.

## Implementation Gate

A command moves from specification to implementation only when it has:

1. a stable input/output contract;
2. fixture workspaces;
3. failure and rollback behavior;
4. cross-platform path handling;
5. tests;
6. documentation that distinguishes local file operations from model calls.
