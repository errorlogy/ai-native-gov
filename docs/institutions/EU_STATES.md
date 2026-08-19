# EU Member States — Simulation Map

**Epistemic label:** `INSTITUTIONAL_MODEL` — all integration depth scores, tension signal estimates, and AI readiness levels are analytical modeling contributions for the AI-Native Government simulator. They are not assessments of real-world governance quality, legitimacy, or legal standing.

---

## Overview

All 27 EU member states are modeled as `NATIONAL_INSTANCES` within the EU multi-level topology ([EU_TOPOLOGY.md](EU_TOPOLOGY.md)). Each instance runs a full institutional stack (national_parliament, national_cabinet, national_judiciary, transnational_ops_interface) constrained by a national_charter and coordinated by the EU supranational layer.

This document provides the complete mapping table, integration depth clusters, and a curated set of interesting tension cases for simulation scenarios.

---

## Full member state table

| # | State | Code | Legal family | System type | Integration depth | Membership rings | AI readiness | Notable tension signals |
|---|-------|------|-------------|------------|------------------|-----------------|-------------|------------------------|
| 1 | Germany | DE | romano-germanic | federal-republic | 0.95 | full, eurozone, schengen | 3 | — |
| 2 | France | FR | romano-germanic | semi-presidential-republic | 0.93 | full, eurozone, schengen | 3 | policy_divergence (sovereignty framing) |
| 3 | Italy | IT | romano-germanic | republic | 0.90 | full, eurozone, schengen | 2 | policy_divergence (fiscal) |
| 4 | Spain | ES | romano-germanic | parliamentary-monarchy | 0.91 | full, eurozone, schengen | 2 | — |
| 5 | Netherlands | NL | romano-germanic | parliamentary-monarchy | 0.92 | full, eurozone, schengen | 3 | — |
| 6 | Belgium | BE | romano-germanic | federal parliamentary-monarchy | 0.91 | full, eurozone, schengen | 2 | — |
| 7 | Portugal | PT | romano-germanic | semi-presidential-republic | 0.90 | full, eurozone, schengen | 2 | — |
| 8 | Austria | AT | romano-germanic | federal-republic | 0.91 | full, eurozone, schengen | 2 | policy_divergence (migration) |
| 9 | Greece | GR | romano-germanic | republic | 0.89 | full, eurozone, schengen | 1 | policy_divergence (fiscal sovereignty) |
| 10 | Finland | FI | nordic | republic | 0.93 | full, eurozone, schengen | 3 | — |
| 11 | Ireland | IE | common-law | republic | 0.76 | full, eurozone | 3 | opt_out_activation (schengen-partial) |
| 12 | Denmark | DK | nordic | parliamentary-monarchy | 0.52 | full, schengen | 3 | opt_out_activation (eurozone, defense, JHA) |
| 13 | Sweden | SE | nordic | parliamentary-monarchy | 0.80 | full, schengen | 3 | policy_divergence (eurozone de facto delay) |
| 14 | Poland | PL | romano-germanic | republic | 0.74 | full, eurozone*, schengen | 2 | rule_of_law_tension (partially resolved 2024) |
| 15 | Hungary | HU | romano-germanic | republic | 0.68 | full, eurozone, schengen | 1 | rule_of_law_tension (high μ), fundamental_rights |
| 16 | Czechia | CZ | romano-germanic | republic | 0.78 | full, schengen | 2 | policy_divergence (eurozone delay) |
| 17 | Romania | RO | romano-germanic | semi-presidential-republic | 0.82 | full, eurozone*, schengen | 1 | — |
| 18 | Slovakia | SK | romano-germanic | republic | 0.88 | full, eurozone, schengen | 1 | policy_divergence (foreign policy) |
| 19 | Bulgaria | BG | romano-germanic | republic | 0.83 | full, eurozone*, schengen | 1 | — |
| 20 | Croatia | HR | romano-germanic | republic | 0.90 | full, eurozone, schengen | 1 | — |
| 21 | Slovenia | SI | romano-germanic | republic | 0.91 | full, eurozone, schengen | 2 | — |
| 22 | Lithuania | LT | romano-germanic | republic | 0.92 | full, eurozone, schengen | 2 | — |
| 23 | Latvia | LV | romano-germanic | republic | 0.92 | full, eurozone, schengen | 2 | — |
| 24 | Estonia | EE | romano-germanic | republic | 0.95 | full, eurozone, schengen | 4 | policy_divergence (digital governance pace) |
| 25 | Luxembourg | LU | romano-germanic | parliamentary-monarchy | 0.94 | full, eurozone, schengen | 3 | — |
| 26 | Malta | MT | mixed | republic | 0.90 | full, eurozone, schengen | 2 | — |
| 27 | Cyprus | CY | common-law | republic | 0.85 | full, eurozone | 2 | — |

> \* Eurozone: legally required to join when convergence criteria met; not yet joined as of 2026 modeling baseline. Membership ring listed as "eurozone*" for in-progress states.

---

## Integration depth clusters

### Cluster A — Deep integration (integration_depth ≥ 0.90)

Full EU membership + eurozone + schengen, no significant opt-outs. Supranational layers fully active for all policy domains.

**States:** Germany (DE), France (FR), Italy (IT), Spain (ES), Netherlands (NL), Belgium (BE), Portugal (PT), Austria (AT), Greece (GR), Finland (FI), Estonia (EE), Luxembourg (LU), Malta (MT), Slovenia (SI), Lithuania (LT), Latvia (LV), Croatia (HR)

