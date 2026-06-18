# Claude Code Adapter

Claude Code can use `GameDesignOS` as project instructions or local documentation.

## Minimal Flow

1. Put the selected skill folder in the project or reference it from project instructions.
2. Tell the agent to read the skill's `SKILL.md` before answering.
3. Read `references/` and `templates/` only when the task requires them.
4. Keep private overlays outside this public repository.
5. Validate Markdown, JSON, YAML, and schema artifacts before publishing repository changes.

## Prompt Shape

```text
Read GameDesignOS/game-experience-analyzer/SKILL.md.
Use only the references/templates needed for this task.
The user material is private unless explicitly marked repo-safe.
Produce an evidence-linked diagnosis and validate structured outputs before saving.
```

## Boundary

`GameDesignOS` does not provide API keys or model credentials. Claude Code or the host environment owns model access, tool permissions, file writes, and any connected services.
