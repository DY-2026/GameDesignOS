# VOI Feasibility Gate

目的：外部证据用于降低关键不确定性，不是为了让每个创意都先泛搜一轮。只有当信息会改变设计决策时，才值得调研。

## 何时需要外部调研

如果答案会改变以下任一项，则外部信息有 VOI：

| 决策点 | 可能改变什么 |
| --- | --- |
| `design_nucleus` | 选择哪个设计核，或是否需要 pivot |
| `target_audience` | 先服务哪类玩家 |
| `platform_fit` | 输入方式、局长、信息密度、分发渠道 |
| `business_model` | 买断、广告、IAP、订阅、B2B、品牌传播等 |
| `scope_gate` | MVP 和 Vertical Slice 的边界 |
| `validation_plan` | 最小原型、指标、通过/失败标准 |
| `go_no_go` | 继续、降 scope、pivot 或暂停 |

## Evidence Status

| 状态 | 定义 | 输出语气 |
| --- | --- | --- |
| `not-run` | 当前没有做外部调研，且 VOI 不足或用户未要求 | “未运行；原因是...” |
| `evidence-needed` | 决策高度依赖证据，但当前没有来源 | “需要验证；不得视为事实” |
| `partial` | 有间接证据，但不足以支持确定判断 | “初步支持/冲突，仍需验证” |
| `verified` | 有当前公开来源、评论、数据或用户材料支持 | “证据支持 X，因此调整 Y” |
| `contradicted` | 证据与原假设冲突 | “降低优先级、pivot 或重测” |

## 最小调研问题

不要泛搜“这个题材有没有市场”。先写具体问题：

- 哪个设计核候选更容易被玩家理解？
- 目标平台上同类操作的局长和输入负担是否匹配？
- 玩家评论中真正想要的是题材、操作、挑战、社交、收集，还是表达？
- 商业模式是否会破坏玩家承诺？
- 竞品差评暴露的缺口是否正好是本设计要解决的点？

## 最小示例

```markdown
## External Evidence Status

| 决策点 | VOI 判断 | Evidence Status | 证据/缺口 | 对设计的影响 |
| --- | --- | --- | --- | --- |
| design_nucleus | 会影响 N1/N2 选择 | evidence-needed | 需要查看塔防+培育混合玩法的评论动机 | 原型先验证照料因果，再决定是否增加布局复杂度 |
| business_model | 当前不会改变最小原型 | not-run | 用户未指定商业模式，MVP 不依赖付费结构 | 仅作为 assumption 记录 |
```

## 质量门

- 没有证据时，必须写 `not-run` 或 `evidence-needed`。
- 不得把未查证的市场、受众、竞品或商业判断写成事实。
- 不得为了显得完整而泛搜；先写 VOI 原因。
- 如果外部证据会改变 Go/No-Go，必须进入 validation plan。
