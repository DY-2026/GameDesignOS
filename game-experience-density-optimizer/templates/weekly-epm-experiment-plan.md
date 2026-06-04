# Weekly ED / EPM Experiment Plan

## 1. Case Boundary

| 字段 | 值 |
| --- | --- |
| experiment_id | unknown |
| case_visibility | unknown |
| game_name | unknown |
| build_version | unknown |
| platform | unknown |
| target_user_segment | unknown |
| session_scope | unknown |
| available_evidence | unknown |
| evidence_status | unknown |

## 2. ED Diagnosis

| 公式项 | 当前判断 | 证据/观察 | 优先级 |
| --- | --- | --- | --- |
| CLP | unknown | unknown | unknown |
| SF | unknown | unknown | unknown |
| EB | unknown | unknown | unknown |
| AR | unknown | unknown | unknown |
| MD/min | unknown | unknown | unknown |

当前浓度问题：`unknown`

建议顺序：`先降噪 / 再提质 / 后调频 / unknown`

## 3. Experiment Hypothesis

```text
如果我们通过【主旋钮】改变【具体体验段】，玩家会在【影响窗口】内产生【行为变化】，并在【目标指标】上体现改善，同时不触发【负向门】。
```

## 4. Variant Matrix

| variant_id | primary_lever | concrete_change | impact_window | owner | risk | rollback |
| --- | --- | --- | --- | --- | --- | --- |
| A_control | none | 当前版本 | current session | design/data | none | none |
| B_clp_or_sf | CLP / SF | unknown | 30-120 sec | design/ui/client | unknown | config off |
| C_eb_or_ar | EB / AR | unknown | 30-180 sec | design/3c/art/audio | unknown | config off |
| D_md_frequency | MD/min | unknown | 60-180 sec | design/system/level | unknown | config off |

## 5. Instrumentation Dictionary

引用 `templates/instrumentation-dictionary.md`，至少包含：`variant_assigned`、`session_started`、`meaningful_decision_made`、`salient_feedback_fired`、`cognitive_load_signal`、`session_checkpoint`、`session_ended`。

## 6. Metric Plan

| 层级 | 指标 | 目标 | 口径 | 分群 |
| --- | --- | --- | --- | --- |
| P1 | unknown | unknown | unknown | new/returning/existing |
| P2 | ED proxy | unknown | same version/session | new/returning/existing |
| negative | unknown | no spike | pre-registered | all segments |

## 7. Dashboard Spec

引用 `templates/dashboard-spec.md`。默认过滤器：experiment_id、variant_id、user_segment、platform、channel、client_version、session_scope、checkpoint_id。

## 8. Decision Rules

| 决策 | 预注册条件 |
| --- | --- |
| amplify | unknown |
| iterate | unknown |
| observe | unknown |
| rollback | unknown |
| kill | dark pattern / negative gate / unsupported evidence |

## 9. Weekly Schedule

| 日期 | 目标 | 产物 |
| --- | --- | --- |
| 周一 | 冻结假设 | variant matrix / metric plan / risk gates |
| 周二 | 上版 | config / instrumentation / QA pass |
| 周三 | 阻断项检查 | crash / event missing / split balance |
| 周四 | 小复查 | TTE / ED proxy / exit point |
| 周五-周日 | 收样本 | segmented dashboard |
| 下周一 | 复盘决策 | amplify / iterate / observe / rollback / kill |

## 10. Handoff Checklist

| 角色 | 交付物 |
| --- | --- |
| design | 假设、变体、成功标准、风险门 |
| client | 开关位、埋点、回滚配置 |
| level/narrative/audio/art | 可上线内容与资源边界 |
| data | 看板、分群、数据质量门 |
| QA | 分流、埋点触发、回滚、关键路径可玩 |
