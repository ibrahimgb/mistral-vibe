---
title: "tests.skills.test_manager"
tldr: "Module tests.skills.test_manager"
tags: [reference, api]
---

# `tests.skills.test_manager`

**Source:** [`tests/skills/test_manager.py`](tests/skills/test_manager.py) · 520 lines

## `TestSkillManagerDiscovery`

**Source:** [`tests/skills/test_manager.py#L26`](tests/skills/test_manager.py#L26)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_discovers_no_skills_when_directory_empty()` | skill_manager | `None` | — |
| `test_discovers_skill_from_skill_paths()` | skills_dir | `None` | — |
| `test_discovers_multiple_skills()` | skills_dir | `None` | — |
| `test_ignores_directories_without_skill_md()` | skills_dir | `None` | — |
| `test_ignores_files_in_skills_directory()` | skills_dir | `None` | — |

## `TestSkillManagerParsing`

**Source:** [`tests/skills/test_manager.py#L102`](tests/skills/test_manager.py#L102)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_parses_all_skill_fields()` | skills_dir | `None` | — |
| `test_sets_correct_skill_path()` | skills_dir | `None` | — |
| `test_skips_skill_with_invalid_frontmatter()` | skills_dir | `None` | — |
| `test_skips_skill_with_missing_required_fields()` | skills_dir | `None` | — |

## `TestSkillManagerSearchPaths`

**Source:** [`tests/skills/test_manager.py#L187`](tests/skills/test_manager.py#L187)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_discovers_from_vibe_skills_when_cwd_trusted()` | tmp_working_directory | `None` | — |
| `test_discovers_from_agents_skills_when_cwd_trusted()` | tmp_working_directory | `None` | — |
| `test_discovers_from_both_vibe_and_agents_skills_when_cwd_trusted()` | tmp_working_directory | `None` | — |
| `test_first_discovered_wins_when_same_skill_in_vibe_and_agents()` | tmp_working_directory | `None` | — |
| `test_discovers_from_multiple_skill_paths()` | tmp_path | `None` | — |
| `test_first_discovered_wins_for_duplicates()` | tmp_path | `None` | — |
| `test_ignores_nonexistent_skill_paths()` | tmp_path | `None` | — |

## `TestSkillManagerGetSkill`

**Source:** [`tests/skills/test_manager.py#L326`](tests/skills/test_manager.py#L326)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_skill_by_name()` | skills_dir | `None` | — |
| `test_returns_none_for_unknown_skill()` | skill_manager | `None` | — |

## `TestSkillManagerFiltering`

**Source:** [`tests/skills/test_manager.py#L345`](tests/skills/test_manager.py#L345)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_enabled_skills_filters_to_only_enabled()` | skills_dir | `None` | — |
| `test_disabled_skills_excludes_disabled()` | skills_dir | `None` | — |
| `test_enabled_skills_takes_precedence_over_disabled()` | skills_dir | `None` | — |
| `test_glob_pattern_matching()` | skills_dir | `None` | — |
| `test_regex_pattern_matching()` | skills_dir | `None` | — |
| `test_get_skill_respects_filtering()` | skills_dir | `None` | — |

## `TestSkillUserInvocable`

**Source:** [`tests/skills/test_manager.py#L457`](tests/skills/test_manager.py#L457)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_user_invocable_defaults_to_true()` | skills_dir | `None` | — |
| `test_user_invocable_can_be_set_to_false()` | skills_dir | `None` | — |
| `test_user_invocable_can_be_explicitly_set_to_true()` | skills_dir | `None` | — |
| `test_mixed_user_invocable_skills()` | skills_dir | `None` | — |

## `config()`

```python
def config() -> VibeConfig
```

**Source:** [`tests/skills/test_manager.py#L15`](tests/skills/test_manager.py#L15)

## `skill_manager()`

```python
def skill_manager(config: VibeConfig) -> SkillManager
```

**Source:** [`tests/skills/test_manager.py#L22`](tests/skills/test_manager.py#L22)

