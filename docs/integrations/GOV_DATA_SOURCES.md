# Integration — Government Data Sources / Parsing

How AI Native Gov ingests government-management and open-data signals into the institutional simulator without claiming verdict authority.

**Epistemic label:** `INSTITUTIONAL_MODEL` for this contract document. Adapter-emitted envelopes default to `OPERATIONAL` until a NAMM `certificate_ref` upgrades them to `COMPUTATIONAL_EVIDENCE`.

---

## Purpose

This layer is the **ingress adapter contract** for official and near-official government data — APIs, legislative/parliamentary feeds, open-data portals, and human-uploaded documents — before institutional framing and Errorlogy computation.

It sits beside [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md) (market/risk signals) and upstream of:

| Downstream | Role |
|------------|------|
| Institutional framer | Maps normalized events → `activated_layers` / topology intersections |
| [ERRORLOGY.md](ERRORLOGY.md) | `DATA → WMS → μ → α → …` (engine owns numeric outputs) |
| [POLITIC_BAR.md](POLITIC_BAR.md) | Signal/noise streams, politifi `stream_refs` |
| [NAMM.md](NAMM.md) | Optional verification certificates |

At world scale ([GLOBAL_AI_GOVERNANCE.md](../institutions/GLOBAL_AI_GOVERNANCE.md)), gov-data ingress feeds **national instances**, **regional blocs** (EU first), and later **global coordination** without claiming sovereignty. Envelope format: [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json).

**Guardrails (shared with Errorlogy / AGENTS language rules):**

| Use | Never use |
|-----|-----------|
| analytical contribution | guilty, criminal |
| legitimacy **signals** (modeled) | legitimate ruler (verdict) |
| institutional framing | sovereign AI government |
| possible / consistent with | "this proves" |

Adapters must not invent mode IDs; taxonomy v16 lives in the Errorlogy child repo.

---

## Source taxonomy

| Class | `source_class` | Examples | Typical evidence_grade |
|-------|----------------|----------|------------------------|
| Official open data APIs | `official_open_data` | Eurostat, data.europa.eu, CELLAR/EUR-Lex REST+SPARQL, Congress.gov, Federal Register, GovInfo | medium–strong |
| Legislative / parliamentary feeds | `legislative_parliamentary` | EP Open Data, national Hansard/bills APIs, LegiScan, Sejm, OpenTK | medium–strong |
| News / geopolitical signal streams | `news_signal` | RSS (BBC, gov.uk), Exa/web search hits, politic.bar streams | weak–medium |
| Financial / market (sibling) | `fin_crypto` | See [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md) | weak–medium |
| On-chain / geo risk | `geo_risk` | Cross-border ops hypotheses, disaster/FEMA-style feeds (when wired) | weak–medium |
| Human-uploaded / parsed docs | `human_upload` | Manual PDF/HTML/transcript upload, agent-parsed communiqués | weak–medium (depends on provenance) |

Each record must carry provenance (`source_refs`) and quality flags. HTML scrape is a **last resort** when no structured API or feed exists.

---

## Adapter interface

Same spirit as FIN_CRYPTO: each source adapter emits a normalized record that the institutional framer may reference via IDs in `stream_refs` / later map into `cross-layer-event.json`.

```json
{
  "adapter_id": "string (stable, e.g. eurostat-api:dataset_snapshot)",
  "record_id": "string (stable within adapter)",
  "story_id": "string (politic.bar story anchor when available)",
  "event_type": "string (from normalized list below)",
  "observed_at": "ISO8601 (adapter produce time)",
  "as_of": "ISO8601|null (underlying data validity time)",
  "jurisdiction_set": ["EU", "DE", "..."],
  "source_class": "official_open_data|legislative_parliamentary|news_signal|fin_crypto|geo_risk|human_upload",
  "document": {
    "title": "string|null",
    "doc_id": "string|null (CELEX, FR doc number, bill id, …)",
    "doc_type": "string|null (regulation|directive|bill|vote|report|rss_item|…)",
    "language": "string|null",
    "canonical_url": "string|null"
  },
  "signal": {
    "name": "string",
    "value": "number|string|null",
    "unit": "string|null"
  },
  "wms_environment": "string|null (Errorlogy source_environment when known)",
  "evidence_grade": "weak|medium|strong",
  "quality_flags": ["string", "..."],
  "uncertainty": {
    "confidence": "float [0,1]",
    "notes": "string|null"
  },
  "parse_method": "official_api|structured_feed|sdk_client|html_parse|human_upload",
  "source_refs": {
    "provider_name": "string",
    "tool_call_id": "string|null",
    "raw_payload_ref": "string|null"
  }
}
```

### Normalized event types

