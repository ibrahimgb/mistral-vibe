---
title: "tests.conftest"
tldr: "Module tests.conftest"
tags: [reference, api]
---

# `tests.conftest`

**Source:** [`tests/conftest.py`](tests/conftest.py) · 208 lines

## `get_base_config()`

```python
def get_base_config() -> dict[str, Any]
```

**Source:** [`tests/conftest.py#L26`](tests/conftest.py#L26)

## `tmp_working_directory()`

```python
def tmp_working_directory(monkeypatch: pytest.MonkeyPatch, tmp_path_factory: pytest.TempPathFactory) -> Path
```

**Source:** [`tests/conftest.py#L49`](tests/conftest.py#L49)

## `config_dir()`

```python
def config_dir(monkeypatch: pytest.MonkeyPatch, tmp_path_factory: pytest.TempPathFactory) -> Path
```

**Source:** [`tests/conftest.py#L58`](tests/conftest.py#L58)

## `_unlock_config_paths()`

```python
def _unlock_config_paths()
```

**Source:** [`tests/conftest.py#L72`](tests/conftest.py#L72)

## `_mock_api_key()`

```python
def _mock_api_key(monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/conftest.py#L77`](tests/conftest.py#L77)

## `_mock_platform()`

```python
def _mock_platform(monkeypatch: pytest.MonkeyPatch) -> None
```

Mock platform to be Linux with /bin/sh shell for consistent test behavior.

This ensures that platform-specific system prompt generation is consistent
across all tests regardless of the actual platform running the tests.

**Source:** [`tests/conftest.py#L82`](tests/conftest.py#L82)

## `_mock_update_commands()`

```python
def _mock_update_commands(monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/conftest.py#L93`](tests/conftest.py#L93)

## `telemetry_events()`

```python
def telemetry_events(monkeypatch: pytest.MonkeyPatch) -> list[dict[str, Any]]
```

**Source:** [`tests/conftest.py#L98`](tests/conftest.py#L98)

## `vibe_app()`

```python
def vibe_app() -> VibeApp
```

**Source:** [`tests/conftest.py#L114`](tests/conftest.py#L114)

## `agent_loop()`

```python
def agent_loop() -> AgentLoop
```

**Source:** [`tests/conftest.py#L119`](tests/conftest.py#L119)

## `vibe_config()`

```python
def vibe_config() -> VibeConfig
```

**Source:** [`tests/conftest.py#L124`](tests/conftest.py#L124)

## `build_test_vibe_config()`

```python
def build_test_vibe_config() -> VibeConfig
```

**Source:** [`tests/conftest.py#L128`](tests/conftest.py#L128)

## `build_test_agent_loop()`

```python
def build_test_agent_loop() -> AgentLoop
```

**Source:** [`tests/conftest.py#L146`](tests/conftest.py#L146)

## `build_test_vibe_app()`

```python
def build_test_vibe_app() -> VibeApp
```

**Source:** [`tests/conftest.py#L166`](tests/conftest.py#L166)

