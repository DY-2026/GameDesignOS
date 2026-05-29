# Issue Card / 诊断问题卡

问题卡用于把“感觉哪里不对”变成可分派、可验证的改动项。每张卡必须能回到 Evidence Index。

## 字段定义

| 字段 | 必填 | 规则 |
| --- | --- | --- |
| `issue_id` | 是 | `I001` 起，按优先级排序。 |
| `priority` | 是 | `P0` / `P1` / `P2` / `P3`。P0 必须影响核心目标或关键转化。 |
| `diagnosis_pack` | 是 | 引用诊断包 ID，不新造 mode。 |
| `symptom` | 是 | 用户或画面层可观察的问题现象。 |
| `evidence_refs` | 是 | 至少 1 个 `evidence_id`；样本不足时写 `unsupported_by_sample: true`。 |
| `root_cause_hypothesis` | 是 | 明确是假设还是证据支持结论。 |
| `impact` | 是 | 影响留存、转化、理解、节奏、付费、传播或立项判断中的哪一项。 |
| `fix_action` | 是 | 最小改动，不写空泛“优化体验”。 |
| `validation` | 是 | 验证方法和通过标准。 |

## 模板

```yaml
issue_id: I001
priority: P0
diagnosis_pack: ""
symptom: ""
evidence_refs:
  - E001
root_cause_hypothesis: ""
impact: ""
fix_action: ""
owner: ""
validation:
  metric: ""
  method: ""
  pass_threshold: ""
  stop_condition: ""
unsupported_by_sample: false
```

## 最小示例

```yaml
issue_id: I001
priority: P0
diagnosis_pack: "first_hour_retention_diagnosis"
symptom: "首战胜利后玩家还没看到下一轮目标，就被双倍奖励广告吸走注意力。"
evidence_refs:
  - E004
  - E005
root_cause_hypothesis: "商业化请求早于长期目标建立，导致首轮 Loop 的目标承接断裂。"
impact: "削弱首 10 分钟继续动机和首轮成就反馈。"
fix_action: "把双倍奖励广告延后到第二轮结算后，并在首轮结算先展示下一关目标。"
owner: "system_design"
validation:
  metric: "首 10 分钟继续率、第二关进入率、广告点击率"
  method: "A/B test"
  pass_threshold: "第二关进入率提升 >= 8%，广告点击率下降 <= 3%"
  stop_condition: "继续率无提升且广告收益下降 > 5%"
unsupported_by_sample: false
```
