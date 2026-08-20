# Integration — Symbolic Visual Ingest (Instagram + Web)

How AI Native Gov discovers and registers **visual/symbolic candidates** from social and the open web into the symbolic graph — without scraping-as-production and without auto-minting rights claims.

**Epistemic label:** `INSTITUTIONAL_MODEL` for this contract. Adapter envelopes default to `OPERATIONAL`. Content hashes may become `COMPUTATIONAL_EVIDENCE` only with a NAMM `certificate_ref`. Provenance gaps stay incomplete — never upgraded to mint authority.

**Sibling contracts:** registry/graph = [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md); gov open data = [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md); markets/NFT trade = [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md).

---

## Purpose

Ingress adapters for **symbolic media candidates** that feed:

```text
discover → fetch metadata → hash blob → archetype/lore tag suggest (heuristic)
  → human review gate → register in SEED_CATALOG / symbolic graph
```

| Downstream | Role |
|------------|------|
| [SEED_CATALOG.md](symbolic/SEED_CATALOG.md) | Human-curated seed rows + SHA-256 |
| [`schemas/symbolic-asset.json`](../../schemas/symbolic-asset.json) | Symbol / Variant / MediaAsset shape |
| Symbolic graph | Edges (`has_media`, `derives_from`, …) after review |
| [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md) | Optional market events **only after** rights-cleared `minted_as` |

**Not claimed:** that Instagram posts or web images confer trademark, copyright clearance, or institutional legitimacy.

**Claimed (as model):** ingest produces **candidates** with provenance and `rights_status`; registration is gated; mint is never automatic from scrape.

---

## Preference order (hard)

Same spirit as GOV_DATA_SOURCES / FIN_CRYPTO: structured official surfaces first; scrape last and gated.

| Priority | Method | `parse_method` | Production mint / catalog claim? |
|----------|--------|----------------|----------------------------------|
| 1 | Official APIs (Meta Graph, museum/GLAM) | `official_api` | Yes, if license + `rights_status` allow |
| 2 | Creator-provided exports / DAM upload | `creator_export` / `human_upload` | Yes, with creator license recorded |
| 3 | Embeds / oEmbed / OpenGraph (public metadata) | `structured_feed` / `oembed` | Metadata OK; binary fetch still needs rights |
| 4 | RSS / Exa search MCP (discovery only) | `structured_feed` / `search_mcp` | Discovery only → review gate |
| 5 | Wayback / archive snapshots | `archive_fetch` | Analysis/provenance aid; license inherited from original |
| 6 | HTML scrape (IG or web) | `html_parse` | **No** — experimental, approval-gated; never production mint |

---

## Adapter interface

Normalized record (institutional framer may reference via `stream_refs` / map into [`cross-layer-event.json`](../../schemas/cross-layer-event.json)):

```json
{
  "adapter_id": "string (e.g. meta-graph:media_discover | exa:symbolic_search | europeana:object)",
  "record_id": "string (stable within adapter)",
  "story_id": "string|null",
  "event_type": "symbolic_media_discovered|symbolic_media_fetched|symbolic_provenance_incomplete|symbolic_rights_blocked|…",
  "observed_at": "ISO8601",
  "as_of": "ISO8601|null",
  "source_class": "social_official_api|creator_export|web_search|rss|oembed|glam_open_api|archive|html_scrape_experimental",
  "media": {
    "canonical_url": "string|null",
    "embed_url": "string|null",
    "mime_hint": "string|null",
    "content_hash": "string|null (sha256:… after fetch)",
    "cid": "string|null (ipfs://… optional)"
  },
  "provenance": {
    "creator_handle": "string|null",
    "platform": "instagram|web|europeana|met|rijks|wayback|other",
    "platform_media_id": "string|null",
    "license_hint": "string|null",
    "same_as": ["string URI …"]
  },
  "rights_status": "unknown|blocked|analysis_only|cleared_internal|cleared_merch|cleared_nft",
  "tag_suggest": {
    "lore_cluster": "string|null",
    "archetype_tags": ["string", "..."],
    "culture_refs": ["string", "..."],
    "ontology_refs": ["string URI …"]
  },
  "evidence_grade": "weak|medium|strong",
  "quality_flags": ["string", "..."],
  "uncertainty": {
    "confidence": "float [0,1]",
    "notes": "string|null"
  },
  "parse_method": "official_api|creator_export|oembed|structured_feed|search_mcp|archive_fetch|html_parse|human_upload",
  "review_gate": "pending|approved|rejected",
  "source_refs": {
    "provider_name": "string",
    "tool_call_id": "string|null",
    "raw_payload_ref": "string|null"
  }
}
```

