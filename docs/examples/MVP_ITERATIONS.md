# MVP Iterations — Validated Against Real Code

**Epistemic label:** `OPERATIONAL` planning note (repo inventory + proposed cuts). Not a product release plan with authority claims.

**Validated against (2026-08-20):**

| Path | Role |
|------|------|
| `C:\Users\Public\AI_NATIVE_GOV` | Umbrella contracts / topology |
| `C:\Users\Public\ERRORLOGY_MVP\errorlogy-mas` | FastAPI runtime |
| `C:\Users\Public\ERRORLOGY_MVP\errorlogy-gui-v2` | Browser UI target |
| `C:\Users\Public\POLITIC_BAR`, `C:\Users\Public\NAMM` | Later only (out of MVP) |

---

## Verdict

**Proceed with revisions** — do not implement the chat proposal as-is.

| Proposed | Reality check | Revision |
|----------|---------------|----------|
| 1. `cross-layer-event` → FastAPI → institutional activation stub | Ingress already exists (`/api/ingest/*`); no institutional router; analyze has optional JWT (`current_user` may be `None`) | Thin **institutions** router + stub activator; do **not** fork a second full ingest stack |
| 2. UI: EU/national map + event stream in gui-v2 | gui-v2 has 4 routes (`/`, `/stream`, `/case`, `/data`); `/data` already polls ingest docs/signals; Electron `errorlogy-gui/` is separate ACTIVE desktop | Keep **gui-v2**; map is feasible as one new page + API client methods |
| 3. One fin-crypto adapter (TradingView **or** CCXT MCP) | No `ccxt` / TradingView in `requirements.txt`; FIN doc prefers TradingView **MCP** first, then CCXT MCP; FastAPI has no MCP client bridge | Prefer **CCXT Python library, market-data only** (not MCP) for first adapter |

Roadmap alignment: Phase 0 ✅; this MVP is **Phase 1–2 contracts + early Phase 4 adapter smoke**, not Phase 5 or world-scale Stage D in full.

---

## What already exists (do not reinvent)

### errorlogy-mas FastAPI (`api/main.py`)

| Router | Prefix | Notes |
|--------|--------|--------|
| `auth` | `/api/auth` | Google / GitHub / Telegram → JWT |
| `analysis` | `/api` | `/analyze`, `/analyze/stream` (SSE), `/cases/{id}`, `/taxonomy*`, `/health` — `Depends(current_user)` is **optional** (`auto_error=False`) |
| `ingest` | `/api/ingest` | Document/URL/batch, Exa/web/RSS/US-gov fetch, documents list, ingest signals |
| `signals` | `/api/signals` | CEP alerts / trends (Horizon 2) |
| `forecast` | `/api/forecast` | Stream forecast aggregate |
| `stats` / `metrics` | `/api/stats`, `/api/metrics` | Case lists, orchestrator metrics |

There is **no** dedicated “stream” router: “stream” means analyze SSE + `GET /api/forecast/stream`.

**Least-friction fit for institutional activation:** new sibling router `api/routers/institutions.py` (prefix `/api/institutions`), with a small module `mas/institutions/` that validates envelopes and returns `activated_layers` — **without** calling μ/α/PNO and without copying taxonomy JSON into the umbrella.

### errorlogy-gui-v2

| Route | Page | API use |
|-------|------|---------|
| `/` | HomePage | health |
| `/stream` | StreamForecastPage | `GET /api/forecast/stream` |
| `/case` | CaseForecastPage | analyze / analyze SSE |
| `/data` | DataStreamsPage | ingest status/docs/signals + fetch actions |

Vite proxies `/api` → `:8000`. Topology map + institutional event feed = **one new route** (reuse list/poll patterns from `DataStreamsPage`), not a rewrite.

### Umbrella contracts (already usable)

- [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json) — required: `story_id`, `event_type`, `activated_layers`, `epistemic_label`
- [`schemas/institution-layer-id.json`](../../schemas/institution-layer-id.json) — includes EU + national layer IDs
- [`docs/integrations/FIN_CRYPTO_MARKETS.md`](../integrations/FIN_CRYPTO_MARKETS.md) — adapter record shape + event types
- [`docs/integrations/GOV_DATA_SOURCES.md`](../integrations/GOV_DATA_SOURCES.md) — sibling gov ingress (exists)
- [`docs/institutions/EU_TOPOLOGY.md`](../institutions/EU_TOPOLOGY.md) / `EU_STATES.md` — static map source material

---

## Revised iterations (1–3)

### Iteration 1 — Cross-layer ingress + institutional activation stub

