---
title: "tests.tools.test_websearch"
tldr: "Module tests.tools.test_websearch"
tags: [reference, api]
---

# `tests.tools.test_websearch`

**Source:** [`tests/tools/test_websearch.py`](tests/tools/test_websearch.py) · 165 lines

## `_make_response()`

```python
def _make_response(content: list | None, outputs: list | None) -> mistralai.ConversationResponse
```

**Source:** [`tests/tools/test_websearch.py#L13`](tests/tools/test_websearch.py#L13)

## `websearch()`

```python
def websearch(monkeypatch)
```

**Source:** [`tests/tools/test_websearch.py#L28`](tests/tools/test_websearch.py#L28)

## `test_parse_text_chunks()`

```python
def test_parse_text_chunks(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L34`](tests/tools/test_websearch.py#L34)

## `test_parse_sources_deduped()`

```python
def test_parse_sources_deduped(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L43`](tests/tools/test_websearch.py#L43)

## `test_parse_skips_source_without_url()`

```python
def test_parse_skips_source_without_url(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L66`](tests/tools/test_websearch.py#L66)

## `test_parse_empty_text_raises()`

```python
def test_parse_empty_text_raises(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L77`](tests/tools/test_websearch.py#L77)

## `test_parse_whitespace_only_raises()`

```python
def test_parse_whitespace_only_raises(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L83`](tests/tools/test_websearch.py#L83)

## `test_parse_skips_non_message_entries()`

```python
def test_parse_skips_non_message_entries(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L89`](tests/tools/test_websearch.py#L89)

## `test_run_missing_api_key()`

```python
async def test_run_missing_api_key(monkeypatch)
```

**Source:** [`tests/tools/test_websearch.py#L100`](tests/tools/test_websearch.py#L100)

## `test_run_returns_parsed_result()`

```python
async def test_run_returns_parsed_result(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L109`](tests/tools/test_websearch.py#L109)

## `test_run_sdk_error_wrapped()`

```python
async def test_run_sdk_error_wrapped(websearch)
```

**Source:** [`tests/tools/test_websearch.py#L134`](tests/tools/test_websearch.py#L134)

## `test_is_available_with_key()`

```python
def test_is_available_with_key(monkeypatch)
```

**Source:** [`tests/tools/test_websearch.py#L154`](tests/tools/test_websearch.py#L154)

## `test_is_available_without_key()`

```python
def test_is_available_without_key(monkeypatch)
```

**Source:** [`tests/tools/test_websearch.py#L159`](tests/tools/test_websearch.py#L159)

## `test_get_status_text()`

```python
def test_get_status_text()
```

**Source:** [`tests/tools/test_websearch.py#L164`](tests/tools/test_websearch.py#L164)

