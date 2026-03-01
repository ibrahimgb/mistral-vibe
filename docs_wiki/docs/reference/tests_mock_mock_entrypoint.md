---
title: "tests.mock.mock_entrypoint"
tldr: "Wrapper script that intercepts LLM calls when mocking is enabled."
tags: [reference, api]
---

# `tests.mock.mock_entrypoint`

**Source:** [`tests/mock/mock_entrypoint.py`](tests/mock/mock_entrypoint.py) · 65 lines

Wrapper script that intercepts LLM calls when mocking is enabled.

This script is used to mock the LLM calls when testing the CLI.
Mocked returns are stored in the VIBE_MOCK_LLM_DATA environment variable.

