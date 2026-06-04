# Dashboard Spec

## Filters

| filter | required | notes |
| --- | --- | --- |
| `experiment_id` | yes | one experiment at a time |
| `variant_id` | yes | A/B/C/D |
| `user_segment` | yes | new / returning / existing |
| `platform` | yes | iOS / Android / PC / Web |
| `channel` | yes | paid / organic / test group / store |
| `client_version` | yes | avoid mixed builds |
| `session_scope` | yes | first session / return session / fatigue segment |
| `checkpoint_id` | recommended | inspect exit points |

## Core Cards

| card | metric | purpose |
| --- | --- | --- |
| Retention quality | D1 / D3 / D7 / checkpoint reach | P1 outcome |
| ED proxy | `MD/min * (SF + EB + AR) / CLP` | design explanation |
| CLP | confusion, interruptions, repeated clicks, tutorial stalls | noise gate |
| SF | feedback clarity and attribution | vertical quality |
| EB | input latency, camera stability, hitstop, control complaints | embodiment |
| AR | atmosphere segment completion, observation time, positive notes | atmosphere |
| MD/min | meaningful decisions per playable minute | horizontal frequency |
| Negative gates | crash, early exit, failure spike, complaints, economy anomaly | rollback |

## Daily Checks

| day | check |
| --- | --- |
| Wednesday | assignment balance, event missing rate, crash/anr, version mismatch |
| Thursday | TTE, ED proxy direction, exit point, negative sentiment |
| Monday review | P1 first, negative gates second, P2 explanation third |

## Chart Suggestions

- Line chart: ED proxy by variant and day.
- Bar chart: CLP/SF/EB/AR/MD-min by variant.
- Funnel: session start -> first meaningful decision -> first salient feedback -> checkpoint -> session end.
- Table: negative gates by variant, platform, and user segment.
