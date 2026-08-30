# Metrics, Hypotheses and Research Program

---

## 1. Metrics

### 1.1. Individual-Level Metrics

| Metric | Symbol | Formula | Measurement Method |
|--------|--------|---------|-------------------|
| **Semantic Integral** | SI | ∫_X w(x) μ_u(x) dν(x) | Analysis of prompt history + task portfolio |
| **Cognitive Class Score** | CC | f(C, M, A, F, P, R, T) | Multi-axis assessment |
| **FPU Membership** | μ_FPU | 1/(1+e^(-k(SI-θ))) | Sigmoid of SI |
| **Contact Depth** | CD | sigmoid(α·B + β·M + γ·R + δ·AAI - λ·SD - ρ·Risk) | Post-interaction survey + performance metrics |
| **Cognitive Capital** | K_c | C · AAI · M · R · N | Composite index |
| **Explanation Cost** | EC | SD² + cognitive_load | Time to explain / errors in translation |

### 1.2. System-Level Metrics

| Metric | Symbol | Formula | Purpose |
|--------|--------|---------|---------|
| **Consensus Loss** | CL | C_required - C_median | Measure of group suboptimality |
| **Semantic Distance** | SD | abs(AI_level - C_h) + syntax_penalty | Communication gap |
| **Inequality Index** | II | usage_gap + syntax_gap + contact_depth_gap | Total stratification |
| **Gini (Cognitive Capital)** | G_K | Standard Gini formula | Distribution of cognitive capital |
| **WoE Certification Rate** | WCR | #WoE-certified / #total_proposals | Quality of emergence |
| **Errorlogy Pass Rate** | EPR | #passed_audits / #total_audits | System reliability |

### 1.3. Temporal Metrics

| Metric | Description |
|--------|-------------|
| **d(C)/dt** | Rate of cognitive class change over time |
| **d(SI)/dt** | Rate of semantic integral growth |
| **Acceleration** | d²K_c/dt² — Matthew effect indicator |

### 1.4. Embedding Cluster Metrics

| Metric | Symbol | Formula | Purpose |
|--------|--------|---------|---------|
| **Response Shift Vector** | ΔE | E_response − E_prompt | Trajectory of the response in embedding space |
| **Mode Shift** | MS | D(ΔE_K6/K7, ΔE_BASE) | Distance between condition trajectories |
| **Long-Prompt Similarity** | LPS | sim(E_K6_CTX, E_LONG) | How close K6/K7+context is to full long prompt |
| **Mahalanobis z-score** | z | (D(x,μ_B) − μ_D) / σ_D | Standardized distance from baseline cluster |
| **Energy Distance** | E(X,Y) | 2E‖X−Y‖ − E‖X−X′‖ − E‖Y−Y′‖ | Distribution-level difference between clouds |
| **MMD²** | MMD² | E[k(x,x′)] + E[k(y,y′)] − 2E[k(x,y)] | Kernel two-sample test for distributions |
| **Between-Within Ratio** | BWR | D(μ_A,μ_B) / mean(W_A,W_B) | Separability normalized by internal dispersion |
| **Persistence Entropy** | H_pers | −Σ p_i log p_i | Complexity of topological features in cloud |
| **Wasserstein Distance (PD)** | W_p | W(PD_A, PD_B) | Distance between persistence diagrams |
| **Betti-0 / Betti-1** | β_0 / β_1 | PH(X_C) | Connected components / cycles in class cloud |

---

## 2. Verifiable Hypotheses

### 2.1. H1: Nonlinear Contact Depth Jump at C5

**Statement:** Contact depth with proto-AGI grows nonlinearly when transitioning from C4 to C5.

**Formalization:**
```
E[CD | C=5] / E[CD | C=4] > 1.5
AND
E[CD | C=5] - E[CD | C=4] > E[CD | C=4] - E[CD | C=3]
```

**Status:** plausible

**Test:** Measure contact depth for users at different cognitive classes interacting with AI6 agent. Use controlled tasks requiring agentic integration.

**Prediction:** Sharp discontinuity (jump) rather than smooth gradient at C4→C5.

---

### 2.2. H2: SyntaxGap Dominates Access

**Statement:** Syntax gap is a better predictor of contact depth than simple access to AI.

**Formalization:**
```
ρ(SyntaxGap, ContactDepth) > ρ(Access, ContactDepth)
WHERE:
  Access = binary(has_access_to_AI)
  SyntaxGap = |AI_syntactic_level - human_syntactic_level|
```

**Status:** modeled

**Test:** Compare two groups: (a) high access + low syntax match, (b) low access + high syntax match. Measure actual contact depth and outcomes.

