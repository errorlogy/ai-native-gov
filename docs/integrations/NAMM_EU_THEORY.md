# Theoretical Frame — NAMM × EU Multi-State Simulator

**Epistemic label:** `INSTITUTIONAL_MODEL`  
**Scope:** Analytical framing connecting the 27-state EU AI government simulator to NAMM mathematical concepts and the Errorlogy engine.  
**Engine math owner:** [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) — this document defines *contracts and interfaces only*, not implementations.

> All outputs in this frame are `INSTITUTIONAL_MODEL` unless explicitly marked `COMPUTATIONAL_EVIDENCE` (requires linked `certificate.json` from namm-experiments).

---

## Section A — Permanent Sub-optimality of Consensus in Multi-Agent Systems

### A.1 Arrow's Impossibility Analog for AI Agent Collectives

Arrow's Impossibility Theorem establishes that no ranked-preference voting rule can simultaneously satisfy: unanimity, independence of irrelevant alternatives, and non-dictatorship. Applied to a 27-agent EU simulator:

- Each **national AI parliament** produces a ranked preference ordering over policy options.
- The **EU Council aggregation layer** is the social choice function.
- Arrow's conditions map directly: no aggregation rule can be simultaneously Pareto-efficient, IIA-satisfying, and non-dictatorial across 27 heterogeneous preference profiles.

**Institutional implication (`INSTITUTIONAL_MODEL`):**  
The EU Council aggregation is structurally incapable of producing a "best" outcome in any global sense. Sub-optimality is not a defect of deliberation quality — it is a property of multi-agent preference heterogeneity at scale.

### A.2 Condorcet Cycles and Preference Aggregation Failures in the 27-State System

Condorcet cycles (A > B > C > A under pairwise voting) become increasingly probable as the number of agents grows. For a 27-member body with non-trivially correlated but non-identical preferences:

- Probability of a dominant Condorcet winner drops as policy dimensionality rises.
- Regional blocs (Visegrád, Nordic, Mediterranean) introduce **preference clusters** that are internally coherent but mutually intransitive at EU level.
- Agenda sequencing (what gets voted first) can determine outcome independent of underlying preferences — a structural manipulation vector.

**Modeling note:** The μ signal from the Errorlogy engine measures **fuzzy membership** of a policy position within a consensus cluster. A Condorcet cycle manifests as multiple policy positions each holding μ > 0.5 with respect to different sub-coalitions — no single option dominates the full μ space.

### A.3 EU Council Voting as Failure Mode Spectrum

| Voting rule | Failure mode | μ signature |
|-------------|-------------|-------------|
| Unanimity (Article 48 TEU) | Single-state veto → deadlock | μ_consensus → 0 if any member μ_assent < threshold |
| Qualified Majority (55% states, 65% population) | Majority tyranny / minority exclusion | μ_consensus high at EU level, low for excluded bloc |
| Enhanced cooperation (9+ states) | Fragmentation into variable geometry | μ_consensus = cluster-local, not EU-global |

All three modes represent different positions on the sub-optimality spectrum — not resolutions of it. The shift between modes is itself a bifurcation event (see Section B).

### A.4 Modeling Contract: μ and α in Consensus Measurement

Actual μ/α computation belongs to the Errorlogy engine. This section defines the **interface contract** for how institutional layer outputs feed that computation.

**Input contract (umbrella → engine):**

```json
{
  "event_type": "eu_council_vote",
  "vote_topic_id": "string",
  "member_state_positions": [
    {
      "state_id": "iso3166_alpha2",
      "position_vector": "float[]",
      "bloc_membership": "string[]",
      "assent_signal": "float [0,1]"
    }
  ],
  "voting_rule": "unanimity | qmv | enhanced_cooperation",
  "consensus_threshold": "float"
}
```

**Expected engine outputs (OPERATIONAL):**

- `μ_consensus`: fuzzy membership of the proposed outcome in the "valid EU consensus" set
- `α_error`: deviation signal — how far the aggregated outcome is from any member's preference optimum
- `PNO_regime`: whether the system is in a persistent negative offset state (see Section C)

**"Permanent" aspect:**  
Sub-optimality is not measured as distance from an ideal optimum (which Arrow shows is undefined) but as the *structural floor* below which μ_consensus cannot rise given the preference heterogeneity of 27 members. This floor is a property to model and measure, not a defect to fix.

