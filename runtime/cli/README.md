# GameDesignOS v0.9.0 Local Runtime

This directory contains the executable local runtime prototype introduced in v0.9.0.

Install from the repository root:

```bash
python -m pip install -e .
```

Run either entrypoint:

```bash
gamedesignos --version
python -m gamedesignos --version
```

Implemented commands:

```text
init
status
voi
route
new
validate
pack
doctor
```

The runtime is deterministic and local-first. It does not call a model, store credentials, upload workspace files, execute a skill automatically, or approve a Human Gate.

See [commands.md](./commands.md) for command semantics and [`../../docs/product/v0.9.0-definition.md`](../../docs/product/v0.9.0-definition.md) for the product boundary.
