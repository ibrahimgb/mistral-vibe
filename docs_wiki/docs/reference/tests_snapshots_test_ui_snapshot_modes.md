---
title: "tests.snapshots.test_ui_snapshot_modes"
tldr: "Module tests.snapshots.test_ui_snapshot_modes"
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_modes`

**Source:** [`tests/snapshots/test_ui_snapshot_modes.py`](tests/snapshots/test_ui_snapshot_modes.py) · 88 lines

## `test_snapshot_default_mode()`

```python
def test_snapshot_default_mode(snap_compare: SnapCompare) -> None
```

Test that default mode is displayed correctly at startup.

**Source:** [`tests/snapshots/test_ui_snapshot_modes.py#L8`](tests/snapshots/test_ui_snapshot_modes.py#L8)

## `test_snapshot_cycle_to_plan_mode()`

```python
def test_snapshot_cycle_to_plan_mode(snap_compare: SnapCompare) -> None
```

Test that shift+tab cycles from default to plan mode.

**Source:** [`tests/snapshots/test_ui_snapshot_modes.py#L21`](tests/snapshots/test_ui_snapshot_modes.py#L21)

## `test_snapshot_cycle_to_accept_edits_mode()`

```python
def test_snapshot_cycle_to_accept_edits_mode(snap_compare: SnapCompare) -> None
```

Test that shift+tab cycles from plan to accept edits mode.

**Source:** [`tests/snapshots/test_ui_snapshot_modes.py#L37`](tests/snapshots/test_ui_snapshot_modes.py#L37)

## `test_snapshot_cycle_to_auto_approve_mode()`

```python
def test_snapshot_cycle_to_auto_approve_mode(snap_compare: SnapCompare) -> None
```

Test that shift+tab cycles to auto approve mode.

**Source:** [`tests/snapshots/test_ui_snapshot_modes.py#L54`](tests/snapshots/test_ui_snapshot_modes.py#L54)

## `test_snapshot_cycle_wraps_to_default()`

```python
def test_snapshot_cycle_wraps_to_default(snap_compare: SnapCompare) -> None
```

Test that shift+tab cycles back to default mode after auto approve.

**Source:** [`tests/snapshots/test_ui_snapshot_modes.py#L72`](tests/snapshots/test_ui_snapshot_modes.py#L72)

