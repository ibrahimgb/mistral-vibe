---
title: "tests.tools.test_invoke_context"
tldr: "Module tests.tools.test_invoke_context"
tags: [reference, api]
---

# `tests.tools.test_invoke_context`

**Source:** [`tests/tools/test_invoke_context.py`](tests/tools/test_invoke_context.py) · 106 lines

## `SimpleArgs`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/tools/test_invoke_context.py#L13`](tests/tools/test_invoke_context.py#L13)

## `SimpleResult`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/tools/test_invoke_context.py#L17`](tests/tools/test_invoke_context.py#L17)

## `SimpleTool`

**Bases:** `BaseTool[SimpleArgs, SimpleResult, BaseToolConfig, BaseToolState]`

**Source:** [`tests/tools/test_invoke_context.py#L23`](tests/tools/test_invoke_context.py#L23)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `run()` | args, ctx | `AsyncGenerator[ToolStreamEvent | SimpleResult, None]` | — |

## `TestInvokeContext`

**Source:** [`tests/tools/test_invoke_context.py#L42`](tests/tools/test_invoke_context.py#L42)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_default_approval_callback_is_none()` |  | `None` | — |
| `test_approval_callback_can_be_set()` |  | `None` | — |

## `TestToolInvokeWithContext`

**Source:** [`tests/tools/test_invoke_context.py#L58`](tests/tools/test_invoke_context.py#L58)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_invoke_without_context()` | simple_tool | `None` | — |
| 🔄 `test_invoke_with_empty_context()` | simple_tool | `None` | — |
| 🔄 `test_invoke_with_approval_callback()` | simple_tool | `None` | — |
| 🔄 `test_run_receives_context()` | simple_tool | `None` | — |
| 🔄 `test_run_without_context_defaults_to_none()` | simple_tool | `None` | — |

## `simple_tool()`

```python
def simple_tool() -> SimpleTool
```

**Source:** [`tests/tools/test_invoke_context.py#L38`](tests/tools/test_invoke_context.py#L38)

