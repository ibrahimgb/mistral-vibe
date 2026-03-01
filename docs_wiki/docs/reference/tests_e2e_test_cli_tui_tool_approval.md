---
title: "tests.e2e.test_cli_tui_tool_approval"
tldr: "Module tests.e2e.test_cli_tui_tool_approval"
tags: [reference, api]
---

# `tests.e2e.test_cli_tui_tool_approval`

**Source:** [`tests/e2e/test_cli_tui_tool_approval.py`](tests/e2e/test_cli_tui_tool_approval.py) · 87 lines

## Constants

- `PREDICTABLE_OUTPUT`
- `TOOL_ARGUMENTS`

## `_tool_call_factory()`

```python
def _tool_call_factory(request_index: int, _payload: ChatCompletionsRequestPayload) -> list[dict[str, object]]
```

**Source:** [`tests/e2e/test_cli_tui_tool_approval.py#L20`](tests/e2e/test_cli_tui_tool_approval.py#L20)

## `test_spawn_cli_asks_bash_permission_and_shows_tool_output_after_approval()`

```python
def test_spawn_cli_asks_bash_permission_and_shows_tool_output_after_approval(streaming_mock_server: StreamingMockServer, setup_e2e_env: None, e2e_workdir: Path, spawned_vibe_process: SpawnedVibeProcessFixture) -> None
```

**Source:** [`tests/e2e/test_cli_tui_tool_approval.py#L67`](tests/e2e/test_cli_tui_tool_approval.py#L67)

