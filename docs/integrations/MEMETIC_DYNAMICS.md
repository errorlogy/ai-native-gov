# Integration — Memetic Dynamics (Phase A contracts)

How AI Native Gov models **memetic propagation and discourse contours** as institutional optics — without claiming verdict authority or inventing taxonomy mode IDs.

**Epistemic label:** `INSTITUTIONAL_MODEL` for framing; adapter outputs default to `OPERATIONAL` unless NAMM-linked.

## Purpose

Memetic dynamics are **named** in Errorlogy taxonomy v16 (HM layer, SOCIAL_MEDIA layer, EGD echo-room modes) and in umbrella philosophy ([`PHILOSOPHY.md`](../PHILOSOPHY.md) — Homo loquens). Phase A adds **contracts only**: stream envelopes and cross-layer event types. Runtime graph builders, half-life indexers, and sociome coupling ship in Phase B/C.

## Seven dynamic contours (roadmap)

| # | Contour | Phase A (this doc) | Later owner |
|---|---------|---------------------|-------------|
| 1 | Memetic propagation graph (R₀ analog, variant tracking) | `memetic_propagation_snapshot` event type | `errorlogy-mas` engine |
| 2 | Discourse lineage / narrative forks | `discourse_fork_detected`, `narrative_lineage_update` | `errorlogy-mas` (networkx extension) |
| 3 | Sociome coupling (MatrAIx cohorts) | Sidecar fields only — see [`MATRAIX_PERSONA.md`](MATRAIX_PERSONA.md) | Post-MVP |
| 4 | Signal/noise memetic half-life | [`schemas/signal-envelope.json`](../../schemas/signal-envelope.json) | `politic-bar` streams |
| 5 | fin_crypto ↔ memetic momentum | `memetic_market_coupling_snapshot` + FIN join | `errorlogy-mas` — [`MEMETIC_MARKET_COUPLING.md`](MEMETIC_MARKET_COUPLING.md) |
| 6 | Symbolic meme carrier registry | Reuse `symbolic_media_variant` — see [`SYMBOLIC_VISUAL_LAYER.md`](SYMBOLIC_VISUAL_LAYER.md) | Symbolic ingest |
| 7 | SOCIAL_MEDIA platform contour state | `social_contour_state_update` | `errorlogy-mas` ingest |

## Schemas (umbrella)

| Schema | Role |
|--------|------|
| [`signal-envelope.json`](../../schemas/signal-envelope.json) | Graded stream item: `evidence_grade`, `memetic_metrics`, `epistemic_label` |
| [`cross-layer-event.json`](../../schemas/cross-layer-event.json) | Institutional activation envelope; memetic `event_type` examples in schema |

### `signal-envelope.json` fields (Phase A)

- `stream_item_id`, `story_id`, `source_type` (`primary|commentary|speculation|social`)
- `evidence_grade`: `weak|medium|strong`
- `memetic_metrics` (optional): `first_seen`, `peak_velocity`, `decay_tau_hours`, `variant_of`, `platform_contour`
- `epistemic_label`: default `OPERATIONAL` for adapter-derived items

### Cross-layer memetic event types

Add to ingress / institutional stub routing (no new CB-/HM-/PNO- mode IDs):

| `event_type` | Default activated layers (stub) |
|--------------|----------------------------------|
| `memetic_propagation_snapshot` | parliament, party-coalition, executive |
| `discourse_fork_detected` | parliament, party-coalition, judiciary |
| `narrative_lineage_update` | parliament, party-coalition, judiciary |
| `signal_noise_half_life_update` | parliament, executive, national-instance |
| `memetic_market_coupling_snapshot` | central-bank-analog, parliament, regulatory-agency |
| `social_contour_state_update` | parliament, party-coalition, symbolic-visual |

Routing implementation: `errorlogy-mas/mas/institutional/activation.py` prefix table (longest match: `memetic_market_` before `memetic_`).

## Taxonomy references (read-only)

- **HM layer** (Homo-MAS): viral cascade, narrative amplification, meme compression — classifier path in taxonomy v16; do not invent HM-xxx IDs in umbrella docs.
- **SOCIAL_MEDIA layer**: platform environment framing; `platform_contour` in `signal-envelope` references platform slugs only.
- **EGD**: small-group echo-room dynamics — distinct from platform-scale memetics; see existing EGD engine in `errorlogy-mas`.

## Repo ownership

| Knowledge | Repo |
|-----------|------|
| Schemas, integration contracts, topology framing | **ai-native-gov** (this repo) |
| Institutional stub, adapters, engine extensions | **errorlogy-mas** |
| Stream store, politifi, signal/noise UI | **politic-bar** |
| μ/α/PNO/FPD math, taxonomy v16 JSON | **errorlogy/errorlogy** |

## Guardrails

- Use **legitimacy signals (modeled)** and **analytical contribution** — not guilt, criminal, or sovereign AI government language.
- Do **not** merge politic-bar v0.6 taxonomy with v16.
- Do **not** copy `errorlogy_unified_taxonomy_v16.json` into the umbrella.
- `COMPUTATIONAL_EVIDENCE` only when a NAMM `certificate_ref` is linked.

## Related

- [`MEMETIC_MARKET_COUPLING.md`](MEMETIC_MARKET_COUPLING.md) — iter 6 join record + API
- [`MVP_ITERATIONS.md`](../examples/MVP_ITERATIONS.md) — iter 3 CCXT adapter + Phase A section
- [`MATRAIX_PERSONA.md`](MATRAIX_PERSONA.md) — sociome contour (Phase C)
- [`ERRORLOGY.md`](ERRORLOGY.md) — engine pipeline ingress/egress
