---
title: "tests.core.test_trusted_folders"
tldr: "Module tests.core.test_trusted_folders"
tags: [reference, api]
---

# `tests.core.test_trusted_folders`

**Source:** [`tests/core/test_trusted_folders.py`](tests/core/test_trusted_folders.py) · 269 lines

## `TestTrustedFoldersManager`

**Source:** [`tests/core/test_trusted_folders.py#L19`](tests/core/test_trusted_folders.py#L19)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_initializes_with_empty_lists_when_file_does_not_exist()` | tmp_path | `None` | — |
| `test_loads_existing_file()` | tmp_path | `None` | — |
| `test_handles_corrupted_file()` | tmp_path | `None` | — |
| `test_normalizes_paths_to_absolute()` | tmp_working_directory, monkeypatch | `None` | — |
| `test_expands_user_home_in_paths()` | tmp_path, monkeypatch | `None` | — |
| `test_is_trusted_returns_true_for_trusted_path()` | tmp_path | `None` | — |
| `test_is_trusted_returns_false_for_untrusted_path()` | tmp_path | `None` | — |
| `test_is_trusted_returns_none_for_unknown_path()` | tmp_path | `None` | — |
| `test_add_trusted_adds_path_to_trusted_list()` | tmp_path | `None` | — |
| `test_add_trusted_removes_path_from_untrusted()` | tmp_path | `None` | — |
| `test_add_trusted_idempotent()` | tmp_path | `None` | — |
| `test_add_untrusted_adds_path_to_untrusted_list()` | tmp_path | `None` | — |
| `test_add_untrusted_removes_path_from_trusted()` | tmp_path | `None` | — |
| `test_add_untrusted_idempotent()` | tmp_path | `None` | — |
| `test_persistence_across_instances()` | tmp_path | `None` | — |
| `test_handles_multiple_paths()` | tmp_path | `None` | — |
| `test_handles_switching_between_trusted_and_untrusted()` | tmp_path | `None` | — |
| `test_handles_missing_file_during_save()` | tmp_path | `None` | — |

## `TestHasAgentsMdFile`

**Source:** [`tests/core/test_trusted_folders.py#L213`](tests/core/test_trusted_folders.py#L213)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_false_for_empty_directory()` | tmp_path | `None` | — |
| `test_returns_true_when_agents_md_exists()` | tmp_path | `None` | — |
| `test_returns_true_when_vibe_md_exists()` | tmp_path | `None` | — |
| `test_returns_true_when_dot_vibe_md_exists()` | tmp_path | `None` | — |
| `test_returns_false_when_only_other_files_exist()` | tmp_path | `None` | — |
| `test_agents_md_filenames_constant()` |  | `None` | — |

## `TestHasTrustableContent`

**Source:** [`tests/core/test_trusted_folders.py#L238`](tests/core/test_trusted_folders.py#L238)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_true_when_vibe_dir_exists()` | tmp_path | `None` | — |
| `test_returns_true_when_agents_dir_exists()` | tmp_path | `None` | — |
| `test_returns_true_when_agents_md_filename_exists()` | tmp_path | `None` | — |
| `test_returns_false_when_no_trustable_content()` | tmp_path | `None` | — |
| `test_returns_true_when_vibe_config_in_subfolder()` | tmp_path | `None` | — |
| `test_returns_true_when_agents_skills_in_subfolder()` | tmp_path | `None` | — |
| `test_returns_false_when_config_only_inside_ignored_dir()` | tmp_path | `None` | — |

