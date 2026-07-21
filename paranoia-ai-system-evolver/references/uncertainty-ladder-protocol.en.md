# UL (Uncertainty Ladder) Engineering Protocol

> Copyright (c) 2026 @Paranoia. All rights reserved.

## Purpose

UL is the canonical abbreviation for Uncertainty Ladder. It is an experiment-environment protocol for controlled AI-system evolution. VOI chooses which uncertainty is worth reducing; UL controls how much uncertainty is exposed in the next probe so failures remain attributable.

```text
build model -> isolate actions -> controlled composition -> expose failure
-> diagnose bottleneck -> targeted practice -> increase complexity
-> test transfer -> update model
```

It applies to prompts, context, tools, routing, memory, workflows, schemas, evals, agent coordination, and authority design. It does not imply model-weight mutation.

## Control-layer split

| Layer | Responsibility |
| --- | --- |
| Intent Work Order / WOOP | Desired reality, acceptance, recovery |
| Decision Object / VOI | Decision and highest-value uncertainty |
| Uncertainty ladder | Exposure dose, scaffolds, attribution |
| OODA | Execute and update one iteration |
| Eval | Graduation and negative-transfer evidence |
| RJR-AI / Human Gate | Authority and real-world consequence boundary |

## Exposure vector

Do not collapse difficulty into one score. Track at least: `input_novelty`, `context_ambiguity`, `tool_environment_variability`, `coordination_variability`, `authority_and_consequence`, and `evaluation_ambiguity`. Release one major variable per round by default. Authority never auto-promotes because other dimensions passed.

## Rungs

- `UL-L0`: define the minimal source contract, causal model, observable signals, valid action, known failures, and authority boundary.
- `UL-L1`: test isolated behaviors with fixed input and acceptance criteria.
- `UL-L2`: combine passed actions in a short, repeatable, low-consequence chain.
- `UL-L3`: add one high-VOI perturbation, then use ablation, control, or counterfactual evidence to identify the primary bottleneck.
- `UL-L4`: remove scaffolds one at a time and record the newly exposed uncertainty, consequence budget, and fallback.
- `UL-L5`: test near, medium, and—when useful—far transfer, including at least one negative-transfer case.

If two or more leading explanations cannot be separated, mark attribution `confounded`, restore scaffolds, and shrink the environment. Do not build permanent rules on a confounded failure.

## Minimal state

```yaml
ul_state:
  schema_version: "1.0.0"
  ul_id: "UL-YYYYMMDD-001"
  status: "candidate | shadow | warn | enforce"
  target_capability: ""
  decision_ref: null
  voi_gate_ref: null
  current_rung: "UL-L0 | UL-L1 | UL-L2 | UL-L3 | UL-L4 | UL-L5"
  world_model_ref: null
  uncertainty_exposure: {}
  released_this_round: []
  held_constant: []
  scaffolds_present: []
  consequence_budget: ""
  preregistered_signals:
    pass: []
    fail: []
    confounded: []
    stop: []
  attribution_gate:
    observable_failure: null
    candidate_bottlenecks: []
    discriminating_probe: null
    primary_bottleneck: null
    attribution_confidence: "not_tested | low | medium | high | confounded"
    evidence_refs: []
  targeted_intervention: null
  same_rung_replay: []
  graduation_evidence: []
  transfer_checks:
    near: []
    medium: []
    far: []
    negative_transfer: []
  next_uncertainty_to_release: null
  fallback_rung: null
  rollback: ""
  stop_rule: ""
  human_gate:
    required: false
    reason: ""
```

## Graduation and rollback

Graduate only when the current behavior is stable, traces expose the relevant mediators, attribution is not confounded, the next rung adds few named uncertainties, failure cost is budgeted, rollback works, and any real-world consequence has Human Gate approval. Roll back when variables change together, mediators are invisible, a local fix harms representative cases, fixtures pass but novel inputs fail immediately, exception text grows around one unresolved bottleneck, or authority exceeds delegation.

Passing a benchmark is not transfer proof. A polished case is candidate evidence, not a production rule.
