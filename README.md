# Mistral Vibe Enhancment


```
██████████████████░░
██████████████████░░
████  ██████  ████░░
████    ██    ████░░
████          ████░░
████  ██  ██  ████░░
██      ██      ██░░
██████████████████░░
██████████████████░░
```

## Voice Input & Transcription

Mistral Vibe supports voice input as an alternative to typing. Instead of manually typing a prompt, you can speak into your microphone and have your speech automatically transcribed into text — then interact with the model as usual.

This feature, including the animated waveform visualization during recording, was inspired by the voice input experience in [Le Chat](https://chat.mistral.ai).

### How It Works

The voice input pipeline follows these steps:

1. **Record** — Press the mic button (○) or hit `Ctrl+R` to start recording. Audio is captured from your hardware microphone using a callback-based stream via `sounddevice`. A real-time animated waveform is displayed while recording.

2. **Transcribe** — Press the mic button again (or `Ctrl+R`) to stop recording. The captured audio is encoded as a 16 kHz mono WAV, base64-encoded, and sent to **Voxtral** (`voxtral-mini-latest`) through the Mistral chat completions API. Voxtral processes the audio and returns the transcribed text.

3. **Review & Edit** — The transcribed text is placed directly into the text input field. You can review it, make any corrections, or edit it before sending — just like any manually typed prompt.

4. **Send** — Press `Enter` to send the transcribed text to the model. From this point on, the standard workflow applies: the model receives your message and responds as usual.

This pipeline enables a fully hands-free input method while preserving full control over what gets sent to the model.

## Code Wiki

Auto-generated code wiki inspired by [Google's Code Wiki](https://research.google/blog/code-health-googles-internal-code-quality-tool/). The wiki transforms your codebase into comprehensive documentation — not just text extracted from docstrings, but also rich visual diagrams including UML class hierarchies, sequence flows, component diagrams, and data flow visualizations.

### What Gets Generated

The wiki produces dual outputs designed for different audiences:

1. **Developer Docs** — A full MkDocs site with narrative prose pages in Gemini-style markdown, featuring inline GitHub source links, subsystem guides, design pattern catalogs, and 14 auto-generated PlantUML diagrams (mind maps, C4 context, class hierarchies, sequence diagrams, component diagrams, data flow charts).

2. **LLM Docs** — Two flat markdown files for LLM context consumption: `llms.txt` (compact project index) and `llms-full.txt` (complete symbol reference with signatures and source links).

3. **Incremental Rebuilds** — Commit-based change detection skips unchanged builds entirely. Only modified `.py` files trigger re-analysis, and diagram renders are cached by content hash — a full rebuild takes ~40s, an incremental update with one changed file takes ~2s.

### How It Works

The wiki generator analyzes your codebase structure through AST parsing and produces architectural documentation automatically:

1. **Analyze** — Walk every `.py` file, parse the AST, extract modules, classes, functions, imports, docstrings, type annotations, decorators, and build a complete project graph.

2. **Cluster** — Group modules into subsystems (e.g., `core`, `cli`, `acp`, `tools`) based on directory structure and import patterns. Detect design patterns (factories, singletons, dependency injection, observer).

3. **Diagram** — Auto-generate 14 PlantUML diagrams: mind map overview, C4 context diagram, component overview, agent flow sequence, data flow, design patterns catalog, and per-subsystem class hierarchies.

4. **Write** — Render narrative pages with inline `[**ClassName**](https://github.com/...)` links, API reference with function signatures, LLM-optimized flat files, and JSON artefacts (`symbol_index.json`, `dependency_graph.json`).

5. **Serve** — Package everything as a MkDocs site with Material theme, custom CSS, search, syntax highlighting, and auto-generated navigation.

Generate the wiki with `/wiki` in the chat or run:

```bash
uv run python -c "import asyncio; from vibe.core.wiki.site_builder import build_wiki_site; asyncio.run(build_wiki_site('.'))"
```

The generated site lives in `docs_wiki/` and can be served locally with `mkdocs serve`.

## Message Edit & Delete

Edit or delete any user message directly in the TUI chat. Each user message shows a `⋮` menu with **Edit** and **Delete** actions.

### How It Works

- **⋮ Menu** — Every user message displays a small toggle button. Click it to reveal Edit and Delete options.
- **Edit** — Copies the message text back into the input box and removes the message pair (user + assistant response). Edit the text and re-send.
- **Delete** — Instantly removes the user message and its direct LLM response. Messages before and after the pair stay intact.
- **Ctrl+Up** — Shortcut to edit the last user message.
- **Session Persistence** — Deletions atomically rewrite the session's `messages.jsonl` file so changes survive restarts.

## LLM-Generated Session Titles

Sessions in the history picker now show descriptive, human-readable titles instead of raw session IDs, When a session is saved (on `/exit` or app close), the LLM generates a short title summarizing the conversation — similar to how ChatGPT and Le Chat auto-name their threads.

### How It Works

1. **Prompt** — A dedicated utility prompt (`session_title.md`) asks the model to produce a concise title (under 10 words) that captures the topic and intent of the conversation. The prompt explicitly avoids generic phrases like "Help" or "Question".

2. **Silent generation** — `AgentLoop.generate_title()` injects the title prompt into the conversation using `messages.silent()`, a context manager that prevents the title request/response from being persisted into the actual conversation history. This means the title generation is completely invisible to the user and does not pollute the chat.

3. **Save** — The generated title is stored in `SessionLogger.title_override`. When `save_interaction()` writes the session metadata JSON, it uses `title_override` if set, falling back to the old heuristic (`_get_title` — first user message) otherwise. The title lands in the `"title"` field of the session's `metadata.json`.

4. **Display** — The session picker (`/resume`) reads the `"title"` field from metadata and shows it in the list. If a title exists, it takes priority over the first user message preview, giving a cleaner browsing experience.

## Parallel Multi-Session Workflows

When working on a real project you often need the LLM to handle several things at once — refactor a module, write tests, draft docs — but the original CLI forces a strictly sequential workflow: you send a message, wait for the full response, and only then can you ask the next thing. If a task takes minutes (large refactors, long test suites), you're blocked the entire time.

Parallel sessions solve this. You can kick off a long-running task, open a brand-new chat with `/new`, and keep working with the same model in a completely separate conversation context. The first task continues executing in the background. When it finishes (or while it's still running), you can `/switch` back to check its output. Each session has its own message history, its own streaming output container, and its own agent state — they never interfere with each other.

### Usage

| Command | Description |
|---------|-------------|
| `/new` | Create a new session with a fresh conversation context |
| `/sessions` | List all active sessions (shows which are running) |
| `/switch <id>` | Switch to another session by ID (prefix matching supported) |

A **tab bar** appears when multiple sessions exist. Running tasks show `●`, the active session shows `▸`. Click any tab to switch.

### How It Works

The main challenge was that `VibeApp` was built around a single `AgentLoop` with all state (running flag, pending approvals, loading widget, event handler, tool call map, etc.) stored as flat attributes on the app. To support multiple concurrent sessions without rewriting every method, we introduced a layer of indirection:

- **SessionState** — A dataclass that bundles all per-session state into one object. Everything that was `self._agent_running`, `self._loading_widget`, `self.event_handler`, etc. now lives inside a `SessionState` instance. Each session also gets a unique DOM container ID so its chat messages are mounted into a separate `VerticalGroup` in the Textual widget tree.
- **SessionManager** — A registry that holds all `SessionState` objects and tracks which one is active. Switching sessions is just moving the `_active_id` pointer.
- **Property delegation** — ~20 properties on `VibeApp` delegate reads/writes to the active `SessionState`. This means every existing method that reads `self._agent_running` or `self.event_handler` still works — it just routes through the active session transparently. No method signatures had to change.
- **Session-bound EventHandlers** — Each session gets its own `EventHandler` created with a closure that captures that specific session's container. When the LLM streams tokens, the resulting widgets are mounted into the correct container even if the user has switched to a different session while it was running.
- **Turn isolation** — The core agent turn method captures `session = self._active` at the very start. All subsequent operations (streaming, error handling, cleanup) use that captured reference, never the delegating properties. Without this, switching sessions mid-turn would redirect the running task's output into the wrong container.
- **Non-blocking creation** — `AgentLoop.__init__` does heavy sync I/O (walking the file tree, running git, importing tools). We offload it to `run_in_executor()` so the UI doesn't freeze when you type `/new`.
- **No-interrupt flag** — `/new`, `/switch`, `/sessions` are tagged `no_interrupt=True` on the command dataclass. The submit handler checks this before cancelling the running agent — so creating or switching sessions never kills a background task.
- **DOM swap** — Switching hides the old session's `VerticalGroup` and shows (or lazily creates) the new one. Approval/question callbacks and context-progress listeners are re-wired to the new agent loop.
- **Save all on exit** — On quit, the app iterates every session, generates an LLM title for each, and saves all interaction logs — not just the session you happen to be viewing.

## Debug Mode

A dedicated agent mode that enforces a structured, hypothesis-driven debugging methodology — inspired by [Kilo Code](https://kilocode.ai)'s approach to systematic bug diagnosis. Instead of letting the LLM jump straight to a fix (and risk flip-flopping between attempts), Debug Mode forces a strict sequence: reproduce first, hypothesize causes, investigate with read-only tools, validate with diagnostics, confirm with the user, and only then apply a minimal surgical fix.

### How It Works

Switching to Debug Mode (`Shift+Tab` to cycle agents) activates a layered prompt that composes on top of the standard `cli.md` base, so all normal capabilities remain available while the debugging methodology takes priority.

1. **Reproduce** — Confirm the bug exists. Run the failing test, read the error log, or execute the reported command. Never assume the description alone is sufficient.

2. **Hypothesize** — List 5–7 possible causes covering a wide range (wrong input, stale state, off-by-one, race condition, missing null check, config mismatch, dependency version). Rank them and pick the 1–2 most likely.

3. **Investigate** — Gather evidence using read-only tools only (`read_file`, `grep`, `git log`, `git diff`). No file edits during this step.

4. **Validate** — Add temporary diagnostic output (print, logging, assert) to confirm or reject each hypothesis. If wrong, return to step 2 with new information.

5. **Confirm with User** — Present a clear diagnosis: root cause (one sentence), evidence (file:line, variable value), and proposed fix (minimal diff). Wait for user confirmation before proceeding.

6. **Fix** — Apply the smallest possible change. No refactors, no renaming, no unrelated restructuring. Re-run the failing scenario to verify.

### Visual Indicator

When Debug Mode is active, the chat input border turns **orange** — giving an immediate visual cue that you're in a specialized debugging session, distinct from the normal mode's border colors.

### Hard Rules Enforced

- Never jump to a fix without completing steps 1–4.
- Never make broad refactors. One bug, one surgical fix.
- If stuck after 2 investigation rounds, ask the user a specific question.
- Do not guess at runtime values — use tools to observe them.
- Flip-flopping (apply fix, revert, re-apply) is a critical failure. Diagnose fully before touching production code.

## VS Code Chat Integration

Mistral Vibe already had integrations for Zed and JetBrains, but I wanted the ability to chat with Vibe directly from VS Code's native sidebar chat panel — using the same model, tools, and session persistence as the CLI, without leaving the editor.

This is made possible by the **Agent Client Protocol (ACP)**, a JSON-RPC 2.0 protocol over stdio that Vibe already exposes through the `vibe-acp` binary. The VS Code extension acts as a thin client: it spawns `vibe-acp`, performs the handshake, and forwards messages. The full agent loop runs server-side — same Python process as the CLI.

### How It Works

The extension registers a VS Code Chat Participant (`@vibe`). On first use it spawns the `vibe-acp` process with the workspace as `cwd`, performs the ACP initialize handshake, and creates a session. Each chat message becomes a `session/prompt` JSON-RPC request. Responses stream back as `session/update` notifications and render as markdown in the chat panel in real time.

```
VS Code Chat Panel  →  @vibe Participant  →  ACP Client (TS)
                                                    │ stdio
                                                    ▼
                                              vibe-acp (Python)  →  AgentLoop  →  Mistral API
```

### Features

- **Chat** — `@vibe` in the sidebar chat, with streaming markdown responses
- **Slash commands** — `/clear`, `/compact`, `/status`, `/reload`, `/log`
- **Mode & model switching** — `Shift+Tab` or command palette quick picks
- **Voice input** — Status bar mic button (🎤), transcribed via Voxtral
- **Session management** — Create, list, and resume sessions




