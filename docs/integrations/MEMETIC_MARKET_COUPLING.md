# Integration — Memetic ↔ Market Coupling

Join **narrative memetic velocity** (signal-envelope stream items) with **fin-crypto market snapshots** (CCXT adapter) on a shared `story_id` or instrument symbol mapping.

**Epistemic label:** `INSTITUTIONAL_MODEL` for coupling framing; underlying adapter records remain `OPERATIONAL`.

## Purpose

Contour 5 in [`MEMETIC_DYNAMICS.md`](MEMETIC_DYNAMICS.md) — modeled coupling between discourse propagation metrics and market context signals. This is **not** a trading recommendation, legal verdict, or sovereignty claim.

## Join keys

| Priority | Key | When |
|----------|-----|------|
| 1 | `story_id` | Explicit politic.bar / cross-layer story anchor on both sides |
| 2 | `symbol` | Instrument slug mapping when no shared story (default: `fin-crypto-{symbol-normalized}-snapshot`) |

Symbol normalization: `BTC/USDT` → story slug `fin-crypto-btc-usdt-snapshot`; instrument field uses `BTC-USDT`.

## Event type

| `event_type` | Default activated layers | Epistemic label |
|--------------|---------------------------|-----------------|
| `memetic_market_coupling_snapshot` | `institution:central-bank-analog`, `institution:parliament`, `institution:regulatory-agency` | `INSTITUTIONAL_MODEL` |

Routing: `errorlogy-mas/mas/institutional/activation.py` — prefix `memetic_market_` (longest match before `memetic_`).

## Coupling join record (adapter output)

Returned alongside the cross-layer envelope by `POST /api/events/memetic/market-coupling`:

```json
{
  "coupling_id": "memetic_market_coupling:{digest}",
  "event_type": "memetic_market_coupling_snapshot",
  "observed_at": "2026-08-29T12:00:00+00:00",
  "join_key": { "type": "story_id", "value": "fin-crypto-btc-usdt-snapshot" },
  "story_id": "fin-crypto-btc-usdt-snapshot",
  "market_record": { },
  "memetic_sidecar": {
    "stream_item_id": "si-join-btc",
    "story_id": "fin-crypto-btc-usdt-snapshot",
    "peak_velocity": 120.0,
    "decay_tau_hours": 48.0,
    "first_seen": "2026-08-29T06:00:00+00:00"
  },
  "epistemic_label": "INSTITUTIONAL_MODEL",
  "quality_flags": ["institutional_model_join"]
}
```

`market_record` follows the normalized shape in [`FIN_CRYPTO_MARKETS.md`](FIN_CRYPTO_MARKETS.md) (`fin_crypto_market_snapshot` or `fin_crypto_data_unavailable`).

`memetic_sidecar` fields align with [`schemas/signal-envelope.json`](../../schemas/signal-envelope.json) `memetic_metrics` plus `stream_item_id`.

### Quality flags

| Flag | Meaning |
|------|---------|
| `institutional_model_join` | Always present — coupling is modeled context |
| `memetic_sidecar_missing` | Market-only join; no velocity sidecar supplied |
| `market_partial` | Upstream market record is `fin_crypto_data_unavailable` |
| `decay_tau_estimated_missing` | Sidecar present but `decay_tau_hours` not computed |

## Cross-layer envelope

Standard umbrella [`cross-layer-event.json`](../../schemas/cross-layer-event.json) fields only (no extra properties on persist):

```json
{
  "story_id": "fin-crypto-btc-usdt-snapshot",
  "event_type": "memetic_market_coupling_snapshot",
  "activated_layers": [
    "institution:central-bank-analog",
    "institution:parliament",
    "institution:regulatory-agency"
  ],
  "stream_refs": [
    "ccxt:market_snapshot:abc123",
    "si-join-btc"
  ],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

`stream_refs` lists the market `record_id` and memetic `stream_item_id` when available.

## Runtime owners

| Component | Repo | Path |
|-----------|------|------|
| Coupling adapter + API | errorlogy-mas | `mas/memetic/market_coupling.py`, `POST /api/events/memetic/market-coupling` |
| CCXT market snapshot (iter 3) | errorlogy-mas | `mas/adapters/fin_crypto_ccxt.py`, `POST /api/events/fin-crypto/snapshot` |
| Memetic sidecar stub | politic-bar | `politic_bar/memetic_market_join.py` (reuses `half_life_indexer`) |
| Contracts + schema | ai-native-gov | this doc, `cross-layer-event.json`, `signal-envelope.json` |

## API (errorlogy-mas)

```bash
curl -s -X POST "http://127.0.0.1:8000/api/events/memetic/market-coupling" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "BTC/USDT",
    "exchange": "binance",
    "story_id": "fin-crypto-btc-usdt-snapshot",
    "stream_item_id": "si-join-btc",
    "peak_velocity": 120.0,
    "decay_tau_hours": 48.0
  }'
```

Optional: pass `market_record` to skip CCXT fetch; pass `jurisdiction_set` for cross-border framing.

## Guardrails

- Market-data only — no order placement, balances, or private exchange endpoints.
- No new taxonomy mode IDs (CB-/HM-/PNO-).
- Do not label coupling as `COMPUTATIONAL_EVIDENCE` unless a NAMM `certificate_ref` is linked.
- Language: **legitimacy signals (modeled)**, analytical contribution — not guilty/criminal/proven guilt.

## Related

- [`FIN_CRYPTO_MARKETS.md`](FIN_CRYPTO_MARKETS.md) — market adapter contract
- [`MEMETIC_DYNAMICS.md`](MEMETIC_DYNAMICS.md) — seven memetic contours
- [`MVP_ITERATIONS.md`](../examples/MVP_ITERATIONS.md) — Iteration 6 checklist
