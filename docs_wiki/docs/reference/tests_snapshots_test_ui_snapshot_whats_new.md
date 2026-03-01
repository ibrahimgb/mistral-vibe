---
title: "tests.snapshots.test_ui_snapshot_whats_new"
tldr: "Module tests.snapshots.test_ui_snapshot_whats_new"
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_whats_new`

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py`](tests/snapshots/test_ui_snapshot_whats_new.py) · 156 lines

## `SnapshotTestAppWithWhatsNew`

**Bases:** `BaseSnapshotTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L21`](tests/snapshots/test_ui_snapshot_whats_new.py#L21)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | gateway | `—` | — |
| `on_unmount()` |  | `None` | — |

## `SnapshotTestAppWithPlanUpgradeCTA`

**Bases:** `SnapshotTestAppWithWhatsNew`

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L51`](tests/snapshots/test_ui_snapshot_whats_new.py#L51)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `SnapshotTestAppWithSwitchKeyCTA`

**Bases:** `SnapshotTestAppWithWhatsNew`

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L64`](tests/snapshots/test_ui_snapshot_whats_new.py#L64)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `SnapshotTestAppWithWhatsNewNoPlanCTA`

**Bases:** `SnapshotTestAppWithWhatsNew`

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L77`](tests/snapshots/test_ui_snapshot_whats_new.py#L77)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `test_snapshot_shows_whats_new_message()`

```python
def test_snapshot_shows_whats_new_message(snap_compare: SnapCompare, tmp_path: Path) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L90`](tests/snapshots/test_ui_snapshot_whats_new.py#L90)

## `test_snapshot_shows_upgrade_message()`

```python
def test_snapshot_shows_upgrade_message(snap_compare: SnapCompare, tmp_path: Path) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L108`](tests/snapshots/test_ui_snapshot_whats_new.py#L108)

## `test_snapshot_shows_switch_message()`

```python
def test_snapshot_shows_switch_message(snap_compare: SnapCompare, tmp_path: Path) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L125`](tests/snapshots/test_ui_snapshot_whats_new.py#L125)

## `test_snapshot_shows_no_plan_message()`

```python
def test_snapshot_shows_no_plan_message(snap_compare: SnapCompare, tmp_path: Path) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_whats_new.py#L142`](tests/snapshots/test_ui_snapshot_whats_new.py#L142)

