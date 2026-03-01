---
title: "vibe.core.voice.recorder"
tldr: "Audio recorder using sounddevice callback streams."
tags: [reference, api]
---

# [**vibe.core.voice.recorder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/voice/recorder.py)

Audio recorder using sounddevice callback streams.

Records audio in the background via a callback-based ``sd.InputStream`` so the
main thread stays free.  The hardware device is detected automatically and audio
is downsampled to 16 kHz mono WAV for transcription.

This module defines the constants `TARGET_RATE`, `MIN_RECORDING_SECONDS`.

## [**AudioRecorder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/voice/recorder.py#L51)

The [**AudioRecorder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/voice/recorder.py#L51) class records audio from the microphone using *sounddevice*. It exposes `__init__()`, `get_levels()`, `start()`, `stop()`. Internally it relies on `_audio_callback()`.

**Public API:**

- `def __init__()`
- `def is_recording()`
- `def get_levels()` — Return recent RMS amplitude samples (0.0–1.0).
- `def start()` — Open the microphone and begin capturing audio.
- `def stop()` — Stop recording and return the captured audio as WAV bytes.

**Internal helpers:**

- `_audio_callback()` — Called on a background thread by sounddevice for each audio block.

## [**_find_input_device()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/voice/recorder.py#L22)

```python
def _find_input_device() -> tuple[int | None, int, int]
```

Find a working hardware input device.

Returns ``(device_index, channels, sample_rate)``.
Prefers real hardware capture devices over virtual/default nodes.

