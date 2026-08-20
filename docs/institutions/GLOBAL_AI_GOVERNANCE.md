# Global AI Governance — Master Framing

**Epistemic label:** `INSTITUTIONAL_MODEL` — this document frames world-scale AI governance simulation as a three-tier topology. All layers are analytical modeling constructs. The simulator does not claim sovereign authority, legal standing, or operational governance capacity over any real jurisdiction.

---

## What this document is

This is the **umbrella framing document** for simulating AI-managed government at world scale: national instances, regional blocs, and a planned global coordination layer. It sits above [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) (single-jurisdiction stack) and beside [EU_TOPOLOGY.md](EU_TOPOLOGY.md) (first fully specified regional bloc).

**Read order for agents:**

1. [VISION.md](../../VISION.md) — non-sovereignty, epistemic humility
2. [PHILOSOPHY.md](../PHILOSOPHY.md) — Homo loquens heuristic; AI→AGI→ASI as reasoning layers; Errorlogy measures error
3. [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) — base institutional stack per jurisdiction
4. This document — three-tier world model
5. [EU_TOPOLOGY.md](EU_TOPOLOGY.md) — reference regional implementation (27 states)
6. [TOPOLOGY.md](TOPOLOGY.md) — layer intersection matrix

---

## Strategic goal

On one side of the simulator: **AI versions of countries and regional blocs** — each national instance runs a full institutional stack with configurable human involvement. On the other side: **supranational AI Native Gov layers** that coordinate across jurisdictions without replacing or claiming sovereignty over them.

The simulator explores how AI could carry out the full spectrum of government management worldwide while **varying human (homo) participation per country** — from shadow advisory (Phase 0) through co-execution to autonomous AI cabinets with retained human appeal paths (Phase 4). See [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) for the autonomy dial table and gradual replacement phases.

---

## Three-tier model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         GLOBAL_LAYER (planned)                              │
│                                                                             │
│  Global Parliament analog │ Global Executive analog │ Global Judiciary      │
│  Global Transnational Ops │ Charter / treaty framing │ Human Oversight      │
│  (coordination, not sovereignty — models tension and alignment signals)     │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │ treaty / collision / coordination
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ REGIONAL_BLOC   │      │ REGIONAL_BLOC   │      │ REGIONAL_BLOC   │
│ EU (×1, active) │      │ ASEAN (stub)    │      │ AU / Mercosur   │
│ 27 national     │      │                 │      │ (stubs)         │
│ instances       │      │                 │      │                 │
└────────┬────────┘      └────────┬────────┘      └────────┬────────┘
         │                          │                          │
         ▼                          ▼                          ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ NATIONAL_       │      │ NATIONAL_       │      │ NATIONAL_       │
│ INSTANCE ×27    │      │ INSTANCE ×N     │      │ INSTANCE ×N     │
│ (EU members)    │      │ (ASEAN members) │      │ (bloc members)  │
│                 │      │                 │      │                 │
│ Full stack per  │      │ Same template   │      │ Same template   │
│ AI_GOVERNMENT_  │      │ as EU national  │      │ as EU national  │
│ OVERVIEW        │      │ instance        │      │ instance        │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

| Tier | ID prefix | Status | Role in simulator |
|------|-----------|--------|-------------------|
| **NATIONAL_INSTANCE** | `state:{iso2}` | EU: 27 profiles in [EU_STATES.md](EU_STATES.md); rest of world: planned | Independent institutional stack per country; autonomy dials set human↔AI balance |
| **REGIONAL_BLOC** | `bloc:{code}` | EU: [EU_TOPOLOGY.md](EU_TOPOLOGY.md); ASEAN, AU, Mercosur, etc.: stubs | Cross-cutting coordination, treaty-level constraints, bloc judiciary analog |
| **GLOBAL_LAYER** | `global:*` | Planned | World-scale coordination, collision resolution across blocs, global charter framing |

Each tier **extends** the tier below; none replaces national instances. Regional and global layers aggregate positions, surface tensions, and route collision signals — they do not issue sovereign commands.

---

## EU as reference implementation

The European Union is the **first fully documented regional bloc** in this topology:

| Artifact | Purpose |
|----------|---------|
| [EU_TOPOLOGY.md](EU_TOPOLOGY.md) | Role definitions, collision taxonomy, integration depth, variable geometry |
| [EU_SCHEMA.md](EU_SCHEMA.md) | Mermaid visual schema (structure, event flow, rings) |
| [EU_STATES.md](EU_STATES.md) | All 27 member-state profiles (`state-profile.json` fields) |

