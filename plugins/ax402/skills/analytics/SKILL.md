---
name: analytics
description: >
  Analyze Ax402 traffic, settlements, batch activity, seller income, billing,
  webhook deliveries, or payout-request status.
---

# Analytics and operations

Prefer narrow date ranges and API filters. State whether results are
production or Sandbox.

| Need | Tool |
|------|------|
| Account traffic | `ax402_stats_overview` |
| One API's traffic | `ax402_stats_api` |
| API settlements | `ax402_settlements_list` |
| Batch settlements | `ax402_settlements_batch` |
| Paginated cross-API history | `ax402_settlements_history` |
| CSV/JSON history | `ax402_settlements_export` |
| Income totals | `ax402_income_summary` |
| Paginated income entries | `ax402_income_ledger` |
| Existing payout requests | `ax402_income_payout_requests` |
| Billing state | `ax402_billing_overview` |
| Facilitator aggregate stats | `ax402_facilitator_stats` |
| API webhook attempts | `ax402_webhook_deliveries` |
| Batch channel state | `ax402_batch_overview` |

For pagination, preserve `limit`, `offset`, API id, network, and date range in
the summary. Do not present atomic token amounts as decimal amounts unless
token decimals are known from returned metadata.

Creating/cancelling payouts, facilitator event logs, billing invoices, and
exchange-rate lookup are CLI-only in this plugin. Do not synthesize MCP calls
for them.
