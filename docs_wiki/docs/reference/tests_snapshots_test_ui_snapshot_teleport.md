---
title: "tests.snapshots.test_ui_snapshot_teleport"
tldr: "Module tests.snapshots.test_ui_snapshot_teleport"
tags: [reference, api]
---

# `tests.snapshots.test_ui_snapshot_teleport`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py`](tests/snapshots/test_ui_snapshot_teleport.py) · 249 lines

## `TeleportMessageTestApp`

**Bases:** `App`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L17`](tests/snapshots/test_ui_snapshot_teleport.py#L17)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `compose()` |  | `ComposeResult` | — |

## `TeleportMessageCheckingGitApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L25`](tests/snapshots/test_ui_snapshot_teleport.py#L25)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportMessagePushingApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L33`](tests/snapshots/test_ui_snapshot_teleport.py#L33)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportMessageAuthRequiredApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L41`](tests/snapshots/test_ui_snapshot_teleport.py#L41)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportMessageAuthCompleteApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L51`](tests/snapshots/test_ui_snapshot_teleport.py#L51)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportMessageStartingWorkflowApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L59`](tests/snapshots/test_ui_snapshot_teleport.py#L59)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportMessageSendingTokenApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L67`](tests/snapshots/test_ui_snapshot_teleport.py#L67)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportMessageCompleteApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L75`](tests/snapshots/test_ui_snapshot_teleport.py#L75)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportMessageErrorApp`

**Bases:** `TeleportMessageTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L81`](tests/snapshots/test_ui_snapshot_teleport.py#L81)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `on_mount()` |  | `None` | — |

## `TeleportPushConfirmationTestApp`

**Bases:** `App`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L101`](tests/snapshots/test_ui_snapshot_teleport.py#L101)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | count | `—` | — |
| `compose()` |  | `ComposeResult` | — |

## `TeleportPushConfirmationSingleCommitApp`

**Bases:** `TeleportPushConfirmationTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L113`](tests/snapshots/test_ui_snapshot_teleport.py#L113)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `TeleportPushConfirmationMultipleCommitsApp`

**Bases:** `TeleportPushConfirmationTestApp`

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L118`](tests/snapshots/test_ui_snapshot_teleport.py#L118)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `—` | — |

## `_push_confirmation_args()`

```python
def _push_confirmation_args(count: int) -> AskUserQuestionArgs
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L87`](tests/snapshots/test_ui_snapshot_teleport.py#L87)

## `test_snapshot_teleport_status_checking_git()`

```python
def test_snapshot_teleport_status_checking_git(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L123`](tests/snapshots/test_ui_snapshot_teleport.py#L123)

## `test_snapshot_teleport_status_pushing()`

```python
def test_snapshot_teleport_status_pushing(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L134`](tests/snapshots/test_ui_snapshot_teleport.py#L134)

## `test_snapshot_teleport_status_auth_required()`

```python
def test_snapshot_teleport_status_auth_required(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L145`](tests/snapshots/test_ui_snapshot_teleport.py#L145)

## `test_snapshot_teleport_status_auth_complete()`

```python
def test_snapshot_teleport_status_auth_complete(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L156`](tests/snapshots/test_ui_snapshot_teleport.py#L156)

## `test_snapshot_teleport_status_starting_workflow()`

```python
def test_snapshot_teleport_status_starting_workflow(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L167`](tests/snapshots/test_ui_snapshot_teleport.py#L167)

## `test_snapshot_teleport_status_sending_token()`

```python
def test_snapshot_teleport_status_sending_token(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L178`](tests/snapshots/test_ui_snapshot_teleport.py#L178)

## `test_snapshot_teleport_status_complete()`

```python
def test_snapshot_teleport_status_complete(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L189`](tests/snapshots/test_ui_snapshot_teleport.py#L189)

## `test_snapshot_teleport_status_error()`

```python
def test_snapshot_teleport_status_error(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L200`](tests/snapshots/test_ui_snapshot_teleport.py#L200)

## `test_snapshot_teleport_push_confirmation_single_commit()`

```python
def test_snapshot_teleport_push_confirmation_single_commit(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L211`](tests/snapshots/test_ui_snapshot_teleport.py#L211)

## `test_snapshot_teleport_push_confirmation_multiple_commits()`

```python
def test_snapshot_teleport_push_confirmation_multiple_commits(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L224`](tests/snapshots/test_ui_snapshot_teleport.py#L224)

## `test_snapshot_teleport_push_confirmation_cancel_selected()`

```python
def test_snapshot_teleport_push_confirmation_cancel_selected(snap_compare: SnapCompare) -> None
```

**Source:** [`tests/snapshots/test_ui_snapshot_teleport.py#L237`](tests/snapshots/test_ui_snapshot_teleport.py#L237)

