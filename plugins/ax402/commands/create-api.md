---
name: create-api
description: Create an Ax402 wrapped API with a default subdomain
---

Collect `name`, `slug`, and `upstream_base_url` from the user. Optionally `pay_to_address` / `pay_to_addresses` and discovery fields.

1. `ax402_apis_slug_check` on the slug
2. `ax402_apis_probe_upstream` on the upstream URL
3. `ax402_create_api`
4. `ax402_discovery_urls` and show the gateway OpenAPI URL

Stop and report if slug or upstream checks fail.
