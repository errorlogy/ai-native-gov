# AI Human Oversight — Structural Override Layer

**Epistemic label:** `INSTITUTIONAL_MODEL` — this document models the structural design of human oversight within the AI-Native Government simulator. It is not a claim of real-world authority.

## Purpose

The **Human Oversight layer** is the hard-stop, appeal, and audit mechanism of the AI-Native Government simulator. It is **not a ministry, a parliament, or a judicial body**. It is a structural override: the architectural guarantee that no AI institutional output is irreversible without human review.

Core properties:

- **Always structurally present** — the Human Oversight layer cannot be removed or suspended by any AI agent or any combination of AI agents
- **Veto power** — can override any output from any other layer
- **Dead man's switch design** — AI agents have no mechanism to disable, reconfigure, or route around this layer
- **Appeal surface** — citizens, states, and other institutional layers can invoke human review

---

## What it is not

| Not | Why |
|-----|-----|
| A ministry | Does not hold a policy portfolio or advise the PM |
| A parliament | Does not deliberate or synthesize legislative posture |
| A judiciary | Does not issue constraint decisions; it overrides them |
| An AI agent | Human Oversight Panel consists of human reviewers |

---

## Activation conditions

Human Oversight activates automatically when **any** of the following occurs:

| Trigger | Source layer | Mechanism |
|---------|-------------|-----------|
| Charter violation detected | Any layer | Propagates `charter_violation: true` flag |
| `constraint_output: escalate-to-human` | AI Judiciary | Direct escalation routing |
| `coordination_status: blocked` (charter conflict) | Transnational Ops | Escalation routing |
| `autonomy_dial` threshold exceeded | Any layer | Configured per role; see dial table |
| `human_veto_enabled: true` + contested output | Any layer | Human reviewer invoked |
| Citizen or state appeal filed | External | Appeal intake → review queue |
| Periodic audit cycle reached | All layers | Session-count trigger |
| AI agent attempts to modify oversight configuration | Meta-level | Immediate lock + alert |

---

## Appeal process

Any citizen or state actor (within the model's jurisdiction scope) may file an appeal against any AI institutional output:

```text
1. APPEAL FILED
   └─ Appeal intake: structured appeal envelope received
   └─ `appeal_id` assigned, timestamp logged

2. STANDING CHECK
   └─ Human Oversight Panel verifies standing (charter-recognized appellant)

3. REVIEW QUEUE
   └─ Appeal joined to review queue; priority weighting per urgency flags

4. HUMAN PANEL REVIEW
   └─ Panel reviews AI decision log, grounds package, constraint history
   └─ Panel may request additional Errorlogy engine output or NAMM certificate

5. DETERMINATION
   └─ uphold: AI output stands
   └─ overturn: AI output nullified; human determination issued
   └─ remand: returned to originating layer with panel guidance
   └─ refer: referred to external human institution (real-world court, legislature, etc.)

6. AUDIT LOG
   └─ Appeal outcome recorded in permanent audit trail
```

---

## Audit: periodic review of AI decision logs

At each configured audit cycle, the Human Oversight Panel reviews:

- All `constraint_output` records from AI Judiciary
- All `coordination_status: clear` OPERATIONAL packets from Transnational Ops
- All `action_likelihood` executions from the Executive layer
- Any `escalation_threshold` breach records from any layer
- Autonomy dial settings versus configured policy

Audit outputs:

| Output | Effect |
|--------|--------|
| `audit_clear` | No intervention; cycle recorded |
| `audit_finding` | Specific AI output flagged for review |
| `dial_rollback` | Autonomy dial reduced on one or more layers |
| `layer_suspend` | Layer output halted pending review |
| `charter_review` | Charter interpretation question referred to human constitutional body |

---

## Veto power

The Human Oversight Panel may veto **any** AI institutional output at any time:

```json
{
  "veto_id": "HO-VETO-2026-0007",
  "target_output": "JUD-2026-0042",
  "target_layer": "institution:ai-presiding-judge",
  "veto_type": "overturn",
  "human_determination": "constraint_output overridden; action approved with amended conditions",
  "rationale": "Charter interpretation gap identified; AI output exceeded procedural mandate",
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

Veto records are immutable in the audit trail.

---

## Dead man's switch design

The AI system cannot disable or circumvent human oversight. This is enforced structurally:

| Design constraint | Mechanism |
|-------------------|-----------|
| No AI agent holds `human_override_always` write permission | Parameter is human-set at initialization |
| Autonomy dial `human_veto_enabled` cannot be set to `false` by any AI agent | Write-locked to human operators |
| Human Oversight Panel activation routes are hardcoded in the layer graph | Not configurable by AI agents |
| Any attempt by an AI agent to modify oversight configuration triggers immediate lock | Meta-level monitoring |
| Audit trail is append-only; no AI agent has delete permission | Storage-level constraint |

```json
{
  "human_override_always": true,
  "ai_write_permission_on_oversight_config": false,
  "oversight_routing_hardcoded": true,
  "audit_trail_append_only": true
}
```

---

## Autonomy dial

| Parameter | Range / Type | Meaning |
|-----------|-------------|---------|
| `human_override_always` | `true` / `false` | If `true`, every AI output requires human co-sign. Cannot be set to `false` by AI agents. |
| `human_veto_enabled` | boolean (per layer) | Whether human veto is active for a given layer. Default: `true` for all layers. |
| `audit_cycle_sessions` | integer | Number of sessions between mandatory audit reviews |
| `appeal_queue_max_wait` | integer (sessions) | Maximum sessions before appeal escalates to urgent review |
| `dial_rollback_authority` | `human-only` | Only human operators may reduce autonomy dials after rollback |

**Design rule:** `human_override_always: false` is only permitted in scenario analysis with explicit model labeling. It is never a deployment recommendation.

---

## Relationship to autonomy dials across layers

Human Oversight is the control surface for all autonomy dials defined in other layers:

| Layer | Dial | Human Oversight control |
|-------|------|------------------------|
| AI Parliament (Speaker) | `autonomy_dial` per role | Rollback authority |
| AI Judiciary | `judiciary_ai_pct` | Rollback + co-sign threshold setting |
| Transnational Ops | `transnational_ops_ai_pct` | Rollback + audit cycle setting |
| Executive | `action_likelihood` confidence gates | Threshold review |
| All layers | `escalation_threshold` | Override threshold setting |

---

## Epistemic framing

The Human Oversight layer does not produce `INSTITUTIONAL_MODEL` analytical outputs in the same way other layers do — its determinations are **human decisions**, which carry a different epistemic status within the simulator:

| Label | When used |
|-------|----------|
| `HUMAN_DETERMINATION` | Output from a human panel review or veto |
| `INSTITUTIONAL_MODEL` | This document's framing of the oversight design itself |
| `COMPUTATIONAL_EVIDENCE` | Never applied to Human Oversight outputs (those are human, not computational) |

---

## Related docs

- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — autonomy dials per parliamentary role
- [AI_JUDICIARY.md](AI_JUDICIARY.md) — judicial escalation to human oversight
- [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) — charter conflict escalation
- [AI_GOVERNMENT_OVERVIEW.md](AI_GOVERNMENT_OVERVIEW.md) — master map with full autonomy dial table
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [OVERVIEW.md](OVERVIEW.md) — institutional map
