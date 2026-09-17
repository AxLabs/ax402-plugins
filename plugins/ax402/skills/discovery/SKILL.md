---
name: discovery
description: >
  Publish and validate Ax402 API discovery metadata. Use for gateway
  openapi.json, /.well-known/x402.json, AgentCash discovery, guidance,
  contact email, OpenAPI version, or endpoint schemas.
---

# API discovery

Discovery documents are public, unpaid gateway routes generated from live API
and endpoint configuration:

- `https://{gateway-host}/openapi.json`
- `https://{gateway-host}/.well-known/x402.json`

Use `ax402_discovery_urls` to obtain exact URLs. Never derive the hostname by
guessing.

## Improve discovery

1. Read the API and endpoints.
2. Set API-level guidance, contact email, or version with
   `ax402_set_discovery_guidance`.
3. Set meaningful endpoint request/response schemas with
   `ax402_update_endpoint_schemas` or `ax402_update_endpoint`.
4. Fetch fresh URLs with `ax402_discovery_urls`.

Disabled and ephemeral endpoints are omitted from discovery.

## Validate

The AgentCash checker is CLI-only:

```bash
npx -y @agentcash/discovery@latest check "https://gateway.example/"
npx -y @agentcash/discovery@latest discover "https://gateway.example/"
```

Run it only against a URL returned by `ax402_discovery_urls`. Report validation
failures without silently rewriting schemas or guidance.
