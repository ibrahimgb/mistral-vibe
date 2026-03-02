"use strict";
/**
 * Mistral Vibe VS Code Extension — entry point.
 *
 * Registers:
 *  1. @vibe Chat Participant (routes to vibe-acp over ACP)
 *  2. Status bar mic button  (records → transcribes via Voxtral → inserts into chat)
 *  3. Session management commands
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
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const audioRecorder_1 = require("./audioRecorder");
const transcriber_1 = require("./transcriber");
const chatParticipant_1 = require("./chatParticipant");
let statusBarItem;
const recorder = new audioRecorder_1.AudioRecorder();
// ---------------------------------------------------------------------------
// Status bar mic button
// ---------------------------------------------------------------------------
function updateStatusBar(state) {
    switch (state) {
        case "idle":
            statusBarItem.text = "$(mic) Vibe Voice";
            statusBarItem.tooltip = "Click to start voice recording (Ctrl+R)";
            statusBarItem.backgroundColor = undefined;
            break;
        case "recording":
            statusBarItem.text = "$(circle-filled) Recording...";
            statusBarItem.tooltip = "Click to stop recording";
            statusBarItem.backgroundColor = new vscode.ThemeColor("statusBarItem.errorBackground");
            break;
        case "transcribing":
            statusBarItem.text = "$(loading~spin) Transcribing...";
            statusBarItem.tooltip = "Sending audio to Voxtral for transcription";
            statusBarItem.backgroundColor = new vscode.ThemeColor("statusBarItem.warningBackground");
            break;
    }
}
async function toggleRecording() {
    if (recorder.state === "recording") {
        // Stop and transcribe
        updateStatusBar("transcribing");
        const wavBytes = await recorder.stop();
        if (!wavBytes) {
            vscode.window.showWarningMessage("Recording too short or failed. Make sure arecord (Linux) or sox (macOS) is installed.");
            recorder.setIdle();
            updateStatusBar("idle");
            return;
        }
        try {
            const text = await (0, transcriber_1.transcribeAudio)(wavBytes);
            recorder.setIdle();
            updateStatusBar("idle");
            if (text) {
                // Insert the transcribed text into VS Code's chat input by executing
                // the chat command with prefilled text
                await vscode.commands.executeCommand("workbench.action.chat.open", {
                    query: `@vibe ${text}`,
                });
            }
        }
        catch (err) {
            recorder.setIdle();
            updateStatusBar("idle");
            vscode.window.showErrorMessage(`Transcription failed: ${err}`);
        }
    }
    else if (recorder.state === "idle") {
        // Start recording
        try {
            recorder.start();
            updateStatusBar("recording");
        }
        catch (err) {
            vscode.window.showErrorMessage(`Failed to start recording: ${err}`);
        }
    }
    // If transcribing, ignore clicks
}
// ---------------------------------------------------------------------------
// Session commands
// ---------------------------------------------------------------------------
async function listSessionsCommand() {
    try {
        const client = await (0, chatParticipant_1.ensureClient)();
        const cwd = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath ?? process.cwd();
        const result = await client.listSessions(cwd);
        if (!result.sessions.length) {
            vscode.window.showInformationMessage("No previous Vibe sessions found.");
            return;
        }
        const items = result.sessions.map((s) => ({
            label: s.title || s.sessionId,
            description: s.updatedAt
                ? new Date(s.updatedAt).toLocaleString()
                : undefined,
            detail: s.cwd,
            sessionId: s.sessionId,
        }));
        const picked = await vscode.window.showQuickPick(items, {
            placeHolder: "Select a session to resume",
        });
        if (picked) {
            await client.loadSession(cwd, picked.sessionId);
            vscode.window.showInformationMessage(`Resumed session: ${picked.label}`);
        }
    }
    catch (err) {
        vscode.window.showErrorMessage(`Failed to list sessions: ${err}`);
    }
}
async function newSessionCommand() {
    try {
        const client = await (0, chatParticipant_1.ensureClient)();
        const cwd = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath ?? process.cwd();
        await client.newSession(cwd);
        vscode.window.showInformationMessage("New Vibe session created.");
    }
    catch (err) {
        vscode.window.showErrorMessage(`Failed to create session: ${err}`);
    }
}
// ---------------------------------------------------------------------------
// Mode / Model switching
// ---------------------------------------------------------------------------
async function switchModeCommand() {
    try {
        const client = await (0, chatParticipant_1.ensureClient)();
        const modes = client.getModes();
        if (!modes || !modes.availableModes.length) {
            vscode.window.showInformationMessage("No modes available.");
            return;
        }
        const items = modes.availableModes.map((m) => ({
            label: m.name,
            description: m.id === modes.currentModeId ? "(active)" : "",
            detail: m.description,
            modeId: m.id,
        }));
        const picked = await vscode.window.showQuickPick(items, {
            placeHolder: `Current mode: ${modes.currentModeId} — select a new mode`,
        });
        if (picked && picked.modeId !== modes.currentModeId) {
            await client.setMode(picked.modeId);
            // Update local state
            const modesState = client.getModes();
            if (modesState)
                modesState.currentModeId = picked.modeId;
            vscode.window.showInformationMessage(`Switched to mode: ${picked.label}`);
        }
    }
    catch (err) {
        vscode.window.showErrorMessage(`Failed to switch mode: ${err}`);
    }
}
async function switchModelCommand() {
    try {
        const client = await (0, chatParticipant_1.ensureClient)();
        const models = client.getModels();
        if (!models || !models.availableModels.length) {
            vscode.window.showInformationMessage("No models available.");
            return;
        }
        const items = models.availableModels.map((m) => ({
            label: m.name,
            description: m.modelId === models.currentModelId ? "(active)" : "",
            modelId: m.modelId,
        }));
        const picked = await vscode.window.showQuickPick(items, {
            placeHolder: `Current model: ${models.currentModelId} — select a new model`,
        });
        if (picked && picked.modelId !== models.currentModelId) {
            await client.setModel(picked.modelId);
            const modelsState = client.getModels();
            if (modelsState)
                modelsState.currentModelId = picked.modelId;
            vscode.window.showInformationMessage(`Switched to model: ${picked.label}`);
        }
    }
    catch (err) {
        vscode.window.showErrorMessage(`Failed to switch model: ${err}`);
    }
}
// ---------------------------------------------------------------------------
// Activation / Deactivation
// ---------------------------------------------------------------------------
function activate(context) {
    chatParticipant_1.outputChannel.appendLine("[vibe] Extension activating...");
    // Chat participant
    context.subscriptions.push((0, chatParticipant_1.registerChatParticipant)(context));
    // Status bar mic button
    statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
    statusBarItem.command = "mistral-vibe.toggleRecording";
    updateStatusBar("idle");
    statusBarItem.show();
    context.subscriptions.push(statusBarItem);
    // Commands
    context.subscriptions.push(vscode.commands.registerCommand("mistral-vibe.toggleRecording", toggleRecording), vscode.commands.registerCommand("mistral-vibe.listSessions", listSessionsCommand), vscode.commands.registerCommand("mistral-vibe.newSession", newSessionCommand), vscode.commands.registerCommand("mistral-vibe.switchMode", switchModeCommand), vscode.commands.registerCommand("mistral-vibe.switchModel", switchModelCommand));
    // Cleanup recorder on deactivation
    context.subscriptions.push({
        dispose: () => recorder.cancel(),
    });
    chatParticipant_1.outputChannel.appendLine("[vibe] Extension activated.");
}
function deactivate() {
    recorder.cancel();
    chatParticipant_1.outputChannel.appendLine("[vibe] Extension deactivated.");
}
//# sourceMappingURL=extension.js.map