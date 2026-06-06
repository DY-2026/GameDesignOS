# Model Compression Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. Core Judgment

When upgrading an AI system, first ask: what model is this system actually using?

A prompt, skill, agent, workflow, or harness that only adds more scenario-specific steps usually becomes a patch collection. A strong upgrade compresses a class of tasks into a reusable, composable, and verifiable operating model.

The standard is not whether the terminology sounds advanced. The standard is:

```text
shorter core description
+ fewer exception patches
+ clearer mediator variables
+ more actionable control points
+ more reliable validation and recovery
```

## 2. Good Regulator View

To control a system, the regulator must contain a model of that system. For AI workflows, the regulator may be:

- prompt
- skill
- agent loop
- workflow
- tool routing
- memory schema
- eval gate
- human review gate
- rollback policy

If the regulator's model is too coarse, it underfits: it watches the final result but cannot diagnose what broke.

If the regulator's model is too detailed, it overfits: rules, paths, state, and exception patches consume the system's execution capacity.

## 3. WOOP as a Minimal Harness Model

WOOP is a low-cost harness compression model. It does not add scenario scripts; it compresses complex tasks into four stable control points:

```text
Wish -> Outcome -> Obstacle -> Plan
= Intent Spec -> Evaluation Rubric -> Failure Pattern -> If-Then Protocol
```

It reduces downstream patch cost:

- Wish reduces `routing_rule_length`: route by real intent and output boundary instead of scenario nouns.
- Outcome reduces `validation_observation_length`: observe only signals that judge result quality.
- Obstacle reduces `exception_patch_length`: turn repeated failures into recognizable patterns.
- Plan reduces `failure_recovery_length`: recover through if-then protocol instead of human memory.

If a WOOP change only adds more pre-task text without lowering routing, validation, exception, or recovery cost, it is not effective compression.

## 4. Minimum Description Length Gate

Use this approximation to judge model granularity:

```text
model_score = core_model_length
            + data_patch_length
            + routing_rule_length
            + state_injection_length
            + validation_observation_length
            + exception_patch_length
            + failure_recovery_length
```

The goal is not to minimize every term independently. The goal is to reduce total description cost without losing important result quality.

Default interpretation:

| Cost | Question | Reduction Pattern |
| --- | --- | --- |
| `core_model_length` | Is the core rule too long to remember or transfer? | Extract stable operations instead of adding scenario nouns |
| `data_patch_length` | Does every run require many extra exceptions? | Find a better mediator or task boundary |
| `routing_rule_length` | Is routing becoming an if-else maze? | Merge isomorphic tasks and route by information transformation |
| `state_injection_length` | Does each run need a huge context dump? | Externalize state into manifest, spec, or state files |
| `validation_observation_length` | Is validation too heavy or blind to key facts? | Observe only signals that can change decisions |
| `exception_patch_length` | Does every failure add another patch? | Repair the model instead of adding tape |
| `failure_recovery_length` | Does recovery depend on human memory? | Encode retry, rollback, conflict zones, and exit criteria |

## 5. Verbs Before Nouns

Model by how information is transformed, not by what scenario it belongs to.

Scenarios are nouns: boss, ex, project, article, user, competitor.

Operations are verbs: filter, archive, translate, compress, route, validate, align, roll back, transcode, score, compare, deconstruct.

A good skill behaves like a game mechanic: repeatable, composable, and capable of emergence. A weak skill behaves like a level script: useful for one scene and patch-heavy when conditions change.

## 6. Causal Mediator Gate

Do not stop at:

```text
input -> final_output
```

Write:

```text
input -> mediator_1 -> mediator_2 -> final_output
```

Mediator variables are diagnosable, intervenable, and verifiable intermediate nodes. Once you find the mediator, the system knows where its control points are.

Common AI workflow mediators:

| Outcome | Common Mediators |
| --- | --- |
| High-quality answer | task understanding, WOOP admission, context selection, state retention, tool use, process validation, failure recovery |
| Good skill | trigger boundary, core operation, WOOP Task Card, reference path, template reuse, validation gate, rollback path |
| Good RAG | source quality, chunk boundary, retrieval intent, rerank, citation discipline, answer synthesis |
| Good agent | observe fidelity, orientation model, decision policy, tool affordance, state update, WOOP obstacle trigger, eval signal |
| Good management workflow | retention, conversion, delivery speed, information flow, decision efficiency, team coordination |

If a change cannot explain which mediator it improves, it is usually a style preference and should not become a long-term system rule.

## 7. Control Point Gate

Mark control points for each mediator chain:

```yaml
mediator:
  can_observe: true | false
  can_intervene: true | false
  intervention:
  eval_signal:
  failure_signal:
```

Prioritize nodes where `can_observe = true` and `can_intervene = true`.

Observable but non-intervenable nodes are useful for warnings or diagnosis.

Nodes that cannot be observed but are treated as core control points are high-risk black boxes.

## 8. Harness / Agent / Skill Model Differences

Use the same questions to audit different structures:

| Structure | Strong Model | Weak Model |
| --- | --- | --- |
| Harness | Makes task understanding, WOOP admission, state retention, tool use, validation, and recovery explicit | Adds a wrapper while still relying on one-shot model performance |
| Agent | Defines OODA, tool boundaries, state updates, and eval signals | Loops forever with no exit condition or evidence gate |
| Skill | Compresses a class of operations into a reusable mechanic with WOOP, templates, and validation gates | Turns one scenario into a longer script |
| Workflow | Transforms upstream information into a form that downstream work can use | Only arranges roles, steps, and slogans |
| Prompt | Defines task model, inputs, outputs, Outcome, and failure signals | Stacks adjectives and style requests |

## 9. Upgrade Flow

Use this order for each upgrade:

1. Write the system's current implicit model.
2. Write the WOOP Task Card and confirm Intent Spec, Evaluation Rubric, Failure Pattern, and If-Then Protocol.
3. Mark inputs, outputs, mediators, and control points.
4. Estimate total description cost and find the highest-cost term.
5. Diagnose whether the issue is underfit, overfit, or a missing mediator.
6. Design the smallest change that lowers total description cost.
7. Mark the change as `candidate`.
8. Use evals or real task samples to check whether it reduces patches, improves control, or lowers recovery cost.
9. If it should become durable, promote it only after Human Gate.

## 10. Output Shape

```yaml
model_audit:
  current_model: ""
  proposed_model: ""
  compression_claim: ""
  woop_compression:
    intent_spec:
    evaluation_rubric: []
    failure_patterns: []
    if_then_protocols: []
  causal_chain:
    - from:
      mediator:
      to:
      evidence:
  control_points:
    - mediator:
      intervention:
      eval_signal:
      failure_signal:
  description_cost:
    core_model_length: "low | medium | high"
    data_patch_length: "low | medium | high"
    routing_rule_length: "low | medium | high"
    state_injection_length: "low | medium | high"
    validation_observation_length: "low | medium | high"
    exception_patch_length: "low | medium | high"
    failure_recovery_length: "low | medium | high"
  diagnosis: "underfit | overfit | missing_mediator | balanced"
  candidate_change: ""
  expected_cost_delta: ""
```

