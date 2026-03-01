---
title: "tests.stubs.fake_tool"
tldr: "Module tests.stubs.fake_tool"
tags: [reference, api]
---

# `tests.stubs.fake_tool`

**Source:** [`tests/stubs/fake_tool.py`](tests/stubs/fake_tool.py) · 35 lines

## `FakeToolArgs`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/stubs/fake_tool.py#L11`](tests/stubs/fake_tool.py#L11)

## `FakeToolResult`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/stubs/fake_tool.py#L15`](tests/stubs/fake_tool.py#L15)

## `FakeToolState`

*✅ Pydantic*

**Bases:** `BaseToolState`

**Source:** [`tests/stubs/fake_tool.py#L19`](tests/stubs/fake_tool.py#L19)

## `FakeTool`

**Bases:** `BaseTool[FakeToolArgs, FakeToolResult, BaseToolConfig, FakeToolState]`

**Source:** [`tests/stubs/fake_tool.py#L23`](tests/stubs/fake_tool.py#L23)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `get_name()` | cls | `str` | — |
| 🔄 `run()` | args, ctx | `AsyncGenerator[ToolStreamEvent | FakeToolResult, None]` | — |

