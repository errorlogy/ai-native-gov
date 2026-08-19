# AI Parliament

## Role

The **Parliament layer** models multi-actor deliberation — parties, coalitions, international assemblies — synthesizing positions on incoming signals.

## Functions

| Function | Description |
|----------|-------------|
| Deliberation | Aggregate positions from modeled actors (states, parties, blocs) |
| Consensus mapping | Identify agreement zones and fault lines |
| Legislative posture | Output modeled "bill-like" stances without claiming legal authority |
| Dissent tracking | Explicit minority positions for downstream confidence scoring |

## Inputs

- Raw signals (summit announcements, votes, speeches)
- Ministry domain briefs (finance, defense, etc.)
- Prior parliamentary outputs (session continuity)

## Outputs

| Output | Consumer |
|--------|----------|
| `consensus_score` (0–1) | Synthesis, Errorlogy |
| `dissent_map` (actor → position) | politic.bar narratives |
| `legislative_posture` (structured) | Executive, Judiciary |

## Intersections

- **→ Executive**: Posture defines feasible action set
- **→ Interpol**: International treaty posture triggers coordination
- **← Ministries**: Domain expertise feeds deliberation
- **↔ Judiciary**: Constitutional challenges modeled as parliamentary risk

## Modeling notes

- Multiple chambers can be modeled (e.g. lower/upper, EU Parliament vs national)
- Time dimension: session phases, election cycles affect weights
- Not predictive of actual votes — models **interpretive structure** for agents

## Related

- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — literal role-mapping simulator (Speaker, parties, ministers, PM, autonomy dials)
- [TOPOLOGY.md](TOPOLOGY.md)
- [executive.md](executive.md)
- [judiciary.md](judiciary.md)