Other blocs use the EU pattern as a **template stub** — same two-tier shape (national instances + supranational layer), bloc-specific role IDs and membership parameters to be filled in later:

| Bloc stub | `bloc_id` | Member count (modeled) | Status |
|-----------|-----------|------------------------|--------|
| European Union | `bloc:eu` | 27 | **Active** — reference implementation |
| ASEAN | `bloc:asean` | ~10 | Stub — structure TBD |
| African Union | `bloc:au` | ~55 | Stub — structure TBD |
| Mercosur | `bloc:mercosur` | 4+ | Stub — structure TBD |
| USMCA / other | `bloc:*` | varies | Stub — on demand |

When adding a new bloc, copy the EU collision-resolution and delegate-aggregation patterns; do not copy EU-specific treaty names as if they were universal law.

---

## Human involvement dial (national level)

Human participation is **parameterized per national instance**, not globally fixed. Each country can sit at a different point on the homo participation spectrum simultaneously.

### Per-country parameters

From `state-profile.json` / [EU_TOPOLOGY.md](EU_TOPOLOGY.md) national instance template:

| Field | Meaning |
|-------|---------|
| `ai_readiness_level` | 0–4; maps to gradual replacement phases in [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) |
| `autonomy_dials.national_parliament` | 0.0–1.0 — deliberation AI share |
| `autonomy_dials.national_cabinet` | 0.0–1.0 — executive AI share |
| `autonomy_dials.national_judiciary` | 0.0–1.0 — judicial AI share (`judiciary_ai_pct` analog) |
| `autonomy_dials.transnational_ops_interface` | 0.0–1.0 — cross-border ops AI share |

### Homo participation spectrum (modeling scenarios)

Autonomy dials express the spectrum of *homo* vs AI participation in an unfinished civilizational phase (*Homo loquens* / pre-sapiens heuristic). See [PHILOSOPHY.md](../PHILOSOPHY.md). AI→AGI→ASI here means deeper institutional reasoning layers for error-minimization research — not sovereign replacement. Errorlogy measures μ/α/PNO/FPD; this umbrella defines contracts.

| Scenario label | Typical `ai_readiness_level` | Human role |
|----------------|------------------------------|------------|
| **Homo-primary** | 0–1 | Humans confirm all outputs; AI advises |
| **Co-governance** | 2 | AI executes routine; humans retain high-risk and appeal |
| **AI-primary + homo oversight** | 3–4 | AI fills institutional roles; Human Oversight Panel active |

**Invariants (all countries, all phases):**

- `human_override_always: true` — cannot be disabled by AI agents
- `human_veto_enabled: true` by default on all layers
- `judicial_gate_bypass: false` on transnational ops — no exceptions
- Outputs are **analytical contributions**, not verdicts on guilt, legitimacy, or sovereignty

World-scale simulation therefore models **asynchronous transition**: Estonia at `ai_readiness_level: 3` and another state at `0` can coexist in the same run; regional and global layers must handle heterogeneous dial states without assuming uniform AI adoption.

---

## Supranational coordination without sovereignty claims

AI Native Gov operates as a **modeling framework** ([VISION.md](../../VISION.md)), not a government. At regional and global tiers:

| What the model does | What the model does not do |
|---------------------|----------------------------|
| Aggregate delegate positions from national stacks | Claim legitimate rule over territories |
| Surface `collision_signal` when charter/treaty tensions arise | Issue legal verdicts or guilt determinations |
| Route cross-border ops through judicial gates | Bypass national human oversight |
| Emit μ/α/PNO **signals** via Errorlogy | Present fuzzy scores as proof of illegitimacy |
| Feed politic.bar streams for scenario analysis | Replace real-world institutions operationally |

**Coordination mechanics** (EU-proven, global-planned):

