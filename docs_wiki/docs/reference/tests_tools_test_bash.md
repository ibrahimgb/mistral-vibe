---
title: "tests.tools.test_bash"
tldr: "Module tests.tools.test_bash"
tags: [reference, api]
---

# `tests.tools.test_bash`

**Source:** [`tests/tools/test_bash.py`](tests/tools/test_bash.py) · 91 lines

## `bash()`

```python
def bash(tmp_path, monkeypatch)
```

**Source:** [`tests/tools/test_bash.py#L11`](tests/tools/test_bash.py#L11)

## `test_runs_echo_successfully()`

```python
async def test_runs_echo_successfully(bash)
```

**Source:** [`tests/tools/test_bash.py#L18`](tests/tools/test_bash.py#L18)

## `test_fails_cat_command_with_missing_file()`

```python
async def test_fails_cat_command_with_missing_file(bash)
```

**Source:** [`tests/tools/test_bash.py#L27`](tests/tools/test_bash.py#L27)

## `test_uses_effective_workdir()`

```python
async def test_uses_effective_workdir(tmp_path, monkeypatch)
```

**Source:** [`tests/tools/test_bash.py#L38`](tests/tools/test_bash.py#L38)

## `test_handles_timeout()`

```python
async def test_handles_timeout(bash)
```

**Source:** [`tests/tools/test_bash.py#L49`](tests/tools/test_bash.py#L49)

## `test_truncates_output_to_max_bytes()`

```python
async def test_truncates_output_to_max_bytes(bash)
```

**Source:** [`tests/tools/test_bash.py#L57`](tests/tools/test_bash.py#L57)

## `test_decodes_non_utf8_bytes()`

```python
async def test_decodes_non_utf8_bytes(bash)
```

**Source:** [`tests/tools/test_bash.py#L71`](tests/tools/test_bash.py#L71)

## `test_resolve_permission()`

```python
def test_resolve_permission()
```

**Source:** [`tests/tools/test_bash.py#L79`](tests/tools/test_bash.py#L79)