**Title:** Institutional activation stub on FastAPI (schema-validated)

**Runtime home:** `ERRORLOGY_MVP/errorlogy-mas` only.

| Target | Action |
|--------|--------|
| `api/routers/institutions.py` | **New** — `POST /api/institutions/activate`, `GET /api/institutions/events`, `GET /api/institutions/layers` |
| `mas/institutions/activate.py` | **New** — validate body against umbrella `cross-layer-event` fields; if `activated_layers` empty/missing from a partial ingress, apply **static** route table (copy mapping tables from FIN_CRYPTO / GOV_DATA docs as code constants, not LLM) |
| `mas/institutions/store.py` | **New** — in-memory or SQLite table of recent envelopes (reuse `mas/db.py` patterns if cheap) |
| `api/main.py` | `include_router(institutions_router)` |
| Optional | `POST /api/institutions/activate` may accept a **partial** ingress (`story_id`, `event_type`, `jurisdiction_set`, …) and fill `activated_layers` + default `epistemic_label=INSTITUTIONAL_MODEL` or `OPERATIONAL` |

**Do not in iter 1:** wire auto_analyze into μ/α; require OAuth; host schema copies as “new taxonomy”; implement politic.bar story IDs for real.

**Auth:** match ingest — leave open or optional JWT; do not block stub on OAuth.

**Done when:**

- [ ] `POST /api/institutions/activate` accepts a valid cross-layer-event-shaped JSON and returns the same plus stub metadata (`status: activated`, `framer: stub`)
- [ ] Invalid `activated_layers` / `epistemic_label` → 400
- [ ] `GET /api/institutions/events?limit=N` returns recently activated envelopes
- [ ] `GET /api/institutions/layers` returns enum list consistent with umbrella `institution-layer-id.json` (vendored path or documented sync note)
- [ ] No new secrets; umbrella repo unchanged except this planning doc / schema notes if needed
- [ ] Smoke: one curl (or pytest) with `event_type=bilateral_summit` and EU/national layers

---

### Iteration 2 — gui-v2 EU/national topology map + institutional event feed

**Title:** gui-v2 topology map + institutional event feed

**Runtime home:** `ERRORLOGY_MVP/errorlogy-gui-v2`.

| Target | Action |
|--------|--------|
| `src/pages/TopologyPage.tsx` (or `InstitutionsPage.tsx`) | **New** — two-panel: static EU/national layer graph + live event list |
| `src/App.tsx` / `Layout.tsx` / `lib/ru.ts` | Route `/topology` + nav entry |
| `src/lib/api.ts` + `types.ts` | `institutionsActivate`, `institutionsEvents`, `institutionsLayers` |
| Map data | Hardcode or fetch static JSON derived from umbrella `EU_TOPOLOGY` / layer IDs — **no** runtime import from umbrella git path required if a small `public/eu-topology.json` is checked into gui-v2 |

**Feasibility:** 1–2 iterations is realistic if the map is **schematic** (nodes = layer IDs / member ISO codes, highlight on `activated_layers`), not a full GIS product. Reuse poll interval pattern from `DataStreamsPage` (~12s).

**Done when:**

- [ ] `/topology` loads without auth wall
- [ ] Map shows EU supranational nodes + at least a subset of national instances (or “national-instance” generic + sample ISO set)
- [ ] Event feed shows `GET /api/institutions/events`; selecting an event highlights `activated_layers` on the map
- [ ] Manual “activate sample event” button posts a fixture envelope (optional but useful)
- [ ] No Electron packaging; no politic.bar iframe

---

### Iteration 3 — First fin-crypto market-data adapter (CCXT library)

**Title:** CCXT market-data adapter → institutional envelope

**Runtime home:** `ERRORLOGY_MVP/errorlogy-mas`.

| Target | Action |
|--------|--------|
| `requirements.txt` | Add `ccxt` (pin a known stable minor) |
| `mas/adapters/fin_crypto_ccxt.py` (or `mas/ingest/fetchers/ccxt_markets.py`) | Public ticker/OHLCV only → FIN_CRYPTO normalized record → map to `fin_crypto_market_snapshot` |
| `api/routers/institutions.py` or thin `api/routers/fin_crypto.py` | `POST /api/institutions/fin-crypto/snapshot` (symbols + optional exchange) → activate stub |
| Config | Exchange list + symbols via env; **no API keys** for public market path |

**Done when:**

