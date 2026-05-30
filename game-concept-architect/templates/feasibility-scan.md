# External Evidence Status / VOI Feasibility Gate

This file keeps the older `feasibility-scan` template name for compatibility, but the runtime model is VOI-based external evidence status.

## VOI Question

| Decision Point | Would Evidence Change This? | Why / Why Not |
| --- | --- | --- |
| design_nucleus | yes/no/unknown |  |
| target_audience | yes/no/unknown |  |
| platform_fit | yes/no/unknown |  |
| business_model | yes/no/unknown |  |
| scope_gate | yes/no/unknown |  |
| validation_plan | yes/no/unknown |  |
| go_no_go | yes/no/unknown |  |

## External Evidence Status

| Decision Point | Current Finding | Evidence Status | Design Impact | Next Step |
| --- | --- | --- | --- | --- |
|  |  | not-run/evidence-needed/partial/verified/contradicted |  |  |

## Minimal Example

| Decision Point | Current Finding | Evidence Status | Design Impact | Next Step |
| --- | --- | --- | --- | --- |
| design_nucleus | 需要判断“照料变形”是否比“布局改路”更易理解 | evidence-needed | 先做双候选灰盒测试，不写确定市场判断 | 查同类评论动机或做 5 人可理解性测试 |
| business_model | 当前原型不依赖商业化 | not-run | 商业模式只进 assumption ledger | 原型后再评估 |

## Quality Gate

- 没有证据时，必须写 `not-run` 或 `evidence-needed`。
- 不得为了完整而泛搜。
- 不得把未验证市场判断写成事实。
- 有证据时必须说明它改变哪个设计 gate。
