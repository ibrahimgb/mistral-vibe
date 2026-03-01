---
title: "tests.test_middleware"
tldr: "Module tests.test_middleware"
tags: [reference, api]
---

# `tests.test_middleware`

**Source:** [`tests/test_middleware.py`](tests/test_middleware.py) · 606 lines

## Constants

- `REMINDER`
- `EXIT_MSG`
- `TARGET_AGENT`

## `TestReadOnlyAgentMiddleware`

**Source:** [`tests/test_middleware.py#L42`](tests/test_middleware.py#L42)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_injects_reminder_when_target_agent_active()` | ctx | `None` | — |
| 🔄 `test_does_not_inject_when_non_target_agent()` | ctx, agent_name | `None` | — |
| 🔄 `test_injects_reminder_only_once()` | ctx | `None` | — |
| 🔄 `test_injects_exit_message_when_leaving()` | ctx | `None` | — |
| 🔄 `test_reinjects_reminder_on_reentry()` | ctx | `None` | — |
| 🔄 `test_custom_reminder()` | ctx | `None` | — |
| 🔄 `test_custom_exit_message()` | ctx | `None` | — |
| 🔄 `test_reset_clears_state()` | ctx | `None` | — |
| 🔄 `test_exit_message_fires_only_once()` | ctx | `None` | — |
| 🔄 `test_multiple_turns_after_entry()` | ctx | `None` | — |
| 🔄 `test_multiple_turns_after_exit()` | ctx | `None` | — |
| 🔄 `test_rapid_toggling_multiple_cycles()` | ctx | `None` | — |
| 🔄 `test_exit_to_non_default_agent()` | ctx | `None` | — |
| 🔄 `test_switching_between_non_target_agents()` | ctx | `None` | — |
| 🔄 `test_non_target_to_target_entry()` | ctx | `None` | Starting in a non-target agent then entering target should inject reminder. |
| 🔄 `test_reset_while_inactive_after_exit()` | ctx | `None` | — |
| 🔄 `test_reset_while_inactive_then_reenter()` | ctx | `None` | — |
| 🔄 `test_reset_with_compact_reason()` | ctx | `None` | — |
| 🔄 `test_entry_then_continuation_then_exit_then_continuation()` | ctx | `None` | Each call sees one transition at a time. |

## `TestMiddlewarePipelineWithReadOnlyAgent`

**Source:** [`tests/test_middleware.py#L329`](tests/test_middleware.py#L329)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_pipeline_includes_injection()` | ctx | `None` | — |
| 🔄 `test_pipeline_skips_injection_when_not_target_agent()` | ctx | `None` | — |
| 🔄 `test_direct_plan_to_chat_transition_delivers_both_messages()` | ctx | `None` | — |

## `TestReadOnlyAgentMiddlewareIntegration`

**Source:** [`tests/test_middleware.py#L414`](tests/test_middleware.py#L414)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_switch_agent_preserves_middleware_state_for_exit_message()` |  | `None` | — |
| 🔄 `test_switch_agent_allows_reinjection_on_reentry()` |  | `None` | — |
| 🔄 `test_switch_plan_to_auto_approve_fires_exit()` |  | `None` | — |
| 🔄 `test_switch_between_non_plan_agents_no_injection()` |  | `None` | — |
| 🔄 `test_full_lifecycle_plan_default_plan_default()` |  | `None` | Integration test for a full plan -> default -> plan -> default cycle. |

## `_build_middleware()`

```python
def _build_middleware(profile_getter, agent_name: str, reminder: str, exit_message: str) -> ReadOnlyAgentMiddleware
```

**Source:** [`tests/test_middleware.py#L26`](tests/test_middleware.py#L26)

## `ctx()`

```python
def ctx(vibe_config: VibeConfig) -> ConversationContext
```

**Source:** [`tests/test_middleware.py#L36`](tests/test_middleware.py#L36)

## `_find_plan_middleware()`

```python
def _find_plan_middleware(agent) -> ReadOnlyAgentMiddleware
```

**Source:** [`tests/test_middleware.py#L405`](tests/test_middleware.py#L405)