### Normalized event types

| `event_type` | Default epistemic label | Intent |
|--------------|-------------------------|--------|
| `symbolic_media_discovered` | `OPERATIONAL` | Candidate URL/ID found (search, RSS, Graph listing, GLAM hit) |
| `symbolic_media_fetched` | `OPERATIONAL` | Metadata and/or blob retrieved; prefer hash present |
| `symbolic_provenance_incomplete` | `OPERATIONAL` | Missing creator, license, or durable identity of bytes |
| `symbolic_rights_blocked` | `OPERATIONAL` | Rights refuse auto-register / mint path |
| `symbolic_asset_registered` | `OPERATIONAL` | Passed human review → catalog/graph (see SYMBOLIC_VISUAL_LAYER) |
| `symbolic_media_variant` | `OPERATIONAL` | New rendition of existing Symbol |
| `symbolic_nft_mint_signal` | `OPERATIONAL` | Mint/metadata only after `rights_status` cleared for NFT |

Suggested `cross-layer-event.json` examples: `symbolic_media_discovered`, `symbolic_media_fetched`, `symbolic_provenance_incomplete`, `symbolic_rights_blocked` (see schema).

### Quality flags (non-exhaustive)

- `html_parsed` — scrape path used
- `tos_risk` — platform ToS / scraping risk
- `approval_gated` — requires human enablement
- `experimental` — not for production mint claims
- `partial_payload` — incomplete OG/oEmbed/Graph fields
- `hash_pending` — discovered but blob not yet hashed
- `license_unknown` — no machine-readable license
- `third_party_art` — not first-party AING mark
- `glam_open` — museum/open cultural data license path
- `rate_limited` / `key_required_missing` / `error_envelope`

---

## Instagram adapter

### Primary — Meta Graph API (Business / Creator)

| Item | Contract |
|------|----------|
| Surface | Instagram Graph API via Meta for **Business** or **Creator** accounts the operator controls (or has explicit partnership access to) |
| Discover | Media list / media object IDs for owned or authorized accounts |
| Fetch | Caption, permalink, media URL (where API permits), timestamp, owner |
| Emit | `symbolic_media_discovered` → `symbolic_media_fetched` |
| Rights | Still require explicit `rights_status`; API access ≠ NFT clearance |
| Secrets | App tokens / page tokens **never** in umbrella git |

Production registration and any mint signal require: Graph (or creator export) provenance **plus** human review **plus** `rights_status` ∈ {`cleared_internal`, `cleared_merch`, `cleared_nft`} as appropriate.

### Experimental — Instagram HTML scrape

| Item | Contract |
|------|----------|
| Status | **Experimental**, **approval-gated**, **not for production mint claims** |
| Risks | Fragile DOM/API changes; ToS and automation policy risk; incomplete provenance |
| Emit | May emit `symbolic_media_discovered` with `quality_flags: ["html_parsed","tos_risk","experimental","approval_gated"]` |
| Block | Prefer immediate `symbolic_rights_blocked` for any mint/NFT path; catalog register only as `analysis_only` after human gate |
| Hard rule | **Never auto-mint NFT from scraped Instagram media** |

Seed pack v0 (@tonybamber Odyssey/Athena stills) entered via **manual analysis path** into [`symbolic/SEED_CATALOG.md`](symbolic/SEED_CATALOG.md) — analysis only; not ownership for mint. See [`symbolic/seeds/README.md`](symbolic/seeds/README.md).

---

## General web adapters

| Source | Role | Typical emit |
|--------|------|--------------|
| **Exa / search MCP** | Discovery of neoclassical remakes, heraldry refs, lore carriers | `symbolic_media_discovered` (`source_class=web_search`) |
| **RSS / Atom** | Creator or museum feeds | `symbolic_media_discovered` |
| **OpenGraph / oEmbed** | Title, image URL, site name without full page scrape | `symbolic_media_fetched` (metadata); blob fetch separate |
| **Wayback Machine** | Historical snapshots for provenance / disappearance | `symbolic_media_fetched` + archive flags; license from original |
| **Europeana** | Classical / European cultural objects (open API) | discover/fetch with `glam_open` |
| **Met Collection API** | Open-access object metadata + images where CC0/open | same |
| **Rijksmuseum API** | Dutch collection open images | same |

