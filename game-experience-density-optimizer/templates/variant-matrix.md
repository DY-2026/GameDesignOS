# Variant Matrix

| variant_id | purpose | primary_lever | optimal_stimulation_target | prediction_error_target | blanket_coupling_target | concrete_change | impact_window | owner | secondary_noise | confounder_risk | rollback_signal | rollback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_control | 对照组 | none | current | current | current | 保持当前版本 | current session | unknown | none | none | none | none |
| B_reduce_clp | 测试降噪 | CLP | reduce_overload / add_familiar_anchor | reduce_unexplainable_error | lower_noise | unknown | 30-120 sec | design/ui/client | unknown | missing_information | negative metric crosses guardrail | config off |
| C_raise_vertical_quality | 测试提质 | SF / EB / AR | improve_attributable_interest | improve_attribution | improve_sensory_action_mapping | unknown | 30-180 sec | design/3c/art/audio | unknown | sensory_noise | negative metric crosses guardrail | config off |
| D_tune_md_frequency | 测试调频 | MD/min | add_semi_novelty_only_if_window_allows | add_controllable_surprise | preserve_readability | unknown | 60-180 sec | design/system/level | unknown | overload | negative metric crosses guardrail | config off |
| E_anti_habituation | 可选：测试反习惯化 | MD/min / system_depth | anti_habituation | restore_learnable_surprise | preserve_readability | unknown | event cycle / run segment | design/system/liveops | unknown | balance_shift | negative metric crosses guardrail | config off |

## Variant Notes

每个变体只保留一个主旋钮。`E_anti_habituation` 只有在老玩家、长线、赛季、刷子、肉鸽、UGC 或重复日常疲劳时才启用；不适用时不要为了完整而新增 E 组。具体改动必须写到可配置对象，例如 UI 层级、反馈资源、镜头/操控参数、音画氛围层、关卡刷怪表、奖励表、任务链、Build 选项或配置开关。

`optimal_stimulation_target` 用于说明变体服务刺激不足、过载、习惯化、低能动性还是低意义感；`prediction_error_target` 用于说明变体如何管理可控惊讶；`blanket_coupling_target` 用于说明它修复哪个行动-反馈边界。三者不能替代 `primary_lever`，也不能成为多系统同时改动的理由。
