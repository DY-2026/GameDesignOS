# Value of Information Decision Gate Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. Definition

The value of information is not its novelty, truthfulness, rarity, volume, or rhetorical quality. It is the expected improvement in the decision maker's achievable utility after the information becomes available.

```text
VOI(I)
= E_I [ max_a E[U(a, theta) | I] ]
- max_a E_theta [ U(a, theta) ]
```

- `a` is an available action;
- `theta` is an uncertain state of the world;
- `U(a, theta)` is the utility of the action in that state;
- `I` is information that may be observed.

Truth and decision value are different. When every plausible signal leads to the same action, the information has approximately zero value for the current decision.

Use net value, not gross value:

```text
net_voi
= gross_voi
- acquisition_cost
- latency_cost
- attention_cost
- implementation_risk
- privacy_or_contamination_cost
```

When a full utility model is unavailable, use this only as a ranking heuristic:

```text
approx_net_voi
= P(action_switch)
× decision_delta
× reuse_or_scale
× reversibility_factor
- total_information_cost
```

Do not present qualitative high/medium/low judgments as precise mathematics. Money, production release, real-user impact, or irreversible decisions require explicit assumptions, sensitivity checks, and a Human Gate.

## 2. Three Information Modes

| Mode | Function | Default treatment |
| --- | --- | --- |
| `decision_information` | may change a current action, priority, allocation, or stop rule | run the VOI gate |
| `model_learning` | improves a reusable world model but does not change the current action | set a learning budget and reuse target |
| `information_consumption` | provides entertainment, identity, social currency, or emotional value | allow intentionally, but keep it off the decision thread |

Low decision value does not mean worthless. It means the value must be classified honestly.

## 3. Declare the Decision Before Research

```yaml
decision:
  decision_id: "DEC-..."
  owner: ""
  deadline: ""
  decision_question: ""
  options: []
  current_default_action: ""
  stakes: ""
  reversibility: "reversible | costly_to_reverse | irreversible"
  boundary_status: "undefined | far | near | locked"
```

The workflow must answer:

1. What decision is being made?
2. What action will be taken with current information?
3. Which alternatives are still genuinely available?
4. When must the decision be made?
5. What is the cost of being wrong?
6. How reversible is the decision?

Without this object, use a time-boxed exploration budget instead of open-ended research.

## 4. Decision Boundary

| Status | Meaning | Default action |
| --- | --- | --- |
| `undefined` | decision, options, or default action are unclear | define the decision and cap exploration |
| `far` | one option dominates and common signals will not switch the action | act or run only a light check |
| `near` | limited evidence may reverse the option ranking | prioritize high-VOI information |
| `locked` | commitment is already made or the window is closed | stop researching the old choice; execute or review |

A decision is near the boundary when plausible signals can change action, not merely when the user feels uncertain.

## 5. Uncertainty Map

Track only uncertainties that can alter the option ranking:

```yaml
uncertainty_map:
  - uncertainty: ""
    current_belief_or_range: ""
    confidence: "low | medium | high"
    impact_if_wrong: "low | medium | high"
    affected_options: []
    observable: true
    controllable: false
```

A practical priority heuristic is:

```text
uncertainty_priority
≈ impact_if_wrong
× probability_current_model_is_wrong
× action_sensitivity
```

High uncertainty with low impact can use a default assumption. Low uncertainty with high impact deserves a light verification. High uncertainty and high impact justify a meaningful probe.

## 6. Candidate Information Actions

Information must be expressed as an executable action: inspect a log, ask a specific person, run a replay, test a prototype, observe a user segment, or sample a metric.

```yaml
information_action:
  action_id: "INFO-..."
  action: ""
  target_uncertainty: ""
  expected_signals: []
  reliability_and_bias: ""
  acquisition_cost: ""
  latency_cost: ""
  attention_cost: ""
  risk_or_contamination: ""
```

High-VOI signals tend to be local, decision-specific, potentially disconfirming, actionable, close to the decision boundary, and available before the window closes.

## 7. Signal-to-Action Mapping

Pre-register what each plausible signal would cause the team to do.

| Signal | Posterior update | Action if observed |
| --- | --- | --- |
| supports current option | probability or expected benefit rises | continue, invest, or shorten the next test |
| contradicts current option | probability or expected benefit falls | switch, narrow scope, rollback, or stop |
| ambiguous or invalid | little uncertainty reduction | do not buy the same information again; change probe or act on the default |

If every signal maps to the same action:

```text
could_change_action = false
current_decision_voi ≈ 0
```

Stop, or reclassify the activity as model learning or information consumption.

## 8. EVPI, EVPPI, EVSI, and Net Sample Value

### EVPI

```text
EVPI
= E_theta [ max_a U(a, theta) ]
- max_a E_theta [ U(a, theta) ]
```

EVPI is an upper bound on the value of eliminating all uncertainty. No report, test, or research program should cost more than the perfect information it could approximate.

### EVPPI

EVPPI eliminates uncertainty in one parameter or a subset of parameters. Use it conceptually to decide what uncertainty is worth targeting.

### EVSI

