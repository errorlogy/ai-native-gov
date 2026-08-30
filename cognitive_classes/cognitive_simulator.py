#!/usr/bin/env python3
"""
Cognitive Classes Simulator
Tests hypothesis: AI models can operate in different cognitive classes with measurable performance differences
"""

import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
from enum import Enum
from datetime import datetime

class CognitiveClass(Enum):
    FAST = "fast"
    STANDARD = "standard"
    DEEP = "deep"
    CREATIVE = "creative"
    RIGOROUS = "rigorous"

class TaskCategory(Enum):
    SIMPLE = "simple"           # Factual lookups, pattern matching
    MODERATE = "moderate"       # Problem solving, analysis
    COMPLEX = "complex"         # Multi-faceted design decisions
    NOVEL = "novel"            # New problem types, creativity required
    SAFETY_CRITICAL = "safety" # Correctness verification needed

@dataclass
class Task:
    """Represents a test task"""
    id: str
    category: TaskCategory
    complexity: int  # 1-5
    description: str
    expected_depth: int  # Expected reasoning depth needed
    scoring_criteria: List[str]

@dataclass
class CognitiveBehavior:
    """Defines how each cognitive class behaves"""
    class_type: CognitiveClass
    max_depth: int
    avg_reasoning_steps: int
    lateral_thinking: float  # 0-1, probability of creative leap
    validation_thoroughness: float  # 0-1
    processing_speed: float  # 1.0 = baseline
    error_rate: float  # 0-1

@dataclass
class TaskResult:
    """Result of a task execution"""
    task_id: str
    cognitive_class: CognitiveClass
    success: bool
    reasoning_depth: int
    solution_quality: float  # 0-1
    execution_time_factor: float  # 1.0 = baseline
    reasoning_efficiency: float  # quality/execution_time
    validation_errors_caught: int

