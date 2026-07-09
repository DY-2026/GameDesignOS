# Workflow: Decision to Information

## Purpose

Turn an undefined research impulse, information overload, FOMO, or a real choice under uncertainty into a bounded information action that can change a project decision.

This is a cross-cutting workflow. Domain skills still own the game-design work; the VOI gate decides whether more information is worth acquiring before they act.

RJR-AI adds the authority layer before information work: AI may expand options, Workflow may compress the process, Eval may provide feedback, and automation may execute low-risk reversible steps; high-coupling, low-reversibility, under-evidenced direction choices remain human residual judgment.

## Primary Method

`$paranoia-ai-system-evolver` for an explicit VOI audit, using:

- `paranoia-ai-system-evolver/references/value-of-information-playbook.*`;
- `paranoia-ai-system-evolver/templates/voi_decision_gate.*`;
- `contracts/information-value-assessment.schema.json`.

## Workspace Reads

```text
00-inbox/
01-concept/
02-evidence/
03-analysis/
04-proposals/
05-experiments/
06-decisions/
07-retrospectives/
design-asset-index.json
```

Read accepted decisions and existing evidence before asking the user to restate context or commissioning new research.

## Workspace Writes

```text
06-decisions/decision-brief.md
06-decisions/information-value-assessment.json
06-decisions/decision-log.json
```

The selected probe may create downstream assets in the domain directory, such as an evidence index, validation plan, experiment plan, or retrospective.

## Paranoia Checkpoint

This workflow is owned by `$paranoia-ai-system-evolver`. It should also leave a workflow governance trail so other workflows can consume the decision instead of rerunning broad research.

Required checkpoint output:

- `intent_work_order_ref`: the reality change or decision state that information work should serve;
- `decision_ref`: Decision Object and `current_default_action`;
- `voi_gate_ref`: selected probe, rejected information actions, and stop rule;
- `rjr_authority_ref`: coupling, reversibility, authority level, delegation matrix, and residual judgment;
- `paranoia_review_ref`: information-consumption, FOMO, AI fatigue, or branch-explosion findings;
- `candidate_learning_refs`: any reusable rule remains candidate until eval and Human Gate promotion.

## Flow

```text
research impulse or unresolved choice
  -> declare Decision Object
  -> identify current default action
  -> declare RJR-AI authority gate: coupling / reversibility / authority_level / residual_judgment
  -> classify boundary: undefined / far / near / locked
  -> map action-sensitive uncertainties
  -> generate at most three information actions
  -> pre-register signal-to-action mapping
  -> compare EVPI ceiling, EVSI, cost, delay, attention, and risk
  -> run the smallest positive-net-VOI probe or act now
  -> update prior, posterior, and action
  -> stop rule
  -> Human Gate / decision log
```

## Decision Gate

The workflow must answer:

1. What decision is being made?
2. What action happens with current information?
3. Which authority level is allowed before Human Gate?
4. Which plausible signal would reverse or materially alter that action?
5. What is the smallest way to observe such a signal?
6. Is its expected value higher than acquisition, delay, attention, privacy, and contamination costs?
7. When will research stop?

If no plausible signal changes action, mark the current decision VOI as approximately zero. Either act, time-box model learning, or classify the activity as information consumption.

## Boundary Rules

- `undefined`: define the decision before research; cap exploration.
- `far`: act or run a light verification.
- `near`: prioritize the smallest high-VOI sample or experiment.
- `locked`: stop researching the old choice; move to execution metrics or retrospective.

## Information Priority

Prefer:

- project-local data and traces;
- user negative feedback and failed tasks;
- information that challenges the current prior;
- evidence available before the decision deadline;
- small reversible probes with explicit action branches.

Deprioritize:

- generic macro trends that cannot change this project action;
- repeated summaries of already-known facts;
- information that only increases identity, status, or FOMO relief;
- full-scale builds when a smaller sample can answer the decision.

## Human Gate

The owner chooses:

```text
act_with_current_information
run_selected_probe
request_higher_fidelity_information
change_default_action
stop_research
classify_as_model_learning
```

## Minimal Prompt

```text
Use $paranoia-ai-system-evolver to run a VOI decision gate before more research.

Decision question:
Current default action:
Real options:
Deadline:
Stakes and reversibility:
RJR authority level and residual judgment:
Known uncertainty:
Candidate information sources or tests:

Return a Decision Object, RJR-AI authority gate, boundary status, no more than three information actions, signal-to-action mapping, EVPI/EVSI and cost judgment, the smallest selected probe, and a stop rule. Write the assessment to 06-decisions/.
```

## Definition of Done

- decision, options, owner, deadline, and current default action are explicit;
- RJR-AI authority gate names coupling, reversibility, authority level, residual judgment, and Human Gate trigger;
- the boundary is classified;
- every information action targets an action-sensitive uncertainty;
- possible signals map to different actions;
- acquisition, delay, attention, privacy, and contamination costs are visible;
- the selected probe is smaller than the decision it informs;
- a stop rule exists;
- posterior and action change are recorded after the probe.
