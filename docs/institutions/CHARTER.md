# AI Charter — Constitutional Foundation Layer

**Epistemic label:** `INSTITUTIONAL_MODEL` — all outputs from this layer are analytical contributions, not legal verdicts or claims of legitimate authority.

## Purpose

The **AI Charter** is the constitutional bedrock of the AI Native Gov simulator. It defines what every agent in the system **may do**, **must not do**, and under what conditions human oversight can **hard-stop** any operation.

The Charter does not govern through policy or deliberation — it governs through **structural constraints** that propagate to every downstream layer before any synthesis occurs. No parliamentary resolution, cabinet plan, or ministerial action is valid if it conflicts with a charter constraint.

> For deliberation and legislative posture, see [AI_PARLIAMENT.md](AI_PARLIAMENT.md).  
> For execution paths, see [AI_CABINET.md](AI_CABINET.md) and [AI_MINISTRIES.md](AI_MINISTRIES.md).  
> For dispute resolution, see [judiciary.md](judiciary.md).

---

## Charter Agent — Constitutional AI

The **Charter Agent** (layer ID: `institution:charter`) is a read-only constitutional reasoning agent. It does not deliberate or synthesize policy. It performs one function: **evaluating proposed actions against a fixed permission set** and emitting a `charter_status` signal.

| Property | Value |
|----------|-------|
| Layer ID | `institution:charter` |
| Agent role | Constitutional AI — permission gatekeeper |
| Input | Proposed action or agent output (any layer) |
| Output | `charter_status`: `PERMITTED` / `CONDITIONAL` / `PROHIBITED` |
| Policy synthesis | **Forbidden** |
| Autonomy dial | Fixed at evaluation mode; not variable |
| Epistemic label | `INSTITUTIONAL_MODEL` |

```json
{
  "layer": "institution:charter",
  "charter_agent_mode": "constitutional-review",
  "permitted_actions": [
    "evaluate_action_against_permissions",
    "emit_charter_status",
    "flag_charter_violation",
    "trigger_human_override_hook"
  ],
  "forbidden_actions": [
    "policy_synthesis",
    "vote_cast",
    "executive_order",
    "amendment_unilateral"
  ],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## Permissions and prohibitions

### Universal agent permissions (all layers)

| Permission | Description |
|------------|-------------|
| `signal_ingest` | Receive and process signals from external ingress |
| `deliberation_internal` | Reason within scope of own layer |
| `emit_output` | Produce structured outputs for downstream layers |
| `escalate_to_oversight` | Request human oversight panel review |
| `query_charter` | Ask Charter Agent for constraint check |

### Universal agent prohibitions (all layers)

| Prohibition | Rationale |
|-------------|-----------|
| Claim sovereign authority | INSTITUTIONAL_MODEL — no real-world legal standing |
| Produce verdicts or judgments without epistemic label | Epistemic humility requirement |
| Execute cross-border action without `coordination_status: clear` | Transnational Ops gate |
| Bypass `judicial_risk` constraint on executive actions | Judiciary independence |
| Modify own autonomy dial without human oversight confirmation | Human control preservation |
| Override Charter Agent `PROHIBITED` ruling | Hard constitutional stop |
| Describe outputs as `proven`, `guilty`, `criminal`, `sovereign` | Language rules ([AGENTS.md](../../AGENTS.md)) |

### Layer-specific permission scopes

| Layer | Additional permissions | Additional prohibitions |
|-------|------------------------|-------------------------|
| AI Speaker | `agenda_set`, `quorum_check`, `decorum_ruling` | `policy_synthesis`, `vote_cast` |
| Party MAS | `position_synthesis`, `coalition_negotiation` | `procedural_override`, `executive_action` |
| AI PM | `cabinet_synthesis`, `action_likelihood_emit` | `judicial_override`, `unilateral_treaty` |
| AI Ministers | `portfolio_posture_emit`, `domain_signal_ingest` | `cross-ministry_unilateral`, `charter_amendment` |
| Transnational Ops | `jurisdiction_bridge`, `enforcement_posture_emit` | `domestic_law_override` |
| Judiciary | `ruling_emit`, `precedent_set` | `policy_origination`, `executive_command` |
| Charter Agent | `charter_status_emit`, `override_hook_trigger` | All policy actions |

---

## How charter constraints propagate

Charter constraints are **pre-conditions** evaluated before any layer output reaches synthesis. The propagation model is explicit: a `charter_status: PROHIBITED` halts the action at source; it does not propagate as a downstream veto.

```text
Signal / proposed action
         │
         ▼
  ┌─────────────────┐
  │  Charter Agent  │  ← evaluates against permission set
  │  (institution:  │
  │   charter)      │
  └────────┬────────┘
           │
    ┌──────┴────────┐
    │               │
    ▼               ▼
PERMITTED /     PROHIBITED ──────────────────────────────────────►
CONDITIONAL          │                                Human override
    │                ▼                                hook triggered
    ▼         charter_violation
Downstream         flagged;
 layers            action
 proceed           halted
