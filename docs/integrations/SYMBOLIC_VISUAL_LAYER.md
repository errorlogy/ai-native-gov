# Integration — Symbolic / Visual Identity Layer

How AI Native Gov registers and relates **symbolic visual code** — coats of arms, logos, merch/clothing marks, NFT collections, images, drawings, video, and other multimodal identity assets — without treating symbols as legitimacy verdicts.

**Epistemic label:** `INSTITUTIONAL_MODEL` for this contract document. Catalog entries and adapter envelopes default to `OPERATIONAL`. Provenance hashes and NFT mint records may become `COMPUTATIONAL_EVIDENCE` only when a NAMM `certificate_ref` is linked.

---

## Purpose

This layer is the **registry + graph contract** for symbolic visual identity used across:

| Surface | Examples |
|---------|----------|
| Institutional simulator UI | Seals, layer badges, jurisdiction marks, charter emblems |
| Simulated heraldry analogs | National/EU-style coats, party marks, bloc symbols (modeled, not sovereign claims) |
| Product / merch | AI Native Gov clothing marks, logos, print variants |
| NFT / collectible drops | Collections minted from catalog assets; traits as structured attributes |
| Media library | Stills, drawings, video, motion identity packages |

It sits beside [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md) (market/NFT trade signals), [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md) (official open-data coats/marks when ingested), and [SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md) (Instagram/web discovery → review gate → catalog), upstream of institutional framing and optional NAMM verification.

**Not claimed:** that a mark confers real-world legal authority, trademark exclusivity as a court finding, or that NFT ownership proves institutional legitimacy.

**Claimed (as model):** symbols are cultural/institutional **signals** with provenance, license, and binding edges that agents and UIs can query consistently.

**Seed pack (v0):** six analysis images live under [`symbolic/seeds/`](symbolic/seeds/) with catalog tags in [`symbolic/SEED_CATALOG.md`](symbolic/SEED_CATALOG.md). Third-party art — analysis only; not ownership for mint.

---

## Lore axis (INSTITUTIONAL_MODEL)

AI Native Gov visual identity is framed on two complementary axes. Neither is a civilizational verdict; both are **aesthetic / ideological modeling lenses** for catalog tags (`lore_cluster`).

### External lore cluster — Mediterranean antiquity remade

| Ingredient | Role in the simulator |
|------------|------------------------|
| Ancient Greece | Athena / warrior / Odyssey cinematic grammar (strategy, craft, ordeal) |
| Roman Empire | Laurel, civic honor, monumental order as identity codes |
| 21st-century digital remakes | Instagram/AI-art neoclassical stills as successful *contemporary* carriers of those codes (see @tonybamber Odyssey/Athena seeds) |
| Egyptian monumental | Temple / colossus / sacred ascent as “container” images (seed-egypt-temple) |

### Internal axis — scientific-technical progress (SYNTHEΣ)

| Ingredient | Role |
|------------|------|
| Classical human form | Continuity with Greco-Roman visual grammar |
| Geometric / technical overlay | Diagrams, meridians, Σ (summation), eye-on-chest = **synthesis** of form + tech (EIDA, SYNTHEΣ seeds) |
| Progress ideology | Identity signal for error-minimizing, knowledge-extending institutions — paired with [PHILOSOPHY.md](../PHILOSOPHY.md) (*Homo loquens* / cognitive extension), **not** a claim that tech confers sovereignty |

```
External: Greco-Roman + Egypt remakes  ──►  shared antiquity grammar
Internal: EIDA / SYNTHEΣ progress      ──►  classical + technical overlay
```

---

## Analysis methods (heuristic — not academic or clinical verdicts)

### Jungian method card (primary tagging vocabulary)

**Cite:** C. G. Jung et al., *Man and His Symbols* — use as a **method frame** for archetype tags. **Do not** dump verbatim book text or PDFs into this repo (copyright).

| Tag family | Modeling use on `archetype_tags[]` | Seed examples |
|------------|------------------------------------|---------------|
| **Warrior / Hero** | Ordeal, defense, force-as-signal | seed-warrior-odyssey |
| **Wise Youth** | Insight, initiation, unfinished phase | EIDA, SYNTHEΣ, Athena stills |
| **Anima / Athena** | Counsel, craft, strategic intelligence | seed-athena-01/02 |
| **Self / eye** | Integration mark; inner vision; geometric center | seed-synthes-eye, EIDA nodes |
| **Temple / sacred space** | Container for collective symbols; threshold | seed-egypt-temple |
| **Shadow** | Optional opposite tag (e.g. Warrior without Athena = force without counsel) | catalog notes |

