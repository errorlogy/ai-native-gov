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
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │ Ministries │   │ Parliament │   │  Interpol  │
       │ (domain)   │   │(deliberate)│   │ (cross-    │
       │            │   │            │   │  border)   │
       └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
             │                │                │
             └────────┬───────┴───────┬────────┘
                      │               │
                      ▼               ▼
               ┌────────────┐  ┌────────────┐
               │ Executive  │  │ Judiciary  │
               │ (execute)  │  │ (constrain)│
               └─────┬──────┘  └─────┬──────┘
                     │               │
                     └───────┬───────┘
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

## Intersection matrix

| From → To | Relationship |
|-----------|--------------|
| Parliament → Executive | Legislative posture constrains executable actions |
| Executive → Judiciary | Actions may be challenged; judiciary sets bounds |
| Judiciary → Executive | Rulings block or reshape execution paths |
| Interpol → Executive | Cross-border enforcement enables or blocks action |
| Ministries → Parliament | Domain expertise shapes deliberation inputs |
| Parliament → Interpol | International agreements trigger coordination |
| Judiciary ↔ Interpol | Jurisdiction disputes, extradition modeling |

## Checks and balances

| Check | Mechanism |
|-------|-----------|
| Executive vs Judiciary | Executive proposals carry judicial risk score |
| Parliament vs Executive | Dissent ratio caps executive confidence |
| Interpol vs Executive | Cross-border actions require coordination clearance |
| Ministries vs Parliament | Sector forecasts can contradict parliamentary consensus |

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
