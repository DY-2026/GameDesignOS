# Game Design Source Curator

**Parent project:** [ParanoiaSkills](../README.en.md)

This installable skill turns game design articles, videos, creators, columns, and websites into durable local knowledge-base assets.

## Use Cases

- Curate high-quality game design sources over time.
- Build source profiles for websites, authors, creators, public accounts, and columns.
- Review articles, videos, postmortems, and methods with evidence gates.
- Ingest accepted items into local `docs/`.
- Maintain incremental updates, deduplication, catalogs, registries, and update history.
- Add practical design experiment cards for accepted sources.

## Package Structure

- `SKILL.md`: lightweight agent entrypoint.
- `references/curation-workflow.zh-CN.md`: full curation workflow.
- `references/scoring-and-evidence-gates.zh-CN.md`: scoring, evidence gates, and platform limits.
- `templates/`: reusable source profile, catalog, item card, registry, and update-history forms.
- `agents/openai.yaml`: Codex UI metadata.

## Sync Rule

This directory is the project-tracked copy. If a runtime copy in a host agent skill directory changes later, sync those changes back here and revalidate that both copies match.

Copyright (c) 2026 Paranoia. Licensed under the MIT License.
