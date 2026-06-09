# ED Scorecard

这个评分卡用于同一游戏、同一阶段、同一玩家分群内的相对比较。它不是科学量表，不用于跨品类排名。

```yaml
ed_scorecard:
  scope:
    experiment_id: unknown
    game_segment: unknown
    player_segment: unknown
    build_version: unknown
    evidence_level: L0_text_only | L1_static_assets | L2_recording | L3_playtest_notes | L4_telemetry_snapshot | L5_ab_result | unknown
    theory_status: design_hypothesis
  scores:
    MD_min:
      score: 0
      evidence: unknown
      risk: unknown
    SF:
      score: 0
      evidence: unknown
      risk: unknown
    EB:
      score: 0
      evidence: unknown
      risk: unknown
    AR:
      score: 0
      evidence: unknown
      risk: unknown
    CLP:
      score: 0
      evidence: unknown
      risk: unknown
  normalized_ed_proxy:
    status: relative_only
    confidence: low | medium | high | unknown
    formula_note: "ED = MD/min * (SF + EB + AR) / CLP, for same-scope comparison only"
  priority:
    primary_lever: CLP | SF | EB | AR | MD/min | unknown
    next_lever: CLP | SF | EB | AR | MD/min | not_yet | unknown
    reason: unknown
```

## 使用规则

- 分数只用于实验前后或 A/B 变体之间的相对解释，不用于跨游戏打分。
- `CLP` 是分母。`CLP` 高时，不要先提高事件频率。
- 每个分数都要附 `evidence`，证据不足时写 `unknown`，不要补脑。
- `primary_lever` 只能选一个。`next_lever` 只能作为后续实验，不要塞进同一变体。
- 如果 `evidence_level` 低于 `L2_recording`，评分卡只能作为假设，不得宣称真实体验变化。
