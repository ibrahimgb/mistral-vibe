---
title: "tests.tools.test_task"
tldr: "Module tests.tools.test_task"
tags: [reference, api]
---

# `tests.tools.test_task`

**Source:** [`tests/tools/test_task.py`](tests/tools/test_task.py) · 212 lines

## `TestTaskArgs`

**Source:** [`tests/tools/test_task.py#L21`](tests/tools/test_task.py#L21)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_default_agent_is_explore()` |  | `None` | — |
| `test_custom_values()` |  | `None` | — |

## `TestTaskToolValidation`

**Source:** [`tests/tools/test_task.py#L32`](tests/tools/test_task.py#L32)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `ctx()` |  | `InvokeContext` | — |
| 🔄 `test_rejects_primary_agent()` | task_tool, ctx | `None` | — |
| 🔄 `test_rejects_nonexistent_agent()` | task_tool, ctx | `None` | — |
| 🔄 `test_requires_agent_manager_in_context()` | task_tool | `None` | — |
| `test_explore_agent_is_valid_subagent()` |  | `None` | — |

## `TestTaskToolResolvePermission`

**Source:** [`tests/tools/test_task.py#L79`](tests/tools/test_task.py#L79)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_explore_allowed_by_default()` | task_tool | `None` | — |
| `test_unknown_agent_returns_none()` | task_tool | `None` | — |
| `test_denylist_takes_precedence()` |  | `None` | — |
| `test_glob_pattern_in_allowlist()` |  | `None` | — |
| `test_glob_pattern_in_denylist()` |  | `None` | — |
| `test_empty_lists_returns_none()` |  | `None` | — |
| `test_default_config_has_explore_in_allowlist()` |  | `None` | — |

## `TestTaskToolExecution`

**Source:** [`tests/tools/test_task.py#L123`](tests/tools/test_task.py#L123)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `ctx()` |  | `InvokeContext` | — |
| 🔄 `test_happy_path_returns_subagent_response()` | task_tool, ctx | `None` | Test that task tool successfully runs a subagent and returns its response. |
| 🔄 `test_handles_stopped_by_middleware()` | task_tool, ctx | `None` | Test that task tool reports incomplete when stopped by middleware. |
| 🔄 `test_handles_subagent_exception()` | task_tool, ctx | `None` | Test that task tool gracefully handles exceptions from subagent. |

## `task_tool()`

```python
def task_tool() -> Task
```

**Source:** [`tests/tools/test_task.py#L17`](tests/tools/test_task.py#L17)

