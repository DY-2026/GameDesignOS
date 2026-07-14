# ED Handoff 最小契约

独立安装本 skill 时，上游 handoff 至少应提供：

- `schema_version`
- `sample_boundary`
- `evidence_status`
- `issue_cards`
- `unsupported_claims`
- `candidate_levers`
- `validation_constraints`

缺少样本边界、证据状态或不支持主张时，不得直接生成生产实验；先降级为 `assumption_only` 或返回上游补证据。
