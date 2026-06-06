# Dashboard Spec

## Filters

| filter | required | notes |
| --- | --- | --- |
| `experiment_id` | yes | one experiment at a time |
| `variant_id` | yes | A/B/C/D |
| `game_metric_model` | yes | premium_single_player / mobile_liveops / hybrid / unknown |
| `metric_horizon` | yes | total_journey / chapter_segment / run_based / daily_retention / event_cycle / hybrid_split |
| `user_segment` | yes | new / returning / existing |
| `platform` | yes | iOS / Android / PC / Web |
| `channel` | yes | paid / organic / test group / store |
| `client_version` | yes | avoid mixed builds |
| `session_scope` | yes | first session / return session / fatigue segment |
| `checkpoint_id` | recommended | inspect exit points |
| `stimulation_band` | recommended | too_low / optimal / too_high / uneven |
| `boredom_type` | recommended | under_stimulation / over_stimulation / habituation / low_agency / low_meaning / mixed |

## Core Cards

| card | metric | purpose |
| --- | --- | --- |
| Journey quality | total playtime, completion, chapter/demo checkpoint reach, replay intent | single-player or premium P1 |
| Daily retention quality | D1 / D3 / D7 / D30, consecutive active days, return session | mobile/liveops P1 |
| ED proxy | `MD/min * (SF + EB + AR) / CLP` | design explanation |
| CLP | confusion, interruptions, repeated clicks, tutorial stalls | noise gate |
| SF | feedback clarity and attribution | vertical quality |
| EB | input latency, camera stability, hitstop, control complaints | embodiment |
| AR | atmosphere segment completion, observation time, positive notes | atmosphere |
| MD/min | meaningful decisions per playable minute | horizontal frequency |
| Optimal stimulation fit | optimal_stimulation_band, boredom_type_mix, player_resource_segment | distinguish under-stimulation, overload, habituation, agency, and meaning gaps |
| Free energy window | prediction_error_band, attribution_clarity, recovery_action_available | controllable surprise |
| Markov blanket coupling | input latency, feedback latency, mapping clarity, agency score, noise source | action-feedback boundary |
| Anti-habituation | anti_habituation_fit, familiar_anchor, novel_delta, attribution_clarity | long-term fatigue and repeat-loop diagnosis |
| Negative gates | crash, early exit, failure spike, complaints, economy anomaly | rollback |

## Daily Checks

| day | check |
| --- | --- |
| Wednesday | assignment balance, event missing rate, crash/anr, version mismatch |
| Thursday | TTE, ED proxy direction, exit point, negative sentiment, metric horizon sanity |
| Monday review | P1 first, negative gates second, P2 explanation third |

## Chart Suggestions

- Line chart: ED proxy by variant and day.
- Bar chart: CLP/SF/EB/AR/MD-min by variant.
- Band chart: too_low / optimal / too_high prediction-error windows by variant.
- Stacked bar: boredom_type_mix by variant and user segment.
- Heatmap: optimal_stimulation_band by checkpoint and player_resource_segment.
- Scatter: feedback latency vs mapping clarity for blanket coupling checks.
- Funnel: session start -> first meaningful decision -> first salient feedback -> checkpoint -> session end.
- Journey funnel: start -> core loop reached -> chapter/demo checkpoint -> completion/replay intent.
- Liveops calendar: daily activity and return-session quality by variant.
- Table: negative gates by variant, platform, and user segment.
