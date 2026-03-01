---
title: "tests.update_notifier.test_ui_update_notification"
tldr: "Module tests.update_notifier.test_ui_update_notification"
tags: [reference, api]
---

# `tests.update_notifier.test_ui_update_notification`

**Source:** [`tests/update_notifier/test_ui_update_notification.py`](tests/update_notifier/test_ui_update_notification.py) · 389 lines

## Constants

- `TEST_CURRENT_VERSION`

## `build_update_test_app()`

```python
def build_update_test_app(vibe_config_with_update_checks_enabled: VibeConfig) -> Callable[..., VibeApp]
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L33`](tests/update_notifier/test_ui_update_notification.py#L33)

## `_wait_for_notification()`

```python
async def _wait_for_notification(app: VibeApp, pilot) -> Notification
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L53`](tests/update_notifier/test_ui_update_notification.py#L53)

## `_assert_no_notifications()`

```python
async def _assert_no_notifications(app: VibeApp, pilot) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L68`](tests/update_notifier/test_ui_update_notification.py#L68)

## `vibe_config_with_update_checks_enabled()`

```python
def vibe_config_with_update_checks_enabled() -> VibeConfig
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L83`](tests/update_notifier/test_ui_update_notification.py#L83)

## `test_ui_displays_update_notification()`

```python
async def test_ui_displays_update_notification(build_update_test_app: Callable[..., VibeApp]) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L88`](tests/update_notifier/test_ui_update_notification.py#L88)

## `test_ui_does_not_display_update_notification_when_not_available()`

```python
async def test_ui_does_not_display_update_notification_when_not_available(build_update_test_app: Callable[..., VibeApp]) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L106`](tests/update_notifier/test_ui_update_notification.py#L106)

## `test_ui_displays_warning_toast_when_check_fails()`

```python
async def test_ui_displays_warning_toast_when_check_fails(build_update_test_app: Callable[..., VibeApp]) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L118`](tests/update_notifier/test_ui_update_notification.py#L118)

## `test_ui_does_not_invoke_gateway_nor_show_error_notification_when_update_checks_are_disabled()`

```python
async def test_ui_does_not_invoke_gateway_nor_show_error_notification_when_update_checks_are_disabled(build_update_test_app: Callable[..., VibeApp], vibe_config: VibeConfig) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L137`](tests/update_notifier/test_ui_update_notification.py#L137)

## `test_ui_does_not_show_toast_when_update_is_known_in_recent_cache_already()`

```python
async def test_ui_does_not_show_toast_when_update_is_known_in_recent_cache_already(build_update_test_app: Callable[..., VibeApp])
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L150`](tests/update_notifier/test_ui_update_notification.py#L150)

## `test_ui_does_show_toast_when_cache_entry_is_too_old()`

```python
async def test_ui_does_show_toast_when_cache_entry_is_too_old(build_update_test_app: Callable[..., VibeApp]) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L170`](tests/update_notifier/test_ui_update_notification.py#L170)

## `_wait_for_whats_new_message()`

```python
async def _wait_for_whats_new_message(app: VibeApp, pilot) -> WhatsNewMessage
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L198`](tests/update_notifier/test_ui_update_notification.py#L198)

## `test_ui_displays_whats_new_message_when_content_exists()`

```python
async def test_ui_displays_whats_new_message_when_content_exists(build_update_test_app: Callable[..., VibeApp], tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L217`](tests/update_notifier/test_ui_update_notification.py#L217)

## `test_ui_does_not_display_whats_new_when_seen_whats_new_version_matches()`

```python
async def test_ui_does_not_display_whats_new_when_seen_whats_new_version_matches(build_update_test_app: Callable[..., VibeApp], tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L249`](tests/update_notifier/test_ui_update_notification.py#L249)

## `test_ui_does_not_display_whats_new_when_file_is_empty()`

```python
async def test_ui_does_not_display_whats_new_when_file_is_empty(build_update_test_app: Callable[..., VibeApp], tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L280`](tests/update_notifier/test_ui_update_notification.py#L280)

## `test_ui_does_not_display_whats_new_when_file_does_not_exist()`

```python
async def test_ui_does_not_display_whats_new_when_file_does_not_exist(build_update_test_app: Callable[..., VibeApp], tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L314`](tests/update_notifier/test_ui_update_notification.py#L314)

## `test_ui_displays_success_notification_when_auto_update_succeeds()`

```python
async def test_ui_displays_success_notification_when_auto_update_succeeds(build_update_test_app: Callable[..., VibeApp]) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L345`](tests/update_notifier/test_ui_update_notification.py#L345)

## `test_ui_displays_update_notification_when_auto_update_fails()`

```python
async def test_ui_displays_update_notification_when_auto_update_fails(build_update_test_app: Callable[..., VibeApp]) -> None
```

**Source:** [`tests/update_notifier/test_ui_update_notification.py#L369`](tests/update_notifier/test_ui_update_notification.py#L369)

