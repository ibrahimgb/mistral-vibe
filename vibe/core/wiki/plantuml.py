"""PlantUML rendering utilities — local binary or public server fallback.

Provides :func:`render_plantuml` which takes PlantUML source text and
returns SVG (or PNG) bytes.  Prefers a locally-installed ``plantuml``
binary; falls back to the public PlantUML server.
"""

from __future__ import annotations

import asyncio
import shutil
import zlib
from pathlib import Path


# ---------------------------------------------------------------------------
# PlantUML text encoding (for server URLs)
# ---------------------------------------------------------------------------

_B64_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"


def _encode6bit(b: int) -> str:
    return _B64_CHARS[b & 0x3F]


def _append3bytes(b1: int, b2: int, b3: int) -> str:
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    return _encode6bit(c1) + _encode6bit(c2) + _encode6bit(c3) + _encode6bit(c4)


def plantuml_text_encode(text: str) -> str:
    """Encode PlantUML source into the URL-safe format used by the server."""
    compressed = zlib.compress(text.encode("utf-8"))[2:-4]  # raw deflate
    encoded = ""
    for i in range(0, len(compressed), 3):
        if i + 2 < len(compressed):
            encoded += _append3bytes(compressed[i], compressed[i + 1], compressed[i + 2])
        elif i + 1 < len(compressed):
            encoded += _append3bytes(compressed[i], compressed[i + 1], 0)
        else:
            encoded += _append3bytes(compressed[i], 0, 0)
    return encoded


# ---------------------------------------------------------------------------
# Rendering backends
# ---------------------------------------------------------------------------

_DEFAULT_SERVER = "https://www.plantuml.com/plantuml"


def has_local_plantuml() -> bool:
    """Return ``True`` if a ``plantuml`` binary is on ``$PATH``."""
    return shutil.which("plantuml") is not None


async def render_plantuml_local(
    source: str,
    output_path: Path,
    fmt: str = "svg",
) -> Path:
    """Render via the local ``plantuml`` CLI.

    Raises
    ------
    FileNotFoundError
        If ``plantuml`` is not installed.
    RuntimeError
        If the plantuml process exits non-zero.
    """
    if not has_local_plantuml():
        raise FileNotFoundError("plantuml binary not found on $PATH")

    proc = await asyncio.create_subprocess_exec(
        "plantuml", f"-t{fmt}", "-pipe",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate(input=source.encode("utf-8"))

    if proc.returncode != 0:
        raise RuntimeError(f"plantuml failed: {stderr.decode()}")

    out = output_path.with_suffix(f".{fmt}")
    out.write_bytes(stdout)
    return out


async def render_plantuml_server(
    source: str,
    output_path: Path,
    fmt: str = "svg",
    server: str = _DEFAULT_SERVER,
) -> Path:
    """Render via the public PlantUML server (HTTP GET).

    Raises
    ------
    RuntimeError
        If the server returns a non-200 status.
    """
    import httpx

    encoded = plantuml_text_encode(source)
    url = f"{server}/{fmt}/{encoded}"

    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            raise RuntimeError(f"PlantUML server returned {resp.status_code}: {resp.text[:200]}")

    out = output_path.with_suffix(f".{fmt}")
    out.write_bytes(resp.content)
    return out


async def render_plantuml(
    source: str,
    output_path: Path,
    fmt: str = "svg",
    server: str = _DEFAULT_SERVER,
) -> Path:
    """Render PlantUML source to a file, preferring local binary.

    Parameters
    ----------
    source:
        PlantUML diagram source text (including ``@startuml``/``@enduml``).
    output_path:
        Desired output path (extension will be replaced with *fmt*).
    fmt:
        Output format — ``"svg"`` (default) or ``"png"``.
    server:
        PlantUML server URL used as fallback.

    Returns
    -------
    Path:
        The path to the rendered file.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if has_local_plantuml():
        return await render_plantuml_local(source, output_path, fmt)
    return await render_plantuml_server(source, output_path, fmt, server)