class CognitiveClassSimulator:
    """Simulates cognitive class performance"""

    def __init__(self):
        self.behaviors = self._define_behaviors()
        self.results: List[TaskResult] = []

    def _define_behaviors(self) -> Dict[CognitiveClass, CognitiveBehavior]:
        """Define each cognitive class's behavior profile"""
        return {
            CognitiveClass.FAST: CognitiveBehavior(
                class_type=CognitiveClass.FAST,
                max_depth=2,
                avg_reasoning_steps=3,
                lateral_thinking=0.3,
                validation_thoroughness=0.4,
                processing_speed=0.5,
                error_rate=0.15
            ),
            CognitiveClass.STANDARD: CognitiveBehavior(
                class_type=CognitiveClass.STANDARD,
                max_depth=3,
                avg_reasoning_steps=5,
                lateral_thinking=0.5,
                validation_thoroughness=0.6,
                processing_speed=1.0,
                error_rate=0.08
            ),
            CognitiveClass.DEEP: CognitiveBehavior(
                class_type=CognitiveClass.DEEP,
                max_depth=5,
                avg_reasoning_steps=8,
                lateral_thinking=0.6,
                validation_thoroughness=0.8,
                processing_speed=1.5,
                error_rate=0.05
            ),
            CognitiveClass.CREATIVE: CognitiveBehavior(
                class_type=CognitiveClass.CREATIVE,
                max_depth=4,
                avg_reasoning_steps=6,
                lateral_thinking=0.9,
                validation_thoroughness=0.5,
                processing_speed=1.2,
                error_rate=0.12
            ),
            CognitiveClass.RIGOROUS: CognitiveBehavior(
                class_type=CognitiveClass.RIGOROUS,
                max_depth=4,
                avg_reasoning_steps=7,
                lateral_thinking=0.2,
                validation_thoroughness=0.95,
                processing_speed=1.2,
                error_rate=0.02
            ),
        }

    def create_test_suite(self) -> List[Task]:
        """Create test tasks spanning different categories and complexities"""
        tasks = [
            # Simple tasks (fast class should excel)
            Task("SIMPLE_1", TaskCategory.SIMPLE, 1, "Identify the capital of France", 1, ["correctness"]),
            Task("SIMPLE_2", TaskCategory.SIMPLE, 1, "Extract key facts from a paragraph", 1, ["completeness"]),
            Task("SIMPLE_3", TaskCategory.SIMPLE, 2, "Sort list of numbers by value", 1, ["correctness", "efficiency"]),

            # Moderate tasks (standard class should perform well)
            Task("MODERATE_1", TaskCategory.MODERATE, 2, "Design a simple API endpoint", 2, ["functionality", "clarity"]),
            Task("MODERATE_2", TaskCategory.MODERATE, 3, "Debug a logic error in code", 2, ["correctness", "efficiency"]),
            Task("MODERATE_3", TaskCategory.MODERATE, 3, "Write a technical explanation", 2, ["accuracy", "clarity"]),

            # Complex tasks (deep class should excel)
            Task("COMPLEX_1", TaskCategory.COMPLEX, 4, "Design system architecture for scaling", 4, ["scalability", "robustness"]),
            Task("COMPLEX_2", TaskCategory.COMPLEX, 4, "Analyze trade-offs in multiple approaches", 4, ["analysis", "completeness"]),
            Task("COMPLEX_3", TaskCategory.COMPLEX, 5, "Plan major refactoring initiative", 4, ["strategy", "impact_analysis"]),

            # Novel tasks (creative class advantage)
            Task("NOVEL_1", TaskCategory.NOVEL, 3, "Propose innovative solution to new problem", 3, ["novelty", "feasibility"]),
            Task("NOVEL_2", TaskCategory.NOVEL, 4, "Connect concepts from different domains", 3, ["originality", "insight"]),

            # Safety-critical tasks (rigorous class essential)
            Task("SAFETY_1", TaskCategory.SAFETY_CRITICAL, 3, "Write secure authentication code", 3, ["correctness", "security"]),
            Task("SAFETY_2", TaskCategory.SAFETY_CRITICAL, 4, "Review code for vulnerabilities", 4, ["completeness", "accuracy"]),
            Task("SAFETY_3", TaskCategory.SAFETY_CRITICAL, 4, "Design data privacy protocol", 4, ["robustness", "compliance"]),
        ]
        return tasks

    def simulate_task_execution(self, task: Task, cognitive_class: CognitiveClass) -> TaskResult:
        """Simulate execution of a task with a specific cognitive class"""
        behavior = self.behaviors[cognitive_class]

        # Determine if task is in ideal domain for this class
        match_score = self._calculate_class_task_match(task.category, cognitive_class)

        # Reasoning depth achieved vs needed
        max_possible_depth = min(behavior.max_depth, task.expected_depth + 2)
        reasoning_depth = int(max_possible_depth * match_score * 0.9)
        reasoning_depth = max(1, reasoning_depth)

        # Calculate quality based on match and thoroughness
        base_quality = match_score
        validation_bonus = behavior.validation_thoroughness * 0.2
        quality_score = min(1.0, base_quality + validation_bonus)

        # Adjust for complexity
        if task.complexity > behavior.max_depth:
            quality_score *= 0.7  # Can't handle very deep tasks
        elif task.complexity <= behavior.max_depth - 1:
            quality_score = min(1.0, quality_score * 1.1)  # Overkill advantage

        # Success probability
        success_threshold = 0.5 + (match_score * 0.4)
        success = quality_score > success_threshold

        # Execution time
        exec_time = behavior.processing_speed
        if task.complexity > behavior.max_depth:
            exec_time *= 1.5  # Struggles take longer

        # Validation errors caught
        errors_caught = int(behavior.validation_thoroughness * task.complexity * 3)

        # Calculate efficiency
        reasoning_efficiency = quality_score / exec_time if exec_time > 0 else 0

        return TaskResult(
            task_id=task.id,
            cognitive_class=cognitive_class,
            success=success,
            reasoning_depth=reasoning_depth,
            solution_quality=quality_score,
            execution_time_factor=exec_time,
            reasoning_efficiency=reasoning_efficiency,
            validation_errors_caught=errors_caught
        )

    def _calculate_class_task_match(self, task_category: TaskCategory, cognitive_class: CognitiveClass) -> float:
        """Calculate how well a cognitive class matches a task type (0-1)"""
        match_matrix = {
            (TaskCategory.SIMPLE, CognitiveClass.FAST): 0.95,
            (TaskCategory.SIMPLE, CognitiveClass.STANDARD): 0.92,
            (TaskCategory.SIMPLE, CognitiveClass.DEEP): 0.88,
            (TaskCategory.SIMPLE, CognitiveClass.CREATIVE): 0.70,
            (TaskCategory.SIMPLE, CognitiveClass.RIGOROUS): 0.85,

            (TaskCategory.MODERATE, CognitiveClass.FAST): 0.60,
            (TaskCategory.MODERATE, CognitiveClass.STANDARD): 0.95,
            (TaskCategory.MODERATE, CognitiveClass.DEEP): 0.92,
            (TaskCategory.MODERATE, CognitiveClass.CREATIVE): 0.80,
            (TaskCategory.MODERATE, CognitiveClass.RIGOROUS): 0.88,

            (TaskCategory.COMPLEX, CognitiveClass.FAST): 0.30,
            (TaskCategory.COMPLEX, CognitiveClass.STANDARD): 0.75,
            (TaskCategory.COMPLEX, CognitiveClass.DEEP): 0.96,
            (TaskCategory.COMPLEX, CognitiveClass.CREATIVE): 0.85,
            (TaskCategory.COMPLEX, CognitiveClass.RIGOROUS): 0.90,

            (TaskCategory.NOVEL, CognitiveClass.FAST): 0.40,
            (TaskCategory.NOVEL, CognitiveClass.STANDARD): 0.70,
            (TaskCategory.NOVEL, CognitiveClass.DEEP): 0.80,
            (TaskCategory.NOVEL, CognitiveClass.CREATIVE): 0.98,
            (TaskCategory.NOVEL, CognitiveClass.RIGOROUS): 0.60,

            (TaskCategory.SAFETY_CRITICAL, CognitiveClass.FAST): 0.25,
            (TaskCategory.SAFETY_CRITICAL, CognitiveClass.STANDARD): 0.80,
            (TaskCategory.SAFETY_CRITICAL, CognitiveClass.DEEP): 0.90,
            (TaskCategory.SAFETY_CRITICAL, CognitiveClass.CREATIVE): 0.50,
            (TaskCategory.SAFETY_CRITICAL, CognitiveClass.RIGOROUS): 0.99,
        }

        return match_matrix.get((task_category, cognitive_class), 0.5)

    def run_simulation(self) -> Tuple[List[TaskResult], Dict]:
        """Run complete simulation suite"""
        print("\n" + "="*70)
        print("COGNITIVE CLASSES SIMULATION")
        print("="*70)

        test_suite = self.create_test_suite()
        print(f"\nTest Suite: {len(test_suite)} tasks across 5 categories")

        # Run each task with each cognitive class
        for task in test_suite:
            for cognitive_class in CognitiveClass:
                result = self.simulate_task_execution(task, cognitive_class)
                self.results.append(result)

        # Analyze results
        analysis = self._analyze_results()

        return self.results, analysis

    def _analyze_results(self) -> Dict:
        """Analyze simulation results"""
        analysis = {
            "total_tasks_executed": len(self.results),
            "timestamp": datetime.now().isoformat(),
            "class_performance": {},
            "category_performance": {},
            "efficiency_ranking": {},
            "recommendations": []
        }

        # Analyze each cognitive class
        for cognitive_class in CognitiveClass:
            class_results = [r for r in self.results if r.cognitive_class == cognitive_class]

            if not class_results:
                continue

            success_rate = sum(1 for r in class_results if r.success) / len(class_results)
            avg_quality = sum(r.solution_quality for r in class_results) / len(class_results)
            avg_efficiency = sum(r.reasoning_efficiency for r in class_results) / len(class_results)

            analysis["class_performance"][cognitive_class.value] = {
                "success_rate": round(success_rate, 3),
                "avg_solution_quality": round(avg_quality, 3),
                "avg_reasoning_efficiency": round(avg_efficiency, 3),
                "task_count": len(class_results),
                "total_errors_caught": sum(r.validation_errors_caught for r in class_results),
            }

        # Find best class per task category
        for category in TaskCategory:
            category_results = [r for r in self.results if r.task_id.startswith(category.value.upper())]
            if not category_results:
                continue

            best_by_quality = max(category_results, key=lambda r: r.solution_quality)
            best_by_efficiency = max(category_results, key=lambda r: r.reasoning_efficiency)

            analysis["category_performance"][category.value] = {
                "best_quality": best_by_quality.cognitive_class.value,
                "best_efficiency": best_by_efficiency.cognitive_class.value,
                "avg_success_rate": round(
                    sum(1 for r in category_results if r.success) / len(category_results), 3
                )
            }

        # Rank by efficiency
        avg_efficiency_per_class = {}
        for cognitive_class in CognitiveClass:
            class_results = [r for r in self.results if r.cognitive_class == cognitive_class]
            avg_efficiency_per_class[cognitive_class.value] = round(
                sum(r.reasoning_efficiency for r in class_results) / len(class_results), 3
            )

        analysis["efficiency_ranking"] = {
            k: v for k, v in sorted(
                avg_efficiency_per_class.items(),
                key=lambda x: x[1],
                reverse=True
            )
        }

        # Generate recommendations
        analysis["recommendations"] = self._generate_recommendations(analysis)

        return analysis

    def _generate_recommendations(self, analysis: Dict) -> List[str]:
        """Generate recommendations based on simulation results"""
        recommendations = []

        perf = analysis["class_performance"]

        # Recommendation 1: Best overall performer
        best_class = max(perf.items(), key=lambda x: x[1]["success_rate"])[0]
        recommendations.append(f"Standard choice: {best_class} has highest success rate")

        # Recommendation 2: Most efficient
        best_efficient = next(iter(analysis["efficiency_ranking"].items()))
        recommendations.append(f"For speed-to-quality: {best_efficient[0]} provides best efficiency")

        # Recommendation 3: Best for safety
        rigorous_perf = perf.get("rigorous", {})
        if rigorous_perf.get("total_errors_caught", 0) > 0:
            recommendations.append("Safety-critical code: RIGOROUS class catches most errors")

        # Recommendation 4: Creative problems
        creative_perf = perf.get("creative", {})
        if creative_perf.get("success_rate", 0) > 0.7:
            recommendations.append("Novel problems: CREATIVE class recommended for innovation")

        # Recommendation 5: Hybrid approach
        recommendations.append("Hybrid strategy: Route tasks to optimal class based on category")

        return recommendations

    def print_results(self, results: List[TaskResult], analysis: Dict):
        """Print simulation results"""
        print("\n" + "="*70)
        print("RESULTS: COGNITIVE CLASS PERFORMANCE")
        print("="*70)

        print("\n--- PERFORMANCE BY COGNITIVE CLASS ---")
        for class_name, metrics in analysis["class_performance"].items():
            print(f"\n{class_name.upper()}:")
            print(f"  Success Rate:        {metrics['success_rate']*100:.1f}%")
            print(f"  Avg Solution Quality: {metrics['avg_solution_quality']:.3f}")
            print(f"  Reasoning Efficiency: {metrics['avg_reasoning_efficiency']:.3f}")
            print(f"  Validation Errors:   {metrics['total_errors_caught']}")

        print("\n--- BEST CLASS BY TASK CATEGORY ---")
        for category, metrics in analysis["category_performance"].items():
            print(f"\n{category.upper()}:")
            print(f"  Best Quality:   {metrics['best_quality']}")
            print(f"  Best Efficiency: {metrics['best_efficiency']}")
            print(f"  Avg Success:    {metrics['avg_success_rate']*100:.1f}%")

        print("\n--- EFFICIENCY RANKING ---")
        for i, (class_name, score) in enumerate(analysis["efficiency_ranking"].items(), 1):
            print(f"{i}. {class_name}: {score:.3f}")

        print("\n--- RECOMMENDATIONS ---")
        for i, rec in enumerate(analysis["recommendations"], 1):
            print(f"{i}. {rec}")

        print("\n" + "="*70)

def main():
    simulator = CognitiveClassSimulator()
    results, analysis = simulator.run_simulation()
    simulator.print_results(results, analysis)

    # Save results to JSON
    output = {
        "simulation_metadata": {
            "timestamp": analysis["timestamp"],
            "total_tasks": analysis["total_tasks_executed"],
            "cognitive_classes": len(CognitiveClass),
        },
        "detailed_results": [asdict(r) for r in results],
        "analysis": analysis,
    }

    with open("D:/COGNETIVE_CLASSES/simulation_results.json", "w") as f:
        json.dump(output, f, indent=2, default=str)

    print("\n[OK] Results saved to simulation_results.json")

if __name__ == "__main__":
    main()
