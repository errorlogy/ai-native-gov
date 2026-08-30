#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consensus Loss Simulator
Implements Theorem 2: The Limits of Narrative Consensus in Democratic Governance
Simulates:
1. Assembly of N agents with cognitive class distribution F(C)
2. Task complexity C_system vs median consensus C_median
3. Voting aggregation functions (Majority, Supermajority, Unanimous)
4. Dynamic civilizational drift: dC_system/dt > dC_median/dt -> Governance Catastrophe
5. Role of AI6 cognitive extension as a consensus bridge
"""

import random
import json
import statistics
from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class AssemblyDecision:
    task_id: str
    c_system_required: float
    c_median: float
    c_consensus_achieved: float
    consensus_loss: float
    system_error_probability: float
    outcome_status: str

class ConsensusLossSimulator:
    def __init__(self, seed: int = 42):
        random.seed(seed)

    def generate_population(self, size: int = 500, mean_c: float = 2.4, std_c: float = 1.1) -> List[int]:
        """Generates representative population with bounded integer cognitive classes C0-C7."""
        population = []
        for _ in range(size):
            val = round(random.gauss(mean_c, std_c))
            val = max(0, min(7, val))
            population.append(val)
        return population

    def evaluate_task_deliberation(
        self,
        population: List[int],
        c_system: float,
        task_id: str,
        voting_rule: str = "majority",
        ai_extension_active: bool = False,
        ai_class: int = 6
    ) -> AssemblyDecision:
        """Evaluates deliberative assembly on a problem of complexity C_system."""
        c_median = statistics.median(population)
        
        # In narrative consensus, the accepted plan cannot exceed the median level of understanding
        if not ai_extension_active:
            if voting_rule == "majority":
                c_consensus = float(c_median)
            elif voting_rule == "supermajority_two_thirds":
                # 33rd percentile bounds the supermajority
                sorted_pop = sorted(population)
                idx = int(len(sorted_pop) * 0.33)
                c_consensus = float(sorted_pop[idx])
            else: # unanimous
                c_consensus = float(min(population))
        else:
            # AI extension bridges the gap through translation and verifiable constraints
            # The decision matches C_system if within AI reach, while keeping human consensus
            c_consensus = min(c_system, float(ai_class))

        # Consensus loss calculation
        loss = max(0.0, c_system - c_consensus)
        
        # Error probability scales exponentially with consensus loss
        if loss == 0:
            err_prob = 0.02 # baseline noise
            status = "OPTIMAL_COGNITIVE_ALIGNMENT"
        elif loss <= 1.0:
            err_prob = 0.18
            status = "ACCEPTABLE_APPROXIMATION"
        elif loss <= 2.0:
            err_prob = 0.58
            status = "SEVERE_INSTITUTIONAL_ERROR"
        else:
            err_prob = 0.94
            status = "SYSTEMIC_GOVERNANCE_CATASTROPHE"

        return AssemblyDecision(
            task_id=task_id,
            c_system_required=round(c_system, 2),
            c_median=round(c_median, 2),
            c_consensus_achieved=round(c_consensus, 2),
            consensus_loss=round(loss, 2),
            system_error_probability=round(err_prob, 4),
            outcome_status=status
        )

    def simulate_civilizational_drift(self, years: int = 20, initial_c_system: float = 2.0) -> Dict:
        """
        Simulates historical timeline where technology/systems complexity grows exponentially
        while biological human median remains roughly constant (Homo loquens limit).
        """
        timeline = []
        pop = self.generate_population(size=1000, mean_c=2.3, std_c=0.95)
        
        c_sys = initial_c_system
        for y in range(years):
            year_label = 2026 + y
            # System complexity grows by ~0.18 class equivalents per year
            c_sys = min(6.5, c_sys + 0.18)
            
            # Without AI extension
            dec_human = self.evaluate_task_deliberation(
                pop, c_sys, f"crisis_{year_label}", voting_rule="majority", ai_extension_active=False
            )
            # With AI extension (AI Native Gov model)
            dec_augmented = self.evaluate_task_deliberation(
                pop, c_sys, f"crisis_{year_label}", voting_rule="majority", ai_extension_active=True, ai_class=6
            )
            
            timeline.append({
                "year": year_label,
                "c_system": round(c_sys, 2),
                "human_only": {
                    "c_achieved": dec_human.c_consensus_achieved,
                    "loss": dec_human.consensus_loss,
                    "error_prob": dec_human.system_error_probability,
                    "status": dec_human.outcome_status
                },
                "ai_native_gov": {
                    "c_achieved": dec_augmented.c_consensus_achieved,
                    "loss": dec_augmented.consensus_loss,
                    "error_prob": dec_augmented.system_error_probability,
                    "status": dec_augmented.outcome_status
                }
            })

        return {
            "years_simulated": years,
            "population_size": len(pop),
            "timeline": timeline
        }

if __name__ == "__main__":
    sim = ConsensusLossSimulator()
    pop = sim.generate_population(size=500, mean_c=2.3, std_c=1.0)
    
    print("=== POPULATION COGNITIVE DISTRIBUTION (N=500) ===")
    counts = {c: pop.count(c) for c in range(8)}
    for c, count in counts.items():
        bar = "#" * int(count / 5)
        print(f" Class C{c}: {count:3d} ({count/5:4.1f}%) | {bar}")

    print(f"\nPopulation Median: C{statistics.median(pop)}")

    print("\n=== EVALUATING SINGLE TASK (Macro-DeFi Systemic Crisis, C_system=5.0) ===")
    res_human = sim.evaluate_task_deliberation(pop, c_system=5.0, task_id="defi_crisis", ai_extension_active=False)
    print(f"[Human-Only Consensus] C_achieved: {res_human.c_consensus_achieved} | Loss: {res_human.consensus_loss} | Error Prob: {res_human.system_error_probability*100:.1f}% -> {res_human.outcome_status}")

    res_ai = sim.evaluate_task_deliberation(pop, c_system=5.0, task_id="defi_crisis", ai_extension_active=True, ai_class=6)
    print(f"[AI Native Gov Co-Gov] C_achieved: {res_ai.c_consensus_achieved} | Loss: {res_ai.consensus_loss} | Error Prob: {res_ai.system_error_probability*100:.1f}% -> {res_ai.outcome_status}")

    print("\n=== SIMULATING CIVILIZATIONAL COMPLEXITY DRIFT (2026-2035) ===")
    drift_results = sim.simulate_civilizational_drift(years=10, initial_c_system=2.2)
    for step in drift_results["timeline"]:
        print(f"Year {step['year']}: C_sys={step['c_system']:4.2f} | Human Loss={step['human_only']['loss']:4.2f} (Err {step['human_only']['error_prob']*100:4.1f}%) | AI Gov Loss={step['ai_native_gov']['loss']:4.2f} (Err {step['ai_native_gov']['error_prob']*100:4.1f}%)")

    with open("cognitive_classes/consensus_loss_results.json", "w", encoding="utf-8") as f:
        json.dump(drift_results, f, indent=2)
    print("\nConsensus loss results written to cognitive_classes/consensus_loss_results.json")
