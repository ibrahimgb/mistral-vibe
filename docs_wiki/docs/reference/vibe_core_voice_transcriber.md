---
title: "vibe.core.voice.transcriber"
tldr: "Transcribe audio via Voxtral (Mistral multimodal chat completions)."
tags: [reference, api]
---

# [**vibe.core.voice.transcriber**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/voice/transcriber.py)

Transcribe audio via Voxtral (Mistral multimodal chat completions).

This module defines the constants `VOXTRAL_MODEL`.

## [**transcribe_audio()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/voice/transcriber.py#L16)

```python
async def transcribe_audio(wav_bytes: bytes) -> str
```

Send *wav_bytes* to Voxtral and return the transcribed text.

The audio is base64-encoded and sent as a multimodal audio chunk
alongside a text instruction via the chat completions endpoint.

Raises:
    RuntimeError: If ``MISTRAL_API_KEY`` is not set or the API call fails.

