---
title: "tests.autocompletion.test_path_completer_recursive"
tldr: "Module tests.autocompletion.test_path_completer_recursive"
tags: [reference, api]
---

# `tests.autocompletion.test_path_completer_recursive`

**Source:** [`tests/autocompletion/test_path_completer_recursive.py`](tests/autocompletion/test_path_completer_recursive.py) · 69 lines

## `file_tree()`

```python
def file_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path
```

**Source:** [`tests/autocompletion/test_path_completer_recursive.py#L11`](tests/autocompletion/test_path_completer_recursive.py#L11)

## `test_finds_files_recursively_by_filename()`

```python
def test_finds_files_recursively_by_filename(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_recursive.py#L25`](tests/autocompletion/test_path_completer_recursive.py#L25)

## `test_finds_files_recursively_by_partial_path()`

```python
def test_finds_files_recursively_by_partial_path(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_recursive.py#L31`](tests/autocompletion/test_path_completer_recursive.py#L31)

## `test_finds_files_recursively_with_subsequence()`

```python
def test_finds_files_recursively_with_subsequence(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_recursive.py#L37`](tests/autocompletion/test_path_completer_recursive.py#L37)

## `test_finds_multiple_matches_recursively()`

```python
def test_finds_multiple_matches_recursively(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_recursive.py#L43`](tests/autocompletion/test_path_completer_recursive.py#L43)

## `test_prioritizes_exact_path_matches()`

```python
def test_prioritizes_exact_path_matches(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_recursive.py#L51`](tests/autocompletion/test_path_completer_recursive.py#L51)

## `test_finds_files_when_pattern_matches_directory_name()`

```python
def test_finds_files_when_pattern_matches_directory_name(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_recursive.py#L57`](tests/autocompletion/test_path_completer_recursive.py#L57)

