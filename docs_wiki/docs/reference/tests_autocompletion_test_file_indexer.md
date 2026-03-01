---
title: "tests.autocompletion.test_file_indexer"
tldr: "Module tests.autocompletion.test_file_indexer"
tags: [reference, api]
---

# `tests.autocompletion.test_file_indexer`

**Source:** [`tests/autocompletion/test_file_indexer.py`](tests/autocompletion/test_file_indexer.py) · 349 lines

## `file_indexer()`

```python
def file_indexer() -> Generator[FileIndexer]
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L18`](tests/autocompletion/test_file_indexer.py#L18)

## `_wait_for()`

```python
def _wait_for(condition: Callable[[], bool], timeout) -> bool
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L24`](tests/autocompletion/test_file_indexer.py#L24)

## `_assert_index_state_stable()`

```python
def _assert_index_state_stable(file_indexer: FileIndexer, expected_entries: set[str], expected_incremental_updates: int, duration: float) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L33`](tests/autocompletion/test_file_indexer.py#L33)

## `test_updates_index_on_file_creation()`

```python
def test_updates_index_on_file_creation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, file_indexer: FileIndexer) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L47`](tests/autocompletion/test_file_indexer.py#L47)

## `test_updates_index_on_file_deletion()`

```python
def test_updates_index_on_file_deletion(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, file_indexer: FileIndexer) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L63`](tests/autocompletion/test_file_indexer.py#L63)

## `test_updates_index_on_file_rename()`

```python
def test_updates_index_on_file_rename(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, file_indexer: FileIndexer) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L80`](tests/autocompletion/test_file_indexer.py#L80)

## `test_updates_index_on_folder_rename()`

```python
def test_updates_index_on_folder_rename(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, file_indexer: FileIndexer) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L105`](tests/autocompletion/test_file_indexer.py#L105)

## `test_updates_index_incrementally_by_default()`

```python
def test_updates_index_incrementally_by_default(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, file_indexer: FileIndexer) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L133`](tests/autocompletion/test_file_indexer.py#L133)

## `test_rebuilds_index_when_mass_change_threshold_is_exceeded()`

```python
def test_rebuilds_index_when_mass_change_threshold_is_exceeded(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L155`](tests/autocompletion/test_file_indexer.py#L155)

## `test_switching_between_roots_restarts_index()`

```python
def test_switching_between_roots_restarts_index(tmp_path: Path, tmp_path_factory: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch, file_indexer: FileIndexer) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L185`](tests/autocompletion/test_file_indexer.py#L185)

## `test_watcher_failure_does_not_break_existing_index()`

```python
def test_watcher_failure_does_not_break_existing_index(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, file_indexer: FileIndexer) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L216`](tests/autocompletion/test_file_indexer.py#L216)

## `test_shutdown_cleans_up_resources()`

```python
def test_shutdown_cleans_up_resources(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L242`](tests/autocompletion/test_file_indexer.py#L242)

## `test_watcher_is_disabled_by_default()`

```python
def test_watcher_is_disabled_by_default(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L254`](tests/autocompletion/test_file_indexer.py#L254)

## `test_disabling_watcher_stops_runtime_updates()`

```python
def test_disabling_watcher_stops_runtime_updates(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L273`](tests/autocompletion/test_file_indexer.py#L273)

## `_current_entries()`

```python
def _current_entries(file_indexer: FileIndexer) -> set[str]
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L303`](tests/autocompletion/test_file_indexer.py#L303)

## `_assert_created_file_is_not_indexed()`

```python
def _assert_created_file_is_not_indexed(file_indexer: FileIndexer, tmp_path: Path, filename: str) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L307`](tests/autocompletion/test_file_indexer.py#L307)

## `_assert_created_file_is_indexed()`

```python
def _assert_created_file_is_indexed(file_indexer: FileIndexer, tmp_path: Path, filename: str) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L321`](tests/autocompletion/test_file_indexer.py#L321)

## `test_watcher_toggle_flow_off_on_off()`

```python
def test_watcher_toggle_flow_off_on_off(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/autocompletion/test_file_indexer.py#L331`](tests/autocompletion/test_file_indexer.py#L331)

