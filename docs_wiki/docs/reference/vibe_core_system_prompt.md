---
title: "vibe.core.system_prompt"
tldr: "Module vibe.core.system_prompt"
tags: [reference, api]
---

# [**vibe.core.system_prompt**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/system_prompt.py)

## [**ProjectContextProvider**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/system_prompt.py#L36)

The [**ProjectContextProvider**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/system_prompt.py#L36) class. It exposes `__init__()`, `get_directory_structure()`, `get_git_status()`, `get_full_context()`. Internally it relies on `_load_gitignore_patterns()`, `_process_directory()`.

**Public API:**

- `def __init__()`
- `def get_directory_structure()`
- `def get_git_status()`
- `def get_full_context()`

**Internal helpers:**

- `_load_gitignore_patterns()`
- `_process_directory()`

## [**_get_default_shell()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/system_prompt.py#L328)

```python
def _get_default_shell() -> str
```

Get the default shell used by asyncio.create_subprocess_shell.

On Unix, uses $SHELL env var and default to sh.
On Windows, this is COMSPEC or cmd.exe.

## [**_get_available_skills_section()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/system_prompt.py#L374)

```python
def _get_available_skills_section(skill_manager: SkillManager) -> str
```

## [**get_universal_system_prompt()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/system_prompt.py#L415)

```python
def get_universal_system_prompt(tool_manager: ToolManager, config: VibeConfig, skill_manager: SkillManager, agent_manager: AgentManager) -> str
```

