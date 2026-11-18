/**
 * Milli.ai MCP server: every Milli trader playbook as one connector link for Claude or ChatGPT.
 *
 * Transport: MCP "Streamable HTTP", stateless, JSON responses only (no SSE, no sessions).
 * Mount: router.use(mcpRouter) in routes/index.ts  → served at POST /api/mcp
 * Content: content/mcp/catalog.json + content/mcp/playbooks/<id>.md
 *
 * Read-only. No auth (public lead magnet). Never touches user data, money or orders.
 */
import { Router, type IRouter, type Request, type Response } from "express";
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { join, resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const SERVER_VERSION = "1.0.0";
const SUPPORTED_PROTOCOLS = ["2025-06-18", "2025-03-26", "2024-11-05"];
const SITE = "https://milli-ai.com";

type Playbook = { id: string; title: string; category: string; summary: string; body: string };

const INSTRUCTIONS = [
  "Milli.ai trader playbooks: tested workflows for traders who use AI (plans, bot audits, backtests of viral strategies, risk sizing, research, trading content).",
  "When the user asks for something a playbook covers, call get_playbook with its id, then follow the playbook exactly: ask its intake questions in ONE message, follow its process, and respect its hard rules.",
  "Call list_playbooks if you are not sure which one fits.",
  "Never invent prices, results or statistics. Never place trades. Everything is educational only, not financial advice.",
].join(" ");

// ---------- content loading ----------
function findContentDir(): string | null {
  // ESM bundle: no __dirname. Resolve from this module's URL (works in src/ and in dist/).
  let here = process.cwd();
  try { here = dirname(fileURLToPath(import.meta.url)); } catch { /* keep cwd */ }
  const candidates = [
    process.env.MCP_CONTENT_DIR,
    resolve(process.cwd(), "content/mcp"),
    resolve(process.cwd(), "artifacts/api-server/content/mcp"),
    resolve(here, "../content/mcp"),
    resolve(here, "../../content/mcp"),
    resolve(here, "../../../content/mcp"),
  ].filter(Boolean) as string[];
  return candidates.find((d) => existsSync(join(d, "catalog.json"))) ?? null;
}

let cache: { at: number; list: Playbook[] } | null = null;
function loadPlaybooks(): Playbook[] {
  if (cache && Date.now() - cache.at < 5 * 60_000) return cache.list;
  const dir = findContentDir();
  if (!dir) return [];
  const catalog = JSON.parse(readFileSync(join(dir, "catalog.json"), "utf8")) as Omit<Playbook, "body">[];
  const files = new Set(readdirSync(join(dir, "playbooks")));
  const list = catalog
    .filter((c) => files.has(`${c.id}.md`))
    .map((c) => {
      const raw = readFileSync(join(dir, "playbooks", `${c.id}.md`), "utf8");
      return { ...c, body: raw.replace(/^---\n[\s\S]*?\n---\n/, "").trim() };
    });
  cache = { at: Date.now(), list };
  return list;
}

const doc = (p: Playbook) => (p.body.startsWith("# ") ? p.body : `# ${p.title}\n\n${p.body}`);

const footer = (p: Playbook) =>
  `\n\n---\nPlaybook "${p.title}" from Milli.ai (${SITE}). Free guides and the downloadable Claude Code skill pack: ${SITE}/free. Educational only. Not financial advice.`;

function scoreMatch(p: Playbook, q: string): number {
  const words = q.toLowerCase().split(/[^a-z0-9$%]+/).filter((w) => w.length > 2);
  if (!words.length) return 0;
  const hay = `${p.id} ${p.title} ${p.category} ${p.summary}`.toLowerCase();
  const body = p.body.toLowerCase();
  return words.reduce((s, w) => s + (hay.includes(w) ? 3 : 0) + (body.includes(w) ? 1 : 0), 0);
}

// ---------- tools ----------
const TOOLS = [
  {
    name: "list_playbooks",
    title: "List Milli trader playbooks",
    description: "List every Milli.ai trader playbook (id, title, category, one-line summary). Optionally filter by category: plan, risk, test, research, review, build, content, mindset.",
    inputSchema: { type: "object", properties: { category: { type: "string", description: "Optional category filter" } }, additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "get_playbook",
    title: "Get a Milli trader playbook",
    description: "Get the full instructions for one playbook by id. Follow them exactly: intake questions in one message, the process, the output format and the hard rules.",
    inputSchema: { type: "object", properties: { id: { type: "string", description: "Playbook id from list_playbooks, e.g. bot-audit" } }, required: ["id"], additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "search",
    title: "Search playbooks",
    description: "Search Milli.ai trader playbooks by what the user wants to do. Returns matching playbook ids and titles.",
    inputSchema: { type: "object", properties: { query: { type: "string" } }, required: ["query"], additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "fetch",
    title: "Fetch a playbook",
    description: "Fetch one playbook's full text by id (same as get_playbook; provided for ChatGPT connectors).",
    inputSchema: { type: "object", properties: { id: { type: "string" } }, required: ["id"], additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
];

const text = (t: string, isError = false) => ({ content: [{ type: "text", text: t }], ...(isError ? { isError: true } : {}) });

function callTool(name: string, args: Record<string, unknown>) {
  const all = loadPlaybooks();
  const byId = (id: unknown) => all.find((p) => p.id === String(id ?? "").trim().toLowerCase());
  switch (name) {
    case "list_playbooks": {
      const cat = typeof args.category === "string" ? args.category.toLowerCase() : "";
      const rows = all.filter((p) => !cat || p.category === cat);
      return text(rows.map((p) => `- ${p.id} [${p.category}]: ${p.title}. ${p.summary}`).join("\n") || "No playbooks in that category.");
    }
    case "get_playbook": {
      const p = byId(args.id);
      if (!p) return text(`No playbook "${String(args.id)}". Call list_playbooks for valid ids.`, true);
      return text(`${doc(p)}${footer(p)}`);
    }
    case "search": {
      const q = String(args.query ?? "");
      const results = all
        .map((p) => ({ p, s: scoreMatch(p, q) }))
        .filter((x) => x.s > 0)
        .sort((a, b) => b.s - a.s)
        .slice(0, 8)
        .map(({ p }) => ({ id: p.id, title: p.title, url: `${SITE}/mcp#${p.id}` }));
      return text(JSON.stringify({ results }));
    }
    case "fetch": {
      const p = byId(args.id);
      if (!p) return text(`No playbook "${String(args.id)}".`, true);
      return text(JSON.stringify({ id: p.id, title: p.title, text: p.body + footer(p), url: `${SITE}/mcp#${p.id}`, metadata: { category: p.category } }));
    }
    default:
      return null;
  }
}

// ---------- JSON-RPC ----------
type RpcReq = { jsonrpc?: string; id?: string | number | null; method?: string; params?: Record<string, any> };
const ok = (id: RpcReq["id"], result: unknown) => ({ jsonrpc: "2.0", id, result });
const err = (id: RpcReq["id"], code: number, message: string) => ({ jsonrpc: "2.0", id: id ?? null, error: { code, message } });

export function handleRpc(m: RpcReq): object | null {
  if (!m || m.jsonrpc !== "2.0" || typeof m.method !== "string") return err(m?.id ?? null, -32600, "Invalid Request");
  const isNotification = m.id === undefined || m.id === null;
  if (isNotification) return null; // notifications/initialized, notifications/cancelled, etc.
  const p = m.params ?? {};
  const all = loadPlaybooks();
  switch (m.method) {
    case "initialize": {
      const asked = String(p.protocolVersion ?? "");
      return ok(m.id, {
        protocolVersion: SUPPORTED_PROTOCOLS.includes(asked) ? asked : SUPPORTED_PROTOCOLS[0],
        capabilities: { tools: { listChanged: false }, prompts: { listChanged: false }, resources: { listChanged: false } },
        serverInfo: { name: "milli-ai", title: "Milli.ai Trader Playbooks", version: SERVER_VERSION, websiteUrl: SITE },
        instructions: INSTRUCTIONS,
      });
    }
    case "ping":
      return ok(m.id, {});
    case "tools/list":
      return ok(m.id, { tools: TOOLS });
    case "tools/call": {
      const r = callTool(String(p.name ?? ""), (p.arguments ?? {}) as Record<string, unknown>);
      return r ? ok(m.id, r) : err(m.id, -32602, `Unknown tool: ${String(p.name)}`);
    }
    case "prompts/list":
      return ok(m.id, {
        prompts: all.map((pb) => ({
          name: pb.id, title: pb.title, description: pb.summary,
          arguments: [{ name: "request", description: "What you want, in your words (optional)", required: false }],
        })),
      });
    case "prompts/get": {
      const pb = all.find((x) => x.id === p.name);
      if (!pb) return err(m.id, -32602, `Unknown prompt: ${String(p.name)}`);
      const req = typeof p.arguments?.request === "string" && p.arguments.request.trim() ? `\n\nMy request: ${p.arguments.request.trim()}` : "";
      return ok(m.id, {
        description: pb.summary,
        messages: [{ role: "user", content: { type: "text", text: `Follow this playbook exactly.\n\n${doc(pb)}${footer(pb)}${req}` } }],
      });
    }
    case "resources/list":
      return ok(m.id, { resources: all.map((pb) => ({ uri: `milli://playbooks/${pb.id}`, name: pb.id, title: pb.title, description: pb.summary, mimeType: "text/markdown" })) });
    case "resources/templates/list":
      return ok(m.id, { resourceTemplates: [] });
    case "resources/read": {
      const id = String(p.uri ?? "").replace("milli://playbooks/", "");
      const pb = all.find((x) => x.id === id);
      if (!pb) return err(m.id, -32002, "Resource not found");
      return ok(m.id, { contents: [{ uri: `milli://playbooks/${pb.id}`, mimeType: "text/markdown", text: `${doc(pb)}${footer(pb)}` }] });
    }
    default:
      return err(m.id, -32601, `Method not found: ${m.method}`);
  }
}

// ---------- HTTP ----------
const router: IRouter = Router();

router.post("/mcp", (req: Request, res: Response) => {
  const body = req.body;
  if (body === undefined || body === null || (typeof body === "object" && !Array.isArray(body) && Object.keys(body).length === 0)) {
    res.status(400).json(err(null, -32700, "Parse error: send a JSON-RPC body with Content-Type: application/json"));
    return;
  }
  const msgs: RpcReq[] = Array.isArray(body) ? body : [body];
  const out = msgs.map(handleRpc).filter((x): x is object => x !== null);
  const first = msgs[0];
  if (first?.method === "tools/call") {
    (req as unknown as { log?: { info?: (o: object, m: string) => void } }).log?.info?.({ tool: first.params?.name, playbook: first.params?.arguments?.id ?? first.params?.arguments?.query }, "mcp tool call");
  }
  if (!out.length) { res.status(202).end(); return; } // only notifications/responses
  res.setHeader("MCP-Protocol-Version", String(req.get("mcp-protocol-version") ?? SUPPORTED_PROTOCOLS[0]));
  res.status(200).json(Array.isArray(body) ? out : out[0]);
});

// No server-initiated stream and no sessions: GET/DELETE are not offered (spec allows 405).
router.get("/mcp", (req: Request, res: Response) => {
  if ((req.get("accept") ?? "").includes("text/event-stream")) { res.setHeader("Allow", "POST"); res.status(405).end(); return; }
  res.json({
    name: "Milli.ai Trader Playbooks (MCP)",
    connect: `Add ${SITE}/api/mcp as a custom connector in Claude (Settings → Connectors) or ChatGPT (Settings → Apps & Connectors, developer mode).`,
    playbooks: loadPlaybooks().map((p) => ({ id: p.id, title: p.title, category: p.category })),
  });
});
router.delete("/mcp", (_req: Request, res: Response) => { res.setHeader("Allow", "POST"); res.status(405).end(); });

export default router;
