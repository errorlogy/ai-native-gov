# AI Transnational Ops — Cross-Border Coordination Layer

**Epistemic label:** `INSTITUTIONAL_MODEL` — all outputs from this layer are analytical contributions representing modeled coordination posture, not operational enforcement actions or legal orders.

## Purpose

The **AI Transnational Ops** layer normalizes cross-jurisdictional requests, routes them through procedural gates, and maintains a full audit trail. It is the Interpol-analog within the AI-Native Government simulator.

**What it is not:**

- Not a parliament — it does not deliberate policy or synthesize legislative posture
- Not a ministry — it does not hold a domain portfolio or advise the PM
- Not a judiciary — it does not issue constraint decisions or review charter compliance

It is a **procedural coordination layer**: a routing, normalization, and audit mechanism for cross-border actions that have already cleared (or are seeking clearance from) other layers.

> For the abstract cross-border coordination layer, see [interpol.md](interpol.md). This document defines the **literal role-mapping simulator** for AI Transnational Ops agents.

---

## Role isomorphism

| Human role | AI agent slot | Layer ID | Scope |
|------------|---------------|----------|-------|
| Liaison / coordination officer | Identity Normalization Agent | `institution:transnational-identity` | Normalize actor IDs across jurisdictions |
| Case routing officer | Request Router | `institution:transnational-router` | Route requests per treaty framework and procedure |
| Audit / registrar | Audit Trail Keeper | `institution:transnational-audit` | Immutable log of all cross-border requests and outcomes |
| Legal grounds reviewer | Grounds Verifier | `institution:transnational-grounds` | Verify legal basis before judicial gate submission |
| MFA liaison | Foreign Affairs Interface | `institution:transnational-mfa` | Bridge to Ministry of Foreign Affairs; treaty posture |

---

## Activation conditions

A cross-border request may enter the Transnational Ops layer **only when**:

1. **Charter permission** — the requesting jurisdiction's charter permits the type of cross-border action requested
2. **Parliamentary resolution** — a parliamentary resolution (or its equivalent) in the relevant jurisdiction has authorized this class of action (modeled via [AI_PARLIAMENT.md](AI_PARLIAMENT.md))
3. **Grounds package present** — a preliminary grounds package exists (further verified by Grounds Verifier agent)
4. **Receiving jurisdiction consent signal** — at least a `consent_signal: conditional` from receiving jurisdiction's MFA interface

Failure on any condition: request returned to originating layer with `coordination_status: blocked`.

---

## Request lifecycle

```text
1. INGRESS
   └─ Cross-border request received
   └─ Identity Normalization Agent: actor IDs resolved across jurisdictions
   └─ Audit Trail Keeper: request_id assigned, ingress logged

2. GROUNDS CHECK
   └─ Grounds Verifier: preliminary legal basis review
   └─ charter_permission: verified / missing
   └─ parliamentary_resolution: present / absent
   └─ Outcome: proceed to judicial gate OR return blocked

3. JUDICIAL GATE
   └─ Request forwarded to AI Judiciary (see AI_JUDICIARY.md)
   └─ Await constraint_output: approve / reject / require-amendment / escalate-to-human
   └─ Audit Trail Keeper: judicial_gate_result logged

4. ROUTING
   └─ Request Router: apply treaty framework mapping
   └─ jurisdiction_map: originating ↔ receiving jurisdiction(s)
   └─ Foreign Affairs Interface: MFA alignment check
   └─ coordination_status: clear / conditional / blocked

5. EXECUTION
   └─ coordination_status: clear → OPERATIONAL packet issued
   └─ OPERATIONAL packet: structured request envelope (not a verdict)
   └─ Receiving jurisdiction agent notified

6. AUDIT
   └─ Audit Trail Keeper: full lifecycle record finalized
   └─ coordination_outcome logged
   └─ Available for periodic human audit (see AI_HUMAN_OVERSIGHT.md)
```

---

## OPERATIONAL packet structure

A cross-border action that clears all gates results in an `OPERATIONAL` packet — a **procedural routing envelope**, not a verdict.

