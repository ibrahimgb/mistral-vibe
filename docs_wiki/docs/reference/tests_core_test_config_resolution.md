---
title: "tests.core.test_config_resolution"
tldr: "Module tests.core.test_config_resolution"
tags: [reference, api]
---

# `tests.core.test_config_resolution`

**Source:** [`tests/core/test_config_resolution.py`](tests/core/test_config_resolution.py) · 53 lines

## `TestResolveConfigFile`

**Source:** [`tests/core/test_config_resolution.py#L12`](tests/core/test_config_resolution.py#L12)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_resolves_local_config_when_exists_and_folder_is_trusted()` | tmp_path, monkeypatch | `None` | — |
| `test_resolves_local_config_when_exists_and_folder_is_not_trusted()` | tmp_path, monkeypatch | `None` | — |
| `test_falls_back_to_global_config_when_local_missing()` | tmp_path, monkeypatch | `None` | — |
| `test_respects_vibe_home_env_var()` | tmp_path, monkeypatch | `None` | — |

