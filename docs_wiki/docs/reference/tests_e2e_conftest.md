---
title: "tests.e2e.conftest"
tldr: "Module tests.e2e.conftest"
tags: [reference, api]
---

# `tests.e2e.conftest`

**Source:** [`tests/e2e/conftest.py`](tests/e2e/conftest.py) · 82 lines

## `streaming_mock_server()`

```python
def streaming_mock_server(request: pytest.FixtureRequest) -> Iterator[StreamingMockServer]
```

**Source:** [`tests/e2e/conftest.py#L19`](tests/e2e/conftest.py#L19)

## `setup_e2e_env()`

```python
def setup_e2e_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, streaming_mock_server: StreamingMockServer) -> None
```

**Source:** [`tests/e2e/conftest.py#L32`](tests/e2e/conftest.py#L32)

## `e2e_workdir()`

```python
def e2e_workdir(tmp_path: Path) -> Path
```

**Source:** [`tests/e2e/conftest.py#L45`](tests/e2e/conftest.py#L45)

## `spawned_vibe_process()`

```python
def spawned_vibe_process() -> SpawnedVibeFactory
```

**Source:** [`tests/e2e/conftest.py#L59`](tests/e2e/conftest.py#L59)

