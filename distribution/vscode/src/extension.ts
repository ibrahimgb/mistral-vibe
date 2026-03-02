/**
 * Mistral Vibe VS Code Extension — entry point.
 *
 * Registers:
 *  1. @vibe Chat Participant (routes to vibe-acp over ACP)
 *  2. Status bar mic button  (records → transcribes via Voxtral → inserts into chat)
 *  3. Session management commands
 */

import * as vscode from "vscode";
import { AudioRecorder, RecordingState } from "./audioRecorder";
import { ensureClient, outputChannel, registerChatParticipant } from "./chatParticipant";
import { transcribeAudio } from "./transcriber";

let statusBarItem: vscode.StatusBarItem;
const recorder = new AudioRecorder();

// ---------------------------------------------------------------------------
// Status bar mic button
// ---------------------------------------------------------------------------

function updateStatusBar(state: RecordingState): void {
  switch (state) {
    case "idle":
      statusBarItem.text = "$(mic) Vibe Voice";
      statusBarItem.tooltip = "Click to start voice recording (Ctrl+R)";
      statusBarItem.backgroundColor = undefined;
      break;
    case "recording":
      statusBarItem.text = "$(circle-filled) Recording...";
      statusBarItem.tooltip = "Click to stop recording";
      statusBarItem.backgroundColor = new vscode.ThemeColor(
        "statusBarItem.errorBackground"
      );
      break;
    case "transcribing":
      statusBarItem.text = "$(loading~spin) Transcribing...";
      statusBarItem.tooltip = "Sending audio to Voxtral for transcription";
      statusBarItem.backgroundColor = new vscode.ThemeColor(
        "statusBarItem.warningBackground"
      );
      break;
  }
}

async function toggleRecording(): Promise<void> {
  if (recorder.state === "recording") {
    // Stop and transcribe
    updateStatusBar("transcribing");

    const wavBytes = await recorder.stop();
    if (!wavBytes) {
      vscode.window.showWarningMessage(
        "Recording too short or failed. Make sure arecord (Linux) or sox (macOS) is installed."
      );
      recorder.setIdle();
      updateStatusBar("idle");
      return;
    }

    try {
      const text = await transcribeAudio(wavBytes);
      recorder.setIdle();
      updateStatusBar("idle");

      if (text) {
        // Insert the transcribed text into VS Code's chat input by executing
        // the chat command with prefilled text
        await vscode.commands.executeCommand("workbench.action.chat.open", {
          query: `@vibe ${text}`,
        });
      }
    } catch (err) {
      recorder.setIdle();
      updateStatusBar("idle");
      vscode.window.showErrorMessage(`Transcription failed: ${err}`);
    }
  } else if (recorder.state === "idle") {
    // Start recording
    try {
      recorder.start();
      updateStatusBar("recording");
    } catch (err) {
      vscode.window.showErrorMessage(`Failed to start recording: ${err}`);
    }
  }
  // If transcribing, ignore clicks
}

// ---------------------------------------------------------------------------
// Session commands
// ---------------------------------------------------------------------------

async function listSessionsCommand(): Promise<void> {
  try {
    const client = await ensureClient();
    const cwd =
      vscode.workspace.workspaceFolders?.[0]?.uri.fsPath ?? process.cwd();
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
      vscode.window.showInformationMessage(
        `Resumed session: ${picked.label}`
      );
    }
  } catch (err) {
    vscode.window.showErrorMessage(`Failed to list sessions: ${err}`);
  }
}

async function newSessionCommand(): Promise<void> {
  try {
    const client = await ensureClient();
    const cwd =
      vscode.workspace.workspaceFolders?.[0]?.uri.fsPath ?? process.cwd();
    await client.newSession(cwd);
    vscode.window.showInformationMessage("New Vibe session created.");
  } catch (err) {
    vscode.window.showErrorMessage(`Failed to create session: ${err}`);
  }
}

// ---------------------------------------------------------------------------
// Mode / Model switching
// ---------------------------------------------------------------------------

async function switchModeCommand(): Promise<void> {
  try {
    const client = await ensureClient();
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
      if (modesState) modesState.currentModeId = picked.modeId;
      vscode.window.showInformationMessage(`Switched to mode: ${picked.label}`);
    }
  } catch (err) {
    vscode.window.showErrorMessage(`Failed to switch mode: ${err}`);
  }
}

async function switchModelCommand(): Promise<void> {
  try {
    const client = await ensureClient();
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
      if (modelsState) modelsState.currentModelId = picked.modelId;
      vscode.window.showInformationMessage(`Switched to model: ${picked.label}`);
    }
  } catch (err) {
    vscode.window.showErrorMessage(`Failed to switch model: ${err}`);
  }
}

// ---------------------------------------------------------------------------
// Activation / Deactivation
// ---------------------------------------------------------------------------

export function activate(context: vscode.ExtensionContext): void {
  outputChannel.appendLine("[vibe] Extension activating...");

  // Chat participant
  context.subscriptions.push(registerChatParticipant(context));

  // Status bar mic button
  statusBarItem = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Right,
    100
  );
  statusBarItem.command = "mistral-vibe.toggleRecording";
  updateStatusBar("idle");
  statusBarItem.show();
  context.subscriptions.push(statusBarItem);

  // Commands
  context.subscriptions.push(
    vscode.commands.registerCommand(
      "mistral-vibe.toggleRecording",
      toggleRecording
    ),
    vscode.commands.registerCommand(
      "mistral-vibe.listSessions",
      listSessionsCommand
    ),
    vscode.commands.registerCommand(
      "mistral-vibe.newSession",
      newSessionCommand
    ),
    vscode.commands.registerCommand(
      "mistral-vibe.switchMode",
      switchModeCommand
    ),
    vscode.commands.registerCommand(
      "mistral-vibe.switchModel",
      switchModelCommand
    )
  );

  // Cleanup recorder on deactivation
  context.subscriptions.push({
    dispose: () => recorder.cancel(),
  });

  outputChannel.appendLine("[vibe] Extension activated.");
}

export function deactivate(): void {
  recorder.cancel();
  outputChannel.appendLine("[vibe] Extension deactivated.");
}
