---
title: "tests.test_agent_stats"
tldr: "Module tests.test_agent_stats"
tags: [reference, api]
---

# `tests.test_agent_stats`

**Source:** [`tests/test_agent_stats.py`](tests/test_agent_stats.py) · 748 lines

## `TestAgentStatsHelpers`

**Source:** [`tests/test_agent_stats.py#L106`](tests/test_agent_stats.py#L106)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_update_pricing()` |  | `None` | — |
| `test_reset_context_state_preserves_cumulative()` |  | `None` | — |
| `test_session_cost_computed_from_current_pricing()` |  | `None` | — |

## `TestReloadPreservesStats`

**Source:** [`tests/test_agent_stats.py#L160`](tests/test_agent_stats.py#L160)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_reload_preserves_session_tokens()` |  | `None` | — |
| 🔄 `test_reload_preserves_tool_call_stats()` |  | `None` | — |
| 🔄 `test_reload_preserves_steps()` |  | `None` | — |
| 🔄 `test_reload_preserves_context_tokens_when_messages_preserved()` |  | `None` | — |
| 🔄 `test_reload_resets_context_tokens_when_no_messages()` |  | `None` | — |
| 🔄 `test_reload_resets_context_tokens_when_system_prompt_changes()` |  | `None` | — |
| 🔄 `test_reload_updates_pricing_from_new_model()` | monkeypatch | `None` | — |
| 🔄 `test_reload_accumulates_tokens_across_configs()` | monkeypatch | `None` | — |

## `TestReloadPreservesMessages`

**Source:** [`tests/test_agent_stats.py#L328`](tests/test_agent_stats.py#L328)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_reload_preserves_conversation_messages()` |  | `None` | — |
| 🔄 `test_reload_updates_system_prompt_preserves_rest()` |  | `None` | — |
| 🔄 `test_reload_with_no_messages_stays_empty()` |  | `None` | — |
| 🔄 `test_reload_does_not_reemit_to_observer()` | observer_capture | `None` | — |

## `TestCompactStatsHandling`

**Source:** [`tests/test_agent_stats.py#L398`](tests/test_agent_stats.py#L398)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_compact_preserves_cumulative_stats()` |  | `None` | — |
| 🔄 `test_compact_updates_context_tokens()` |  | `None` | — |
| 🔄 `test_compact_preserves_tool_call_stats()` |  | `None` | — |
| 🔄 `test_compact_resets_session_id()` |  | `None` | — |

## `TestAutoCompactIntegration`

**Source:** [`tests/test_agent_stats.py#L496`](tests/test_agent_stats.py#L496)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_auto_compact_triggers_and_preserves_stats()` |  | `None` | — |

## `TestClearHistoryFullReset`

**Source:** [`tests/test_agent_stats.py#L537`](tests/test_agent_stats.py#L537)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_clear_history_preserves_listeners()` |  | `None` | — |
| 🔄 `test_clear_history_fully_resets_stats()` |  | `None` | — |
| 🔄 `test_clear_history_preserves_pricing()` |  | `None` | — |
| 🔄 `test_clear_history_removes_messages()` |  | `None` | — |
| 🔄 `test_clear_history_resets_session_id()` |  | `None` | — |

## `TestClearHistoryObserverBugfix`

**Source:** [`tests/test_agent_stats.py#L626`](tests/test_agent_stats.py#L626)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_clear_history_observer_sees_new_messages()` | observer_capture | `None` | Bug fix: clear_history previously left a stale index, so new messages |

## `TestStatsEdgeCases`

**Source:** [`tests/test_agent_stats.py#L657`](tests/test_agent_stats.py#L657)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_session_cost_approximation_on_model_change()` | monkeypatch | `None` | — |
| 🔄 `test_multiple_reloads_accumulate_correctly()` |  | `None` | — |
| 🔄 `test_compact_then_reload_preserves_both()` |  | `None` | — |
| 🔄 `test_reload_without_config_preserves_current()` |  | `None` | — |
| 🔄 `test_reload_with_new_config_updates_it()` |  | `None` | — |

## `make_config()`

```python
def make_config() -> VibeConfig
```

**Source:** [`tests/test_agent_stats.py#L32`](tests/test_agent_stats.py#L32)

## `observer_capture()`

```python
def observer_capture() -> tuple[list[LLMMessage], Callable[[LLMMessage], None]]
```

**Source:** [`tests/test_agent_stats.py#L97`](tests/test_agent_stats.py#L97)

