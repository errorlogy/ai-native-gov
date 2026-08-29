# Integration — Finance-Crypto Markets

How AI Native Gov integrates finance and crypto market signals into an institutional simulator without claiming verdict authority.

## Sibling layers
Government open-data / legislative / parsing ingress (official APIs, parliamentary feeds, graded news, human uploads) lives in [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md). Use that contract for non-market institutional inputs; keep this file for finance-crypto market adapters.

Symbolic / visual identity (logos, seals, merch marks, NFT **catalog** graph, content-addressed media) lives in [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md). NFT floor/volume/listing and on-chain risk stay here as market signals; symbol↔token registry edges (`minted_as`, collection metadata) stay in the symbolic layer.

## Purpose (INSTITUTIONAL_MODEL framing)
This integration layer collects and normalizes market, technical, and risk-related signals for downstream institutional reasoning.

In the AI Native Gov ecosystem, this layer is an `INSTITUTIONAL_MODEL` adapter contract:
- It provides *context signals* (what happened, with uncertainty and quality flags).
- It does not provide investment advice or moral/legal verdicts.
- It prepares events that later plugins can map into `μ/α/PNO/FPD` computation in the Errorlogy pipeline.

Only downstream certified artifacts may be labeled `COMPUTATIONAL_EVIDENCE` (via NAMM certificates). Otherwise, cross-layer envelopes remain `OPERATIONAL`.

**FastAPI MVP (iter 3):** public market snapshots use the in-process **CCXT Python library** (`errorlogy-mas/mas/adapters/fin_crypto_ccxt.py`, `POST /api/events/fin-crypto/snapshot`). TradingView MCP and community CCXT **MCP** servers remain the preferred **agent/MCP** exploration path — not embedded in FastAPI.

**Memetic ↔ market join (Phase B runtime — Iter 6):** `memetic_market_coupling_snapshot` cross-layer events join narrative velocity from `signal-envelope.json` stream items with `fin_crypto_market_snapshot` records on shared `story_id` or instrument symbol. See [`MEMETIC_MARKET_COUPLING.md`](MEMETIC_MARKET_COUPLING.md). Runtime: `POST /api/events/memetic/market-coupling` in errorlogy-mas.

## What belongs in this layer (signal families)
Adapters under this layer may ingest (or reference) signals from:

1. TradingView MCP server (connected via MCP) — first adapter
2. Exchange and venue feeds via **Exchange MCP adapters** (unified CCXT-style and venue-specific; price, order book, public trades; execution gated) — see section below
3. On-chain / aggregator MCP indicators (CoinGecko, DefiLlama, flows, liquidity, token health proxies, risk heuristics)
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
The institutional framer maps each normalized event to a set of activated institution layers. Layer semantics for monetary, treasury, regulatory, and agentic economics roles: [AI_MONETARY_SYSTEM.md](../institutions/AI_MONETARY_SYSTEM.md). Labels are epistemic labels for the eventual cross-layer envelope:

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

## Exchange MCP adapters
Exchange-specific and unified MCP servers plug into the same adapter contract as TradingView: normalize vendor payloads into the event types above, then route through the institutional framer. None of these sources issue policy verdicts; market data remains `OPERATIONAL` / (optionally) `COMPUTATIONAL_EVIDENCE` when NAMM-linked.

### Market-data vs trading/execution (hard split)
| Mode | Typical tools | Simulator policy |
|---|---|---|
| **Market-data only** (preferred) | tickers, OHLCV/klines, order book depth, public trades, exchange status, listings, fees | Enable by default for `INSTITUTIONAL_MODEL` context. Emit normalized records with `evidence_grade=weak\|medium`. |
| **Account / portfolio read** | balances, open orders, positions, PnL | Optional, approval-gated. Treat as private operational telemetry, not public institutional evidence. Never label as legitimacy or compliance verdicts. |
| **Trading / execution** | place/cancel order, convert, TWAP, smart routing | **High-risk.** Disable in the institutional simulator by default. If ever exposed, require explicit human approval, sandbox/testnet-first, audit journal, and never map fills into μ/α/PNO as “policy outcomes.” |

Quality flags for this family (in addition to the global list):
- `execution_surface`: tool can place or cancel orders (adapter should refuse or no-op in simulator mode)
- `api_key_required`: private endpoints; keys must stay local (never in umbrella docs or git)
- `public_rest_only`: no credentials; preferred for simulator ingest
- `venue_specific`: symbol/venue quirks; normalize `instrument.exchange_or_venue`

