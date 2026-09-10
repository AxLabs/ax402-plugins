---
name: ax402
description: >
  Manage Ax402 seller APIs and x402 payments via MCP tools. Use when wrapping
  an upstream API, pricing endpoints, inspecting HTTP 402 Payment Required,
  listing settlements, or the user mentions Ax402 / x402 / paid APIs.
---

# Ax402

Talk to the Ax402 control plane through MCP tools from `@ax402/mcp-server`.
Do not invent payment headers or facilitator URLs — use the tools.

Requires `AX402_API_KEY` (`ax402_live_...` or `ax402_test_...`) from
[the Ax402 dashboard](https://ax402.io). Optional `AX402_BASE_URL`
(default `https://api.ax402.io`). For Sandbox / Test mode use a test key
and `AX402_ENVIRONMENT=development` (or `AX402_SANDBOX=1`).

If tools fail with `AX402_API_KEY required`, follow the `setup` skill.

## Tool map

Seller (scoped by the API key):

| Tool | When |
|------|------|
| `ax402_list_apis` / `ax402_get_api` | Inventory |
| `ax402_create_api` | New wrap (`name`, `slug`, `upstream_base_url`) |
| `ax402_add_endpoint` | Price a route (`method`, `path_pattern`, `price_usdc`) |
| `ax402_import_openapi` | Bulk routes from an OpenAPI spec |
| `ax402_update_endpoint_schemas` | Request/response JSON Schema |
| `ax402_set_discovery_guidance` | Agent discovery copy on an API |
| `ax402_discovery_urls` | Gateway OpenAPI / `/.well-known/x402.json` |
| `ax402_add_domain` / `ax402_list_domains` / `ax402_verify_domain` | Custom hostname |
| `ax402_domain_suggest` | Hostname plan for an apex |
| `ax402_apis_slug_check` / `ax402_apis_probe_upstream` | Pre-create checks |
| `ax402_stats_overview` / `ax402_stats_api` | Analytics |
| `ax402_settlements_list` / `ax402_settlements_export` | Settlement history |
| `ax402_billing_overview` / `ax402_billing_catalog` / `ax402_income_summary` | Billing |
| `ax402_facilitator_stats` / `ax402_supported_networks` / `ax402_platform_config` | Platform |

Buyer (no seller key needed for inspect):

| Tool | When |
|------|------|
| `ax402_inspect_url` | Parse 402 requirements (read-only) |
| `ax402_pay_url` | Sign and retry. Needs wallet env — see below. |

## Rules

- Prefer MCP tools over guessing dashboard URLs or writing raw `PAYMENT-*` headers.
- `pay_to_address` / `pay_to_addresses` are CAIP-2 → recipient maps. Do not invent chain IDs or token addresses; use `ax402_supported_networks` and `ax402_platform_config`.
- Never print or log API keys or wallet private keys.
- Do not set `AX402_EVM_PRIVATE_KEY` / Hedera keys in chat. `ax402_pay_url` is opt-in via the user's local env.
- Sandbox wallet get/reset is CLI + JWT only — not available over MCP. Point the user at `ax402 --sandbox sandbox-wallet get`.
- Live keys (`ax402_live_...`) hit production. Test keys (`ax402_test_...`) hit Sandbox / Test mode.

## Typical flows

**Wrap and price**

1. `ax402_apis_slug_check` then `ax402_apis_probe_upstream`
2. `ax402_create_api`
3. `ax402_add_endpoint` or `ax402_import_openapi`
4. `ax402_discovery_urls` — give the user the gateway OpenAPI URL

**Debug a 402**

1. `ax402_inspect_url` on the resource URL
2. Summarize network, asset, amount, `payTo`, scheme
3. Do not call `ax402_pay_url` unless the user explicitly asks to pay and wallet env is already configured

Docs: https://ax402.io/docs/agents