1. **Delegate aggregation** — national parliaments → regional parliament analog (D'Hondt or bloc-specific rule)
2. **Council intergovernmental tier** — national cabinets → weighted council voting
3. **Commission / executive analog** — proposals, monitoring, infringement-style collision paths
4. **Supranational judiciary** — procedural constraint; preliminary ruling **tension**, not verdict
5. **Transnational ops** — always via national judicial-gate interface
6. **Human Oversight** — hard stop on all tiers; veto, appeal, audit, dial rollback

Collision taxonomy and resolution paths: [EU_TOPOLOGY.md](EU_TOPOLOGY.md#collision-resolution-national-charter-vs-eu-supranational-layer). Global layer will extend this with `bloc_vs_bloc` and `national_vs_global_charter` collision types (planned).

---

## Cross-cutting signal ingress

Institutional layers do not ingest raw feeds directly. **Integration adapters** normalize external signals into `cross-layer-event.json` envelopes with `activated_layers` and epistemic labels.

### Finance-crypto markets

[FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md) is the reference integration for **economic and market context**:

- Normalized event types (`fin_crypto_market_snapshot`, `fin_crypto_onchain_risk`, etc.)
- Routing to executive, parliament, judiciary, transnational-ops layers by event type
- Default epistemic label: `OPERATIONAL`; `COMPUTATIONAL_EVIDENCE` only with NAMM `certificate_ref`
- No investment advice; on-chain risk = dispute-surface **hypothesis**, not accusation

At world scale, fin-crypto signals may activate **multiple national instances** (e.g. BTC liquidity shock → finance ministries in US, EU, JP instances) plus **regional** fiscal coordination layers (ECOFIN analog) without implying a single global monetary authority.

### Government data sources / parsing

[GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md) is the reference integration for **official open data, legislative/parliamentary feeds, graded news, and human-uploaded docs**:

- Normalized event types (`gov_open_data_snapshot`, `gov_legislative_document`, …)
- EU-first priority (EUR-Lex/CELLAR, EP Open Data, Eurostat) for the 27-state simulator
- Official API first; HTML parse as last resort with quality flags
- Default epistemic label: `OPERATIONAL`; `COMPUTATIONAL_EVIDENCE` only with NAMM `certificate_ref`

### Symbolic / visual identity

[SYMBOLIC_VISUAL_LAYER.md](../integrations/SYMBOLIC_VISUAL_LAYER.md) is the registry + graph contract for **symbolic visual code** (marks, seals, merch, NFT collections, multimodal media):

- Layer ID: `institution:symbolic-visual`
- Property-graph + content-addressed blobs (JSON stubs now; Neo4j/Memgraph later)
- Lore axis: Greco-Roman/Egyptian remakes + SYNTHEΣ progress-synthesis ([PHILOSOPHY.md](../PHILOSOPHY.md)); Jungian tags as heuristic vocabulary only
- Seeds: [`docs/integrations/symbolic/SEED_CATALOG.md`](../integrations/symbolic/SEED_CATALOG.md)
- Symbols are cultural/institutional **signals**, not legitimacy verdicts; NFT provenance may be `COMPUTATIONAL_EVIDENCE` only with NAMM

### Other integration layers

| Integration | Role at world scale |
|-------------|---------------------|
| [GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md) | Gov/open-data/legislative ingress; parsing adapters → cross-layer events |
| [SYMBOLIC_VISUAL_LAYER.md](../integrations/SYMBOLIC_VISUAL_LAYER.md) | Symbolic marks, seals, merch, NFT/media catalog graph |
| [ERRORLOGY.md](../integrations/ERRORLOGY.md) | μ/α/PNO/FPD validation on institutional outputs; collision fuzzy membership |
| [POLITIC_BAR.md](../integrations/POLITIC_BAR.md) | Error cards, politifi streams; surfaces tensions across jurisdictions |
| [NAMM.md](../integrations/NAMM.md) | Verification certificates for grounds packages (`COMPUTATIONAL_EVIDENCE`) |

Signal flow: **ingress adapter → institutional framer → national/regional/global layers → synthesis → Errorlogy → politic.bar**. See [ARCHITECTURE.md](../../ARCHITECTURE.md).

---

## Phased rollout

Aligned with [ROADMAP.md](../../ROADMAP.md) Phase 0–5 and the Global AI governance simulator track:

| Rollout stage | Scope | ROADMAP alignment |
|---------------|-------|-------------------|
| **A — EU complete** | 27 national profiles, EU supranational layer, collision taxonomy, EU_SCHEMA diagrams | Phase 3 (institutional depth) |
| **B — Regional stubs** | ASEAN, AU, Mercosur bloc shells; national instance template reused; minimal collision rules | Phase 3 → Phase 4 |
| **C — Global coordination layer** | `GLOBAL_LAYER` role IDs, bloc-to-bloc collision, global charter stub, heterogeneous dial orchestration | Phase 4–5 |
| **D — Live ingress** | Fin-crypto and other adapters feeding multi-jurisdiction scenarios | Phase 4 (pipeline integration) |
| **E — Agent automation** | Playbooks for topology updates, new bloc stubs, cascade scenarios | Phase 5 |

**Current baseline (2026):** Stage A substantially documented; Stages B–E planned.

---

## Event routing at world scale

| Signal scope | First activation | Escalation |
|--------------|------------------|------------|
| Domestic (single state) | That state's national stack only | Human Oversight on escalation |
| Bilateral (two states) | Both national instances + optional transnational ops | Judiciary gate on both sides |
| Regional (bloc-internal) | National instances in bloc + `bloc:*` supranational layer | EU collision paths ([EU_TOPOLOGY.md](EU_TOPOLOGY.md)) |
| Cross-bloc | National instances in each bloc + both regional layers | Planned: `global:*` collision mediation |
| Global market / macro | Multiple nationals via integration routing + finance ministry slots | Fin-crypto adapter → [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md) |

Envelope format: `schemas/cross-layer-event.json` with `activated_layers` listing `state:{iso2}`, `bloc:{code}`, and `global:*` as applicable.

---

## Institution document index

### World-scale and EU

| Document | Description |
|----------|-------------|
| **This document** | Three-tier global framing |
| [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) | Master map — single-jurisdiction full stack |
| [EU_TOPOLOGY.md](EU_TOPOLOGY.md) | EU regional bloc — roles, collisions, dials |
| [EU_SCHEMA.md](EU_SCHEMA.md) | EU mermaid visual schema |
| [EU_STATES.md](EU_STATES.md) | 27 EU national instance profiles |
| [OVERVIEW.md](OVERVIEW.md) | Short institutional map |
| [TOPOLOGY.md](TOPOLOGY.md) | Layer intersection matrix |

### Base institutional layers

| Document | Layer ID (examples) |
|----------|---------------------|
| [CHARTER.md](CHARTER.md) | `institution:charter` |
| [parliament.md](parliament.md) | `institution:parliament` |
| [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | `institution:ai-speaker`, `institution:party-coalition`, `institution:ai-minister`, `institution:ai-pm` |
| [executive.md](executive.md) | `institution:executive` |
| [AI_CABINET.md](AI_CABINET.md) | Cabinet MAS, `cabinet_intent` |
| [AI_MINISTRIES.md](AI_MINISTRIES.md) | `institution:minister-*` |
| [judiciary.md](judiciary.md) | `institution:judiciary` |
| [AI_JUDICIARY.md](AI_JUDICIARY.md) | `institution:ai-presiding-judge`, `institution:ai-judicial-panel` |
| [interpol.md](interpol.md) | Cross-border coordination (abstract) |
| [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) | `institution:transnational-ops` |
| [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) | Human veto, appeal, audit |

### Integrations and architecture

| Document | Description |
|----------|-------------|
| [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md) | Market/crypto signal ingress |
| [SYMBOLIC_VISUAL_LAYER.md](../integrations/SYMBOLIC_VISUAL_LAYER.md) | Symbolic / visual identity registry + graph |
| [ERRORLOGY.md](../integrations/ERRORLOGY.md) | Engine validation contract |
| [POLITIC_BAR.md](../integrations/POLITIC_BAR.md) | Stream publishing contract |
| [NAMM.md](../integrations/NAMM.md) | Verification certificates |
| [ARCHITECTURE.md](../../ARCHITECTURE.md) | Umbrella system architecture |
| [VISION.md](../../VISION.md) | Principles and non-sovereignty |
| [PHILOSOPHY.md](../PHILOSOPHY.md) | Homo loquens, AI→AGI→ASI framing, Errorlogy role |
| [AGENTS.md](../../AGENTS.md) | Language rules, routing, epistemic labels |
| [docs/examples/trump-macron-cascade.md](../examples/trump-macron-cascade.md) | Cross-layer cascade example |

### Schemas

| Schema | Purpose |
|--------|---------|
| `schemas/cross-layer-event.json` | Event envelope with institutional activation |
| `schemas/institution-layer-id.json` | Stable layer IDs (including EU extensions) |
| `schemas/state-profile.json` | National instance profile fields |
| `schemas/institution-graph.json` | Machine-readable topology (planned depth) |
| `schemas/symbolic-asset.json` | Symbolic/visual identity catalog stub |

---

## Epistemic guarantees (world scale)

Same constraints as [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md), extended:

- **Heterogeneous dials** — no implicit assumption that all countries share the same AI autonomy level
- **Bloc stubs** — ASEAN/AU/Mercosur entries are structural placeholders until populated; agents must not treat stubs as verified geopolitical fact
- **Global layer** — when implemented, remains `INSTITUTIONAL_MODEL` only; coordinates simulation runs, does not govern the real world
- **Integration signals** — fin-crypto and news adapters provide context with mandatory uncertainty; never upgrade to verdict language without NAMM linkage

---

*Phase classification: cross-cutting — Stage A (EU) in Phase 3; global layer in Phase 4–5. See [ROADMAP.md](../../ROADMAP.md#global-ai-governance-simulator).*
