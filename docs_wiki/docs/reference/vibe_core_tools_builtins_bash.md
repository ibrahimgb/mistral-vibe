---
title: "vibe.core.tools.builtins.bash"
tldr: "Module vibe.core.tools.builtins.bash"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.bash**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py)

## [**BashToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L168)

The [**BashToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L168) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `max_output_bytes`, `default_timeout`, `allowlist`, `denylist`, `denylist_standalone`.

## [**BashArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L190)

The [**BashArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L190) Pydantic model (extending `BaseModel`). Key fields include `command`, `timeout`.

## [**BashResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L197)

The [**BashResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L197) Pydantic model (extending `BaseModel`). Key fields include `command`, `stdout`, `stderr`, `returncode`.

## [**Bash**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L204)

The [**Bash**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L204) class (extending `BaseTool[BashArgs, BashResult, BashToolConfig, BaseToolState]`, `ToolUIData[BashArgs, BashResult]`). It exposes `format_call_display()`, `get_result_display()`, `get_status_text()`, `resolve_permission()`, `run()`.

**Public API:**

- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `def resolve_permission()`
- `async def run()`

## [**_extract_commands()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L33)

```python
def _extract_commands(command: str) -> list[str]
```

## [**_kill_process_tree()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/bash.py#L91)

```python
async def _kill_process_tree(proc: asyncio.subprocess.Process) -> None
```

