---
title: "tests.snapshots.test_ui_snapshot_ask_user_question"
tldr: "Module tests.snapshots.test_ui_snapshot_ask_user_question"
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_ask_user_question`

**Source:** [`tests/snapshots/test_ui_snapshot_ask_user_question.py`](tests/snapshots/test_ui_snapshot_ask_user_question.py) · 80 lines

## `AskUserQuestionResultApp`

**Bases:** `BaseSnapshotTestApp`

Test app that displays an AskUserQuestion tool result.

**Source:** [`tests/snapshots/test_ui_snapshot_ask_user_question.py#L16`](tests/snapshots/test_ui_snapshot_ask_user_question.py#L16)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `on_mount()` |  | `None` | — |

## `test_snapshot_ask_user_question_collapsed()`

```python
def test_snapshot_ask_user_question_collapsed(snap_compare: SnapCompare) -> None
```

Test collapsed AskUserQuestion result shows summary.

**Source:** [`tests/snapshots/test_ui_snapshot_ask_user_question.py#L55`](tests/snapshots/test_ui_snapshot_ask_user_question.py#L55)

## `test_snapshot_ask_user_question_expanded()`

```python
def test_snapshot_ask_user_question_expanded(snap_compare: SnapCompare) -> None
```

Test expanded AskUserQuestion result shows formatted Q&A pairs.

**Source:** [`tests/snapshots/test_ui_snapshot_ask_user_question.py#L68`](tests/snapshots/test_ui_snapshot_ask_user_question.py#L68)

