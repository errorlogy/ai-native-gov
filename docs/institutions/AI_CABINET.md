# AI Cabinet — Prime Minister and Executive Ensemble

**Epistemic label:** `INSTITUTIONAL_MODEL` — all outputs from this layer are analytical contributions, not legal verdicts or claims of legitimate authority.

## Purpose

The **AI Cabinet** is the executive synthesis layer of the AI Native Gov simulator. It sits between parliamentary deliberation and operational execution, translating legislative posture into a coherent executive plan — subject to charter constraints, judicial gates, and human oversight.

The AI Prime Minister is a **coordinator**, not a sovereign. The cabinet is an **ensemble** — no single agent within it may unilaterally define policy.

> For the legislative layer feeding cabinet, see [AI_PARLIAMENT.md](AI_PARLIAMENT.md).  
> For domain execution agents, see [AI_MINISTRIES.md](AI_MINISTRIES.md).  
> For constitutional constraints, see [CHARTER.md](CHARTER.md).  
> For judicial gating, see [judiciary.md](judiciary.md).

---

## Role isomorphism

| Human role | AI agent slot | Layer ID | Scope |
|------------|---------------|----------|-------|
| Prime Minister | AI PM | `institution:ai-pm` | Cabinet coordination, executive intent synthesis; NOT sovereign |
| Cabinet minister | AI Minister (domain) | `institution:ai-minister` | Portfolio execution posture, domain constraints |
| Cabinet secretariat | Cabinet MAS coordinator | `institution:cabinet-mas` | Parallel minister aggregation, conflict surfacing |
| Deputy PM / acting authority | Fallback PM slot | `institution:ai-pm-fallback` | Activated when PM in human-override suspension |

---

## AI PM — coordinator, not sovereign

The **AI PM** receives inputs from three sources and synthesizes them into `cabinet_intent`:

