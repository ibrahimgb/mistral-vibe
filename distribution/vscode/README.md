# Mistral Vibe — VS Code Extension

Mistral's open-source coding assistant, integrated into VS Code's chat panel.

## Features

- **`@vibe` Chat Participant** — Talk to Mistral Vibe directly in VS Code's built-in chat
- **Voice Input** — Click the mic button in the status bar (or press `Ctrl+R`) to record audio, auto-transcribed by Voxtral
- **Session Management** — Resume past sessions via the command palette
- **Full Tool Support** — File editing, bash commands, search & replace — powered by `vibe-acp`

## Prerequisites

- **vibe-acp** must be installed and available on your PATH
  - Install via: `uv tool install mistral-vibe` (provides both `vibe` and `vibe-acp`)
  - Or download from [GitHub releases](https://github.com/mistralai/mistral-vibe/releases)
- **MISTRAL_API_KEY** environment variable set (for the AI model + Voxtral voice transcription)
- For voice recording: `arecord` (Linux/ALSA) or `sox` (macOS/Windows)

## Usage

1. Open VS Code's Chat panel (`Ctrl+Shift+I`)
2. Type `@vibe` followed by your message
3. Vibe responds with full agent capabilities (file edits, bash, etc.)

### Voice Input

- Click `🎤 Vibe Voice` in the status bar, or press `Ctrl+R`
- Speak your request
- Click again to stop — audio is sent to Voxtral for transcription
- Transcribed text is inserted into the chat

### Commands

- **Vibe: New Session** — Start a fresh conversation
- **Vibe: Browse Sessions** — Pick and resume a past session
- **Vibe: Toggle Voice Recording** — Start/stop mic recording

## Extension Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `mistral-vibe.vibeAcpPath` | `vibe-acp` | Path to the vibe-acp binary |
| `mistral-vibe.mistralApiKey` | *(empty)* | API key for Voxtral transcription (falls back to `MISTRAL_API_KEY` env var) |

## Architecture

```
┌────────────────────┐     stdio / ACP      ┌───────────┐
│  VS Code Chat UI   │ ◄── JSON-RPC 2.0 ──► │ vibe-acp  │
│  (@vibe participant)│                      │           │
│                    │                      │ Agent Loop │
│  Status Bar Mic    │                      │ Tools      │
│  🎤 Vibe Voice     │                      │ Sessions   │
└────────────────────┘                      └───────────┘
         │
         │ Voxtral API (HTTPS)
         ▼
   Mistral Speech-to-Text
```

The extension is a thin bridge. All intelligence (agent loop, tools, sessions, context) lives in `vibe-acp`.

## Slash Commands (via ACP)

These commands are available in the chat (type them as your message):

| Command | Description |
|---------|-------------|
| `/clear` | Clear conversation history |
| `/compact` | Summarize and compact conversation |
| `/status` | Show token usage, cost, and step count |
| `/reload` | Reload configuration from disk |
| `/log` | Show session log directory path |
| `/proxy-setup` | Configure proxy and SSL settings |

Skills registered in `~/.vibe/agents/` are also available as `/skillname` commands.
