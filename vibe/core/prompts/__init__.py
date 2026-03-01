from __future__ import annotations

from enum import StrEnum, auto
from pathlib import Path

from vibe import VIBE_ROOT

_PROMPTS_DIR = VIBE_ROOT / "core" / "prompts"

# Prompts that layer on top of CLI base prompt rather than replacing it.
_COMPOSED_PROMPTS: set[str] = {"debug"}


class Prompt(StrEnum):
    @property
    def path(self) -> Path:
        return (_PROMPTS_DIR / self.value).with_suffix(".md")

    def read(self) -> str:
        return self.path.read_text(encoding="utf-8").strip()


class SystemPrompt(Prompt):
    CLI = auto()
    DEBUG = auto()
    EXPLORE = auto()
    TESTS = auto()

    def read(self) -> str:
        """Read the prompt, composing with CLI base if this is a layered prompt."""
        content = self.path.read_text(encoding="utf-8").strip()
        if self.value in _COMPOSED_PROMPTS and self != SystemPrompt.CLI:
            base = SystemPrompt.CLI.path.read_text(encoding="utf-8").strip()
            return f"{base}\n\n---\n\n{content}"
        return content


class UtilityPrompt(Prompt):
    COMPACT = auto()
    DANGEROUS_DIRECTORY = auto()
    PROJECT_CONTEXT = auto()
    SESSION_TITLE = auto()


__all__ = ["SystemPrompt", "UtilityPrompt"]
