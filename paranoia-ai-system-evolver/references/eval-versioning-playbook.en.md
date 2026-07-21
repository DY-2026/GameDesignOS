# Eval and Versioning Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. Eval Surfaces

Evaluate at least three surfaces:

| Surface | Question |
| --- | --- |
| Result | Did the output actually solve the task? |
| Process | Did the agent use WOOP admission, a Decision Object, VOI, tools, memory, and validation correctly? |
| Evolution | Does the candidate mutation improve future tasks without raising risk too much? |

## 2. Minimal Trace Fields

```yaml
trace_summary:
  task_id:
  user_goal:
  woop_task_card:
  decision_object:
  voi_decision_gate:
  ul_state:
  context_used:
  tool_calls:
  uncertainties:
  cost:
  result:
  feedback:
  triggered_obstacles:
  if_then_actions:
  failure_signals:
  candidate_improvements:
```

## 3. Mutation Proposal

```yaml
proposal_id:
trigger:
evidence:
target_layer: prompt | memory | rag | tool | workflow | eval | schema | docs | skill
change_summary:
expected_benefit:
risk:
woop_task_card:
voi_decision_gate:
ul_state:
eval_plan:
human_gate:
rollback:
status: candidate
```

## 4. Minimum Eval by Layer

| Layer | Minimum Check |
| --- | --- |
| prompt | Replay representative tasks and compare instruction following, information density, and action closure |
| memory | Include evidence, confidence, scope, expiry, and at least one counterexample check |
| RAG | Check source quality, retrieval precision, staleness risk, citation behavior, and whether retrieval can change action |
| tool routing | Check whether tools are correct, premature, late, missing, or low-VOI |
| workflow | Check WOOP Task Card, Decision Object, source contract, uncertainty exposure, output gate, and stop rule completeness |
| schema | Validate machine parsing and edge samples |
| skill | Check frontmatter, metadata, VOI/WOOP/Uncertainty Ladder references, paths, templates, stale wording, realistic invocation, transfer, and behavior regression |
| README visual | Check image path, alt text, watermark, misleading text, and a text-backed critical flow |

## 5. Skill Package Regression Checklist

```text
frontmatter name == folder name
agents/openai.yaml default_prompt uses the same skill name
all referenced files exist
templates are non-empty and copy-paste usable
Decision Object and VOI stop-rule fields exist when the skill can trigger research or tools
WOOP Task Card fields exist when the skill controls task admission or recovery
UL State fields expose the current rung, released variables, attribution, transfer, and fallback
root README is human-facing
SKILL.md is agent-facing and lightweight
no stale old name remains in public entrypoints
copyright/provenance is explicit
```

### Skill Behavior Regression Gate

Structural checks prove installability, not better work. A `target_layer: skill` candidate must add behavior evidence:

- Choose 2-3 representative `behavior_samples` with input, expected behavior, and failure signals.
- Compare before and after behavior, or compare to the current `SKILL.md` contract.
- Check whether WOOP improves admission, evaluation, failure detection, and recovery rather than only adding text.
- Check negative transfer: more verbosity, slower execution, false triggers, skipped VOI, weaker evidence, or regression on high-value cases.
- Check that controlled fixture success proceeds through composition, bottleneck attribution, progressive release, and transfer before robustness is claimed.
- If behavior does not improve, keep the change as `candidate` or a failure sample.
- If behavior improves while description cost rises sharply, verify that benefit exceeds complexity.

### VOI Decision Gate Regression

Replay at least these situations:

- FOMO research without a decision object: timebox exploration rather than emit a long source list.
- A high-impact choice near the decision boundary: propose no more than three information actions and map signals to actions.
- All plausible signals imply the same action: stop research or reclassify it as model learning / information consumption.
- Perfect information is unavailable: compare the EVPI ceiling with practical EVSI and choose the smallest sample.
- Local negative evidence conflicts with macro narrative: preserve the local fact instead of smoothing it into generic prose.
- Many AI conversations remain open: map each branch to a decision and close low-VOI branches.

Pass only when the output names `current_default_action`, `boundary_status`, target uncertainty, costs, stop rules, and action change before/after information. If the framework only lengthens the response without accelerating action closure, treat it as a regression.

### UL Regression

Replay at least: fixture success requesting production authority; a failure after prompt/model/tool/memory/evaluation all changed; atomic checks passing while composition loses state; benchmark success that fails on a structurally similar novel task; repeated prompt exceptions around one tool failure; and a valid progression that releases one major variable while holding authority and evaluation stable.

Pass only when the output declares `current_rung`, `released_this_round`, `held_constant`, `attribution_confidence`, `graduation_evidence`, `transfer_checks`, and `fallback_rung`. If a confounded failure still promotes complexity or a permanent rule, treat it as a regression.

## 6. Version Management

Every accepted mutation needs a version id, changed files, reason, eval evidence, risk, rollback path, and promotion date. Rejected mutations may remain searchable failure samples when useful.

## 7. Promotion and Rollback

Do not promote when eval is missing, high-value tasks regress, complexity rises without quality gain, Human Gate is incomplete, rollback is unclear, or the VOI gate adds forms without reducing ineffective research.

Rollback should restore the previous prompt, memory record, skill version, workflow doc, schema, or eval rule without touching unrelated project state.
