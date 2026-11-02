# Start here: give Claude access to your files and tools, safely

**What this does:** MCP lets Claude use other tools: read your files, look at GitHub, check a database. This kit gets your first one working in 30 minutes, in a safe test folder, so nothing important can break.

**What you'll have in 30 minutes:**

- ✅ Claude reading files from a folder you choose
- ✅ You knowing exactly what Claude can and can't touch
- ✅ The steps to add GitHub or a database next

**What you need:**

- [Node.js](https://nodejs.org/) installed (free)
- [Claude Code](https://code.claude.com/docs/en/overview) or [Claude Desktop](https://claude.ai/download)

## Step 1: Make a safe test folder (5 minutes)

1. Make a new, empty folder called `mcp-sandbox`.
2. Inside it, make a text file called `hello.txt`. Type: `first MCP test`
3. Find the folder's full path. Open a terminal in the folder and type `pwd` (Mac/Linux) or `cd` (Windows). Copy what it shows.

**Never point this at your home folder.** Use only this test folder.

## Step 2: Connect it (Claude Code)

In your terminal, paste this. Swap `/absolute/path/to/mcp-sandbox` for the path you just copied:

```bash
claude mcp add --transport stdio filesystem -- npx -y @modelcontextprotocol/server-filesystem /absolute/path/to/mcp-sandbox
claude mcp list
```

You should see `filesystem` in the list.

Using **Claude Desktop** instead? Follow [setup](01-connect-clients.md). It has the exact file to paste and you'll need to fully restart the app.

## Step 3: Test it

1. Type `claude` to start Claude Code.
2. Type `/mcp` to check it's connected.
3. Ask: **"Using the filesystem MCP tool, list files in my allowed sandbox and read hello.txt. Do not write anything."**

✅ **It works when** Claude names `hello.txt` and reads back "first MCP test".

If Claude asks permission to use a tool, read what it wants to do before you say yes.

## Important: this tool can write files

The file tool can also change and create files. That's why we use a throwaway test folder. Telling Claude "don't write" is not a lock. Only connect folders you're OK with it changing.

## What's next

[Setup](01-connect-clients.md) and the other chapters walk you through:

- Connecting GitHub
- Connecting a Postgres database
- Controlling what each tool can access
- Building your own tiny tool
- Fixing connection problems
- A worksheet to track what you've given access to

You don't need all of them. Pick one.

## If something goes wrong

| Problem | Fix |
|---|---|
| `npx: command not found` | Install [Node.js](https://nodejs.org/), then open a new terminal. |
| `filesystem` isn't in `claude mcp list` | Run the `claude mcp add` line again. Check the path has no typos. |
| Claude says it can't see the file | Make sure the path is the full path, and `hello.txt` is inside that folder. |

Stuck? Email support@milli-ai.com. If it's not working in 7 days, you get every dollar back, and you keep the files.