---

## Section B — Catastrophe Theory Applied to EU Political Dynamics

### B.1 Core Concepts Applied to Institutional Stability

Catastrophe theory (Thom, Zeeman) describes systems where smooth variation in control parameters produces discontinuous jumps in state. The relevant elementary catastrophes for EU political dynamics:

**Fold catastrophe** — one control parameter, two stable states, sudden jump between them:  
- Example: a member state's position on EU integration has two stable attractors (in/out, compliant/defiant). Incremental pressure produces no response until a fold point, then discontinuous regime shift.

**Cusp catastrophe** — two control parameters, hysteresis region, divergent outcomes from similar starting points:  
- Example: EU enlargement combined with rule-of-law tension creates a cusp surface where identical governance scores produce either stable integration or sudden defection depending on path history.

### B.2 State Variables for the EU Simulator

| State variable | Description | Engine signal |
|---------------|-------------|---------------|
| `integration_depth` | Degree of supranational competence ceded by member states | μ_membership in "deep integration" mode cluster |
| `consensus_signal` | Aggregate EU Council agreement level | μ_consensus (see Section A) |
| `rule_of_law_tension` | Divergence between member state judicial practice and EU Charter | α_error from judiciary layer |
| `economic_divergence` | North-South / East-West economic gap proxy | FPD divergence metric (see Section C) |

### B.3 Bifurcation Conditions: When Does a Member State Exit or Defect?

A member state exits the consensus attractor basin when:

1. `rule_of_law_tension` crosses a threshold such that judiciary-layer α exceeds PNO unstable regime boundary
2. `economic_divergence` triggers FPD scenario bifurcation (two plausible futures > one)
3. Domestic political signal (national parliament μ_opposition > 0.7) makes EU position domestically untenable

**Brexit as historical fold catastrophe (`INSTITUTIONAL_MODEL`):**  
The UK's trajectory represents a fold catastrophe in retrospect:
- Control parameter: integration_depth (increasing with Lisbon, then perceived as further increasing)
- State variable: domestic political stability of EU membership consensus
- Fold point: 2016 referendum — the smooth variation in integration perception reached the fold, producing a discontinuous jump to the "exit" attractor
- Hysteresis: re-entry to previous state is blocked by the fold topology (no smooth path back through the same parameter values)

This is an analytical framing only — it does not determine causal responsibility for Brexit.

### B.4 EU Enlargement as Parameter Shift on the Catastrophe Manifold

Enlargement changes the shape of the catastrophe manifold itself:

- Each new member adds a preference dimension, widening the Condorcet cycle probability space (Section A)
- Enlargement to heterogeneous rule-of-law states shifts the cusp parameter toward the hysteresis region
- A stable EU-27 cusp manifold may become a fold manifold under EU-35+ conditions — the same governance stress that produced only tension at 27 members produces a bifurcation at 35

**Early warning signal detection:**  
The following signal patterns precede catastrophic bifurcation in the model:

| Early warning signal | Engine observable | Threshold indicator |
|---------------------|------------------|---------------------|
| Critical slowing down | α_error variance increasing | FPD forecast uncertainty widening |
| Flickering | μ_consensus oscillating between two basins | Repeated vote reversals without stable outcome |
| Rising correlation | Cross-state α signals becoming correlated | Bloc defection risk rising |
| FPD divergence spike | Forecast-performance gap widening before event | See Section C |

### B.5 Integration with Errorlogy Engine: Bifurcation Detection Contract

**Input contract (umbrella → engine):**

```json
{
  "event_type": "bifurcation_detection_request",
  "state_id": "iso3166_alpha2 | EU",
  "state_vector": {
    "integration_depth": "float [0,1]",
    "consensus_signal": "float [0,1]",
    "rule_of_law_tension": "float [0,1]",
    "economic_divergence": "float"
  },
  "time_window": "ISO8601_duration",
  "reference_manifold": "fold | cusp | eu_custom"
}
```

**Expected outputs (OPERATIONAL from engine):**

- `bifurcation_proximity`: distance to nearest fold/cusp boundary in state space
- `attractor_basin_id`: which stable state the system currently occupies
- `early_warning_signals`: array of detected precursor patterns with μ weights

