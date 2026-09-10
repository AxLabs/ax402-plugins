---
name: setup
description: >
  Configure the Ax402 plugin MCP server (API key, base URL, sandbox vs live).
  Use on first install, when tools fail with AX402_API_KEY required, or when
  switching Sandbox and production.
---

# Ax402 plugin setup

The MCP server is `npx -y @ax402/mcp-server` (stdio). It reads env vars;
this plugin does not ship secrets.

## Required

1. Create a scoped API key in the [Ax402 dashboard](https://ax402.io).
2. Set `AX402_API_KEY` to that value (`ax402_live_...` or `ax402_sandbox_...`).
   An `ax402_sandbox_...` key selects Sandbox automatically; `AX402_ENVIRONMENT` is optional.

Optional:

| Variable | Default | When |
|----------|---------|------|
| `AX402_BASE_URL` | `https://api.ax402.io` | Staging / self-host |
| `AX402_ENVIRONMENT` | unset | `development` for Sandbox / Test mode |
| `AX402_SANDBOX` | unset | `1` / `true` — alias for development |

## Per client

- **Cursor:** Customize → plugin → Configure. Fill `AX402_API_KEY` (and optional base URL). Reload if tools stay missing.
- **Grok Build:** export the vars in the environment Grok inherits, or set them on the `ax402` MCP server (`grok mcp` / `/mcps`).
- **Claude Code:** export `AX402_API_KEY` in the shell that launches `claude`, then `/reload-plugins`.
- **Codex / ChatGPT desktop:** set `AX402_API_KEY` in the host environment before enabling the plugin. Public ChatGPT directory listing needs a hosted Streamable HTTP MCP (not this stdio package).

Restart / reload the client after changing env.

## Wallet pay (optional)

`ax402_pay_url` also needs `AX402_EVM_PRIVATE_KEY` and/or `HEDERA_ACCOUNT_ID` + `HEDERA_PRIVATE_KEY`. Do not put those in the plugin repo, chat, or git. Leave them unset unless the user is explicitly paying.

Sandbox wallet private keys are CLI + JWT only (`ax402 --sandbox sandbox-wallet get`).

## Check

Call `ax402_list_apis` or `ax402_platform_config`. Auth errors mean a bad key or the wrong `AX402_BASE_URL`.
