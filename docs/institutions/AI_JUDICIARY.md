# AI Judiciary — Institutional Simulator

**Epistemic label:** `INSTITUTIONAL_MODEL` — all outputs from this layer are analytical contributions, never legal verdicts or moral determinations.

## Purpose

The **AI Judiciary** is the procedural constraint layer of the AI-Native Government simulator. It models judicial roles as **protocol-executing agents** — checking whether proposed actions are consistent with the charter, prior constraint records, and due-process requirements — not as moral arbiters.

Key design principle: the AI Judiciary does **not** issue verdicts on guilt or innocence. It outputs **constraint decisions** against a procedural standard.

> For the abstract legitimacy-constraint layer, see [judiciary.md](judiciary.md). This document defines the **literal role-mapping simulator** for AI judicial agents.

---

## Role isomorphism

| Human role | AI agent slot | Layer ID | Scope |
|------------|---------------|----------|-------|
| Presiding judge | AI Presiding Judge | `institution:ai-presiding-judge` | Procedural control, constraint application, output issuance |
| Judicial panel / bench | AI Judicial Panel | `institution:ai-judicial-panel` | Multi-agent review for escalated or high-stakes items |
| Public defender | AI Public Defender Agent | `institution:ai-public-defender` | Analytical counter-argument generation, due-process checks |
| Prosecutor | AI Prosecutor Agent | `institution:ai-prosecutor` | Grounds articulation, evidence package assembly (analytical, not adversarial) |
| Clerk / registrar | AI Court Registrar | `institution:ai-court-registrar` | Docket management, procedural record-keeping |

**Modeling note:** "Adversarial" framing is a structural artifact. The AI Prosecutor agent articulates grounds analytically; it does not pursue a conviction — it constructs a grounds package for procedural evaluation.

---

## Due process as machine protocol

Due process in this layer is a **formal protocol specification**, not a philosophical concept. An action clears due-process requirements when:

1. **Standing verified** — the requesting party has charter-recognized standing to invoke judicial review
2. **Grounds package complete** — structured evidence envelope provided (see NAMM integration below)
3. **Notice requirement met** — affected party/agent has been notified per procedure model
4. **Constraint check complete** — prior constraint records searched; no conflicting precedent unresolved
5. **Proportionality check** — proposed constraint output is proportionate to grounds severity

Failure at any step yields `due_process_status: incomplete` and blocks downstream execution.