- [ ] One public call (e.g. Binance or Kraken ticker for `BTC/USDT`) returns normalized record + cross-layer envelope with layers from FIN_CRYPTO table (`executive`, `central-bank-analog`, `regulatory-agency`) and `epistemic_label=OPERATIONAL`
- [ ] Provider failure emits `fin_crypto_data_unavailable` (or equivalent quality flags) without crashing the API
- [ ] No order placement / balance / private endpoints exposed
- [ ] Umbrella FIN_CRYPTO doc gains a one-line note: “FastAPI MVP uses CCXT **library**; TradingView MCP remains agent/MCP path”

---

## What stays in the umbrella (contracts only)

| Keep here | Do not put here |
|-----------|-----------------|
| `schemas/cross-layer-event.json`, `institution-layer-id.json` | FastAPI apps, adapters, SQLite |
| `docs/integrations/FIN_CRYPTO_MARKETS.md`, `GOV_DATA_SOURCES.md` | MCP server processes as “product runtime” |
| `docs/institutions/EU_*.md`, `TOPOLOGY.md`, `GLOBAL_AI_GOVERNANCE.md` | gui-v2 / Electron binaries |
| This file (`docs/examples/MVP_ITERATIONS.md`) | Copied `errorlogy_unified_taxonomy_v16.json` |
| Integration pointers to child repos | Secrets, `.env`, API keys |

ARCHITECTURE remains: umbrella = topology + contracts; Errorlogy = runtime.

---

## Out of scope for this MVP

- Electron desktop (`errorlogy-gui/`) packaging or porting the topology page there
- politic.bar live signal/noise streams and politifi asset updates
- NAMM `certificate.json` / `COMPUTATIONAL_EVIDENCE` upgrades
- TradingView MCP (or any MCP subprocess) inside FastAPI
- Exchange **execution** / private account reads
- Full 27-state interactive GIS; ASEAN/AU/Mercosur blocs
- Engine math changes (μ/α/PNO/FPD); taxonomy v0.6 ↔ v16 merge
- `schemas/signal-envelope.json` full Phase 2 suite (optional follow-on; activate stub can stay on `cross-layer-event` alone)

---

## Recommended FIRST fin-crypto choice

**CCXT Python library (market-data / public REST only)** — one pip dependency, no MCP bridge, no vendor OAuth, reliable public tickers/OHLCV, and it matches the FIN_CRYPTO hard split (reads OK, execution off) with the least FastAPI friction.

TradingView MCP stays the preferred **agent/MCP** exploration path in docs; defer it until a client bridge exists. Community CCXT **MCP** servers are unnecessary for iter 3 if the library is already in-process.

---

## Risks (explicit)

| Risk | Mitigation |
|------|------------|
| Taxonomy mixing (politic-bar v0.6 vs MAS v16) | Institutional stub uses **umbrella layer IDs only**; never invent CB-/PNO- mode IDs; do not auto-merge catalogs |
| Umbrella hosts runtime | All code in `ERRORLOGY_MVP`; umbrella stays docs/schemas |
| Electron premature | gui-v2 browser only; Electron remains ACTIVE for existing desktop, not for this MVP path |
| MCP-first fin-crypto slows FastAPI | Prefer library adapter; keep MCP as optional later |
| Auth surprise | Analyze “requires” `current_user` but JWT is optional — document; do not suddenly lock institutions behind OAuth |
| “Activation” mistaken for sovereignty | Responses always carry `epistemic_label`; UI copy = institutional model / signals |

---

## Checklist rollup

### Iteration 1 done when…
Schema-valid activate + list events + layers enum; stub only; pytest or curl green.

### Iteration 2 done when…
`/topology` map + event feed wired to institutions API; schematic EU/national highlight works.

### Iteration 3 done when…
Public CCXT snapshot → normalized record → institutional envelope `OPERATIONAL`; failures soft-fail; no trading surface.

---

## Later (explicitly after MVP)

1. Electron-gui parity (optional port of `/topology`)
2. politic.bar stream_refs / story anchors
3. NAMM certificate_ref → `COMPUTATIONAL_EVIDENCE`
4. TradingView MCP or official `ccxt-mcp` as alternate adapters
5. Gov open-data fetchers already in MAS (`fetch-us-gov`, etc.) mapped through the same institutions framer

---

## Links

- [`ROADMAP.md`](../../ROADMAP.md)
- [`ARCHITECTURE.md`](../../ARCHITECTURE.md)
- [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json)
- [`docs/integrations/FIN_CRYPTO_MARKETS.md`](../integrations/FIN_CRYPTO_MARKETS.md)
- Child: `ERRORLOGY_MVP/errorlogy-mas/api/main.py`, `errorlogy-gui-v2/src/App.tsx`
