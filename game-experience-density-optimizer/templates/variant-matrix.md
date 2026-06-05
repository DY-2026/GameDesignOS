# Variant Matrix

| variant_id | purpose | primary_lever | concrete_change | impact_window | owner | secondary_noise | confounder_risk | rollback_signal | rollback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_control | 对照组 | none | 保持当前版本 | current session | unknown | none | none | none | none |
| B_reduce_clp | 测试降噪 | CLP | unknown | 30-120 sec | design/ui/client | unknown | missing_information | negative metric crosses guardrail | config off |
| C_raise_vertical_quality | 测试提质 | SF / EB / AR | unknown | 30-180 sec | design/3c/art/audio | unknown | sensory_noise | negative metric crosses guardrail | config off |
| D_tune_md_frequency | 测试调频 | MD/min | unknown | 60-180 sec | design/system/level | unknown | overload | negative metric crosses guardrail | config off |

## Variant Notes

每个变体只保留一个主旋钮。具体改动必须写到可配置对象，例如 UI 层级、反馈资源、镜头/操控参数、音画氛围层、关卡刷怪表、奖励表、任务链、Build 选项或配置开关。
