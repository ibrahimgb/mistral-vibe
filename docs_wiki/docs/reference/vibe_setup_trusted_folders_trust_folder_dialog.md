---
title: "vibe.setup.trusted_folders.trust_folder_dialog"
tldr: "Module vibe.setup.trusted_folders.trust_folder_dialog"
tags: [reference, api]
---

# [**vibe.setup.trusted_folders.trust_folder_dialog**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py)

## [**TrustDialogQuitException**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py#L17)

The [**TrustDialogQuitException**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py#L17) class (extending `Exception`).

## [**TrustFolderDialog**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py#L21)

The [**TrustFolderDialog**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py#L21) class (extending `CenterMiddle`). It exposes `__init__()`, `compose()`, `on_mount()`, `action_move_left()`, `action_move_right()` among 9 public methods. Internally it relies on `_update_options()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `async def on_mount()`
- `def action_move_left()`
- `def action_move_right()`
- `def action_select()`
- `def action_select_1()`
- `def action_select_2()`
- `def on_blur()`

**Internal helpers:**

- `_update_options()`

## [**TrustFolderApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py#L139)

The [**TrustFolderApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py#L139) class (extending `App`). It exposes `__init__()`, `on_mount()`, `compose()`, `action_quit_without_saving()`, `on_trust_folder_dialog_trusted()` among 7 public methods.

**Public API:**

- `def __init__()`
- `def on_mount()`
- `def compose()`
- `def action_quit_without_saving()`
- `def on_trust_folder_dialog_trusted()`
- `def on_trust_folder_dialog_untrusted()`
- `def run_trust_dialog()`

## [**ask_trust_folder()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/setup/trusted_folders/trust_folder_dialog.py#L178)

```python
def ask_trust_folder(folder_path: Path) -> bool | None
```

