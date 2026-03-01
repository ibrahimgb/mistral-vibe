---
title: "tests.cli.test_ui_clipboard_notifications"
tldr: "Module tests.cli.test_ui_clipboard_notifications"
tags: [reference, api]
---

# `tests.cli.test_ui_clipboard_notifications`

**Source:** [`tests/cli/test_ui_clipboard_notifications.py`](tests/cli/test_ui_clipboard_notifications.py) · 40 lines

## `ClipboardSelectionWidget`

**Bases:** `Widget`

**Source:** [`tests/cli/test_ui_clipboard_notifications.py#L13`](tests/cli/test_ui_clipboard_notifications.py#L13)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | selected_text | `None` | — |
| `text_selection()` |  | `Selection | None` | — |
| `get_selection()` | selection | `tuple[str, str] | None` | — |

## `test_ui_clipboard_notification_does_not_crash_on_markup_text()`

```python
async def test_ui_clipboard_notification_does_not_crash_on_markup_text(monkeypatch: pytest.MonkeyPatch, vibe_app: VibeApp) -> None
```

**Source:** [`tests/cli/test_ui_clipboard_notifications.py#L27`](tests/cli/test_ui_clipboard_notifications.py#L27)

