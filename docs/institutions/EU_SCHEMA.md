# EU AI-State Schema (visual)

**Epistemic label:** `INSTITUTIONAL_MODEL` — diagrams model the European Union as a two-tier topology inside the AI-Native Government simulator. They are not a claim of legal authority, sovereign standing, or real-world governance capacity.

This page is the **look-at-it** schema. Narrative, collision taxonomy, and dials live in [EU_TOPOLOGY.md](EU_TOPOLOGY.md). Member-state parameters live in [EU_STATES.md](EU_STATES.md). Stable IDs: `schemas/institution-layer-id.json`. National instance fields: `schemas/state-profile.json`.

---

## Diagram 1 — Two-tier structure and role mapping

National parliaments send **delegates** into EU Parliament. National ministers sit in EU Council. The Commission is the **EU-level executive**. ECJ and national judiciary are **co-present constraint layers** (tension, not a verdict). Transnational Ops always uses the national judicial-gate interface. Human Oversight is a hard stop on both tiers.

```mermaid
flowchart TB
  HO["Human Oversight — HARD STOP<br/>human_override_always true<br/>AI cannot disable this layer"]

  subgraph EU["EU_SUPRANATIONAL_LAYER ×1"]
    direction LR
    euParl["EU Parliament<br/>eu-parliament"]
    euComm["EU Commission<br/>eu-commission<br/>EU executive"]
    euCouncil["EU Council<br/>eu-council"]
    euECJ["Court of Justice<br/>eu-court-of-justice"]
    euOps["Transnational Ops<br/>eu-transnational-ops<br/>Europol / Frontex analog"]
    euParl --- euComm
    euComm --- euCouncil
    euComm --> euECJ
    euECJ --> euOps
  end

  subgraph NAT["NATIONAL_INSTANCES ×27 — template"]
    direction TB
    nCharter["National Charter<br/>institution:charter"]
    nParl["National Parliament<br/>Speaker / parties MAS"]
    nCab["Cabinet / PM<br/>ai-pm + ministers"]
    nMin["Ministries<br/>domain portfolios"]
    nJud["National Judiciary"]
    nOpsIf["Transnational Ops interface<br/>judicial gate required"]
    nCharter --> nParl
    nCharter --> nCab
    nCharter --> nJud
    nParl --> nCab
    nCab --> nMin
    nMin --> nOpsIf
    nJud --> nOpsIf
  end

  HO -.->|veto / appeal / audit| EU
  HO -.->|veto / appeal / audit| NAT

  nParl -->|"delegates D'Hondt analog"| euParl
  nCab -->|"ministers sit in Council"| euCouncil
  euComm -->|"proposals + infringement path"| NAT
  nJud -.->|"conformity / preliminary ruling TENSION"| euECJ
  nOpsIf -->|"ops packet after judicial gate"| euOps
  nCharter -.->|"treaty vs charter TENSION"| euECJ
```

---

## Diagram 2 — Collision and event flow (μ/α, not verdicts)

When a national charter or national output diverges from an EU-layer requirement, the simulator emits a `collision_signal`. Opt-outs **filter** activation (no `treaty_conformity` collision). Unresolved tension routes to Errorlogy as fuzzy membership — **not** guilt or legitimacy verdicts. Human Oversight can halt the cascade at any step.

