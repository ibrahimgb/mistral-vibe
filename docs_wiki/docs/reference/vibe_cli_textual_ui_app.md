---
title: "vibe.cli.textual_ui.app"
tldr: "Module vibe.cli.textual_ui.app"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.app**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py)

This module defines the constants `PRUNE_LOW_MARK`, `PRUNE_HIGH_MARK`.

## [**BottomApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L128)

The [**BottomApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L128) enum (extending `StrEnum`) bottom panel app types. Key fields include `Approval`, `Config`, `Input`, `ProxySetup`, `Question`, `SessionPicker`.

## [**ChatScroll**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L144)

The [**ChatScroll**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L144) class (extending `VerticalScroll`) optimized scroll container that skips cascading style recalculations. It exposes `update_node_styles()`.

**Public API:**

- `def is_at_bottom()`
- `def update_node_styles()`

## [**VibeApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L195)

The [**VibeApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L195) class (extending `App`). It exposes `__init__()`, `compose()`, `on_mount()`, `on_chat_input_container_submitted()`, `on_approval_app_approval_granted()` among 28 public methods. Internally it relies on `_handle_skill()`, `_handle_bash_command()`, `_resume_history_from_messages()`.

**Public API:**

- `def __init__()`
- `def config()`
- `def compose()`
- `async def on_mount()`
- `async def on_chat_input_container_submitted()`
- `async def on_approval_app_approval_granted()`
- `async def on_approval_app_approval_granted_always_tool()`
- `async def on_approval_app_approval_rejected()`
- `async def on_question_app_answered()`
- `async def on_question_app_cancelled()`
- `async def on_config_app_config_closed()`
- `async def on_proxy_setup_app_proxy_setup_closed()`
- `async def on_compact_message_completed()`
- `async def on_session_picker_app_session_selected()`
- `async def on_session_picker_app_cancelled()`
- `def action_interrupt()`
- `async def on_history_load_more_requested()`
- `async def action_toggle_tool()`
- `def action_cycle_mode()`
- `def action_clear_quit()`
- `def action_force_quit()`
- `def action_scroll_chat_up()`
- `def action_scroll_chat_down()`
- `def action_toggle_recording()` — Toggle voice recording via the mic button (Ctrl+R).
- `def action_copy_selection()`
- `def on_mouse_up()`
- `def on_app_blur()`
- `def on_app_focus()`
- `def action_suspend_with_message()`

**Internal helpers:**

- `_handle_skill()`
- `_handle_bash_command()`
- `_resume_history_from_messages()`
- `_mount_history_batch()`
- `_handle_agent_loop_turn()`
- `_teleport()`
- `_ask_push_approval()`
- `_interrupt_agent_loop()`
- `_wiki_command()` — Build the Code Wiki and display a summary.
- `_show_config()` — Switch to the configuration app in the bottom panel.
- `_show_session_picker()`
- `_clear_history()`
- `_show_log_path()`
- `_compact_history()`
- `_cycle_agent()`
- `_check_and_show_whats_new()`
- `_plan_offer_cta()`
- `_check_update()`

## [**prune_oldest_children()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L159)

```python
async def prune_oldest_children(messages_area: Widget, low_mark: int, high_mark: int) -> bool
```

Remove the oldest children so the virtual height stays within bounds.

Walks children back-to-front to find how much to keep (up to *low_mark*
of visible height), then removes everything before that point.

## [**run_textual_ui()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/app.py#L1676)

```python
def run_textual_ui(agent_loop: AgentLoop, initial_prompt: str | None, teleport_on_start: bool) -> None
```

