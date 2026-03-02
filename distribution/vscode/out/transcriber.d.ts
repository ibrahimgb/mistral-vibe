/**
 * Voxtral transcription — mirrors vibe/core/voice/transcriber.py.
 *
 * Sends base64-encoded WAV to the Mistral Chat Completions API using the
 * voxtral-mini-latest model with an input_audio content block.
 */
/**
 * Transcribe WAV audio bytes using Voxtral.
 * Returns the transcription text.
 */
export declare function transcribeAudio(wavBuffer: Buffer): Promise<string>;
//# sourceMappingURL=transcriber.d.ts.map