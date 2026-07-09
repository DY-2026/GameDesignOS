# GameDesignOS Workflows

These workflow guides describe how existing skills write durable assets into a GameDesignOS project workspace.

> 中文摘要：工作流文档不是新的 skill，而是规定已有 skill 如何读取上游资产、用 VOI 判断是否需要更多信息、把结果写回 workspace，并在关键节点进入 Human Gate。

## Cross-Cutting Route

- [Decision to Information](./decision-to-information.md): define the decision, current default action, boundary, information actions, EVSI probe, and stop rule before research expands.

## Project Governance Checkpoints

`$paranoia-ai-system-evolver` is a cross-cutting governance layer for every workflow, not a replacement for the domain skill that owns the work.

Each workflow should expose these checkpoints in `workflow-run.governance`:

1. intake intent: convert vague instructions into an Intent Work Order when the task is open-ended;
2. VOI/RJR boundary: name the Decision Object, `current_default_action`, authority level, residual judgment, and Human Gate trigger;
3. midstream drift: check branch explosion, scope creep, low-VOI research, missing evidence, and over-structured output;
4. delivery gate: verify first-glance acceptance, non-sacrifice constraints, rollback, and unsupported claims;
5. retrospective learning: persist only candidate rules until eval evidence and Human Gate justify promotion.

Default enforcement is `shadow`. Move to `warn` or `enforce` only after representative evals show that the checkpoint improves output without hiding useful domain work.

## Core Production Routes

- [Idea to Validation](./idea-to-validation.md)
- [Media to Diagnosis](./media-to-diagnosis.md)
- [Weekly ED Experiment](./weekly-ed-experiment.md)
- [Evidence to Proposal](./evidence-to-proposal.md)

## Shared Rules

Every workflow must:

1. declare its input and evidence boundary;
2. identify the decision, owner, deadline, real options, and `current_default_action`;
3. inspect accepted decisions and upstream assets before asking the user to repeat context;
4. classify the decision boundary as `undefined`, `far`, `near`, or `locked`;
5. acquire new information only when a plausible signal can change action, priority, allocation, or a stop condition;
6. generate no more than three candidate information actions per VOI round;
7. prefer the smallest sample or experiment with positive net value after acquisition, delay, attention, privacy, and contamination costs;
8. route to the smallest suitable skill;
9. save outputs to the documented workspace area and update asset relationships;
10. distinguish observations, interpretations, assumptions, model learning, consumption, and decisions;
11. preserve local negative evidence instead of washing it into generic prose;
12. end with a next action, Human Gate, or explicit research stop condition;
13. write workflow governance refs for intent, VOI/RJR, Human Gate, rollback, and candidate learning;
14. avoid publishing private project material back to the public repository.

The full method lives in [`paranoia-ai-system-evolver/references/value-of-information-playbook.zh-CN.md`](../../paranoia-ai-system-evolver/references/value-of-information-playbook.zh-CN.md).
