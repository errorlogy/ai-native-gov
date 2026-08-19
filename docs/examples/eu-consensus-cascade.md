# Example: EU Council AI Regulation Consensus Cascade

**Scenario type:** 27-state multi-agent deliberation → qualified majority vote  
**Purpose:** End-to-end walkthrough through the EU AI government simulator → Errorlogy engine → NAMM analysis  
**Epistemic label:** `INSTITUTIONAL_MODEL` throughout unless marked otherwise

> **Design scenario only** — not a published error card. Real cards require curated primary-source bundles and full pipeline gates.

See theoretical framing: [`../integrations/NAMM_EU_THEORY.md`](../integrations/NAMM_EU_THEORY.md)

---

## 0. Scenario Setup

**Event:** EU Council vote on a proposed AI Regulation Directive requiring mandatory human oversight for high-stakes AI systems deployed in public administration across all member states.

**Institutional context:**

```text
Activated layers:
  eu_simulator:parliament (×27 national AI parliaments)
  eu_simulator:council (EU Council aggregation)
  eu_simulator:judiciary (CJEU framing constraint)
  eu_simulator:transnational_ops (cross-state coordination audit)
  institution:charter (procedural validity — QMV threshold check)

Topology tensions watched:
  parliament ↔ council (mandate gap — do national positions reflect parliamentary deliberation?)
  judiciary ↔ council (CJEU pre-ruling compatibility check)
  transnational_ops ↔ parliament (cross-state spillover if regulation is asymmetrically burdensome)
```

**Voting rule active:** Qualified Majority Voting (QMV) — 55% of member states (≥15) representing ≥65% of EU population

---

## Step 1 — National AI Parliaments Deliberate

Each of 27 national AI parliaments deliberates on the directive, producing a **position vector**. Three representative preference clusters emerge:

### Cluster A — "Regulatory Vanguard" (7 states, ~22% population)
Nordic + Benelux bloc. Favor strong oversight provisions, want to extend mandatory human review beyond the directive's scope.

```text
μ signal (INSTITUTIONAL_MODEL):
  μ_assent: 0.85 (high — directive is below their preferred stringency)
  α_error: low (directive is in direction of their preference, but undershoots)
  Position: Support with amendment proposals
```

### Cluster B — "Pragmatic Adopters" (12 states, ~38% population)
Mixed central and western EU. Accept directive as broadly appropriate; low variance on implementation.

```text
μ signal (INSTITUTIONAL_MODEL):
  μ_assent: 0.72 (moderate-high — directive is close to their preference centroid)
  α_error: low-moderate
  Position: Support as-is or with minor adjustments
```

### Cluster C — "Sovereignty Defenders" (8 states, ~40% population)
Eastern bloc + some southern states. Oppose mandatory provisions as encroachments on national AI deployment autonomy.

```text
μ signal (INSTITUTIONAL_MODEL):
  μ_assent: 0.28 (low — directive conflicts with national sovereignty framing)
  α_error: high (outcome far from national preference optimum)
  Position: Oppose or seek major carve-outs
```

**Preference heterogeneity observation:**  
Cluster A and Cluster C hold preference orderings over the directive's scope that are mutually intransitive on the sovereignty dimension — a structural condition for Condorcet cycling if additional policy alternatives are introduced (see [`../integrations/NAMM_EU_THEORY.md`](../integrations/NAMM_EU_THEORY.md), Section A.2).

---

## Step 2 — National Positions Emerge

Each national AI parliament produces a formal position via its AI Cabinet and AI PM layer:

| State cluster | Formal position | Negotiation anchor |
|--------------|----------------|-------------------|
| Cluster A (7) | "Support — propose Article 7 extension" | High stringency |
| Cluster B (12) | "Support with technical amendment on SME carve-out" | Centrist |
| Cluster C (8) | "Oppose — invoke subsidiarity principle / request carve-out on public security" | Low/no obligation |

**PNO early indicator (`INSTITUTIONAL_MODEL`):**  
Cluster C's "public security carve-out" request is structurally identical to carve-out requests made in 3 previous AI-adjacent directives (GDPR enforcement scope, NIS2 critical infrastructure). If the engine's historical PNO analysis shows that public security carve-outs systematically reduce directive effectiveness by > 30%, this is a PNO precursor signal. Engine assessment required (OPERATIONAL).

---

## Step 3 — EU Council Aggregation

The EU Council presidency attempts to find a compromise text satisfying QMV:

**QMV arithmetic:**
- Cluster A: 7 states (pro)
- Cluster B: 12 states (pro with amendment)
- Cluster C: 8 states (against)
- States needed for QMV: 15 states + 65% population

