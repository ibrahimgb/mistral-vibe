---
title: "tests.snapshots.test_ui_snapshot_question_app"
tldr: "Module tests.snapshots.test_ui_snapshot_question_app"
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_question_app`

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py`](tests/snapshots/test_ui_snapshot_question_app.py) · 365 lines

## `QuestionAppTestApp`

**Bases:** `App`

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L66`](tests/snapshots/test_ui_snapshot_question_app.py#L66)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | args | `—` | — |
| `compose()` |  | `ComposeResult` | — |

## `SingleQuestionApp`

**Bases:** `QuestionAppTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L78`](tests/snapshots/test_ui_snapshot_question_app.py#L78)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `MultiQuestionApp`

**Bases:** `QuestionAppTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L83`](tests/snapshots/test_ui_snapshot_question_app.py#L83)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `MultiSelectApp`

**Bases:** `QuestionAppTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L88`](tests/snapshots/test_ui_snapshot_question_app.py#L88)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `single_question_args()`

```python
def single_question_args() -> AskUserQuestionArgs
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L16`](tests/snapshots/test_ui_snapshot_question_app.py#L16)

## `multi_question_args()`

```python
def multi_question_args() -> AskUserQuestionArgs
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L32`](tests/snapshots/test_ui_snapshot_question_app.py#L32)

## `multi_select_args()`

```python
def multi_select_args() -> AskUserQuestionArgs
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L49`](tests/snapshots/test_ui_snapshot_question_app.py#L49)

## `test_snapshot_question_app_initial()`

```python
def test_snapshot_question_app_initial(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L96`](tests/snapshots/test_ui_snapshot_question_app.py#L96)

## `test_snapshot_question_app_navigate_down()`

```python
def test_snapshot_question_app_navigate_down(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L107`](tests/snapshots/test_ui_snapshot_question_app.py#L107)

## `test_snapshot_question_app_navigate_to_third_option()`

```python
def test_snapshot_question_app_navigate_to_third_option(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L120`](tests/snapshots/test_ui_snapshot_question_app.py#L120)

## `test_snapshot_question_app_navigate_to_other()`

```python
def test_snapshot_question_app_navigate_to_other(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L136`](tests/snapshots/test_ui_snapshot_question_app.py#L136)

## `test_snapshot_question_app_navigate_up_wraps()`

```python
def test_snapshot_question_app_navigate_up_wraps(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L151`](tests/snapshots/test_ui_snapshot_question_app.py#L151)

## `test_snapshot_question_app_other_typing()`

```python
def test_snapshot_question_app_other_typing(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L164`](tests/snapshots/test_ui_snapshot_question_app.py#L164)

## `test_snapshot_multi_question_initial()`

```python
def test_snapshot_multi_question_initial(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L183`](tests/snapshots/test_ui_snapshot_question_app.py#L183)

## `test_snapshot_multi_question_tab_to_second()`

```python
def test_snapshot_multi_question_tab_to_second(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L194`](tests/snapshots/test_ui_snapshot_question_app.py#L194)

## `test_snapshot_multi_question_answer_first_advance()`

```python
def test_snapshot_multi_question_answer_first_advance(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L207`](tests/snapshots/test_ui_snapshot_question_app.py#L207)

## `test_snapshot_multi_question_navigate_right()`

```python
def test_snapshot_multi_question_navigate_right(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L222`](tests/snapshots/test_ui_snapshot_question_app.py#L222)

## `test_snapshot_multi_question_navigate_left_wraps()`

```python
def test_snapshot_multi_question_navigate_left_wraps(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L235`](tests/snapshots/test_ui_snapshot_question_app.py#L235)

## `test_snapshot_multi_question_first_answered_checkmark()`

```python
def test_snapshot_multi_question_first_answered_checkmark(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L248`](tests/snapshots/test_ui_snapshot_question_app.py#L248)

## `test_snapshot_multi_select_initial()`

```python
def test_snapshot_multi_select_initial(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L267`](tests/snapshots/test_ui_snapshot_question_app.py#L267)

## `test_snapshot_multi_select_toggle_first()`

```python
def test_snapshot_multi_select_toggle_first(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L278`](tests/snapshots/test_ui_snapshot_question_app.py#L278)

## `test_snapshot_multi_select_toggle_multiple()`

```python
def test_snapshot_multi_select_toggle_multiple(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L291`](tests/snapshots/test_ui_snapshot_question_app.py#L291)

## `test_snapshot_multi_select_navigate_to_submit()`

```python
def test_snapshot_multi_select_navigate_to_submit(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L306`](tests/snapshots/test_ui_snapshot_question_app.py#L306)

## `test_snapshot_multi_select_other_with_text()`

```python
def test_snapshot_multi_select_other_with_text(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L319`](tests/snapshots/test_ui_snapshot_question_app.py#L319)

## `test_snapshot_multi_select_mixed_selection()`

```python
def test_snapshot_multi_select_mixed_selection(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L335`](tests/snapshots/test_ui_snapshot_question_app.py#L335)

## `test_snapshot_multi_select_untoggle()`

```python
def test_snapshot_multi_select_untoggle(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_question_app.py#L354`](tests/snapshots/test_ui_snapshot_question_app.py#L354)

