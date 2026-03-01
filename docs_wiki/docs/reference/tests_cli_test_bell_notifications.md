---
title: "tests.cli.test_bell_notifications"
tldr: "Module tests.cli.test_bell_notifications"
tags: [reference, api]
---

# `tests.cli.test_bell_notifications`

**Source:** [`tests/cli/test_bell_notifications.py`](tests/cli/test_bell_notifications.py) · 151 lines

## `TestTextualNotificationAdapter`

**Source:** [`tests/cli/test_bell_notifications.py#L38`](tests/cli/test_bell_notifications.py#L38)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_no_notification_when_disabled()` | adapter_disabled, fake_app | `None` | — |
| `test_no_notification_when_focused()` | adapter_enabled, fake_app | `None` | — |
| `test_notification_sent_when_unfocused_and_enabled()` | adapter_enabled, fake_app | `None` | — |
| `test_throttle_prevents_rapid_notifications()` | adapter_enabled, fake_app | `None` | — |
| `test_contextual_title_for_action_required()` | adapter_enabled, fake_app | `None` | — |
| `test_contextual_title_for_complete()` | adapter_enabled, fake_app | `None` | — |
| `test_restore_sets_default_title()` | adapter_enabled, fake_app | `None` | — |
| `test_on_focus_restores_title()` | adapter_enabled, fake_app | `None` | — |
| `test_on_focus_prevents_notifications()` | adapter_enabled, fake_app | `None` | — |
| `test_no_title_write_when_headless()` |  | `None` | — |
| `test_enabled_callback_reads_live_value()` | fake_app | `None` | — |

## `_make_fake_app()`

```python
def _make_fake_app() -> MagicMock
```

**Source:** [`tests/cli/test_bell_notifications.py#L13`](tests/cli/test_bell_notifications.py#L13)

## `fake_app()`

```python
def fake_app() -> MagicMock
```

**Source:** [`tests/cli/test_bell_notifications.py#L20`](tests/cli/test_bell_notifications.py#L20)

## `adapter_enabled()`

```python
def adapter_enabled(fake_app: MagicMock) -> TextualNotificationAdapter
```

**Source:** [`tests/cli/test_bell_notifications.py#L25`](tests/cli/test_bell_notifications.py#L25)

## `adapter_disabled()`

```python
def adapter_disabled(fake_app: MagicMock) -> TextualNotificationAdapter
```

**Source:** [`tests/cli/test_bell_notifications.py#L32`](tests/cli/test_bell_notifications.py#L32)