1. **Coalition consensus** from AI Parliament (Party MAS `consensus_score`, `dissent_map`)
2. **Portfolio postures** from AI Ministers (each ministry's `portfolio_posture`, `implementation_capacity`)
3. **Judicial risk** from Judiciary layer (`judicial_risk` score, `constraint_set`)

The PM agent **cannot**:

- Override a `charter_status: PROHIBITED` ruling
- Initiate executive actions without parliamentary mandate (`consensus_score` threshold)
- Sign treaties unilaterally (requires Transnational Ops clearance + Parliament ratification)
- Override judicial constraints
- Modify its own autonomy dial without human oversight confirmation

```json
{
  "layer": "institution:ai-pm",
  "agent_role": "cabinet_coordinator",
  "inputs_required": ["coalition_consensus", "minister_postures", "judicial_risk"],
  "output": "cabinet_intent",
  "permitted_actions": [
    "cabinet_synthesis",
    "action_likelihood_emit",
    "inter_ministry_conflict_resolve",
    "escalate_to_parliament",
    "escalate_to_human_oversight"
  ],
  "forbidden_actions": [
    "judicial_override",
    "charter_override",
    "unilateral_treaty",
    "autonomy_dial_self_modify"
  ],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

### PM conflict resolution

When minister postures conflict, the PM applies a **weighted synthesis** — not an override:

| Conflict type | Resolution mechanism |
|---------------|---------------------|
| Scope overlap between ministries | PM broker note; both postures preserved in output with `tension_flag` |
| Policy direction contradiction | PM emits `inter_ministry_tension`; escalates to Parliament if unresolved |
| Resource contention (modeled) | PM emits priority ranking as `HYPOTHESIS`; requires Parliament confirmation |
| Judicial block on minister proposal | PM removes proposal from `action_likelihood`; logs `judicial_constraint_applied` |

Conflicts resolved by PM are **analytical contributions** — they surface tensions for deliberation, not verdicts.

---

## Cabinet as ensemble

The **Cabinet MAS** runs minister agents in parallel. Each minister contributes a `portfolio_posture` object. The PM coordinator aggregates these into the `cabinet_intent` envelope.

```text
┌──────────────────────────────────────────────────────────┐
│                       Cabinet MAS                        │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │ Finance     │  │  Justice    │  │  Foreign Affairs │  │
│  │ Minister    │  │  Minister   │  │  Minister        │  │
│  └──────┬──────┘  └──────┬──────┘  └────────┬─────────┘  │
│         │                │                  │            │
│  ┌──────┴──────┐  ┌──────┴──────┐  ┌────────┴─────────┐  │
│  │  Interior/  │  │  Science/   │  │   [additional    │  │
│  │  Safety     │  │  Technology │  │    ministries]   │  │
│  └──────┬──────┘  └──────┬──────┘  └────────┬─────────┘  │
│         │                │                  │            │
│         └────────────────┼──────────────────┘            │
│                          ▼                               │
│                    ┌──────────┐                          │
│                    │  AI PM   │  (coordinator)           │
│                    └──────────┘                          │
└──────────────────────────────────────────────────────────┘
```

### Cabinet reporting protocol

Ministers report to PM at each deliberation cycle:

| Report field | Type | Description |
|-------------|------|-------------|
| `portfolio_posture` | object | Domain-specific action posture |
| `implementation_capacity` | float 0–1 | Modeled capacity to execute |
| `constraint_set` | array | Active constraints (charter, judicial, resource) |
| `tension_flags` | array | Identified conflicts with other portfolio areas |
| `epistemic_label` | string | Always `INSTITUTIONAL_MODEL` |

---

## Decision flow

The full decision flow from parliamentary resolution to execution follows a strict gate sequence:

```text
1. Parliament resolution
   │  AI Parliament: Party MAS deliberation cycle concludes
   │  Output: consensus_score, dissent_map, legislative_posture
   ▼
2. Charter pre-check
   │  Charter Agent evaluates legislative_posture
   │  charter_status: PERMITTED / CONDITIONAL / PROHIBITED
   │  PROHIBITED → halt; Human override hook triggered
   ▼
3. PM synthesis
   │  AI PM ingests: coalition_consensus + minister_postures + judicial_risk
   │  Resolves inter-ministry conflicts (broker note, not override)
   │  Emits: cabinet_intent, action_likelihood
   ▼
4. Judiciary gate
   │  Judiciary evaluates cabinet_intent against precedent + statute model
   │  judicial_risk score emitted
   │  High judicial_risk → action_likelihood reduced or branch removed
   ▼
5. Transnational Ops gate (if cross-border)
   │  Transnational Ops / Interpol layer: jurisdiction check
   │  coordination_status: clear / conditional / blocked
   │  blocked → action branch removed from cabinet_intent
   ▼
6. Execution signal
   │  Remaining branches of cabinet_intent → Executive layer
   │  Each branch carries: action_likelihood, constraint_set, epistemic_label
   ▼
7. Accountability loop
   → Cabinet synthesizes outcome report
   → Report returned to Parliament (next deliberation cycle input)
   → Charter Agent logs execution trace
```

---

## Accountability loop

The cabinet does not operate in open-loop. After execution-phase outputs, the cabinet reports back to Parliament:

| Report type | Recipient | Trigger |
|-------------|-----------|---------|
| `execution_outcome` | AI Parliament | After each action cycle |
| `constraint_hit_log` | Charter Agent + Judiciary | When judicial or charter constraints applied |
| `ministry_capacity_update` | PM (internal) | Each minister's updated `implementation_capacity` |
| `inter_ministry_tension_log` | Parliament + Human oversight | When PM cannot resolve conflict |
| `anomaly_report` | Human oversight panel | Agent loop anomaly or unexpected `PROHIBITED` cluster |

Parliament uses `execution_outcome` as input to the next deliberation cycle — closing the governance loop.

---

## Autonomy dial parameters

| Parameter | Scope | Range | Meaning |
|-----------|-------|-------|---------|
| `pm_ai_pct` | AI PM | 0.0–1.0 | Share of PM coordination handled by AI agent |
| `cabinet_ai_pct` | Cabinet MAS | 0.0–1.0 | Share of cabinet deliberation handled by AI |
| `minister_ai_pct` | Per minister | 0.0–1.0 | Per-portfolio AI autonomy (see [AI_MINISTRIES.md](AI_MINISTRIES.md)) |
| `human_veto_enabled` | All cabinet slots | boolean | Human oversight can block any output |
| `escalation_threshold` | AI PM | 0.0–1.0 | Below this `consensus_score`, PM escalates to Parliament before acting |

**Typical phased profile (modeled example):**

```text
Phase 0 — Shadow:   pm_ai_pct = 0.0, cabinet_ai_pct = 0.0  (observe only)
Phase 1 — Advise:   pm_ai_pct = 0.2, cabinet_ai_pct = 0.2  (human confirms all)
Phase 2 — Execute:  pm_ai_pct = 0.5, cabinet_ai_pct = 0.5  (human veto contested)
Phase 3 — Coord:    pm_ai_pct = 0.8, cabinet_ai_pct = 0.7  (oversight panel retained)
```

Autonomy dials are **modeling parameters** for scenario analysis, not operational deployment instructions.

---

## Sample cabinet_intent envelope

```json
{
  "event_id": "2026-CAB-07",
  "layer": "institution:ai-pm",
  "session_id": "session-42",
  "source_parliament_resolution": "res-2026-19",
  "cabinet_intent": {
    "primary_branch": {
      "action": "sanctions_adjustment",
      "action_likelihood": 0.72,
      "ministry_leads": ["institution:minister-finance", "institution:minister-foreign-affairs"],
      "constraint_set": ["judicial_risk:0.28", "coordination_status:conditional"],
      "epistemic_label": "INSTITUTIONAL_MODEL"
    },
    "secondary_branch": {
      "action": "diplomatic_outreach",
      "action_likelihood": 0.55,
      "ministry_leads": ["institution:minister-foreign-affairs"],
      "constraint_set": [],
      "epistemic_label": "INSTITUTIONAL_MODEL"
    }
  },
  "inter_ministry_tensions": [],
  "charter_status": "PERMITTED",
  "judicial_risk": 0.28,
  "pm_ai_pct": 0.7,
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## Cross-layer integration

| Layer | Cabinet relationship |
|-------|---------------------|
| [AI Parliament](AI_PARLIAMENT.md) | Source of `coalition_consensus`; receives `execution_outcome` accountability reports |
| [AI Ministries](AI_MINISTRIES.md) | Ministers feed `portfolio_posture` into cabinet ensemble; PM coordinates |
| [CHARTER.md](CHARTER.md) | Charter pre-validates cabinet proposals; PROHIBITED halts PM synthesis |
| [judiciary.md](judiciary.md) | Judiciary gate on `cabinet_intent`; `judicial_risk` reshapes action branches |
| [interpol.md](interpol.md) | Transnational Ops gate for cross-border cabinet actions |
| Errorlogy engine | `action_likelihood` feeds μ/α/PNO forecast deltas via [ERRORLOGY.md](../integrations/ERRORLOGY.md) |

---

## Related docs

- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — deliberation, coalition MAS, autonomy dials
- [AI_MINISTRIES.md](AI_MINISTRIES.md) — domain executive agents, minister swarms
- [CHARTER.md](CHARTER.md) — constitutional constraints, human override hook
- [executive.md](executive.md) — abstract executive layer
- [judiciary.md](judiciary.md) — dispute resolution, judicial gate
- [interpol.md](interpol.md) — cross-border coordination
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [OVERVIEW.md](OVERVIEW.md) — institutional map
