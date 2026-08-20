# Integration — Finance-Crypto Markets

How AI Native Gov integrates finance and crypto market signals into an institutional simulator without claiming verdict authority.

## Purpose (INSTITUTIONAL_MODEL framing)
This integration layer collects and normalizes market, technical, and risk-related signals for downstream institutional reasoning.

In the AI Native Gov ecosystem, this layer is an `INSTITUTIONAL_MODEL` adapter contract:
- It provides *context signals* (what happened, with uncertainty and quality flags).
- It does not provide investment advice or moral/legal verdicts.
- It prepares events that later plugins can map into `μ/α/PNO/FPD` computation in the Errorlogy pipeline.

Only downstream certified artifacts may be labeled `COMPUTATIONAL_EVIDENCE` (via NAMM certificates). Otherwise, cross-layer envelopes remain `OPERATIONAL`.

## What belongs in this layer (signal families)
Adapters under this layer may ingest (or reference) signals from:

1. TradingView MCP server (connected via MCP)
2. Exchange and venue feeds (price, order book summaries, liquidity proxies)
3. On-chain indicators (flows, liquidity movement, token health proxies, risk heuristics)
4. Macro and cross-asset feeds (rates, FX, risk-on/off proxies, volatility proxies)
5. News and sentiment feeds (headlines, sentiment aggregates, social momentum)

## Normalized event types (adapter-level)
Adapters normalize their raw outputs into a shared set of event types. Example event_type strings (used by the institutional framer and/or mapped into `event_type` in `schemas/cross-layer-event.json`):

- `fin_crypto_market_snapshot`: price/volume/liquidity snapshot or market-wide overview
- `fin_crypto_technical_indicator`: RSI/MACD/Bollinger/Keltner/supertrend-style indicator snapshot
- `fin_crypto_screener_rank_update`: screener results as ranks plus the filters used
- `fin_crypto_news_headline`: news headline or structured headline record
- `fin_crypto_sentiment_momentum`: sentiment/momentum aggregate (e.g., reddit or price momentum)
- `fin_crypto_onchain_risk`: on-chain risk hypothesis signals (not accusations)
- `fin_crypto_backtest_result`: backtest summary metrics (Sharpe, drawdown, expectancy)
- `fin_crypto_walk_forward_validation`: walk-forward robustness verdict (if provided by source)
- `fin_crypto_data_unavailable`: provider failure, rate limit, missing fields (no values)

## Routing targets inside the institutional simulator
The institutional framer maps each normalized event to a set of activated institution layers. Labels are epistemic labels for the eventual cross-layer envelope:

- `OPERATIONAL`: default for adapter-derived signals and computed indicators without NAMM certificate linking
- `COMPUTATIONAL_EVIDENCE`: only when a linked `certificate_ref` (NAMM `certificate.json`) is present
- `INSTITUTIONAL_MODEL`: used only for framing/hypotheses with no evidence-grade payload
- `PHILOSOPHICAL_INFERENCE`: discouraged for public gates (no verdict authority)

Mapping (starting point):

| Normalized event_type | Activated institution layers (examples) | Epistemic label (default) | Simulator intent |
|---|---|---|---|
| `fin_crypto_market_snapshot` | `institution:executive`, `institution:central-bank-analog`, `institution:regulatory-agency` | `OPERATIONAL` | economic stability context and monitoring signals |
| `fin_crypto_technical_indicator` | `institution:regulatory-agency`, `institution:ai-minister` | `OPERATIONAL` | technical dynamics as weak evidence, uncertainty-aware |
| `fin_crypto_screener_rank_update` | `institution:parliament`, `institution:regulatory-agency` | `OPERATIONAL` | agenda-level attention signals (no “buy/sell” verdicts) |
| `fin_crypto_news_headline` | `institution:parliament`, `institution:executive` | `OPERATIONAL` | narrative context for deliberation and dispute surfacing |
| `fin_crypto_sentiment_momentum` | `institution:parliament`, `institution:central-bank-analog` | `OPERATIONAL` | crowd/market momentum as uncertainty-tagged input |
| `fin_crypto_onchain_risk` | `institution:judiciary`, `institution:transnational-ops`, `institution:interpol-analog` | `OPERATIONAL` | dispute surface and cross-border risk hypotheses (not accusations) |
| `fin_crypto_backtest_result` | `institution:audit`, `institution:regulatory-agency` | `OPERATIONAL` | methodological performance context (weak-to-medium evidence grade) |
| `fin_crypto_walk_forward_validation` | `institution:audit`, `institution:regulatory-agency` | `OPERATIONAL` | robustness context, never a trading recommendation |
| `fin_crypto_data_unavailable` | `institution:audit` | `OPERATIONAL` | observability: missing data, provider health, retry semantics |

## Adapter plugin interface (what each source adapter must output)
Each source adapter in this layer must output a normalized record with the following shape (the institutional framer may later reference these records via IDs in `stream_refs`):

