---
title: "tests.snapshots.test_ui_snapshot_empty_assistant_before_reasoning"
tldr: "Snapshot tests for empty assistant message removed when reasoning starts (e.g. Opus)."
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_empty_assistant_before_reasoning`

**Source:** [`tests/snapshots/test_ui_snapshot_empty_assistant_before_reasoning.py`](tests/snapshots/test_ui_snapshot_empty_assistant_before_reasoning.py) · 58 lines

Snapshot tests for empty assistant message removed when reasoning starts (e.g. Opus).

## `SnapshotTestAppEmptyAssistantThenReasoning`

**Bases:** `BaseSnapshotTestApp`

Backend stream: first chunk is assistant content only (empty), then reasoning.

Ensures the empty assistant bubble is removed when the first reasoning chunk
arrives, so the UI does not show a blank assistant message above the thinking block.

**Source:** [`tests/snapshots/test_ui_snapshot_empty_assistant_before_reasoning.py#L14`](tests/snapshots/test_ui_snapshot_empty_assistant_before_reasoning.py#L14)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `None` | — |

## `test_snapshot_empty_assistant_removed_when_reasoning_starts()`

```python
def test_snapshot_empty_assistant_removed_when_reasoning_starts(snap_compare: SnapCompare) -> None
```

Empty assistant message is removed when reasoning starts; no blank bubble above thinking.

**Source:** [`tests/snapshots/test_ui_snapshot_empty_assistant_before_reasoning.py#L44`](tests/snapshots/test_ui_snapshot_empty_assistant_before_reasoning.py#L44)

