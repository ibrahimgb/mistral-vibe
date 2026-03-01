---
title: "tests.snapshots.base_snapshot_test_app"
tldr: "Module tests.snapshots.base_snapshot_test_app"
tags: [reference, api]
---

# `tests.snapshots.base_snapshot_test_app`

**Source:** [`tests/snapshots/base_snapshot_test_app.py`](tests/snapshots/base_snapshot_test_app.py) · 69 lines

## `BaseSnapshotTestApp`

**Bases:** `VibeApp`

**Source:** [`tests/snapshots/base_snapshot_test_app.py#L29`](tests/snapshots/base_snapshot_test_app.py#L29)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | config, backend | `—` | — |
| 🔄 `on_mount()` |  | `None` | — |

??? note "Private Methods"

    - `def _hide_chat_input_cursor(self) -> None`

## `default_config()`

```python
def default_config() -> VibeConfig
```

Default configuration for snapshot testing.
Remove as much interference as possible from the snapshot comparison, in order to get a clean pixel-to-pixel comparison.
- Injects a fake backend to prevent (or stub) LLM calls.
- Disables the banner animation.
- Forces a value for the displayed workdir
- Hides the chat input cursor (as the blinking animation is not deterministic).

**Source:** [`tests/snapshots/base_snapshot_test_app.py#L16`](tests/snapshots/base_snapshot_test_app.py#L16)

