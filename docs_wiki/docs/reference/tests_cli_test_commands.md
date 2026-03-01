---
title: "tests.cli.test_commands"
tldr: "Module tests.cli.test_commands"
tags: [reference, api]
---

# `tests.cli.test_commands`

**Source:** [`tests/cli/test_commands.py`](tests/cli/test_commands.py) · 62 lines

## `TestCommandRegistry`

**Source:** [`tests/cli/test_commands.py#L6`](tests/cli/test_commands.py#L6)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_get_command_name_returns_canonical_name_for_alias()` |  | `None` | — |
| `test_get_command_name_normalizes_input()` |  | `None` | — |
| `test_get_command_name_returns_none_for_unknown()` |  | `None` | — |
| `test_find_command_returns_command_when_alias_matches()` |  | `None` | — |
| `test_find_command_returns_none_when_no_match()` |  | `None` | — |
| `test_find_command_uses_get_command_name()` |  | `None` | find_command and get_command_name stay in sync for same input. |
| `test_excluded_commands_not_in_registry()` |  | `None` | — |
| `test_resume_command_registration()` |  | `None` | — |

