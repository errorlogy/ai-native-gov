# CMS Fit — Layer-by-Layer Platform Analysis

**Epistemic label:** `INSTITUTIONAL_MODEL` — architectural compatibility framing, not a claim of sole correct stack or replacement of real-world governance systems.

**Related:** [ARCHITECTURE.md](../../ARCHITECTURE.md) · [MVP_ITERATIONS.md](../examples/MVP_ITERATIONS.md) · [CONNECTION_GUIDE.md](../integrations/CONNECTION_GUIDE.md)

---

## AI Native Gov is not one CMS site

AI Native Gov is an **umbrella repository**: institutional topology, integration contracts, schemas, and cascade examples. Product runtime lives in child repos:

| Repository | Stack | Role |
|------------|-------|------|
| `ai-native-gov` | Git + Markdown + JSON Schema | Contracts, topology, vision |
| `errorlogy-mas` | **FastAPI** + SQLite/Postgres | Simulator, ingest, institutions stub |
| `errorlogy-gui-v2` | **React/Vite** | Topology map, event feeds |
| `politic-bar` | CLI + streams/cards | Politifi, signal/noise |
| `namm-experiments` | CLI | Verification certificates |

**Correct question:** which layers need a content system vs API, database, graph, or static assets — not "which single CMS implements AI Native Gov."

```text
┌─────────────────────────────────────────────────────────────┐
│  Signal ingress (gov APIs, fin-crypto, symbolic, NAMM)      │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│  Umbrella: topology + schemas (Git/MD — not CMS)            │
└──────────────────────────┬──────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   FastAPI runtime    politic.bar        Symbolic registry
   (NOT CMS)           (headless/static)  (DAM/graph/IPFS)
```

---

## Layer vs system type

| Layer | What is stored | Current stack | System type | CMS appropriate? |
|-------|----------------|---------------|-------------|------------------|
| **Umbrella: docs & topology** | `TOPOLOGY.md`, `EU_STATES.md`, integration contracts | Git + MD | Docs-as-code | Optional headless for non-dev editors |
| **Institutional simulator runtime** | `cross-layer-event`, activation stub, event store | FastAPI + SQLite/Postgres | **Application DB + API** | **No** — not a content site |
| **gui-v2 (EU map, event feed)** | Static topology, polling API | React + `public/eu-topology.json` | SPA + static JSON | CMS not needed; JSON from Git or headless export |
| **politic.bar streams/cards** | Story anchors, signal/noise, politifi refs | CLI, JSON streams | Pipeline + headless **or** static JSON | Headless (Phase 2–4) or Git JSON in MVP |
| **Symbolic visual registry** | Seeds, SHA-256, `symbolic-asset.json`, graph edges | Git seeds + MD catalog | **DAM + knowledge graph + IPFS** | Not WordPress; DAM or custom graph |
| **Symbolic ingest** | Instagram/web candidates → review gate | Adapter contract | Ingest pipeline | Discovery via APIs/MCP; catalog via DAM |
| **EU state profiles** | 27 national instances, dials, collision taxonomy | MD + future `state-profile.json` | **Structured data (JSON Schema)** | Optional collection types in headless CMS |
| **Gov data ingress** | Eurostat, EUR-Lex, parliamentary feeds | FastAPI fetchers (`/api/ingest/*`) | **Official APIs + normalized records** | **APIs, not CMS** |
| **Fin-crypto / NFT markets** | CCXT snapshots, OpenSea/Alchemy MCP | Adapters → `fin_crypto_*` events | **Market adapters** | On-chain + market APIs; collection metadata — headless or on-chain |
| **Public lore / ideology site** | PHILOSOPHY, VISION, Anthemium narrative | No separate site yet | Marketing/docs site | **Traditional or static CMS** — only layer where WP/Drupal fit |
| **MatrAIx personas** | ~1M persona records, cohort tags | HuggingFace dataset + sidecar metadata | **Dataset / ML infra** | **Not CMS** — Parquet/JSON + optional vector DB |