**Collective unconscious (modeling only):** treat shared visual codes (laurel, temple, eye, crest) as *reusable cultural signals* agents can cluster — not as proof of universal psyche or of institutional legitimacy.

Epistemic default for Jungian readings: `INSTITUTIONAL_MODEL` or `PHILOSOPHICAL_INFERENCE` — never upgrade to `COMPUTATIONAL_EVIDENCE` without NAMM on *bytes/provenance*, and never treat archetype tags as psychological diagnosis.

### Adjacent practices (optional, short)

| Practice | Use in this layer | Guardrail |
|----------|-------------------|-----------|
| **Semiotics** | Signifier/signified pairs for marks (crest → martial authority *signal*) | Denotation ≠ legal authority |
| **Heraldic grammar** | Blazon-like fields for simulated coats (tincture, charge, crest) | Simulated heraldry only |
| **Sacred geometry as visual grammar** | Circles, axes, vesica as *composition rules* (EIDA/SYNTHEΣ) | Not mysticism-as-truth |

---

## External ontological libraries (reference — don’t dump)

Prefer **URI pointers** in `ontology_refs[]` / `culture_refs[]` / `same_as[]`:

| Library | What to use it for |
|---------|-------------------|
| [Wikidata](https://www.wikidata.org/) | Entity QIDs (Athena, Corinthian helmet, Abu Simbel, …) |
| [Iconclass](https://iconclass.org/) | Art-historical subject codes for myth/scene classes |
| [Getty AAT](https://www.getty.edu/research/tools/vocabularies/aat/) | Object/motif type vocabulary (helmets, columns, laurel wreaths) |
| schema.org | `ImageObject` / `CreativeWork` JSON-LD when publishing public pages |

Schema fields for analysis: `archetype_tags[]`, `culture_refs[]`, `lore_cluster`, `usage_contexts[]`, optional `ontology_refs[]` — see [`schemas/symbolic-asset.json`](../../schemas/symbolic-asset.json).

---

## Seed catalog (v0)

| Seed id | Lore cluster | Primary archetype tags |
|---------|--------------|------------------------|
| seed-warrior-odyssey | greco-roman-neoclassical-digital | Warrior, Hero |
| seed-athena-01 | greco-roman-neoclassical-digital | Anima, Athena, WiseYouth |
| seed-athena-02 | greco-roman-neoclassical-digital | Anima, Athena, WiseYouth |
| seed-egypt-temple | egyptian-monumental | Temple, SacredSpace, Self |
| seed-eida-geometry | progress-synthesis | WiseYouth, Self |
| seed-synthes-eye | progress-synthesis | Self, Scholar, WiseYouth |

Full visual-code notes + SHA-256: [`symbolic/SEED_CATALOG.md`](symbolic/SEED_CATALOG.md). Provenance/license: [`symbolic/seeds/README.md`](symbolic/seeds/README.md).

---

## Research snapshot (current practice)


| Domain | Current best practice (summary) | Implication for MVP |
|--------|----------------------------------|---------------------|
| Brand / symbol ontologies | Public web: JSON-LD + schema.org `Organization`/`logo` + Wikidata `sameAs` QIDs; internal: property graphs (Neo4j/Memgraph) with optional RDF/OWL via neosemantics when W3C exchange is required | Umbrella: JSON graph stubs now; property graph DB later |
| NFT metadata | ERC-721 `tokenURI` / ERC-1155 `uri` → JSON (`name`, `description`, `image`, `attributes` traits); storage: hosted URL, `ipfs://` CID, Arweave, or on-chain data URI | Treat mint metadata as edge to `MediaAsset` + optional market events via FIN_CRYPTO |
| DAM + CAS | DAM owns workflow/metadata; content-addressed storage (hash/CID) for binaries; optional on-chain anchor of CID for provenance | Local hash or IPFS CID in schema; binaries out of git |
| Design tokens / brand registries | Token registries (color/type/icon) + DAM as single source of truth for approved marks | `Variant` + `UsageContext` model token-like constraints without inventing sovereignty |
| Multimodal catalogs | Metadata graph + embeddings optional; provenance and rights remain first-class | Graph + CAS primary; vector search optional Phase 4+ |

Primary recommendation aligns with industry default: **property graph for relations + content-addressed blobs for media**, with schema.org/JSON-LD-shaped node documents in umbrella schemas until a graph engine is wired.

---

## Recommended architecture (MVP)

### Primary: property graph + content-addressed blobs

**Why this wins for AI Native Gov**

1. Symbolic identity is **relational** (derives_from, used_by_institution, minted_as) — property graphs express this without RDF triple explosion.
2. Binaries must be **content-addressed** (SHA-256 / IPFS CID) so NFT metadata, UI caches, and NAMM certificates can agree on the same bytes.
3. Umbrella stays contract-only: ship **JSON node/edge stubs** (schema.org-like fields) now; Neo4j or Memgraph later as child-repo or infra plugin.
4. Matches FIN_CRYPTO NFT path: market adapters emit trade/mint *signals*; this layer owns the *catalog graph*.

```
┌─────────────────────────────────────────────────────────────────┐
│  Umbrella schemas (now)                                         │
│  symbolic-asset.json  ·  cross-layer-event.json                  │
│  nodes: Symbol, Variant, MediaAsset, Collection, …              │
│  edges: derives_from, variant_of, used_by_institution, …        │
└───────────────────────────────┬─────────────────────────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Blob store      │   │ Graph runtime   │   │ Market ingress  │
│ local CAS /     │   │ (later) Neo4j / │   │ FIN_CRYPTO      │
│ IPFS CID pin    │   │ Memgraph        │   │ mint/trade evt  │
└─────────────────┘   └─────────────────┘   └─────────────────┘
```

### Alternatives (compared, not chosen for MVP)

| Approach | Strengths | Weaknesses for this layer |
|----------|-----------|---------------------------|
| **Pure SQL DAM** | Strong ACID, familiar ops, good for file workflows | Weak multi-hop “who may use this seal in which jurisdiction” queries; graph is bolted on |
| **RDF triple store** | W3C interoperability, OWL reasoning, Wikidata alignment | Heavier ontology upfront; overkill for MVP simulator + merch catalogs |
| **Vector + metadata only** | Fast multimodal similarity search | Poor provenance/license/binding semantics; embeddings ≠ registry of record |

**Later (optional):** RDF export via JSON-LD `@context` for Wikidata/`sameAs` alignment; vector index as a *search* overlay, never as sole catalog.

---

## Entity model

All entities below are `INSTITUTIONAL_MODEL` / `OPERATIONAL` catalog objects unless certified.

| Entity | Role |
|--------|------|
| **Symbol** | Abstract identity unit (e.g. “AI Native Gov primary mark”, “state:fr simulated coat analog”) |
| **Variant** | Concrete design revision (colorway, mono, embroidery, seal size) |
| **MediaAsset** | Binary-backed image/video/drawing; content hash or CID required |
| **Collection** | NFT drop, merch line, or bundled set of variants |
| **Provenance** | Creator, source system, parent hash chain, optional on-chain anchor |
| **License** | Usage terms slug (internal-sim, CC-BY, proprietary-merch, etc.) — not a legal verdict |
| **InstitutionalBinding** | Which institution layer / state / party / bloc may display or mint the symbol |
| **UsageContext** | Where it appears: `gov-sim-ui`, `clothing`, `nft-drop`, `seal`, `charter-mark`, `politifi-card`, `analysis-seed` |
| **Analysis fields** | `archetype_tags[]`, `culture_refs[]`, `lore_cluster`, `ontology_refs[]` (Jungian/semiotic tags + external ontology URIs) |

Minimal machine shape: [`schemas/symbolic-asset.json`](../../schemas/symbolic-asset.json).

### Graph relations

| Edge type | From → To | Meaning |
|-----------|-----------|---------|
| `derives_from` | Symbol/Variant → Symbol | Lineage / redesign from prior mark |
| `variant_of` | Variant → Symbol | Concrete rendering of abstract symbol |
| `used_by_institution` | Symbol/Variant → InstitutionalBinding target | Allowed display binding (modeled) |
| `minted_as` | Variant/MediaAsset → Collection (NFT token ref) | Catalog asset linked to mint metadata |
| `references_charter_mark` | Symbol → charter/seal Symbol | Simulator seal referencing charter identity |
| `has_media` | Variant → MediaAsset | Binary attachment |
| `licensed_under` | Symbol/Variant/Collection → License | Rights signal for downstream UI/merch |

Layer ID for activation envelopes: `institution:symbolic-visual` (see [`institution-layer-id.json`](../../schemas/institution-layer-id.json)).

---

## Epistemic rules

| Situation | Label | Rule |
|-----------|-------|------|
| Registry entry, UI bind, merch SKU | `OPERATIONAL` | Catalog fact; cultural/institutional **signal** only |
| Framing “how seals work in the simulator” | `INSTITUTIONAL_MODEL` | This document and topology hypotheses |
| Content hash / CID verified + NAMM cert | `COMPUTATIONAL_EVIDENCE` | Provenance of bytes, not legitimacy of a government |
| NFT marketplace price/volume | via FIN_CRYPTO → usually `OPERATIONAL` | Market context; not “authentic state seal” |
| Philosophical / Jungian reading of marks | `PHILOSOPHICAL_INFERENCE` or `INSTITUTIONAL_MODEL` | Tagging vocabulary only; not clinical or legitimacy proof |
| Third-party seed art in repo | `INSTITUTIONAL_MODEL` analysis | Not ownership; no mint without rights clearance |

Language (shared with [AGENTS.md](../../AGENTS.md) / [PHILOSOPHY.md](../PHILOSOPHY.md)):

| Use | Never use |
|-----|-----------|
| institutional mark / modeled heraldry analog | legitimate seal of state (verdict) |
| NFT = catalog + optional provenance evidence | NFT proves sovereignty |
| cultural / identity **signals** | this proves rightful authority |
| archetype **tags** (heuristic) | Jungian diagnosis / universal truth claim |

Symbols do **not** upgrade institutional outputs to verdicts. A coat of arms in the graph is a coordination and branding artifact inside the simulator and product surfaces.

---

## Cross-layer event types

Normalized `event_type` strings for [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json):

| `event_type` | Default epistemic label | Intent |
|--------------|-------------------------|--------|
| `symbolic_media_discovered` | `OPERATIONAL` | Candidate URL/ID from IG Graph, Exa, RSS, GLAM, or gated scrape ([SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md)) |
| `symbolic_media_fetched` | `OPERATIONAL` | Metadata and/or blob retrieved; prefer content hash |
| `symbolic_provenance_incomplete` | `OPERATIONAL` | Missing creator, license, or durable byte identity |
| `symbolic_rights_blocked` | `OPERATIONAL` | Rights refuse auto-register / mint path |
| `symbolic_asset_registered` | `OPERATIONAL` | New Symbol / MediaAsset / Collection entered in registry (post review) |
| `symbolic_nft_mint_signal` | `OPERATIONAL` (→ `COMPUTATIONAL_EVIDENCE` if NAMM-linked) | Mint or metadata URI observed; may also emit FIN_CRYPTO market events |
| `symbolic_media_variant` | `OPERATIONAL` | New Variant or media rendition of an existing Symbol |

Typical `activated_layers`: `institution:symbolic-visual` plus relevant bindings (`institution:executive`, `institution:national-instance`, EU layers, etc.). Ingest-only events stay on `institution:symbolic-visual` (+ audit when blocked/incomplete).

Example envelope (illustrative):

```json
{
  "story_id": "2026-aing-identity-pack-v1",
  "event_type": "symbolic_asset_registered",
  "activated_layers": ["institution:symbolic-visual", "institution:executive"],
  "jurisdiction_set": ["global"],
  "stream_refs": ["symbolic:symbol:aing-primary"],
  "epistemic_label": "OPERATIONAL"
}
```

---

## Sibling integrations

| Sibling | Boundary |
|---------|----------|
| [SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md) | Instagram (Graph primary; scrape experimental) + web (Exa, RSS, oEmbed, Wayback, GLAM) → candidates → human gate → this registry |
| [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md) | Floor price, volume, listing, on-chain risk for NFT collections → market event types; **this layer** owns symbol↔token catalog edges (`minted_as`) |
| [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md) | Official open-data coats, flags, emblem APIs (when available) → ingest as `MediaAsset` + `Provenance` with `source_class=official_open_data`; never treat as sovereignty upgrade |
| [NAMM.md](NAMM.md) | Optional certificate over content hash / graph invariant of a collection |
| [POLITIC_BAR.md](POLITIC_BAR.md) | Card/UI surfaces may reference `politifi` or symbol slugs via `stream_refs` |
| [ERRORLOGY.md](ERRORLOGY.md) | Does not reimplement μ/α here; symbolic events are weak context unless certified |
| [PHILOSOPHY.md](../PHILOSOPHY.md) | Homo loquens / progress-as-cognitive-extension frame for SYNTHEΣ axis |

---

## MVP schema stub plan

1. **Now (umbrella):** [`schemas/symbolic-asset.json`](../../schemas/symbolic-asset.json) — Symbol / Variant / MediaAsset / Collection + analysis fields (`archetype_tags`, `culture_refs`, `lore_cluster`, `ontology_refs`).
2. **Now:** `institution:symbolic-visual` layer id; cross-layer events `symbolic_*`; seed binaries + [`SEED_CATALOG.md`](symbolic/SEED_CATALOG.md).
3. **Phase 1–2:** child-repo parsers validate stubs; store blobs under local CAS (`sha256:…`) or pin to IPFS (`ipfs://…`).
4. **Phase 3:** machine-readable edge list export compatible with `institution-graph.json` style (or dedicated `symbolic-graph.json` if needed).
5. **Phase 4:** Neo4j/Memgraph load; FIN_CRYPTO mint/trade adapters join on `collection_id` / contract+tokenId; optional vector index for similarity search.
6. **Phase 5:** agent playbooks for “register mark”, “bind to state profile”, “tag archetypes”, “emit mint signal”.

Do **not** copy large binary packs, full NFT metadata dumps, or copyrighted books (e.g. Jung PDFs) into this repo — reference by hash/CID/citation.

---

## Plugin / adapter order

1. **Local CAS registrar** — hash file → `MediaAsset` record → `symbolic_asset_registered`.
2. **Symbol + Variant editor** — JSON stubs + InstitutionalBinding / UsageContext / archetype tags.
3. **Seed / lore tagger** — apply `lore_cluster` + Jungian method card; link Wikidata/Iconclass/AAT URIs.
4. **Social + web ingest** — [SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md): Meta Graph (primary), Exa/RSS/oEmbed/GLAM; IG scrape experimental only; human review before catalog.
5. **Open-data emblem ingest** (optional) — GOV_DATA_SOURCES adapter → MediaAsset with official provenance flags.
6. **NFT metadata mapper** — ERC-721/1155 OpenSea-style JSON → Collection + `minted_as` edges → `symbolic_nft_mint_signal` (only after rights clearance for third-party art).
7. **FIN_CRYPTO join** — market snapshots for collection contract addresses (no investment advice).
8. **NAMM optional** — certify content hash / collection root for `COMPUTATIONAL_EVIDENCE`.
9. **Graph runtime** (later) — Neo4j/Memgraph Cypher over the same edge vocabulary.

---

## Guardrails

- No sovereignty, legitimacy, or guilt language tied to marks.
- Simulated heraldry ≠ real state authority.
- Merch and NFT are product/catalog surfaces; minting does not authorize institutional acts.
- Secrets, private keys, and marketplace API credentials stay out of umbrella git.
- Prefer content hashes over mutable CDN URLs when claiming durable identity of bytes.
- Third-party seeds: analysis only until rights cleared; never imply NFT mint readiness from repo presence alone.
- No verbatim copyrighted books (Jung, etc.) in git — cite titles only.
- Never auto-mint NFT from scraped Instagram; `rights_status` required on every ingest→register path ([SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md)).

---

## Links

- Schema: [`schemas/symbolic-asset.json`](../../schemas/symbolic-asset.json)
- Events: [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json)
- Layer IDs: [`schemas/institution-layer-id.json`](../../schemas/institution-layer-id.json)
- Seed catalog: [`symbolic/SEED_CATALOG.md`](symbolic/SEED_CATALOG.md)
- Seed binaries: [`symbolic/seeds/`](symbolic/seeds/)
- Ingest (IG + web): [SYMBOLIC_INGEST.md](SYMBOLIC_INGEST.md)
- World framing: [GLOBAL_AI_GOVERNANCE.md](../institutions/GLOBAL_AI_GOVERNANCE.md)
- Philosophy / Homo loquens: [PHILOSOPHY.md](../PHILOSOPHY.md)
- Markets: [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md)
- Gov open data: [GOV_DATA_SOURCES.md](GOV_DATA_SOURCES.md)
- Verification: [NAMM.md](NAMM.md)
- OpenSea metadata standards: https://docs.opensea.io/docs/metadata-standards
- Property vs RDF graphs (Neo4j): https://neo4j.com/blog/knowledge-graph/rdf-vs-property-graphs-knowledge-graphs/
- Wikidata: https://www.wikidata.org/ · Iconclass: https://iconclass.org/ · Getty AAT: https://www.getty.edu/research/tools/vocabularies/aat/

*Phase classification: Phase 2 schema contracts (stub now); Phase 3–4 graph runtime and pipeline join.*
