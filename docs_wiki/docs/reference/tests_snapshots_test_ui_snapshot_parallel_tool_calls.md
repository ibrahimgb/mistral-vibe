---
title: "tests.snapshots.test_ui_snapshot_parallel_tool_calls"
tldr: "Module tests.snapshots.test_ui_snapshot_parallel_tool_calls"
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_parallel_tool_calls`

**Source:** [`tests/snapshots/test_ui_snapshot_parallel_tool_calls.py`](tests/snapshots/test_ui_snapshot_parallel_tool_calls.py) · 114 lines

## `ParallelToolCallsApp`

**Bases:** `App`

**Source:** [`tests/snapshots/test_ui_snapshot_parallel_tool_calls.py#L17`](tests/snapshots/test_ui_snapshot_parallel_tool_calls.py#L17)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `None` | — |
| `compose()` |  | `ComposeResult` | — |
| `on_mount()` |  | `None` | — |
| 🔄 `emit_all_tool_calls()` |  | `None` | — |
| `freeze_spinners()` |  | `None` | — |
| 🔄 `resolve_all_results()` |  | `None` | — |

## `test_snapshot_parallel_tool_calls_pending()`

```python
def test_snapshot_parallel_tool_calls_pending(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_parallel_tool_calls.py#L87`](tests/snapshots/test_ui_snapshot_parallel_tool_calls.py#L87)

## `test_snapshot_parallel_tool_calls_resolved()`

```python
def test_snapshot_parallel_tool_calls_resolved(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_parallel_tool_calls.py#L102`](tests/snapshots/test_ui_snapshot_parallel_tool_calls.py#L102)

