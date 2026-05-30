---
case_type: synthetic_example
source_status: synthetic
contains_private_project_info: false
license_status: repo_safe
intended_use: skill_behavior_demo
---

# Game Experience Analyzer 示例索引

本目录只收录可公开展示或完全合成的样例。新增示例必须先给 `sample_scope_gate`，再声明 `diagnosis_pack` 与 `primary_mode`；`diagnosis_pack: none` 只表示当前输入没有命中已命名诊断包，仍然必须走 `analysis-mode-router`，不得新增泛泛分析模式。

| status | example | input_type | diagnosis_pack | main_mode | confidence_boundary | output_file |
| --- | --- | --- | --- | --- | --- | --- |
| current | Survival 33 Days gameplay recording review | `video_url` / gameplay recording | `first_hour_retention_diagnosis` | `early_experience` | Public gameplay recording sample with page metadata and sampled keyframes; supports first-session flow, Hook/Loop/Link/Surprise evidence, feature exposure/unlock/first-use ledger, and UI density. It does not support claims about real D1/D7/D30 retention, revenue, paid conversion, official balance, or complete player sentiment. | [`survival-33-days-gameplay-experience-report.md`](./survival-33-days-gameplay-experience-report.md) |
