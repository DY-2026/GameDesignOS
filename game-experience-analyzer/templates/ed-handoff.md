# ED Handoff

Use this template only after `sample_boundary` and `evidence_index` exist. It lets `game-experience-density-optimizer` design experiments without repeating the full experience analysis.

```yaml
handoff_id: EDH001
source_skill: game-experience-analyzer
target_skill: game-experience-density-optimizer
case_boundary:
  sample_type: ""
  supported_judgment_scope: []
  unsupported_judgment_scope: []
  key_unknowns: []
issue_cards_for_ed:
  - issue_id: I001
    evidence_refs:
      - E001
    symptom: ""
    ed_terms:
      - CLP
    suggested_primary_lever: ""
    secondary_noise: ""
    confounder_risk: ""
    confidence: 0.5
    unknowns: []
    unsupported_by_sample: false
recommended_next_step: "Use game-experience-density-optimizer to build a one-week ED experiment plan."
```

## Rules

- Every `issue_cards_for_ed` item must cite at least one `evidence_id`.
- Use `unsupported_by_sample: true` when a screenshot, trailer, store page, or inaccessible link cannot support rhythm, handfeel, retention, or business-result claims.
- `suggested_primary_lever` must name one main experimental lever only.
- Put likely noise into `secondary_noise` and attribution risks into `confounder_risk`.
- Do not convert this handoff into a release recommendation. It is an experiment input.
