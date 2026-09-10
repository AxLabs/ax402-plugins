# ax402-plugins

Installable agent plugins for [Ax402](https://ax402.io). One plugin directory is loaded by Cursor, Grok Build, Claude Code, and Codex / ChatGPT desktop.

The MCP server is the published npm package [`@ax402/mcp-server`](https://www.npmjs.com/package/@ax402/mcp-server) (stdio). This repo is packaging + marketplace indexes, not a fork of the server.

```
plugins/ax402/          portable plugin (Agent Plugins 1.0 + client shims)
.cursor-plugin/         Cursor marketplace index
.claude-plugin/         Claude marketplace index
.grok-plugin/           Grok marketplace index
.agents/plugins/        ChatGPT / Codex marketplace index
```

## Install

Set `AX402_API_KEY` from the [Ax402 dashboard](https://ax402.io) first.

**Cursor** — submit/install from this repo, or locally:

```bash
ln -s /path/to/ax402-plugins/plugins/ax402 ~/.cursor/plugins/local/ax402
```

Then Customize → Configure the `AX402_API_KEY` variable. Official listing: [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish) (see [SUBMIT.md](SUBMIT.md)).

**Grok Build** — add this repo as a marketplace, then install:

```bash
grok plugin marketplace add AxLabs/ax402-plugins
grok plugin install ax402 --trust
```

**Claude Code**

```bash
claude plugin marketplace add AxLabs/ax402-plugins
claude plugin install ax402@ax402-plugins
```

**Codex / ChatGPT desktop** — add this repo (`codex plugin marketplace add AxLabs/ax402-plugins`) or point `.agents/plugins/marketplace.json` at `./plugins/ax402`. Public ChatGPT directory listing needs a hosted Streamable HTTP MCP; this package is local stdio.

**cursor.directory** — repo-root `.mcp.json` is for auto-detect. Submit at [cursor.directory/plugins/new](https://cursor.directory/plugins/new).

## Configure

| Variable | Required | Purpose |
|----------|----------|---------|
| `AX402_API_KEY` | Yes | `ax402_live_...` or `ax402_test_...` |
| `AX402_BASE_URL` | No | Default `https://api.ax402.io` |
| `AX402_ENVIRONMENT` | No | `development` for Sandbox / Test mode |

Wallet keys for `ax402_pay_url` stay in the user's environment, not in this plugin.

## One plugin, several manifests

Yes — skills, commands, and the MCP command are shared. Each client still wants its own tiny manifest:

| File | Who |
|------|-----|
| `plugin.json` + `mcp.json` | Agent Plugins 1.0 (Cursor, Codex, others) |
| `.cursor-plugin/plugin.json` | Cursor variables UI |
| `.grok-plugin/plugin.json` + `.mcp.json` | Grok Build |
| `.claude-plugin/plugin.json` + `.mcp.json` | Claude |
| `.codex-plugin/plugin.json` | Codex compatibility fallback |

Portable `mcp.json` does not embed API keys (Agent Plugins leaves unknown `${VAR}` placeholders literal). Cursor / Grok / Claude configs pass `AX402_API_KEY` through client-specific substitution.

## Validate

```bash
python3 scripts/validate.py
```

## License

Apache-2.0. MCP server: [AxLabs/ax402-sdks](https://github.com/AxLabs/ax402-sdks) (`tools/mcp-server`).
