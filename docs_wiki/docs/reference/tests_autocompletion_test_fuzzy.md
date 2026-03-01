---
title: "tests.autocompletion.test_fuzzy"
tldr: "Module tests.autocompletion.test_fuzzy"
tags: [reference, api]
---

# `tests.autocompletion.test_fuzzy`

**Source:** [`tests/autocompletion/test_fuzzy.py`](tests/autocompletion/test_fuzzy.py) · 96 lines

## `test_empty_pattern_matches_anything()`

```python
def test_empty_pattern_matches_anything() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L6`](tests/autocompletion/test_fuzzy.py#L6)

## `test_matches_exact_prefix()`

```python
def test_matches_exact_prefix() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L14`](tests/autocompletion/test_fuzzy.py#L14)

## `test_no_match_when_characters_are_out_of_order()`

```python
def test_no_match_when_characters_are_out_of_order() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L20`](tests/autocompletion/test_fuzzy.py#L20)

## `test_treats_consecutive_characters_as_subsequence()`

```python
def test_treats_consecutive_characters_as_subsequence() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L26`](tests/autocompletion/test_fuzzy.py#L26)

## `test_ignores_case()`

```python
def test_ignores_case() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L32`](tests/autocompletion/test_fuzzy.py#L32)

## `test_treats_scattered_characters_as_subsequence()`

```python
def test_treats_scattered_characters_as_subsequence() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L38`](tests/autocompletion/test_fuzzy.py#L38)

## `test_treats_path_separator_as_word_boundary()`

```python
def test_treats_path_separator_as_word_boundary() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L44`](tests/autocompletion/test_fuzzy.py#L44)

## `test_prefers_word_boundary_matching_over_subsequence()`

```python
def test_prefers_word_boundary_matching_over_subsequence() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L50`](tests/autocompletion/test_fuzzy.py#L50)

## `test_scores_exact_prefix_match_higher_than_consecutive_and_subsequence()`

```python
def test_scores_exact_prefix_match_higher_than_consecutive_and_subsequence() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L57`](tests/autocompletion/test_fuzzy.py#L57)

## `test_finds_no_match_when_pattern_is_longer_than_entry()`

```python
def test_finds_no_match_when_pattern_is_longer_than_entry() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L67`](tests/autocompletion/test_fuzzy.py#L67)

## `test_prefers_consecutive_match_over_subsequence()`

```python
def test_prefers_consecutive_match_over_subsequence() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L73`](tests/autocompletion/test_fuzzy.py#L73)

## `test_prefers_case_sensitive_match_over_case_insensitive()`

```python
def test_prefers_case_sensitive_match_over_case_insensitive() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L80`](tests/autocompletion/test_fuzzy.py#L80)

## `test_treats_uppercase_letter_as_word_boundary()`

```python
def test_treats_uppercase_letter_as_word_boundary() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L87`](tests/autocompletion/test_fuzzy.py#L87)

## `test_favors_earlier_positions()`

```python
def test_favors_earlier_positions() -> None
```

**Source:** [`tests/autocompletion/test_fuzzy.py#L93`](tests/autocompletion/test_fuzzy.py#L93)

