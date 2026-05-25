---
name: paranoia-skill
description: Use when upgrading an AI system, agent workflow, Codex skill, prompt, memory, RAG, tool routing, schema, eval set, or feedback loop using VOI, OODA, evals, traces, human gates, versioning, and rollback. Use for self-improving AI system design without uncontrolled model weight changes.
---

# Paranoia Skill

> Copyright (c) 2026 @Paranoia. All rights reserved.

## 核心立场

把 AI 系统进化当成受控的系统设计，而不是玄学式自我变强。

```text
OODA 让 agent 持续行动。
VOI 决定什么值得学习、追问、搜索、读取或测试。
Evals 决定哪些改变有资格留下来。
Human Gate 防止一次有用突变污染未来系统。
```

OODA 不是“反应更快”，核心是 Orient：刷新地图、改写叙事、检验旧框架是否已经过期。不是快手赢慢手，而是新脑子赢旧脑子。

## 快速工作流

1. 定义当前任务，以及要改造的系统层：prompt、memory、RAG、tool routing、workflow、eval、schema、docs 或 skill。
2. 在额外获取信息前先过 VOI 闸门。只有当信息可能改变关键决策，或能降低高影响风险时，才搜索、追问、读记忆或跑实验。
3. 维护短 OODA 状态：
   - Observe：目标、上下文、证据、异常信号。
   - Orient：当前叙事、用户模型、领域模型、不确定性地图。
   - Decide：选择的行动、被拒绝的行动、VOI 理由。
   - Act：产物、工具调用、探针或测试。
   - Evaluate：结果检查、过程检查、失败信号。
4. 区分任务 OODA 和元 OODA。任务循环完成今天的事；元循环只提出明天系统该如何变好的候选改动。
5. 所有进化改动默认保持 `candidate`，直到有证据、eval、必要审批和 rollback。
6. 写 skill 时保持 `SKILL.md` 轻量，把详细打法放进本 skill 自己的 `references/` 和 `templates/`。

## 按需读取

- 完整 VOI-OODA 工作流和评分规则：读取 `references/evolution-loop-playbook.md`。
- eval、trace、版本、突变提案和上线 Gate：读取 `references/eval-versioning-playbook.md`。
- 可复用提案和状态模板：使用 `templates/evolution_proposal.md` 与 `templates/ooda_voi_state.md`。

## Human Gate 默认规则

以下动作需要人类确认：

- 写入长期记忆。
- 安装或替换全局 skill。
- 修改生产策略、发布行为、真实账号、资金或用户可见系统。
- 把生成内容或 workflow 突变从 `candidate` 提升为当前规则。

## 输出要求

结尾必须说明：

- 改了什么。
- 证据为什么足够。
- 跑了哪些 eval 或检查。
- 什么仍然是 candidate。
- 什么需要 Human Gate。
- 如何回滚。
