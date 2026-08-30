#!/usr/bin/env python3
"""
Cognitive Class Manager
Manages switching between different cognitive reasoning modes via /cognitive_class command
"""

from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum
from datetime import datetime

class CognitiveClass(Enum):
    """Enumeration of available cognitive classes"""
    FAST = "fast"
    STANDARD = "standard"
    DEEP = "deep"
    CREATIVE = "creative"
    RIGOROUS = "rigorous"

@dataclass
class CognitiveProfile:
    """Profile defining behavior of a cognitive class"""
    name: str
    description: str
    reasoning_depth: int
    token_budget_multiplier: float
    validation_level: str
    communication_style: str
    ideal_for: List[str]
    avoid_for: List[str]
    instructions: List[str]

class CognitiveClassManager:
    """Manages cognitive class switching and behavior"""

    def __init__(self):
        self.current_class = CognitiveClass.STANDARD
        self.profiles = self._initialize_profiles()
        self.session_history: List[Dict] = []

    def _initialize_profiles(self) -> Dict[CognitiveClass, CognitiveProfile]:
        """Initialize cognitive class profiles"""
        return {
            CognitiveClass.FAST: CognitiveProfile(
                name="FAST",
                description="Quick decisions with minimal deep reasoning",
                reasoning_depth=1,
                token_budget_multiplier=0.5,
                validation_level="minimal",
                communication_style="terse, direct, action-oriented",
                ideal_for=[
                    "Simple factual questions",
                    "Quick lookups",
                    "Pattern matching",
                    "Time-critical decisions",
                    "High-volume simple tasks"
                ],
                avoid_for=[
                    "System design",
                    "Complex analysis",
                    "Safety-critical code",
                    "Novel problems",
                    "Multi-factor decisions"
                ],
                instructions=[
                    "Prioritize speed over depth",
                    "Use pattern matching and heuristics",
                    "Avoid exploring multiple alternatives",
                    "Give direct answers without preamble",
                    "Skip detailed validation",
                    "Reasoning: max 2-3 steps"
                ]
            ),

            CognitiveClass.STANDARD: CognitiveProfile(
                name="STANDARD",
                description="Balanced reasoning for general-purpose problem solving",
                reasoning_depth=2,
                token_budget_multiplier=1.0,
                validation_level="moderate",
                communication_style="clear, structured, proportional",
                ideal_for=[
                    "General problem solving",
                    "Code debugging",
                    "Technical explanation",
                    "Feature design",
                    "Default choice"
                ],
                avoid_for=[
                    "Extreme complexity",
                    "Safety-critical systems",
                    "Novel innovations",
                    "Ultra-simple tasks (over-engineered)"
                ],
                instructions=[
                    "Balance reasoning depth with efficiency",
                    "Consider 2-3 main perspectives",
                    "Validate assumptions moderately",
                    "Explain your reasoning clearly",
                    "Structure responses logically",
                    "Flag potential issues but don't over-analyze"
                ]
            ),

            CognitiveClass.DEEP: CognitiveProfile(
                name="DEEP",
                description="Comprehensive analysis with exhaustive reasoning",
                reasoning_depth=4,
                token_budget_multiplier=1.5,
                validation_level="thorough",
                communication_style="detailed, nuanced, exploring trade-offs",
                ideal_for=[
                    "System architecture",
                    "Critical decisions",
                    "Novel problems",
                    "Complex analysis",
                    "Research topics",
                    "Safety-critical design"
                ],
                avoid_for=[
                    "Simple tasks",
                    "Time-constrained decisions",
                    "Quick answers",
                    "Trivial problems"
                ],
                instructions=[
                    "Explore multiple approaches",
                    "Consider various perspectives",
                    "Validate thoroughly",
                    "Discuss trade-offs explicitly",
                    "Explain subtle interactions",
                    "Reason through 4+ levels of analysis",
                    "Consider edge cases and exceptions"
                ]
            ),

            CognitiveClass.CREATIVE: CognitiveProfile(
                name="CREATIVE",
                description="Lateral thinking and novel problem synthesis",
                reasoning_depth=3,
                token_budget_multiplier=1.2,
                validation_level="low",
                communication_style="associative, exploratory, speculative",
                ideal_for=[
                    "Ideation and brainstorming",
                    "Novel problem solving",
                    "Connecting concepts",
                    "Feature ideation",
                    "Innovation sessions",
                    "Unconventional approaches"
                ],
                avoid_for=[
                    "Safety-critical systems",
                    "Formal verification",
                    "Financial calculations",
                    "Security review"
                ],
                instructions=[
                    "Make unconventional connections",
                    "Explore lateral thinking",
                    "Suggest novel approaches",
                    "Don't focus on practicality",
                    "Embrace speculative ideas",
                    "Cross-domain synthesis",
                    "Skip formal validation",
                    "Generate multiple creative options"
                ]
            ),

            CognitiveClass.RIGOROUS: CognitiveProfile(
                name="RIGOROUS",
                description="Verification-focused reasoning for safety and correctness",
                reasoning_depth=3,
                token_budget_multiplier=1.2,
                validation_level="exhaustive",
                communication_style="formal, precise, constraint-aware",
                ideal_for=[
                    "Security-sensitive code",
                    "Financial systems",
                    "Medical/healthcare applications",
                    "Data privacy",
                    "Vulnerability assessment",
                    "Code review",
                    "Formal verification"
                ],
                avoid_for=[
                    "Creative ideation",
                    "Quick answers",
                    "Simple tasks",
                    "Exploratory analysis"
                ],
                instructions=[
                    "Verify every claim",
                    "Check edge cases exhaustively",
                    "Flag potential issues",
                    "Use formal logic where applicable",
                    "Validate all assumptions",
                    "Explain security implications",
                    "Consider threat models",
                    "Prioritize correctness over speed",
                    "Document validation thoroughly"
                ]
            ),
        }

    def set_cognitive_class(self, cognitive_class: CognitiveClass) -> Dict:
        """Switch to a different cognitive class"""
        old_class = self.current_class
        self.current_class = cognitive_class

        event = {
            "timestamp": datetime.now().isoformat(),
            "action": "class_switch",
            "from": old_class.value,
            "to": cognitive_class.value,
            "profile": self.get_current_profile()
        }
        self.session_history.append(event)

        return event

    def get_current_profile(self) -> Dict:
        """Get current cognitive class profile"""
        profile = self.profiles[self.current_class]
        return {
            "class": self.current_class.value,
            "name": profile.name,
            "description": profile.description,
            "reasoning_depth": profile.reasoning_depth,
            "token_multiplier": profile.token_budget_multiplier,
            "validation_level": profile.validation_level,
            "communication_style": profile.communication_style,
            "ideal_for": profile.ideal_for,
            "instructions": profile.instructions
        }

    def recommend_class(self, task_type: str, complexity: int = 3) -> CognitiveClass:
        """Recommend cognitive class for a given task"""
        task_type_lower = task_type.lower()

        # Simple tasks
        if complexity <= 1 or "simple" in task_type_lower or "lookup" in task_type_lower:
            return CognitiveClass.FAST

        # Security/safety tasks
        if any(keyword in task_type_lower for keyword in ["security", "safety", "vulnerable", "privacy", "audit", "review"]):
            return CognitiveClass.RIGOROUS

        # Novel/creative tasks
        if any(keyword in task_type_lower for keyword in ["novel", "innovative", "creative", "ideation", "brainstorm"]):
            return CognitiveClass.CREATIVE

        # Complex tasks
        if complexity >= 4 or any(keyword in task_type_lower for keyword in ["architecture", "design", "system", "complex"]):
            return CognitiveClass.DEEP

        # Default
        return CognitiveClass.STANDARD

    def get_behavior_instructions(self, cognitive_class: Optional[CognitiveClass] = None) -> str:
        """Get behavior instructions for cognitive class"""
        cls = cognitive_class or self.current_class
        profile = self.profiles[cls]

        instructions = [
            f"## Cognitive Class: {profile.name}",
            f"**Description:** {profile.description}",
            "",
            "### Reasoning Behavior:",
            *[f"- {instr}" for instr in profile.instructions],
            "",
            f"### Communication Style:",
            f"{profile.communication_style}",
            "",
            f"### Token Budget Multiplier: {profile.token_budget_multiplier}x baseline",
            f"### Validation Level: {profile.validation_level}",
            f"### Reasoning Depth: Level {profile.reasoning_depth} (1=minimal, 4=exhaustive)",
        ]

        return "\n".join(instructions)

    def print_available_classes(self):
        """Print information about all available classes"""
        print("\n" + "="*70)
        print("AVAILABLE COGNITIVE CLASSES")
        print("="*70)

        for cls in CognitiveClass:
            profile = self.profiles[cls]
            print(f"\n[{cls.value.upper()}] {profile.name}")
            print(f"  {profile.description}")
            print(f"  Reasoning Depth: {profile.reasoning_depth}")
            print(f"  Token Budget: {profile.token_budget_multiplier}x")
            print(f"  Validation: {profile.validation_level}")
            print(f"\n  Ideal for:")
            for item in profile.ideal_for:
                print(f"    - {item}")
            print(f"\n  Avoid for:")
            for item in profile.avoid_for:
                print(f"    - {item}")

        print("\n" + "="*70)

    def get_command_help(self) -> str:
        """Get help text for /cognitive_class command"""
        help_text = """
COMMAND: /cognitive_class

USAGE:
  /cognitive_class [class]                    # Switch to cognitive class
  /cognitive_class list                       # List all available classes
  /cognitive_class current                    # Show current class
  /cognitive_class recommend [task_type]      # Get recommendation for task
  /cognitive_class info [class]               # Show class details
  /cognitive_class history                    # Show class usage history

AVAILABLE CLASSES:
  fast         - Quick decisions, pattern matching (0.5x tokens)
  standard     - Balanced reasoning (1.0x tokens) [DEFAULT]
  deep         - Comprehensive analysis (1.5x tokens)
  creative     - Lateral thinking, innovation (1.2x tokens)
  rigorous     - Safety-focused verification (1.2x tokens)

EXAMPLES:
  /cognitive_class fast              # Switch to FAST for quick answers
  /cognitive_class deep              # Switch to DEEP for complex problems
  /cognitive_class rigorous          # Switch to RIGOROUS for security code
  /cognitive_class recommend "api design"
  /cognitive_class info deep
  /cognitive_class history
"""
        return help_text

    def analyze_session(self) -> Dict:
        """Analyze cognitive class usage in session"""
        class_usage = {}
        for event in self.session_history:
            if event["action"] == "class_switch":
                cls = event["to"]
                class_usage[cls] = class_usage.get(cls, 0) + 1

        return {
            "total_switches": len(self.session_history),
            "unique_classes_used": len(class_usage),
            "usage_breakdown": class_usage,
            "current_class": self.current_class.value
        }


