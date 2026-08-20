# Institutions Overview

AI Native Gov models **institutions as processing layers** — each applies checks, constraints, and synthesis to geopolitical signals before outputs feed Errorlogy and politic.bar.

At **world scale**, the simulator stacks three tiers: **national instances** (per-country full stacks with configurable human↔AI dials), **regional blocs** (EU as the first reference implementation; ASEAN, AU, Mercosur as planned stubs), and a **global coordination layer** (planned) that mediates cross-bloc tensions without claiming sovereignty. See [GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md).

## Institutional map

| Institution | Model role | Primary output |
|-------------|------------|----------------|
| [Charter](CHARTER.md) | Constitutional foundation — permissions, prohibitions, human override hook | `charter_status`: PERMITTED / CONDITIONAL / PROHIBITED |
| [Parliament](parliament.md) | Multi-actor deliberation, legislative posture | Consensus, dissent, bill-like proposals |
| [AI Parliament](AI_PARLIAMENT.md) | Literal role-mapping simulator (Speaker, parties, ministers, PM) | Isomorphic agent graph, autonomy dials, phased human→AI modeling |
| [AI Cabinet](AI_CABINET.md) | PM coordination + cabinet ensemble; executive intent synthesis | `cabinet_intent`, `action_likelihood` |
| [AI Ministries](AI_MINISTRIES.md) | Domain executive agents (Finance, Justice, Interior, Foreign Affairs, Science/Tech) | `portfolio_posture`, `implementation_capacity` per domain |
| [Executive](executive.md) | Abstract policy execution layer | Implementation paths, executive orders (modeled) |
| [Judiciary](judiciary.md) | Dispute resolution, precedent | Rulings, legitimacy constraints |
| [Interpol](interpol.md) | Cross-border coordination | Jurisdiction bridges, enforcement posture |

## Ministries

Domain-specific layers that feed into Cabinet and Parliament. See [AI_MINISTRIES.md](AI_MINISTRIES.md) for full ministry template and each domain doc.

| Ministry | Layer ID | Domain |
|----------|----------|--------|
| Finance | `institution:minister-finance` | Sanctions, trade, currency, fiscal signals |
| Justice | `institution:minister-justice` | Legal framework, rights signals, Judiciary interface |
| Interior / Public Safety | `institution:minister-interior` | Civil order, emergency management, internal enforcement signals |
| Foreign Affairs | `institution:minister-foreign-affairs` | Diplomacy, treaties, Transnational Ops interface |
| Science / Technology | `institution:minister-science-tech` | AI regulation, cyber, platform governance, research policy |

Additional ministries (Defense, Climate, etc.) can be added using the ministry template in [AI_MINISTRIES.md](AI_MINISTRIES.md).

## How institutions interact

No institution operates alone. See [TOPOLOGY.md](TOPOLOGY.md) for intersection maps.

**Example flow:**

1. Signal enters (e.g. bilateral summit announcement)
2. Parliament models deliberation across parties/states
3. Executive models likely policy actions
4. Judiciary models legal constraints on those actions
5. Interpol models cross-border enforcement if applicable
6. Synthesized output → Errorlogy validation → politic.bar streams

## Modeling vs reality

These are **AI modeling layers**, not operational governments. They provide:

- Structured reasoning scaffolding for agents
- Explicit disagreement and constraint surfaces
- Reproducible scenario analysis (see `docs/examples/`)

## Global AI governance

Three-tier world model — national → regional bloc → global coordination. EU is the reference regional implementation; human involvement varies per country via autonomy dials. Full framing: [GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md).

## EU multi-level topology

The simulator also models the EU as a two-tier `INSTITUTIONAL_MODEL`: one `EU_SUPRANATIONAL_LAYER` plus 27 `NATIONAL_INSTANCES`. See [EU_TOPOLOGY.md](EU_TOPOLOGY.md) (roles and collisions) and [EU_SCHEMA.md](EU_SCHEMA.md) (mermaid diagrams). Member-state parameters: [EU_STATES.md](EU_STATES.md).

## AI Government simulator

For the full AI-Native Government simulator — all layers, autonomy dial table, gradual replacement phases, and epistemic guarantees in one place — see [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md).

Individual simulator docs:

| Document | Description |
|----------|-------------|
| [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | Speaker, parties, ministers, PM, autonomy dials |
| [AI_JUDICIARY.md](AI_JUDICIARY.md) | Procedural constraint layer, due process, NAMM integration |
| [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) | Cross-border coordination, routing, audit trail |
| [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) | Veto, appeal, audit, dead man's switch |

## Constitutional foundation

The **AI Charter** ([CHARTER.md](CHARTER.md)) is the hard-stop layer above all others. It defines what agents may and may not do, propagates permission constraints to every downstream layer, and provides the human override hook. No parliamentary resolution, cabinet plan, or ministerial output is valid against a `charter_status: PROHIBITED` ruling.

## Related docs

- [GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md) — three-tier world model (national → regional → global)
- [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) — master map (all layers + autonomy dials)
- [EU_SCHEMA.md](EU_SCHEMA.md) — EU two-tier mermaid schema (INSTITUTIONAL_MODEL)
- [EU_TOPOLOGY.md](EU_TOPOLOGY.md) — EU supranational vs national instances
- [EU_STATES.md](EU_STATES.md) — 27 national instance profiles
- [CHARTER.md](CHARTER.md) — constitutional foundation, permissions, human override hook
- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — role-mapping simulator
- [AI_JUDICIARY.md](AI_JUDICIARY.md) — procedural constraint, due process, NAMM integration
- [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) — cross-border coordination layer
- [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) — veto, appeal, audit, dead man's switch
- [AI_CABINET.md](AI_CABINET.md) — PM coordination, cabinet ensemble, decision flow
- [AI_MINISTRIES.md](AI_MINISTRIES.md) — domain executive agents
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [ARCHITECTURE.md](../ARCHITECTURE.md) — system architecture
- Integrations: [ERRORLOGY.md](../integrations/ERRORLOGY.md), [POLITIC_BAR.md](../integrations/POLITIC_BAR.md)
