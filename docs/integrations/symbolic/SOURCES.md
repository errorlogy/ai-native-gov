# Symbolic lore — curated source provenance

**Epistemic label:** `INSTITUTIONAL_MODEL`. Sources listed here are **cultural signal references** for SYMBOLIC layer analysis — not legitimacy verdicts, not automatic copyright clearance, and not NFT mint authority.

---

## Purpose

Index **where visual lore enters** the umbrella before (optional) promotion to [`SEED_CATALOG.md`](SEED_CATALOG.md) or the symbolic graph. Distinguishes:

| Class | Meaning |
|-------|---------|
| **Owner-curated** | Operator-controlled collection workflow (saved pins, exports, uploads) |
| **Third-party reference** | External art cited for analysis only until rights cleared |
| **Official open** | GLAM / gov open data (see [GOV_DATA_SOURCES.md](../GOV_DATA_SOURCES.md)) |

Pipeline: [SYMBOLIC_INGEST.md](../SYMBOLIC_INGEST.md) — discover → fetch metadata → hash (when allowed) → human review gate → catalog.

**Canonical source ids:** [`CURATED_SOURCES.md`](CURATED_SOURCES.md). Registry framing: [SYMBOLIC_VISUAL_LAYER.md](../SYMBOLIC_VISUAL_LAYER.md#curated-lore-sources-external-collections).

---

## Registered sources (v0)

| Platform | Source id | Brand / handle | URL | Lore focus | Default `rights_status` | Ingest path |
|----------|-----------|----------------|-----|------------|-------------------------|-------------|
| **Pinterest** | `source:pinterest:ainativelife` | **ANTHEMIUM** / [@ainativelife](https://www.pinterest.com/ainativelife/) | https://www.pinterest.com/ainativelife/ | Curated lore / visual references — Greco-Roman, digital remake, symbolic visual codes | `owner_curated` | Manual export, oEmbed/link, future Pinterest API (ToS-gated); **no auto-mint** |
| **Instagram** | — | @tonybamber (v0 seeds) | https://www.instagram.com/tonybamber/ | *The Odyssey!* neoclassical cinematic stills | `analysis_only` | Manual analysis path into git seeds (see [`seeds/README.md`](seeds/README.md)) |

---

## Provenance pattern (Instagram vs Pinterest)

Both platforms feed **candidates**, not verdicts. The difference is **who curates** and **default rights posture**.

```text
Instagram (third-party creator)
  creator post URL → manual copy + catalog note
  rights_status: analysis_only
  mint: blocked until explicit clearance

Pinterest (ANTHEMIUM / ainativelife)
  operator saves pin to own board → permalink + optional export
  rights_status: owner_curated (workflow) / per-pin may stay analysis_only
  emit: symbolic_lore_source_linked (board) + symbolic_media_* (selected pins)
  mint: never automatic; per-pin review + cleared_* required
```

### Pinterest guardrails

- Respect [Pinterest Terms of Service](https://policy.pinterest.com/en/terms-of-service).
- Prefer **user-owned curation** (pins the operator saves) over mirroring third-party boards without rights review.
- oEmbed/OpenGraph may enrich metadata; binary fetch and catalog registration still require review.
- Do not scrape production catalogs without API approval or operator enablement.

### Instagram guardrails

- Meta Graph API for owned/authorized accounts is primary social ingress ([SYMBOLIC_INGEST.md](../SYMBOLIC_INGEST.md)).
- HTML scrape: experimental only; never production mint.
- v0 git seeds remain third-party analysis references.

---

## Event types

| `event_type` | When |
|--------------|------|
| `symbolic_lore_source_linked` | External collection (e.g. Pinterest profile) registered as workflow anchor |
| `symbolic_media_discovered` | Individual pin/post selected for review |
| `symbolic_media_fetched` | Metadata and/or hash retrieved |
| `symbolic_asset_registered` | Passed human gate → SEED_CATALOG / symbolic graph |

Example — collection anchor:

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

- Curated source registry: [CURATED_SOURCES.md](CURATED_SOURCES.md)
- Registry / lore axis: [SYMBOLIC_VISUAL_LAYER.md](../SYMBOLIC_VISUAL_LAYER.md)
- Ingest contract: [SYMBOLIC_INGEST.md](../SYMBOLIC_INGEST.md)
- Seed catalog: [SEED_CATALOG.md](SEED_CATALOG.md)
- Seed binaries: [seeds/](seeds/)
- Events: [`schemas/cross-layer-event.json`](../../../schemas/cross-layer-event.json)
