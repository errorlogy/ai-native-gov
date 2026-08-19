# EU Multi-Level Topology

**Epistemic label:** `INSTITUTIONAL_MODEL` — this document models the European Union as a two-tier institutional topology for the AI-Native Government simulator. All layers are analytical modeling constructs. No claim of legal authority, sovereign standing, or real-world governance capacity is made.

---

## Overview

The EU topology introduces a **two-tier structure** layered on top of the base simulator architecture:

| Tier | Instances | Role in Simulator |
|------|-----------|-------------------|
| `NATIONAL_INSTANCES` | ×27 member states | Independent institutional stacks with national charters, parliaments, cabinets, judiciaries |
| `EU_SUPRANATIONAL_LAYER` | ×1 (EU-level) | Cross-cutting coordination, treaty-level constraints, supranational judicial oversight |

Each national instance runs a full local copy of the base topology ([AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md)). The supranational layer adds EU-specific roles that constrain and coordinate national instances without replacing them.

---

## Structural diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        EU_SUPRANATIONAL_LAYER                               │
│                                                                             │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐  │
│  │  EU_Parliament   │  │  EU_Commission   │  │      EU_Council          │  │
│  │  (delegates from │  │  (AI executive   │  │  (national ministers     │  │
│  │   nat. parliaments│  │   at EU level)   │  │   sitting in council)    │  │
│  └────────┬─────────┘  └────────┬─────────┘  └────────────┬─────────────┘  │
│           │                     │                         │                │
│           └─────────────────────┼─────────────────────────┘                │
│                                 │                                          │
│              ┌──────────────────┼──────────────────┐                       │
│              ▼                  ▼                  ▼                       │
│   ┌──────────────────┐  ┌────────────────┐  ┌──────────────────────────┐  │
│   │EU_Court_of_Justice│  │  (Charter of   │  │ EU_Transnational_Ops     │  │
│   │(procedural        │  │  Fundamental   │  │ (Europol/Frontex analog) │  │
│   │ constraint at EU) │  │   Rights)      │  └──────────────────────────┘  │
│   └──────────────────┘  └────────────────┘                                 │
└──────────────────────────────────────────────────────────────────────────┬─┘
                                 ▲ treaty constraints / coordination        │
                                 │                                          │
         ┌───────────────────────┴──────────────────────────────────────────┘
         │                    NATIONAL_INSTANCES (×27)
         │
         ├── [DE] Germany ──────────────────────────────────────────────────┐
         │   national_charter ─► national_parliament ─► national_cabinet    │
         │   national_judiciary ─► transnational_ops_interface              │
         │   integration_depth: 0.95 | membership_rings: full+euro+schengen │
         │   ai_readiness_level: 3                                          │
         └──────────────────────────────────────────────────────────────────┘
         ├── [FR] France ────────────────────────────────────────────────────
         ├── [DK] Denmark (opt-outs: eurozone, defense, JHA) ──────────────
         ├── [EE] Estonia (high AI readiness) ──────────────────────────────
         ├── [HU] Hungary (rule-of-law tension) ───────────────────────────
         └── … (22 further member states — see EU_STATES.md)
```

---

## Supranational layer: role definitions

| Role ID | Institutional analog | Function in simulator |
|---------|----------------------|-----------------------|
| `institution:eu-parliament` | European Parliament | Deliberation across delegated national positions; legislative posture at EU level |
| `institution:eu-commission` | European Commission | AI executive for EU-level policy proposals; treaty guardian |
| `institution:eu-council` | Council of the EU | Aggregate of national ministers; weighted voting; final legislative co-decision |
| `institution:eu-court-of-justice` | Court of Justice of the EU | Procedural constraint; treaty interpretation; national law conformity check |
| `institution:eu-transnational-ops` | Europol / Frontex / OLAF analog | Cross-border enforcement coordination; activates via judicial gate |

### EU Parliament (delegates model)

The `eu-parliament` instance does **not** replace national parliaments. It aggregates delegate positions produced by national parliamentary stacks. Delegate weights are proportional to seat allocations (D'Hondt analog). EP output feeds EU Commission proposals and co-decision flows.

### EU Commission (AI executive)

The `eu-commission` is the supranational executive. It proposes legislation, monitors treaty compliance, and can trigger infringement proceedings against national instances. In the simulator, infringement proceedings activate the `collision_resolution` pathway (see below).

### EU Council (intergovernmental tier)

The `eu-council` aggregates `national_cabinet` outputs from all 27 national instances. Voting weights are QMV (qualified majority voting): 55% of states representing 65% of EU population. The Council can be modeled with or without veto powers depending on the policy domain (unanimity vs. QMV switch).

### EU Court of Justice

The `eu-court-of-justice` operates as the supranational judiciary. It constrains both national instances and the EU supranational layer. A national instance output that violates EU treaty obligations routes to `eu-court-of-justice` before becoming actionable at the EU level.

### EU Transnational Ops

The `eu-transnational-ops` extends the base `transnational-ops` layer to EU-specific coordination (Europol crime coordination, Frontex border ops, OLAF anti-fraud). The `judicial_gate_bypass` invariant from the base topology applies here without exception.

---

## National instance template

Each of the 27 national instances conforms to the following template. All fields map to `state-profile.json` (see `schemas/state-profile.json`).

```yaml
national_instance:
  state_id: "iso2-code"          # ISO 3166-1 alpha-2 (e.g. "DE")
  name: "Full state name"
  legal_family: romano-germanic | common-law | nordic | mixed
  system_type: parliamentary-monarchy | republic | federal-republic | semi-presidential-republic
  integration_depth: 0.0–1.0    # 1.0 = fully integrated; lower = more opt-outs
  membership_rings:              # array: schengen | eurozone | eea | full
    - full
    - eurozone
    - schengen
  ai_readiness_level: 0–4       # matches Phase 0–4 autonomy dial range
  autonomy_dials:
    national_parliament:   0.0–1.0
    national_cabinet:      0.0–1.0
    national_judiciary:    0.0–1.0
    transnational_ops_interface: 0.0–1.0
  national_charter_ref: "path/to/charter-stub.md"
  opt_outs: []                   # list of specific EU policies opted out of

sub_layers:
  national_charter:              # Constitutional/treaty framing; constrains all national layers
  national_parliament:           # Deliberation; produces legislative_posture + delegate positions for eu-parliament
  national_cabinet:              # Executive; produces national positions fed to eu-council
  national_judiciary:            # Procedural constraint at national level; coordinates with eu-court-of-justice
  transnational_ops_interface:   # Gateway to eu-transnational-ops; always requires judicial gate clearance
```

---

## Collision resolution: national charter vs. EU supranational layer

When a **national_charter** constraint diverges from an **EU supranational** requirement, the simulator fires a `collision_signal`. This is the primary tension modeling mechanism.

### Collision taxonomy

| Collision type | Trigger | Resolution path |
|----------------|---------|-----------------|
| `treaty_conformity` | National law output contradicts EU treaty obligation | → `eu-court-of-justice` → infringement proceedings (EU Commission) |
| `fundamental_rights` | National output violates EU Charter of Fundamental Rights | → `eu-court-of-justice` → suspension signal |
| `policy_divergence` | National cabinet position conflicts with EU Council supermajority | → EU Council negotiation round; tension remains if unresolved |
| `opt_out_activation` | National instance activates registered opt-out | → filtered at supranational layer; no collision signal (expected divergence) |
| `rule_of_law_tension` | National judiciary signals structural independence compromise | → `eu-court-of-justice` + Article 7 analog activation; high μ in Errorlogy |

### Measurability via Errorlogy

Collision signals map to Errorlogy μ/α outputs:

- `μ_divergence`: fuzzy membership score of how far the national output deviates from EU norm (0.0 = full alignment, 1.0 = full conflict)
- `α_escalation`: accumulated tension across time (prior collision events referenced in `precedent_refs`)
- `PNO_block`: probability that the next national action will be blocked by EU-level constraint

Signal envelope format: `cross-layer-event.json` with `activated_layers` including both the national instance layer and the relevant supranational layer.

---

## Integration depth parameter

`integration_depth` (0.0–1.0) is a single scalar summarizing how deeply a member state participates in EU integration across all policy domains. It is computed from membership rings and registered opt-outs:

| Membership rings | Approximate integration_depth |
|------------------|-------------------------------|
| full + eurozone + schengen | 0.90–1.00 |
| full + schengen (non-euro) | 0.75–0.89 |
| full only (EEA partial) | 0.60–0.74 |
| full + opt-outs (JHA, defense, euro) | 0.40–0.59 |

### Opt-out registry (as of 2026 modeling baseline)

| Country | Opt-out domain | Membership ring affected |
|---------|---------------|--------------------------|
| Denmark | Eurozone, Defense cooperation, Parts of JHA | eurozone ring, schengen-jha |
| Ireland | Schengen (partial), Common travel area | schengen ring |
| Sweden | Eurozone (de facto; treaty obligation pending) | eurozone ring |
| Hungary | Rule-of-law mechanism resistance | Article 7 analog activation |
| Poland | Historical rule-of-law tension (partially resolved as of 2024) | Article 7 analog (reduced) |

---

## Variable geometry / multi-speed integration

The EU does not operate as a uniform bloc. The simulator models **three concentric integration rings**:

```
┌─────────────────────────────────────────────────────────────┐
│  RING 1: Full EU + Eurozone + Schengen                      │
│  (19+ states; deepest integration; all supranational        │
│   layers fully active)                                      │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  RING 2: Full EU + Schengen (non-euro)                │  │
│  │  (e.g. Sweden, Czechia, Romania; monetary policy      │  │
│  │   remains national; fiscal coordination partial)      │  │
│  │                                                       │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  RING 3: Full EU + significant opt-outs         │  │  │
│  │  │  (e.g. Denmark; multiple supranational layers   │  │  │
│  │  │   filtered out; collision signals suppressed    │  │  │
│  │  │   for opted-out domains)                        │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

When simulating an EU-level event, the activated supranational layers are filtered per national instance by `membership_rings` before collision resolution is applied. An opted-out domain produces no `treaty_conformity` collision — only `policy_divergence` signals at most.

---

## Intersection matrix: EU extensions

Extends [TOPOLOGY.md](TOPOLOGY.md) with EU-specific intersections.

| From → To | Relationship |
|-----------|--------------|
| `eu-commission` → `eu-parliament` + `eu-council` | Proposal; co-decision required |
| `eu-council` → national_cabinet (×27) | Council decisions bind national cabinets in implementation |
| `eu-parliament` ← national_parliament (×27) | Delegate positions aggregate into EP deliberation |
| `eu-court-of-justice` → national_judiciary | Preliminary rulings; conformity enforcement |
| `eu-court-of-justice` → `eu-commission` | Confirms infringement grounds |
| `eu-transnational-ops` → national transnational_ops_interface | Operational coordination; judicial gate required |
| national_charter → `eu-court-of-justice` | Collision check (treaty_conformity path) |
| `eu-commission` → national_instance | Infringement proceedings if collision unresolved |
| EU Council unanimity requirement → national_cabinet veto | State veto blocks EU Council output for unanimity domains |

---

## Signal routing for EU-level events

| Signal type | National layer activation | Supranational layer activation |
|-------------|--------------------------|-------------------------------|
| Cross-border enforcement | `transnational_ops_interface` (all relevant states) | `eu-transnational-ops` + `eu-court-of-justice` |
| Legislative proposal | `national_parliament` (via EP delegates) | `eu-parliament` + `eu-commission` + `eu-council` |
| Rule-of-law tension | `national_judiciary` (affected state) | `eu-court-of-justice` + Article 7 analog |
| Monetary/fiscal | `national_cabinet` (finance minister slot) | `eu-council` (ECOFIN configuration) |
| Treaty conformity dispute | `national_charter` + `national_judiciary` | `eu-court-of-justice` + `eu-commission` |

---

## Autonomy dials: EU-level layer defaults

| Layer | Parameter | Default | Notes |
|-------|-----------|---------|-------|
| `eu-parliament` | `autonomy_dial` | 0.70 | Delegate aggregation; human oversight retained |
| `eu-commission` | `autonomy_dial` | 0.65 | Proposal engine; human Commissioner oversight |
| `eu-council` | `autonomy_dial` | 0.60 | Intergovernmental; lower AI autonomy by design |
| `eu-court-of-justice` | `judiciary_ai_pct` | 0.55 | High epistemic caution; close to national judiciary defaults |
| `eu-transnational-ops` | `transnational_ops_ai_pct` | 0.60 | Same as base layer; `judicial_gate_bypass: false` invariant |
| national_parliament (per state) | `autonomy_dial` | 0.70 | Adjusted per `ai_readiness_level` |
| national_cabinet (per state) | `autonomy_dial` | 0.60 | Adjusted per `ai_readiness_level` |
| national_judiciary (per state) | `judiciary_ai_pct` | 0.55 | Conservative default |

---

## Related documents

- [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) — base topology; EU layers extend this
- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — parliament role isomorphism (national + EU parliament inherit this)
- [AI_JUDICIARY.md](AI_JUDICIARY.md) — judiciary constraint model (national + EU court inherit this)
- [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) — transnational ops base (EU layer extends this)
- [TOPOLOGY.md](TOPOLOGY.md) — base intersection matrix
- [EU_STATES.md](EU_STATES.md) — all 27 member states mapped
- `schemas/state-profile.json` — national instance JSON schema
- `schemas/institution-layer-id.json` — stable layer IDs including EU additions

---

*Phase classification: Phase 3 (institutional depth — multi-state topology extension). See ROADMAP.md.*
