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

## Signal routing rules

1. **Bilateral diplomatic** → Parliament + Executive first; Interpol if multilateral enforcement implied
2. **Legal/regulatory** → Judiciary + Parliament; Executive for implementation
3. **Sanctions/trade** → Ministries (finance) + Executive + Interpol
4. **Military/security** → Ministries (defense) + Executive + Interpol

## Topology evolution

Topology is versioned in this doc. Machine-readable graph planned in Phase 3 ([ROADMAP.md](../ROADMAP.md)).

When adding a new intersection:

1. Update this matrix
2. Update affected institution docs
3. Update integration contracts if output shape changes

## Example

See [trump-macron-cascade.md](../examples/trump-macron-cascade.md) for a full cascade through multiple layers.

For the AI Parliament role-mapping simulator (cross-border tracking request through Speaker → parties → minister → Transnational Ops → Judiciary), see [AI_PARLIAMENT.md](AI_PARLIAMENT.md#example-cascade-cross-border-tracking-request).