### Candidate MCP servers (community / vendor — not endorsements)
Candidates below are discovery notes for Phase 1–2 linkage. Star counts and APIs change; verify before wiring. Prefer market-data modes. Flag any execution surface as approval-gated.

| Name | GitHub / endpoint | Data types | Auth notes | Fit for INSTITUTIONAL_MODEL simulator |
|---|---|---|---|---|
| **CCXT (community, market-data lean)** — `Nayshins/mcp-server-ccxt` | https://github.com/Nayshins/mcp-server-ccxt | OHLCV, tickers, volume ranks, multi-exchange summaries (Binance, Coinbase, Kraken, Bybit, OKX, …) | Public market data; no keys for read path | **Strong fit** as unified next adapter after TradingView |
| **CCXT (community, trading-capable)** — `lazy-dinosaur/ccxt-mcp` | https://github.com/lazy-dinosaur/ccxt-mcp | Market data + trading across 100+ venues | API keys for private/trade | Use **market-data subset only**; gate execution |
| **CCXT (community)** — `doggybee/mcp-server-ccxt` | https://github.com/doggybee/mcp-server-ccxt | Spot/futures market data + trade ops | Keys for trade | Same: prefer public reads; gate execution |
| **CCXT (community)** — `dante1989/mcp-ccxt` | https://github.com/dante1989/mcp-ccxt | Market data, account, trading (sandbox-default claimed) | Keys optional; sandbox-on default | Good unified candidate if sandbox stays default |
| **CCXT official MCP (in progress)** | https://github.com/ccxt/ccxt/pull/29277 (`ccxt-mcp` npm package proposed) | Public market data; private reads; opt-in trading with caps/audit | Keys in OS keychain; model sees account names only | Watch for merge/release — preferred long-term unified adapter if shipped with trading opt-in |
| **CEX watch (public REST)** — `Zanecex101/cex-watch-mcp` | https://github.com/Zanecex101/cex-watch-mcp | Listings, fee compare, exchange status (Binance, OKX, Bybit, Coinbase, Kraken) | **None** (public REST) | **Strong fit** for venue health / listing context; narrow scope |
| **Order book analytics** — `kukapay/crypto-orderbook-mcp` | https://github.com/kukapay/crypto-orderbook-mcp | Order book depth / imbalance (Binance, Kraken, Coinbase, Bitfinex, OKX, Bybit) | Public APIs | Good liquidity-proxy signals → `fin_crypto_market_snapshot` |
| **Binance** — `AnalyticAce/binance-mcp-server` | https://github.com/AnalyticAce/binance-mcp-server | Ticker, order book, balances, orders, PnL | API key/secret | Prefer ticker/order book only; **execution high-risk** |
| **Binance** — `nirholas/Binance-MCP` | https://github.com/nirholas/Binance-MCP | Very broad Binance surface (market + many private products) | API credentials local | Too wide for simulator; whitelist market-data tools |
| **Binance** — `ethancod1ng/binance-mcp-server` | https://github.com/ethancod1ng/binance-mcp-server | Price, order book, klines, account, place/cancel | Key/secret; testnet flag | Market-data OK; gate `place_order` / cancel tools |
| **Binance** — `TermiX-official/binance-mcp` | https://github.com/TermiX-official/binance-mcp | Market data + portfolio + order execution | Binance API + optional wallet key | High-risk execution surface; not default for simulator |
| **Coinbase** — `visusnet/coinbase-mcp-server` | https://github.com/visusnet/coinbase-mcp-server | Market data, balances, Advanced Trade | Coinbase API credentials | Market-data subset only; gate trading |
| **Coinbase** — `almoore/coinbase-mcp` | https://github.com/almoore/coinbase-mcp | Spot/futures, paper trading, technicals | Advanced Trade auth | Prefer paper/market-data paths if retained |
| **Kraken** — `oilst/kraken-mcp` | https://github.com/oilst/kraken-mcp | Kraken exchange MCP (community) | Per-repo; expect API keys for private | Verify market-data vs trade tools before enable |
| **Kraken (public)** — `sebastiancoombs/kraken-mcp` | https://github.com/sebastiancoombs/kraken-mcp | server_time, asset_pairs, ticker, OHLC, order book | Public REST (x402 pay-per-call wrapper) | Market-data fit; note payment/wrapper complexity |
| **Bybit** — `ethancod1ng/bybit-mcp-server` | https://github.com/ethancod1ng/bybit-mcp-server | Market data, account, trading | Bybit API keys | Same split: reads OK, execution gated |
| **OKX** — `mbarinov/okx-mcp` | https://github.com/mbarinov/okx-mcp | Portfolio, positions, order history, trading | OKX API credentials | Account-heavy; whitelist public market tools if present |
| **OKX** — `esshka/okx-mcp` | https://github.com/esshka/okx-mcp | OKX MCP (community) | Per-repo | Evaluate before wiring |
| **CoinGecko (official)** | Docs: https://docs.coingecko.com/ai-integration/mcp-server · package: `@coingecko/coingecko-mcp` · source under https://github.com/coingecko/coingecko-typescript/tree/main/packages/mcp-server · remote `https://mcp.api.coingecko.com/mcp` | Prices, caps, volumes, charts, DEX pools, trending (aggregator — **not** exchange execution) | Keyless free remote or Demo/Pro key | **Strong fit** for cross-venue market snapshots / screener ranks |
| **DefiLlama (official remote)** | https://mcp.defillama.com/mcp · skills: https://github.com/DefiLlama/defillama-skills | TVL, yields, protocol metrics, stablecoins, bridges (on-chain/DeFi analytics — **not** CEX execution) | DefiLlama account + API plan | Strong fit for `fin_crypto_onchain_risk` / liquidity context |
| **DefiLlama (community free)** — `friendlygeorge/defillama-mcp-server` | https://github.com/friendlygeorge/defillama-mcp-server | TVL, yields, stablecoins, bridges, DEX volumes | None (public API) | Good no-key on-chain metrics adapter |
| **DefiLlama (community)** — `dcSpark/mcp-server-defillama` | https://github.com/dcSpark/mcp-server-defillama | Protocols, TVL, token prices, stablecoins | Public DefiLlama API | Alternative on-chain metrics path |
| **Hybrid metrics** — `copperxx/mcp-crypto-metrics` | https://github.com/copperxx/mcp-crypto-metrics | CoinGecko + DefiLlama dominance/TVL/cycle proxies | Free APIs, no key | Useful macro/crypto context; keep `evidence_grade=weak` on derived “cycle” proxies |
| **Hybrid + MCP** — `nirholas/crypto-market-data` | https://github.com/nirholas/crypto-market-data (`mcp-server/`) | CoinGecko prices/OHLCV + DefiLlama TVL/yields | Public APIs | Market-data / on-chain metrics; not execution |