### Layer notes

- **Umbrella (Git + MD):** Optimal for agents and versioned contracts. Headless CMS (Strapi, Directus, Payload) helps when non-developers edit institution copy, EU profiles, or integration blurbs with preview → export to Git.
- **Simulator runtime (FastAPI):** MVP per [MVP_ITERATIONS.md](../examples/MVP_ITERATIONS.md) — `POST /api/institutions/activate`, event store, CCXT adapter. Stateful API + relational/event store, not editorial CMS.
- **politic.bar:** Structured stream items with `evidence_grade`, `institution:*` refs. MVP: static JSON in Git + CLI; Phase 2–4: headless CMS with custom content types synced to child repo.
- **Symbolic layer:** Registry + graph (`has_media`, `derives_from`, `minted_as`). Multimodal assets, IPFS CID, rights gates → **DAM + graph** (Neo4j, Wikibase, Directus relations).
- **Gov / Fin ingress:** Adapter contracts per [GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md) and [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md). Eurostat REST, CCXT, OpenSea MCP — CMS does not replace fetchers.

---

## CMS categories matrix

| Category | Examples | Fit for AI Native Gov | Layers |
|----------|----------|----------------------|--------|
| **Headless CMS** | Strapi, Directus, Payload, Sanity, Contentful | **High** (Phase 2–4) | Institution copy, EU profiles, politic.bar story metadata, symbolic catalog rows, NFT off-chain metadata |
| **Traditional CMS** | WordPress, Drupal | **Low for core; medium for public site** | Public lore/docs/marketing only |
| **Static site generators** | Astro, Next.js, Hugo, Eleventy | **High for docs/lore** | Umbrella public mirror, philosophy site |
| **DAM** | Bynder, Cloudinary, ResourceSpace, Directus files | **High for symbolic** | Seeds, seals, merch marks, video identity, review-gated media |
| **Knowledge graph** | Neo4j, Wikibase, Apache Jena | **High for symbolic + topology** | Symbol↔token edges, institution layer graph, EU collision taxonomy |
| **Commerce / NFT metadata** | Shopify, Manifold, thirdweb (off-chain) | **Narrow, Phase 5** | Merch drops, NFT traits; execution wallet-gated per [CONNECTION_GUIDE.md](../integrations/CONNECTION_GUIDE.md) |
| **Application runtime** | FastAPI, Postgres, SQLite | **Required for simulator** | Institutions stub, ingest, adapters — **not a CMS category** |
| **Dataset / ML** | HuggingFace, Parquet, feature stores | **MatrAIx only** | Persona cohorts — not editorial CMS |

### Platform × layer matrix

| Platform | Umbrella docs | Simulator | politic.bar | Symbolic | Gov/Fin ingress | Public lore |
|----------|:-------------:|:---------:|:-----------:|:--------:|:---------------:|:-------------:|
| Git + MD | ✅ primary | — | MVP | seeds v0 | — | — |
| FastAPI + DB | — | ✅ primary | — | — | ✅ adapters | — |
| Headless CMS | ○ optional | ✗ | ○ Phase 2+ | ○ catalog | ✗ | ○ |
| WordPress/Drupal | ✗ | ✗ | ✗ | ✗ | ✗ | ○ Phase 4–5 |
| Astro/Next static | ○ mirror | — | ○ | — | — | ✅ good |
| DAM + Graph | — | — | — | ✅ primary | — | — |
| Market APIs (CCXT, OpenSea) | — | ✅ | — | ○ mint metadata | ✅ primary | — |

✅ = recommended · ○ = optional · ✗ = do not use for this layer

---

## Phase recommendations

