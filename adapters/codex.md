# Codex Adapter

Codex-style environments can load `GameDesignOS` as local Markdown skill folders.

## Install Shape

Copy or sync one skill folder into the host skill directory:

```text
game-concept-architect/
game-experience-analyzer/
game-design-proposal-writer/
paranoia-ai-system-evolver/
game-design-book-translator/
game-design-source-curator/
game-experience-density-optimizer/
```

Each folder should keep:

```text
SKILL.md
references/
templates/
examples/
agents/openai.yaml
evals/
```

Not every skill needs every subfolder, but `SKILL.md` and `README.md` are required.

## Runtime Boundary

`GameDesignOS` does not manage API keys, credentials, billing, shell permissions, browser access, or memory writes. Those remain controlled by the Codex host and the user's current session policy.

## Minimal Flow

1. The user requests a task or names `$skill-name`.
2. Codex loads the matching `SKILL.md`.
3. Codex reads only the needed `references/` and `templates/`.
4. Codex executes the task with the user's supplied materials.
5. Codex validates outputs and reports what changed.

## Validation

Run from the repository root before packaging or syncing:

```text
python scripts/validate_repo.py
python scripts/validate_skill.py <skill-folder>
```
