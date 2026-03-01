---
title: "vibe.core.autocompletion.fuzzy"
tldr: "Module vibe.core.autocompletion.fuzzy"
tags: [reference, api]
---

# [**vibe.core.autocompletion.fuzzy**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py)

This module defines the constants `PREFIX_MULTIPLIER`, `WORD_BOUNDARY_MULTIPLIER`, `CONSECUTIVE_MULTIPLIER`.

## [**MatchResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py#L11)

The [**MatchResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py#L11) dataclass. Key fields include `matched`, `score`, `matched_indices`.

## [**fuzzy_match()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py#L17)

```python
def fuzzy_match(pattern: str, text: str, text_lower: str | None) -> MatchResult
```

## [**_find_best_match()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py#L26)

```python
def _find_best_match(pattern_original: str, pattern_lower: str, text_lower: str, text_original: str) -> MatchResult
```

## [**_try_word_boundary_match()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py#L60)

```python
def _try_word_boundary_match(pattern_original: str, pattern: str, text_lower: str, text_original: str) -> MatchResult
```

## [**_try_consecutive_match()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py#L94)

```python
def _try_consecutive_match(pattern_original: str, pattern: str, text_lower: str, text_original: str) -> MatchResult
```

## [**_calculate_score()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/fuzzy.py#L146)

```python
def _calculate_score(pattern_original: str, pattern: str, text_lower: str, indices: tuple[int, ...], text_original: str) -> float
```