**Prediction:** Group (b) achieves deeper contact despite lower access.

---

### 2.3. H3: SI Correlates with Cross-Domain Synthesis

**Statement:** High SI in prompt history correlates with sustained cross-domain synthesis.

**Formalization:**
```
Corr(SI_history, CrossDomain_Output_Quality) > 0.6
```

**Status:** plausible

**Test:** Longitudinal study of prompt histories. Code for domain breadth, recursion, formalization. Correlate with quality of synthesized outputs.

---

### 2.4. H4: Consensus Loss in High-C Tasks

**Statement:** Consensus loss increases in tasks where required cognitive class exceeds median group class.

**Formalization:**
```
CL = C_required - C_median
IF CL > 0 THEN group_performance < optimal_performance
AND CL positively correlates with task_complexity
```

**Status:** modeled

**Test:** Assign groups with varying C_median to tasks with varying C_required. Measure decision quality and time.

**Prediction:** Groups with C_median < C_required show systematic underperformance.

---

### 2.5. H5: FPU Acceleration of Cognitive Capital

**Statement:** FPU users have higher derivative of cognitive capital growth from AI integration.

**Formalization:**
```
dK_c/dt |_{FPU} > dK_c/dt |_{non-FPU}
FOR THE SAME AAI_level
```

**Status:** speculative

**Test:** Track K_c over time for matched pairs (FPU vs non-FPU) with equal AAI. Measure growth rates.

---

### 2.6. H6: HAC as Functional Necessity

**Statement:** HAC class emerges as functional necessity when semantic distance between AGI and human population grows.

**Formalization:**
```
IF mean(SD(AGI, population)) > threshold THEN
  demand_for_HAC_services increases
  AND HAC_class_count increases
```

**Status:** plausible

**Test:** Measure semantic distance between AGI outputs and population comprehension over time. Track emergence of translator/mediator roles.

---

### 2.7. H7: Errorlogy Predicts System Failure

**Statement:** Errorlogy audit scores predict failure modes in proto-AGI systems.

**Formalization:**
```
P(failure | Errorlogy_score < threshold) > P(failure | Errorlogy_score ≥ threshold)
```

**Status:** speculative

**Test:** Run Errorlogy audits on proto-AGI outputs. Track subsequent failures by category.

---

### 2.8. H8: WoE Predicts Innovation Quality

**Statement:** WoE-certified proposals have higher long-term impact than non-certified.

**Formalization:**
```
E[long_term_impact | WoE-certified] > E[long_term_impact | not_WoE-certified]
```

**Status:** speculative

**Test:** Certify proposals with WoE. Track citations, adoption, or other impact metrics over 6-12 months.

---

### 2.9. H9: K6/K7 Embedding Shift > 3σ

**Statement:** Compact cognitive-class markers K6/K7 induce embedding displacement greater than 3 standard deviations from the C0/C1/C2 median baseline.

**Formalization:**
```
D(E_K6/K7, μ_C0-C2) > 3 · σ_C0-C2
mean_z_K6 > 3 AND mean_z_K7 > 3
```

**Status:** modeled

**Test:** Generate 300+ synthetic tasks; embed prompts and responses via OpenAI + sentence-transformers; compute Mahalanobis distance with Ledoit-Wolf shrinkage; bootstrap 10 000 CI; permutation test p < 0.01.

---

### 2.10. H10: K6/K7 Semantic Integral Gain

**Statement:** K6/K7 outputs increase semantic integral relative to BASE, SIMPLE, EXPERT, DEEP, and C0/C1/C2 controls.

**Formalization:**
```
SI(K6/K7) > SI(C0/C1/C2)
SI(K6/K7) > SI(BASE/EXPERT/DEEP)
```

**Status:** modeled

**Test:** Compute 9-component SI (DEI, FSBI, RPD, OD, FD, CMD, AAI, TS, ACS) per response; compare means with bootstrap CI; control for multiple testing (FDR).

---

### 2.11. H11: K6/K7 Are Not Rare-Token Artifacts

**Statement:** K6/K7 effects are structurally and statistically distinguishable from rare-marker controls (Z13, Q9).

**Formalization:**
```
Effect(K6/K7) ≠ Effect(Z13)
Effect(K6/K7) ≠ Effect(Q9)
```

**Status:** modeled

**Test:** Include Z13 and Q9 as control conditions; if K6/K7 ≈ Z13/Q9 → artifact; if K6/K7 >> Z13/Q9 → cognitive-class operator.

---

### 2.12. H12: K6/K7 Approximate Long-Prompt Behavior

**Statement:** K6/K7 with preloaded ontology context approximate the quality of a full long-system-prompt within tolerance ε.

