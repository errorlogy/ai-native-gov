# AI Parliament — Institutional Simulator

**Epistemic label:** `INSTITUTIONAL_MODEL` — all outputs from this layer are analytical contributions, not legal verdicts or claims of legitimate authority.

## Purpose

The **AI Parliament** is a bold institutional simulator where real government roles are mapped **literally** to AI agents — not merely as an abstract deliberation layer, but as a one-to-one isomorphism between human institutional positions and modeled agent slots.

This layer enables:

- **Role isomorphism** — each human office (Speaker, party whip, minister, PM) has a corresponding AI agent with defined scope
- **Gradual replacement** — autonomy dials per role allow human→AI transition without abrupt handover (UAE-style phased AI-in-government management)
- **Checks & balances** — Charter/Legal, Parliament, Judiciary, Transnational Ops, Ministries, and Human oversight constrain each other
- **Reproducible cascades** — cross-border requests traceable through the full institutional graph

The simulator does **not** claim sovereign authority. It provides structured reasoning scaffolding for agents analyzing geopolitical signals.

> For the abstract deliberation layer (consensus, dissent, legislative posture), see [parliament.md](parliament.md). This document defines the **literal role-mapping simulator** built on top of that foundation.

---

## Role isomorphism

Each real-world government role maps to a modeled AI agent slot. The mapping is **structural**, not predictive of actual personnel or AI deployment.

| Human role | AI agent slot | Layer ID | Scope |
|------------|---------------|----------|-------|
| Speaker / procedural chair | AI Speaker | `institution:ai-speaker` | Agenda control, time allocation, procedural rulings only |
| Party / faction | AI Party agent | `institution:party-coalition` | Position synthesis within coalition MAS |
| Coalition bloc | Party Coalition MAS | `institution:party-coalition` | Multi-agent negotiation, whip coordination |
| Minister (domain) | AI Minister | `institution:ai-minister` | Domain briefs, portfolio execution posture |
| Prime Minister / head of government | AI PM | `institution:ai-pm` | Cabinet coordination, executive intent synthesis |
| Cross-border coordination body | Transnational Ops | `institution:transnational-ops` | Jurisdiction bridges, enforcement posture (Interpol-analog) |
| Constitutional / charter authority | Charter/Legal layer | *(doc-only stub)* | Framing constraints, procedural validity |
| Human oversight panel | Human oversight | *(doc-only stub)* | Veto, review, autonomy dial control |

**Modeling note:** Isomorphism means the agent graph mirrors institutional topology — not that AI replaces humans in reality.

---

## AI Speaker models

The Speaker agent controls **procedure only**. Substantive policy reasoning belongs to party and minister agents.

| Mode | Description | Autonomy typical range |
|------|-------------|------------------------|
| **Procedural-only** | Strict chair: agenda, speaking order, quorum checks. No policy synthesis. | 0.7–1.0 AI |
| **Rotating** | Speaker role cycles among party agents per session phase; procedural rules fixed. | 0.3–0.7 AI (human handoff per rotation) |
| **Hybrid** | AI handles routine procedure; human confirms contested rulings. | 0.4–0.6 AI |