GLAM/open APIs are preferred for **classical lore remakes** and ontology `same_as` / `ontology_refs` (Wikidata, Iconclass, Getty AAT) over scraping contemporary social posts.

Parsing ladder:

```text
1. Official API / GLAM          → official_api
2. Creator export / human upload → creator_export | human_upload
3. oEmbed / OpenGraph / RSS      → oembed | structured_feed
4. Exa / search MCP              → search_mcp (discovery)
5. Wayback                       → archive_fetch
6. HTML scrape                   → html_parse + experimental flags
```

---

## Pipeline (discover → catalog)

```text
1. Discover
   Exa/RSS/Graph/GLAM → symbolic_media_discovered
2. Fetch metadata
   oEmbed / Graph / museum JSON → symbolic_media_fetched
   (if rights unclear → keep rights_status=unknown)
3. Hash blob (when fetch allowed)
   SHA-256 (or IPFS CID) on bytes → MediaAsset.content_hash
   Missing creator/license → symbolic_provenance_incomplete
4. Archetype / lore suggest (heuristic)
   Jungian method card + lore_cluster from SYMBOLIC_VISUAL_LAYER
   tag_suggest only — never clinical or legitimacy verdict
5. Human review gate
   review_gate=approved|rejected
   rights_status must be set explicitly
   blocked → symbolic_rights_blocked (stop mint/register-as-cleared)
6. Register
   Write/update SEED_CATALOG row and/or symbolic-asset stub
   → symbolic_asset_registered
   Optional FIN_CRYPTO mint signal only if rights_status=cleared_nft
```

Activated layers for envelopes: typically `institution:symbolic-visual`; optional bindings to executive/UI surfaces after register.

---

## Rights (non-negotiable)

| Rule | Detail |
|------|--------|
| `rights_status` **required** on every fetched/register path | Default `unknown` until set |
| No auto-mint from scraped IG | Scrape → at most `analysis_only` after review |
| Third-party seeds in git | Analysis / visual-code study — not ownership |
| GOV open emblems | Via [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md) with `source_class=official_open_data`; still not sovereignty |
| FIN_CRYPTO join | Floor/volume only for collections already `minted_as` with clearance |

---

## Routing → layers

| Event | Activated layers (examples) | Notes |
|-------|----------------------------|-------|
| `symbolic_media_discovered` | `institution:symbolic-visual` | Weak; discovery only |
| `symbolic_media_fetched` | `institution:symbolic-visual` | Hash when possible |
| `symbolic_provenance_incomplete` | `institution:symbolic-visual`, `institution:audit` | Block upgrade |
| `symbolic_rights_blocked` | `institution:symbolic-visual`, `institution:audit` | Hard stop on mint |
| `symbolic_asset_registered` | `institution:symbolic-visual` (+ bindings) | Post-review |

---

## Plug-in order

1. **Human upload / creator export** — safest path into seeds + CAS hash.
2. **Meta Graph API** (owned/authorized IG) — primary social ingress.
3. **GLAM open APIs** (Europeana, Met, Rijks) — classical lore + open licenses.
4. **Exa / RSS / oEmbed** — discovery and metadata enrichment.
5. **Wayback** — provenance aid.
6. **IG/web HTML scrape** — experimental only; approval-gated; never production mint.
7. **Register → SEED_CATALOG / symbolic-asset** — human gate.
8. **Optional NAMM** on content hash; **optional FIN_CRYPTO** mint/trade join.

Phase: **Phase 2** contract (this doc + event examples); **Phase 4** live adapters in child repos / MCP.

---

## Links

- Registry / lore / Jungian tags: [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md)
- Seed catalog: [symbolic/SEED_CATALOG.md](symbolic/SEED_CATALOG.md)
- Seed binaries: [symbolic/seeds/](symbolic/seeds/)
- Schema asset: [`schemas/symbolic-asset.json`](../../schemas/symbolic-asset.json)
- Events: [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json)
- Gov open data: [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md)
- Markets: [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md)
- Meta Instagram Graph API: https://developers.facebook.com/docs/instagram-api/
- Europeana API: https://pro.europeana.eu/page/apis
- Met Collection API: https://metmuseum.github.io/
- Rijksmuseum API: https://data.rijksmuseum.nl/
