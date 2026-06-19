# Local CLI Command Reference

All commands operate on local files. Commands that mutate files support `--dry-run` where applicable.

## Initialize

```bash
gamedesignos init <project-name> [--destination PATH] [--codename SLUG] [--visibility private|public-synthetic|public-cleared] [--owner NAME] [--dry-run]
```

Creates `game.designos.yaml`, lifecycle directories, an empty asset index, an empty decision log, and a Decision Brief template. `--force` never overwrites an existing GameDesignOS workspace.

## Status

```bash
gamedesignos status [--workspace PATH] [--json]
```

Reports project identity, declared/runtime compatibility, asset counts, accepted decisions, open Human Gates, default actions, and missing directories.

## VOI

```bash
gamedesignos voi DEC-ID --decision QUESTION --default-action ACTION --option ACTION --option ACTION --owner NAME [--boundary undefined|far|near|locked] [--candidate-info ACTION] [--stop-when RULE] [--workspace PATH]
```

Creates a qualitative Information Value Assessment. Each round accepts at most three candidate information actions. Review an edited assessment with:

```bash
gamedesignos voi --input 06-decisions/information-value-assessment.json --write --workspace PATH
```

The reviewer checks option consistency, uncertainty references, signal-to-action mappings, stop rules, and whether any candidate can actually change action. It does not invent probabilities or monetary EV.

## Route

```bash
gamedesignos route <task text> [--workspace PATH] [--json]
```

Recommends the smallest suitable skill, names missing upstream assets, and preserves the eventual target skill. It never executes the skill.

## New Asset

```bash
gamedesignos new <asset-type> [--title TITLE] [--filename NAME] [--workspace PATH] [--dry-run]
```

Initial asset types are `concept`, `evidence-index`, `issue-card`, `validation-plan`, `information-assessment`, `ed-handoff`, `experiment`, `proposal`, `decision`, and `retrospective`. Generated files remain drafts with explicit TODO fields.

## Validate

```bash
gamedesignos validate [--workspace PATH] [--repo-root PATH] [--json]
```

Checks manifest compatibility, lifecycle directories, asset IDs and paths, dependency references, decision records, source-status boundaries, JSON syntax, and available canonical schemas.

## Pack

```bash
gamedesignos pack [--mode internal-review|publisher|public-synthetic] [--output FILE] [--workspace PATH] [--dry-run] [--force]
```

Creates a source-status-filtered bundle containing only registered assets allowed by the selected mode, plus a filtered index, summary, manifest, and SHA-256 record. Existing bundles are not overwritten unless `--force` is explicit.

## Doctor

```bash
gamedesignos doctor [--workspace PATH] [--json]
```

Checks Python, dependencies, repository contracts, workspace compatibility, and write access without changing project assets.
