#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cognitive Economics Simulator
Models:
1. Dynamic growth of Cognitive Capital (Kc) with Matthew effect (Theorem 1)
2. Bifurcation threshold Kc* and stratification divergence
3. Cognitive Gini Coefficient G_Kc(t)
4. Explanation costs C_explain between cognitive classes
5. Consensus loss dynamics (Theorem 2)
"""

import math
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple

@dataclass
class HomoAgent:
    agent_id: str
    cognitive_class: int  # 0 to 7
    aai: float            # Agentic AI integration [0, 1]
    metacognition: float  # [0, 1]
    recursion: int        # [1, 5]
    network_capital: float # [0, 1]
    kc: float             # Cognitive Capital

class CognitiveEconomicsEngine:
    def __init__(
        self,
        alpha: float = 0.15,     # Learning / synthesis rate
        gamma: float = 1.35,     # Non-linear synergy coefficient (> 1 -> Matthew effect)
        delta: float = 0.05,     # Depreciation / entropy decay rate
        k_max: float = 1000.0,   # Maximum capacity
        kappa: float = 2.5,      # Explanation cost multiplier
        lambda_gap: float = 1.8  # Syntax gap penalty multiplier
    ):
        self.alpha = alpha
        self.gamma = gamma
        self.delta = delta
        self.k_max = k_max
        self.kappa = kappa
        self.lambda_gap = lambda_gap

    def calculate_bifurcation_threshold(self, aai: float) -> float:
        """Calculates critical capital threshold Kc* below which decay dominates."""
        if self.gamma <= 1.0 or aai <= 0:
            return 0.0
        effective_alpha = self.alpha * aai
        if effective_alpha <= 0:
            return float('inf')
        return (self.delta / effective_alpha) ** (1.0 / (self.gamma - 1.0))

    def d_kc_dt(self, kc: float, aai: float) -> float:
        """Rate of change of cognitive capital."""
        if kc <= 0:
            return 0.0
        growth = self.alpha * aai * (kc ** self.gamma) * (1.0 - kc / self.k_max)
        depreciation = self.delta * kc
        return growth - depreciation

    def calculate_explanation_cost(self, c_source: int, c_target: int, syntax_gap: float) -> float:
        """Calculates cost to explain model from source class to target class."""
        diff = float(c_source - c_target)
        if diff <= 0:
            # Explaining downwards is costly, explaining upwards or equal is baseline verification
            return self.kappa * 0.2 + self.lambda_gap * syntax_gap
        return self.kappa * (diff ** 2) + self.lambda_gap * syntax_gap

    def calculate_gini(self, values: List[float]) -> float:
        """Calculates Gini coefficient for a distribution."""
        n = len(values)
        if n == 0:
            return 0.0
        sorted_vals = sorted(values)
        total = sum(sorted_vals)
        if total == 0:
            return 0.0
        cumulative = 0.0
        gini_sum = 0.0
        for i, val in enumerate(sorted_vals, 1):
            cumulative += val
            gini_sum += (2 * i - n - 1) * val
        return gini_sum / (n * total)

    def simulate_population(self, agents: List[HomoAgent], timesteps: int = 50, dt: float = 0.1) -> Dict:
        """Simulates time evolution of cognitive capital across heterogeneous population."""
        history = []
        for t_step in range(timesteps):
            current_time = round(t_step * dt, 2)
            kc_snapshot = []
            
            for agent in agents:
                # Update capital
                dkc = self.d_kc_dt(agent.kc, agent.aai) * dt
                agent.kc = max(0.1, min(self.k_max, agent.kc + dkc))
                kc_snapshot.append(agent.kc)

            gini = self.calculate_gini(kc_snapshot)
            avg_kc = sum(kc_snapshot) / len(kc_snapshot)
            
            history.append({
                "time": current_time,
                "gini": round(gini, 4),
                "mean_kc": round(avg_kc, 2),
                "agents_kc": [round(a.kc, 2) for a in agents]
            })

        return {
            "timesteps": timesteps,
            "dt": dt,
            "final_gini": history[-1]["gini"],
            "initial_gini": history[0]["gini"],
            "history": history
        }

if __name__ == "__main__":
    # Create representative population: C0 to C6
    population = [
        HomoAgent("agent_C0", cognitive_class=0, aai=0.05, metacognition=0.1, recursion=1, network_capital=0.1, kc=5.0),
        HomoAgent("agent_C1", cognitive_class=1, aai=0.15, metacognition=0.2, recursion=1, network_capital=0.2, kc=12.0),
        HomoAgent("agent_C2", cognitive_class=2, aai=0.30, metacognition=0.3, recursion=1, network_capital=0.3, kc=25.0),
        HomoAgent("agent_C3", cognitive_class=3, aai=0.50, metacognition=0.5, recursion=2, network_capital=0.5, kc=45.0),
        HomoAgent("agent_C4", cognitive_class=4, aai=0.70, metacognition=0.7, recursion=3, network_capital=0.7, kc=75.0),
        HomoAgent("agent_C5", cognitive_class=5, aai=0.85, metacognition=0.8, recursion=3, network_capital=0.85, kc=120.0),
        HomoAgent("agent_C6", cognitive_class=6, aai=0.95, metacognition=0.92, recursion=4, network_capital=0.95, kc=200.0),
    ]

    engine = CognitiveEconomicsEngine(alpha=0.12, gamma=1.30, delta=0.04)
    
    print("=== COGNITIVE CAPITAL THRESHOLDS ===")
    for agent in population:
        threshold = engine.calculate_bifurcation_threshold(agent.aai)
        status = "EXPONENTIAL GROWTH" if agent.kc > threshold else "DECAY / STAGNATION"
        print(f"[{agent.agent_id} (Class {agent.cognitive_class})] Kc: {agent.kc:5.1f} | Kc* Threshold: {threshold:5.1f} -> Status: {status}")

    print("\n=== EXPLANATION COST MATRIX (From -> To) ===")
    for src in [2, 4, 6]:
        for tgt in [0, 2, 4]:
            syntax_gap = abs(src - tgt) * 0.25
            cost = engine.calculate_explanation_cost(src, tgt, syntax_gap)
            print(f"C{src} -> C{tgt} : Explanation Cost = {cost:6.2f}")

    print("\n=== SIMULATING POPULATION STRATIFICATION (50 STEPS) ===")
    results = engine.simulate_population(population, timesteps=30, dt=0.2)
    print(f"Initial Gini: {results['initial_gini']} -> Final Gini: {results['final_gini']}")
    print("Final Capital by Agent:")
    for a in population:
        print(f" - {a.agent_id} (C{a.cognitive_class}): {a.kc:6.2f}")

    with open("cognitive_classes/cognitive_economics_simulation_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("\nResults written to cognitive_classes/cognitive_economics_simulation_results.json")