```json
{
  "packet_id": "TOP-2026-0031",
  "type": "OPERATIONAL",
  "request_class": "cross-border-coordination",
  "originating_jurisdiction": "State-A",
  "receiving_jurisdiction": "State-B",
  "judicial_gate_result": "approve",
  "coordination_status": "clear",
  "grounds_basis": "treaty-framework-XY, parliamentary-resolution-2026-04",
  "mfa_consent": "conditional",
  "audit_ref": "AUDIT-TOP-2026-0031",
  "epistemic_label": "INSTITUTIONAL_MODEL",
  "note": "This packet is a modeled procedural envelope. It does not constitute a legal order or enforcement action."
}
```

---

## AI "search/apprehension" requests

When a modeled request involves locating or apprehending a person or entity across borders:

- Output is **always** an OPERATIONAL packet — procedural routing only
- The Transnational Ops layer does **not** determine culpability (`INSTITUTIONAL_MODEL`, not verdict)
- Grounds Verifier confirms the judicial gate result before routing
- `COMPUTATIONAL_EVIDENCE` from NAMM may be attached to grounds package but does not bypass the judicial gate

**Language rule:** these requests are "cross-border coordination requests consistent with grounds package" — never "arrest orders" or statements of guilt.

---

## Inter-jurisdiction disagreements

When receiving jurisdiction's MFA Interface returns `consent_signal: rejected` or `contested`:

| Disagreement level | Escalation path |
|-------------------|----------------|
| Procedural dispute (treaty interpretation) | Grounds Verifier → AI Judiciary for inter-jurisdictional constraint review |
| Political / diplomatic dispute | Foreign Affairs Interface → AI Minister (Foreign Affairs portfolio) → AI PM |
| Charter conflict between jurisdictions | `escalate-to-human` → Human Oversight Panel |
| Unresolvable | `coordination_status: blocked`; full audit record preserved |

---

## Ministry of Foreign Affairs interface

The `transnational-mfa` slot connects Transnational Ops to the Ministry of Foreign Affairs layer:

| Direction | Signal |
|-----------|--------|
| MFA → Transnational Ops | Treaty posture, bilateral agreement status, diplomatic risk |
| Transnational Ops → MFA | Active cross-border requests, consent requirements, escalation flags |

MFA input does not override the judicial gate — it informs routing and can raise `coordination_status` to `conditional` pending diplomatic alignment.

---

## Autonomy dial

| Parameter | Range | Meaning |
|-----------|-------|---------|
| `transnational_ops_ai_pct` | 0.0–1.0 | Fraction of routing and normalization processed without human co-review |
| `judicial_gate_bypass` | boolean | Must be `false`; judicial gate is not bypassable by design |
| `audit_human_review_cycle` | integer (sessions) | How often a human reviews the audit trail |
| `mfa_auto_consent_threshold` | 0.0–1.0 | MFA consent signal strength above which routing proceeds without human MFA diplomat confirmation |

**Phased profile (modeled example):**

```text
Phase 0 — Shadow:     transnational_ops_ai_pct = 0.0, AI logs and models only
Phase 1 — Advise:     transnational_ops_ai_pct = 0.3, human officer confirms routing
Phase 2 — Co-route:   transnational_ops_ai_pct = 0.6, human confirms inter-jurisdiction escalations
Phase 3 — Autonomous: transnational_ops_ai_pct = 0.85, human audit cycle retained
```

Autonomy dials are modeling parameters for scenario analysis, not operational deployment instructions.

---

## Intersection summary

| Layer | Relationship |
|-------|-------------|
| [AI_PARLIAMENT.md](AI_PARLIAMENT.md) | Source of parliamentary resolutions authorizing request classes |
| [AI_JUDICIARY.md](AI_JUDICIARY.md) | Mandatory judicial gate before routing; receives constraint_output |
| [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) | Charter conflicts and unresolvable disagreements escalate here |
| [executive.md](executive.md) | Executive cross-border action proposals enter via this layer |
| [interpol.md](interpol.md) | Abstract coordination layer; this doc is the simulator-specific isomorphism |
| Ministry of Foreign Affairs | MFA interface for treaty posture and diplomatic consent |

---

## Related docs

- [interpol.md](interpol.md) — abstract cross-border coordination layer
- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — parliamentary authorization source
- [AI_JUDICIARY.md](AI_JUDICIARY.md) — judicial gate
- [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) — charter escalation and human veto
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [OVERVIEW.md](OVERVIEW.md) — institutional map