```json
{
  "adapter_id": "string (stable, e.g. tradingview-mcp:market_snapshot)",
  "record_id": "string (stable within adapter)",
  "story_id": "string (maps to a politic.bar story anchor when available)",
  "event_type": "string (from the normalized list above)",
  "observed_at": "ISO8601 timestamp (when the adapter produced the record)",
  "as_of": "ISO8601 timestamp (when the underlying data is valid, if known)",
  "instrument": {
    "asset_class": "crypto|fx|equity|index|macro|other",
    "symbol": "string (e.g., BTC-USD, ETH-USD, SPY, EURUSD=X)",
    "exchange_or_venue": "string|null"
  },
  "timeframe": "string|null (e.g., 1m, 15m, 1h, 1d)",
  "signal": {
    "name": "string (e.g., RSI, MACD_hist, Bollinger_upper, rank_score)",
    "value": "number|string|null",
    "unit": "string|null"
  },
  "evidence_grade": "weak|medium|strong",
  "quality_flags": ["string", "..."],
  "uncertainty": {
    "confidence": "float [0,1]",
    "notes": "string|null"
  },
  "source_refs": {
    "provider_name": "string",
    "tool_call_id": "string|null",
    "raw_payload_ref": "string|null (pointer/id to stored raw response)"
  }
}
```

Quality flag examples (non-exhaustive):
- `data_delayed`: provider indicates stale timestamps
- `rate_limited`: upstream throttling encountered
- `partial_payload`: only some fields present
- `estimated`: value derived/approximated by provider
- `error_envelope`: upstream returned structured error information
- `outlier_suspected`: statistical anomaly detection triggered by adapter logic

Guardrail requirement:
- Adapters must never convert signals into investment “verdict language” (buy/sell/strong buy).
- If a source includes suggestion-like outputs, adapters must store them as `signal` values with explicit uncertainty and treat them as hypotheses only.

## Minimal first adapter plan: TradingView MCP
TradingView MCP (connected via MCP) provides market data, technical indicators, screeners, and backtesting capabilities.
Reference: [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp).

Minimal plan (MVP adapter behavior):
1. Tool selection (start with a small subset)
   - Market context: `market_snapshot`, `yahoo_price`
   - Technical context: `get_technical_analysis`, `get_multi_timeframe_analysis` (or closest available technical endpoints in the MCP server)
   - Screener context: `top_gainers` / `top_losers` and/or dedicated screener tools
   - News/sentiment context: `financial_news` and/or `market_sentiment` (if enabled)
2. Request strategy
   - For each configured symbol/timeframe, call the relevant MCP tools.
   - Keep per-symbol sampling sparse at first (to avoid rate bursts) and emit `fin_crypto_data_unavailable` records when calls fail.
3. Normalization rules (conversion into normalized event_type records)
   - Convert price/volume/liquidity fields into `fin_crypto_market_snapshot`.
   - Convert indicator families (RSI/MACD/Bollinger/Keltner/supertrend-style values) into one or more `fin_crypto_technical_indicator` records.
   - Convert screener ranks and filter metadata into `fin_crypto_screener_rank_update` records (store rank and filter criteria as structured context in `signal.name/value` and/or additional `quality_flags`/`notes`).
   - Convert headlines into `fin_crypto_news_headline` with `evidence_grade=weak|medium` depending on provider completeness.
   - Convert sentiment/momentum aggregates into `fin_crypto_sentiment_momentum` (confidence derived from provider-provided distribution when available).
4. Error envelope handling (from the TradingView MCP provider)
   - If a tool returns a structured error envelope (e.g., `{ "error": { "code": "...", "retryable": true } }`), do one of:
     - retry with backoff (if `retryable=true`) and only then emit, or
     - skip values and emit `fin_crypto_data_unavailable` with `quality_flags: ["error_envelope", "<code>"]`.

Epistemic label policy:
- Until NAMM verification is linked, the eventual cross-layer envelope for these events uses `epistemic_label=OPERATIONAL`.

## Guardrails (epistemic humility)
- No legal or moral verdict claims: on-chain risk signals are hypotheses about risk/dispute surfaces, not accusations.
- No financial advice: backtest and technical indicators are recorded as evidence-grade context only.
- Uncertainty is mandatory:
  - `evidence_grade` must be set even when the provider supplies a confidence score (the adapter must translate provider confidence into this scale).
  - `quality_flags` must capture provider health and completeness.
- Certificate discipline:
  - Use `COMPUTATIONAL_EVIDENCE` only when a NAMM certificate is linked via `certificate_ref`.

## Downstream: where signals feed μ/α/PNO/FPD computation
- Errorlogy integration contract and engine pipeline definitions: [ERRORLOGY.md](ERRORLOGY.md)
- NAMM verification and epistemic labels: [NAMM.md](NAMM.md)

This layer produces normalized operational inputs that later institutional framing and engine adapters can map into WMS/μ/α/PNO/FPD stages.

---

## Links
- TradingView MCP server: https://github.com/atilaahmettaner/tradingview-mcp
- [`ERRORLOGY.md`](ERRORLOGY.md)
- [`NAMM.md`](NAMM.md)

