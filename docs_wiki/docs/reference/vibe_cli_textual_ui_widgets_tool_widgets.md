---
title: "vibe.cli.textual_ui.widgets.tool_widgets"
tldr: "Module vibe.cli.textual_ui.widgets.tool_widgets"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.tool_widgets**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py)

This module defines the constants `APPROVAL_WIDGETS`, `RESULT_WIDGETS`.

## [**ToolApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L67)

The [**ToolApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L67) class (extending `Vertical`) base class for approval widgets with typed args. It exposes `__init__()`, `compose()`.

**Public API:**

- `def __init__()`
- `def compose()`

## [**ToolResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L92)

The [**ToolResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L92) class (extending `Static`) base class for result widgets with typed result. It exposes `__init__()`, `compose()`. Internally it relies on `_footer()`.

**Public API:**

- `def __init__()`
- `def compose()` — Default: show result fields.

**Internal helpers:**

- `_footer()` — Yield the footer with optional extra info.

## [**BashApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L128)

The [**BashApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L128) class (extending `ToolApprovalWidget[BashArgs]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**BashResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L133)

The [**BashResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L133) class (extending `ToolResultWidget[BashResult]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**WriteFileApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L163)

The [**WriteFileApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L163) class (extending `ToolApprovalWidget[WriteFileArgs]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**WriteFileResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L173)

The [**WriteFileResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L173) class (extending `ToolResultWidget[WriteFileResult]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**SearchReplaceApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L197)

The [**SearchReplaceApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L197) class (extending `ToolApprovalWidget[SearchReplaceArgs]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**SearchReplaceResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L209)

The [**SearchReplaceResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L209) class (extending `ToolResultWidget[SearchReplaceResult]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**TodoApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L222)

The [**TodoApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L222) class (extending `ToolApprovalWidget[TodoArgs]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**TodoResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L233)

The [**TodoResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L233) class (extending `ToolResultWidget[TodoResult]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**ReadFileApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L264)

The [**ReadFileApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L264) class (extending `ToolApprovalWidget[ReadFileArgs]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**ReadFileResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L277)

The [**ReadFileResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L277) class (extending `ToolResultWidget[ReadFileResult]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**GrepApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L297)

The [**GrepApprovalWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L297) class (extending `ToolApprovalWidget[GrepArgs]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**GrepResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L309)

The [**GrepResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L309) class (extending `ToolResultWidget[GrepResult]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**AskUserQuestionResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L325)

The [**AskUserQuestionResultWidget**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L325) class (extending `ToolResultWidget[AskUserQuestionResult]`). It exposes `compose()`.

**Public API:**

- `def compose()`

## [**_truncate_lines()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L26)

```python
def _truncate_lines(content: str, max_lines: int) -> tuple[str, str | None]
```

Truncate content to max_lines, returning (content, truncation_info).

## [**parse_search_replace_to_diff()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L35)

```python
def parse_search_replace_to_diff(content: str) -> list[str]
```

Parse SEARCH/REPLACE blocks and generate unified diff lines.

## [**render_diff_line()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L53)

```python
def render_diff_line(line: str) -> Static
```

Render a single diff line with appropriate styling.

## [**get_approval_widget()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L359)

```python
def get_approval_widget(tool_name: str, args: BaseModel) -> ToolApprovalWidget
```

## [**get_result_widget()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tool_widgets.py#L364)

```python
def get_result_widget(tool_name: str, result: BaseModel | None, success: bool, message: str, collapsed: bool, warnings: list[str] | None) -> ToolResultWidget
```