For NAMM verification of bifurcation detection geometry, see Section D.

---

## Section C — PNO/FPD in Multi-Jurisdictional Context

### C.1 PNO as Systematic Bias in Consensus Outcomes

PNO (Permanent Negative Offset) in the Errorlogy engine captures systematic underperformance relative to stated targets — a persistent gap between declared policy intent and measured outcome that does not close over time.

In the EU multi-jurisdictional context, PNO manifests as:

**Structural PNO sources:**

| Source | Mechanism | EU manifestation |
|--------|-----------|-----------------|
| Preference aggregation floor | Arrow/Condorcet structural sub-optimality (Section A) | EU directives systematically satisfy no member state's optimum |
| Implementation divergence | National transposition introduces drift from directive intent | μ_compliance gap between directive and national law |
| Enforcement asymmetry | Commission enforcement capacity vs. member state count | Some violations persist without correction → PNO regime |
| Veto-point accumulation | Each unanimity requirement adds potential negative offset | Policy reform consistently delayed relative to external rate of change |

**PNO regime definition for EU context:**  
A PNO regime is active when `α_error` remains persistently positive (outcome < intent) across ≥ 3 consecutive policy cycles for a given domain, with no convergence trend. The Errorlogy engine determines PNO regime status — this is the interface contract for triggering that assessment.

### C.2 FPD in Cross-State Policy Predictions

FPD (Forecast-Performance Divergence) measures the gap between institutional forecast and measured outcome. In a 27-state system, FPD compounds:

**Aggregation FPD:**  
A forecast made at EU level (e.g., "AI regulation directive will be adopted by Q3 2027") has FPD contributions from:
- Each member state's implementation variance
- Council vote sequencing effects (Section A.3)
- Catastrophe proximity effects — high bifurcation proximity inflates forecast variance (Section B.4)

**Cross-state FPD correlation:**  
When national AI ministers' local forecasts are aggregated without accounting for preference heterogeneity, the resulting EU-level FPD will be systematically understated. Each national model is calibrated to domestic conditions; cross-state policy produces outcomes outside any single model's training distribution.

**FPD measurement contract (umbrella → engine):**

```json
{
  "forecast_id": "string",
  "forecast_scope": "eu_wide | member_state | cross_border",
  "member_state_forecasts": [
    {
      "state_id": "iso3166_alpha2",
      "forecast_vector": "float[]",
      "forecast_horizon": "ISO8601_date",
      "model_confidence": "float [0,1]"
    }
  ],
  "aggregation_method": "weighted_average | qmv_analogy | council_simulation",
  "reference_outcome": "float[] (ex-post, for historical calibration)"
}
```

### C.3 Local Optima → EU-Level Sub-optimality: The Aggregation Problem

Each national AI minister operates a policy optimization process targeting national welfare. The EU policy outcome is a constrained aggregation of 27 such optima.

**Why local optima aggregate to EU-level sub-optimality:**

1. **Preference heterogeneity** (Section A): no policy exists at the intersection of 27 national optima
2. **Strategic behavior**: national ministers anchor to domestic optima and negotiate from there, producing outcomes in the interior of the preference space (satisficing, not optimizing)
3. **Information asymmetry**: each national model has domain-specific information the others lack; no aggregation mechanism fully pools this information
4. **PNO accumulation**: each compromise step introduces a negative offset; stacked over 27 preferences, the cumulative PNO can be large

**Modeling implication:**  
The EU-level policy optimum, as computed by a single "EU AI super-minister" with full information, would differ from the Council-aggregated outcome by the **consensus discount** — a measurable quantity that PNO and FPD together can bound. The engine computes this; the umbrella layer names the institutional mechanism.

### C.4 Measurement: Errorlogy Engine Outputs Capturing These Signals

| Signal | Engine output field | Institutional source |
|--------|-------------------|---------------------|
| Consensus strength | μ_consensus | EU Council vote aggregate |
| Deviation from member optima | α_error per member state | National parliament vs. Council outcome |
| Systematic underperformance | PNO_regime flag | Council vote history |
| Forecast accuracy at EU level | FPD_eu_aggregate | Cross-state policy prediction |
| Bloc-level divergence | ACC_cluster membership | Regional bloc positioning |

