# Evolution Loop Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. System Definition

Self-evolving AI does not mean a model secretly changing its own weights. It means an AI application improving external system layers under stable goals:

- prompt
- memory
- retrieval
- tool routing
- workflow
- schema
- eval set
- skill reference

The loop is:

```text
real task pressure
-> WOOP Task Card
-> information scarcity
-> VOI choice
-> OODA probe
-> result feedback
-> candidate improvement
-> eval
-> Human Gate
-> versioned promotion
-> rollback path
```

## 2. WOOP Task Admission

Before VOI/OODA, translate the task into an executable `WOOP Task Card`:

- Wish: task goal, artifact, scope, and stop condition.
- Outcome: acceptance picture, evaluation rubric, and decision value.
- Obstacle: internal human-AI system Failure Pattern, not external difficulty.
- Plan: if-then protocol, judge, retry, fallback, or Human Gate.

Admission rules:

- If Wish is unclear, clarify, split, or enter exploration mode.
- If Outcome is unclear, do not enter production mode; define the rubric or draft only.
- If Obstacle is unclear, apply default Failure Patterns and lower autonomy.
- If Plan is unclear, do not automate high-risk or irreversible actions.

For the deeper method, read `references/woop-harness-protocol.en.md`.

## 3. Scarce Resources

An agent must treat these as scarce:

- tokens
- time
- user attention
- tool calls
- context window
- trustworthy feedback
- labeled samples
- money
- trust budget

Scarcity creates selection pressure. Selection pressure makes VOI necessary.

## 4. Quick VOI Estimate

Use this approximate formula:

```text
VOI = P(change_decision)
    x decision_delta_value
    x reuse_count
    - acquisition_cost
    - latency_cost
    - risk_cost
    - contamination_cost
```

Default actions:

| Uncertainty | Impact | Action |
| --- | --- | --- |
| High | High | Verify, experiment, or ask for approval |
| High | Low | Proceed with a default assumption and record the risk |
| Low | High | Run a lightweight check |
| Low | Low | Act directly |

## 5. Orient-first OODA

Do not turn OODA into a speed checklist. Its purpose is to refresh the cognitive map.

Observe should capture:

- surprising signals
- consequences of the last action
- missing source of truth
- tool failures
- user corrections
- cost and latency
- triggered or near-triggered WOOP Obstacles

Orient should capture:

- the current frame
- the old frame that may now be wrong
- the model that should replace it
- key uncertainties
- which information would change the map
- whether the WOOP Outcome is still the right evaluation rubric

Decide is not declaring truth. It is choosing the most valuable hypothesis to test now.

Act is not the end. When uncertainty remains, action should be a probe or pressure test that forces reality to answer.

## 6. Model Compression Gate

The Orient phase must explicitly inspect the current system model. Do not only ask "which prompt / workflow / skill should change?" Also ask:

- Is the current model too short, so it only watches the endpoint and cannot locate mediators?
- Is the current model too long, so routing, state, exception patches, and recovery rules consume execution capacity?
- Which mediator variable does this change improve?
- Is that mediator observable, intervenable, and verifiable?
- After the change, did total description cost fall, or did complexity move somewhere else?

Approximate total description cost:

```text
total_description_cost
= core_model_length
+ routing_rule_length
+ state_injection_length
+ validation_observation_length
+ exception_patch_length
+ failure_recovery_length
```

For the deeper method, read `references/model-compression-playbook.en.md`.

## 7. Task Loop and Meta Loop

Task loop:

```text
user goal -> context -> orientation -> action -> result
```

Meta loop:

```text
trace -> failure mode -> mutation candidate -> eval -> approval -> promotion
```

Never promote a long-term rule from a single case automatically.

## 8. Candidate Mutation Rules

A system change may enter the evolution queue only when it is:

- repeated or high-impact
- fixable
- reusable
- evidence-backed
- reversible

Otherwise, keep it as a task note.

## 9. Permission Ladder

| Level | Examples | Default Rule |
| --- | --- | --- |
| A0 | Analysis, draft text | Automatic |
| A1 | Read-only research, local checks | Automatic, but record it |
| A2 | Docs, templates, candidate skill files, model-audit fields | Automatic, but reversible |
| A3 | Long-term memory, global skill installation, production strategy | Human Gate required |
| A4 | Deletion, publishing, money, real-user impact | Explicit approval required |

## 10. Public Skill Package Check

For a public skill package, check at least:

- `SKILL.md` frontmatter `name` matches the folder name.
- `agents/openai.yaml` display name and default prompt match `SKILL.md`.
- The root README is human-facing; `SKILL.md` is agent-facing.
- `SKILL.md` stays lightweight and routes only to this skill's own `references/` and `templates/`.
- Reference files are one hop away and do not contain one-off rollout reports.
- Templates can be copied directly and support WOOP Task Card, evidence, model audit, eval, Human Gate, and rollback.
- Copyright, provenance, and reuse boundaries are explicit.
- A final stale-name and old-project wording sweep has run.

## 11. README Visual Asset Gate

README files can use generated images, but generated images should carry atmosphere, structure metaphors, and recognition, not critical text.

Before publishing, check:

- The image is stored inside the repository, not in a temporary generation folder.
- README uses relative paths and clear alt text.
- Critical process information also has Markdown, table, or Mermaid representation.
- The image has no watermark, obvious typo, brand infringement, or misleading UI text.
- Size and dimensions are appropriate for GitHub reading.
