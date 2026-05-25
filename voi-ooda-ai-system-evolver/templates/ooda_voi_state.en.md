# OODA / VOI State Template

> Copyright (c) 2026 @Paranoia. All rights reserved.

```yaml
ooda_state:
  observe:
    user_goal:
    context_used: []
    surprising_signals: []
    tool_results: []
  orient:
    current_frame:
    old_frame_risk:
    domain_model:
    user_model:
    uncertainty_map:
      - item:
        confidence:
        impact:
        action:
  voi:
    candidate_information_actions:
      - action:
        could_change_decision: "high | medium | low"
        decision_delta: "high | medium | low"
        reuse_value: "high | medium | low"
        cost: "high | medium | low"
        risk: "high | medium | low"
        conclusion: "do | skip | ask_human"
  decide:
    chosen_action:
    rejected_actions: []
    hypothesis:
  act:
    artifact_or_probe:
    permission_level: "A0 | A1 | A2 | A3 | A4"
  evaluate:
    result_check:
    process_check:
    failure_signals: []
  evolve:
    candidate_improvements: []
    enter_evolution_flow: false
```
