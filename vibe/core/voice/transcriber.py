"""Transcribe audio via Voxtral (Mistral multimodal chat completions)."""

from __future__ import annotations

import base64
import os

from mistralai import Mistral

from vibe.core.logger import logger


VOXTRAL_MODEL = "voxtral-mini-latest"


async def transcribe_audio(wav_bytes: bytes) -> str:
    """Send *wav_bytes* to Voxtral and return the transcribed text.

    The audio is base64-encoded and sent as a multimodal audio chunk
    alongside a text instruction via the chat completions endpoint.

    Raises:
        RuntimeError: If ``MISTRAL_API_KEY`` is not set or the API call fails.
    """
    api_key = os.environ.get("MISTRAL_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "MISTRAL_API_KEY environment variable is not set – "
            "cannot transcribe audio"
        )

    audio_b64 = base64.b64encode(wav_bytes).decode("utf-8")

    client = Mistral(api_key=api_key)

    logger.debug("Sending %d bytes of audio to %s for transcription", len(wav_bytes), VOXTRAL_MODEL)

    response = await client.chat.complete_async(
        model=VOXTRAL_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_audio",
                        "input_audio": audio_b64,
                    },
                    {
                        "type": "text",
                        "text": "Transcribe this audio exactly. Return only the transcription, nothing else.",
                    },
                ],
            }
        ],
    )

    if not response or not response.choices:
        raise RuntimeError("Voxtral returned an empty response")

    text = response.choices[0].message.content
    if not isinstance(text, str):
        raise RuntimeError(f"Unexpected response type from Voxtral: {type(text)}")

    logger.debug("Transcription result: %s", text[:120])
    return text.strip()
