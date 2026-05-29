# Validation Plan / 验证计划模板

验证计划只回答“下一步收集什么证据会改变判断”。不要把验证计划写成泛泛待办。

## 字段定义

| 字段 | 必填 | 规则 |
| --- | --- | --- |
| `validation_id` | 是 | `V001` 起。 |
| `target_judgment` | 是 | 需要验证或可能被推翻的判断。 |
| `evidence_refs` | 是 | 当前判断依赖的证据 ID；没有则写空数组并说明 unknown。 |
| `unknown_to_resolve` | 是 | 本次验证要消除的 unknown。 |
| `minimum_sample` | 是 | 最小样本材料、人数、时长或数据。 |
| `method` | 是 | `playtest` / `ab_test` / `store_page_ab` / `creative_test` / `telemetry_review` / `expert_review`。 |
| `metric` | 是 | 可观察指标。 |
| `pass_threshold` | 是 | 通过标准，必须可检查。 |
| `kill_condition` | 是 | 出现什么信号就停止或降级。 |
| `decision_after_result` | 是 | 结果对应的动作。 |

## 模板

```yaml
validation_id: V001
target_judgment: ""
evidence_refs:
  - E001
unknown_to_resolve: ""
minimum_sample: ""
method: ""
metric:
  primary: ""
  secondary: []
pass_threshold: ""
kill_condition: ""
decision_after_result:
  pass: ""
  fail: ""
```

## 最小示例

```yaml
validation_id: V001
target_judgment: "PV 有强热度潜力，但可玩性证明不足。"
evidence_refs:
  - E001
  - E003
unknown_to_resolve: "观众是否理解这是可实际操作的玩法。"
minimum_sample: "2 个 20 秒剪辑版本，每版 3000 次曝光。"
method: "creative_test"
metric:
  primary: "前 5 秒留存"
  secondary:
    - "点击率"
    - "评论中提到玩法的比例"
pass_threshold: "实机版前 5 秒留存不低于视觉奇观版，且玩法评论占比 >= 20%。"
kill_condition: "两版 CTR 都低于历史同品类素材 P25。"
decision_after_result:
  pass: "继续扩展实机证明镜头并制作 Steam 页面版本。"
  fail: "重做首秒卖点，不进入大规模投放。"
```
