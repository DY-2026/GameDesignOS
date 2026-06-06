# WOOP Harness Protocol

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. Positioning

WOOP in an AI harness is not motivational coaching. It is a control protocol for task admission, execution checks, and failure recovery.

External references:

- Harness engineering treats guides, sensors, tools, and feedback loops outside the model as the outer system that makes agents more trustworthy: <https://martinfowler.com/articles/harness-engineering.html>
- WOOP uses the ordered steps Wish, Outcome, Obstacle, and Plan: <https://woopmylife.org/en/practice>

This skill uses the engineering translation: make wishes, outcomes, obstacles, and plans recognizable, triggerable, executable, and recordable by the harness.

## 2. Four Engineering Modules

| WOOP | Human Use | AI Harness Module | Control Role |
| --- | --- | --- | --- |
| Wish | What to achieve | `Intent Spec` | Goal, artifact, boundary, and stop condition |
| Outcome | Desired result | `Evaluation Rubric` | Acceptance picture, scoring rule, value function |
| Obstacle | Inner obstacle | `Failure Pattern` | High-probability human-AI collaboration failure |
| Plan | If-then plan | `If-Then Protocol` | Trigger, checker, retry, fallback, Human Gate |

WOOP sits before OODA as the task entry point and reappears during Evaluate as the failure-pattern check.

## 3. Obstacle Means Internal Failure Pattern

Do not write external difficulty as the Obstacle. External difficulty explains why work is hard; it does not tell the harness when to trigger or what to do.

Translate it into an internal human-AI system pattern:

| Weak Obstacle | Harness-ready Failure Pattern |
| --- | --- |
| Not enough sources | When sources are thin, I let the AI fill gaps and accept fluent answers |
| Not enough time | Under time pressure, I skip validation and read only conclusions |
| AI hallucination | When the AI sounds confident, I mistake fluency for truth |
| Complex task | The agent may mistake local completeness for whole-system correctness |
| Too many tools | The agent may overuse tools and forget VOI |
| Changing requirements | The agent may drift from the original Outcome |

A strong Failure Pattern is observable, intervenable, and replayable.

## 4. WOOP Task Card

Before a complex task enters production mode, fill at least:

```yaml
woop_task_card:
  wish:
    intent_spec: ""
    output_artifact: ""
    scope_boundary: ""
    stop_condition: ""
  outcome:
    decision_value: ""
    acceptance_rubric: []
  obstacle:
    failure_patterns:
      - pattern: ""
        trigger: ""
        severity: "low | medium | high"
  plan:
    if_then_protocols:
      - if: ""
        then: ""
        judge: "agent | user | validator | test | reviewer"
        next_step: "continue | retry | rewrite | verify | ask_human | rollback"
```

## 5. Admission Rules

| Missing Field | Default Action |
| --- | --- |
| Wish unclear | Clarify, split, or enter exploration mode |
| Outcome unclear | Do not enter production mode; draft only or define acceptance criteria |
| Obstacle unclear | Apply default Failure Patterns and lower autonomy |
| Plan unclear | Do not automate A3/A4 or irreversible actions |

Useful default Failure Patterns: fluency mistaken for truth, goal drift, treating organization as insight, premature tool use, context pollution, local optimization, no stop condition, formatter-driven evaluation, and skipped validation under pressure.

## 6. Execution Monitoring

After each phase:

1. Score with Outcome: does the result satisfy the acceptance picture and decision value?
2. Check Obstacle: did a preset Failure Pattern trigger?

If an Obstacle triggers, do not keep polishing. Execute the Plan first.

## 7. Failure Recovery

Plans must be executable. Avoid "be critical"; write triggers and actions.

```text
If a factual claim has no source,
Then split source / uncertainty / inference, or downgrade it to a hypothesis.

If validation is being skipped,
Then run at least one lightweight counterexample or red-team check.

If the output is complete but lacks decision tension,
Then remove decorative modules and keep one core loop plus two or three tradeoff variables.

If a tool call is costly and cannot change the decision,
Then record a low-confidence assumption and continue.

If a high-impact action has no rollback,
Then keep it candidate and ask the Human Gate.
```

## 8. Relation to VOI/OODA/Eval

WOOP defines where to go, what good means, where the system breaks, and what to do when it breaks. VOI chooses information actions. OODA executes reality-facing loops. Eval judges whether candidate changes improve result, process, or evolution quality. Human Gate promotes durable rules. Rollback keeps recovery reversible.

## 9. Trace and Writeback

Record triggered Obstacles:

```yaml
woop_trace:
  triggered_obstacles:
    - pattern:
      trigger_seen:
      plan_executed:
      outcome_after_plan:
      should_become_candidate_rule: true | false
```

Only repeated, high-impact, reusable, reversible, evidence-backed patterns should enter meta OODA as `candidate`. Long-term memory, global skills, and production strategy require Human Gate.
