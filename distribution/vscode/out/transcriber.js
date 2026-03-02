"use strict";
/**
 * Voxtral transcription — mirrors vibe/core/voice/transcriber.py.
 *
 * Sends base64-encoded WAV to the Mistral Chat Completions API using the
 * voxtral-mini-latest model with an input_audio content block.
 */
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.transcribeAudio = transcribeAudio;
const https = __importStar(require("https"));
const vscode = __importStar(require("vscode"));
const VOXTRAL_MODEL = "voxtral-mini-latest";
const MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions";
function getApiKey() {
    const config = vscode.workspace.getConfiguration("mistral-vibe");
    const configKey = config.get("mistralApiKey");
    return configKey || process.env["MISTRAL_API_KEY"] || "";
}
/**
 * Transcribe WAV audio bytes using Voxtral.
 * Returns the transcription text.
 */
async function transcribeAudio(wavBuffer) {
    const apiKey = getApiKey();
    if (!apiKey) {
        throw new Error("Mistral API key not configured. Set it in extension settings or MISTRAL_API_KEY env var.");
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
        const req = https.request({
            hostname: url.hostname,
            path: url.pathname,
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${apiKey}`,
                "Content-Length": Buffer.byteLength(body),
            },
        }, (res) => {
            let data = "";
            res.on("data", (chunk) => (data += chunk));
            res.on("end", () => {
                if (res.statusCode !== 200) {
                    reject(new Error(`Voxtral API error ${res.statusCode}: ${data.slice(0, 200)}`));
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
                }
                catch (e) {
                    reject(new Error(`Failed to parse Voxtral response: ${e}`));
                }
            });
        });
        req.on("error", reject);
        req.write(body);
        req.end();
    });
}
//# sourceMappingURL=transcriber.js.map