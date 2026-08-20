# AI Government Overview — Master Map

**Epistemic label:** `INSTITUTIONAL_MODEL` — this document maps the full AI-Native Government simulator topology. All layers are analytical modeling constructs. The simulator does not claim sovereign authority, legal standing, or operational governance capacity.

## What this document is

This is the **single reference document** for the full AI-Native Government simulator: all institutional layers, their relationships, the complete autonomy dial table, gradual replacement phases, and epistemic guarantees.

For implementation detail on each layer, follow the cross-links.

---

## Full layer diagram

```
                    ┌──────────────────────────┐
                    │    CHARTER / LEGAL        │
                    │  (framing constraints,    │
                    │   procedural validity)    │
                    └────────────┬─────────────┘
                                 │ constrains all layers
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
┌──────────────────┐  ┌─────────────────────┐  ┌────────────────────┐
│  HUMAN OVERSIGHT  │  │   AI PARLIAMENT      │  │  TRANSNATIONAL OPS │
│  (structural      │  │  ┌───────────────┐  │  │  (cross-border     │
│   override, veto, │  │  │ AI Speaker    │  │  │   coordination,    │
│   audit, appeal)  │  │  │ Party MAS     │  │  │   audit trail)     │
└────────┬──────────┘  │  │ AI Ministers  │  │  └──────────┬─────────┘
         │             │  │ AI PM         │  │             │
         │             │  └───────────────┘  │             │
         │             │  + Cabinet MAS      │             │
         │             └──────────┬──────────┘             │
         │                        │                        │
         │             ┌──────────┤                        │
         │             │          │                        │
         │      ┌──────┴──┐  ┌────┴────────────────────┐  │
         │      │Ministries│  │   AI CABINET / EXECUTIVE │  │
         │      │(domain)  │  │   (action_likelihood,    │  │
         │      └──────┬───┘  │    executive posture)    │  │
         │             │      └────────────┬─────────────┘  │
         │             └──────────┬────────┘               │
         │                        │                         │
         │                        ▼                         │
         │               ┌─────────────────┐               │
         │               │  AI JUDICIARY    │◄──────────────┘
         │               │  (procedural     │  judicial gate for
         │               │   constraint,    │  all cross-border
         │               │   due process)   │  requests
         │               └────────┬────────┘
         │                        │
         └──────────────────┬─────┘
                            │  escalate-to-human
                            ▼
                   ┌─────────────────┐
                   │    SYNTHESIS    │
                   │ (checks &       │
                   │  balances       │
                   │  output)        │
                   └────────┬────────┘
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
      ┌────────────┐                ┌────────────┐
      │ Errorlogy  │                │ politic.bar│
      └────────────┘                └────────────┘
```

---

## Layer index

