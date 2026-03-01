---
title: "tests.autocompletion.test_path_prompt_transformer"
tldr: "Module tests.autocompletion.test_path_prompt_transformer"
tags: [reference, api]
---

# `tests.autocompletion.test_path_prompt_transformer`

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py`](tests/autocompletion/test_path_prompt_transformer.py) · 142 lines

## `test_treats_paths_to_files_as_embedded_resources()`

```python
def test_treats_paths_to_files_as_embedded_resources(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L11`](tests/autocompletion/test_path_prompt_transformer.py#L11)

## `test_treats_path_to_directory_as_resource_links()`

```python
def test_treats_path_to_directory_as_resource_links(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L33`](tests/autocompletion/test_path_prompt_transformer.py#L33)

## `test_keeps_emails_and_embeds_paths()`

```python
def test_keeps_emails_and_embeds_paths(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L47`](tests/autocompletion/test_path_prompt_transformer.py#L47)

## `test_ignores_nonexistent_paths()`

```python
def test_ignores_nonexistent_paths(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L64`](tests/autocompletion/test_path_prompt_transformer.py#L64)

## `test_falls_back_to_link_for_binary_files()`

```python
def test_falls_back_to_link_for_binary_files(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L74`](tests/autocompletion/test_path_prompt_transformer.py#L74)

## `test_excludes_supposed_binary_files_quickly_before_reading_content()`

```python
def test_excludes_supposed_binary_files_quickly_before_reading_content(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L87`](tests/autocompletion/test_path_prompt_transformer.py#L87)

## `test_applies_max_embed_size_guard()`

```python
def test_applies_max_embed_size_guard(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L105`](tests/autocompletion/test_path_prompt_transformer.py#L105)

## `test_parses_paths_with_special_characters_when_quoted()`

```python
def test_parses_paths_with_special_characters_when_quoted(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L116`](tests/autocompletion/test_path_prompt_transformer.py#L116)

## `test_deduplicates_identical_paths()`

```python
def test_deduplicates_identical_paths(tmp_path: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_prompt_transformer.py#L129`](tests/autocompletion/test_path_prompt_transformer.py#L129)

