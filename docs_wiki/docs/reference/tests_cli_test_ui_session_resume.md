---
title: "tests.cli.test_ui_session_resume"
tldr: "Module tests.cli.test_ui_session_resume"
tags: [reference, api]
---

# `tests.cli.test_ui_session_resume`

**Source:** [`tests/cli/test_ui_session_resume.py`](tests/cli/test_ui_session_resume.py) · 197 lines

## `test_ui_displays_messages_when_resuming_session()`

```python
async def test_ui_displays_messages_when_resuming_session(vibe_config: VibeConfig) -> None
```

Test that messages are properly displayed when resuming a session.

**Source:** [`tests/cli/test_ui_session_resume.py#L32`](tests/cli/test_ui_session_resume.py#L32)

## `test_ui_does_not_display_messages_when_only_system_messages_exist()`

```python
async def test_ui_does_not_display_messages_when_only_system_messages_exist(vibe_config: VibeConfig) -> None
```

Test that no messages are displayed when only system messages exist.

**Source:** [`tests/cli/test_ui_session_resume.py#L91`](tests/cli/test_ui_session_resume.py#L91)

## `test_ui_displays_multiple_user_assistant_turns()`

```python
async def test_ui_displays_multiple_user_assistant_turns(vibe_config: VibeConfig) -> None
```

Test that multiple conversation turns are properly displayed.

**Source:** [`tests/cli/test_ui_session_resume.py#L115`](tests/cli/test_ui_session_resume.py#L115)

## `test_ui_rebuilds_history_when_whats_new_is_shown()`

```python
async def test_ui_rebuilds_history_when_whats_new_is_shown(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None
```

**Source:** [`tests/cli/test_ui_session_resume.py#L149`](tests/cli/test_ui_session_resume.py#L149)

