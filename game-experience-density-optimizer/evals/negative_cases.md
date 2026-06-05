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