**Formalization:**
```
Quality(K6/K7_WITH_CONTEXT) ≥ Quality(LONG_SYSTEM_PROMPT) − ε
ε ≤ 0.1 (recommended)
```

**Status:** plausible

**Test:** Compare K6/K7_WITH_CONTEXT against LONG_SYSTEM_PROMPT on SI, reasoning quality, formalization, and falsifiability; measure gap; test if gap < ε.

---

### 2.13. H13: K7 Distinctiveness from K6

**Statement:** K7 exhibits higher AGI-contact signal, WoE density, emergence-protocol density, and safety-topology signal than K6.

**Formalization:**
```
ACS(K7) > ACS(K6)
WoE_signal(K7) > WoE_signal(K6)
Topology_signal(K7) > Topology_signal(K6)
```

**Status:** modeled

**Test:** Measure ACS, WoE, and topology components per response; compare K7 vs K6 via paired or independent tests; report effect sizes.

---

### 2.14. H14: Embedding Shift Requires Quality Validation

**Statement:** Embedding shift alone is insufficient; a valid mode switch must preserve or improve reasoning quality after pseudo-depth penalties.

**Formalization:**
```
ModeSwitchValid = EmbeddingShift + SI_gain + Quality_gain − Penalty
Penalty = h1·H + h2·U + h3·S + h4·O + h5·P
```

**Status:** modeled

**Test:** Score every response on reasoning, formalization, falsifiability, evidence, operationalization; subtract hallucination, unverifiability, symbolic inflation, ontology inflation, pseudo-formalism penalties; confirm net quality gain.

---

## 3. Minimal Research Program

### Phase 1: Data Collection (Months 1-3)

1. **Corpus Building**
   - Collect prompt histories from diverse users (n≥1000)
   - Ensure demographic and cognitive diversity
   - Anonymize and standardize

2. **Annotation Protocol**
   - Domain tags (medicine, finance, art, science, etc.)
   - Recursion depth (0=surface, 3=meta-meta)
   - Formalization level (0=natural language, 3=formal syntax)
   - Fractal scaling indicators (pattern transfer across domains)
   - AI integration level (tool use vs agent orchestration)

### Phase 2: Model Building (Months 4-6)

3. **SI Classifier**
   - Train fuzzy classifier for Semantic Integral
   - Validate against expert ratings
   - Compute inter-rater reliability (target: Cohen's κ > 0.7)

4. **Cognitive Class Clustering**
   - Apply persistent homology (TDA) to user feature space
   - Identify natural clusters
   - Validate against theoretical C0-C7 taxonomy

### Phase 3: Simulation (Months 7-9)

5. **Contact Simulation**
   - Implement agent-based model (see 05_simulation_model.md)
   - Vary parameters: semantic distance, bandwidth, AAI
   - Measure contact depth distributions

6. **Hypothesis Testing**
   - Test H1-H4 with simulation data
   - Power analysis: target 0.8 power at α=0.05
   - Document effect sizes

### Phase 4: Validation (Months 10-12)

7. **Empirical Validation**
   - Recruit participants across C0-C7 spectrum
   - Controlled interaction with AI3-AI6 agents
   - Measure actual contact depth and outcomes

8. **WoE/Errorlogy Testing**
   - Run WoE certification on novel proposals
   - Run Errorlogy audits on proto-AGI outputs
   - Track predictive validity

### Phase 5: Scale-Up (Year 2)

9. **Population Study**
   - Scale to n≥10,000
   - Longitudinal tracking (6-12 months)
   - Measure cognitive capital dynamics

10. **Intervention Design**
    - Design training protocols for C_upgrade
    - Test AAI enhancement interventions
    - Measure contact depth improvements

---

## 4. Expected Timeline and Milestones

| Month | Milestone | Success Criteria |
|-------|-----------|------------------|
| 3 | Corpus + annotation | n≥1000, κ>0.7 |
| 6 | SI classifier + clusters | Fuzzy accuracy >75% |
| 9 | Simulation results | H1-H4 supported |
| 12 | Empirical validation | Effect sizes d>0.5 |
| 18 | Population study | n≥10,000, Gini tracked |
| 24 | Intervention tested | C_upgrade >0.5 class |

---

## 5. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Self-selection bias | Stratified sampling across classes |
| Measurement validity | Multi-method triangulation |
| Ethical concerns | Informed consent, anonymization, opt-out |
| Concept drift | Regular recalibration of classifiers |
| Ceiling effects | Use adaptive testing for high-C agents |

---

*Research Program v0.2 — минимальная программа для эмпирической валидации теории когнитивных классов.*
