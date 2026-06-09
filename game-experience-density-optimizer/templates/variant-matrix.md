# Variant Matrix

| variant_id | purpose | primary_lever | optimal_stimulation_target | concrete_change | config_keys | asset_changes | engineering_scope | impact_window | owner | qa_checks | secondary_noise | confounder_risk | rollback_signal | rollback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_control | 对照组 | none | current | 保持当前版本 | none | none | none | current session | unknown | 分流和埋点触发 | none | none | none | none |
| B_reduce_clp | 测试降噪 | CLP | reduce_overload / add_familiar_anchor | unknown | unknown | unknown | feature_flag / telemetry | 30-120 sec | design/ui/client | 关键路径可玩、无信息缺失 | unknown | missing_information | negative metric crosses guardrail | config off |
| C_raise_vertical_quality | 测试提质 | SF / EB / AR | improve_attributable_interest | unknown | unknown | unknown | feature_flag / asset_config / telemetry | 30-180 sec | design/3c/art/audio | 反馈不遮挡关键目标 | unknown | sensory_noise | negative metric crosses guardrail | config off |
| D_tune_md_frequency | 测试调频 | MD/min | add_semi_novelty_only_if_window_allows | unknown | unknown | unknown | feature_flag / spawn_or_choice_config / telemetry | 60-180 sec | design/system/level | 不提高 CLP、不破坏教学 | unknown | overload | negative metric crosses guardrail | config off |
| E_anti_habituation | 可选：测试反习惯化 | MD/min / system_depth | anti_habituation | unknown | unknown | unknown | feature_flag / economy_safe_config / telemetry | event cycle / run segment | design/system/liveops | 不破坏经济、公平和老玩家路径 | unknown | balance_shift | negative metric crosses guardrail | config off |

## Variant Notes

每个变体只保留一个主旋钮。`E_anti_habituation` 只有在老玩家、长线、赛季、刷子、肉鸽、UGC 或重复日常疲劳时才启用；不适用时不要为了完整而新增 E 组。具体改动必须写到可配置对象，例如 UI 层级、反馈资源、镜头/操控参数、音画氛围层、关卡刷怪表、奖励表、任务链、Build 选项或配置开关。

`optimal_stimulation_target` 用于说明变体服务刺激不足、过载、习惯化、低能动性还是低意义感；`prediction_error_target` 用于说明变体如何管理可控惊讶；`blanket_coupling_target` 用于说明它修复哪个行动-反馈边界。三者不能替代 `primary_lever`，也不能成为多系统同时改动的理由。

`config_keys`、`engineering_scope`、`qa_checks` 和 `rollback` 必须写到可派单粒度。不能只写“优化反馈”“调整节奏”“增强氛围”。
