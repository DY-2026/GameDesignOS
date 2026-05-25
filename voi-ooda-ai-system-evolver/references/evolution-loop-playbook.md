# 进化闭环 Playbook

> Copyright (c) 2026 @Paranoia. All rights reserved.

## 1. 系统定义

自我进化 AI 不等于模型权重失控地自己改自己。它指的是 AI 应用在稳定目标下，持续改进外部系统：

- prompt
- memory
- retrieval
- tool routing
- workflow
- schema
- eval set
- skill reference

闭环是：

```text
真实任务压力
-> 信息稀缺
-> VOI 选择
-> OODA 探针
-> 结果反馈
-> 候选改进
-> eval
-> Human Gate
-> 版本化上线
-> rollback path
```

## 2. 稀缺资源

agent 必须把这些东西当成稀缺资源：

- token
- 时间
- 用户注意力
- 工具调用
- 上下文窗口
- 可信反馈
- 标注样本
- 金钱
- 信任额度

稀缺制造选择压力，选择压力逼出 VOI。

## 3. VOI 近似判断

使用这个快速估算：

```text
VOI = P(change_decision)
    x decision_delta_value
    x reuse_count
    - acquisition_cost
    - latency_cost
    - risk_cost
    - contamination_cost
```

四种默认行动：

| 不确定性 | 影响 | 行动 |
| --- | --- | --- |
| 高 | 高 | 查证、实验或请人审批 |
| 高 | 低 | 用默认假设推进，并记录风险 |
| 低 | 高 | 做轻量验证 |
| 低 | 低 | 直接行动 |

## 4. Orient-first OODA

不要把 OODA 做成奖励速度的清单。它的目标是刷新认知地图。

Observe 要抓：

- 惊讶信号
- 上一轮行动带来的后果
- 缺失的真源
- 工具失败
- 用户纠偏
- 成本与延迟

Orient 要抓：

- 当前叙事
- 可能已经错误的旧叙事
- 应该切换到的模型
- 关键不确定性
- 什么信息会改变地图

Decide 不是宣布真理，而是选择一个当前最值得下注验证的假设。

Act 不是结局；当不确定性仍然存在时，行动应当是一个探针或压力测试，用来逼现实表态。

## 5. 任务循环与元循环

任务循环：

```text
用户目标 -> 上下文 -> 定向 -> 行动 -> 结果
```

元循环：

```text
trace -> 失败模式 -> 突变候选 -> eval -> 审批 -> 上线
```

永远不要让元循环从单个案例自动提升出长期规则。

## 6. 候选突变规则

一个系统改动只有满足以下条件，才允许进入进化队列：

- 重复出现或高影响
- 可修复
- 可复用
- 有证据
- 可回滚

否则只保留为任务笔记。

## 7. 行动权限阶梯

| 等级 | 例子 | 默认规则 |
| --- | --- | --- |
| A0 | 分析、草稿文本 | 可自动 |
| A1 | 只读调研、本地检查 | 可自动，但要记录 |
| A2 | 文档、模板、候选 skill 文件 | 可自动，但要可回滚 |
| A3 | 长期记忆、全局 skill 安装、生产策略 | 需要 Human Gate |
| A4 | 删除、发布、资金、真实用户影响 | 必须明确审批 |

## 8. 公开 Skill 包检查

公开给别人使用的 skill 包，至少检查：

- `SKILL.md` frontmatter `name` 与文件夹名一致。
- `agents/openai.yaml` 的展示名、默认提示与 `SKILL.md` 一致。
- 根 README 面向人类；`SKILL.md` 面向 agent，不互相复制污染。
- `SKILL.md` 保持轻量，只路由到本 skill 自己的 `references/` 与 `templates/`。
- 参考文件是一层可达，不把一次性 rollout 报告塞进长期 reference。
- 模板可以直接复制使用，且字段能支持 evidence、eval、Human Gate 与 rollback。
- 版权、来源和复用边界清楚。
- 最后做一次陈旧命名和旧项目措辞扫描。

## 9. README 视觉资产 Gate

README 可以使用生成图，但生成图只适合承载氛围、结构隐喻和识别度，不应该承载关键文字信息。

发布前检查：

- 图片文件保存在仓库内，不引用临时生成目录。
- README 使用相对路径和明确 alt text。
- 关键流程另有 Markdown、表格或 Mermaid 版本。
- 图片没有水印、明显错字、品牌侵权或误导性 UI 文案。
- 图片体积和尺寸适合 GitHub 阅读。
