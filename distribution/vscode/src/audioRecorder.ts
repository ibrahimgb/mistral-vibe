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

import { ChildProcessWithoutNullStreams, spawn } from "child_process";
import * as fs from "fs";
import * as os from "os";
import * as path from "path";

export type RecordingState = "idle" | "recording" | "transcribing";

export class AudioRecorder {
  private process: ChildProcessWithoutNullStreams | null = null;
  private tempFile: string = "";
  private _state: RecordingState = "idle";

  get state(): RecordingState {
    return this._state;
  }

  /** Start recording audio to a temp WAV file. */
  start(): void {
    if (this._state !== "idle") {
      throw new Error(`Cannot start: state is ${this._state}`);
    }

    this.tempFile = path.join(
      os.tmpdir(),
      `vibe-recording-${Date.now()}.wav`
    );

    const platform = os.platform();
    let cmd: string;
    let args: string[];

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
    } else if (platform === "darwin") {
      // sox's rec command
      cmd = "rec";
      args = [
        "-r", "16000",
        "-c", "1",
        "-b", "16",
        this.tempFile,
      ];
    } else {
      // Windows / fallback — try sox
      cmd = "sox";
      args = [
        "-d",              // default input device
        "-r", "16000",
        "-c", "1",
        "-b", "16",
        this.tempFile,
      ];
    }

    this.process = spawn(cmd, args, { stdio: ["pipe", "pipe", "pipe"] });
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
  async stop(): Promise<Buffer | null> {
    if (this._state !== "recording" || !this.process) {
      return null;
    }

    this._state = "transcribing";

    return new Promise((resolve) => {
      const proc = this.process!;

      proc.on("close", () => {
        try {
          if (fs.existsSync(this.tempFile)) {
            const wavBytes = fs.readFileSync(this.tempFile);
            fs.unlinkSync(this.tempFile);

            // Minimum sanity: at least 1KB (WAV header is 44 bytes)
            if (wavBytes.length > 1024) {
              resolve(wavBytes);
            } else {
              resolve(null);
            }
          } else {
            resolve(null);
          }
        } catch {
          resolve(null);
        }
      });

      // Send SIGINT to gracefully stop arecord/sox so it writes the WAV header
      proc.kill("SIGINT");
      this.process = null;
    });
  }

  /** Reset state back to idle (e.g., after transcription completes). */
  setIdle(): void {
    this._state = "idle";
  }

  /** Forcibly cancel any in-progress recording. */
  cancel(): void {
    if (this.process) {
      this.process.kill("SIGKILL");
      this.process = null;
    }
    if (this.tempFile && fs.existsSync(this.tempFile)) {
      try {
        fs.unlinkSync(this.tempFile);
      } catch {
        // ignore
      }
    }
    this._state = "idle";
  }
}
