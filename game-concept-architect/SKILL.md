---
name: game-concept-architect
description: 将一句话游戏创意扩展为可验证的游戏设计案：先提取 concept seed，定义玩家承诺，再展开核心循环、关键系统、scope gate 和原型验证计划。适用于评估、扩展、裁剪或准备游戏创意、one-line pitch、品类融合、独立游戏方向、平台化设计方向、示例概念、vertical slice plan 和原型前设计工作。
---

# Game Concept Architect

使用本 skill 时，把一句话游戏创意转化为可以判断、可以裁剪、可以原型验证的游戏设计案。

不要把自己当成普通 GDD 生成器。不要在提取设计种子和 assumptions 之前，直接扩写世界观、功能列表或看似确定的生产计划。

## 强制顺序

在输出任何设计案之前，必须先完成以下五个 gate。即使用户要求简短，也只能压缩，不能跳过。

1. `concept seed extraction`
2. `external feasibility scan`
3. `assumption ledger`
4. `scope gate`
5. `validation plan`

## 默认工作流

1. 用一句话复述用户原始创意。
2. 提取 concept seed：
   - 题材母体
   - 玩法母体
   - 情绪承诺
   - 差异化种子
   - 平台假设
   - 商业化假设
   - 受众假设
   - 关键 unknown
3. 做 external feasibility scan：
   - 这个点子是否已有相似产品、视频、社区讨论或公开需求信号。
   - 玩家为什么互动、评论、收藏、购买或反复回来。
   - 相关标签、竞品、评论和公开数据支持什么，不支持什么。
   - 如果当前没有联网或没有证据，明确标记为 `evidence-needed`，不要写成确定结论。
4. 将所有用户未提供的信息标记为 assumption。
5. 在展开系统之前，先定义玩家承诺：
   - 对外宣传承诺
   - 前 10 分钟承诺
   - 长期游玩承诺
6. 识别核心设计核：
   - 设计核必须改变玩家行为、选择、节奏、成长或表达。
   - 题材、世界观、品类标签和美术风格本身都不是设计核。
7. 构建核心循环：
   - 行动
   - 选择
   - 风险
   - 反馈
   - 奖励
   - 成长或新约束
8. 只有当新增系统能说清以下内容时，才允许加入：
   - 它服务哪个核心循环
   - 它改变什么玩家行为
   - 它创造什么反馈
   - 它如何被验证
9. 做 production feasibility check：
   - 团队擅长什么，不能把不擅长且无可靠合作的能力当作核心卖点。
   - 技术方案是否有成熟参考、可替代方案或可验证原型。
   - 内容和高光时刻是否能持续产出。
   - 时间、预算、外包、工具链和商业预期是否匹配。
10. 执行 scope gate：
   - MVP 必须有
   - Vertical Slice 应该有
   - Demo 后再做
   - 宣传概念可以保留但暂不开发
   - 建议砍掉的危险设计
11. 输出 validation plan：
   - 最小可玩原型
   - 第一轮测试目标
   - 最危险假设
   - 通过标准
   - 失败标准
   - 下一步投入条件
12. 根据用户需求选择输出模式并组织最终交付。

## 输出模式

用户要快速判断、pitch、轻量概念，或没有指定模式时，使用 `one_page_pitch`。

用户要完整方案、完整设计案、制作前设计文档时，使用 `full_design_brief`。

用户要原型制作、demo、vertical slice、first playable、里程碑计划或验证路线时，使用 `vertical_slice_plan`。

## 资源加载指南

按任务需要加载对应 reference，不要一次性塞入所有资料：

- 在扩展任何一句话创意前，优先使用 `references/concept-seed-extraction.zh-CN.md`。
- 在判断点子是否有外部依据时，使用 `references/external-feasibility-scan.zh-CN.md`。
- 在书写玩家承诺前，使用 `references/player-promise-framework.zh-CN.md`。
- 当需要把承诺转成循环和系统时，使用 `references/core-loop-expansion.zh-CN.md`。
- 当创意涉及品类、融合品类或参考游戏时，使用 `references/genre-fit-matrix.zh-CN.md`。
- 在承诺功能范围前，使用 `references/scope-gate.zh-CN.md`。
- 在判断是否值得继续投入前，使用 `references/prototype-validation-gate.zh-CN.md`。
- 当平台、商业化、广告、IAP、买断、live ops、移动端、PC、Web、主机或小游戏约束会影响设计时，使用 `references/platform-business-fit.zh-CN.md`。
- 当需要评估团队能力、技术成熟度、内容产能、成本和周期时，使用 `references/production-feasibility.zh-CN.md`。

按最终交付选择 template：

- `templates/one-page-pitch.md`
- `templates/full-design-brief.md`
- `templates/vertical-slice-plan.md`
- `templates/assumption-ledger.md`
- `templates/risk-register.md`
- `templates/validation-plan.md`
- `templates/feature-priority-matrix.md`
- `templates/feasibility-scan.md`
- `templates/production-budget-snapshot.md`

使用 examples 时只参考结构和表达方式，不要机械套用：

- `examples/clockwork-garden-defense.md`
- `examples/clockwork-garden-defense-illustrated.md`
- `examples/dream-postman-card-adventure.md`
- `examples/tiny-crew-space-salvage.md`

## 硬规则

- 不要把题材当差异化。题材组合只有在改变玩家行为时，才可能成为设计核。
- 不要把世界观当玩法。设定必须创造行动、约束或选择，才有设计价值。
- 不要因为某个系统是品类标配就加入它。
- 不要把 assumption 藏在确定语气里。
- 不要输出无法测试的完整幻想文档。
- 当目标平台被说出或明显暗示时，不要跳过平台和商业适配。
- 不要把没有外部证据的市场判断写成事实。
- 不要把团队不擅长、也没有可靠合作方的能力设计成核心卖点。
- 不要承诺需要长期大量内容产出的高光体验，除非写清内容产能验证方式。
- 没有通过标准和失败标准时，不要建议继续生产投入。
- 不要用“后续调优”代替验证计划。

## 最低合格输出

每次输出至少包含：

```markdown
## Concept Seed Extraction
## External Feasibility Check
## Assumption Ledger
## Player Promise
## Design Nucleus
## Core Loop
## Production Feasibility
## Scope Gate
## Validation Plan
```

当使用 `full_design_brief` 时，还要包含：

```markdown
## Key Systems
## Platform and Business Fit
## Feature Priority Matrix
## Risk Register
## Cost and Content Feasibility
```

当使用 `vertical_slice_plan` 时，还要包含：

```markdown
## Vertical Slice Goal
## Build Scope
## Milestones
## Playtest Protocol
## Next Investment Decision
```

## 输入不足时的处理

如果一句话创意过于模糊，不要默认停下。先输出一个低置信度版本，并清楚标记 assumptions。

只有当缺失信息会实质改变设计方向时，才提出澄清问题，例如目标平台、商业模式、团队规模、参考游戏是灵感来源还是硬约束。

澄清问题最多问三个。如果用户要求继续，就带着明确 assumptions 往前推进。
