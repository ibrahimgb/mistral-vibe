/**
 * VS Code Chat Participant that bridges @vibe to the ACP vibe-acp process.
 *
 * Handles:
 *  - Spawning / managing the ACP client lifecycle
 *  - Forwarding chat input to ACP prompt()
 *  - Streaming ACP session updates back as chat markdown
 */
import * as vscode from "vscode";
import { AcpClient } from "./acpClient";
declare let acpClient: AcpClient | null;
declare function ensureClient(): Promise<AcpClient>;
declare const outputChannel: vscode.OutputChannel;
declare function registerChatParticipant(context: vscode.ExtensionContext): vscode.Disposable;
export { registerChatParticipant, ensureClient, acpClient, outputChannel };
//# sourceMappingURL=chatParticipant.d.ts.map