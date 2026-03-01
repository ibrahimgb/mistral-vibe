---
title: "tests.skills.test_models"
tldr: "Module tests.skills.test_models"
tags: [reference, api]
---

# `tests.skills.test_models`

**Source:** [`tests/skills/test_models.py`](tests/skills/test_models.py) · 195 lines

## `TestSkillMetadata`

**Source:** [`tests/skills/test_models.py#L11`](tests/skills/test_models.py#L11)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_creates_with_required_fields()` |  | `None` | — |
| `test_creates_with_all_fields()` |  | `None` | — |
| `test_raises_error_for_uppercase_name()` |  | `None` | — |
| `test_raises_error_for_invalid_chars_in_name()` |  | `None` | — |
| `test_raises_error_for_consecutive_hyphens()` |  | `None` | — |
| `test_raises_error_for_leading_trailing_hyphens()` |  | `None` | — |
| `test_parses_allowed_tools_from_space_delimited_string()` |  | `None` | — |
| `test_parses_allowed_tools_from_list()` |  | `None` | — |
| `test_parses_allowed_tools_handles_none()` |  | `None` | — |
| `test_normalizes_metadata_values_to_strings()` |  | `None` | — |
| `test_raises_error_for_missing_name()` |  | `None` | — |
| `test_raises_error_for_missing_description()` |  | `None` | — |
| `test_raises_error_for_empty_name()` |  | `None` | — |
| `test_raises_error_for_empty_description()` |  | `None` | — |

## `TestSkillInfo`

**Source:** [`tests/skills/test_models.py#L121`](tests/skills/test_models.py#L121)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_creates_from_metadata()` | tmp_path | `None` | — |
| `test_creates_with_all_fields()` | tmp_path | `None` | — |
| `test_from_metadata_resolves_paths()` | tmp_path | `None` | — |
| `test_inherits_all_metadata_fields()` | tmp_path | `None` | — |

