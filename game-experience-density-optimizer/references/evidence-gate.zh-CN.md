# 证据门：把材料强度转成允许结论

本文件用于让 `game-experience-density-optimizer` 在编译实验前先判断证据强度。证据等级决定可以说什么、必须降级什么、哪些结论禁止输出。

## 输出字段

```yaml
evidence_gate:
  evidence_level: L0_text_only | L1_static_assets | L2_recording | L3_playtest_notes | L4_telemetry_snapshot | L5_ab_result
  evidence_status: assumption_only | partial_evidence | directional_evidence | measured_evidence
  confidence: low | medium | high
  available_evidence:
    - ...
  allowed_claims:
    - ...
  forbidden_claims:
    - ...
  missing_evidence:
    - ...
  confounder_risks:
    - ...
```

`evidence_status` 默认保守：只有口述时是 `assumption_only`；静态素材和局部录屏通常是 `partial_evidence`；可追溯试玩记录或足够清晰的录屏可以是 `directional_evidence`；口径清楚的遥测或 A/B 结果才是 `measured_evidence`。

## 等级表

| 等级 | 材料 | 允许输出 | 禁止输出 |
| --- | --- | --- | --- |
| `L0_text_only` | 用户口述、会议纪要、无样本描述 | 设计假设、最小可回滚实验、埋点需求、需要补的证据 | 声称真实原因、承诺留存/总时长提升、推断玩家心理 |
| `L1_static_assets` | 截图、商店页、PV 截帧、静态 UI | 信息层级、视觉噪声、文案/入口风险、静态反馈可读性 | 判断真实节奏、手感、会话流失、玩家操作行为 |
| `L2_recording` | 录屏、试玩视频、可定位时间轴 | 时间轴断点、反馈窗口、首个有效选择时间、退出前行为、可观察操作问题 | 推断所有玩家群体、忽略录屏样本边界 |
| `L3_playtest_notes` | 试玩笔记、访谈摘要、QA 记录 | 玩家分群假设、问题卡、方向性实验、待验证指标 | 把小样本当总体结论、忽略访谈诱导和记录偏差 |
| `L4_telemetry_snapshot` | 指标快照、事件表、看板截图 | 分流方案、埋点核对、指标周期门、方向性实验 | 混版本、混渠道、混新老用户、直接宣布因果 |
| `L5_ab_result` | 预注册 A/B 结果、口径清楚的实验数据 | `review_and_decide`、放大/迭代/观察/回滚/Kill 判断 | 跳过负向门、数据质量门、样本门或预注册规则 |

## 默认允许结论

### L0_text_only

- 可以写“假设是……”
- 可以输出 A/B 最小实验。
- 可以输出埋点字典和证据补采清单。
- 必须写 `unsupported_claims`。

### L1_static_assets

- 可以判断静态信息层级、视觉噪声、入口暴露、反馈符号是否清晰。
- 不能把静态截图当作真实节奏、真实手感或真实留存证据。
- 如果涉及手感、节奏、退出点，必须要求录屏、试玩或遥测。

### L2_recording

- 可以从时间轴判断节奏空窗、反馈延迟、首个有效选择、认知负荷代理信号。
- 可以生成 `ed-handoff` 兼容的问题卡。
- 不能把单个录屏外推到所有玩家。

### L3_playtest_notes

- 可以提出玩家分群和体验原因假设。
- 必须标注样本量、样本来源、访谈偏差和记录偏差。
- 结论通常仍是 `directional_evidence`，除非有足够一致的量化记录。

### L4_telemetry_snapshot

- 可以设计分流、口径核对、指标树、看板和实验决策门。
- 必须检查 `client_version`、`channel`、`user_segment`、`time_window`、事件缺失和重复。
- 不得把指标相关性直接包装成设计因果。

### L5_ab_result

- 先读负向门和数据质量门，再看 P1。
- P1 改善但负向门触发时，不得宣布成功。
- Hybrid 项目中，总旅程 P1 和 liveops P1 必须分开判断。

## 混淆风险

输出时优先检查这些风险：

- `version_mismatch`：不同客户端版本混在一起。
- `channel_mix`：买量、自然、测试群、老玩家社区混在一起。
- `player_segment_mix`：新手、回流、老玩家、核心玩家混成平均值。
- `economy_change`：奖励、货币、付费、掉落同时变化。
- `difficulty_change`：难度变化掩盖体验浓度变化。
- `novelty_decay`：短期新鲜感被误判为长期改善。
- `instrumentation_missing`：关键事件缺失或重复。
- `post_hoc_success`：事后改胜利标准。
- `dark_pattern_contamination`：指标改善来自误导、焦虑或强迫。

## 降级规则

- 证据不足时，输出 `evidence_status: assumption_only` 或 `partial_evidence`。
- 无法确认游戏形态时，`game_metric_model: unknown`，并写明 D1/D7 或总旅程指标是否暂不适用。
- 无法确认刺激窗口时，`optimal_stimulation_fit.band: unknown`，不要自动加事件。
- 无法确认主旋钮时，优先输出两步方案：先补证据，再跑低风险实验。
- 任何真实账号、商业化、付费、经济、删除、发布或线上风险动作，都需要 Human Gate。
