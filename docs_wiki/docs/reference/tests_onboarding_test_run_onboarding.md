---
title: "tests.onboarding.test_run_onboarding"
tldr: "Module tests.onboarding.test_run_onboarding"
tags: [reference, api]
---

# `tests.onboarding.test_run_onboarding`

**Source:** [`tests/onboarding/test_run_onboarding.py`](tests/onboarding/test_run_onboarding.py) · 60 lines

## `StubApp`

**Bases:** `App[str | None]`

**Source:** [`tests/onboarding/test_run_onboarding.py#L13`](tests/onboarding/test_run_onboarding.py#L13)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | return_value | `None` | — |
| `run()` |  | `str | None` | — |

## `_exit_raiser()`

```python
def _exit_raiser(code: int) -> None
```

**Source:** [`tests/onboarding/test_run_onboarding.py#L23`](tests/onboarding/test_run_onboarding.py#L23)

## `test_exits_on_cancel()`

```python
def test_exits_on_cancel(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None
```

**Source:** [`tests/onboarding/test_run_onboarding.py#L27`](tests/onboarding/test_run_onboarding.py#L27)

## `test_warns_on_save_error()`

```python
def test_warns_on_save_error(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None
```

**Source:** [`tests/onboarding/test_run_onboarding.py#L40`](tests/onboarding/test_run_onboarding.py#L40)

## `test_successfully_completes()`

```python
def test_successfully_completes(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None
```

**Source:** [`tests/onboarding/test_run_onboarding.py#L52`](tests/onboarding/test_run_onboarding.py#L52)

