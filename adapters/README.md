# Adapters

`ParanoiaSkills` is not an API service. It does not hold, request, proxy, store, or manage API keys.

This repository is a set of Markdown skill packages:

```text
SKILL.md
references/
templates/
examples/
agents/
evals/
```

API keys, model credentials, user identity, billing, tool permissions, and runtime policy belong to the host agent or harness that loads these files.

## Minimal Integration Model

1. Load the target skill's `SKILL.md`.
2. Read `references/` and `templates/` only when the task needs them.
3. Inject the selected skill instructions into the agent context.
4. Pass the user task and user-provided materials to the host model.
5. Validate Markdown, JSON, and YAML output before saving or publishing it.

## Adapter Notes

- [`openai-compatible.md`](./openai-compatible.md): minimal pseudocode for OpenAI-compatible model clients.
- [`codex.md`](./codex.md): local Codex-style skill loading and validation notes.
- [`claude-code.md`](./claude-code.md): using skill folders as Claude Code project instructions or local docs.
- [`local-agent-harness.md`](./local-agent-harness.md): minimum local harness component sketch.

When packaging examples, evals, demos, or public adapter fixtures, follow [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## FAQ

**Q: 支持 API key 调用吗？**

**A:** ParanoiaSkills 本身不是 API 服务，也不持有 API key。它是一组 Markdown skill 包。你可以在任意 OpenAI-compatible、Claude Code、Codex、OpenCode 或本地 agent harness 中加载这些 skill，由宿主环境管理 API key 和模型调用。