```text
EVSI
= E_X [ max_a E[U(a, theta) | X] ]
- max_a E_theta [ U(a, theta) ]
```

`X` is data from a proposed sample, experiment, playtest, A/B test, interview, or log inspection.

### Net Sample Value

```text
net_EVSI_or_ENBS
= EVSI
- study_cost
- delay_cost
- operational_risk
```

Prefer the smallest, fastest, reversible sample that can reduce uncertainty in a consequential decision.

## 9. Eight-Step Gate

1. **Decision:** define options, default action, deadline, reversibility, and loss function.
2. **Boundary:** classify `undefined / far / near / locked`.
3. **Uncertainty:** keep only variables that can change the option ranking.
4. **Information actions:** generate at most three candidates; prefer local evidence, negative signals, and small experiments.
5. **Signal-to-action:** pre-register how possible signals change action.
6. **Value and cost:** compare the value ceiling and sample value with acquisition, delay, attention, privacy, and contamination costs.
7. **Probe:** choose the smallest information action with the highest positive net value.
8. **Stop and record:** capture prior, signal, posterior, action change, residual uncertainty, and stop reason.

Stop when the preferred action is robust across plausible signals, marginal VOI is no greater than marginal cost, the evidence gate or sample limit is reached, the deadline arrives, remaining uncertainty cannot change action, or a Human Gate has committed the project to execution.

## 10. AI Workflow Rules

AI lowers generation cost but not human evaluation cost. Every extra answer, option, and conversation can create unresolved decision residue.

- Declare the decision or artifact before opening a long AI thread.
- Without a decision object, allow only budgeted exploration.
- Propose no more than three real information actions per round.
- Do not repeat macro research that cannot change the current action.
- Prefer project data, failure traces, user corrections, negative feedback, and local constraints.
- End with what to stop, start, invest in, reject, or test.
- Label non-action-changing output as `model_learning` or `information_consumption`.
- Keep production, publishing, money, memory, and real-user actions behind a Human Gate.

### AI Fatigue Gate

```text
open branches
-> map each branch to a decision
-> keep branches that may change action
-> archive model-learning branches
-> close consumption branches
-> choose one next probe
```

### Anti-Generic-Output Gate

High structure does not imply high VOI. Preserve local facts, constraints, negative feedback, failure details, decision impact, and unsupported boundaries. Do not wash a specific operational signal into generic management prose.

## 11. GameDesignOS Applications

- **Idea to validation:** select the player promise, core-loop risk, or production assumption whose sample information most affects prototype investment.
- **Media to diagnosis:** collect evidence only when it can change issue priority, a proposed change, or the next validation action.
- **Weekly ED experiment:** compare playtest, telemetry, and variant designs by expected sample value and pre-register amplify, iterate, observe, rollback, or kill actions.
- **Evidence to proposal:** request missing research only when it can change Go/No-Go, scope, budget, milestone, or the decision request.
- **System evolution:** do not promote a prompt, skill, schema, or router change from one attractive case; use repeated failures, high-impact regressions, and cross-task behavior samples.

## 12. Failure Modes

| Failure mode | Symptom | Correction |
| --- | --- | --- |
| FOMO research | trend tracking without a decision | define the decision or cap consumption |
| research theater | research substitutes for action | pre-register signal-to-action and deadline |
| confirmation bias | only supportive evidence is requested | seek the strongest plausible disconfirmation |
| option explosion | AI keeps generating alternatives | cap real options and information actions |
| information laundering | local negative detail becomes generic prose | preserve provenance and action impact |
| false precision | unsupported percentages disguise intuition | state ranges, assumptions, and sensitivity |
| delay blindness | information arrives after the decision window | include latency cost |
| repetitive low-value evidence | more sources do not alter action | trigger the stop rule |
| post-lock research | a committed choice keeps attracting justification | move to execution metrics or retrospective |
| high-VOI signal without action | evidence is learned but workflow does not change | attach an if-then protocol or Human Gate |

## 13. Behavior Eval

A passing output must include a decision object, options and current default action, boundary status, targeted uncertainty, signal-to-action mapping, information costs, EVPI-versus-EVSI distinction, the smallest selected probe, a stop rule, and an eventual posterior/action update.

Fail outputs that provide research lists without a decision, equate truth with value, recommend more research without action branches, ignore attention or delay costs, promote a rule from one case, or erase local negative evidence during summarization.

## 14. Sources and Boundary

The formal definitions follow Ronald A. Howard's information value theory and later work on EVPI, EVPPI, EVSI, and net sample value. The boundary labels and qualitative scoring used in GameDesignOS are engineering heuristics for triage, not replacements for full statistical decision models in high-stakes settings.

- Ronald A. Howard, Information Value Theory, IEEE Transactions on Systems Science and Cybernetics, 1966, DOI: 10.1109/TSSC.1966.300074.
- Mark Strong et al., Estimating the Expected Value of Sample Information Using the Probabilistic Sensitivity Analysis Sample, Medical Decision Making, 2015, DOI: 10.1177/0272989X15575286.
- Natalia Kunst et al., Computing the Expected Value of Sample Information Efficiently, Value in Health, 2020, DOI: 10.1016/j.jval.2020.02.010.