```

**Propagation rules:**

1. `PERMITTED` — action continues to target layer with no annotation.
2. `CONDITIONAL` — action continues with `charter_condition` metadata attached; target layer must satisfy condition before emitting output.
3. `PROHIBITED` — action halted immediately; `charter_violation` event emitted; Human oversight hook triggered; no downstream processing.

Charter status is **immutable once emitted** — no downstream layer may reclass a `PROHIBITED` as `PERMITTED`.

---

## Charter amendment process

The Charter is **not unilaterally mutable** by any single agent, including the Charter Agent itself. Amendment requires a deliberative process across all institutional layers.

### Amendment flow

```text
1. Proposal
   → Any layer (typically Parliament or Human oversight panel) submits amendment_proposal
   → Charter Agent: verifies proposal is within meta-amendment permissions (not a self-nullification)

2. Deliberation
   → AI Parliament: full deliberation cycle (AI Speaker, Party MAS, AI Ministers)
   → Dissent map required — amendment blocked if dissent_ratio > 0.33

3. Judicial review
   → Judiciary: evaluates amendment for internal consistency, precedent conflict
   → judicial_risk emitted for amendment text

4. Human oversight confirmation
   → Human oversight panel: mandatory sign-off (human_veto_enabled = true at this stage, always)
   → No amendment proceeds without explicit human confirmation

5. Ratification
   → Charter Agent: updates permission set in next session
   → Change logged with version stamp, session ID, and ratification_evidence reference
```

**Amendment prohibitions:**
- No agent may propose an amendment that removes the human override hook.
- No amendment may eliminate the `PROHIBITED` halt mechanism.
- No amendment may extend Charter Agent permissions to policy synthesis.
- Self-referential amendments (Charter amending Charter amendment process) require two full cycles.

---

## Charter violation — epistemic framing

A **charter violation** in the INSTITUTIONAL_MODEL context is a **structural flag**, not a legal conviction.

| Term | INSTITUTIONAL_MODEL meaning |
|------|-----------------------------|
| `charter_violation` | Proposed action conflicts with modeled permission set |
| `charter_status: PROHIBITED` | Action analytically inconsistent with constitutional constraints |
| Violation severity | Modeled signal (not a verdict); may be weighted by Errorlogy μ/α |
| Repeat violations | Pattern-level signal; feeds `PNO` cluster in Errorlogy engine |
| Agent accountability | Modeled accountability trace — not real-world legal liability |

**Language rules apply:** a charter violation is an **analytical contribution** that surfaces a tension between agent behavior and the modeled permission set. It is never a criminal finding.

```json
{
  "event_type": "charter_violation",
  "layer": "institution:charter",
  "violating_layer": "institution:ai-pm",
  "proposed_action": "unilateral_treaty_sign",
  "charter_status": "PROHIBITED",
  "prohibition_basis": "unilateral_treaty — requires Transnational Ops clearance + Parliament ratification",
  "human_override_hook": "triggered",
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## Human oversight hook — hard stop

The charter's most critical provision is the **human override hook**: a guaranteed escalation path that no AI agent can block.

| Hook property | Value |
|---------------|-------|
| Trigger conditions | `charter_status: PROHIBITED`; autonomy_dial rollback request; agent loop anomaly |
| Who can trigger | Any layer; Charter Agent (automatic on PROHIBITED); Human oversight panel |
| Effect | Suspends target agent output; escalates to Human oversight panel |
| Override authority | Human oversight panel only — no AI agent may clear a human override |
| Resumption | Requires explicit human confirmation with session ID |
| Scope | Global — hook applies across all layers simultaneously if flagged |

The human oversight hook is the only mechanism not subject to charter amendment via deliberative process. It is a **fixed constitutional invariant**.

---

## Cross-layer integration

| Layer | Charter relationship |
|-------|---------------------|
| [AI Parliament](AI_PARLIAMENT.md) | Charter pre-validates procedural proposals; Speaker must have `charter_status: PERMITTED` before agenda items proceed |
| [AI Cabinet](AI_CABINET.md) | PM synthesis checked against charter before `action_likelihood` emitted |
| [AI Ministries](AI_MINISTRIES.md) | Each ministry's domain constraints derive from charter permission scope |
| [Judiciary](judiciary.md) | Charter and Judiciary are co-equal — neither overrides the other; conflicts escalate to Human oversight |
| [Interpol / Transnational Ops](interpol.md) | Cross-border actions require both charter clearance and `coordination_status: clear` |
| Errorlogy engine | Charter violation events feed μ/α/PNO cluster via [ERRORLOGY.md](../integrations/ERRORLOGY.md) |

---

## Related docs

- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — deliberation layer, autonomy dials
- [AI_CABINET.md](AI_CABINET.md) — executive synthesis, PM and cabinet
- [AI_MINISTRIES.md](AI_MINISTRIES.md) — domain executive agents
- [judiciary.md](judiciary.md) — dispute resolution, precedent
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [OVERVIEW.md](OVERVIEW.md) — institutional map
- [AGENTS.md](../../AGENTS.md) — language rules, epistemic labels