No first-party “official exchange MCP” from Binance/Coinbase/Kraken/Bybit/OKX was confirmed as a vendor-published standard product in this pass; listings above are community or aggregator/vendor-data (CoinGecko, DefiLlama) unless noted.

### Mapping exchange MCP outputs → normalized event types
| Upstream MCP payload | Normalized `event_type` | Notes |
|---|---|---|
| Ticker / last price / 24h stats / OHLCV | `fin_crypto_market_snapshot` | Set `instrument.exchange_or_venue`, `timeframe`, `as_of` |
| Order book depth / imbalance / spread | `fin_crypto_market_snapshot` | Encode depth metrics in `signal.name` (e.g. `bid_depth_bps`, `imbalance`); `quality_flags` may include `partial_payload` |
| Public recent trades (tape summary) | `fin_crypto_market_snapshot` | Prefer aggregates over raw tape spam; throttle |
| Volume / gainer-loser / listing ranks | `fin_crypto_screener_rank_update` | Store filter criteria in `signal` / notes |
| Exchange status / latency / fee compare | `fin_crypto_market_snapshot` or `fin_crypto_data_unavailable` | Status failures → unavailable with `quality_flags` |
| Aggregator prices (CoinGecko) | `fin_crypto_market_snapshot` | `exchange_or_venue` = aggregator or null; note delayed/composite |
| TVL / protocol / bridge / stablecoin metrics | `fin_crypto_onchain_risk` (context) or `fin_crypto_market_snapshot` | Hypotheses/context only — not accusations or sanctions findings |
| Account balances / open orders / PnL | *(do not emit into public institutional stream by default)* | If needed for private ops: separate adapter_id namespace; never `COMPUTATIONAL_EVIDENCE` without NAMM |
| Place/cancel/convert orders | **Refuse in simulator** | Emit nothing, or `fin_crypto_data_unavailable` with `quality_flags: ["execution_surface"]` if a tool was invoked by mistake |
| Provider errors / rate limits | `fin_crypto_data_unavailable` | Preserve retryable metadata in `uncertainty.notes` |

Cross-layer envelopes that reference these records keep `epistemic_label=OPERATIONAL` until a NAMM `certificate_ref` justifies `COMPUTATIONAL_EVIDENCE`. Framing hypotheses about institutional response remain `INSTITUTIONAL_MODEL` — market numbers do not become policy verdicts.