All numerical values are `OPERATIONAL` — produced by the Errorlogy engine only. This section defines what institutional observables map to each signal field.

---

## Section D — Integration with Simulator

### D.1 EU Topology Tension Signals Feeding NAMM Analysis

The EU simulator topology (see [`../institutions/AI_TRANSNATIONAL_OPS.md`](../institutions/AI_TRANSNATIONAL_OPS.md) and [`../institutions/TOPOLOGY.md`](../institutions/TOPOLOGY.md)) produces tension signals that feed into both Errorlogy and NAMM:

| Tension signal | Source topology layer | NAMM analogue |
|---------------|----------------------|---------------|
| Parliament ↔ Council mandate gap | `institution:parliament` × `institution:eu-council` | Graph invariant on α-propagation |
| Judiciary rule-of-law alert | `institution:judiciary` | Attractor boundary certificate |
| Cross-state coordination failure | `institution:transnational-ops` | Meta-operator fixed point |
| Enlargement parameter shift | `institution:charter` update | Manifold topology change |

### D.2 Event Types Triggering Catastrophe Detection

The following event types, when received by the EU simulator, should trigger a bifurcation detection request (Section B.5):

- `eu_council_vote_failure` — unanimous veto or QMV threshold not met
- `member_state_defection_signal` — state withdraws from negotiation or invokes Article 7
- `rule_of_law_ruling` — CJEU ruling against member state with non-compliance history
- `enlargement_accession_event` — new member state accession or application
- `economic_divergence_alert` — economic gap metric exceeds historical 90th percentile

### D.3 Output Format: COMPUTATIONAL_EVIDENCE Packets to NAMM

When the Errorlogy engine produces certified outputs (bifurcation proximity, PNO regime, FPD holdout), the NAMM experiments repo receives packets in the following envelope (from [`../../schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json)):

```json
{
  "schema_version": "1.0",
  "event_id": "string",
  "source_layer": "eu_simulator",
  "timestamp": "ISO8601",
  "institutional_context": {
    "activated_layers": ["string"],
    "topology_tensions": ["string"],
    "voting_rule_active": "string"
  },
  "engine_outputs": {
    "mu_consensus": "float",
    "alpha_error": "float",
    "pno_regime": "boolean",
    "fpd_aggregate": "float",
    "bifurcation_proximity": "float | null"
  },
  "epistemic_label": "COMPUTATIONAL_EVIDENCE | OPERATIONAL | INSTITUTIONAL_MODEL",
  "certificate_ref": "namm_certificate_url | null"
}
```

`certificate_ref` is populated only when a NAMM experiment has run and produced a `certificate.json`. Until then, the packet carries `INSTITUTIONAL_MODEL` or `OPERATIONAL` labels.

### D.4 NAMM Experiment Queue for EU Simulator

Priority experiments to queue in [namm-experiments](https://github.com/errorlogy/namm-experiments):

1. **Catastrophe manifold certificate** — verify that the fold/cusp geometry in Section B is consistent with the observed EU tension signal dataset (requires retrospective corpus)
2. **Condorcet cycle frequency** — holdout experiment: given 27-state preference profiles, certify the probability of Condorcet cycle occurrence as a function of preference heterogeneity
3. **PNO regime persistence** — certify whether detected PNO regimes in EU policy domains satisfy the persistence criterion (≥ 3 cycles, no convergence)
4. **FPD aggregation bias** — generative holdout: does aggregating 27 national FPD signals understate EU-level forecast variance? Certify the bias direction and magnitude.

---

## Links

- [`ERRORLOGY.md`](ERRORLOGY.md) — engine pipeline, μ/α/PNO/FPD definitions
- [`NAMM.md`](NAMM.md) — NAMM integration, epistemic labels, experiment queue
- [`../institutions/AI_TRANSNATIONAL_OPS.md`](../institutions/AI_TRANSNATIONAL_OPS.md) — EU-level transnational layer
- [`../institutions/TOPOLOGY.md`](../institutions/TOPOLOGY.md) — intersection map
- [`../examples/eu-consensus-cascade.md`](../examples/eu-consensus-cascade.md) — worked cascade example
- [namm-experiments](https://github.com/errorlogy/namm-experiments) — verification experiments
- [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) — engine math source
