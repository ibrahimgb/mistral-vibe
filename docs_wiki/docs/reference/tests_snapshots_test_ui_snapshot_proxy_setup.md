---
title: "tests.snapshots.test_ui_snapshot_proxy_setup"
tldr: "Module tests.snapshots.test_ui_snapshot_proxy_setup"
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_proxy_setup`

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py`](tests/snapshots/test_ui_snapshot_proxy_setup.py) · 129 lines

## `ProxySetupTestApp`

**Bases:** `BaseSnapshotTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L11`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L11)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `on_mount()` |  | `None` | — |

## `PrePopulatedProxySetupTestApp`

**Bases:** `BaseSnapshotTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L17`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L17)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `on_mount()` |  | `None` | — |

## `test_snapshot_proxy_setup_initial_empty()`

```python
def test_snapshot_proxy_setup_initial_empty(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L25`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L25)

## `test_snapshot_proxy_setup_initial_with_values()`

```python
def test_snapshot_proxy_setup_initial_with_values(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L36`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L36)

## `test_snapshot_proxy_setup_save_new_values()`

```python
def test_snapshot_proxy_setup_save_new_values(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L47`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L47)

## `test_snapshot_proxy_setup_edit_existing_values()`

```python
def test_snapshot_proxy_setup_edit_existing_values(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L68`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L68)

## `test_snapshot_proxy_setup_cancel_discards_changes()`

```python
def test_snapshot_proxy_setup_cancel_discards_changes(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L90`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L90)

## `test_snapshot_proxy_setup_save_error()`

```python
def test_snapshot_proxy_setup_save_error(snap_compare: SnapCompare, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_proxy_setup.py#L111`](tests/snapshots/test_ui_snapshot_proxy_setup.py#L111)