### Plug-in order (recommended)
1. **TradingView MCP** (first) — already planned above; indicators, screeners, multi-asset context.
2. **Unified exchange MCP (CCXT-style)** — `Nayshins/mcp-server-ccxt` or successor official `ccxt-mcp`; one adapter covering many venues for OHLCV/tickers.
3. **Major exchange MCPs (narrow whitelist)** — Binance / Coinbase / Kraken / Bybit / OKX only where venue-specific depth, status, or symbol coverage is missing from CCXT; **market-data tools only**.
4. **On-chain / aggregator MCPs** — CoinGecko (official), DefiLlama (official or community free), optional hybrid metrics; feeds liquidity and protocol-health context, not CEX execution.
5. **Specialized microstructure** (optional) — order-book MCP / CEX-watch for depth and venue health overlays.

Do not enable multi-exchange “all-in-one trading” MCP servers in the institutional simulator path without an explicit approval and sandbox policy.

## NFT marketplace MCP (research note)
Official **OpenSea MCP** ([docs](https://docs.opensea.io/reference/mcp), `https://mcp.opensea.io/mcp`) is the main vendor NFT surface: floor/stats/portfolio = **market-data**; SeaDrop `get_mint_action` / `deploy_seadrop_contract` = **execution prep** (returns txs for wallet sign — approval-gated, high risk if auto-submitted). **Alchemy MCP** ([docs](https://www.alchemy.com/docs/alchemy-mcp-server)) is read-only NFT metadata/ownership. Community/vendor mint paths (Rare Protocol `rare mcp serve --allow-writes`, thirdweb remote MCP `deployContract`/`writeContract`, Solana Agent Kit MCP `MINT_NFT`, Story Protocol MCP hub collection/IP mint) require keys or server wallets — do not wire into the simulator without sandbox policy. No official Manifold / Zora / Foundation MCP found; Crossmint exposes docs + checkout MCP, not a first-party collection-mint MCP. Catalog ownership and `rights_status` stay in [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md) — never auto-mint scraped art.

**Practical setup (Cursor + cross-layer POST):** [CONNECTION_GUIDE.md](CONNECTION_GUIDE.md) — OpenSea/Alchemy MCP config, normalize → `POST /api/events/cross-layer`, mint approval gates.

## Sibling layers
- **Gov open data** — [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md): official APIs, parliamentary feeds, graded news, human uploads. Keep ownership separate so crypto venue adapters do not absorb gov data contracts.
- **Symbolic / visual** — [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md) catalog graph; [SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md) for IG/web media candidates (rights-gated before any NFT join).

## Guardrails (epistemic humility)
- No legal or moral verdict claims: on-chain risk signals are hypotheses about risk/dispute surfaces, not accusations.
- No financial advice: backtest and technical indicators are recorded as evidence-grade context only.
- Uncertainty is mandatory:
  - `evidence_grade` must be set even when the provider supplies a confidence score (the adapter must map provider confidence into this scale).
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
- Unified / CCXT-style: https://github.com/Nayshins/mcp-server-ccxt · https://github.com/lazy-dinosaur/ccxt-mcp · https://github.com/ccxt/ccxt/pull/29277
- CoinGecko MCP: https://docs.coingecko.com/ai-integration/mcp-server
- DefiLlama MCP: https://mcp.defillama.com/mcp · https://github.com/DefiLlama/defillama-skills
- Sibling ingress: [`GOV_DATA_SOURCES.md`](GOV_DATA_SOURCES.md)
- Symbolic / NFT catalog: [`SYMBOLIC_VISUAL_LAYER.md`](SYMBOLIC_VISUAL_LAYER.md)
- OpenSea MCP: https://docs.opensea.io/reference/mcp · https://docs.opensea.io/docs/build-with-ai-agents
- Alchemy MCP (NFT read): https://www.alchemy.com/docs/alchemy-mcp-server
- Cursor connection playbook: [`CONNECTION_GUIDE.md`](CONNECTION_GUIDE.md)
- [`ERRORLOGY.md`](ERRORLOGY.md)
- [`NAMM.md`](NAMM.md)
- [`MEMETIC_DYNAMICS.md`](MEMETIC_DYNAMICS.md) — Phase A memetic contracts + `memetic_market_coupling_snapshot` join
- [`MEMETIC_MARKET_COUPLING.md`](MEMETIC_MARKET_COUPLING.md) — Iter 6 join record + API contract

