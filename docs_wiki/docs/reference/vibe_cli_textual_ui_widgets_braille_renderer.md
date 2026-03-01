---
title: "vibe.cli.textual_ui.widgets.braille_renderer"
tldr: "Module vibe.cli.textual_ui.widgets.braille_renderer"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.braille_renderer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/braille_renderer.py)

This module defines the constants `_BRAILLE_DOT_COUNT`.

## [**_braille_dot_index()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/braille_renderer.py#L11)

```python
def _braille_dot_index(x: int, y: int) -> int
```

returns the number associated with a dot in a braille character
x ∈ {0, 1}, y ∈ {0, 1, 2, 3}
 -x->
| 1 4
y 2 5
| 3 6
V 7 8

## [**render_braille()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/braille_renderer.py#L31)

```python
def render_braille(dot_coords: Iterable[complex], width: int, height: int) -> str
```

this function receives a list of dot coordinantes, a width and a height,
and returns a string representing these dots with braille characters.

Origin is (0,0) and is located at the top left:
0----x---->
|
y
|
V

