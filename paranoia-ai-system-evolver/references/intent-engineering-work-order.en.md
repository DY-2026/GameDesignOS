# Intent Engineering Work Order

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

This backup note defines the intent-first task entry used by `paranoia-ai-system-evolver`.

Intent engineering upgrades a task from "ask AI to perform an action" to "give AI a clear operational intent, context, acceptance criteria, autonomy boundary, loop contract, and retrospective contract."

Minimum questions:

1. What reality should change?
2. Which larger project goal does this serve?
3. What should the outside world look like after completion?
4. Who verifies the result?
5. What must the verifier understand at first glance?
6. What must not be sacrificed?
7. What may AI freely change?
8. What must AI not touch?
9. If the plan fails, which principles should guide a direction change?
10. Which failure signals must be checked before delivery?

The work order maps into the existing GameDesignOS chain:

```text
Intent Work Order
-> WOOP Task Card
-> Decision Object
-> RJR-AI authority gate
-> VOI decision gate
-> OODA loop
-> acceptance check
-> retrospective
-> candidate learning record
```

Rules:

- Start with intent before tools.
- Define the verifier and first-glance acceptance before long loops.
- Declare both what AI may change and what it must not touch.
- Direction changes must preserve the original intent rather than protect the old plan.
- Retrospective lessons remain `candidate` until behavior evals, negative-transfer checks, Human Gate, and rollback exist.
