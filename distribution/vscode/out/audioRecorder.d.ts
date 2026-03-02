/**
 * Audio recording via Node.js child process + sox/arecord.
 *
 * Since VS Code extensions run in Node.js (not a browser), we can't use
 * Web Audio API. Instead we shell out to a system recorder:
 *  - Linux:  arecord (ALSA)
 *  - macOS:  sox (rec)
 *  - Windows: sox (rec)
 *
 * Records 16 kHz mono WAV to a temp file, then reads it back as a Buffer.
 */
export type RecordingState = "idle" | "recording" | "transcribing";
export declare class AudioRecorder {
    private process;
    private tempFile;
    private _state;
    get state(): RecordingState;
    /** Start recording audio to a temp WAV file. */
    start(): void;
    /**
     * Stop recording and return the WAV bytes.
     * Returns null if recording failed.
     */
    stop(): Promise<Buffer | null>;
    /** Reset state back to idle (e.g., after transcription completes). */
    setIdle(): void;
    /** Forcibly cancel any in-progress recording. */
    cancel(): void;
}
//# sourceMappingURL=audioRecorder.d.ts.map