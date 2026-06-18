# v0.8.0 MVP Definition

**Release theme:** Runtime Foundation — from portable skill packages to a project workspace foundation.

> 中文摘要：v0.8.0 的成功标准不是自动制作完整游戏，而是让用户第一次能把真实或合成项目放进统一 workspace，并让创意、证据、分析、实验、策划案和人类决策形成连续资产。

## Problem Statement

Before v0.8.0, GameDesignOS already had specialist skills and cross-skill contracts, but users still needed to decide where outputs should live and how project context should persist. The MVP closes that gap without prematurely building a hosted application.

## In Scope

v0.8.0 includes:

- a product vision and four-layer architecture;
- a copyable `runtime/workspace-template/`;
- a `game.designos.yaml` workspace manifest;
- a decision-information schema plus workspace-level schemas for project manifests, asset indexes, and decision logs;
- a cross-cutting decision-to-information workflow plus guides for idea-to-validation, media-to-diagnosis, weekly ED experiments, and evidence-to-proposal;
- workspace-aware adapter guidance;
- a documented future CLI surface;
- repository validation for the new runtime foundation;
- release notes and README positioning.

## Non-Goals

v0.8.0 does not include:

- a hosted API or SaaS;
- API-key, identity, billing, or credential management;
- a complete CLI binary;
- a graphical project dashboard;
- automatic execution of game-engine production work;
- private project data in the public repository;
- an eighth public skill;
- a claim that AI replaces human game-design judgment.

## Primary User Stories

### Start a Project

A designer can copy the workspace template outside the public repository, edit `game.designos.yaml`, and immediately know where concepts, evidence, analysis, experiments, proposals, decisions, and retrospectives belong.

### Stop Low-Value Research

A designer can declare a decision and current default action, compare no more than three information actions, select the smallest positive-net-VOI probe, and stop when plausible signals no longer change the action or marginal value falls below cost.

### Continue Without Rebuilding Context

An agent can inspect the manifest and existing asset index, choose the smallest suitable skill, and save the output to the correct project area.

### Make a Reviewable Decision

A proposal or experiment ends in a Human Gate and a decision-log entry rather than disappearing into a chat transcript.

### Keep Public and Private Work Separate

A user can use the public base safely while keeping real production data in a private workspace or overlay.

## Acceptance Gates

The MVP passes when all of the following are true:

1. The README explains GameDesignOS as `Skill Kernel + Contract Layer + Project Workspace + Runtime Interface`.
2. `runtime/workspace-template/` can be copied as a coherent project skeleton.
3. `game.designos.yaml` parses as YAML and matches the intended workspace schema shape.
4. Every workspace lifecycle directory contains a purpose and boundary guide.
5. The four new schemas are valid JSON Schema documents, including an information-value assessment.
6. Five workflow guides name decisions, information gates, inputs, outputs, workspace paths, skill routes, Human Gates, stop rules, and definitions of done.
7. Existing skill packages remain independently installable.
8. `python scripts/validate_repo.py` validates the new required paths and workspace conventions.
9. Public examples remain synthetic, public, cleared, or explicitly `needs_review`.
10. Release notes state that the runtime layer is optional and backward compatible.

## Product Quality Test

A v0.8.0 artifact should answer five questions:

- What decision is this asset for?
- What is the current default action?
- What information could change the current action?
- When should information gathering stop?
- What evidence or assumptions support it?
- What upstream assets did it consume?
- What human review state is it in?
- What happens next if it succeeds or fails?
