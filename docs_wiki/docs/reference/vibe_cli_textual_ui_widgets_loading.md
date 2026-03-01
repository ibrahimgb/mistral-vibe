---
title: "vibe.cli.textual_ui.widgets.loading"
tldr: "Module vibe.cli.textual_ui.widgets.loading"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.loading**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/loading.py)

## [**LoadingWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/loading.py#L30)

The [**LoadingWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/loading.py#L30) class (extending `SpinnerMixin`, `Static`). It exposes `__init__()`, `pause_timer()`, `resume_timer()`, `set_status()`, `compose()` among 7 public methods. Internally it relies on `_update_animation()`.

**Public API:**

- `def __init__()`
- `def pause_timer()`
- `def resume_timer()`
- `def set_status()`
- `def compose()`
- `def on_mount()`
- `def on_resize()`

**Internal helpers:**

- `_update_animation()`

## [**paused_timer()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/loading.py#L196)

```python
def paused_timer(loading_widget: LoadingWidget | None) -> Iterator[None]
```

