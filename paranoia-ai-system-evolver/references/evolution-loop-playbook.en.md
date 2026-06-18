# Evolution Loop Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. Controlled Evolution

Self-evolving AI means improving external system layers under stable goals: prompts, memory, retrieval, tool routing, workflows, schemas, eval sets, and skill references. It does not mean uncontrolled model-weight mutation.

```text
real task pressure
-> WOOP Task Card
-> Decision Object
-> VOI decision gate
-> smallest information probe
-> Orient-first OODA
-> result feedback
-> candidate mutation
-> behavior eval
-> Human Gate
-> versioned promotion
-> rollback path
```

## 2. WOOP Admission

Wish defines intent, artifact, scope, and stop condition. Outcome defines the acceptance rubric and decision value. Obstacle identifies internal human-agent Failure Patterns. Plan defines executable If-Then Protocols, judges, retries, handoff, and rollback.

Unclear Wish means clarify or shrink. Unclear Outcome means draft only. Unclear Obstacle lowers autonomy. Unclear Plan blocks high-risk and irreversible actions.

## 3. Decision Object

Before VOI, declare the decision question, real options, current default action, owner, deadline, stakes, reversibility, and boundary status. Without a default action there is no action-change test; without options there is no decision comparison; without a deadline research can become avoidance.

## 4. Scarce Resources

Treat tokens, time, attention, tool calls, context, trustworthy feedback, labeled samples, money, trust, and decision windows as scarce. AI makes information generation cheap while increasing evaluation and closure costs. Optimize for closing low-value branches, not maximizing output volume.

## 5. VOI Gate

Use `references/value-of-information-playbook.en.md` for the full method.

```text
1. What decision is being supported?
2. What action is taken with current information?
3. Which uncertainties can change the option ranking?
4. Which concrete information actions target them?
5. What action follows each plausible signal?
6. What are the EVPI ceiling and realistic EVSI?
7. What are acquisition, delay, attention, privacy, and contamination costs?
8. What is the smallest high-value probe and its stop rule?
```

```text
approx_net_voi
= P(action_switch)
× decision_delta
× reuse_or_scale
× reversibility_factor
- total_information_cost
```

This is a triage heuristic. If all plausible signals lead to the same action, stop or classify the work as model learning or information consumption.

## 6. Orient-First OODA

Observe goals, evidence, surprise, failures, corrections, costs, latency, and triggered Obstacles. Orient around the current frame, obsolete narratives, decision boundary, user/domain/operating models, and whether the information is decision, model, or consumption value. Decide one action or probe and explicitly reject low-VOI branches. Act through an artifact, tool call, or bounded test. Evaluate the chain:

```text
prior -> signal -> posterior -> action_before -> action_after -> stop reason
```

## 7. Model Compression Gate

Check whether the model is too short to expose mediators, too long to execute, or merely moving complexity. Every new rule should name its mediator, control point, observation, validation, and effect on future decision cost.

```text
total_description_cost
= core_model_length
+ routing_rule_length
+ state_injection_length
+ validation_observation_length
+ exception_patch_length
+ failure_recovery_length
```

## 8. Task and Meta Loops

```text
Decision Object -> VOI Gate -> smallest probe or direct action -> result -> Human Gate / stop
```

```text
trace -> repeated/high-impact failure -> mutation candidate -> behavior eval -> approval -> promotion/rollback
```

Never promote a permanent rule from one attractive case. More complete prose is not evidence of lower decision error or lower attention cost.

## 9. Candidate Mutation Gate

A mutation enters the queue only when it is repeated or high-impact, can change a system decision or reduce major risk, is repairable, reusable, evidenced, reversible, cheaper than its expected benefit, tested against a counterexample, and has a stop rule.

## 10. AI Fatigue and Anti-Generic Output

```text
open branches -> map to decisions -> keep action-changing branches -> archive model learning -> close consumption -> choose one probe
```

Preserve local facts, negative feedback, failure details, provenance, constraints, and action impact. Added headings and abstract structure without added decision boundaries, signals, costs, or actions are high-structure/low-VOI output.

## 11. Permission Ladder

| Level | Example | Default |
| --- | --- | --- |
| A0 | analysis, draft, VOI audit | automatic |
| A1 | read-only research, local inspection, log sampling | automatic with decision/cost trace |
| A2 | docs, templates, candidate skill files, reversible experiment | automatic with backup, validation, and stop rule |
| A3 | long-term memory, global skill install, production policy | Human Gate |
| A4 | deletion, publishing, money, real-user impact | explicit approval |

## 12. Public Skill Checks

The package must keep names aligned, keep `SKILL.md` lightweight, route to one-hop references and templates, include decision/default-action/signal-to-action/cost/stop fields, cover VOI failure cases in behavior evals, preserve public/private boundaries, and retain rollback.
