---
title: "vibe.cli.textual_ui.notifications.ports.notification_port"
tldr: "Module vibe.cli.textual_ui.notifications.ports.notification_port"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.notifications.ports.notification_port**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/notifications/ports/notification_port.py)

## [**NotificationContext**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/notifications/ports/notification_port.py#L7)

The [**NotificationContext**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/notifications/ports/notification_port.py#L7) enum (extending `StrEnum`). Key fields include `ACTION_REQUIRED`, `COMPLETE`.

## [**NotificationPort**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/notifications/ports/notification_port.py#L12)

The [**NotificationPort**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/notifications/ports/notification_port.py#L12) protocol (extending `Protocol`). It exposes `notify()`, `on_focus()`, `on_blur()`, `restore()`.

**Public API:**

- `def notify()`
- `def on_focus()`
- `def on_blur()`
- `def restore()`

