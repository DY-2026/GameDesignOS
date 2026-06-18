# OpenAI-Compatible Adapter

This adapter sketch is intentionally pseudocode. Do not hard-code API keys in this repository.

`GameDesignOS` provides Markdown skill instructions. The host harness owns credentials, model selection, network calls, logging, and safety policy.

## Minimal Flow

```python
from pathlib import Path


REPO = Path("GameDesignOS")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_skill(skill_name: str) -> dict:
    skill_dir = REPO / skill_name
    return {
        "name": skill_name,
        "skill": load_text(skill_dir / "SKILL.md"),
        "references": skill_dir / "references",
        "templates": skill_dir / "templates",
    }


def select_context(skill: dict, user_task: str) -> str:
    # Keep context small. Add only references/templates that can change the output.
    extra_sections = []

    if "validation" in user_task.lower():
        path = skill["templates"] / "validation-plan.md"
        if path.exists():
            extra_sections.append(load_text(path))

    return "\n\n".join([skill["skill"], *extra_sections])


def run_agent(client, skill_name: str, user_task: str, user_materials: str) -> str:
    skill = load_skill(skill_name)
    context = select_context(skill, user_task)

    response = client.chat.completions.create(
        model="your-host-selected-model",
        messages=[
            {
                "role": "system",
                "content": "Follow the selected Markdown skill. Keep public examples synthetic/public/cleared.",
            },
            {
                "role": "developer",
                "content": context,
            },
            {
                "role": "user",
                "content": f"{user_task}\n\nMaterials:\n{user_materials}",
            },
        ],
    )

    markdown = response.choices[0].message.content
    Path("outputs").mkdir(exist_ok=True)
    Path("outputs/result.md").write_text(markdown, encoding="utf-8")
    return markdown
```

## Validation

After generation:

```text
python scripts/validate_repo.py
python scripts/validate_skill.py <skill-folder>
```

For structured outputs, parse JSON/YAML with the host language before saving artifacts.
