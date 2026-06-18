# 06 Decisions

Store human authority, decision objects, information-value assessments, commitment changes, and rollback conditions here.

Recommended assets:

```text
decision-brief.template.md
information-value-assessment.example.json
decision-log.json
milestone-gate.md
human-review-notes.md
rollback-decision.md
```

Before commissioning research or an experiment, record:

- the decision question, owner, deadline, and real options;
- the action that will occur with current information;
- boundary status: `undefined`, `far`, `near`, or `locked`;
- uncertainties that can change the option ranking;
- candidate information actions and signal-to-action mapping;
- acquisition, delay, attention, privacy, and contamination costs;
- the selected smallest probe and research stop rule.

Agent outputs remain proposals until a Human Gate records an accepted, rejected, reversed, or superseded decision. When decisions conflict, the newest explicit decision must reference what it supersedes.

Do not keep researching a locked decision. Move to execution metrics or a retrospective unless new evidence can trigger a pre-registered rollback.
