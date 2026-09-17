---
name: inspect-pay
description: >
  Inspect or pay an HTTP 402 / x402 gateway URL. Use when diagnosing Payment
  Required, choosing a payment accept, or explicitly paying an Ax402 resource.
---

# Inspect and pay

Buyer calls target gateway hostnames, not the Ax402 control-plane API.

## Inspect first

Call `ax402_inspect_url` with the exact URL and HTTP method. Summarize each
accept:

- scheme
- network
- asset and atomic amount
- `payTo`
- timeout and transfer method when present

Inspection is read-only and needs no wallet.

## Pay

Call `ax402_pay_url` only when:

1. The user explicitly asks to pay.
2. The user confirms the selected amount, asset, network, recipient, URL,
   method, and scheme.
3. Wallet credentials are already present in the MCP host environment.

Never ask the user to paste a private key into chat. Never print keys. Do not
blindly retry a failed payment because a retry can create another authorization.

`ax402_pay_url` supports the SDK's EVM and Hedera wallet env. For Solana,
Permit2 approval, ERC-7710 grants, or advanced batch-channel management, use
the Simple Agent Wallet (`saw`) instead:

```bash
saw inspect URL
saw pay URL --confirm
```

The gateway handles facilitator verification and settlement; do not configure
or call a facilitator directly.
