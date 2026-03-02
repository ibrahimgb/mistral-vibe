/**
 * VS Code Chat Participant that bridges @vibe to the ACP vibe-acp process.
 *
 * Handles:
 *  - Spawning / managing the ACP client lifecycle
 *  - Forwarding chat input to ACP prompt()
 *  - Streaming ACP session updates back as chat markdown
 */

import * as vscode from "vscode";
import {
    AcpClient,
    AgentMessageChunk,
    AgentThoughtChunk,
    SessionUpdate,
} from "./acpClient";

let acpClient: AcpClient | null = null;

// ---------------------------------------------------------------------------
// ACP lifecycle helpers
// ---------------------------------------------------------------------------

function getVibeAcpPath(): string {
  const config = vscode.workspace.getConfiguration("mistral-vibe");
  return config.get<string>("vibeAcpPath") || "vibe-acp";
}

function getWorkspaceCwd(): string {
  const folders = vscode.workspace.workspaceFolders;
  return folders?.[0]?.uri.fsPath ?? process.cwd();
}

async function ensureClient(): Promise<AcpClient> {
  if (acpClient) return acpClient;

  const vibeAcpPath = getVibeAcpPath();
  const cwd = getWorkspaceCwd();

  const client = new AcpClient(vibeAcpPath, {});

  client.on("exit", (code: number | null) => {
    if (code !== 0 && code !== null) {
      vscode.window.showWarningMessage(
        `vibe-acp exited with code ${code}. Restart with a new message.`
      );
    }
    acpClient = null;
  });

  client.on("error", (err: Error) => {
    vscode.window.showErrorMessage(`vibe-acp error: ${err.message}`);
    acpClient = null;
  });

  client.on("log", (text: string) => {
    outputChannel.appendLine(`[vibe-acp] ${text.trimEnd()}`);
  });

  try {
    const initResult = await client.start(cwd);
    outputChannel.appendLine(
      `[vibe] Connected to ${initResult.agentInfo.name} v${initResult.agentInfo.version}`
    );
    outputChannel.appendLine(`[vibe] Workspace cwd: ${cwd}`);

    await client.newSession(cwd);
    outputChannel.appendLine(
      `[vibe] Session created: ${client.getSessionId()}`
    );

    acpClient = client;
    return client;
  } catch (err) {
    client.dispose();
    throw err;
  }
}

// ---------------------------------------------------------------------------
// Output channel for debug logs
// ---------------------------------------------------------------------------

const outputChannel = vscode.window.createOutputChannel("Mistral Vibe");

// ---------------------------------------------------------------------------
// Chat Participant
// ---------------------------------------------------------------------------

function registerChatParticipant(
  context: vscode.ExtensionContext
): vscode.Disposable {
  const participant = vscode.chat.createChatParticipant(
    "mistral-vibe.chat",
    chatHandler
  );

  participant.iconPath = vscode.Uri.joinPath(
    context.extensionUri,
    "icons",
    "mistral_vibe.png"
  );

  return participant;
}

async function chatHandler(
  request: vscode.ChatRequest,
  _context: vscode.ChatContext,
  stream: vscode.ChatResponseStream,
  token: vscode.CancellationToken
): Promise<vscode.ChatResult> {
  // If a slash command was used, convert it to /command format for ACP
  const slashCommand = request.command;
  const userText = request.prompt.trim();

  let userPrompt: string;
  if (slashCommand) {
    // e.g. command="clear" + prompt="" → "/clear"
    // e.g. command="proxy-setup" + prompt="HTTP_PROXY http://..." → "/proxy-setup HTTP_PROXY http://..."
    userPrompt = userText ? `/${slashCommand} ${userText}` : `/${slashCommand}`;
  } else {
    userPrompt = userText;
  }

  if (!userPrompt) {
    stream.markdown("Please enter a message.");
    return {};
  }

  let client: AcpClient;
  try {
    client = await ensureClient();
  } catch (err) {
    stream.markdown(
      `**Failed to start vibe-acp.** Make sure \`vibe-acp\` is installed and on your PATH.\n\n\`\`\`\n${err}\n\`\`\``
    );
    return {};
  }

  // Collect streaming updates
  let currentMarkdown = "";
  let thoughtMarkdown = "";

  const onUpdate = (update: SessionUpdate) => {
    switch (update.sessionUpdate) {
      case "agent_message_chunk": {
        const chunk = update as unknown as AgentMessageChunk;
        if (chunk.content?.text) {
          currentMarkdown += chunk.content.text;
          stream.markdown(chunk.content.text);
        }
        break;
      }
      case "agent_thought_chunk": {
        const thought = update as unknown as AgentThoughtChunk;
        if (thought.content?.text) {
          thoughtMarkdown += thought.content.text;
          // Show thoughts as progress
          stream.progress(thought.content.text.slice(0, 80));
        }
        break;
      }
      case "tool_call_update": {
        const toolUpdate = update as Record<string, unknown>;
        const toolCallId = toolUpdate["toolCallId"] as string;
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
    } catch {
      // ignore cancel errors
    }
  });

  try {
    const result = await client.prompt(userPrompt);

    if (result.stopReason === "cancelled") {
      stream.markdown("\n\n*Cancelled.*");
    }
  } catch (err) {
    stream.markdown(`\n\n**Error:** ${err}`);
  } finally {
    client.removeListener("sessionUpdate", onUpdate);
    cancelListener.dispose();
  }

  return {};
}

// ---------------------------------------------------------------------------
// Exports
// ---------------------------------------------------------------------------

export { acpClient, ensureClient, outputChannel, registerChatParticipant };

