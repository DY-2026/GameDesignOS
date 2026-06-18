# GameDesignOS Product Vision

GameDesignOS is an AI-native game design operating system for turning ideas, evidence, analysis, experiments, proposals, and decisions into durable project assets.

> 中文摘要：GameDesignOS 不是自动替代策划的写稿机器，而是一套帮助策划保存判断、证据、实验与决策，并让不同 AI skill 在同一项目上下文中协作的工作系统。

It is not an automated game designer, a prompt collection, or a hosted model service. It is a public method and runtime foundation that helps human designers preserve judgment, route work through suitable expert skills, and keep project context reviewable across iterations.

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

The product evolves through three milestones:

1. **Runtime Foundation:** workspace template, contracts, workflow routes, and validation conventions.
2. **Local Runtime:** project initialization, routing, asset creation, and validation through a local CLI or agent harness.
3. **Project-Ready Operating System:** asset graph, review gates, project dashboard, private overlays, and validated end-to-end cases.

The long-term test is simple: GameDesignOS should help a designer make a more traceable decision, run a smaller and more valuable experiment, and preserve what the project learned.
