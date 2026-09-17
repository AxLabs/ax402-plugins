---
name: wrap-api
description: >
  Wrap an upstream HTTP API with an Ax402 payment gateway. Use when creating,
  updating, inspecting, or deleting an Ax402 API or configuring its payout,
  webhook, default subdomain, or unmatched-route proxying.
---

# Wrap an API

Use Ax402 MCP tools. Do not construct control-plane HTTP requests manually.

## Create

Collect:

- `name`, lowercase `slug`, and HTTPS `upstream_base_url`
- payout recipient when the account uses `user_wallet`
- optional webhook and discovery fields

Then:

1. Call `ax402_platform_config` for the current gateway hostname format.
2. Call `ax402_apis_slug_check`.
3. Create with `ax402_create_api`.
4. Call `ax402_apis_probe_upstream` using the returned API id.
5. Call `ax402_discovery_urls` and report the primary gateway and discovery URLs.

`pay_to_addresses` is a CAIP-2 network-to-recipient map. Obtain supported
networks from `ax402_supported_networks`; never invent chain IDs, assets, or
addresses.

## Update

Read current state with `ax402_get_api`, then pass only changed fields to
`ax402_update_api`. An empty `pay_to_addresses` object replaces and clears the
map; omission leaves it unchanged. `clear_webhook` removes webhook settings.

## Delete

Show the API name, id, gateway hosts, and affected endpoint count. Call
`ax402_delete_api` only after explicit user confirmation.

## CLI-only fallback

Authentication and API-key management require the CLI:

```bash
ax402 auth login ...
ax402 keys create ...
```

Never request passwords, JWTs, API keys, webhook secrets, or wallet keys in chat.
