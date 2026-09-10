---
name: inspect-url
description: Parse x402 / HTTP 402 payment requirements for a URL
---

Ask the user for the resource URL if they did not provide one. Call MCP tool `ax402_inspect_url`. Report network, asset, amount, `payTo`, scheme, and extra accepts. Do not pay unless the user explicitly asks.
