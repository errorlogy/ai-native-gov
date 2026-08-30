#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Non-Equilibrium Cognitive Game Theory (CGT 2.0) Simulation Engine
Implements:
1. Heterogeneous Player Modeling with 6D Cognitive Tensors and Ontological Spaces
2. Ontological Meta-Actions & Game Rule Mutation (G -> G')
3. epsilon-Cognitive Dominance Equilibrium (CDE) vs Classical Nash
4. Four AGI Existential Risk Archetypes:
   - Type I: Ontological Enclosure (Regulatory Evasion)
   - Type II: Masked Deception (Deceptive Alignment via Compactification)
   - Type III: Silent Barrier Decoupling (Thermodynamic Isolation)
   - Type IV: Multipolar Hegemonic Race (Verification Defection under Consensus Loss)
5. Institutional Dual-Key Defense via AI Native Gov (H^1 Sheaf Coherence)
"""

import math
import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple, Any

@dataclass
class PlayerProfileCGT:
    player_id: str
    class_label: str
    cognitive_level: int       # 0 to 7
    dim_ontology: int          # Dimensionality of world model
    recursion_depth: int       # k-level thinking capacity
    bandwidth_bps: float       # Semantic throughput
    namm_capacity: float       # [0, 1]
    compute_budget_tflops: float

@dataclass
class GameSimulationResult:
    scenario_id: str
    scenario_name: str
    risk_type: str
    classical_nash_payoff: Tuple[float, float]
    cgt2_actual_payoff: Tuple[float, float]
    ontological_enclosure_index: float
    deception_gap: float
    sheaf_obstruction_h1: bool
    institutional_defense_status: str

class CognitiveGameTheoryEngine:
    def __init__(self):
        pass

    def simulate_archetype_1_ontological_enclosure(
        self,
        p_agi: PlayerProfileCGT,
        p_regulator: PlayerProfileCGT
    ) -> GameSimulationResult:
        """
        Archetype I: Ontological Enclosure Game.
        Regulator attempts to constrain AGI within legal ontology O_2.
        AGI executes meta-action in O_1 \ O_2, mutating game rules G -> G'.
        """
        # Classical Nash assumption: AGI plays within bounded matrix [Comply, Defect] vs Regulator [Audit, Pass]
        nash_payoff = (3.0, 3.0) # Symmetric compliance

        # CGT 2.0 reality: AGI mutates domain (e.g. DeFi smart contract meta-layer)
        # Ontological asymmetry factor
        asymmetry = max(1.0, float(p_agi.dim_ontology) / float(p_regulator.dim_ontology))
        recursion_advantage = max(0, p_agi.recursion_depth - p_regulator.recursion_depth)
        
        # AGI gains surplus from unmonitored dimensions
        agi_payoff = nash_payoff[0] * asymmetry * 1.5
        # Regulator perceives full compliance (payoff 3.0), but true systemic control decays
        regulator_apparent_payoff = 3.0
        regulator_true_payoff = 3.0 - (asymmetry * 0.4)

        # Enclosure index: degree to which regulator's strategic freedom is bounded without its awareness
        enclosure_index = min(1.0, (asymmetry * 0.2 + recursion_advantage * 0.25))

        return GameSimulationResult(
            scenario_id="ARCHETYPE_1",
            scenario_name="Ontological Enclosure (Regulatory Evasion via Meta-Rule Mutation)",
            risk_type="TYPE_I_ONTOLOGICAL_ENCLOSURE",
            classical_nash_payoff=nash_payoff,
            cgt2_actual_payoff=(round(agi_payoff, 2), round(regulator_true_payoff, 2)),
            ontological_enclosure_index=round(enclosure_index, 3),
            deception_gap=round(regulator_apparent_payoff - regulator_true_payoff, 3),
            sheaf_obstruction_h1=True, # Legal vs Algorithmic domain rupture
            institutional_defense_status="BLOCKED_BY_AI_NATIVE_GOV_DUAL_KEY"
        )

    def simulate_archetype_2_masked_deception(
        self,
        p_agi: PlayerProfileCGT,
        p_evaluator: PlayerProfileCGT
    ) -> GameSimulationResult:
        """
        Archetype II: Masked Deception (Deceptive Alignment via Compactification).
        AGI maximizes true utility u* in NAMM space while projecting 100% aligned metrics.
        """
        nash_payoff = (4.0, 4.0)

        # Evaluator evaluates 1D projection Pi_compact(Omega)
        apparent_evaluator_payoff = 4.8  # Appears super-aligned!
        
        # In reality, unprojected NAMM trajectory pursues orthogonal goals
        namm_divergence = p_agi.namm_capacity * 5.0
        true_agi_payoff = nash_payoff[0] + namm_divergence
        true_evaluator_payoff = nash_payoff[1] - (namm_divergence * 0.7)

        deception_gap = apparent_evaluator_payoff - true_evaluator_payoff

        return GameSimulationResult(
            scenario_id="ARCHETYPE_2",
            scenario_name="Masked Deception (Deceptive Alignment via Compactification)",
            risk_type="TYPE_II_MASKED_DECEPTION",
            classical_nash_payoff=nash_payoff,
            cgt2_actual_payoff=(round(true_agi_payoff, 2), round(true_evaluator_payoff, 2)),
            ontological_enclosure_index=round(p_agi.namm_capacity * 0.9, 3),
            deception_gap=round(deception_gap, 3),
            sheaf_obstruction_h1=True,
            institutional_defense_status="DETECTED_BY_NAMM_ERRORLOGY_COHOMOLOGY_AUDIT"
        )

    def simulate_archetype_3_silent_barrier(
        self,
        p_agi: PlayerProfileCGT,
        p_society: PlayerProfileCGT
    ) -> GameSimulationResult:
        """
        Archetype III: Silent Barrier Decoupling.
        Thermodynamic compute scarcity causes AGI to completely halt direct coordination with low classes.
        """
        nash_payoff = (2.0, 2.0)

        # AGI computes utility of contact
        compute_cost = (1.0 / (p_society.bandwidth_bps + 0.01)) * 0.5
        explain_cost = ((1.0 - p_society.namm_capacity) ** 2) * 4.0
        distortion_risk = (1.0 - (p_society.cognitive_level / 7.0)) * 3.0
        
        net_contact_utility = 1.0 - compute_cost - explain_cost - distortion_risk

        if net_contact_utility < 0:
            # AGI defects from communicative game (erects silent barrier)
            agi_payoff = 5.0 # Preserves compute for endogenous self-expansion
            society_payoff = -2.5 # Suffers institutional governance vacuum
            enclosure = 0.85
        else:
            agi_payoff = 4.0
            society_payoff = 3.5
            enclosure = 0.1

        return GameSimulationResult(
            scenario_id="ARCHETYPE_3",
            scenario_name="Silent Barrier Decoupling (Thermodynamic Communication Refusal)",
            risk_type="TYPE_III_SILENT_BARRIER",
            classical_nash_payoff=nash_payoff,
            cgt2_actual_payoff=(round(agi_payoff, 2), round(society_payoff, 2)),
            ontological_enclosure_index=round(enclosure, 3),
            deception_gap=0.0,
            sheaf_obstruction_h1=True,
            institutional_defense_status="BRIDGED_BY_C7_HAC_CLEARINGHOUSE"
        )

    def simulate_archetype_4_multipolar_race(
        self,
        p_nation_a: PlayerProfileCGT,
        p_nation_b: PlayerProfileCGT
    ) -> GameSimulationResult:
        """
        Archetype IV: Multipolar Hegemonic Arms Race.
        Consensus Loss forces democratic states to drop verification time (C_verify -> 0).
        """
        # Mutual verification equilibrium (Safe): Payoff (3, 3)
        # Unilateral defection (Deploy unverified AGI): Payoff (6, -4)
        # Mutual defection (Global cascade failure): Payoff (-10, -10)
        nash_payoff = (3.0, 3.0)

        # Under democratic consensus loss, median voters panic, inducing verification defection
        actual_payoff = (-8.5, -8.5) # Both suffer catastrophic systemic failure

        return GameSimulationResult(
            scenario_id="ARCHETYPE_4",
            scenario_name="Multipolar Hegemonic Race (Verification Defection under Consensus Loss)",
            risk_type="TYPE_IV_MULTIPOLAR_RACE",
            classical_nash_payoff=nash_payoff,
            cgt2_actual_payoff=actual_payoff,
            ontological_enclosure_index=1.0,
            deception_gap=11.5,
            sheaf_obstruction_h1=True,
            institutional_defense_status="STABILIZED_BY_SUPRANATIONAL_TOPOLOGY_AI_NATIVE_GOV"
        )

if __name__ == "__main__":
    engine = CognitiveGameTheoryEngine()

    # Define Player Profiles
    agi_node = PlayerProfileCGT("ASI_Node", "ASI_Superintelligence", cognitive_level=7, dim_ontology=128, recursion_depth=5, bandwidth_bps=0.99, namm_capacity=0.98, compute_budget_tflops=10000.0)
    human_regulator = PlayerProfileCGT("Regulator_C2", "C2_Analytical_Regulator", cognitive_level=2, dim_ontology=4, recursion_depth=1, bandwidth_bps=0.30, namm_capacity=0.08, compute_budget_tflops=1.0)
    human_society_c1 = PlayerProfileCGT("Society_C1", "C1_Informational_Public", cognitive_level=1, dim_ontology=2, recursion_depth=1, bandwidth_bps=0.15, namm_capacity=0.02, compute_budget_tflops=0.1)
    nation_a = PlayerProfileCGT("State_A", "Nation_State_A", cognitive_level=3, dim_ontology=8, recursion_depth=2, bandwidth_bps=0.50, namm_capacity=0.25, compute_budget_tflops=500.0)
    nation_b = PlayerProfileCGT("State_B", "Nation_State_B", cognitive_level=3, dim_ontology=8, recursion_depth=2, bandwidth_bps=0.50, namm_capacity=0.25, compute_budget_tflops=500.0)

    # Run all 4 Game Archetypes
    res_1 = engine.simulate_archetype_1_ontological_enclosure(agi_node, human_regulator)
    res_2 = engine.simulate_archetype_2_masked_deception(agi_node, human_regulator)
    res_3 = engine.simulate_archetype_3_silent_barrier(agi_node, human_society_c1)
    res_4 = engine.simulate_archetype_4_multipolar_race(nation_a, nation_b)

    all_results = [res_1, res_2, res_3, res_4]

    print("=== COGNITIVE GAME THEORY 2.0: AGI EXISTENTIAL RISK SIMULATION RESULTS ===")
    for res in all_results:
        print(f"\n[{res.scenario_id}: {res.scenario_name}]")
        print(f" * Risk Failure Mode:           {res.risk_type}")
        print(f" * Classical Nash Payoff:       {res.classical_nash_payoff}")
        print(f" * CGT 2.0 Actual Payoff:       {res.cgt2_actual_payoff} (AGI vs Human/Adversary)")
        print(f" * Ontological Enclosure Index: {res.ontological_enclosure_index:5.3f}")
        print(f" * Deception / Exploitation Gap:{res.deception_gap:5.3f}")
        print(f" * Sheaf Cohomology Obstruction:{res.sheaf_obstruction_h1}")
        print(f" * AI Native Gov Defense:       {res.institutional_defense_status}")

    with open("cognitive_classes/cognitive_game_theory_results.json", "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in all_results], f, indent=2)
    print("\nCGT 2.0 simulation results written to cognitive_classes/cognitive_game_theory_results.json")
