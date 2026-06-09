---
case_type: synthetic_case
source_status: synthetic
contains_private_project_info: false
license_status: MIT-compatible example text
intended_use: public_repo_example
---
# Synthetic Example: Clockwork Garden Defense Commercial Proposal

## Case Visibility

| 字段 | 值 |
| --- | --- |
| case_visibility | synthetic_case |
| output_destination | repo_example |
| redaction_required | false |

## Proposal Intake

| 字段 | 值 |
| --- | --- |
| target_reader | internal_leadership / producer |
| document_goal | approve 2-week first playable |
| platform | mobile, assumed |
| business_model | unknown, assumed F2P test only |
| project_stage | concept |
| available_materials | synthetic concept seed and player promise |

## Source Artifact Inventory

| artifact | status | usable_in_this_doc | notes |
| --- | --- | --- | --- |
| concept brief | partial | yes | synthetic seed only |
| player-promise-contract | partial | yes | inferred for example |
| validation plan | missing | no | generated as proposal output |
| evidence index | missing | no | no gameplay sample |
| market/source notes | missing | no | marked not_run |
| production profile | missing | partial | assumed small prototype team |

## Executive Summary

### One-Line Product Statement

A lightweight strategy defense game where players cultivate semi-mechanical plants by day and watch those care decisions transform the night defense against insect swarms.

### Why This Project Is Worth Reviewing

The proposal has a clear early prototype question: can care order become a readable strategic input rather than a decorative tower-defense wrapper? If this causal promise works, the project can differentiate through player planning and feedback clarity without requiring large content volume in the first test.

### Current Recommendation

Run a 2-week first playable. Do not approve full production, monetization design, or long-term live operations until the care-order causality is proven.

## Product Positioning

| 字段 | 内容 | 来源标签 |
| --- | --- | --- |
| genre / adjacent genre | light strategy defense + cultivation | assumption |
| platform fit | mobile short-session possible, not verified | assumption |
| business model fit | F2P may fit if sessions are short and readable | needs_research |
| differentiation boundary | plants change function based on care order, not just placement | derived |
| reference boundary | use tower defense only as loop reference, not content cloning | derived |

## Target Player and Desire

| 维度 | 内容 |
| --- | --- |
| target behavior | likes planning before pressure and watching a defense plan unfold |
| motivation | wants to feel clever through preparation rather than high APM |
| emotional payoff | day-time care creates night-time consequence |
| rejection points | unclear causality, passive waiting, opaque random failure |
| adjacent products/scenes | light defense, autobattler planning, cultivation loops; specific market evidence not run |

## Player Promise

| 层级 | 承诺 | 可观察行为 |
| --- | --- | --- |
| external promise | Grow strange mechanical plants, then survive the swarm they were prepared for | players understand plant transformation before night begins |
| first 10 minutes promise | I can change defense outcomes by changing care order | players try a different care sequence in round two |
| long-term promise | A compact garden can produce many defensive plans through plant combinations | players discuss builds rather than only levels |

## Core Loop and Key Systems

```text
choose care action -> change plant state -> predict night path -> swarm attacks -> read feedback -> earn parts/seeds -> unlock new constraints -> choose care action again
```

| system | serves_which_loop | changes_what_player_behavior | feedback | validation |
| --- | --- | --- | --- | --- |
| care order | core preparation | players prioritize which plant to tune first | visible morphology and stat change | second-round behavior change |
| night swarm | pressure feedback | players evaluate prior plan | pathing and damage timeline | failure attribution interview |
| plant parts | small growth | players choose new constraints | unlock one new care option | not needed before first playable |

## Scope Gate

| 层级 | 内容 | 理由 |
| --- | --- | --- |
| MVP | 3 plants, 2 care actions, 2 swarm types, 1 small grid | enough to test causality |
| Vertical Slice | 1 polished garden, 5-8 nights, basic upgrade path | proves loop and presentation |
| Demo | 20-30 minutes with build variation | only after MVP behavior proof |
| Release | multiple gardens and plant sets | depends on content pipeline |
| Post-launch | seasonal plants, events | not a current promise |
| Parked | narrative greenhouse lore | nice but not needed for core proof |
| Cut | base building, multiplayer, gacha economy | high cost and unrelated to first proof |

## Metrics and Validation Plan

| assumption | metric / observation | sample | pass standard | fail standard | decision |
| --- | --- | --- | --- | --- | --- |
| players understand care causality | second-round care sequence changes | 5-8 testers | at least 60% intentionally change order | most attribute result to random stats | Go/Pivot |
| night outcome is readable | failure attribution interview | same sample | players can name at least one cause | players cannot explain losses | revise feedback |
| loop has replay pull | voluntary replay | same sample | at least half start another run | no one wants replay | stop or redesign |

## Decision Request

| 决策项 | 建议 | 理由 |
| --- | --- | --- |
| approve_next_step | approve 2-week first playable | cheapest way to test the nucleus |
| resource_request | 1 designer, 1 programmer, placeholder art | no need for final art yet |
| validation_window | 2 weeks build + 1 week test | enough for MVP signal |
| stop_or_pivot_condition | if players cannot link care to night outcome | core promise fails |

## Evidence and Assumption Ledger

| 判断 | 来源标签 | 依据 | 置信度 | 影响等级 | 验证动作 |
| --- | --- | --- | --- | --- | --- |
| care order is the design nucleus | derived | synthetic concept seed | medium | high | MVP test |
| mobile platform is plausible | assumption | short-session loop assumption | low | medium | platform research after MVP |
| F2P is plausible | needs_research | no current evidence | low | high | monetization fit scan later |
| no market claim made | not_run | VOI is low before nucleus proof | medium | medium | research only after core passes |
