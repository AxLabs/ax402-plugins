# Ax402 plugin

Agent plugin for the [Ax402](https://ax402.io) platform. Bundles `@ax402/mcp-server` (stdio via `npx`) plus skills and slash commands.

One package, four clients:

| Client | How it loads this folder |
|--------|--------------------------|
| Cursor | `.cursor-plugin/plugin.json` + `mcp.json` |
| Grok Build | `.grok-plugin/plugin.json` + `.mcp.json` |
| Claude Code / Cowork | `.claude-plugin/plugin.json` + `.mcp.json` |
| Codex / ChatGPT desktop | root `plugin.json` (Agent Plugins) + optional `.codex-plugin/` |

ChatGPT's **public** plugin directory wants a hosted Streamable HTTP MCP. This package is local stdio. Codex and ChatGPT desktop can still install it from this repo.

## Configure

Set `AX402_API_KEY` from the [Ax402 dashboard](https://ax402.io). Optional `AX402_BASE_URL` (default `https://api.ax402.io`).

Do not commit keys. Do not put wallet private keys in plugin config.

## Local test

```bash
# Cursor
ln -s "$(pwd)" ~/.cursor/plugins/local/ax402

# Grok
grok plugin install . --trust

# Claude
claude plugin validate .
```

Then reload the client and call `ax402_list_apis`.
