---
title: "tests.test_message_id"
tldr: "Module tests.test_message_id"
tags: [reference, api]
---

# `tests.test_message_id`

**Source:** [`tests/test_message_id.py`](tests/test_message_id.py) · 162 lines

## `TestLLMMessageId`

**Source:** [`tests/test_message_id.py#L15`](tests/test_message_id.py#L15)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_user_message_gets_message_id()` |  | `None` | — |
| `test_assistant_message_gets_message_id()` |  | `None` | — |
| `test_system_message_gets_message_id()` |  | `None` | — |
| `test_tool_message_does_not_get_message_id()` |  | `None` | — |
| `test_each_message_gets_unique_id()` |  | `None` | — |
| `test_message_id_preserved_from_dict()` |  | `None` | — |
| `test_message_id_preserved_for_tool_from_dict()` |  | `None` | — |
| `test_tool_message_no_id_from_dict_without_id()` |  | `None` | — |

## `TestLLMMessageAccumulation`

**Source:** [`tests/test_message_id.py#L68`](tests/test_message_id.py#L68)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_message_id_preserved_on_add()` |  | `None` | — |
| `test_message_id_preserved_after_multiple_adds()` |  | `None` | — |

## `TestEventMessageId`

**Source:** [`tests/test_message_id.py#L89`](tests/test_message_id.py#L89)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_user_message_event_has_message_id()` |  | `None` | — |
| `test_assistant_event_has_message_id()` |  | `None` | — |
| `test_assistant_event_message_id_optional()` |  | `None` | — |
| `test_reasoning_event_has_message_id()` |  | `None` | — |
| `test_reasoning_event_message_id_optional()` |  | `None` | — |
| `test_assistant_event_add_preserves_message_id()` |  | `None` | — |

## `TestMessageIdExcludedFromAPI`

**Source:** [`tests/test_message_id.py#L121`](tests/test_message_id.py#L121)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_message_id_excluded_with_exclude_param()` |  | `None` | — |
| `test_message_id_included_in_normal_dump()` |  | `None` | — |

## `TestMessageIdInLogs`

**Source:** [`tests/test_message_id.py#L138`](tests/test_message_id.py#L138)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_message_id_in_json_dump()` |  | `None` | — |
| `test_message_id_roundtrip()` |  | `None` | — |
| `test_tool_message_id_none_in_json()` |  | `None` | — |

