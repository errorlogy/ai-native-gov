# AI Executive

## Role

The **Executive layer** models policy execution — what actions governments and leaders are likely to take given parliamentary posture, judicial constraints, and operational capacity.

## Functions

| Function | Description |
|----------|-------------|
| Action likelihood | Score probable executive actions (orders, deployments, diplomacy) |
| Implementation paths | Sequence of steps from signal to action |
| Capacity assessment | Resources, timing, political capital required |
| Escalation modeling | De-escalation and escalation branches |

## Inputs

- Parliamentary `legislative_posture` and `consensus_score`
- Judicial constraints and risk scores
- Interpol coordination status (for cross-border actions)
- Ministry operational briefs

## Outputs

| Output | Consumer |
|--------|----------|
| `action_likelihood` (action → probability) | Synthesis, Errorlogy |
| `implementation_timeline` | politic.bar streams |
| `escalation_branches` | Examples, scenario docs |

## Intersections

- **← Parliament**: Constrained by legislative posture and dissent
- **→ Judiciary**: Actions may trigger judicial review modeling
- **↔ Interpol**: Cross-border actions require coordination clearance
- **← Ministries**: Operational reality (defense readiness, fiscal headroom)

## Modeling notes

- Distinguish **announced intent** vs **executable action**
- Executive confidence capped by parliamentary dissent ratio (see TOPOLOGY.md)
- Multiple executives in a scenario (e.g. US + France) modeled in parallel with interaction edges

## Related

- [TOPOLOGY.md](TOPOLOGY.md)
- [parliament.md](parliament.md)
- [judiciary.md](judiciary.md)
- [interpol.md](interpol.md)
