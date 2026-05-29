# Eval and Versioning Playbook

> Copyright (c) 2026 @Paranoia. All rights reserved.

## 1. Eval Surfaces

Evaluate at least three surfaces:

| Surface | Question |
| --- | --- |
| Result | Did the output actually solve the task? |
| Process | Did the agent use VOI, tools, memory, and validation correctly? |
| Evolution | Does the candidate mutation improve future tasks without raising risk too much? |

## 2. Minimal Trace Fields

Each candidate improvement must preserve enough evidence for a future maintainer to reconstruct why it exists:

```yaml
trace_summary:
  task_id:
  user_goal:
  context_used:
  tool_calls:
  uncertainties:
  cost:
  result:
  feedback:
  failure_signals:
  candidate_improvements:
```

## 3. Mutation Proposal

Use this structure:

```yaml
proposal_id:
trigger:
evidence:
target_layer: prompt | memory | rag | tool | workflow | eval | schema | docs | skill
change_summary:
expected_benefit:
risk:
eval_plan:
human_gate:
rollback:
status: candidate
```

## 4. Minimum Eval by Layer

| Layer | Minimum Check |
| --- | --- |
| prompt | Replay representative tasks and compare instruction following and style match |
| memory | Include evidence, confidence, scope, expiry, and at least one counterexample check |
| RAG | Check source quality, retrieval precision, staleness risk, and citation behavior |
| tool routing | Check whether tools are used correctly, too early, too late, or not at all |
| workflow | Check source contract and output gate completeness |
| schema | Validate machine parsing and cover edge samples |
| skill | Check frontmatter, metadata, reference paths, template usability, stale wording, realistic invocation, and behavior regression |
| README visual | Check image path, alt text, no watermark, no misleading text, and text-backed critical flow |

## 5. Skill Package Regression Checklist

When editing a skill package, run at least:

```text
frontmatter name == folder name
agents/openai.yaml default_prompt uses the same skill name
all referenced files exist
templates are non-empty and copy-paste usable
root README is human-facing
SKILL.md is agent-facing and lightweight
no stale old name remains in public entrypoints
copyright/provenance is explicit
```

### Skill Behavior Regression Gate

Structural checks prove that a skill can be installed. They do not prove that it improves real work. A `target_layer: skill` candidate mutation must add behavior evidence:

- Choose 2-3 `behavior_samples` from real tasks or frequent scenarios, with input, expected behavior, and failure signals.
- Compare behavior before and after the change. If the old version cannot run, compare against the current `SKILL.md` output contract.
- Check for negative transfer: more verbosity, slower execution, false triggers, skipped VOI, weaker evidence use, or regression on high-value scenarios.
- If behavior does not improve, keep the change as `candidate` or a failure sample; do not promote it just because the structure looks cleaner.
- If behavior improves but description cost rises sharply, return to the model-compression gate and verify that the benefit covers the added complexity.

## 6. Version Management

Every accepted mutation needs:

- version id
- changed files
- reason for change
- eval evidence
- risk
- rollback path
- promotion date

Rejected mutations may be kept as searchable failure samples when they have retrospective value.

## 7. Promotion and Rollback

Do not promote a change as current rule when:

- eval is missing
- high-value tasks regress
- complexity increases without quality gain
- Human Gate is incomplete
- rollback is unclear

Rollback should restore the previous prompt, memory record, skill version, workflow doc, schema, or eval rule without touching unrelated project state.