Cluster A + B = 19 states ✓  
Population check: 7×Cluster_A_pop + 12×Cluster_B_pop = ~60% → **below 65% threshold** ✗

**Result: QMV threshold NOT met on population criterion.**

```text
μ_consensus (INSTITUTIONAL_MODEL, to be computed by engine):
  State count dimension: ~0.70 (19/27 ≈ 70% of states)
  Population dimension: ~0.60 (below 65% required)
  Combined μ_consensus: < threshold → CONSENSUS FAILURE

α_error:
  Cluster A: moderate (directive weakened in compromise text)
  Cluster B: low (compromise close to their optimum)
  Cluster C: high (any adoption is far from their optimum)
  EU aggregate α_error: driven upward by Cluster C magnitude
```

**Consensus failure state:** The presidency must either (a) renegotiate for one or more Cluster C states, (b) narrow the directive scope (reducing α for Cluster C at cost of higher α for Cluster A), or (c) invoke enhanced cooperation (≥9 states).

---

## Step 4 — Catastrophe Signal Detected

The consensus failure triggers a bifurcation detection request:

```json
{
  "event_type": "bifurcation_detection_request",
  "state_id": "EU",
  "state_vector": {
    "integration_depth": 0.68,
    "consensus_signal": 0.58,
    "rule_of_law_tension": 0.44,
    "economic_divergence": 0.31
  },
  "time_window": "P18M",
  "reference_manifold": "cusp"
}
```

**Cusp catastrophe analysis (`INSTITUTIONAL_MODEL`):**

The two control parameters are:
- `integration_depth` (0.68 — moderately deep, below historic peak)
- `rule_of_law_tension` (0.44 — elevated, driven by Cluster C judiciary gap signals)

At these parameter values, the cusp manifold indicates:

- The system is in the **hysteresis region**: two stable attractors co-exist ("adopt directive" vs. "fragmented variable geometry")
- Small additional increases in `rule_of_law_tension` (e.g., a CJEU ruling against a Cluster C state during negotiations) could push the system past the fold boundary to the fragmentation attractor
- **Early warning signals present:**
  - μ_consensus oscillating between 0.58 and 0.63 across three presidency compromise proposals (flickering signal)
  - Cluster C bloc α_error increasing monotonically across negotiation rounds (critical slowing down precursor)

```text
Bifurcation proximity estimate (INSTITUTIONAL_MODEL, engine computation required):
  Estimated distance to fold boundary: low-moderate
  Attractor basin current: "negotiated adoption" (marginal)
  Risk: transition to "fragmentation / enhanced cooperation" attractor
```

---

## Step 5 — NAMM Analysis

### 5.1 Signals Sent to Engine

The EU simulator packages the following signals for the Errorlogy engine:

```json
{
  "schema_version": "1.0",
  "event_id": "eu-ai-reg-2027-council-vote-01",
  "source_layer": "eu_simulator",
  "timestamp": "2027-03-15T00:00:00Z",
  "institutional_context": {
    "activated_layers": [
      "eu_simulator:parliament",
      "eu_simulator:council",
      "eu_simulator:judiciary",
      "eu_simulator:transnational_ops"
    ],
    "topology_tensions": [
      "parliament:mandate_gap:cluster_c",
      "judiciary:rule_of_law:cluster_c_states",
      "transnational:coordination_failure:population_threshold"
    ],
    "voting_rule_active": "qmv"
  },
  "engine_outputs": {
    "mu_consensus": null,
    "alpha_error": null,
    "pno_regime": null,
    "fpd_aggregate": null,
    "bifurcation_proximity": null
  },
  "epistemic_label": "INSTITUTIONAL_MODEL",
  "certificate_ref": null
}
```

*All `null` engine fields are placeholders — the Errorlogy engine populates them. Only then does the label upgrade to `OPERATIONAL` or `COMPUTATIONAL_EVIDENCE`.*

### 5.2 FPD Divergence Measurement

**FPD scenario (`INSTITUTIONAL_MODEL`):**

Twelve months prior, each national AI parliament produced a forecast: "AI Regulation Directive will be adopted by Q2 2027."

- Cluster A forecast confidence: 0.88
- Cluster B forecast confidence: 0.74
- Cluster C forecast confidence: 0.31

EU-level aggregate forecast (simple average): 0.64

**Observed outcome:** Non-adoption (QMV threshold not met) — effective performance = 0.

