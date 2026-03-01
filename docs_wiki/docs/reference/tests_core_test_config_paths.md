---
title: "tests.core.test_config_paths"
tldr: "Module tests.core.test_config_paths"
tags: [reference, api]
---

# `tests.core.test_config_paths`

**Source:** [`tests/core/test_config_paths.py`](tests/core/test_config_paths.py) · 184 lines

## `TestDiscoverLocalSkillsDirs`

**Source:** [`tests/core/test_config_paths.py#L13`](tests/core/test_config_paths.py#L13)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_empty_list_when_dir_not_trusted()` | tmp_path | `None` | — |
| `test_returns_empty_list_when_trusted_but_no_skills_dirs()` | tmp_path | `None` | — |
| `test_returns_vibe_skills_only_when_only_it_exists()` | tmp_path | `None` | — |
| `test_returns_agents_skills_only_when_only_it_exists()` | tmp_path | `None` | — |
| `test_returns_both_in_order_when_both_exist()` | tmp_path | `None` | — |
| `test_ignores_vibe_skills_when_file_not_dir()` | tmp_path | `None` | — |
| `test_finds_skills_dirs_recursively_in_trusted_folder()` | tmp_path | `None` | — |
| `test_does_not_descend_into_ignored_dirs()` | tmp_path | `None` | — |

## `TestDiscoverLocalToolsDirs`

**Source:** [`tests/core/test_config_paths.py#L87`](tests/core/test_config_paths.py#L87)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_empty_list_when_dir_not_trusted()` | tmp_path | `None` | — |
| `test_returns_empty_list_when_trusted_but_no_tools_dir()` | tmp_path | `None` | — |
| `test_returns_tools_dir_when_exists()` | tmp_path | `None` | — |
| `test_ignores_tools_when_file_not_dir()` | tmp_path | `None` | — |
| `test_finds_tools_dirs_recursively()` | tmp_path | `None` | — |
| `test_does_not_descend_into_ignored_dirs()` | tmp_path | `None` | — |

## `TestDiscoverLocalAgentsDirs`

**Source:** [`tests/core/test_config_paths.py#L137`](tests/core/test_config_paths.py#L137)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_empty_list_when_dir_not_trusted()` | tmp_path | `None` | — |
| `test_returns_empty_list_when_trusted_but_no_agents_dir()` | tmp_path | `None` | — |
| `test_returns_agents_dir_when_exists()` | tmp_path | `None` | — |
| `test_ignores_agents_when_file_not_dir()` | tmp_path | `None` | — |
| `test_finds_agents_dirs_recursively()` | tmp_path | `None` | — |
| `test_does_not_descend_into_ignored_dirs()` | tmp_path | `None` | — |

