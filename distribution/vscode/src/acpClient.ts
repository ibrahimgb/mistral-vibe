/**
 * ACP (Agent Client Protocol) client that communicates with vibe-acp over stdio.
 *
 * Speaks JSON-RPC 2.0: one JSON object per line, newline-delimited.
 */

import { ChildProcessWithoutNullStreams, spawn } from "child_process";
import { EventEmitter } from "events";
import * as readline from "readline";

// ---------------------------------------------------------------------------
// JSON-RPC types
// ---------------------------------------------------------------------------

interface JsonRpcRequest {
  jsonrpc: "2.0";
  id: number;
  method: string;
  params?: unknown;
}

interface JsonRpcResponse {
  jsonrpc: "2.0";
  id: number | null;
  result?: unknown;
  error?: { code: number; message: string; data?: unknown };
}

interface JsonRpcNotification {
  jsonrpc: "2.0";
  method: string;
  params?: unknown;
}

type JsonRpcMessage = JsonRpcResponse | JsonRpcNotification;

// ---------------------------------------------------------------------------
// ACP-specific types
// ---------------------------------------------------------------------------

export interface TextContentBlock {
  type: "text";
  text: string;
}

export interface AgentMessageChunk {
  sessionUpdate: "agent_message_chunk";
  content: TextContentBlock;
  _meta?: Record<string, unknown>;
}

export interface AgentThoughtChunk {
  sessionUpdate: "agent_thought_chunk";
  content: TextContentBlock;
  _meta?: Record<string, unknown>;
}

export interface ToolCallUpdate {
  sessionUpdate: "tool_call_update";
  toolCallId: string;
  content: Array<{ type: string; content: TextContentBlock }>;
}

export interface SessionUpdate {
  sessionUpdate: string;
  [key: string]: unknown;
}

export interface SessionInfo {
  sessionId: string;
  cwd?: string;
  title?: string;
  updatedAt?: string;
}

export interface ConfigOption {
  configId: string;
  displayName: string;
  type: string;
  options?: Array<{ id: string; label: string }>;
  value?: string;
}

export interface ModeInfo {
  id: string;
  name: string;
  description?: string;
}

export interface ModelInfo {
  modelId: string;
  name: string;
}

export interface ModesState {
  availableModes: ModeInfo[];
  currentModeId: string;
}

export interface ModelsState {
  availableModels: ModelInfo[];
  currentModelId: string;
}

export interface NewSessionResult {
  sessionId: string;
  models?: ModelsState;
  modes?: ModesState;
  configOptions?: ConfigOption[];
}

export interface PromptResult {
  stopReason: string;
}

export interface ListSessionsResult {
  sessions: SessionInfo[];
}

export interface InitializeResult {
  agentCapabilities: unknown;
  protocolVersion: number;
  agentInfo: { name: string; title: string; version: string };
  authMethods?: unknown[];
}

// ---------------------------------------------------------------------------
// Pending request tracker
// ---------------------------------------------------------------------------

interface PendingRequest {
  resolve: (value: unknown) => void;
  reject: (reason: Error) => void;
}

// ---------------------------------------------------------------------------
// AcpClient
// ---------------------------------------------------------------------------

export class AcpClient extends EventEmitter {
  private process: ChildProcessWithoutNullStreams | null = null;
  private nextId = 1;
  private pending = new Map<number, PendingRequest>();
  private sessionId: string | null = null;
  private rl: readline.Interface | null = null;
  private currentModes: ModesState | null = null;
  private currentModels: ModelsState | null = null;

  constructor(
    private readonly vibeAcpPath: string,
    private readonly env: Record<string, string> = {}
  ) {
    super();
  }