```mermaid
flowchart TB
  ingress["Signal ingress<br/>legislative / ops / rule-of-law"]

  subgraph NATF["National instance"]
    nCh["National Charter check"]
    nStack["Parliament → Cabinet → Ministries"]
    nJ["National Judiciary"]
    nGate["Ops interface + judicial gate"]
    nCh --> nStack --> nJ --> nGate
  end

  subgraph EUF["EU_SUPRANATIONAL_LAYER"]
    euC["Commission proposal / monitoring"]
    euP["Parliament co-decision"]
    euR["Council QMV or unanimity"]
    euJ["ECJ procedural constraint"]
    euO["eu-transnational-ops"]
    euC --> euP --> euR
    euR --> euJ
    euJ --> euO
  end

  collide{"collision_signal?"}
  optOut["opt_out_activation<br/>filter layers — expected divergence"]
  tax["Collision taxonomy<br/>treaty_conformity<br/>fundamental_rights<br/>policy_divergence<br/>rule_of_law_tension"]
  err["Errorlogy μ_divergence / α_escalation / PNO_block<br/>INSTITUTIONAL_MODEL — not a verdict"]
  pb["politic.bar streams"]
  HO2["Human Oversight HARD STOP<br/>cannot be disabled by AI"]

  ingress --> nCh
  ingress --> euC
  nGate --> collide
  euJ --> collide
  nCh -.-> collide
  collide -->|"registered opt-out domain"| optOut
  collide -->|"divergence"| tax
  tax --> err --> pb
  optOut -.->|"no treaty_conformity"| err

  HO2 -.->|halt / remand / dial rollback| NATF
  HO2 -.->|halt / remand / dial rollback| EUF
  HO2 -.->|halt| collide
```

---

## Diagram 3 — Variable geometry (integration rings)

The EU is not a uniform bloc. Before collision resolution, each national instance filters activated EU layers by `membership_rings` and `opt_outs` (`state-profile.json`). Rings are **modeling clusters**, not ranks of legitimacy.

```mermaid
flowchart TB
  ringsFilter["membership_rings + opt_outs<br/>filter which EU layers activate"]

  subgraph RING1["RING 1 — Full + Eurozone + Schengen<br/>integration_depth ~ 0.90–1.00"]
    r1["DE FR IT ES NL BE PT AT FI EE LU MT SI LT LV HR SK GR …<br/>all supranational layers active"]
  end

  subgraph RING2["RING 2 — Full EU with a ring gap<br/>integration_depth ~ 0.75–0.89"]
    r2a["Non-euro or eurozone-pending: SE CZ RO BG PL<br/>monetary policy stays national"]
    r2b["Schengen gap or partial: IE CY<br/>ops routing adjusted"]
  end

  subgraph RING3["RING 3 — Significant opt-outs<br/>integration_depth ~ 0.40–0.59"]
    r3["DK — eurozone, defense, JHA opt-outs<br/>collision suppressed in opted-out domains"]
  end

  subgraph TENSION["Ring membership is not compliance alignment"]
    hu["HU — inside euro + Schengen<br/>rule_of_law_tension high μ — Errorlogy not a verdict"]
  end

  ringsFilter --> RING1
  ringsFilter --> RING2
  ringsFilter --> RING3
  RING1 -.-> TENSION
```

---

## How to read the schema

| Element | Meaning in the simulator |
|---------|--------------------------|
| Two tiers | 27 full national stacks + one EU coordination layer. EU does not replace national instances. |
| Delegate / minister arrows | Aggregation into EP and Council — not a transfer of sovereignty. |
| Commission | EU-level executive analog (`institution:eu-commission`). |
| Dashed judiciary / charter arrows | Modeled **tension**. Feeds Errorlogy μ/α. Not a court verdict. |
| Judicial gate | `judicial_gate_bypass: false` — invariant on transnational ops. |
| Human Oversight | Structural hard stop; AI agents cannot remove or route around it. |
| Rings | Variable geometry. Opt-outs filter layer activation. |

---

## Related documents

- [EU_TOPOLOGY.md](EU_TOPOLOGY.md) — role definitions, collision taxonomy, autonomy dials
- [EU_STATES.md](EU_STATES.md) — all 27 member-state profiles
- [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) — base national stack
- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — Speaker / parties / ministers / PM
- [CHARTER.md](CHARTER.md) — charter constraints and human override hook
- [OVERVIEW.md](OVERVIEW.md) — short institutional map
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — umbrella data flow

---

*Phase classification: Phase 3 (institutional depth — visual schema). See ROADMAP.md.*
