---
title: "tests.tools.test_ask_user_question"
tldr: "Module tests.tools.test_ask_user_question"
tags: [reference, api]
---

# `tests.tools.test_ask_user_question`

**Source:** [`tests/tools/test_ask_user_question.py`](tests/tools/test_ask_user_question.py) · 188 lines

## `TestToolUIDisplay`

**Source:** [`tests/tools/test_ask_user_question.py#L128`](tests/tools/test_ask_user_question.py#L128)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_get_call_display_single_question()` | single_question_args | `—` | — |
| `test_get_call_display_multiple_questions()` | multi_question_args | `—` | — |
| `test_get_result_display_success()` |  | `—` | — |
| `test_get_result_display_cancelled()` |  | `—` | — |
| `test_get_result_display_other()` |  | `—` | — |

## `tool()`

```python
def tool()
```

**Source:** [`tests/tools/test_ask_user_question.py#L19`](tests/tools/test_ask_user_question.py#L19)

## `single_question_args()`

```python
def single_question_args()
```

**Source:** [`tests/tools/test_ask_user_question.py#L25`](tests/tools/test_ask_user_question.py#L25)

## `multi_question_args()`

```python
def multi_question_args()
```

**Source:** [`tests/tools/test_ask_user_question.py#L41`](tests/tools/test_ask_user_question.py#L41)

## `run_tool_with_callback()`

```python
async def run_tool_with_callback(tool, args, callback)
```

**Source:** [`tests/tools/test_ask_user_question.py#L58`](tests/tools/test_ask_user_question.py#L58)

## `test_raises_error_without_callback()`

```python
async def test_raises_error_without_callback(tool, single_question_args)
```

**Source:** [`tests/tools/test_ask_user_question.py#L69`](tests/tools/test_ask_user_question.py#L69)

## `test_calls_callback_and_returns_result()`

```python
async def test_calls_callback_and_returns_result(tool, single_question_args)
```

**Source:** [`tests/tools/test_ask_user_question.py#L78`](tests/tools/test_ask_user_question.py#L78)

## `test_handles_cancelled_result()`

```python
async def test_handles_cancelled_result(tool, single_question_args)
```

**Source:** [`tests/tools/test_ask_user_question.py#L98`](tests/tools/test_ask_user_question.py#L98)

## `test_handles_other_response()`

```python
async def test_handles_other_response(tool, single_question_args)
```

**Source:** [`tests/tools/test_ask_user_question.py#L112`](tests/tools/test_ask_user_question.py#L112)

