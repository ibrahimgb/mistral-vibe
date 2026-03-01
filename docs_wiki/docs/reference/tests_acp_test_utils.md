---
title: "tests.acp.test_utils"
tldr: "Module tests.acp.test_utils"
tags: [reference, api]
---

# `tests.acp.test_utils`

**Source:** [`tests/acp/test_utils.py`](tests/acp/test_utils.py) · 55 lines

## `TestGetProxyHelpText`

**Source:** [`tests/acp/test_utils.py#L13`](tests/acp/test_utils.py#L13)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_string()` |  | `None` | — |
| `test_includes_proxy_configuration_header()` |  | `None` | — |
| `test_includes_usage_section()` |  | `None` | — |
| `test_includes_all_supported_variables()` |  | `None` | — |
| `test_shows_none_configured_when_no_settings()` |  | `None` | — |
| `test_shows_current_settings_when_configured()` |  | `None` | — |
| `test_shows_only_set_values()` |  | `None` | — |

## `_write_env_file()`

```python
def _write_env_file(content: str) -> None
```

**Source:** [`tests/acp/test_utils.py#L8`](tests/acp/test_utils.py#L8)

