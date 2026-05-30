# External Evidence Status

这个文件保留旧文件名，便于已有引用不失效。当前规则以 `references/voi-feasibility-gate.zh-CN.md` 为准：外部证据由 VOI 决定，不强制联网，不做泛搜。

## 使用原则

| 原则 | 说明 |
| --- | --- |
| 先判断 VOI | 外部信息是否会改变 design nucleus、target audience、platform fit、business model、scope gate、validation plan 或 Go/No-Go |
| 没有证据就标注 | 使用 `not-run` 或 `evidence-needed`，不要写成确定市场判断 |
| 只查关键问题 | 不泛搜“有没有市场”，而是查会改变设计决策的问题 |
| 证据回写 gate | 查到的证据必须影响某个设计 gate，否则只是噪音 |

## Evidence Status

| 状态 | 定义 |
| --- | --- |
| `not-run` | 当前未运行外部调研，且 VOI 不足或用户未要求 |
| `evidence-needed` | 关键判断需要证据，但当前没有来源 |
| `partial` | 有间接证据，但不足以支持确定判断 |
| `verified` | 有当前公开来源、评论、数据或用户材料支持 |
| `contradicted` | 外部证据与创意假设冲突 |

## 最小示例

```markdown
## External Evidence Status

| 决策点 | VOI 判断 | Evidence 状态 | 对设计的影响 | 下一步 |
| --- | --- | --- | --- | --- |
| design_nucleus | 会影响 N1/N2 选择 | evidence-needed | 先不把市场需求写成事实 | 查评论动机或做 5 人可理解性测试 |
| business_model | 当前不会改变最小原型 | not-run | 仅记录为 assumption | 原型通过后再评估 |
```

## 质量门

- 没有当前证据时，不得输出“市场已验证”“玩家一定喜欢”等确定结论。
- 外部调研必须说明 VOI，不能为了完整而泛搜。
- 如果外部证据与原假设冲突，必须调整设计核、scope gate 或 validation plan。