```json
{
  "layer": "institution:ai-speaker",
  "speaker_mode": "procedural-only",
  "autonomy_dial": 0.85,
  "permitted_actions": ["agenda_set", "time_allocate", "quorum_check", "decorum_ruling"],
  "forbidden_actions": ["policy_synthesis", "vote_cast", "executive_order"],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## AI parties as coalition MAS

Party agents form a **Multi-Agent System (MAS)** within the Parliament layer. Each party agent:

- Ingests signals tagged to its constituency / bloc
- Synthesizes a **position vector** (not a verdict)
- Negotiates via coalition edges to produce `dissent_map` and `consensus_score`

| MAS component | Function |
|---------------|----------|
| Party agent | Local position synthesis |
| Whip agent (sub-slot) | Coalition discipline modeling |
| Coalition graph | Edge-weighted agreement zones |
| Opposition slot | Explicit minority position (required for dissent tracking) |

Outputs feed [parliament.md](parliament.md) deliberation record and downstream [executive.md](executive.md).

Cross-repo: coalition position vectors may be validated via [Errorlogy engine](https://github.com/errorlogy/errorlogy) (μ/α/PNO); narratives surface on [politic.bar](https://github.com/errorlogy/politic-bar).

---

## AI ministers, PM, and cabinet

Executive-facing roles sit at the Parliament→Executive boundary:

| Agent | Inputs | Outputs |
|-------|--------|---------|
| **AI Minister** | Domain signals, ministry briefs, parliamentary posture | `portfolio_posture`, `implementation_capacity` |
| **AI PM** | Minister outputs, coalition consensus, judicial risk | `cabinet_intent`, `action_likelihood` (feeds Executive) |
| **Cabinet MAS** | Parallel minister agents + PM coordinator | Synthesized executive posture |

The PM agent does **not** override Judiciary or Transnational Ops clearance gates (see Checks & balances).

---

## Transnational Ops layer

Transnational Ops is modeled as a **separate layer** from Parliament — not a subcommittee of deliberation.

| Aspect | Parliament | Transnational Ops |
|--------|------------|-------------------|
| Primary function | Deliberation, legislative posture | Cross-border coordination, enforcement posture |
| Layer ID | `institution:parliament` | `institution:transnational-ops` |
| Analog | National assembly, EU Parliament | Interpol-analog, NATO/EU coordination (see [interpol.md](interpol.md)) |
| Trigger | Domestic signals, treaty debate | Cross-border action proposals, extradition, multilateral enforcement |

Transnational Ops agents require **coordination clearance** before executive cross-border actions proceed. See [TOPOLOGY.md](TOPOLOGY.md) intersection matrix.

---

## Autonomy dial parameters

Gradual human→AI replacement is parameterized per role. Inspired by phased AI-in-government management (e.g. UAE-style gradual deployment), not as endorsement of any specific national program.

| Parameter | Range | Meaning |
|-----------|-------|---------|
| `autonomy_dial` | 0.0–1.0 | 0 = human-only; 1 = full AI procedural control |
| `human_veto_enabled` | boolean | Human oversight can block agent output |
| `escalation_threshold` | 0.0–1.0 | Above this confidence, human review required |
| `rollback_generation` | integer | Session ID at which dial was last reduced |

**Typical phased profile (modeled example):**

```text
Phase 0 — Observe:     autonomy_dial = 0.0, agent produces shadow outputs only
Phase 1 — Advise:      autonomy_dial = 0.2, human confirms all actions
Phase 2 — Execute:     autonomy_dial = 0.5, human veto on contested items
Phase 3 — Autonomous:  autonomy_dial = 0.8+, human oversight panel retained
```

Autonomy dials are **modeling parameters** for scenario analysis, not operational deployment instructions.

---

## Checks & balances flow

```text
                    ┌─────────────────┐
                    │ Charter / Legal │  ← framing, procedural validity
                    └────────┬────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
    ▼                        ▼                        ▼
┌─────────┐           ┌─────────────┐          ┌──────────────┐
│ AI      │           │ AI Parties  │          │ Human        │
│ Speaker │◄─────────►│ (coalition  │          │ oversight    │
│         │           │  MAS)       │          │ (veto dial)  │
└────┬────┘           └──────┬──────┘          └──────┬───────┘
     │                       │                        │
     └───────────┬───────────┘                        │
                 ▼                                    │
          ┌─────────────┐                             │
          │ AI Ministers│◄────────────────────────────┘
          │ + AI PM     │
          └──────┬──────┘
                 │
     ┌───────────┼───────────┐
     ▼           ▼           ▼
┌─────────┐ ┌─────────┐ ┌──────────────────┐
│Executive│ │Judiciary│ │ Transnational Ops│
│ layer   │ │ layer   │ │ (separate)       │
└────┬────┘ └────┬────┘ └────────┬─────────┘
     │           │               │
     └───────────┴───────┬───────┘
                         ▼
                  ┌─────────────┐
                  │  Synthesis  │ → Errorlogy, politic.bar
                  └─────────────┘
