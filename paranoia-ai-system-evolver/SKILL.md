---
name: paranoia-ai-system-evolver
description: 用于升级 AI 系统、agent workflow、Codex skill、prompt、memory、RAG、tool routing、schema、eval set 或 feedback loop；需要 WOOP 任务准入、VOI/OODA、eval、Human Gate、versioning 与 rollback 的受控演化时使用。Use when controlled AI system evolution is needed.
metadata:
  short-description: 用 WOOP/VOI/OODA/Evals 受控进化 AI 系统
---

# Paranoia AI System Evolver

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 核心立场

把 AI 系统演化当成受控系统设计，而不是神秘的自我改良。

```text
模型质量决定系统是否可控。
WOOP 把任务意图、验收结果、失败模式和 if-then 恢复计划变成 harness 控制面。
OODA 让 agent 持续贴近现实。
VOI 决定什么值得学习、询问、检索、阅读或测试。
Evals 决定哪些改动值得留下。
Human Gate 防止一次有用突变污染长期系统。
Rollback 让每次提升都可逆。
```

WOOP 在本 skill 里不是心理激励，而是任务进入、执行监控、失败恢复的 harness 协议。Wish 是 `Intent Spec`，Outcome 是 `Evaluation Rubric`，Obstacle 是人机系统的 `Failure Pattern`，Plan 是可触发的 `If-Then Protocol`。

OODA 不是比谁反应快。重心在 Orient：刷新地图，重写框架，测试旧叙事是否已经过期。

好的 AI engineering 不是堆 prompt、tool、skill 和 workflow，而是把任务变成可执行模型：足够短，能复用；足够因果化，能暴露控制点；足够明确，能验证、恢复和修正。

## 何时使用

用于改动这些层：

- prompt、system instruction、memory、RAG、tool routing、workflow、schema、eval set、docs 或 Codex skill
- agent feedback loop、trace format、release gate 与 rollback policy
- 需要轻入口、清晰 reference、可验证和可版本化纪律的公开 skill package
- 需要 model compression、causal mediator、WOOP harness protocol 或 total description cost 降低的 AI engineering 结构

不要用它来合理化失控的模型权重改动、静默长期记忆写入、未经批准的全局 skill 安装，或没有 Human Gate 的生产影响行为。

## 快速流程

1. 定义当前任务和被改动的系统层：`prompt`、`memory`、`RAG`、`tool routing`、`workflow`、`eval`、`schema`、`docs` 或 `skill`。
2. 先写一张轻量 `WOOP Task Card`：
   - `Wish / Intent Spec`：任务目标、输出物、范围和边界是什么？
   - `Outcome / Evaluation Rubric`：什么结果算好？最好有 3 条验收标准或决策收益。
   - `Obstacle / Failure Pattern`：最可能破坏任务的人机系统内在失败模式是什么？不要写外部困难，要写可识别的误判、目标漂移、过度信任、上下文污染、工具滥用、虚假确定性等模式。
   - `Plan / If-Then Protocol`：如果失败模式出现，触发条件、判断者、动作、重试或交还人的规则是什么？
3. 用 WOOP 做任务准入：Wish 不清楚就先澄清或进入探索；Outcome 不清楚就不要进入生产模式；Obstacle 不清楚就用默认失败模式低自主推进；Plan 不清楚就不要自动执行高风险动作。
4. 在继续获取更多信息前，通过 VOI gate。只有当信息可能改变关键决策或降低高影响风险时，才搜索、追问、读记忆或实验。
5. 显式写出 operating model：
   - compression：什么短模型能解释多数真实案例，而不是堆补丁？
   - causality：哪些 mediator 把输入连接到目标结果？
   - control points：agent、workflow 或 human 能干预哪个 mediator？
   - cost：core model、routing、state、validation、exception、recovery 的成本在哪里累积？
6. 维护紧凑 OODA 状态：
   - Observe：目标、上下文、证据、惊讶信号、触发过的 Obstacle。
   - Orient：当前框架、用户模型、领域模型、WOOP 风险、 uncertainty map。
   - Decide：选择动作、拒绝动作、VOI 理由。
   - Act：artifact、tool call、probe 或 test。
   - Evaluate：用 Outcome 打分，用 Obstacle 查风险，用 Plan 处理触发项。
7. 分离 task OODA 和 meta OODA。任务循环完成今天的工作；元循环只提出明天系统可考虑的 `candidate` 改动。
8. 每个演化改动都保持 `candidate`，直到证据、eval、必要审批和 rollback 都存在。
9. 当目标层是 `skill`，增加行为回归门：回放代表性任务，对比改动前后的预期行为，检查负迁移，并在证据不足时保持 `candidate`。

## 按需读取

- WOOP 任务准入、执行监控和失败恢复协议：`references/woop-harness-protocol.zh-CN.md`；英文备份：`references/woop-harness-protocol.en.md`。
- 完整 VOI/OODA 工作流与评分规则：`references/evolution-loop-playbook.zh-CN.md`；英文备份：`references/evolution-loop-playbook.en.md`。
- Model compression、causal mediator、control point 与 total description cost：`references/model-compression-playbook.zh-CN.md`；英文备份：`references/model-compression-playbook.en.md`。
- Eval、trace、versioning、promotion 与 rollback 规则：`references/eval-versioning-playbook.zh-CN.md`；英文备份：`references/eval-versioning-playbook.en.md`。
- 可复制工作表单：
  - 默认中文：`templates/evolution_proposal.md` 与 `templates/ooda_voi_state.md`
  - 中文显式版：`templates/evolution_proposal.zh-CN.md` 与 `templates/ooda_voi_state.zh-CN.md`
  - 英文备份：`templates/evolution_proposal.en.md` 与 `templates/ooda_voi_state.en.md`

## Human Gate 默认项

执行以下动作前必须询问人：

- 写入长期记忆
- 安装或替换全局 skill
- 改动生产策略、发布行为、真实账号、资金或用户可见系统
- 把生成内容或 workflow mutation 从 `candidate` 提升为当前规则
- 删除、镜像、批量移动或覆盖项目工作区

## 输出契约

结束时说明：

- 改了什么
- WOOP Task Card 中的 Wish、Outcome、Obstacle、Plan 如何落到结果里
- 证据为什么足够
- 哪些 eval 或检查已经运行
- 哪些仍然是 `candidate`
- 哪些需要 Human Gate
- 如何 rollback
