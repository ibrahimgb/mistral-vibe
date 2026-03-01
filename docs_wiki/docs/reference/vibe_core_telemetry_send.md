---
title: "vibe.core.telemetry.send"
tldr: "Module vibe.core.telemetry.send"
tags: [reference, api]
---

# [**vibe.core.telemetry.send**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/telemetry/send.py)

This module defines the constants `DATALAKE_EVENTS_URL`.

## [**TelemetryClient**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/telemetry/send.py#L21)

The [**TelemetryClient**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/telemetry/send.py#L21) class. It exposes `__init__()`, `send_telemetry_event()`, `aclose()`, `send_tool_call_finished()`, `send_user_copied_text()` among 10 public methods. Internally it relies on `_get_mistral_api_key()`, `_is_enabled()`.

**Public API:**

- `def __init__()`
- `def client()`
- `def send_telemetry_event()`
- `async def aclose()`
- `def send_tool_call_finished()`
- `def send_user_copied_text()`
- `def send_user_cancelled_action()`
- `def send_auto_compact_triggered()`
- `def send_slash_command_used()`
- `def send_new_session()`
- `def send_onboarding_api_key_added()`

**Internal helpers:**

- `_get_mistral_api_key()` — Get the current API key from the active provider.
- `_is_enabled()` — Check if telemetry is enabled in the current config.

