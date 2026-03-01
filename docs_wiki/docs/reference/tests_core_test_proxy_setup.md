---
title: "tests.core.test_proxy_setup"
tldr: "Module tests.core.test_proxy_setup"
tags: [reference, api]
---

# `tests.core.test_proxy_setup`

**Source:** [`tests/core/test_proxy_setup.py`](tests/core/test_proxy_setup.py) · 304 lines

## `TestProxySetupError`

**Source:** [`tests/core/test_proxy_setup.py#L21`](tests/core/test_proxy_setup.py#L21)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_inherits_from_exception()` |  | `None` | — |
| `test_preserves_message()` |  | `None` | — |

## `TestSupportedProxyVars`

**Source:** [`tests/core/test_proxy_setup.py#L30`](tests/core/test_proxy_setup.py#L30)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_contains_all_expected_keys()` |  | `None` | — |
| `test_all_keys_are_uppercase()` |  | `None` | — |
| `test_all_values_are_non_empty_strings()` |  | `None` | — |

## `TestGetCurrentProxySettings`

**Source:** [`tests/core/test_proxy_setup.py#L52`](tests/core/test_proxy_setup.py#L52)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_all_none_when_env_file_does_not_exist()` |  | `None` | — |
| `test_returns_dict_with_all_supported_keys()` |  | `None` | — |
| `test_returns_values_from_env_file()` |  | `None` | — |
| `test_returns_none_for_unset_keys()` |  | `None` | — |
| `test_ignores_non_proxy_vars_in_env_file()` |  | `None` | — |
| `test_handles_values_with_special_characters()` |  | `None` | — |
| `test_returns_all_none_when_env_file_read_fails()` | monkeypatch | `None` | — |

## `TestSetProxyVar`

**Source:** [`tests/core/test_proxy_setup.py#L112`](tests/core/test_proxy_setup.py#L112)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_sets_valid_proxy_var()` |  | `None` | — |
| `test_sets_all_supported_vars()` | key | `None` | — |
| `test_uppercases_key_before_validation()` |  | `None` | — |
| `test_raises_error_for_unknown_key()` |  | `None` | — |
| `test_error_message_contains_supported_keys()` |  | `None` | — |
| `test_creates_env_file_if_missing()` |  | `None` | — |
| `test_overwrites_existing_value()` |  | `None` | — |
| `test_preserves_other_values()` |  | `None` | — |
| `test_handles_value_with_spaces()` |  | `None` | — |
| `test_handles_url_with_credentials()` |  | `None` | — |

## `TestUnsetProxyVar`

**Source:** [`tests/core/test_proxy_setup.py#L181`](tests/core/test_proxy_setup.py#L181)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_removes_existing_var()` |  | `None` | — |
| `test_uppercases_key_before_validation()` |  | `None` | — |
| `test_raises_error_for_unknown_key()` |  | `None` | — |
| `test_error_message_contains_supported_keys()` |  | `None` | — |
| `test_no_op_when_env_file_does_not_exist()` |  | `None` | — |
| `test_no_op_when_key_not_in_file()` |  | `None` | — |
| `test_preserves_other_values()` |  | `None` | — |
| `test_all_supported_vars_can_be_unset()` | key | `None` | — |

## `TestParseProxyCommand`

**Source:** [`tests/core/test_proxy_setup.py#L242`](tests/core/test_proxy_setup.py#L242)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_parses_key_only()` |  | `None` | — |
| `test_parses_key_and_value()` |  | `None` | — |
| `test_uppercases_key()` |  | `None` | — |
| `test_preserves_value_case()` |  | `None` | — |
| `test_strips_leading_whitespace()` |  | `None` | — |
| `test_strips_trailing_whitespace()` |  | `None` | — |
| `test_splits_on_first_space_only()` |  | `None` | — |
| `test_raises_error_for_empty_string()` |  | `None` | — |
| `test_raises_error_for_whitespace_only()` |  | `None` | — |
| `test_handles_tab_as_separator()` |  | `None` | — |
| `test_handles_multiple_spaces_as_separator()` |  | `None` | — |

## `_write_env_file()`

```python
def _write_env_file(content: str) -> None
```

**Source:** [`tests/core/test_proxy_setup.py#L16`](tests/core/test_proxy_setup.py#L16)

