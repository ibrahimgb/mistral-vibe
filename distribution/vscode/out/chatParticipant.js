"use strict";
/**
 * VS Code Chat Participant that bridges @vibe to the ACP vibe-acp process.
 *
 * Handles:
 *  - Spawning / managing the ACP client lifecycle
 *  - Forwarding chat input to ACP prompt()
 *  - Streaming ACP session updates back as chat markdown
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
exports.outputChannel = exports.acpClient = void 0;
exports.registerChatParticipant = registerChatParticipant;
exports.ensureClient = ensureClient;
const vscode = __importStar(require("vscode"));
const acpClient_1 = require("./acpClient");
let acpClient = null;
exports.acpClient = acpClient;
// ---------------------------------------------------------------------------
// ACP lifecycle helpers
// ---------------------------------------------------------------------------
function getVibeAcpPath() {
    const config = vscode.workspace.getConfiguration("mistral-vibe");
    return config.get("vibeAcpPath") || "vibe-acp";
}
function getWorkspaceCwd() {
    const folders = vscode.workspace.workspaceFolders;
    return folders?.[0]?.uri.fsPath ?? process.cwd();
}
async function ensureClient() {
    if (acpClient)
        return acpClient;
    const vibeAcpPath = getVibeAcpPath();
    const cwd = getWorkspaceCwd();
    const client = new acpClient_1.AcpClient(vibeAcpPath, {});
    client.on("exit", (code) => {
        if (code !== 0 && code !== null) {
            vscode.window.showWarningMessage(`vibe-acp exited with code ${code}. Restart with a new message.`);
        }
        exports.acpClient = acpClient = null;
    });
    client.on("error", (err) => {
        vscode.window.showErrorMessage(`vibe-acp error: ${err.message}`);
        exports.acpClient = acpClient = null;
    });
    client.on("log", (text) => {
        outputChannel.appendLine(`[vibe-acp] ${text.trimEnd()}`);
    });
    try {
        const initResult = await client.start(cwd);
        outputChannel.appendLine(`[vibe] Connected to ${initResult.agentInfo.name} v${initResult.agentInfo.version}`);
        outputChannel.appendLine(`[vibe] Workspace cwd: ${cwd}`);
        await client.newSession(cwd);
        outputChannel.appendLine(`[vibe] Session created: ${client.getSessionId()}`);
        exports.acpClient = acpClient = client;
        return client;
    }
    catch (err) {
        client.dispose();
        throw err;
    }
}
// ---------------------------------------------------------------------------
// Output channel for debug logs
// ---------------------------------------------------------------------------
const outputChannel = vscode.window.createOutputChannel("Mistral Vibe");
exports.outputChannel = outputChannel;
// ---------------------------------------------------------------------------
// Chat Participant
// ---------------------------------------------------------------------------
function registerChatParticipant(context) {
    const participant = vscode.chat.createChatParticipant("mistral-vibe.chat", chatHandler);
    participant.iconPath = vscode.Uri.joinPath(context.extensionUri, "icons", "mistral_vibe.png");
    return participant;
}
async function chatHandler(request, _context, stream, token) {
    // If a slash command was used, convert it to /command format for ACP
    const slashCommand = request.command;
    const userText = request.prompt.trim();
    let userPrompt;
    if (slashCommand) {
        // e.g. command="clear" + prompt="" → "/clear"
        // e.g. command="proxy-setup" + prompt="HTTP_PROXY http://..." → "/proxy-setup HTTP_PROXY http://..."
        userPrompt = userText ? `/${slashCommand} ${userText}` : `/${slashCommand}`;
    }
    else {
        userPrompt = userText;
    }
    if (!userPrompt) {
        stream.markdown("Please enter a message.");
        return {};
    }
    let client;
    try {
        client = await ensureClient();
    }
    catch (err) {
        stream.markdown(`**Failed to start vibe-acp.** Make sure \`vibe-acp\` is installed and on your PATH.\n\n\`\`\`\n${err}\n\`\`\``);
        return {};
    }
    // Collect streaming updates
    let currentMarkdown = "";
    let thoughtMarkdown = "";
    const onUpdate = (update) => {
        switch (update.sessionUpdate) {
            case "agent_message_chunk": {
                const chunk = update;
                if (chunk.content?.text) {
                    currentMarkdown += chunk.content.text;
                    stream.markdown(chunk.content.text);
                }
                break;
            }
            case "agent_thought_chunk": {
                const thought = update;
                if (thought.content?.text) {
                    thoughtMarkdown += thought.content.text;
                    // Show thoughts as progress
                    stream.progress(thought.content.text.slice(0, 80));
                }
                break;
            }
            case "tool_call_update": {
                const toolUpdate = update;
                const toolCallId = toolUpdate["toolCallId"];
                stream.progress(`Running tool ${toolCallId}...`);
                break;
            }
            case "compact_start": {
                stream.progress("Compacting conversation...");
                break;
            }
            case "compact_end": {
                stream.progress("Conversation compacted.");
                break;
            }
        }
    };
    client.on("sessionUpdate", onUpdate);
    // Cancel support
    const cancelListener = token.onCancellationRequested(() => {
        try {
            client.cancel();
        }
        catch {
            // ignore cancel errors
        }
    });
    try {
        const result = await client.prompt(userPrompt);
        if (result.stopReason === "cancelled") {
            stream.markdown("\n\n*Cancelled.*");
        }
    }
    catch (err) {
        stream.markdown(`\n\n**Error:** ${err}`);
    }
    finally {
        client.removeListener("sessionUpdate", onUpdate);
        cancelListener.dispose();
    }
    return {};
}
//# sourceMappingURL=chatParticipant.js.map