  /** Spawn vibe-acp and perform the ACP initialize handshake. */
  async start(cwd: string): Promise<InitializeResult> {
    const spawnEnv = { ...process.env, ...this.env };

    this.process = spawn(this.vibeAcpPath, [], {
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
    this.process.stderr.on("data", (chunk: Buffer) => {
      this.emit("log", chunk.toString());
    });

    // Line-delimited JSON-RPC on stdout
    this.rl = readline.createInterface({ input: this.process.stdout });
    this.rl.on("line", (line) => this.handleLine(line));

    // Initialize handshake
    const result = await this.send<InitializeResult>("initialize", {
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
  async newSession(cwd: string): Promise<NewSessionResult> {
    const result = await this.send<NewSessionResult>("session/new", {
      cwd,
      mcpServers: [],
    });
    this.sessionId = result.sessionId;
    if (result.modes) this.currentModes = result.modes;
    if (result.models) this.currentModels = result.models;
    return result;
  }

  /** Load an existing session by ID. */
  async loadSession(cwd: string, sessionId: string): Promise<unknown> {
    const result = await this.send("session/load", {
      cwd,
      sessionId,
      mcpServers: [],
    });
    this.sessionId = sessionId;
    return result;
  }

  /** Send a prompt to the current session. Returns when the agent finishes. */
  async prompt(text: string): Promise<PromptResult> {
    if (!this.sessionId) {
      throw new Error("No active session. Call newSession() first.");
    }

    return this.send<PromptResult>("session/prompt", {
      sessionId: this.sessionId,
      prompt: [{ type: "text", text }],
    });
  }

  /** Cancel a running prompt (sent as a JSON-RPC notification — no response expected). */
  cancel(): void {
    if (!this.sessionId) return;
    this.notify("session/cancel", { sessionId: this.sessionId });
  }

  /** List past sessions. */
  async listSessions(cwd?: string): Promise<ListSessionsResult> {
    return this.send<ListSessionsResult>("session/list", { cwd });
  }

  /** Set model. */
  async setModel(modelId: string): Promise<void> {
    if (!this.sessionId) return;
    await this.send("session/set_model", {
      sessionId: this.sessionId,
      modelId,
    });
  }

  /** Set mode (agent profile). */
  async setMode(modeId: string): Promise<void> {
    if (!this.sessionId) return;
    await this.send("session/set_mode", {
      sessionId: this.sessionId,
      modeId,
    });
  }

  /** Get current session ID. */
  getSessionId(): string | null {
    return this.sessionId;
  }

  /** Get available modes from the last session creation. */
  getModes(): ModesState | null {
    return this.currentModes;
  }

  /** Get available models from the last session creation. */
  getModels(): ModelsState | null {
    return this.currentModels;
  }

  /** Shut down the vibe-acp process. */
  dispose(): void {
    this.pending.forEach(({ reject }) =>
      reject(new Error("ACP client disposed"))
    );
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
  private notify(method: string, params?: unknown): void {
    if (!this.process?.stdin.writable) return;

    const notification = { jsonrpc: "2.0" as const, method, params };
    const line = JSON.stringify(notification) + "\n";
    this.process.stdin.write(line);
  }

  private send<T = unknown>(method: string, params?: unknown): Promise<T> {
    return new Promise((resolve, reject) => {
      if (!this.process?.stdin.writable) {
        return reject(new Error("ACP process not running"));
      }

      const id = this.nextId++;
      this.pending.set(id, {
        resolve: resolve as (v: unknown) => void,
        reject,
      });

      const request: JsonRpcRequest = {
        jsonrpc: "2.0",
        id,
        method,
        params,
      };

      const line = JSON.stringify(request) + "\n";
      this.process.stdin.write(line);
    });
  }

  private handleLine(raw: string): void {
    const line = raw.trim();
    if (!line) return;

    let msg: JsonRpcMessage;
    try {
      msg = JSON.parse(line);
    } catch {
      // Not JSON — ignore (stderr bleed-through or log line)
      return;
    }

    // Server→client request (has both id AND method, e.g. session/request_permission)
    if ("id" in msg && "method" in msg && msg.id !== null && msg.id !== undefined) {
      this.handleNotification(msg as JsonRpcNotification);
      return;
    }

    // Response to a request we sent (has id but no method)
    if ("id" in msg && msg.id !== null && msg.id !== undefined) {
      const resp = msg as JsonRpcResponse;
      const pending = this.pending.get(resp.id as number);
      if (pending) {
        this.pending.delete(resp.id as number);
        if (resp.error) {
          pending.reject(
            new Error(`ACP error ${resp.error.code}: ${resp.error.message}`)
          );
        } else {
          pending.resolve(resp.result);
        }
      }
      return;
    }

    // Notification (session update, permission request, etc.)
    if ("method" in msg) {
      const notif = msg as JsonRpcNotification;
      this.handleNotification(notif);
      return;
    }
  }

  private handleNotification(notif: JsonRpcNotification): void {
    const params = notif.params as Record<string, unknown> | undefined;

    switch (notif.method) {
      case "session/update": {
        const update = params?.["update"] as SessionUpdate | undefined;
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

  private handlePermissionRequest(notif: JsonRpcNotification): void {
    // The server sends a request (with id) for permission — respond with allow_once
    const raw = notif as unknown as JsonRpcResponse;
    if (!("id" in raw) || raw.id === null || raw.id === undefined) return;

    const response = {
      jsonrpc: "2.0" as const,
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
