---
title: "tests.cli.test_external_editor"
tldr: "Tests for the external editor module."
tags: [reference, api]
---

# `tests.cli.test_external_editor`

**Source:** [`tests/cli/test_external_editor.py`](tests/cli/test_external_editor.py) · 72 lines

Tests for the external editor module.

## `TestGetEditor`

**Source:** [`tests/cli/test_external_editor.py#L10`](tests/cli/test_external_editor.py#L10)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_visual_first()` |  | `None` | — |
| `test_falls_back_to_editor()` |  | `None` | — |
| `test_falls_back_when_no_editor()` |  | `None` | — |

## `TestEdit`

**Source:** [`tests/cli/test_external_editor.py#L24`](tests/cli/test_external_editor.py#L24)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_modified_content()` |  | `None` | — |
| `test_returns_none_when_content_unchanged()` |  | `None` | — |
| `test_strips_trailing_whitespace()` |  | `None` | — |
| `test_handles_editor_with_args()` |  | `None` | — |
| `test_returns_none_on_subprocess_error()` |  | `None` | — |

