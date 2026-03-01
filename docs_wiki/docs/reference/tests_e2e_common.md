---
title: "tests.e2e.common"
tldr: "Module tests.e2e.common"
tags: [reference, api]
---

# `tests.e2e.common`

**Source:** [`tests/e2e/common.py`](tests/e2e/common.py) · 86 lines

## `SpawnedVibeProcessFixture`

*🔌 Protocol*

**Bases:** `Protocol`

**Source:** [`tests/e2e/common.py#L14`](tests/e2e/common.py#L14)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__call__()` | workdir | `AbstractContextManager[tuple[pexpect.spawn, io.StringIO]]` | — |

## `ansi_tolerant_pattern()`

```python
def ansi_tolerant_pattern(text: str) -> re.Pattern[str]
```

**Source:** [`tests/e2e/common.py#L20`](tests/e2e/common.py#L20)

## `write_e2e_config()`

```python
def write_e2e_config(vibe_home: Path, api_base: str) -> None
```

**Source:** [`tests/e2e/common.py#L25`](tests/e2e/common.py#L25)

## `strip_ansi()`

```python
def strip_ansi(text: str) -> str
```

**Source:** [`tests/e2e/common.py#L48`](tests/e2e/common.py#L48)

## `wait_for_request_count()`

```python
def wait_for_request_count(request_count_getter: Callable[[], int], expected_count: int, timeout: float) -> None
```

**Source:** [`tests/e2e/common.py#L52`](tests/e2e/common.py#L52)

## `wait_for_main_screen()`

```python
def wait_for_main_screen(child: pexpect.spawn, timeout: float) -> None
```

**Source:** [`tests/e2e/common.py#L63`](tests/e2e/common.py#L63)

## `wait_for_rendered_text()`

```python
def wait_for_rendered_text(child: pexpect.spawn, captured: io.StringIO, needle: str, timeout: float) -> None
```

**Source:** [`tests/e2e/common.py#L67`](tests/e2e/common.py#L67)