| Layer | File | Layer ID | Primary function |
|-------|------|----------|-----------------|
| Charter / Legal | *(stub)* | `institution:charter` | Procedural validity constraints on all layers |
| AI Parliament | [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | `institution:parliament` | Deliberation, legislative posture, role isomorphism |
| AI Speaker | [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | `institution:ai-speaker` | Procedural chair |
| Party Coalition MAS | [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | `institution:party-coalition` | Multi-agent coalition synthesis |
| AI Ministers | [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | `institution:ai-minister` | Domain portfolio posture |
| AI PM | [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | `institution:ai-pm` | Cabinet coordination, executive intent |
| Ministries (domain) | *(stubs planned)* | `institution:ministry-*` | Sector signals: defense, finance, climate, tech |
| AI Cabinet / Executive | [executive.md](executive.md) | `institution:executive` | Action likelihood, policy execution paths |
| AI Judiciary | [AI_JUDICIARY.md](AI_JUDICIARY.md) | `institution:ai-presiding-judge` / `institution:ai-judicial-panel` | Procedural constraint, due process, constraint outputs |
| Transnational Ops | [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) | `institution:transnational-ops` | Cross-border coordination, routing, audit trail |
| Human Oversight | [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) | *(human layer)* | Veto, appeal, audit, dead man's switch |

---

## Event flow: how layers interact

A signal entering the simulator flows through layers in priority order determined by signal type. Below is the canonical full-cascade flow:

```text
1. SIGNAL INGRESS
   └─ Signal tagged by type (bilateral, legal, cross-border, military, economic…)

2. CHARTER CHECK
   └─ Procedural validity: does this signal class have a defined processing path?
   └─ charter_valid: true / false

3. PARLIAMENT
   └─ AI Speaker: agenda slot allocated
   └─ Party MAS: deliberation, position vectors, dissent_map
   └─ AI Ministers: portfolio_posture per relevant domain
   └─ AI PM: cabinet_intent synthesis
   └─ Output: legislative_posture, dissent_map, consensus_score

4. EXECUTIVE
   └─ action_likelihood computed from cabinet_intent + legislative_posture
   └─ judicial_risk flagged for high-risk actions

5. JUDICIARY (pre-execution gate for flagged actions)
   └─ Due process check
   └─ constraint_output: approve / reject / require-amendment / escalate-to-human

6. TRANSNATIONAL OPS (if cross-border)
   └─ Activation conditions checked (charter_permission + parliamentary_resolution)
   └─ Grounds verification
   └─ Judicial gate (routes to Judiciary)
   └─ OPERATIONAL packet issued if cleared

7. HUMAN OVERSIGHT (on escalation or audit trigger)
   └─ Appeal review / veto / dial rollback / audit determination

8. SYNTHESIS
   └─ Checks & balances surface (tensions, blocks, confidence)
   └─ Output → Errorlogy (μ/α/PNO validation) → politic.bar streams
```

---

## Autonomy dial table — all parameters

This is the authoritative consolidated reference. Individual layer docs carry the same parameters for context.

| Layer | Parameter | Range / Type | Default | Human control |
|-------|-----------|-------------|---------|---------------|
| AI Speaker | `autonomy_dial` | 0.0–1.0 | 0.85 | Rollback via Human Oversight |
| AI Speaker | `human_veto_enabled` | boolean | `true` | Human-set |
| Party MAS | `autonomy_dial` (per party) | 0.0–1.0 | 0.7 | Rollback via Human Oversight |
| AI Ministers | `autonomy_dial` (per minister) | 0.0–1.0 | 0.6 | Rollback via Human Oversight |
| AI PM | `escalation_threshold` | 0.0–1.0 | 0.75 | Human-set |
| AI Judiciary | `judiciary_ai_pct` | 0.0–1.0 | 0.6 | Rollback via Human Oversight |
| AI Judiciary | `human_cosign_threshold` | 0.0–1.0 | 0.65 | Human-set |
| AI Judiciary | `panel_required_above` | 0.0–1.0 | 0.8 | Human-set |
| AI Judiciary | `appeal_auto_route` | boolean | `true` | Human-set |
| Transnational Ops | `transnational_ops_ai_pct` | 0.0–1.0 | 0.6 | Rollback via Human Oversight |
| Transnational Ops | `judicial_gate_bypass` | boolean | `false` | **Not configurable** |
| Transnational Ops | `audit_human_review_cycle` | integer | 10 | Human-set |
| Human Oversight | `human_override_always` | boolean | `true` | Human-set only |
| Human Oversight | `audit_cycle_sessions` | integer | 20 | Human-set |
| Human Oversight | `dial_rollback_authority` | `human-only` | fixed | Not configurable |

**Key constraints:**
- `judicial_gate_bypass` is always `false`; cross-border requests always pass through the Judiciary gate
- `human_override_always` and `dial_rollback_authority` cannot be modified by AI agents
- `human_veto_enabled` defaults to `true` on all layers; must be explicitly and intentionally set otherwise by human operators in scenario analysis only

---

## Gradual replacement phases

Phased human→AI transition is parameterized across all roles simultaneously. Phases are modeling scenarios, not deployment plans.

| Phase | Name | Description | Typical dial range |
|-------|------|-------------|-------------------|
| **Phase 0** | Procedural AI only | AI produces shadow outputs; all decisions human-confirmed | 0.0 (all layers) |
| **Phase 1** | Advise | AI outputs visible to human decision-makers; humans act | 0.1–0.3 |
| **Phase 2** | Co-execute | AI executes routine items; human confirms contested or high-risk | 0.4–0.6 |
| **Phase 3** | Autonomous + oversight | AI executes most items; human oversight panel retained for appeals, audits, escalations | 0.7–0.85 |
| **Phase 4** | Full AI cabinet + human appeal | All institutional roles AI-filled; Human Oversight Panel active; any output appealable | 0.85–1.0 |

Phase 4 is the maximum modeled autonomy level. `human_override_always: true` and `human_veto_enabled: true` are **always active** regardless of phase.

---

## Epistemic guarantees

### What the simulator can provide

| Guarantee | Description |
|-----------|-------------|
| Structural consistency | Layer interactions follow defined topology; no layer can unilaterally bypass another |
| Traceability | Every output carries provenance: layer ID, input signals, dial state, epistemic label |
| Constraint surfacing | Judicial and charter constraints are explicit and logged |
| Dissent representation | Opposition positions are structurally required (not suppressed) |
| Human override path | Every AI output has a defined human override route |
| Audit trail | Append-only records for all institutional outputs |

### What the simulator cannot provide

| Limitation | Description |
|-----------|-------------|
| Real-world authority | Simulator outputs have no legal standing outside this model |
| Verdict on guilt/innocence | No layer issues moral or legal guilt determinations |
| Prediction of actual government behavior | Outputs are analytical contributions, not forecasts |
| Replacement for human judgment | Simulator supports structured reasoning; human judgment is preserved via oversight |
| Verification of real-world agent identity | Actor IDs are modeled; real-world identity requires external verification |

---

## Cross-repo integration summary

| Repo | Role |
|------|------|
| [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) | μ/α/PNO/FPD engine validates institutional outputs; fuzzy membership scores |
| [errorlogy/politic-bar](https://github.com/errorlogy/politic-bar) | Error cards, politifi streams; surfaces institutional tensions as signals |
| [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) | Verification certificates (`COMPUTATIONAL_EVIDENCE`) attached to grounds packages |

Integration contracts: [ERRORLOGY.md](../integrations/ERRORLOGY.md), [POLITIC_BAR.md](../integrations/POLITIC_BAR.md).

---

## All institution docs

| Document | Status | Description |
|----------|--------|-------------|
| [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | Active | Speaker, parties, ministers, PM, autonomy dials |
| [AI_JUDICIARY.md](AI_JUDICIARY.md) | Active | Procedural constraint layer, due process, NAMM integration |
| [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) | Active | Cross-border coordination, routing, audit trail |
| [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) | Active | Veto, appeal, audit, dead man's switch |
| [GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md) | Active | Three-tier world model (national → regional → global) |
| [EU_SCHEMA.md](EU_SCHEMA.md) | Active | EU two-tier mermaid schema (structure, flow, rings) |
| [EU_TOPOLOGY.md](EU_TOPOLOGY.md) | Active | EU supranational layer vs 27 national instances |
| [EU_STATES.md](EU_STATES.md) | Active | Member-state profiles and tension cases |
| [parliament.md](parliament.md) | Active | Abstract deliberation layer |
| [executive.md](executive.md) | Active | Policy execution modeling |
| [judiciary.md](judiciary.md) | Active | Abstract legitimacy-constraint layer |
| [interpol.md](interpol.md) | Active | Abstract cross-border coordination layer |
| [OVERVIEW.md](OVERVIEW.md) | Active | Institutional map (short reference) |
| [TOPOLOGY.md](TOPOLOGY.md) | Active | Layer intersection matrix |
| AI_CABINET.md | Planned | Cabinet MAS detail |
| AI_MINISTRIES.md | Planned | Domain ministry stubs (defense, finance, climate, tech) |

---

## Related docs

- [GLOBAL_AI_GOVERNANCE.md](GLOBAL_AI_GOVERNANCE.md) — three-tier world model (national → regional bloc → global)
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersection matrix
- [OVERVIEW.md](OVERVIEW.md) — short institutional map
- [EU_SCHEMA.md](EU_SCHEMA.md) — EU two-tier mermaid schema
- [EU_TOPOLOGY.md](EU_TOPOLOGY.md) — EU multi-level topology
- [EU_STATES.md](EU_STATES.md) — 27 national instances
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — system architecture
- [VISION.md](../../VISION.md) — epistemic humility, non-sovereignty
- [AGENTS.md](../../AGENTS.md) — language rules, routing, epistemic labels
- [docs/examples/trump-macron-cascade.md](../examples/trump-macron-cascade.md) — full cross-layer cascade example
