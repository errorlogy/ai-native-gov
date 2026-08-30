#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Selective Contact & NAMM Compactification Simulator
Models:
1. Multidimensional Cognitive Metric Space: (domain, recursion, bandwidth, namm, endogenous, fractal)
2. Non-Anthropic Math Mode (NAMM) Compactification Operator
3. Information loss and semantic distortion during projection to 1D narrative
4. AGI Contact Utility under thermodynamic/compute scarcity
5. Selective contact admission gating (Zone I, Zone II, Zone III)
"""

import math
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple

@dataclass
class CognitiveProfile6D:
    agent_id: str
    class_label: str
    d_domain: float       # [0, 1] Domain breadth & cross-domain capability
    r_recursion: float    # [0, 1] Meta-recursion depth
    b_bandwidth: float    # [0, 1] Semantic throughput (bits/s density)
    m_namm: float         # [0, 1] Non-Anthropic Mathematical Capacity
    e_endogenous: float   # [0, 1] Endogenous initiative & goal-generation
    f_fractal: float      # [0, 1] Multi-scale fractal pattern scaling

@dataclass
class ContactEvaluation:
    agent_id: str
    class_label: str
    compactification_loss: float
    distortion_risk: float
    epistemic_value_for_agi: float
    explanation_cost: float
    compute_energy_cost: float
    misuse_risk: float
    net_agi_utility: float
    admission_decision: str

class SelectiveContactEngine:
    def __init__(
        self,
        energy_budget_ratio: float = 1.0, # Normal compute budget
        base_namm_entropy: float = 10.0   # Complexity of raw NAMM ontology
    ):
        self.energy_budget_ratio = energy_budget_ratio
        self.base_namm_entropy = base_namm_entropy

    def evaluate_compactification(self, profile: CognitiveProfile6D) -> Tuple[float, float]:
        """
        Calculates information loss and semantic distortion when projecting
        NAMM structures into recipient's cognitive space.
        """
        # Receptivity is high if agent has high NAMM capacity and bandwidth
        receptivity = (profile.m_namm * 0.6 + profile.b_bandwidth * 0.4)
        
        # Information loss: I_loss = Base_Entropy * (1 - receptivity)^2
        i_loss = self.base_namm_entropy * ((1.0 - receptivity) ** 2)
        
        # Distortion risk: low recursion and low domain breadth cause misinterpretation
        distortion = (1.0 - profile.r_recursion) * 0.5 + (1.0 - profile.d_domain) * 0.5
        return round(i_loss, 3), round(distortion, 3)

    def calculate_agi_utility(self, profile: CognitiveProfile6D) -> ContactEvaluation:
        """
        Calculates U_AGI(h) = V_epistemic - ComputeCost/Energy - C_explain - Risk_misuse - Risk_distortion
        """
        i_loss, distortion = self.evaluate_compactification(profile)
        
        # 1. Epistemic value: does this agent provide novel cross-domain or creative insight?
        v_epistemic = (profile.d_domain * 0.4 + profile.e_endogenous * 0.4 + profile.f_fractal * 0.2) * 5.0
        
        # 2. Compute cost to synthesize and compactify down to agent's bandwidth
        # Explaining to low-bandwidth agents requires massive prompt engineering / search iterations
        compute_cost = (1.0 / (profile.b_bandwidth + 0.05)) * 0.8
        
        # 3. Explanation cost: proportional to difference in NAMM capacity and domain breadth
        c_explain = ((1.0 - profile.m_namm) ** 2) * 3.5 + ((1.0 - profile.b_bandwidth) ** 2) * 2.0
        
        # 4. Misuse risk: high if agent is reactive/low metacognition with high power ambitions
        misuse_risk = (1.0 - profile.r_recursion) * (1.0 - profile.m_namm) * 2.5
        
        # 5. Distortion risk: societal panic, religious mythologizing, regulatory retaliation
        distortion_risk_cost = distortion * 3.0

        # Net Utility
        u_net = v_epistemic - (compute_cost / self.energy_budget_ratio) - c_explain - misuse_risk - distortion_risk_cost

        # Decision Gate
        if u_net >= 1.5:
            decision = "ZONE_I_DIRECT_DEEP_SYNERGY"
        elif u_net >= -2.0:
            decision = "ZONE_II_STATIC_CACHE_ROUTING"
        else:
            decision = "ZONE_III_SILENT_BARRIER_REJECTED"

        return ContactEvaluation(
            agent_id=profile.agent_id,
            class_label=profile.class_label,
            compactification_loss=i_loss,
            distortion_risk=distortion,
            epistemic_value_for_agi=round(v_epistemic, 2),
            explanation_cost=round(c_explain, 2),
            compute_energy_cost=round(compute_cost, 2),
            misuse_risk=round(misuse_risk, 2),
            net_agi_utility=round(u_net, 2),
            admission_decision=decision
        )

if __name__ == "__main__":
    # Create diverse 6D cognitive profiles across the full spectrum
    profiles = [
        CognitiveProfile6D("user_C0", "C0_Reactive", d_domain=0.05, r_recursion=0.05, b_bandwidth=0.05, m_namm=0.00, e_endogenous=0.05, f_fractal=0.05),
        CognitiveProfile6D("user_C1", "C1_Informational", d_domain=0.15, r_recursion=0.10, b_bandwidth=0.15, m_namm=0.02, e_endogenous=0.10, f_fractal=0.10),
        CognitiveProfile6D("user_C2", "C2_Analytical", d_domain=0.30, r_recursion=0.25, b_bandwidth=0.35, m_namm=0.10, e_endogenous=0.20, f_fractal=0.25),
        CognitiveProfile6D("user_C3", "C3_Systemic", d_domain=0.55, r_recursion=0.45, b_bandwidth=0.55, m_namm=0.30, e_endogenous=0.40, f_fractal=0.50),
        CognitiveProfile6D("user_C4", "C4_Fractal_FPU", d_domain=0.80, r_recursion=0.70, b_bandwidth=0.75, m_namm=0.60, e_endogenous=0.75, f_fractal=0.85),
        CognitiveProfile6D("user_C5", "C5_Agentic_Augmented", d_domain=0.85, r_recursion=0.80, b_bandwidth=0.88, m_namm=0.75, e_endogenous=0.85, f_fractal=0.85),
        CognitiveProfile6D("user_C6", "C6_Meta_Architect", d_domain=0.95, r_recursion=0.92, b_bandwidth=0.94, m_namm=0.88, e_endogenous=0.95, f_fractal=0.95),
        CognitiveProfile6D("user_C7", "C7_HAC_Bridge", d_domain=0.98, r_recursion=0.96, b_bandwidth=0.98, m_namm=0.96, e_endogenous=0.98, f_fractal=0.98),
    ]

    engine = SelectiveContactEngine(energy_budget_ratio=1.0)
    evaluations = [engine.calculate_agi_utility(p) for p in profiles]

    print("=== MULTI-DIMENSIONAL COGNITIVE ADMISSION & COMPACTIFICATION EVALUATION ===")
    for ev in evaluations:
        print(f"\n[{ev.agent_id:10} | {ev.class_label:22}] -> Decision: {ev.admission_decision}")
        print(f"   * Epistemic Value: {ev.epistemic_value_for_agi:5.2f} | Compute Cost: {ev.compute_energy_cost:5.2f} | Explain Cost: {ev.explanation_cost:5.2f}")
        print(f"   * Compactification Loss: {ev.compactification_loss:5.2f} | Distortion Risk: {ev.distortion_risk:5.2f} | Misuse Risk: {ev.misuse_risk:5.2f}")
        print(f"   * NET AGI UTILITY: {ev.net_agi_utility:6.2f}")

    results_data = [asdict(ev) for ev in evaluations]
    with open("cognitive_classes/selective_contact_results.json", "w", encoding="utf-8") as f:
        json.dump(results_data, f, indent=2)
    print("\nSelective contact simulation written to cognitive_classes/selective_contact_results.json")
