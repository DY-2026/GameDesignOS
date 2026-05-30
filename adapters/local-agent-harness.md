# Local Agent Harness Adapter

This is a minimal design sketch for loading `ParanoiaSkills` in a local agent harness. It is not a full SDK.

## Components

- `skill_loader`: reads `SKILL.md` and basic metadata.
- `reference_router`: selects only the needed `references/` and `templates/`.
- `prompt_builder`: composes system, developer, and user messages.
- `model_client`: calls the host-selected model or OpenAI-compatible endpoint.
- `output_validator`: parses Markdown, JSON, YAML, and schemas.
- `artifact_writer`: saves outputs with clear public/private destination rules.

## Pseudocode

```python
def run_skill_task(skill_name, user_task, user_materials):
    skill = skill_loader.load(skill_name)
    context_files = reference_router.select(skill, user_task)
    messages = prompt_builder.compose(
        skill=skill,
        context_files=context_files,
        user_task=user_task,
        user_materials=user_materials,
    )
    output = model_client.complete(messages)
    output_validator.check(output)
    artifact_writer.save(output, destination="private_notes")
    return output
```

## Public Repository Rule

Default outputs should be treated as private unless the user explicitly asks to publish them to this repository and the material passes `CONTRIBUTING.md`.
