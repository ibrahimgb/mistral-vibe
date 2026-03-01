---
title: "tests.tools.test_grep"
tldr: "Module tests.tools.test_grep"
tags: [reference, api]
---

# `tests.tools.test_grep`

**Source:** [`tests/tools/test_grep.py`](tests/tools/test_grep.py) · 341 lines

## `TestGnuGrepBackend`

**Source:** [`tests/tools/test_grep.py#L202`](tests/tools/test_grep.py#L202)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_finds_pattern_in_file()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_finds_multiple_matches()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_returns_empty_on_no_matches()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_case_insensitive_for_lowercase_pattern()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_case_sensitive_for_mixed_case_pattern()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_respects_exclude_patterns()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_searches_in_specific_path()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_respects_vibeignore_file()` | grep_gnu_only, tmp_path | `—` | — |
| 🔄 `test_truncates_to_max_matches()` | grep_gnu_only, tmp_path | `—` | — |

## `TestRipgrepBackend`

**Source:** [`tests/tools/test_grep.py#L305`](tests/tools/test_grep.py#L305)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_smart_case_lowercase_pattern()` | grep, tmp_path | `—` | — |
| 🔄 `test_smart_case_mixed_case_pattern()` | grep, tmp_path | `—` | — |
| 🔄 `test_searches_ignored_files_when_use_default_ignore_false()` | grep, tmp_path | `—` | — |

## `grep()`

```python
def grep(tmp_path, monkeypatch)
```

**Source:** [`tests/tools/test_grep.py#L13`](tests/tools/test_grep.py#L13)

## `grep_gnu_only()`

```python
def grep_gnu_only(tmp_path, monkeypatch)
```

**Source:** [`tests/tools/test_grep.py#L20`](tests/tools/test_grep.py#L20)

## `test_detects_ripgrep_when_available()`

```python
def test_detects_ripgrep_when_available(grep)
```

**Source:** [`tests/tools/test_grep.py#L34`](tests/tools/test_grep.py#L34)

## `test_falls_back_to_gnu_grep()`

```python
def test_falls_back_to_gnu_grep(grep, monkeypatch)
```

**Source:** [`tests/tools/test_grep.py#L39`](tests/tools/test_grep.py#L39)

## `test_raises_error_if_no_grep_available()`

```python
def test_raises_error_if_no_grep_available(grep, monkeypatch)
```

**Source:** [`tests/tools/test_grep.py#L53`](tests/tools/test_grep.py#L53)

## `test_finds_pattern_in_file()`

```python
async def test_finds_pattern_in_file(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L63`](tests/tools/test_grep.py#L63)

## `test_finds_multiple_matches()`

```python
async def test_finds_multiple_matches(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L75`](tests/tools/test_grep.py#L75)

## `test_returns_empty_on_no_matches()`

```python
async def test_returns_empty_on_no_matches(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L86`](tests/tools/test_grep.py#L86)

## `test_fails_with_empty_pattern()`

```python
async def test_fails_with_empty_pattern(grep)
```

**Source:** [`tests/tools/test_grep.py#L97`](tests/tools/test_grep.py#L97)

## `test_fails_with_nonexistent_path()`

```python
async def test_fails_with_nonexistent_path(grep)
```

**Source:** [`tests/tools/test_grep.py#L105`](tests/tools/test_grep.py#L105)

## `test_searches_in_specific_path()`

```python
async def test_searches_in_specific_path(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L113`](tests/tools/test_grep.py#L113)

## `test_truncates_to_max_matches()`

```python
async def test_truncates_to_max_matches(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L127`](tests/tools/test_grep.py#L127)

## `test_truncates_to_max_output_bytes()`

```python
async def test_truncates_to_max_output_bytes(grep, tmp_path, monkeypatch)
```

**Source:** [`tests/tools/test_grep.py#L137`](tests/tools/test_grep.py#L137)

## `test_respects_default_ignore_patterns()`

```python
async def test_respects_default_ignore_patterns(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L150`](tests/tools/test_grep.py#L150)

## `test_respects_vibeignore_file()`

```python
async def test_respects_vibeignore_file(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L163`](tests/tools/test_grep.py#L163)

## `test_ignores_comments_in_vibeignore()`

```python
async def test_ignores_comments_in_vibeignore(grep, tmp_path)
```

**Source:** [`tests/tools/test_grep.py#L179`](tests/tools/test_grep.py#L179)

## `test_uses_effective_workdir()`

```python
async def test_uses_effective_workdir(tmp_path, monkeypatch)
```

**Source:** [`tests/tools/test_grep.py#L189`](tests/tools/test_grep.py#L189)

