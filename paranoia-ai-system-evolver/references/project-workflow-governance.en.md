# Project Workflow Governance Playbook

`paranoia-ai-system-evolver` is the cross-workflow governance layer in GameDesignOS. It does not replace domain skills.

It checks:

- Intent Work Order: what reality should change, who verifies it, what cannot be sacrificed, and where AI autonomy ends;
- Decision Object / VOI: which decision this workflow serves, the current default action, and which information can change action;
- UL (Uncertainty Ladder): optional exposure control, bottleneck attribution, transfer checks, and fallback;
- RJR-AI: authority boundaries for AI, workflow, eval, automation, and human residual judgment;
- Drift Gate: low-VOI research, branch explosion, over-structured output, weak evidence, or scope drift;
- Human Gate / rollback: which commitments require human approval and how failure is reversed;
- Candidate Learning: retrospective rules stay candidate before promotion through `shadow -> warn -> enforce -> rollbackable`.

Each `workflow-run.governance` block should keep:

```yaml
evolver_required: true
enforcement_mode: shadow
status: pending
intent_work_order_ref: null
decision_ref: null
voi_gate_ref: null
ul_state_ref: null
rjr_authority_ref: null
paranoia_review_ref: null
human_gate_refs: []
rollback_ref: null
candidate_learning_refs: []
retrospective_ref: null
```

UL is optional and should not force ordinary domain workflows to create extra state. Default `enforcement_mode` is `shadow`. Promote to `warn` or `enforce` only after representative evals show the checkpoint improves workflow quality without hiding useful domain work.
