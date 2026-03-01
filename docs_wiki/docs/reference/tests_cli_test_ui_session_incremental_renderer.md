---
title: "tests.cli.test_ui_session_incremental_renderer"
tldr: "Module tests.cli.test_ui_session_incremental_renderer"
tags: [reference, api]
---

# `tests.cli.test_ui_session_incremental_renderer`

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py`](tests/cli/test_ui_session_incremental_renderer.py) · 173 lines

## `vibe_config()`

```python
def vibe_config() -> VibeConfig
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L26`](tests/cli/test_ui_session_incremental_renderer.py#L26)

## `_pro_plan_gateway()`

```python
def _pro_plan_gateway() -> FakeWhoAmIGateway
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L32`](tests/cli/test_ui_session_incremental_renderer.py#L32)

## `_wait_until()`

```python
async def _wait_until(pause, predicate, timeout: float) -> None
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L42`](tests/cli/test_ui_session_incremental_renderer.py#L42)

## `_wait_for_load_more()`

```python
async def _wait_for_load_more(app: VibeApp, pause) -> None
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L51`](tests/cli/test_ui_session_incremental_renderer.py#L51)

## `_load_more_remaining()`

```python
def _load_more_remaining(app: VibeApp) -> int
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L57`](tests/cli/test_ui_session_incremental_renderer.py#L57)

## `test_ui_session_incremental_loader_shows_tail_and_load_more()`

```python
async def test_ui_session_incremental_loader_shows_tail_and_load_more(vibe_config: VibeConfig) -> None
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L65`](tests/cli/test_ui_session_incremental_renderer.py#L65)

## `test_ui_session_incremental_loader_load_more_shows_remaining_count()`

```python
async def test_ui_session_incremental_loader_load_more_shows_remaining_count(vibe_config: VibeConfig) -> None
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L90`](tests/cli/test_ui_session_incremental_renderer.py#L90)

## `test_ui_session_incremental_loader_load_more_batches_until_done()`

```python
async def test_ui_session_incremental_loader_load_more_batches_until_done(vibe_config: VibeConfig) -> None
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L123`](tests/cli/test_ui_session_incremental_renderer.py#L123)

## `test_ui_session_incremental_loader_keeps_top_alignment_when_not_scrollable()`

```python
async def test_ui_session_incremental_loader_keeps_top_alignment_when_not_scrollable(vibe_config: VibeConfig) -> None
```

**Source:** [`tests/cli/test_ui_session_incremental_renderer.py#L158`](tests/cli/test_ui_session_incremental_renderer.py#L158)