```json
{
  "layer": "institution:ai-presiding-judge",
  "due_process_check": {
    "standing_verified": true,
    "grounds_package": "complete",
    "notice_status": "served",
    "constraint_history_clear": true,
    "proportionality_score": 0.82
  },
  "due_process_status": "complete",
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## Constraint outputs

The AI Judiciary issues one of four constraint outputs per reviewed action:

| Output | Meaning | Downstream effect |
|--------|---------|-------------------|
| `approve` | Action consistent with charter and prior constraints | Executive / Transnational Ops may proceed |
| `reject` | Action inconsistent; cannot proceed as submitted | Execution blocked; grounds returned |
| `require-amendment` | Action viable with specified modifications | Execution held; amendment loop opened |
| `escalate-to-human` | Constraint ambiguity or charter gap beyond AI resolution | Human Oversight Panel activated |

**Language note:** outputs are framed as "consistent with charter" or "inconsistent with charter" — never as "guilty" or "innocent."

```json
{
  "review_id": "JUD-2026-0042",
  "reviewed_action": "cross-border-tracking-request",
  "constraint_output": "require-amendment",
  "grounds": "privacy statute conflict (μ=0.71); amendment path: data-minimization clause required",
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## Judicial review of executive and ministerial actions

The AI Judiciary reviews proposed actions from the Executive layer and AI Ministers **before execution** for high-risk items, and **post-hoc** for routine items.

| Review trigger | Mode | Threshold |
|----------------|------|-----------|
| `judicial_risk > 0.6` | Pre-execution review | Automatic gate |
| Cross-border enforcement request | Pre-execution review | Always |
| `escalation_threshold` exceeded on any layer | Pre-execution review | Configured per role |
| Citizen/state appeal filed | Post-hoc appeal review | On filing |
| Periodic audit | Post-hoc audit | Per session cycle |

Executive `action_likelihood` is suppressed until judicial review resolves for pre-execution gated items.

---

## COMPUTATIONAL_EVIDENCE integration (NAMM)

When the Errorlogy engine or [namm-experiments](https://github.com/errorlogy/namm-experiments) produces a verification certificate, it can be attached to the grounds package as `COMPUTATIONAL_EVIDENCE`.

```json
{
  "grounds_package": {
    "type": "COMPUTATIONAL_EVIDENCE",
    "source": "namm-experiments",
    "certificate_id": "NAMM-2026-0117",
    "claim": "analytical contribution: action pattern consistent with precedent cluster ACC-7",
    "fuzzy_membership": { "μ": 0.74, "α": 0.61 },
    "epistemic_label": "COMPUTATIONAL_EVIDENCE"
  }
}
```

**Integration rule:** `COMPUTATIONAL_EVIDENCE` raises grounds-package completeness score but does **not** substitute for procedural due-process steps. A NAMM certificate alone cannot trigger an `approve` output.

---

## Appeals and human oversight activation

Appeals route to the **Human Oversight Panel** (see [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md)) under these conditions:

| Trigger | Escalation path |
|---------|----------------|
| `constraint_output: escalate-to-human` | Automatic routing to Human Oversight Panel |
| Affected party files appeal | Docket entry → Human Oversight Panel |
| `judiciary_ai_pct` dial below override threshold | Human judge reviews AI output before issuance |
| Charter gap detected | Paused; Human Oversight Panel determines charter interpretation |

Human override of any constraint output is always structurally possible — see [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md).

---

## Autonomy dial

| Parameter | Range | Meaning |
|-----------|-------|---------|
| `judiciary_ai_pct` | 0.0–1.0 | Fraction of constraint checks processed without human co-signature |
| `human_cosign_threshold` | 0.0–1.0 | Judicial risk score above which human co-signature is required |
| `panel_required_above` | 0.0–1.0 | Confidence gap above which single-judge output is escalated to panel |
| `appeal_auto_route` | boolean | Whether citizen appeals auto-route to Human Oversight Panel |

**Phased profile (modeled example):**

```text
Phase 0 — Shadow:     judiciary_ai_pct = 0.0, AI produces shadow constraint checks only
Phase 1 — Advise:     judiciary_ai_pct = 0.3, human judge confirms all outputs
Phase 2 — Co-sign:    judiciary_ai_pct = 0.6, human co-sign on risk > threshold
Phase 3 — Autonomous: judiciary_ai_pct = 0.85, human oversight retained for appeals
```

Autonomy dials are modeling parameters for scenario analysis, not operational deployment instructions.

---

## Agent interaction summary

```text
Executive / AI PM
        │ proposed action + judicial_risk
        ▼
AI Court Registrar ──► docket_entry, standing_check
        │
        ▼
AI Prosecutor Agent ──► grounds_package (COMPUTATIONAL_EVIDENCE optional)
AI Public Defender Agent ──► counter-grounds (due-process check)
        │
        ▼
AI Presiding Judge ──► due_process_status, constraint_output
        │
        ├── approve / reject / require-amendment ──► Executive
        └── escalate-to-human ──────────────────────► Human Oversight Panel
```

---

## Epistemic framing

| Use | Never use |
|-----|-----------|
| "consistent with charter" | "guilty" |
| analytical contribution | criminal verdict |
| `constraint_output: reject` | condemnation |
| grounds package (modeled) | proven wrongdoing |
| fuzzy membership μ | definitive legal finding |

---

## Related docs

- [judiciary.md](judiciary.md) — abstract legitimacy-constraint layer
- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — parliament simulator (source of parliamentary review requests)
- [AI_TRANSNATIONAL_OPS.md](AI_TRANSNATIONAL_OPS.md) — cross-border coordination (requires judicial gate)
- [AI_HUMAN_OVERSIGHT.md](AI_HUMAN_OVERSIGHT.md) — human appeal and override layer
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [OVERVIEW.md](OVERVIEW.md) — institutional map
- Integration: [ERRORLOGY.md](../integrations/ERRORLOGY.md)