```

| Check | Mechanism |
|-------|-----------|
| Speaker vs Parties | Speaker cannot synthesize policy; parties cannot override procedure |
| Parliament vs Executive | `dissent_ratio` caps PM `action_likelihood` confidence |
| Executive vs Judiciary | `judicial_risk` blocks or reshapes cabinet intent |
| Transnational Ops vs Executive | Cross-border actions require `coordination_status: clear` |
| Human oversight vs all | Veto and autonomy dial rollback on any layer |
| Charter/Legal vs all | Procedural invalidity flags propagate to Synthesis |

---

## Epistemic labels and language rules

All AI Parliament outputs carry explicit epistemic metadata.

| Label | When to use |
|-------|-------------|
| `INSTITUTIONAL_MODEL` | Default for all simulator outputs |
| `COMPUTATIONAL_EVIDENCE` | When backed by Errorlogy engine run or NAMM certificate |
| `HYPOTHESIS` | Unconfirmed mandate gaps, speculative coalition positions |

**Language rules** (shared with [AGENTS.md](../../AGENTS.md)):

| Use | Never use |
|-----|-----------|
| analytical contribution | guilty, criminal |
| fuzzy membership μ | proven guilt |
| legitimacy **signals** (modeled) | legitimate ruler (verdict) |
| institutional framing | sovereign AI government |
| possible / consistent with | "this proves" |

---

## Example cascade: cross-border tracking request

**Scenario type:** modeled cross-border law-enforcement coordination request  
**Epistemic label:** `INSTITUTIONAL_MODEL` — design scenario, not operational guidance.

### Flow

```text
1. Signal ingress
   → Cross-border tracking request enters (jurisdiction: State A → State B)

2. AI Parliament
   → AI Speaker: agenda item registered, procedural slot allocated
   → AI Party agents: deliberation on privacy vs cooperation framing
   → Output: legislative_posture (cooperation-conditional), dissent_map

3. AI Minister (Interior / Justice portfolio)
   → portfolio_posture: conditional cooperation pending judicial review
   → Feeds AI PM cabinet synthesis

4. AI PM → Executive layer
   → action_likelihood: request forwarding (0.6), denial branch (0.3)

5. Transnational Ops (separate layer)
   → jurisdiction_map: State A ↔ State B, treaty framework check
   → coordination_status: conditional (awaiting judiciary)

6. Judiciary layer
   → judicial_risk: privacy statute conflict (0.7)
   → constraint_set: blocks automatic forwarding

7. Synthesis
   → Institutional tension: parliament cooperation posture vs judicial block
   → Feed to Errorlogy (ACC cluster) → politic.bar stream
   → Optional: NAMM certificate link on constraint_set derivation
```

### Sample envelope

```json
{
  "event_id": "2026-XB-TRACK-01",
  "activated_layers": [
    "institution:ai-speaker",
    "institution:party-coalition",
    "institution:ai-minister",
    "institution:ai-pm",
    "institution:transnational-ops",
    "institution:judiciary"
  ],
  "topology_tensions": [
    "parliament-executive: cooperation posture vs low executive confidence",
    "executive-judiciary: forwarding blocked by privacy constraint",
    "transnational-ops-judiciary: jurisdiction clearance pending ruling"
  ],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

For a bilateral summit cascade with similar topology annotations, see [trump-macron-cascade.md](../examples/trump-macron-cascade.md).

---

## Cross-repo integration

| Repo | Role in AI Parliament simulator |
|------|----------------------------------|
| [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) | μ/α/PNO/FPD engine validates coalition positions and forecast deltas |
| [errorlogy/politic-bar](https://github.com/errorlogy/politic-bar) | Error cards, politifi streams, signal/noise ingest |
| [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) | Optional verification certificates on institutional outputs |

Integration contracts: [ERRORLOGY.md](../integrations/ERRORLOGY.md), [POLITIC_BAR.md](../integrations/POLITIC_BAR.md).

---

## Related docs

- [parliament.md](parliament.md) — abstract deliberation layer
- [executive.md](executive.md) — policy execution modeling
- [judiciary.md](judiciary.md) — dispute resolution, constraints
- [interpol.md](interpol.md) — cross-border coordination (Transnational Ops analog)
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [OVERVIEW.md](OVERVIEW.md) — institutional map
