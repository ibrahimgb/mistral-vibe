"use strict";
/**
 * ACP (Agent Client Protocol) client that communicates with vibe-acp over stdio.
 *
 * Speaks JSON-RPC 2.0: one JSON object per line, newline-delimited.
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
exports.AcpClient = void 0;
const child_process_1 = require("child_process");
const events_1 = require("events");
const readline = __importStar(require("readline"));
// ---------------------------------------------------------------------------
// AcpClient
// ---------------------------------------------------------------------------
class AcpClient extends events_1.EventEmitter {
    vibeAcpPath;
    env;
    process = null;
    nextId = 1;
    pending = new Map();
    sessionId = null;
    rl = null;
    currentModes = null;
    currentModels = null;
    constructor(vibeAcpPath, env = {}) {
        super();
        this.vibeAcpPath = vibeAcpPath;
        this.env = env;
    }
    /** Spawn vibe-acp and perform the ACP initialize handshake. */
    async start(cwd) {
        const spawnEnv = { ...process.env, ...this.env };
        this.process = (0, child_process_1.spawn)(this.vibeAcpPath, [], {
            cwd,
            stdio: ["pipe", "pipe", "pipe"],
            env: spawnEnv,
        });
        this.process.on("exit", (code) => {
            this.emit("exit", code);
        });
        this.process.on("error", (err) => {
            this.emit("error", err);
        });
        // Read stderr for debug logging
        this.process.stderr.on("data", (chunk) => {
            this.emit("log", chunk.toString());
        });
        // Line-delimited JSON-RPC on stdout
        this.rl = readline.createInterface({ input: this.process.stdout });
        this.rl.on("line", (line) => this.handleLine(line));
        // Initialize handshake
        const result = await this.send("initialize", {
            protocolVersion: 1,
            clientCapabilities: {
                terminal: true,
                fs: { readTextFile: true, writeTextFile: true },
            },
            clientInfo: {
                name: "vscode-mistral-vibe",
                version: "0.1.0",
            },
        });
        return result;
    }
    /** Create a new ACP session. */
    async newSession(cwd) {
        const result = await this.send("session/new", {
            cwd,
            mcpServers: [],
        });
        this.sessionId = result.sessionId;
        if (result.modes)
            this.currentModes = result.modes;
        if (result.models)
            this.currentModels = result.models;
        return result;
    }
    /** Load an existing session by ID. */
    async loadSession(cwd, sessionId) {
        const result = await this.send("session/load", {
            cwd,
            sessionId,
            mcpServers: [],
        });
        this.sessionId = sessionId;
        return result;
    }
    /** Send a prompt to the current session. Returns when the agent finishes. */
    async prompt(text) {
        if (!this.sessionId) {
            throw new Error("No active session. Call newSession() first.");
        }
        return this.send("session/prompt", {
            sessionId: this.sessionId,
            prompt: [{ type: "text", text }],
        });
    }
    /** Cancel a running prompt (sent as a JSON-RPC notification — no response expected). */
    cancel() {
        if (!this.sessionId)
            return;
        this.notify("session/cancel", { sessionId: this.sessionId });
    }
    /** List past sessions. */
    async listSessions(cwd) {
        return this.send("session/list", { cwd });
    }
    /** Set model. */
    async setModel(modelId) {
        if (!this.sessionId)
            return;
        await this.send("session/set_model", {
            sessionId: this.sessionId,
            modelId,
        });
    }
    /** Set mode (agent profile). */
    async setMode(modeId) {
        if (!this.sessionId)
            return;
        await this.send("session/set_mode", {
            sessionId: this.sessionId,
            modeId,
        });
    }
    /** Get current session ID. */
    getSessionId() {
        return this.sessionId;
    }
    /** Get available modes from the last session creation. */
    getModes() {
        return this.currentModes;
    }
    /** Get available models from the last session creation. */
    getModels() {
        return this.currentModels;
    }
    /** Shut down the vibe-acp process. */
    dispose() {
        this.pending.forEach(({ reject }) => reject(new Error("ACP client disposed")));
        this.pending.clear();
        this.rl?.close();
        this.rl = null;
        if (this.process) {
            this.process.kill();
            this.process = null;
        }
    }
    // -----------------------------------------------------------------------
    // Internal
    // -----------------------------------------------------------------------
    /** Send a JSON-RPC notification (fire-and-forget, no id, no response). */
    notify(method, params) {
        if (!this.process?.stdin.writable)
            return;
        const notification = { jsonrpc: "2.0", method, params };
        const line = JSON.stringify(notification) + "\n";
        this.process.stdin.write(line);
    }
    send(method, params) {
        return new Promise((resolve, reject) => {
            if (!this.process?.stdin.writable) {
                return reject(new Error("ACP process not running"));
            }
            const id = this.nextId++;
            this.pending.set(id, {
                resolve: resolve,
                reject,
            });
            const request = {
                jsonrpc: "2.0",
                id,
                method,
                params,
            };
            const line = JSON.stringify(request) + "\n";
            this.process.stdin.write(line);
        });
    }
    handleLine(raw) {
        const line = raw.trim();
        if (!line)
            return;
        let msg;
        try {
            msg = JSON.parse(line);
        }
        catch {
            // Not JSON — ignore (stderr bleed-through or log line)
            return;
        }
        // Server→client request (has both id AND method, e.g. session/request_permission)
        if ("id" in msg && "method" in msg && msg.id !== null && msg.id !== undefined) {
            this.handleNotification(msg);
            return;
        }
        // Response to a request we sent (has id but no method)
        if ("id" in msg && msg.id !== null && msg.id !== undefined) {
            const resp = msg;
            const pending = this.pending.get(resp.id);
            if (pending) {
                this.pending.delete(resp.id);
                if (resp.error) {
                    pending.reject(new Error(`ACP error ${resp.error.code}: ${resp.error.message}`));
                }
                else {
                    pending.resolve(resp.result);
                }
            }
            return;
        }
        // Notification (session update, permission request, etc.)
        if ("method" in msg) {
            const notif = msg;
            this.handleNotification(notif);
            return;
        }
    }
    handleNotification(notif) {
        const params = notif.params;
        switch (notif.method) {
            case "session/update": {
                const update = params?.["update"];
                if (update) {
                    this.emit("sessionUpdate", update);
                }
                break;
            }
            case "session/request_permission": {
                // For now, auto-approve. A proper implementation would show a VS Code dialog.
                this.handlePermissionRequest(notif);
                break;
            }
            default:
                this.emit("notification", notif);
        }
    }
    handlePermissionRequest(notif) {
        // The server sends a request (with id) for permission — respond with allow_once
        const raw = notif;
        if (!("id" in raw) || raw.id === null || raw.id === undefined)
            return;
        const response = {
            jsonrpc: "2.0",
            id: raw.id,
            result: {
                outcome: {
                    outcome: "selected",
                    optionId: "allow_once",
                },
            },
        };
        const line = JSON.stringify(response) + "\n";
        this.process?.stdin.write(line);
    }
}
exports.AcpClient = AcpClient;
//# sourceMappingURL=acpClient.js.map