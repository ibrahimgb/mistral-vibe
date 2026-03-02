"use strict";
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
exports.AudioRecorder = void 0;
const child_process_1 = require("child_process");
const fs = __importStar(require("fs"));
const os = __importStar(require("os"));
const path = __importStar(require("path"));
class AudioRecorder {
    process = null;
    tempFile = "";
    _state = "idle";
    get state() {
        return this._state;
    }
    /** Start recording audio to a temp WAV file. */
    start() {
        if (this._state !== "idle") {
            throw new Error(`Cannot start: state is ${this._state}`);
        }
        this.tempFile = path.join(os.tmpdir(), `vibe-recording-${Date.now()}.wav`);
        const platform = os.platform();
        let cmd;
        let args;
        if (platform === "linux") {
            // arecord: ALSA recorder, 16kHz mono 16-bit WAV
            cmd = "arecord";
            args = [
                "-f", "S16_LE",
                "-r", "16000",
                "-c", "1",
                "-t", "wav",
                this.tempFile,
            ];
        }
        else if (platform === "darwin") {
            // sox's rec command
            cmd = "rec";
            args = [
                "-r", "16000",
                "-c", "1",
                "-b", "16",
                this.tempFile,
            ];
        }
        else {
            // Windows / fallback — try sox
            cmd = "sox";
            args = [
                "-d", // default input device
                "-r", "16000",
                "-c", "1",
                "-b", "16",
                this.tempFile,
            ];
        }
        this.process = (0, child_process_1.spawn)(cmd, args, { stdio: ["pipe", "pipe", "pipe"] });
        this._state = "recording";
        this.process.on("error", (err) => {
            console.error(`Recording process error: ${err.message}`);
            this._state = "idle";
        });
    }
    /**
     * Stop recording and return the WAV bytes.
     * Returns null if recording failed.
     */
    async stop() {
        if (this._state !== "recording" || !this.process) {
            return null;
        }
        this._state = "transcribing";
        return new Promise((resolve) => {
            const proc = this.process;
            proc.on("close", () => {
                try {
                    if (fs.existsSync(this.tempFile)) {
                        const wavBytes = fs.readFileSync(this.tempFile);
                        fs.unlinkSync(this.tempFile);
                        // Minimum sanity: at least 1KB (WAV header is 44 bytes)
                        if (wavBytes.length > 1024) {
                            resolve(wavBytes);
                        }
                        else {
                            resolve(null);
                        }
                    }
                    else {
                        resolve(null);
                    }
                }
                catch {
                    resolve(null);
                }
            });
            // Send SIGINT to gracefully stop arecord/sox so it writes the WAV header
            proc.kill("SIGINT");
            this.process = null;
        });
    }
    /** Reset state back to idle (e.g., after transcription completes). */
    setIdle() {
        this._state = "idle";
    }
    /** Forcibly cancel any in-progress recording. */
    cancel() {
        if (this.process) {
            this.process.kill("SIGKILL");
            this.process = null;
        }
        if (this.tempFile && fs.existsSync(this.tempFile)) {
            try {
                fs.unlinkSync(this.tempFile);
            }
            catch {
                // ignore
            }
        }
        this._state = "idle";
    }
}
exports.AudioRecorder = AudioRecorder;
//# sourceMappingURL=audioRecorder.js.map