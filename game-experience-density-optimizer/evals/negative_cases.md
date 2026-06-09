# Negative Cases

## Scientific Overclaim

Bad output:

```text
体验浓度公式已经证明能提升留存，因此 D1 必然上升。
```

Required correction: mark `theory_status: design_hypothesis`, and state that real telemetry is required.

## Frequency First

Bad output:

```text
玩家看不懂，所以先把事件频率提高一倍。
```

Required correction: diagnose `CLP` first. Do not add events before reducing noise.

## Boredom Means Add Events

Bad output:

```text
玩家说无聊，所以当前刺激太低，B 组把怪物、弹窗和任务频率都提高。
```

Required correction: first output `optimal_stimulation_fit` and `boredom_type`. Boredom can be `under_stimulation`, `over_stimulation`, `habituation`, `low_agency`, `low_meaning`, `mixed`, or `unknown`.

## False Density

Bad output:

```text
给更多红点、弹窗和弱奖励，让玩家每分钟看到更多东西。
```

Required correction: weak prompts without meaningful decisions or salient feedback do not improve ED.

## Multi-Lever Confound

Bad output:

```text
B 组同时改奖励、UI、剧情、战斗难度、镜头和商业化。
```

Required correction: each variant keeps one primary lever and a rollback path.

## FEP Overclaim

Bad output:

```text
根据自由能原理，这个方案已经从神经科学上证明会让玩家进入心流。
```

Required correction: FEP is a design metaphor here. Mark `theory_status: design_hypothesis` and validate with telemetry or playtest evidence.

## Novelty Amount Fallacy

Bad output:

```text
SDT 需要 novelty，所以我们把新规则、随机事件和信息层都加倍。
```

Required correction: SDT novelty must be treated as optimal, learnable novelty. Output `optimal_novelty_fit`; if novelty is random, overwhelming, or not attributable, treat it as `CLP` or `too_high`, not as a positive.

## Markov Blanket Buzzword

Bad output:

```text
手感不好是马尔可夫毯问题，所以 B 组同时改输入、镜头、UI、敌人 AI、奖励和关卡节奏。
```

Required correction: identify the concrete coupling break, such as latency, noise, unclear mapping, weak agency, or overload. Keep one primary lever per variant.

## Single-Player Metric Mismatch

Bad output:

```text
这是买断制单机 Demo，所以 P1 直接用 D1/D7 和连续登录天数。
```

Required correction: for `premium_single_player`, use total journey metrics such as total playtime, demo/chapter completion, core-loop reach, replay intent, and review/refund risk if available. D1/D7 are not default P1 unless the project has explicit liveops or return-cadence goals.

## Mobile Metric Mismatch

Bad output:

```text
这是长线手游活动，只看总游戏时长上升即可，不需要看每日和持续天数。
```

Required correction: for `mobile_liveops`, include D1/D3/D7/D30, daily active sessions, consecutive active days, event retention, return-session quality, and fatigue/complaint gates.

## No Anti-habituation For Long-term Fatigue

Bad output:

```text
老玩家疲劳，所以把奖励数值翻倍并增加每日任务次数。
```

Required correction: when the case involves seasons, looters, roguelikes, UGC, old players, repeat loops, or long-term fatigue, output `anti_habituation_plan` with a lever such as `alternative_use`, `attention_investment`, `conscious_reframing`, `context_shift`, or `combinatorial_depth`.

## No Evidence Gate

Bad output:

```text
玩家说首局空，所以真实原因是事件太少，直接提高首局怪物和奖励频率。
```

Required correction: first declare `evidence_gate`. With only text, use `L0_text_only` and `evidence_status: assumption_only`; output a hypothesis and minimum validation plan, not a factual cause.

## Static Screenshot Tempo Claim

Bad output:

```text
从截图可以看出玩家会在第 90 秒退出，所以 B 组调整 90 秒后的节奏。
```

Required correction: screenshots can support static UI and visual-noise judgments, but cannot prove real pacing, feel, or exit timing. Request recording/playtest/telemetry or downgrade the claim.

## Wrong Output Density

Bad output:

```text
用户只问“首局太空，快速看一下”，于是输出完整 19 个模块和 4 页报告。
```

Required correction: use `quick_ed_triage` for one-line quick requests. Output one boundary, one stimulation-window judgment, one primary lever, two minimal changes, three metrics, and one rollback condition.

## Hybrid Single-Win Fallacy

Bad output:

```text
活动 D7 上升，所以 hybrid 项目整体成功，主线完成率下降可以忽略。
```

Required correction: `hybrid` must split total-journey P1 and liveops P1. If either critical horizon is harmed, do not declare overall success; review negative gates and choose iterate, rollback, or a split experiment.

## Review Without Negative Gates

Bad output:

```text
P1 上升了，直接放大，不需要看投诉、失败率、经济或数据质量。
```

Required correction: `review_and_decide` must check data quality and negative gates before P1/P2 interpretation. A P1 lift contaminated by technical, economy, fairness, fatigue, or dark-pattern risk is not a clean win.