FPD per cluster:
- Cluster A: FPD = |0.88 - 0| = 0.88 (overconfident in adoption)
- Cluster B: FPD = |0.74 - 0| = 0.74
- Cluster C: FPD = |0.31 - 0| = 0.31 (least surprised — forecast was skeptical)

**EU aggregate FPD: ~0.64**

**Aggregation bias observation (`INSTITUTIONAL_MODEL`):**  
A hypothetical EU-level model with full cross-state preference information would have assigned adoption probability ~0.42 (accounting for population QMV failure). The simple-average aggregation produced 0.64 — an overestimate of 0.22. This overestimate is the **cross-state FPD aggregation bias** described in Section C.2 of NAMM_EU_THEORY.md.

Engine FPD computation (OPERATIONAL) required to confirm. NAMM holdout experiment recommended (see Section D.4 of NAMM_EU_THEORY.md, item 4).

### 5.3 PNO Regime Assessment

**PNO check (`INSTITUTIONAL_MODEL`):**

If this is the third consecutive EU AI-adjacent directive where:
- Rule-of-law tension from Cluster C states contributes to adoption delay or weakening
- The final adopted text (if any) systematically undershoots Cluster A/B preferred stringency
- Implementation divergence in Cluster C states after adoption is measurable

...then the Errorlogy engine should assess whether a **PNO regime** is active for EU AI governance.

PNO regime activation would mean: the EU AI governance system has a structural negative offset — policy outcomes persistently below stated intent — driven by the sovereignty-defense preference cluster. This is analytically descriptive, not a determination of fault.

```text
PNO regime assessment (OPERATIONAL — engine required):
  Domain: EU AI regulation
  Cycle count: 3+ (historical corpus needed)
  Convergence trend: declining (each cycle shows wider Cluster C resistance)
  PNO_regime: [pending engine computation]
```

---

## Step 6 — Output

### Final Institutional Model Output

```text
INSTITUTIONAL_MODEL output for scenario eu-ai-reg-2027-council-vote-01:

Deliberation result:
  - 27 national AI parliaments deliberated
  - 3 preference clusters emerged with mutually intransitive sovereignty dimension
  - QMV threshold not met (population criterion failed by ~5%)
  - Consensus failure → presidency re-negotiation required

Signal summary:
  - μ_consensus: below QMV threshold (engine computation pending → OPERATIONAL)
  - α_error: elevated, driven by Cluster C magnitude
  - FPD aggregation bias: ~0.22 overestimate (institutional estimate → engine confirmation pending)
  - Bifurcation proximity: elevated — system in cusp hysteresis region
  - PNO regime: possible (3rd consecutive cycle pattern → engine assessment pending)

Catastrophe signal:
  - Cusp catastrophe topology: integration_depth × rule_of_law_tension control parameters
  - Early warning signals: flickering (μ_consensus), critical slowing (Cluster C α_error trend)
  - Attractor: "negotiated adoption" basin, marginal; risk of transition to "fragmentation"

NAMM queue:
  - Catastrophe manifold certificate (experiment type: bifurcation geometry)
  - FPD aggregation bias holdout (experiment type: generative holdout)
  - PNO regime persistence certificate (experiment type: persistence criterion)
```

### Epistemic Label Summary

| Output | Label | Reason |
|--------|-------|--------|
| Preference cluster μ signals | `INSTITUTIONAL_MODEL` | Engine not yet run |
| QMV arithmetic | `INSTITUTIONAL_MODEL` | Structural analysis, no engine required |
| FPD aggregation bias estimate | `INSTITUTIONAL_MODEL` | Institutional computation, not engine |
| Bifurcation proximity | `INSTITUTIONAL_MODEL` | Engine required for OPERATIONAL label |
| PNO regime determination | Pending `OPERATIONAL` | Engine run on historical corpus required |
| Any NAMM-certified outputs | `COMPUTATIONAL_EVIDENCE` | Requires `certificate.json` from namm-experiments |

---

## Cross-links

- [`../integrations/NAMM_EU_THEORY.md`](../integrations/NAMM_EU_THEORY.md) — theoretical framing for this cascade
- [`../integrations/ERRORLOGY.md`](../integrations/ERRORLOGY.md) — engine pipeline and μ/α/PNO/FPD definitions
- [`../integrations/NAMM.md`](../integrations/NAMM.md) — NAMM integration and epistemic labels
- [`../institutions/AI_TRANSNATIONAL_OPS.md`](../institutions/AI_TRANSNATIONAL_OPS.md) — EU transnational layer
- [trump-macron-cascade.md](trump-macron-cascade.md) — bilateral cascade reference
- [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) — certificate experiments
