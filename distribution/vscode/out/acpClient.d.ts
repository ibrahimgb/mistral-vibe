/**
 * ACP (Agent Client Protocol) client that communicates with vibe-acp over stdio.
 *
 * Speaks JSON-RPC 2.0: one JSON object per line, newline-delimited.
 */
import { EventEmitter } from "events";
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
    content: Array<{
        type: string;
        content: TextContentBlock;
    }>;
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
    options?: Array<{
        id: string;
        label: string;
    }>;
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
    agentInfo: {
        name: string;
        title: string;
        version: string;
    };
    authMethods?: unknown[];
}
export declare class AcpClient extends EventEmitter {
    private readonly vibeAcpPath;
    private readonly env;
    private process;
    private nextId;
    private pending;
    private sessionId;
    private rl;
    private currentModes;
    private currentModels;
    constructor(vibeAcpPath: string, env?: Record<string, string>);
    /** Spawn vibe-acp and perform the ACP initialize handshake. */
    start(cwd: string): Promise<InitializeResult>;
    /** Create a new ACP session. */
    newSession(cwd: string): Promise<NewSessionResult>;
    /** Load an existing session by ID. */
    loadSession(cwd: string, sessionId: string): Promise<unknown>;
    /** Send a prompt to the current session. Returns when the agent finishes. */
    prompt(text: string): Promise<PromptResult>;
    /** Cancel a running prompt (sent as a JSON-RPC notification — no response expected). */
    cancel(): void;
    /** List past sessions. */
    listSessions(cwd?: string): Promise<ListSessionsResult>;
    /** Set model. */
    setModel(modelId: string): Promise<void>;
    /** Set mode (agent profile). */
    setMode(modeId: string): Promise<void>;
    /** Get current session ID. */
    getSessionId(): string | null;
    /** Get available modes from the last session creation. */
    getModes(): ModesState | null;
    /** Get available models from the last session creation. */
    getModels(): ModelsState | null;
    /** Shut down the vibe-acp process. */
    dispose(): void;
    /** Send a JSON-RPC notification (fire-and-forget, no id, no response). */
    private notify;
    private send;
    private handleLine;
    private handleNotification;
    private handlePermissionRequest;
}
//# sourceMappingURL=acpClient.d.ts.map