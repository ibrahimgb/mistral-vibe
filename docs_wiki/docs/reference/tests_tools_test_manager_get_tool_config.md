---
title: "tests.tools.test_manager_get_tool_config"
tldr: "Module tests.tools.test_manager_get_tool_config"
tags: [reference, api]
---

# `tests.tools.test_manager_get_tool_config`

**Source:** [`tests/tools/test_manager_get_tool_config.py`](tests/tools/test_manager_get_tool_config.py) · 478 lines

## `TestToolManagerFiltering`

**Source:** [`tests/tools/test_manager_get_tool_config.py#L74`](tests/tools/test_manager_get_tool_config.py#L74)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_enabled_tools_filters_to_only_enabled()` |  | `—` | — |
| `test_disabled_tools_excludes_disabled()` |  | `—` | — |
| `test_enabled_tools_takes_precedence_over_disabled()` |  | `—` | — |
| `test_glob_pattern_matching()` |  | `—` | — |
| `test_regex_pattern_matching()` |  | `—` | — |
| `test_case_insensitive_matching()` |  | `—` | — |
| `test_empty_enabled_tools_returns_all()` |  | `—` | — |
| `test_tool_paths_with_file_and_directory()` | tmp_path | `—` | Should handle a mix of file and directory paths in tool_paths. |

## `TestToolRuntimeAvailability`

Tests for is_available() filtering in ToolManager.

**Source:** [`tests/tools/test_manager_get_tool_config.py#L230`](tests/tools/test_manager_get_tool_config.py#L230)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_unavailable_tool_excluded_from_available_tools()` | tmp_path, monkeypatch | `—` | Tools where is_available() returns False should be excluded. |
| `test_default_is_available_returns_true()` |  | `—` | Tools without is_available() override should be available. |

## `TestToolManagerModuleReuse`

Tests for module reuse across ToolManager instances.

When multiple ToolManager instances are created (e.g., main agent + subagent),
they should reuse the same tool modules from sys.modules to preserve class identity.
This prevents Pydantic validation errors when tool results from one agent
are validated against types from another.

**Source:** [`tests/tools/test_manager_get_tool_config.py#L294`](tests/tools/test_manager_get_tool_config.py#L294)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_multiple_managers_share_tool_classes()` |  | `—` | Tool classes should be identical across multiple ToolManager instances. |
| `test_tool_state_classes_are_identical()` |  | `—` | Tool state classes should be identical across managers. |
| `test_tool_args_results_classes_are_identical()` |  | `—` | Tool args and result classes should be identical across managers. |
| `test_tool_instances_are_isolated()` |  | `—` | Tool instances should be separate even though classes are shared. |
| `test_class_shared_but_instances_isolated()` |  | `—` | Classes must be shared (for validation) but instances isolated (for state). |
| `test_different_files_same_stem_get_different_modules()` | tmp_path | `—` | Tools with same stem but different paths should be separate modules. |

## `config()`

```python
def config()
```

**Source:** [`tests/tools/test_manager_get_tool_config.py#L13`](tests/tools/test_manager_get_tool_config.py#L13)

## `tool_manager()`

```python
def tool_manager(config)
```

**Source:** [`tests/tools/test_manager_get_tool_config.py#L20`](tests/tools/test_manager_get_tool_config.py#L20)

## `test_returns_default_config_when_no_overrides()`

```python
def test_returns_default_config_when_no_overrides(tool_manager)
```

**Source:** [`tests/tools/test_manager_get_tool_config.py#L24`](tests/tools/test_manager_get_tool_config.py#L24)

## `test_merges_user_overrides_with_defaults()`

```python
def test_merges_user_overrides_with_defaults()
```

**Source:** [`tests/tools/test_manager_get_tool_config.py#L35`](tests/tools/test_manager_get_tool_config.py#L35)

## `test_preserves_tool_specific_fields_from_overrides()`

```python
def test_preserves_tool_specific_fields_from_overrides()
```

**Source:** [`tests/tools/test_manager_get_tool_config.py#L52`](tests/tools/test_manager_get_tool_config.py#L52)

## `test_falls_back_to_base_config_for_unknown_tool()`

```python
def test_falls_back_to_base_config_for_unknown_tool(tool_manager)
```

**Source:** [`tests/tools/test_manager_get_tool_config.py#L67`](tests/tools/test_manager_get_tool_config.py#L67)

