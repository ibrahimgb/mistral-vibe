---
title: "tests.cli.textual_ui.test_session_picker"
tldr: "Module tests.cli.textual_ui.test_session_picker"
tags: [reference, api]
---

# `tests.cli.textual_ui.test_session_picker`

**Source:** [`tests/cli/textual_ui/test_session_picker.py`](tests/cli/textual_ui/test_session_picker.py) · 131 lines

## `TestFormatRelativeTime`

**Source:** [`tests/cli/textual_ui/test_session_picker.py#L47`](tests/cli/textual_ui/test_session_picker.py#L47)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_just_now()` |  | `None` | — |
| `test_minutes_ago()` |  | `None` | — |
| `test_hours_ago()` |  | `None` | — |
| `test_days_ago()` |  | `None` | — |
| `test_weeks_ago()` |  | `None` | — |
| `test_none_returns_unknown()` |  | `None` | — |
| `test_invalid_format_returns_unknown()` |  | `None` | — |
| `test_handles_z_suffix()` |  | `None` | — |
| `test_boundary_59_seconds()` |  | `None` | — |
| `test_boundary_60_seconds()` |  | `None` | — |

## `TestSessionPickerAppInit`

**Source:** [`tests/cli/textual_ui/test_session_picker.py#L87`](tests/cli/textual_ui/test_session_picker.py#L87)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_init_sets_properties()` | sample_sessions, sample_latest_messages | `None` | — |
| `test_id_is_sessionpicker_app()` |  | `None` | — |
| `test_can_focus_children_is_true()` |  | `None` | — |

## `TestSessionPickerMessages`

**Source:** [`tests/cli/textual_ui/test_session_picker.py#L105`](tests/cli/textual_ui/test_session_picker.py#L105)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_session_selected_stores_session_id()` |  | `None` | — |
| `test_session_selected_with_full_uuid()` |  | `None` | — |
| `test_cancelled_can_be_instantiated()` |  | `None` | — |

## `TestSessionPickerAppBindings`

**Source:** [`tests/cli/textual_ui/test_session_picker.py#L120`](tests/cli/textual_ui/test_session_picker.py#L120)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_has_escape_binding()` |  | `None` | — |

??? note "Private Methods"

    - `def _get_binding_keys(self) -> list[str]`

## `sample_sessions()`

```python
def sample_sessions() -> list[SessionInfo]
```

**Source:** [`tests/cli/textual_ui/test_session_picker.py#L15`](tests/cli/textual_ui/test_session_picker.py#L15)

## `sample_latest_messages()`

```python
def sample_latest_messages() -> dict[str, str]
```

**Source:** [`tests/cli/textual_ui/test_session_picker.py#L39`](tests/cli/textual_ui/test_session_picker.py#L39)

