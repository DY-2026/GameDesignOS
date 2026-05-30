# 模型压缩 Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. 核心判断

升级 AI 系统时，先问一句：这个系统到底在按什么模型工作？

一个 prompt、skill、agent、workflow 或 harness，如果只是把场景流程写得更长，通常会变成补丁集合。好的系统升级应该把一类任务压缩成可复用、可组合、可验证的操作模型。

判断标准不是术语是否先进，而是：

```text
更短的核心描述
+ 更少的例外补丁
+ 更清楚的中介变量
+ 更可执行的控制点
+ 更可靠的验证和恢复
```

## 2. 好调节器视角

想控制一个系统，调节器本身必须包含那个系统的模型。对 AI 工作流来说，调节器可以是：

- prompt
- skill
- agent loop
- workflow
- tool routing
- memory schema
- eval gate
- human review gate
- rollback policy

如果调节器的模型过粗，就会欠拟合：只盯最终结果，无法定位哪里坏了。

如果调节器的模型过细，就会过拟合：规则太多，路径太碎，状态和例外补丁吞掉执行能力。

## 3. 最小描述长度 Gate

用这个近似判断模型颗粒度是否合适：

```text
model_score = core_model_length
            + data_patch_length
            + routing_rule_length
            + state_injection_length
            + validation_observation_length
            + exception_patch_length
            + failure_recovery_length
```

升级目标不是让每一项都最小，而是让总描述成本下降，同时不牺牲关键结果质量。

默认解释：

| 成本项 | 问题 | 降低方式 |
| --- | --- | --- |
| `core_model_length` | 核心规则太长，agent 记不住或迁移不了 | 抽出稳定操作，而不是堆场景名词 |
| `data_patch_length` | 每次都需要额外解释大量例外 | 找更好的中介变量或任务边界 |
| `routing_rule_length` | 入口判断越来越像 if-else 迷宫 | 合并同构任务，按信息变换路由 |
| `state_injection_length` | 每次执行都要塞大量上下文 | 外置状态，做 manifest/spec/state |
| `validation_observation_length` | 校验太重或看不到关键事实 | 只观测能改变决策的信号 |
| `exception_patch_length` | 每次失败都新增补丁 | 回到模型层修正，而不是继续贴胶布 |
| `failure_recovery_length` | 失败后恢复靠人记忆 | 固化 retry、rollback、冲突区和退出条件 |

## 4. 动词优先

优先按“信息如何被变换”建模，而不是按“这是什么场景”建模。

场景是名词：老板、前任、项目、文章、用户、竞品。

操作是动词：筛选、归档、翻译、压缩、路由、验证、对齐、回滚、转译、评分、对比、拆解。

好的 skill 更像游戏机制：可重复调用、可组合、可涌现。坏的 skill 更像关卡脚本：服务一个特定场景，失败后只能继续补丁。

## 5. 因果中介 Gate

不要只写：

```text
input -> final_output
```

要写：

```text
input -> mediator_1 -> mediator_2 -> final_output
```

中介变量是可诊断、可干预、可验证的中间节点。找到中介，系统才知道控制点在哪里。

常见 AI workflow 中介：

| 终点 | 常见中介 |
| --- | --- |
| 高质量答案 | 任务理解、上下文选择、状态保持、工具调用、过程校验、失败恢复 |
| 好 skill | 触发边界、核心操作、引用路径、模板复用、验证门、回滚路径 |
| 好 RAG | source quality、chunk boundary、retrieval intent、rerank、citation discipline、answer synthesis |
| 好 agent | observe fidelity、orientation model、decision policy、tool affordance、state update、eval signal |
| 好管理工作流 | 留存、转化、交付速度、信息流、决策效率、团队协作 |

如果一个改动不能说清楚它优化了哪个中介变量，它通常只是风格偏好，不应直接进入长期系统。

## 6. 控制点 Gate

每条中介链都要标出控制点：

```text
mediator:
  can_observe: true | false
  can_intervene: true | false
  intervention:
  eval_signal:
  failure_signal:
```

优先升级 `can_observe = true` 且 `can_intervene = true` 的节点。

只可观察、不可干预的节点适合做告警或诊断。

不可观察、却被当成核心控制点的节点，是高风险黑箱。

## 7. Harness / Agent / Skill 的模型差异

可以用同一套问题审计不同结构：

| 结构 | 好模型 | 坏模型 |
| --- | --- | --- |
| Harness | 把任务理解、状态保持、工具调用、校验、恢复显式化 | 只包一层外壳，仍靠模型单次发挥 |
| Agent | 明确 OODA、工具边界、状态更新和 eval 信号 | 无限循环、无退出条件、无证据门 |
| Skill | 把一类操作压缩成可复用机制 | 把一个场景写成越来越长的脚本 |
| Workflow | 把上游信息转成下游更容易处理的形式 | 只安排角色、流程和口号 |
| Prompt | 明确任务模型、输入输出和失败信号 | 堆形容词和风格要求 |

## 8. 升级流程

每次升级按这个顺序走：

1. 写出当前系统隐含模型。
2. 标出输入、输出、中介变量、控制点。
3. 估算总描述成本，找出最高成本项。
4. 判断问题是欠拟合、过拟合，还是中介缺失。
5. 设计最小改动，让总描述成本下降。
6. 把改动标记为 `candidate`。
7. 用 eval 或真实任务样本检查它是否减少补丁、提升控制或降低恢复成本。
8. 需要长期生效时，经过 Human Gate 后再提升为规则。

## 9. 输出格式

```yaml
model_audit:
  current_model: ""
  proposed_model: ""
  compression_claim: ""
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

