---
title: "tests.test_agents"
tldr: "Module tests.test_agents"
tags: [reference, api]
---

# `tests.test_agents`

**Source:** [`tests/test_agents.py`](tests/test_agents.py) · 619 lines

## `TestDeepMerge`

**Source:** [`tests/test_agents.py#L35`](tests/test_agents.py#L35)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_simple_merge()` |  | `None` | — |
| `test_override_existing_key()` |  | `None` | — |
| `test_nested_dict_merge()` |  | `None` | — |
| `test_deeply_nested_merge()` |  | `None` | — |
| `test_override_dict_with_non_dict()` |  | `None` | — |
| `test_override_non_dict_with_dict()` |  | `None` | — |
| `test_preserves_original_base()` |  | `None` | — |
| `test_empty_override()` |  | `None` | — |
| `test_empty_base()` |  | `None` | — |
| `test_lists_are_overridden_not_merged()` |  | `None` | Lists should be replaced entirely, not merged element-by-element. |
| `test_nested_lists_are_overridden_not_merged()` |  | `None` | Nested lists in dicts should also be replaced, not merged. |

## `TestAgentSafety`

**Source:** [`tests/test_agents.py#L105`](tests/test_agents.py#L105)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_safety_enum_values()` |  | `None` | — |
| `test_default_agent_is_neutral()` |  | `None` | — |
| `test_auto_approve_agent_is_yolo()` |  | `None` | — |
| `test_plan_agent_is_safe()` |  | `None` | — |
| `test_accept_edits_agent_is_destructive()` |  | `None` | — |

## `TestAgentProfile`

**Source:** [`tests/test_agents.py#L128`](tests/test_agents.py#L128)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_all_builtin_agents_have_valid_names()` |  | `None` | — |
| `test_display_name_property()` |  | `None` | — |
| `test_description_property()` |  | `None` | — |
| `test_explore_is_subagent()` |  | `None` | — |
| `test_agents()` |  | `None` | — |

## `TestAgentApplyToConfig`

**Source:** [`tests/test_agents.py#L172`](tests/test_agents.py#L172)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_custom_prompt_found_in_global_when_missing_from_project()` | tmp_path, monkeypatch | `None` | Regression test for https://github.com/mistralai/mistral-vibe/issues/288 |

## `TestAgentProfileOverrides`

**Source:** [`tests/test_agents.py#L209`](tests/test_agents.py#L209)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_default_agent_has_no_overrides()` |  | `None` | — |
| `test_auto_approve_agent_sets_auto_approve()` |  | `None` | — |
| `test_plan_agent_restricts_tools()` |  | `None` | — |
| `test_accept_edits_agent_sets_tool_permissions()` |  | `None` | — |

## `TestAgentManagerCycling`

**Source:** [`tests/test_agents.py#L232`](tests/test_agents.py#L232)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `base_config()` |  | `VibeConfig` | — |
| `backend()` |  | `FakeBackend` | — |
| `test_get_agent_order_includes_primary_agents()` | base_config, backend | `None` | — |
| `test_next_agent_cycles_through_all()` | base_config, backend | `None` | — |
| `test_next_agent_wraps_around()` | base_config, backend | `None` | — |

## `TestAgentProfileConfig`

**Source:** [`tests/test_agents.py#L289`](tests/test_agents.py#L289)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_agent_profile_frozen()` |  | `None` | — |

## `TestAgentSwitchAgent`

**Source:** [`tests/test_agents.py#L301`](tests/test_agents.py#L301)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `base_config()` |  | `VibeConfig` | — |
| `backend()` |  | `FakeBackend` | — |
| 🔄 `test_switch_to_plan_agent_restricts_tools()` | base_config, backend | `None` | — |
| 🔄 `test_switch_from_plan_to_default_restores_tools()` | base_config, backend | `None` | — |
| 🔄 `test_switch_agent_preserves_conversation_history()` | base_config, backend | `None` | — |
| 🔄 `test_switch_to_same_agent_is_noop()` | base_config, backend | `None` | — |

## `TestAcceptEditsAgent`

**Source:** [`tests/test_agents.py#L382`](tests/test_agents.py#L382)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_accept_edits_config_sets_write_file_always()` |  | `None` | — |
| `test_accept_edits_config_sets_search_replace_always()` |  | `None` | — |
| 🔄 `test_accept_edits_agent_auto_approves_write_file()` |  | `None` | — |
| 🔄 `test_accept_edits_agent_requires_approval_for_other_tools()` |  | `None` | — |

## `TestPlanAgentToolRestriction`

**Source:** [`tests/test_agents.py#L420`](tests/test_agents.py#L420)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_plan_agent_only_exposes_read_tools_to_llm()` |  | `None` | — |
| 🔄 `test_plan_agent_rejects_non_plan_tool_call()` |  | `None` | — |

## `TestAgentManagerFiltering`

**Source:** [`tests/test_agents.py#L470`](tests/test_agents.py#L470)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_enabled_agents_filters_to_only_enabled()` |  | `None` | — |
| `test_disabled_agents_excludes_disabled()` |  | `None` | — |
| `test_enabled_agents_takes_precedence_over_disabled()` |  | `None` | — |
| `test_glob_pattern_matching()` |  | `None` | — |
| `test_regex_pattern_matching()` |  | `None` | — |
| `test_empty_enabled_agents_returns_all()` |  | `None` | — |
| `test_get_subagents_respects_filtering()` |  | `None` | — |

## `TestAgentLoopInitialization`

**Source:** [`tests/test_agents.py#L568`](tests/test_agents.py#L568)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_agent_system_prompt_id_is_applied_on_init()` | tmp_path, monkeypatch | `None` | — |

