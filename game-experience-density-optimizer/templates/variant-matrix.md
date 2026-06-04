# Variant Matrix

| variant_id | purpose | primary_lever | concrete_change | impact_window | owner | risk | rollback |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_control | 对照组 | none | 保持当前版本 | current session | unknown | none | none |
| B_event_frequency | 测试有效事件频率 | event_frequency | unknown | 30-120 sec | design/client | false_density | config off |
| C_decision_weight | 测试选择重量 | decision_weight | unknown | 60-120 sec | design/system | difficulty_spike | config off |
| D_narrative_compression | 测试叙事压缩 | narrative_compression | unknown | 30-180 sec | narrative/design | emotion_loss | config off |

## Variant Notes

每个变体只保留一个主旋钮。具体改动必须写到可配置对象，例如关卡刷怪表、奖励表、任务链、剧情包、UI 提示、Build 选项或配置开关。