*Simulation note:* Collision signals in this cluster are primarily `policy_divergence` type (negotiating positions) rather than `treaty_conformity`. Rule-of-law tensions are low. EU Court of Justice referrals are routine and expected.

---

### Cluster B — Standard integration with partial gaps (0.75–0.89)

Full EU membership, either missing eurozone or schengen ring, or with moderate policy divergence patterns.

**States:** Ireland (IE, 0.76), Sweden (SE, 0.80), Czechia (CZ, 0.78), Romania (RO, 0.82), Slovakia (SK, 0.88), Bulgaria (BG, 0.83), Cyprus (CY, 0.85), Poland (PL, 0.74)

*Simulation note:* Eurozone-gap states produce `policy_divergence` signals in monetary coordination rounds. Ireland's partial schengen status creates routing adjustments for `eu-transnational-ops` flows.

---

### Cluster C — Opt-out heavy / rule-of-law tension (integration_depth < 0.75)

States with multiple registered opt-outs or active rule-of-law tension signals. Supranational layer filtering is significant.

**States:** Denmark (DK, 0.52), Hungary (HU, 0.68)

*Simulation note:* These states require special handling in collision resolution. Denmark's opt-outs suppress collision signals for opted-out domains by design. Hungary's `article7-resistance` produces sustained high-μ signals that feed the Errorlogy engine as priority tension cases.

---

## Highlighted tension cases for simulation scenarios

### Hungary (HU) — Rule-of-law tension case

**Why interesting:** Hungary presents the highest sustained `μ_divergence` score in the EU topology (estimated 0.80 for rule-of-law signals, 0.65 for fundamental rights). It is fully inside the eurozone and schengen rings yet structurally diverges from EU rule-of-law requirements — a case where `integration_depth` is a poor proxy for compliance alignment.

**Active tension signals:**
- `rule_of_law_tension` — `eu-court-of-justice` + Article 7 analog activation
- `fundamental_rights` — multiple Charter conformity disputes
- `policy_divergence` — foreign policy misalignment with EU Council consensus

**Simulation use:** Test `collision_resolution` pathways at high sustained μ. Test Errorlogy `α_escalation` accumulation over time. Model infringement proceedings cascade from `eu-commission` through `eu-court-of-justice` to national_judiciary.

---

### Poland (PL) — Partially resolved rule-of-law case

**Why interesting:** Poland transitioned from a high rule-of-law tension state (2016–2023) toward partial resolution following government change in 2023–2024. Provides a modeling scenario for tension reduction and signal decay.

**Current tension signals (2026 baseline):**
- `rule_of_law_tension` — reduced to `partially_resolved`; Article 7 analog deactivated
- EU funds previously frozen partially restored

**Simulation use:** Model tension signal decay and `resolution_status` transitions in `cross-layer-event.json`. Test signal hysteresis — does α score decay proportionally when conditions improve?

---

### Denmark (DK) — Opt-out management case

**Why interesting:** Denmark has the highest number of formal opt-outs of any full EU member, covering three major policy domains. It demonstrates that `integration_depth` can be structurally low while institutional function remains high — i.e., low integration_depth ≠ institutional dysfunction.

**Registered opt-outs:** eurozone, defense-cooperation, schengen-jha

**Simulation use:** Test opt-out filtering in supranational layer activation. Verify that opted-out domains produce no `treaty_conformity` collision signals. Model the Denmark-specific `transnational_ops_interface` routing (JHA opt-out means direct EU coordination pathways are filtered; bilateral substitutes apply).

---

### Estonia (EE) — High AI readiness case

**Why interesting:** Estonia is the only EU member modeled at `ai_readiness_level: 4` (full AI cabinet with human appeal), reflecting its digital governance infrastructure (X-Road, e-Residency, i-Voting). This creates an interesting mismatch where national autonomy dials are significantly higher than the EU supranational layer defaults.

**Current tension signals:**
- `policy_divergence` (low μ: 0.10) — digital governance pace may outrun EU AI Act compliance schedules

**Simulation use:** Test scenarios where a national instance operates at higher autonomy than the supranational layer. Model regulatory sandbox dynamics where Estonia's AI practices become reference inputs for EU Commission proposals.

---

### France (FR) — Sovereignty framing divergence

**Why interesting:** France maintains strong national sovereignty framing in industrial and agricultural policy, creating persistent `policy_divergence` signals even with deep integration. The semi-presidential system also gives the national_cabinet elevated weight relative to national_parliament — a structural asymmetry compared to most EU states.

**Simulation use:** Test cabinet-heavy vs. parliament-heavy national stack configurations. Model how semi-presidential `system_type` affects the aggregation of national positions into `eu-council` outputs. Explore strategic divergence patterns where high integration_depth coexists with persistent policy tension.

---

## Coverage notes

- AI readiness levels are modeling estimates based on publicly available digital governance indices (e-Government Development Index, Digital Economy and Society Index) as of 2026 baseline. They are not verified by NAMM certificates.
- Integration depth scores are computed from membership ring participation and registered opt-outs; they do not reflect treaty compliance quality.
- `notable_tensions` entries are analytical contributions, not guilt or legitimacy verdicts. Fuzzy membership scores (μ) are illustrative estimates; authoritative values require Errorlogy engine computation.

---

*See also:* [EU_TOPOLOGY.md](EU_TOPOLOGY.md) | [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) | `schemas/state-profile.json`

*Phase classification: Phase 3 (institutional depth). See ROADMAP.md.*
