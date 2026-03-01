---
title: "tests.autocompletion.test_path_completer_fuzzy"
tldr: "Module tests.autocompletion.test_path_completer_fuzzy"
tags: [reference, api]
---

# `tests.autocompletion.test_path_completer_fuzzy`

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py`](tests/autocompletion/test_path_completer_fuzzy.py) · 122 lines

## `file_tree()`

```python
def file_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L11`](tests/autocompletion/test_path_completer_fuzzy.py#L11)

## `test_fuzzy_matches_subsequence_characters()`

```python
def test_fuzzy_matches_subsequence_characters(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L31`](tests/autocompletion/test_path_completer_fuzzy.py#L31)

## `test_fuzzy_matches_consecutive_characters_higher()`

```python
def test_fuzzy_matches_consecutive_characters_higher(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L37`](tests/autocompletion/test_path_completer_fuzzy.py#L37)

## `test_fuzzy_matches_prefix_highest()`

```python
def test_fuzzy_matches_prefix_highest(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L43`](tests/autocompletion/test_path_completer_fuzzy.py#L43)

## `test_fuzzy_matches_across_directory_boundaries()`

```python
def test_fuzzy_matches_across_directory_boundaries(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L49`](tests/autocompletion/test_path_completer_fuzzy.py#L49)

## `test_fuzzy_matches_case_insensitive()`

```python
def test_fuzzy_matches_case_insensitive(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L55`](tests/autocompletion/test_path_completer_fuzzy.py#L55)

## `test_fuzzy_matches_word_boundaries_preferred()`

```python
def test_fuzzy_matches_word_boundaries_preferred(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L61`](tests/autocompletion/test_path_completer_fuzzy.py#L61)

## `test_fuzzy_matches_empty_pattern_shows_all()`

```python
def test_fuzzy_matches_empty_pattern_shows_all(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L67`](tests/autocompletion/test_path_completer_fuzzy.py#L67)

## `test_fuzzy_matches_hidden_files_only_with_dot()`

```python
def test_fuzzy_matches_hidden_files_only_with_dot(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L74`](tests/autocompletion/test_path_completer_fuzzy.py#L74)

## `test_fuzzy_matches_directories_and_files()`

```python
def test_fuzzy_matches_directories_and_files(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L80`](tests/autocompletion/test_path_completer_fuzzy.py#L80)

## `test_fuzzy_matches_sorted_by_score()`

```python
def test_fuzzy_matches_sorted_by_score(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L87`](tests/autocompletion/test_path_completer_fuzzy.py#L87)

## `test_fuzzy_matches_nested_directories()`

```python
def test_fuzzy_matches_nested_directories(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L93`](tests/autocompletion/test_path_completer_fuzzy.py#L93)

## `test_fuzzy_matches_partial_filename()`

```python
def test_fuzzy_matches_partial_filename(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L99`](tests/autocompletion/test_path_completer_fuzzy.py#L99)

## `test_fuzzy_matches_multiple_files_with_same_pattern()`

```python
def test_fuzzy_matches_multiple_files_with_same_pattern(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L105`](tests/autocompletion/test_path_completer_fuzzy.py#L105)

## `test_fuzzy_matches_no_results_when_no_match()`

```python
def test_fuzzy_matches_no_results_when_no_match(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L112`](tests/autocompletion/test_path_completer_fuzzy.py#L112)

## `test_fuzzy_matches_directory_traversal()`

```python
def test_fuzzy_matches_directory_traversal(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completer_fuzzy.py#L117`](tests/autocompletion/test_path_completer_fuzzy.py#L117)

