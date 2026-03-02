/**
 * Voxtral transcription — mirrors vibe/core/voice/transcriber.py.
 *
 * Sends base64-encoded WAV to the Mistral Chat Completions API using the
 * voxtral-mini-latest model with an input_audio content block.
 */

import * as https from "https";
import * as vscode from "vscode";

const VOXTRAL_MODEL = "voxtral-mini-latest";
const MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions";

function getApiKey(): string {
  const config = vscode.workspace.getConfiguration("mistral-vibe");
  const configKey = config.get<string>("mistralApiKey");
  return configKey || process.env["MISTRAL_API_KEY"] || "";
}

/**
 * Transcribe WAV audio bytes using Voxtral.
 * Returns the transcription text.
 */
export async function transcribeAudio(wavBuffer: Buffer): Promise<string> {
  const apiKey = getApiKey();
  if (!apiKey) {
    throw new Error(
      "Mistral API key not configured. Set it in extension settings or MISTRAL_API_KEY env var."
    );
  }

  const audioB64 = wavBuffer.toString("base64");

  const body = JSON.stringify({
    model: VOXTRAL_MODEL,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "input_audio",
            input_audio: audioB64,
          },
          {
            type: "text",
            text: "Transcribe this audio exactly. Return only the transcription, nothing else.",
          },
        ],
      },
    ],
  });

  return new Promise((resolve, reject) => {
    const url = new URL(MISTRAL_API_URL);

    const req = https.request(
      {
        hostname: url.hostname,
        path: url.pathname,
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${apiKey}`,
          "Content-Length": Buffer.byteLength(body),
        },
      },
      (res) => {
        let data = "";
        res.on("data", (chunk) => (data += chunk));
        res.on("end", () => {
          if (res.statusCode !== 200) {
            reject(
              new Error(
                `Voxtral API error ${res.statusCode}: ${data.slice(0, 200)}`
              )
            );
            return;
          }

          try {
            const parsed = JSON.parse(data);
            const text = parsed?.choices?.[0]?.message?.content;
            if (typeof text !== "string") {
              reject(new Error("Unexpected Voxtral response structure"));
              return;
            }
            resolve(text.trim());
          } catch (e) {
            reject(new Error(`Failed to parse Voxtral response: ${e}`));
          }
        });
      }
    );

    req.on("error", reject);
    req.write(body);
    req.end();
  });
}
