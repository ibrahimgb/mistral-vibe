"""Tests for MessageList.remove_pair()."""

from __future__ import annotations

import pytest

from vibe.core.types import LLMMessage, MessageList, Role


def _user(content: str, message_id: str | None = None) -> LLMMessage:
    msg = LLMMessage(role=Role.user, content=content)
    if message_id is not None:
        msg.message_id = message_id
    return msg


def _assistant(content: str) -> LLMMessage:
    return LLMMessage(role=Role.assistant, content=content)


def _tool(content: str, tool_call_id: str = "tc1") -> LLMMessage:
    return LLMMessage(
        role=Role.tool, content=content, tool_call_id=tool_call_id, name="test_tool"
    )


class TestRemovePairBasic:
    def test_basic_pair_removal(self) -> None:
        """User + assistant → both removed, list empty."""
        u = _user("hello", message_id="u1")
        a = _assistant("hi")
        ml = MessageList([u, a])

        ml.remove_pair("u1")

        assert len(ml) == 0

    def test_pair_with_tool_messages(self) -> None:
        """User → assistant(tool_call) → tool → assistant → next_user.
        Remove first user: everything up to (not including) next_user is removed.
        """
        u1 = _user("build it", message_id="u1")
        a1 = _assistant("calling tool")
        t1 = _tool("tool result")
        a2 = _assistant("done")
        u2 = _user("thanks", message_id="u2")
        a3 = _assistant("you're welcome")

        ml = MessageList([u1, a1, t1, a2, u2, a3])

        ml.remove_pair("u1")

        assert len(ml) == 2
        assert ml[0].message_id == "u2"
        assert ml[1].content == "you're welcome"

    def test_last_pair(self) -> None:
        """Three pairs, remove last → first two intact."""
        u1 = _user("one", message_id="u1")
        a1 = _assistant("r1")
        u2 = _user("two", message_id="u2")
        a2 = _assistant("r2")
        u3 = _user("three", message_id="u3")
        a3 = _assistant("r3")

        ml = MessageList([u1, a1, u2, a2, u3, a3])

        ml.remove_pair("u3")

        assert len(ml) == 4
        assert ml[0].message_id == "u1"
        assert ml[1].content == "r1"
        assert ml[2].message_id == "u2"
        assert ml[3].content == "r2"

    def test_middle_pair(self) -> None:
        """Three pairs, remove middle → first and third stay."""
        u1 = _user("one", message_id="u1")
        a1 = _assistant("r1")
        u2 = _user("two", message_id="u2")
        a2 = _assistant("r2")
        u3 = _user("three", message_id="u3")
        a3 = _assistant("r3")

        ml = MessageList([u1, a1, u2, a2, u3, a3])

        ml.remove_pair("u2")

        assert len(ml) == 4
        assert ml[0].message_id == "u1"
        assert ml[1].content == "r1"
        assert ml[2].message_id == "u3"
        assert ml[3].content == "r3"

    def test_unknown_id_raises_value_error(self) -> None:
        u1 = _user("hello", message_id="u1")
        a1 = _assistant("hi")
        ml = MessageList([u1, a1])

        with pytest.raises(ValueError, match="No user message with message_id='bogus'"):
            ml.remove_pair("bogus")

    def test_user_message_with_no_response(self) -> None:
        """User message at end of list with no assistant reply → only user removed."""
        u1 = _user("one", message_id="u1")
        a1 = _assistant("r1")
        u2 = _user("trailing", message_id="u2")

        ml = MessageList([u1, a1, u2])

        ml.remove_pair("u2")

        assert len(ml) == 2
        assert ml[0].message_id == "u1"
        assert ml[1].content == "r1"

    def test_preserves_system_messages(self) -> None:
        """System message at the start is untouched."""
        sys = LLMMessage(role=Role.system, content="system prompt")
        u1 = _user("hello", message_id="u1")
        a1 = _assistant("hi")

        ml = MessageList([sys, u1, a1])

        ml.remove_pair("u1")

        assert len(ml) == 1
        assert ml[0].role == Role.system
