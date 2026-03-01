---
title: "vibe.core.tools.builtins.ask_user_question"
tldr: "Module vibe.core.tools.builtins.ask_user_question"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.ask_user_question**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py)

## [**Choice**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L20)

The [**Choice**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L20) Pydantic model (extending `BaseModel`). Key fields include `label`, `description`.

## [**Question**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L27)

The [**Question**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L27) Pydantic model (extending `BaseModel`). Key fields include `question`, `header`, `options`, `multi_select`, `hide_other`.

## [**AskUserQuestionArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L47)

The [**AskUserQuestionArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L47) Pydantic model (extending `BaseModel`). Key fields include `questions`.

## [**Answer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L55)

The [**Answer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L55) Pydantic model (extending `BaseModel`). Key fields include `question`, `answer`, `is_other`.

## [**AskUserQuestionResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L63)

The [**AskUserQuestionResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L63) Pydantic model (extending `BaseModel`). Key fields include `answers`, `cancelled`.

## [**AskUserQuestionConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L70)

The [**AskUserQuestionConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L70) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`.

## [**AskUserQuestion**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L74)

The [**AskUserQuestion**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/ask_user_question.py#L74) class (extending `BaseTool[AskUserQuestionArgs, AskUserQuestionResult, AskUserQuestionConfig, BaseToolState]`, `ToolUIData[AskUserQuestionArgs, AskUserQuestionResult]`). It exposes `format_call_display()`, `get_result_display()`, `get_status_text()`, `run()`.

**Public API:**

- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `async def run()`