| `event_type` | Meaning |
|--------------|---------|
| `gov_open_data_snapshot` | Statistical or portal dataset slice (e.g. Eurostat indicator) |
| `gov_legislative_document` | Bill, act, regulation, directive, OJ item, CELEX-resolved text |
| `gov_parliamentary_activity` | Debate, vote, question, committee action, plenary session |
| `gov_executive_publication` | Executive order, register notice, government announcement |
| `gov_judicial_docket` | Court filing / docket pointer (not a guilt determination) |
| `gov_audit_oversight_report` | GAO, OIG, ECA, NAO-style oversight document |
| `gov_news_signal` | Graded news/RSS/search hit for institutional context |
| `gov_human_upload_parsed` | Human-provided document after parse + provenance tagging |
| `gov_data_unavailable` | Provider failure, rate limit, missing fields |

Suggested `cross-layer-event.json` examples for ingress: `gov_open_data_snapshot`, `gov_legislative_document` (see schema).

### Quality flags (non-exhaustive)

- `data_delayed` — stale timestamps
- `rate_limited` — upstream throttling
- `partial_payload` — incomplete fields
- `estimated` — derived/approximated
- `html_parsed` — no official structured API used
- `translation_uncertain` — cross-language retrieval without native text
- `error_envelope` — structured provider error
- `key_required_missing` — keyed API skipped
- `duplicate_suspected` — near-duplicate of prior ingest

---

## Inventory

### A) Available MCP in this Cursor session (now)

Configured MCP servers in this workspace (catalog at research time). **None were live for tool calls** — all reported discovery/auth errors; only `mcp_auth` was exposed until re-auth.

| Server ID | Intended role for gov ingress | Status (session) | Notes |
|-----------|------------------------------|------------------|-------|
| `plugin-exa-exa` | Web/news discovery, secondary corroboration (`news_signal`) | **Unavailable** (auth/discovery failed) | Errorlogy already has `mas/ingest/fetchers/exa.py` for batch ingest |
| `user-obsidian-cursor` | Local research notes / prior session context | **Unavailable** | Not a gov data plane |
| `plugin-figma-figma` | Design only | **Unavailable** | Out of scope |
| `plugin-slack-slack` | Ops notifications | **Unavailable** | Out of scope |
| TradingView MCP | Finance sibling layer | **Not in catalog** this session | Documented in FIN_CRYPTO; candidate install: [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) |

**Umbrella repo:** no `.cursor` MCP config files and no MCP docs beyond this integration set. Gov ingress is a **contract** here; fetchers/MCP plugins live in child repos or Cursor MCP install.

### B) Candidate GitHub MCP / repos (install / evaluate)

EU-first and high-value national/US candidates (links verified via GitHub API / search where possible):

| Candidate | URL | Fit | Priority for EU-27 sim |
|-----------|-----|-----|------------------------|
| European Parliament MCP | https://github.com/Hack23/European-Parliament-MCP-Server | MEPs, votes, procedures, EP Open Data | **P0** |
| EUR-Lex MCP (SOAP bridge) | https://github.com/scimorph/eur-lex-mcp | Expert search + CELEX document fetch | **P0** |
| EULEX AI (hosted MCP) | https://mcp.eulex.ai/ | Indexed EU law + Eurostat context (OAuth) | **P0** evaluate (hosted) |
| legislation.gov.uk MCP | https://github.com/legislation/legislation-mcp-ts | UK acts/SIs (non-EU but ELI-aligned patterns) | P2 |
| GB ELI + case law MCP | https://github.com/matematicsolutions/gb-eli-mcp | legislation.gov.uk + Find Case Law + GOV.UK | P2 |
| UK Parliament MCP | https://github.com/i-dot-ai/parliament-mcp | Hansard / Members APIs | P2 |
| OpenTK (NL Tweede Kamer) | https://github.com/r-huijts/opentk-mcp | NL national parliament (`state:NL`) | **P1** |
| Sejm MCP (PL) | https://github.com/janisz/sejm-mcp | Polish Sejm + ELI | **P1** |
| US Gov Open Data MCP | https://github.com/lzinga/us-gov-open-data-mcp | 40+ federal APIs (Congress, FR, FRED, …) | P1 (US scenarios / comparative) |
| Federal Register MCP | https://github.com/aml25/federal-register-mcp | Executive/register focus | P2 |
| Congress.gov MCP | https://mcpservers.org/servers/AshwinSundar/congress_gov_mcp | US legislative | P2 |
| TradingView MCP | https://github.com/atilaahmettaner/tradingview-mcp | Sibling fin-crypto layer | See FIN_CRYPTO |
| awesome-mcp-servers | https://github.com/punkpeye/awesome-mcp-servers | Discovery index | Ongoing |
| WorldMonitor | https://github.com/koala73/worldmonitor | Geo/news dashboard (not MCP-first) | Optional signal research |

