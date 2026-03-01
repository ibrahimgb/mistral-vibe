---
title: "tests.cli.test_braille_renderer"
tldr: "Module tests.cli.test_braille_renderer"
tags: [reference, api]
---

# `tests.cli.test_braille_renderer`

**Source:** [`tests/cli/test_braille_renderer.py`](tests/cli/test_braille_renderer.py) · 114 lines

## `TestBrailleDotIndex`

Tests for _braille_dot_index(x, y).

**Source:** [`tests/cli/test_braille_renderer.py#L12`](tests/cli/test_braille_renderer.py#L12)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_dot_positions_per_docstring()` |  | `None` | — |
| `test_all_indices_in_range_one_to_eight()` | x, y | `None` | — |

## `TestBrailleCharFromDotIndices`

Tests for _braille_char_from_dot_indices.

**Source:** [`tests/cli/test_braille_renderer.py#L34`](tests/cli/test_braille_renderer.py#L34)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_empty_indices_returns_space()` |  | `None` | — |
| `test_single_dot_one_returns_braille_char()` |  | `None` | — |
| `test_all_dots_returns_full_cell()` |  | `None` | — |
| `test_invalid_index_below_one_raises()` |  | `None` | — |
| `test_invalid_index_above_eight_raises()` |  | `None` | — |
| `test_order_of_indices_does_not_matter()` |  | `None` | — |

## `TestRenderBraille`

Tests for render_braille(dot_coords, width, height).

**Source:** [`tests/cli/test_braille_renderer.py#L64`](tests/cli/test_braille_renderer.py#L64)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_empty_coords_produces_blank_grid()` |  | `None` | — |
| `test_origin_one_dot()` |  | `None` | — |
| `test_output_dimensions_match_ceiled_width_and_height()` |  | `None` | — |
| `test_multiple_dots_in_same_cell_combine()` |  | `None` | — |
| `test_dots_in_different_cells()` |  | `None` | — |
| `test_multiple_rows()` |  | `None` | — |
| `test_accepts_complex_coords()` |  | `None` | — |

