# Changelog

All notable changes to GameDesignOS will be recorded here.

## [Unreleased]

## [v0.8.0] - 2026-06-18

### Added

- Added the GameDesignOS Runtime Foundation: product vision, four-layer architecture, MVP boundary, and capability-gated roadmap.
- Added a copyable project workspace template with a manifest, lifecycle directories, design-asset index example, and Human Gate decision-log example.
- Added workspace-level schemas for project manifests, design-asset indexes, and decision logs.
- Added four workspace-aware workflow guides: idea-to-validation, media-to-diagnosis, weekly ED experiment, and evidence-to-proposal.
- Added planned local CLI command contracts without claiming that a complete CLI ships in this version.
- Added a complete VOI Decision Gate for Decision Object, current default action, decision boundary, signal-to-action mapping, EVPI/EVSI, information costs, smallest probes, and stop rules.
- Added `information-value-assessment` as a workspace contract and durable decision asset.
- Added VOI behavior evals for FOMO research, branch explosion, local negative evidence, irreversible changes, and high-structure/low-value output.

### Changed

- Repositioned the README trio around `Skill Kernel + Contract Layer + Project Workspace + Runtime Interface`.
- Reused the existing no-text hero background so the v0.7.0 title layer is not shown on a v0.8.0 page.
- Upgraded adapter guidance from direct skill loading to workspace-aware routing and asset writeback.
- Extended repository validation to protect runtime paths, workspace conventions, schemas, examples, and the VOI Decision Gate.
- Upgraded `paranoia-ai-system-evolver` so research, retrieval, tests, memory reads, and AI branches must justify how they can change action.
- Preserved direct installation and invocation of all seven existing skill packages.

### Safety

- Kept real project material in private workspaces or overlays outside the public repository.
- Kept Human Gates for project commitments and publication.
- Kept API keys, credentials, billing, and host permissions outside GameDesignOS.

## [v0.7.0] - 2026-06-18

### Added

- Added the `GameDesignOS by Paranoia` v7 README banner assets with a no-text background and deterministic local title/signature layer: `assets/gamedesignos-overview-banner-v7-background.png` and `assets/gamedesignos-overview-banner-v7.png`.
- Added the Dreamina-generated `assets/showcase-game-design-proposal-writer.png` so all seven public skills now have visible README showcase art.

### Changed

- Updated canonical public repository references to `DY-2026/GameDesignOS`, including README Star History, GitHub About metadata, showcase feedback links, and schema identifiers.
- Refined the public visual direction toward `GameDesignOS` as an AI-native game design operating system rather than a skill-list wrapper.
- Consolidated the `《生存33天》` Game Experience Analyzer report and the `《冒险家艾略特的千年奇谭》` ED proof path into the featured cases table so the 60-second demo stays a quick interaction example.
- Reorganized the README showcase grid into seven clickable module cards following the GameDesignOS product path: concept, evidence, proposal, ED iteration, workflow governance, translation, and source curation.
- Updated current adapter docs, skill sub-README parent links, and the ED experiment schema id from the old `ParanoiaSkills` name to `GameDesignOS` / `GameDesignOS by Paranoia`.
- Marked the older public article as a historical `ParanoiaSkills` draft so it does not conflict with the v0.7.0 identity.

## [v0.6.1] - 2026-06-10

### Fixed

- Re-added repository `.gitignore` as a required tracked file so CI validation can pass without repository-local exceptions.

- Documented the release housekeeping so the versioning sequence remains accurate after the hotfix.

## [v0.6.0] - 2026-06-09

### Added

- Added `game-design-proposal-writer` as the seventh public skill package for turning research, concept contracts, evidence notes, validation plans, production constraints, and business goals into reviewable proposals, pitch outlines, decision memos, and vertical-slice documents.
- Added proposal-writing references, templates, evals, negative cases, synthetic outputs, and public synthetic examples.
- Added `game-experience-density-optimizer` evidence-gate and scorecard surfaces for weekly ED experiment planning, schema output, hybrid-conflict review, instrumentation, and decision rules.
- Added a new GitHub landing banner asset for the seven-skill architecture: `assets/paranoia-skills-overview-banner-v6.png`.

### Changed

- Updated the README trio, showcase index, router contracts, and repository validation for the seven-skill architecture.
- Repositioned the public GitHub intro around a verifiable agent-skill operating system for game design: evidence diagnosis, concept contracts, proposal writing, ED experiments, and workflow governance.
- Upgraded `game-experience-density-optimizer` from a methods-heavy skill into an evidence-gated experiment compiler with explicit modes, templates, schemas, examples, and eval coverage.

### Safety

- Kept public examples synthetic or explicitly bounded by the repository contribution policy.
- Generated the new banner from a no-text background and overlaid exact project/version text locally to avoid model-generated typo artifacts.

## [v0.5.0] - 2026-06-06

### Changed

- Refreshed the public README introduction around cross-skill contracts, ED experiments, WOOP/VOI/OODA workflow governance, and eval-backed evolution.
- Added a new overview banner asset with project name, one-line positioning, and version marker for the GitHub landing page.
- Updated the GitHub About description for the new contracted workflow positioning.

### Added

- Added cross-skill routing and handoff language to the public introduction, including concept contracts, evidence indexes, issue cards, ED handoffs, and validation plans.
- Added WOOP Task Card positioning to the public workflow-evolution language.

## [v0.4.0] - 2026-06-04

### Added

- Added `game-experience-density-optimizer` for turning experience concentration, retention, pacing, feedback, embodiment, atmosphere, and cognitive-load problems into weekly ED experiments.
- Added ED templates, telemetry/dashboard specs, evals, a synthetic public example, and showcase imagery.

### Changed

- Updated the README trio, onboarding guide, showcase index, and repository validator for the six-skill architecture.
- Updated the overview/showcase layout so visual cards render four per row instead of squeezing six into one row.

## [v0.3.0] - 2026-06-03

### Added

- Added star-supported public content promise.
- Added try-it-in-10-minutes onboarding.
- Added showcase index.
- Added examples index.
- Added issue templates.
- Added v0.3.0 release draft.
- Added Star History chart to the README trio.
- Reworked the README opening so positioning and value come before specific examples.
- Added a generated overview banner with title and one-line positioning.
- Simplified repository layout docs into reader-facing layers instead of a full asset tree.

## [v0.2.0] - 2026-05-30

### Added

- Added `game-concept-architect` as a public base skill for turning one-line game ideas into verifiable concept blueprints.
- Added adapters, contracts, repository validation, and contribution boundaries for public-safe examples.

### Changed

- Reorganized the repository into skill packages, adapters, contracts, docs, releases, and validation scripts.
- Strengthened the public/private boundary for examples, assets, evals, and docs.

## [v0.1.0] - 2026-05-29

### Added

- Released the public base version of `game-experience-analyzer`.
- Added initial release notes, installation guidance, and validation examples.

[Unreleased]: https://github.com/DY-2026/GameDesignOS/compare/v0.8.0...HEAD
[v0.8.0]: ./releases/v0.8.0.md
[v0.7.0]: ./releases/v0.7.0.md
[v0.6.1]: ./releases/v0.6.1.md
[v0.6.0]: ./releases/v0.6.0.md
[v0.5.0]: ./releases/v0.5.0.md
[v0.4.0]: ./releases/v0.4.0.md
[v0.3.0]: ./releases/v0.3.0.md
[v0.2.0]: ./releases/v0.2.0.md
[v0.1.0]: ./releases/v0.1.0.md
