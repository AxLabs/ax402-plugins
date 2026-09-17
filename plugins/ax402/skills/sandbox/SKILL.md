---
name: sandbox
description: >
  Use Ax402 Sandbox / Test mode for APIs and x402 payments without real funds.
  Use when the user mentions ax402_sandbox keys, development mode, the Anvil
  fork, test payments, or the Sandbox wallet.
---

# Sandbox

Sandbox is the `development` control-plane environment and uses an
`ax402_sandbox_...` key.
The key prefix selects Sandbox; `AX402_ENVIRONMENT` / `AX402_SANDBOX` are optional.

```bash
export AX402_ENVIRONMENT=development
# or
export AX402_SANDBOX=1
```

The hosted fork network is `eip155:845320402`. Do not substitute public Base
or Base Sepolia. Obtain the current token, RPC, and gateway details from
`ax402_supported_networks` and `ax402_platform_config`; do not hardcode them
into mutations.

Sandbox endpoint defaults support `exact` only, not `batch-settlement`.

## Funded test wallet

Sandbox wallet retrieval is JWT-only and intentionally not exposed over MCP:

```bash
export AX402_JWT="$(ax402 auth login --email ... --password ...)"
ax402 --sandbox sandbox-wallet get --json --wait
```

The JSON output contains a private key. The user must run this locally and
place it in `AX402_EVM_PRIVATE_KEY`; never request or display it in chat.

Fork state is ephemeral and can be wiped by restarts. Do not treat Sandbox
transactions or balances as production state.
