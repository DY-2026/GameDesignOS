# Planned CLI Command Contracts

The examples below use the future executable name `gamedesignos`. Until a CLI is implemented, copy the workspace template manually and use the documented workflows.

## `gamedesignos init <project-name>`

Creates a new workspace from `runtime/workspace-template/`.

Expected options:

```text
--destination <path>
--codename <slug>
--visibility private|public-synthetic|public-cleared
--force
```

Expected behavior:

- refuse to overwrite a non-empty directory unless `--force` is explicit;
- write `game.designos.yaml`;
- preserve all lifecycle directories;
- print the next three setup actions.

## `gamedesignos status`

Reads the workspace manifest, asset index, and latest decision entries.

Expected output:

```text
project identity
project status
asset counts by type and review state
unresolved Human Gates
missing required directories
manifest/runtime version compatibility
```

## `gamedesignos voi <decision-id>`

Creates or reviews a VOI decision gate before research, retrieval, experimentation, or another AI branch.

Expected inputs:

```text
--decision <question>
--default-action <action>
--option <action>          # repeatable
--deadline <date-or-gate>
--stakes low|medium|high|critical
--reversibility reversible|costly_to_reverse|irreversible
--candidate-info <action>  # repeatable, maximum three per round
```

Expected behavior:

- classify the boundary as `undefined`, `far`, `near`, or `locked`;
- identify only uncertainties that can change the option ranking;
- require signal-to-action mapping for every candidate information action;
- compare EVPI ceiling, realistic EVSI, acquisition, delay, attention, privacy, and contamination costs;
- select the smallest positive-net-VOI probe or recommend acting now;
- write `06-decisions/information-value-assessment.json`;
- refuse open-ended research without a stop rule.

## `gamedesignos route <task>`

Suggests the smallest suitable skill using the request, available upstream assets, and `contracts/router.yaml`.

Expected behavior:

- explain why the route was selected;
- identify missing upstream assets;
- avoid loading every skill at once;
- never claim that a route executed successfully when it only produced a recommendation.

## `gamedesignos new <asset-type>`

Creates a contract-shaped asset stub.

Initial asset types:

```text
concept
evidence-index
issue-card
validation-plan
information-assessment
ed-handoff
experiment
proposal
decision
retrospective
```

Expected behavior:

- choose the correct lifecycle directory;
- create a unique asset ID;
- register the path in the asset index;
- leave explicit placeholders rather than invented evidence.

## `gamedesignos validate`

Validates:

- `game.designos.yaml`;
- required lifecycle directories;
- JSON/YAML syntax;
- workspace-level contracts;
- referenced local asset paths;
- asset IDs and review states;
- public/private source-status consistency.

Suggested exit codes:

```text
0  valid
1  validation errors
2  invalid invocation
3  workspace not found
4  incompatible schema/runtime version
```

## `gamedesignos pack`

Creates a review-safe project bundle.

Expected options:

```text
--mode internal-review|publisher|public-synthetic
--output <path>
```

Expected behavior:

- include only assets allowed by the selected mode;
- exclude credentials, local tool state, and private overlay files;
- emit a manifest of included and excluded assets;
- stop when source status is ambiguous.

## `gamedesignos doctor`

Diagnoses local runtime readiness without modifying project assets.

Checks may include:

- supported Python/runtime version;
- workspace access;
- schema availability;
- broken relative paths;
- optional host-agent configuration;
- stale or missing asset index.

## Command Safety Rule

A command that mutates project files should support a dry-run or preview mode. A command that triggers a model should display which local assets will be shared with the host before invocation.