| Phase | CMS strategy | Rationale |
|-------|--------------|-----------|
| **MVP (Phase 0–1, iter 1–3)** | **No CMS.** Git + MD + FastAPI + static JSON in gui-v2 | Validated: institutions stub, `/topology`, CCXT adapter. Minimum moving parts. |
| **Phase 2 — Schema contracts** | Git remains source of truth for schemas; headless **not required** | `signal-envelope`, `institutional-output` — JSON Schema, not editorial pages. |
| **Phase 2–3 — Non-dev editors** | **Headless** (Directus or Payload self-host; Sanity/Contentful managed) | EU state profile fields, institution descriptions, symbolic catalog rows after review gate. Export/sync → Git or FastAPI API. |
| **Phase 3 — Machine-readable topology** | **Graph DB** (Neo4j) or JSON graph in repo + optional Wikibase | `TOPOLOGY.md` → queryable graph; page builder CMS not suitable. |
| **Phase 4 — Pipeline integration** | politic.bar: headless **or** Git JSON + CI; symbolic: DAM | Streams published via pipeline, not WP admin. |
| **Phase 4–5 — Public site** | **Static (Astro/Next)** or **WordPress** for lore/marketing only | errorlogy.com / philosophy / Anthemium — separate from simulator. |
| **Phase 5 — NFT/merch** | Manifold/thirdweb off-chain + optional Shopify | Mint stays human-approved per CONNECTION_GUIDE; not CMS-as-blockchain. |

### Default stack trajectory

```text
MVP:     Git + FastAPI + React gui-v2
Phase 2: + Directus OR Payload (self-host, EU profiles + institution copy)
Phase 3: + Neo4j OR structured JSON graph (topology)
Phase 4: + politic.bar headless sync OR static pipeline
Phase 5: + Astro public site + optional WP for blog-only
```

---

## Anti-patterns

| Anti-pattern | Why |
|--------------|-----|
| **WordPress as "government engine"** | No event-sourced institutional activation, no typed adapters (gov/fin/symbolic), conflates content with runtime state |
| **Drupal for realtime market/gov ingest** | CMS batch ETL — latency, no OPERATIONAL envelope pipeline |
| **Any CMS as sole source of truth for schemas** | Contracts must be versioned in Git (`schemas/*.json`); CMS is derivative or editorial layer |
| **Shopify/Magento for institutions** | Commerce ≠ institutional topology |
| **Notion/Confluence as runtime registry** | No API contract, no `epistemic_label`, no cross-repo CI |
| **MatrAIx dataset as "persona CMS"** | Large-scale records ≠ editorial content; cohort tags are sidecar metadata |
| **Instagram/Pinterest scrape → auto-mint via CMS plugin** | Violates symbolic contract: review gate + `rights_status` required |

---

## Epistemic note (`INSTITUTIONAL_MODEL`)

No CMS platform should emit outputs labeled "legitimate ruler," "guilty," or "sovereign AI government." UI and CMS copy use **institutional framing** and **legitimacy signals (modeled)** only.

Language rules shared with Errorlogy / politic.bar:

| Use | Never use |
|-----|-----------|
| analytical contribution | guilty, criminal |
| fuzzy membership μ | proven guilt |
| legitimacy **signals** (modeled) | legitimate ruler (verdict) |
| institutional framing | sovereign AI government |
| possible / consistent with | "this proves" |

---

## Summary

Full AI Native Gov implementation does **not** reduce to one CMS:

1. **Core (simulator + adapters)** — **not CMS**: FastAPI + Postgres/SQLite + React gui-v2.
2. **Contracts & topology** — **Git + MD** (current optimum); headless optional for editors.
3. **Streams/cards (politic.bar)** — headless CMS **or** static JSON pipeline.
4. **Symbolic identity** — **DAM + graph + IPFS**, not classic CMS.
5. **Gov/fin ingress** — **APIs and adapters** (Eurostat, CCXT, OpenSea MCP).
6. **Public lore site** — only layer where WordPress/Drupal/Astro are normal choices.
7. **MatrAIx** — **dataset**, not CMS.

**Today (MVP):** CMS **not required**.  
**Phase 2–3:** headless (Directus / Payload / Sanity) for structured editorial data.  
**Phase 4–5:** optional public CMS (Astro preferred; WordPress acceptable for marketing only).