Official APIs (prefer over MCP wrappers when building production fetchers):

| API / portal | URL | Use |
|--------------|-----|-----|
| Eurostat Statistics API | https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access | `gov_open_data_snapshot` |
| data.europa.eu | https://data.europa.eu | EU open datasets catalog |
| CELLAR / EUR-Lex reuse | https://op.europa.eu/en/web/cellar/cellar-data · https://eur-lex.europa.eu/content/help/data-reuse/reuse-contents-eurlex-details.html | Legal text + SPARQL metadata |
| EP Open Data | https://data.europarl.europa.eu | Parliamentary activity |
| Congress.gov API | https://api.congress.gov | US comparative |
| Federal Register API | https://www.federalregister.gov/developers | US executive |

### C) What is / was in Errorlogy (local clone)

**Clone found:** `C:\Users\Public\ERRORLOGY_MVP` (also `repos/errorlogy` under umbrella). Prior sessions wired an **ingest info-stream layer** used with the MAS engine — US gov APIs + RSS + web search, not EU-complete yet.

| Artifact | Path / note |
|----------|-------------|
| Ingest package | `errorlogy-mas/mas/ingest/` |
| Fetchers | `rss`, `url`, `exa`, `federal_register`, `courtlistener`, `govinfo`, `oig`, `legiscan`, `openrouter_search`, `gemini_search` |
| US source config | `errorlogy-mas/data/ingest_sources_us.json` |
| RSS feeds | `errorlogy-mas/data/ingest_feeds.json` (BBC Politics, gov.uk, NASA, GAO) |
| CLI | `scripts/fetch_gov_media.py` (`--us-gov-only`, `--rss-only`) |
| API | `POST /api/ingest/fetch-all`, `fetch-us-gov` |
| Obsidian notes | `Ingest — info stream layer`, `Data Sources — overview`, `Data Sources — environments` |
| Provenance | US fetchers adapted from [democracy-monitor](https://github.com/agile-explorations/democracy-monitor) (**collection only** — no DM concern-scoring into μ) |
| Roadmap gap | H2 notes call for **EU/UK analogues** (NAO, EUR-Lex RSS) — not yet first-class fetchers |

**politic-bar** (`C:\Users\Public\POLITIC_BAR`): signal/noise stream **design** and cascade examples; product ingest services still largely future (`services/` planned). Umbrella owns institutional routing; politic-bar owns stream UX and politifi refs.

**errorlogy org on GitHub** (private/public siblings): `errorlogy`, `politic-bar`, `ai-native-gov`, `namm-experiments`, `eia`, `silovik-org` — no dedicated public “gov-mcp” product; ingest lives inside `errorlogy-mas`.

WMS `source_environment` tags already used / planned in Errorlogy (map adapters when emitting):

`parliamentary_inquiry`, `legal_judicial`, `audit_oversight`, `regulatory_agency`, `executive_branch`, `media_investigation`, `academic_research`, `whistleblowers`, `international_body`, `corporate_disclosure`, `civil_society`, `technical_literature`.

---

## EU-first priority sources (27-state simulator)

Ordered for Stage A / Phase 3–4 ([GLOBAL_AI_GOVERNANCE.md](../institutions/GLOBAL_AI_GOVERNANCE.md), [EU_TOPOLOGY.md](../institutions/EU_TOPOLOGY.md)):

| Priority | Source | Emits | Activates (typical) |
|----------|--------|-------|---------------------|
| 1 | EUR-Lex / CELLAR (API or MCP) | `gov_legislative_document` | `bloc:eu` parliament/judiciary analogs, national charter collision paths |
| 2 | European Parliament Open Data / EP MCP | `gov_parliamentary_activity` | EU parliament analog, national delegate aggregation cues |
| 3 | Eurostat Statistics API | `gov_open_data_snapshot` | Finance/economy ministries, ECOFIN-style regional context |
| 4 | data.europa.eu catalog datasets | `gov_open_data_snapshot` | Domain ministries by dataset theme |
| 5 | Commission / Council RSS or open endpoints (when wired) | `gov_executive_publication` | EU executive analog + national cabinets |
| 6 | National parliament MCPs (NL OpenTK, PL Sejm, …) | `gov_parliamentary_activity` | `state:{iso2}` parliament layers |
| 7 | Member-state open data portals (DE, FR, …) | mixed | National stacks per [EU_STATES.md](../institutions/EU_STATES.md) |
| 8 | Graded news RSS / Exa | `gov_news_signal` | Weak corroboration only |

Comparative US/UK sources remain valuable for cascade examples and Errorlogy continuity, but **do not block** EU-27 plug-in order.

---

## Parsing strategy

```text
1. Official structured API / SDK     → parse_method=official_api|sdk_client
2. Structured feed (RSS/Atom/JSON) → parse_method=structured_feed
3. MCP tool wrapping official API  → same as (1)/(2); record tool_call_id
4. HTML / PDF scrape               → parse_method=html_parse + quality_flags+=html_parsed
5. Human upload                    → parse_method=human_upload + provenance required
```

Rules:

1. Prefer **official API first**; MCP is a convenient agent bridge, not a higher authority than the underlying portal.
2. Never treat scraped HTML as strong evidence without human or secondary corroboration.
3. Deduplicate on `doc_id` / canonical URL before Scout/WMS.
4. Preserve original language when available; flag `translation_uncertain` if only translated text is used.
5. On failure: emit `gov_data_unavailable` (do not invent values).
6. Do **not** port democracy-monitor (or any) “concern scoring” into μ — ingest collection only ([ERRORLOGY.md](ERRORLOGY.md)).

---

## Routing — source classes → institutional layers

| Normalized event_type | Activated layers (examples) | Default epistemic label |
|-----------------------|----------------------------|-------------------------|
| `gov_open_data_snapshot` | `institution:executive`, ministry economy/finance analogs, `bloc:eu` fiscal coordination | `OPERATIONAL` |
| `gov_legislative_document` | `institution:parliament`, `institution:judiciary`, `bloc:eu` legal layers | `OPERATIONAL` |
| `gov_parliamentary_activity` | `institution:parliament`, national `state:{iso2}` parliament dials | `OPERATIONAL` |
| `gov_executive_publication` | `institution:executive`, regulatory-agency analogs | `OPERATIONAL` |
| `gov_judicial_docket` | `institution:judiciary` — dispute **surface**, not verdict | `OPERATIONAL` |
| `gov_audit_oversight_report` | `institution:audit`, parliament oversight | `OPERATIONAL` |
| `gov_news_signal` | parliament + executive (weak); politic.bar streams | `OPERATIONAL` |
| `gov_human_upload_parsed` | layers inferred from doc type + human tags | `OPERATIONAL` / `INSTITUTIONAL_MODEL` if framing-only |
| `gov_data_unavailable` | audit / observability | `OPERATIONAL` |

Fin-crypto events continue to route per [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md). Multi-jurisdiction shocks may activate many `state:{iso2}` instances plus `bloc:eu` without implying a single global authority.

---

## Downstream engine mapping

```text
gov-data adapter → normalized record → institutional framer (cross-layer-event)
                 → politic.bar stream_refs
                 → Errorlogy ingest/Scout → WMS → μ/α/PNO/FPD
                 → optional NAMM certificate_ref
```

Institutional context enters **before and alongside** WMS — it does not replace μ ([ERRORLOGY.md](ERRORLOGY.md)).

---

## Next steps / plug-in order

| Step | Action | Owner |
|------|--------|-------|
| 1 | Keep this doc as umbrella contract; link from GLOBAL_AI_GOVERNANCE ingress table | ai-native-gov |
| 2 | Install/evaluate **EP MCP** + **EUR-Lex MCP** (or EULEX hosted) in Cursor for EU agent workflows | local MCP config |
| 3 | Add Errorlogy fetchers: Eurostat + EUR-Lex/CELLAR (+ EP RSS) mirroring US `ingest_sources_us.json` pattern | errorlogy-mas |
| 4 | Adapter that maps ingest hits → `gov_*` event types → `cross-layer-event.json` | umbrella schema + child adapter |
| 5 | Wire NL/PL (OpenTK, Sejm) as first national parliament plugins for EU_STATES coverage | errorlogy-mas / MCP |
| 6 | politic.bar: attach `stream_refs` + `evidence_grade` for gov ingress items | politic-bar |
| 7 | Re-auth Exa MCP in Cursor for secondary `news_signal` discovery | Cursor MCP |
| 8 | Optional: TradingView MCP remain under FIN_CRYPTO sibling layer | FIN_CRYPTO |

Phase alignment: **Phase 2** (schema contracts) for event types; **Phase 4** (pipeline integration) for live cron/MCP → engine; **GLOBAL Stage D — Live ingress**.

---

## Links

- Sibling: [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md)
- Symbolic catalog: [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md) · ingest: [SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md)
- [ERRORLOGY.md](ERRORLOGY.md) · [POLITIC_BAR.md](POLITIC_BAR.md) · [NAMM.md](NAMM.md)
- [GLOBAL_AI_GOVERNANCE.md](../institutions/GLOBAL_AI_GOVERNANCE.md) — cross-cutting signal ingress
- [EU_TOPOLOGY.md](../institutions/EU_TOPOLOGY.md) · [EU_STATES.md](../institutions/EU_STATES.md)
- Schema: [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json)