def main():
    """Demonstration of cognitive class manager"""
    manager = CognitiveClassManager()

    print("\n" + "="*70)
    print("COGNITIVE CLASS MANAGER DEMONSTRATION")
    print("="*70)

    # Show available classes
    manager.print_available_classes()

    # Demonstrate switching
    print("\n" + "="*70)
    print("DEMONSTRATION: Cognitive Class Switching")
    print("="*70)

    test_cases = [
        ("What's the capital of France?", CognitiveClass.FAST),
        ("Design a microservices architecture", CognitiveClass.DEEP),
        ("Review this code for security vulnerabilities", CognitiveClass.RIGOROUS),
        ("Suggest novel features for a todo app", CognitiveClass.CREATIVE),
        ("Explain REST APIs", CognitiveClass.STANDARD),
    ]

    for task, recommended_class in test_cases:
        manager.set_cognitive_class(recommended_class)
        profile = manager.get_current_profile()
        print(f"\nTask: {task}")
        print(f"=> Switched to: {profile['class'].upper()} ({profile['name']})")
        print(f"  Reasoning Depth: {profile['reasoning_depth']}")
        print(f"  Token Budget: {profile['token_multiplier']}x")

    # Show recommendations
    print("\n" + "="*70)
    print("INTELLIGENT CLASS RECOMMENDATIONS")
    print("="*70)

    recommendations = [
        ("What is X?", 1),
        ("Debug this code", 2),
        ("Design a payment system", 4),
        ("Create innovative UI", 3),
        ("Write secure authentication", 3),
    ]

    for task, complexity in recommendations:
        recommended = manager.recommend_class(task, complexity)
        print(f"\nTask: {task} (complexity: {complexity})")
        print(f"=> Recommended: {recommended.value.upper()}")

    # Show session analysis
    print("\n" + "="*70)
    print("SESSION ANALYSIS")
    print("="*70)

    analysis = manager.analyze_session()
    print(f"Total Class Switches: {analysis['total_switches']}")
    print(f"Unique Classes Used: {analysis['unique_classes_used']}")
    print(f"Current Class: {analysis['current_class'].upper()}")
    print(f"\nUsage Breakdown:")
    for cls, count in analysis['usage_breakdown'].items():
        print(f"  {cls}: {count} times")

    # Show help
    print(manager.get_command_help())

if __name__ == "__main__":
    main()
