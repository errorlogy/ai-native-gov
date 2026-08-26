# AI National Instance — Per-Country Institutional Stack

**Epistemic label:** `INSTITUTIONAL_MODEL` — each national instance is an analytical modeling construct. No claim of sovereignty, legal authority, or operational government capacity over any real state.

## Purpose

An **AI National Instance** is a complete institutional stack for one country, parameterized by `state:{iso2}` (e.g. `state:DE`, `state:FR`). It extends the single-jurisdiction map in [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) with explicit **national** roles: charter, parliament, cabinet, ministries, monetary system, judiciary, transnational interface, and human oversight dials.

National instances are **independent** within the simulator. Regional blocs ([EU_TOPOLOGY.md](EU_TOPOLOGY.md)) and the global layer ([GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md)) coordinate and surface collisions — they do not replace national stacks.

---

## Stack template

Each `state:{iso2}` instance runs:

```text
┌─────────────────────────────────────────────────────────────┐
│  state:{iso2} — NATIONAL_INSTANCE                           │
│                                                             │
│  institution:charter (national charter variant)             │
│  institution:parliament + AI Parliament slots               │
│  institution:ai-pm + institution:cabinet-mas                │
│  institution:ai-minister × N (ministries)                   │
│  institution:executive                                      │
│  institution:central-bank-analog                            │
│  institution:treasury-analog                                │
│  institution:regulatory-agency                              │
│  institution:agentic-economics                              │
│  institution:judiciary + AI Judiciary slots                 │
│  institution:transnational-ops (national interface)         │
│  Human oversight (structural; not an AI ministry)           │
│  institution:audit | institution:ombudsman (when activated) │
└─────────────────────────────────────────────────────────────┘
         ▲                              │
         │ treaty / collision           │ fin_crypto / gov_data ingress
         │                              ▼
┌─────────────────────────────────────────────────────────────┐
│  bloc:{code} — REGIONAL_BLOC (optional, e.g. bloc:eu)       │
└─────────────────────────────────────────────────────────────┘
```

Layer ID for the instance container: `institution:national-instance` (used in cross-layer envelopes when the whole stack is activated).

---

## National vs EU vs global

| Tier | ID pattern | Example | Doc |
|------|------------|---------|-----|
| National | `state:{iso2}` | `state:PL` | This doc + [EU_STATES.md](EU_STATES.md) profiles |
| Regional bloc | `bloc:{code}` | `bloc:eu` | [EU_TOPOLOGY.md](EU_TOPOLOGY.md) |
| Global | `global:*` | planned | [GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md) |

EU member states carry **dual membership**: full national stack **plus** supranational EU roles. Non-EU countries use the same national template without `bloc:eu` collision paths unless configured.

---

## Executive branch (national)

| Component | Layer ID | Doc |
|-----------|----------|-----|
| Prime Minister / coordinator | `institution:ai-pm` | [AI_CABINET.md](AI_CABINET.md) |
| Cabinet ensemble | `institution:cabinet-mas` | [AI_CABINET.md](AI_CABINET.md) |
| Domain ministers | `institution:minister-*` | [AI_MINISTRIES.md](AI_MINISTRIES.md) |
| Abstract execution | `institution:executive` | [executive.md](executive.md) |

**PM Office (modeled):** The AI PM slot includes cabinet secretariat functions via `institution:cabinet-mas` — agenda aggregation, inter-ministerial conflict surfacing, and accountability loop to Parliament. There is no separate sovereign "PM Office" layer; coordination is explicit in [AI_CABINET.md](AI_CABINET.md).

---

## Monetary and fiscal (national)

| Component | Layer ID | Doc |
|-----------|----------|-----|
| Central bank analog | `institution:central-bank-analog` | [AI_MONETARY_SYSTEM.md](AI_MONETARY_SYSTEM.md) |
| Treasury analog | `institution:treasury-analog` | [AI_MONETARY_SYSTEM.md](AI_MONETARY_SYSTEM.md) |
| Markets regulator | `institution:regulatory-agency` | [AI_MONETARY_SYSTEM.md](AI_MONETARY_SYSTEM.md) |
| Agentic / on-chain economics | `institution:agentic-economics` | [AI_MONETARY_SYSTEM.md](AI_MONETARY_SYSTEM.md) |
| Finance ministry | `institution:minister-finance` | [AI_MINISTRIES.md](AI_MINISTRIES.md) |

Fin-crypto ingress routes per [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md). Gov fiscal ingress routes per [GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md).

---

## Legislature, judiciary, oversight

| Component | Layer ID | Doc |
|-----------|----------|-----|
| Parliament (abstract) | `institution:parliament` | [parliament.md](parliament.md) |
| AI Parliament simulator | `institution:ai-speaker`, `party-coalition`, etc. | [AI_PARLIAMENT.md](AI_PARLIAMENT.md) |
| Judiciary (abstract) | `institution:judiciary` | [judiciary.md](judiciary.md) |
| AI Judiciary simulator | `institution:ai-presiding-judge`, etc. | [AI_JUDICIARY.md](AI_JUDICIARY.md) |
| Human oversight | *(human layer)* | [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) |
| Charter | `institution:charter` | [CHARTER.md](CHARTER.md) |

---

## Instance parameters (EU reference)

Member-state profiles in [EU_STATES.md](EU_STATES.md) include:

| Field | Meaning |
|-------|---------|
| `integration_depth` | EU treaty integration (0–1) |
| `membership_rings` | eurozone, schengen, defense, JHA opt-outs |
| `ai_readiness_level` | Modeled Phase 0–4 default for national dials |
| `rule_of_law_tension` | Collision signal weight with EU judiciary analog |

These parameters adjust autonomy dials and collision resolution — they do not assert real-world legal status.

---

## Signal ingress by jurisdiction

Cross-layer events should tag `jurisdiction_set` ([GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md)):

| Ingress | Typical activation |
|---------|-------------------|
| `gov_parliamentary_activity` | `state:{iso2}` parliament + `institution:parliament` |
| `gov_open_data_snapshot` | national ministries + treasury/central-bank analogs |
| `fin_crypto_market_snapshot` | multiple `state:{iso2}` instances + optional `bloc:eu` |
| `gov_legislative_document` | national + bloc legal layers when CELEX/EU scope |

Multi-jurisdiction shocks activate many national instances in parallel without implying a single global executive ([GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md)).

---

## Adding a new national instance

1. Assign `state:{iso2}` and document profile (copy [EU_STATES.md](EU_STATES.md) row template for non-EU states)
2. Set autonomy dial defaults per [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md)
3. Configure bloc membership (`bloc:*`) if applicable
4. Wire ingress adapters with `jurisdiction_set`
5. Update [TOPOLOGY.md](TOPOLOGY.md) if new cross-layer intersections appear

---

## Related docs

- [GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md) — three-tier world model
- [EU_STATES.md](EU_STATES.md) — 27 EU member profiles
- [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) — master layer map
- [AI_MONETARY_SYSTEM.md](AI_MONETARY_SYSTEM.md) — monetary/fiscal/regulatory/agentic layers
- [AI_CABINET.md](AI_CABINET.md) — executive cabinet detail
- [TOPOLOGY.md](TOPOLOGY.md) — intersections
