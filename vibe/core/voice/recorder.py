"""Audio recorder using sounddevice callback streams.

Records audio in the background via a callback-based ``sd.InputStream`` so the
main thread stays free.  The hardware device is detected automatically and audio
is downsampled to 16 kHz mono WAV for transcription.
"""

from __future__ import annotations

import collections
import io

import numpy as np
import sounddevice as sd
import soundfile as sf


TARGET_RATE = 16_000
MIN_RECORDING_SECONDS = 0.5


def _find_input_device() -> tuple[int | None, int, int]:
    """Find a working hardware input device.

    Returns ``(device_index, channels, sample_rate)``.
    Prefers real hardware capture devices over virtual/default nodes.
    """
    devices = sd.query_devices()

    # Prefer known hardware names first
    for i, d in enumerate(devices):
        if d["max_input_channels"] > 0 and (
            d["name"].startswith("HDA")
            or d["name"].startswith("WD19")
            or "USB Audio" in d["name"]
        ):
            sr = int(d["default_samplerate"])
            ch = min(d["max_input_channels"], 2)
            return i, ch, sr

    # Fallback: any non-default device with input channels
    for i, d in enumerate(devices):
        if d["max_input_channels"] > 0 and "default" not in d["name"]:
            sr = int(d["default_samplerate"])
            ch = min(d["max_input_channels"], 2)
            return i, ch, sr

    return None, 1, 16_000


class AudioRecorder:
    """Records audio from the microphone using *sounddevice*.

    Usage::

        recorder = AudioRecorder()
        recorder.start()             # begins capturing
        wav_bytes = recorder.stop()  # stops and returns WAV bytes
    """

    def __init__(self) -> None:
        self._chunks: list[np.ndarray] = []
        self._stream: sd.InputStream | None = None
        self._is_recording = False
        self._device, self._channels, self._hw_rate = _find_input_device()
        self._levels: collections.deque[float] = collections.deque(maxlen=80)

    @property
    def is_recording(self) -> bool:
        return self._is_recording

    def get_levels(self) -> list[float]:
        """Return recent RMS amplitude samples (0.0–1.0)."""
        return list(self._levels)

    def start(self) -> None:
        """Open the microphone and begin capturing audio."""
        self._chunks = []
        self._levels.clear()
        self._stream = sd.InputStream(
            device=self._device,
            samplerate=self._hw_rate,
            channels=self._channels,
            dtype="float32",
            callback=self._audio_callback,
        )
        self._stream.start()
        self._is_recording = True

    def stop(self) -> bytes:
        """Stop recording and return the captured audio as WAV bytes.

        Raises:
            RuntimeError: If stop is called while not recording.
            ValueError: If the recording is shorter than *MIN_RECORDING_SECONDS*.
        """
        if not self._is_recording or self._stream is None:
            raise RuntimeError("Not currently recording")

        self._stream.stop()
        self._stream.close()
        self._stream = None
        self._is_recording = False

        if not self._chunks:
            raise ValueError("No audio was captured – check your microphone")

        audio = np.concatenate(self._chunks, axis=0)

        # Stereo → mono
        if audio.ndim == 2 and audio.shape[1] > 1:
            audio = audio.mean(axis=1)

        # Downsample to 16 kHz if the hardware rate differs
        if self._hw_rate != TARGET_RATE:
            ratio = TARGET_RATE / self._hw_rate
            num_samples = int(len(audio) * ratio)
            indices = np.linspace(0, len(audio) - 1, num_samples).astype(int)
            audio = audio[indices]

        duration = len(audio) / TARGET_RATE
        if duration < MIN_RECORDING_SECONDS:
            raise ValueError("Recording too short – please speak for at least half a second")

        # Write to an in-memory WAV buffer
        buf = io.BytesIO()
        sf.write(buf, audio, TARGET_RATE, format="WAV")
        return buf.getvalue()

    # ── internals ───────────────────────────────────────────────

    def _audio_callback(
        self,
        indata: np.ndarray,
        frames: int,
        time_info: object,
        status: sd.CallbackFlags,
    ) -> None:
        """Called on a background thread by sounddevice for each audio block."""
        if status:
            from vibe.core.logger import logger
            logger.debug("audio status: %s", status)
        self._chunks.append(indata.copy())
        # Compute RMS for waveform visualisation
        mono = indata[:, 0] if indata.ndim == 2 else indata
        rms = float(np.sqrt(np.mean(mono ** 2)))
        self._levels.append(min(rms * 8.0, 1.0))
