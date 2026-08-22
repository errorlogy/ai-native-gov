# Symbolic lore — curated source registry

**Epistemic label:** `INSTITUTIONAL_MODEL`. Entries here are **cultural signal references** for the SYMBOLIC layer — not legitimacy verdicts, not automatic copyright clearance, and not NFT mint authority.

**Sibling contracts:** registry / lore axis = [SYMBOLIC_VISUAL_LAYER.md](../SYMBOLIC_VISUAL_LAYER.md); ingest pipeline = [SYMBOLIC_INGEST.md](../SYMBOLIC_INGEST.md); provenance index = [SOURCES.md](SOURCES.md).

---

## Purpose

Machine-readable **source ids** for operator-curated lore and visual reference collections that feed the symbolic ingest pipeline before optional promotion to [SEED_CATALOG.md](SEED_CATALOG.md) or the symbolic graph.

| Field | Meaning |
|-------|---------|
| `source_id` | Stable identifier for adapters, `stream_refs`, and catalog provenance |
| `purpose` | Why the collection exists in the SYMBOLIC layer |
| `ingest` | Allowed fetch paths, default `rights_status`, mint posture |
| `registry` | Link to [SYMBOLIC_VISUAL_LAYER.md](../SYMBOLIC_VISUAL_LAYER.md#curated-lore-sources-external-collections) framing |

---

## Registered sources

### `source:pinterest:ainativelife`

| Field | Value |
|-------|-------|
| **Source id** | `source:pinterest:ainativelife` |
| **Platform** | Pinterest |
| **Brand / handle** | **ANTHEMIUM** / [@ainativelife](https://www.pinterest.com/ainativelife/) |
| **URL** | https://www.pinterest.com/ainativelife/ |
| **Purpose** | Curated lore / visual references — Greco-Roman, digital remake, and symbolic visual codes accumulated for SYMBOLIC layer analysis, tagging, and ontology linking |
| **Class** | Owner-curated (operator save workflow) |
| **Default `rights_status`** | `owner_curated` (collection workflow); individual pins may remain `analysis_only` or `unknown` until cleared |
| **Mint posture** | **No auto-mint** — per-pin human review and explicit `rights_status` ∈ {`cleared_merch`, `cleared_nft`} required before any FIN_CRYPTO mint signal |

#### Ingest paths

| Priority | Method | `parse_method` | Notes |
|----------|--------|----------------|-------|
| 1 | Manual pin/board export, screenshot + permalink | `creator_export` / `human_upload` | Preferred MVP; operator selects pins for review |
| 2 | oEmbed / OpenGraph on pin or board URL | `oembed` | Metadata discovery; binary fetch still needs rights |
| 3 | Pinterest Developer API (future) | `official_api` | Only when app approved and [ToS](https://policy.pinterest.com/en/terms-of-service) permits; not assumed in Phase 2 |

**Emit sequence:**

```text
source:pinterest:ainativelife (profile/board URL)
  → symbolic_lore_source_linked (collection anchor)
  → operator selects pin(s)
  → symbolic_media_discovered | symbolic_media_fetched (per pin)
  → human review gate → SEED_CATALOG / symbolic-asset stub
```

**Guardrails:** respect Pinterest ToS; prefer user-owned saves over bulk third-party mirroring; board link ≠ copyright or NFT clearance.

**Cross-layer `stream_refs` example:** `symbolic:source:pinterest:ainativelife` (prefix optional per adapter).

Full ingest contract: [SYMBOLIC_INGEST.md — Pinterest adapter](../SYMBOLIC_INGEST.md#pinterest-adapter--anthemium-owner-curated). Registry framing: [SYMBOLIC_VISUAL_LAYER.md — Curated lore sources](../SYMBOLIC_VISUAL_LAYER.md#curated-lore-sources-external-collections).

---

## Event anchor (collection link)

```json
{
  "story_id": "2026-anthemium-pinterest-lore",
  "event_type": "symbolic_lore_source_linked",
  "activated_layers": ["institution:symbolic-visual"],
  "stream_refs": ["source:pinterest:ainativelife"],
  "epistemic_label": "OPERATIONAL"
}
```

---

## Links

- Registry / lore axis: [SYMBOLIC_VISUAL_LAYER.md](../SYMBOLIC_VISUAL_LAYER.md)
- Ingest contract: [SYMBOLIC_INGEST.md](../SYMBOLIC_INGEST.md)
- Provenance index: [SOURCES.md](SOURCES.md)
- Seed catalog: [SEED_CATALOG.md](SEED_CATALOG.md)
- Events: [`schemas/cross-layer-event.json`](../../../schemas/cross-layer-event.json)
