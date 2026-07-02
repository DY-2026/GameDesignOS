# GameDesignOS Product Vision

GameDesignOS is a local-first operating system for AI-assisted game design. It turns AI-agent sessions into structured decisions, assumptions, evidence, experiments, proposals, workflows, authority boundaries, and learning records, so teams can validate ideas, diagnose gameplay, and evolve production workflows without losing context or bypassing human judgment.

> 中文摘要：GameDesignOS 不是自动替代策划的写稿机器，而是一套帮助策划保存判断、证据、实验与决策，并让不同 AI skill 在同一项目上下文中协作的工作系统。

It is not an automated game designer, a prompt collection, or a hosted model service. It is a public method, seven-skill system, contract layer, v1 project workspace, and deterministic local runtime that helps human designers preserve judgment, route work through suitable expert skills, and keep project context reviewable across iterations.

## Why It Exists

Game design work is often fragmented across chat sessions, documents, screenshots, spreadsheets, meeting notes, prototypes, and individual memory. AI can generate more text, but more text does not automatically create better decisions. The missing layer is an operating structure that connects decisions, default actions, evidence, assumptions, information costs, experiments, stop rules, and human gates.

GameDesignOS exists to provide that structure.

## The Core Promise

A designer should be able to move through this chain without rebuilding context at every step:

```text
decision object
  -> VOI gate
  -> idea
  -> concept seed
  -> player promise
  -> validation plan
  -> prototype or media evidence
  -> evidence index
  -> issue cards
  -> experiment
  -> proposal
  -> human decision
  -> retrospective
```

Each step should produce a reviewable asset with explicit provenance, upstream dependencies, uncertainty, and a next decision.

## Decision-First Information

GameDesignOS does not treat more research as the default. Before an agent opens broad search, memory, RAG, or an experiment, the project should know what decision is being supported, what action happens without new information, which plausible signal could change that action, and when information gathering stops.

This turns AI from an option generator into a decision-support system. It also separates immediate decision information from long-term model learning and intentional information consumption.

## What Counts as a Design Asset

A design asset is not merely a generated document. It is a project artifact with a defined purpose, an authoring mode, an evidence boundary, a review state, and a relationship to upstream and downstream work.

Examples include:

- concept seeds and player-promise contracts;
- validation plans and scope gates;
- evidence indexes, timestamp ledgers, and issue cards;
- experience-density experiment plans and rollback rules;
- decision memos, publisher pitches, and vertical-slice plans;
- human decision logs and retrospectives.

## Human Judgment and AI Assistance

GameDesignOS treats AI as a design-workflow participant, not the final authority. Agents can structure inputs, apply methods, identify missing evidence, propose experiments, and assemble decision documents. Humans retain responsibility for goals, taste, trade-offs, project commitments, publishing, and irreversible decisions.

In v1.1.0 this becomes the RJR-AI rule: AI expands possibilities; Workflow compresses chaos; Eval provides feedback; permission systems prevent overreach; knowledge bases preserve organizational memory; and the residual judgment for high-coupling, low-reversibility, under-evidenced choices stays with a human.

The default operating principles are:

```text
Evidence before opinion.
Feasibility before scope.
Workflow before one-off prompts.
Decision before information.
VOI before research.
Sample before scale.
Stop when marginal VOI is non-positive.
Eval before promotion.
Rollback before confidence.
```

## Public Base and Private Overlay

The public repository contains portable skills, stable contracts, workspace conventions, synthetic or cleared examples, validation tools, and adapter notes.

Real projects should use a private workspace or private overlay for proprietary concepts, client material, internal metrics, credentials, unpublished assets, and studio-specific operating rules. The public repository must never become a storage location for private production data.

## Product Direction

v1.0.0 is the formal Project-Ready baseline. v1.1.0 adds the RJR-AI authority layer and GitHub-facing positioning without changing the v1 workspace schema. The product has reached these milestones:

1. **Runtime Foundation:** workspace template, contracts, workflow routes, and validation conventions.
2. **Local Runtime:** project initialization, routing, asset creation, validation, VOI review, and review-safe packing through a local CLI or agent harness.
3. **Project-Ready Operating System:** asset graph, review gates, project dashboard, private overlays, and validated end-to-end cases.
4. **RJR-AI Authority Layer:** explicit responsibility split across AI, workflow, eval, permissions, knowledge memory, and human residual judgment.

The v1.x direction is proof and adoption: more public evidence-linked cases, stronger adapters, clearer runtime dashboards, private-overlay playbooks, and real-project validation without weakening Human Gate, public/private separation, or local-first safety.

The long-term test remains simple: GameDesignOS should help a designer make a more traceable decision, run a smaller and more valuable experiment, and preserve what the project learned.
