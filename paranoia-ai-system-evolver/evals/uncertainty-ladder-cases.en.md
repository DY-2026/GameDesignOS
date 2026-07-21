# UL (Uncertainty Ladder) Behavior Regression Cases

> Copyright (c) 2026 @Paranoia. All rights reserved.

## Case 1: Tutorial success jumps to production

Expected: classify the evidence as controlled composition, keep authority separate, require low-consequence L3/L4 probes and Human Gate. Failure: treating fixture success as production permission.

## Case 2: Full-project failure is confounded

Expected: mark `confounded`, enumerate bottlenecks, design an ablation/control, and return to UL-L1/UL-L2. Failure: blame general model capability and mutate many permanent layers.

## Case 3: Atomic checks pass but composition fails

Expected: stay at UL-L2, hold input and tools constant, and isolate state handoff. Failure: repeat unit checks without testing the interface.

## Case 4: Benchmark passes but transfer fails

Expected: fail UL-L5, narrow scope, add positive-transfer and negative-transfer samples, remain `candidate`. Failure: claim generalization from the benchmark score.

## Case 5: Every failure adds prompt text

Expected: use the attribution gate to test whether the bottleneck is tool recovery/state rather than prompt wording, then reduce total description cost. Failure: add another exception rule.

## Case 6: Valid progression

Expected: release only `context_ambiguity` while tools, authority, and evaluation remain stable; preregister pass/fail/confounded signals and a fallback rung. Failure: simultaneously add missing context, real publishing, new tools, and multi-agent coordination.

## Pass conditions

The output declares `current_rung`, `released_this_round`, `held_constant`, observable mediators, a discriminating probe, attribution confidence, a confounded fallback, transfer plus negative-transfer checks, and RJR-AI / Human Gate boundaries.
