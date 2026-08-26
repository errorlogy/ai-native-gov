# Institutional Topology

Topology defines **how institutional layers intersect** — which layers can constrain, override, or amplify each other.

## Layer diagram

```
                         ┌──────────────┐
                         │   Ingress    │
                         │  (signals)   │
                         └──────┬───────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
       ┌────────────┐   ┌────────────────────┐   ┌──────────────────┐
       │ Ministries │   │ AI Parliament      │   │ Transnational Ops│
       │ (domain)   │   │ ┌────────────────┐ │   │ (cross-border;   │
       │            │   │ │ AI Speaker     │ │   │  separate layer) │
       └─────┬──────┘   │ │ Party MAS      │ │   └────────┬─────────┘
             │          │ │ AI Ministers   │ │            │
             │          │ │ AI PM          │ │            │
             │          │ └────────────────┘ │            │
             │          │ + Charter/Legal    │            │
             │          │ + Human oversight  │            │
             │          └─────────┬──────────┘            │
             │                    │                       │
             └────────┬───────────┴───────────┬───────────┘
                      │                       │
                      ▼                       ▼
               ┌────────────┐          ┌────────────┐
               │ Executive  │          │ Judiciary  │
               │ (execute)  │          │ (constrain)│
               └─────┬──────┘          └─────┬──────┘
                     │                       │
                     └───────┬───────────────┘
                             ▼
                    ┌────────────────┐
                    │   Synthesis    │
                    │ (checks &      │
                    │  balances)     │
                    └────────┬───────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
       ┌────────────┐                 ┌────────────┐
       │ Errorlogy  │                 │ politic.bar│
       └────────────┘                 └────────────┘
```

> **AI Parliament detail:** literal role isomorphism, autonomy dials, and Speaker modes — see [AI_PARLIAMENT.md](AI_PARLIAMENT.md). Transnational Ops maps to [interpol.md](interpol.md) at the abstract layer; `institution:transnational-ops` is the simulator-specific ID.

## Intersection matrix

| From → To | Relationship |
|-----------|--------------|
| Parliament → Executive | Legislative posture constrains executable actions |
| Executive → Judiciary | Actions may be challenged; judiciary sets bounds |
| Judiciary → Executive | Rulings block or reshape execution paths |
| Interpol / Transnational Ops → Executive | Cross-border enforcement enables or blocks action |
| Ministries → Parliament | Domain expertise shapes deliberation inputs |
| Parliament → Interpol / Transnational Ops | International agreements trigger coordination |
| Judiciary ↔ Interpol / Transnational Ops | Jurisdiction disputes, extradition modeling |
| AI Speaker → Party MAS | Procedural control only; no policy override |
| Party MAS → AI PM | Coalition consensus feeds cabinet synthesis |
| AI Ministers → AI PM | Portfolio postures aggregate to executive intent |
| AI PM → Executive | Cabinet intent becomes action likelihood |
| Human oversight → all AI slots | Veto and autonomy dial rollback |
| Charter/Legal → all layers | Procedural validity constraints |
| Central bank analog → Treasury analog | Monetary stability signals constrain fiscal headroom hypotheses |
| Treasury analog → Finance Ministry | Fiscal capacity caps minister `branch_likelihood` |
| Regulatory agency → Judiciary | Market integrity hypotheses become dispute surfaces (not verdicts) |
| Agentic economics → Central bank / Regulatory | On-chain liquidity and platform context feed monetary and oversight layers |
| Agentic economics → Transnational Ops | Cross-border on-chain risk routes to coordination layer |
| FIN_CRYPTO ingress → Monetary stack | Normalized market events activate central-bank, treasury, regulatory, agentic layers per [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md) |
| National instance → Regional bloc | Treaty collisions and delegate aggregation (EU: [EU_TOPOLOGY.md](EU_TOPOLOGY.md)) |

## Checks and balances

| Check | Mechanism |
|-------|-----------|
| Executive vs Judiciary | Executive proposals carry judicial risk score |
| Parliament vs Executive | Dissent ratio caps executive confidence |
| Interpol / Transnational Ops vs Executive | Cross-border actions require coordination clearance |
| Ministries vs Parliament | Sector forecasts can contradict parliamentary consensus |
| AI Speaker vs Party MAS | Speaker procedural-only; parties hold substantive positions |
| Human oversight vs AI agents | Veto enabled per role; autonomy dial rollback |
| Charter/Legal vs Parliament | Invalid procedure blocks downstream synthesis |
| Central bank analog vs Executive | Monetary independence modeled as constraint on executive fiscal pressure |
| Regulatory agency vs Agentic economics | Oversight posture vs on-chain coordination hypotheses (peer tension) |
| Treasury vs Finance Ministry | Fiscal capacity constrains minister portfolio without PM override |

## Signal routing rules

1. **Bilateral diplomatic** → Parliament + Executive first; Interpol if multilateral enforcement implied
2. **Legal/regulatory** → Judiciary + Parliament; Executive for implementation
3. **Sanctions/trade** → Ministries (finance) + Executive + Interpol
4. **Military/security** → Ministries (defense) + Executive + Interpol
5. **Market / crypto snapshot** → Central bank analog + Regulatory agency + Treasury analog; Executive for stability context ([FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md))
6. **On-chain risk / DeFi stress** → Agentic economics + Regulatory agency + Judiciary; Transnational Ops if cross-border ([AI_MONETARY_SYSTEM.md](AI_MONETARY_SYSTEM.md))
7. **Fiscal / macro open data** → Treasury analog + Finance Ministry + optional `bloc:eu` coordination ([GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md))

## Topology evolution

Topology is versioned in this doc. Machine-readable graph planned in Phase 3 ([ROADMAP.md](../ROADMAP.md)).

When adding a new intersection:

1. Update this matrix
2. Update affected institution docs
3. Update integration contracts if output shape changes

## Example

See [trump-macron-cascade.md](../examples/trump-macron-cascade.md) for a full cascade through multiple layers.

For the AI Parliament role-mapping simulator (cross-border tracking request through Speaker → parties → minister → Transnational Ops → Judiciary), see [AI_PARLIAMENT.md](AI_PARLIAMENT.md#example-cascade-cross-border-tracking-request).
