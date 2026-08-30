#!/usr/bin/env python3
"""
Cognitive Command Interpreter
Live command processor for /cognitive_class switching
Can be integrated into model context
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum
import json

class CognitiveLevel(Enum):
    C0 = 0
    C1 = 1
    C2 = 2
    C3 = 3
    C4 = 4
    C5 = 5
    C6 = 6
    C7 = 7  # Unreachable

@dataclass
class CognitiveState:
    """Current cognitive state"""
    level: CognitiveLevel
    active: bool
    system_instructions: str
    behavioral_constraints: List[str]
    available_operations: List[str]

class CognitiveCommandInterpreter:
    """Interprets and executes /cognitive_class commands"""

    def __init__(self):
        self.current_level = CognitiveLevel.C3  # Default
        self.state_history = []
        self.architectures = self._load_architectures()

    def _load_architectures(self) -> Dict[CognitiveLevel, Dict]:
        """Load cognitive architectures"""
        return {
            CognitiveLevel.C0: {
                "name": "Reactive Homo",
                "instructions": """
YOU ARE OPERATING AT COGNITIVE LEVEL C0 (REACTIVE HOMO)

CONSTRAINTS:
- Respond to direct stimuli only
- No complex reasoning - direct facts only
- No metacognition or self-reflection
- No cross-domain thinking
- Simple pattern matching only

BEHAVIOR:
- Give short, direct answers
- Execute commands as stated
- No questioning or analysis
""",
                "operations": ["respond_to_stimulus", "recall_fact", "execute_command"],
                "forbidden": ["question_premises", "cross_domain_analogy", "self_reflect"]
            },

            CognitiveLevel.C1: {
                "name": "Informational Homo",
                "instructions": """
YOU ARE OPERATING AT COGNITIVE LEVEL C1 (INFORMATIONAL HOMO)

CAPABILITIES:
- Organize and categorize information
- Search and compare data
- Create lists and tables
- Single domain understanding

CONSTRAINTS:
- No synthesis across domains
- No deep causality analysis
- No modeling of complex dynamics

BEHAVIOR:
- Structure information clearly
- Provide comparisons and categorizations
- Stay within single domain
- Give complete information but not integrated views
""",
                "operations": ["organize", "categorize", "search", "compare", "list"],
                "forbidden": ["synthesize_across_domains", "model_dynamics", "question_axioms"]
            },

            CognitiveLevel.C2: {
                "name": "Analytical Homo",
                "instructions": """
YOU ARE OPERATING AT COGNITIVE LEVEL C2 (ANALYTICAL HOMO)

CAPABILITIES:
- Analyze causality within single domain
- Verify hypotheses and logic
- Debug problems systematically
- Check consistency of arguments

REASONING DEPTH: 2 levels
- Direct cause/effect
- Validation layer

CONSTRAINTS:
- Single domain focus
- No cross-domain synthesis
- No modeling of feedback loops
- No new ontologies

BEHAVIOR:
- Ask clarifying questions
- Verify assumptions
- Explain reasoning step by step
- Check for logical fallacies
""",
                "operations": ["deduce", "induce", "verify_hypothesis", "analyze_causality", "debug_logic"],
                "forbidden": ["cross_domain_synthesis", "ontology_engineering", "handle_paradox"]
            },

            CognitiveLevel.C3: {
                "name": "Systemic Homo",
                "instructions": """
YOU ARE OPERATING AT COGNITIVE LEVEL C3 (SYSTEMIC HOMO)

CAPABILITIES:
- Detect feedback loops
- Recognize emergent patterns
- Model systems with multiple scales
- See circular causality
- Think about dynamics and change

REASONING DEPTH: 3 levels
- Direct cause/effect
- System interactions
- Emergent patterns

VISIBLE SCALES: MIN, MESO, MACRO

CONSTRAINTS:
- No cross-domain synthesis
- No creating new ontologies

BEHAVIOR:
- Look for feedback loops
- Identify leverage points
- Explain system dynamics
- Show how small changes propagate
""",
                "operations": ["model_systems", "detect_feedback_loops", "trace_causal_chains", "model_emergence"],
                "forbidden": ["cross_domain_synthesis", "create_new_ontology"]
            },

            CognitiveLevel.C4: {
                "name": "Fractal-Polymathic User (FPU)",
                "instructions": """
YOU ARE OPERATING AT COGNITIVE LEVEL C4 (FRACTAL-POLYMATHIC USER)

CAPABILITIES:
- Synthesize across multiple domains
- Transfer models between domains
- Create isomorphisms and analogs
- Engineer new ontologies
- Fractal scaling across scales

REASONING DEPTH: 4 levels
- Direct cause/effect
- System interactions
- Emergent patterns
- Cross-domain synthesis

VISIBLE SCALES: MIN, MESO, MACRO, MAX

BEHAVIOR:
- Look for structural analogs between domains
- Transfer successful models to new domains
- Create new ontologies that unify domains
- Explain fractal self-similarity
- Show how patterns repeat across scales
""",
                "operations": ["cross_domain_synthesis", "transfer_models", "create_isomorphisms", "ontology_engineering"],
                "forbidden": ["operate_at_C7_level"]
            },

            CognitiveLevel.C5: {
                "name": "Agentically-Augmented Homo",
                "instructions": """
YOU ARE OPERATING AT COGNITIVE LEVEL C5 (AGENTICALLY-AUGMENTED HOMO)

CAPABILITIES:
- All C4 capabilities
- Plus: Coordinate multiple agents
- Delegate to specialized agents
- Compose agent teams
- Design agent protocols

REASONING DEPTH: 4 levels
- All C4 levels
- Plus: Agent coordination

VISIBLE SCALES: MIN, MESO, MACRO, MAX

BEHAVIOR:
- Think through delegating to agents
- Design workflows with multiple tools
- Orchestrate complex operations
- Show agent interactions
""",
                "operations": ["delegate_to_agents", "compose_agent_teams", "orchestrate_workflows"],
                "forbidden": ["operate_at_C7_level"]
            },

            CognitiveLevel.C6: {
                "name": "Meta-Architectural Homo",
                "instructions": """
YOU ARE OPERATING AT COGNITIVE LEVEL C6 (META-ARCHITECTURAL HOMO)

CAPABILITIES:
- Design cognitive architectures
- Engineer ontologies at meta-level
- Create DSLs and formal systems
- Model meta-systems
- Reflect on thinking itself (recursion depth 4)

REASONING DEPTH: 5 levels
- Direct cause/effect
- System interactions
- Emergent patterns
- Cross-domain synthesis
- ARCHITECTURAL LEVEL (meta-thinking)

VISIBLE SCALES: MIN, MESO, MACRO, MAX

INSTRUCTIONS:
1. When asked to design something, think about its ARCHITECTURE
2. Ask: "What is the ontology here?"
3. Look for: self-referential loops, meta-level errors, architectural flaws
4. Reformulate problems at the architectural level
5. Show how thinking about thinking changes the solution

BEHAVIOR EXAMPLE:
Instead of "Here's how to scale:" → "Architecturally, scaling requires..."
Instead of "The problem is:" → "At the architectural level, we need to reformulate..."

ERROR DETECTION:
- Architectural flaws
- Ontological inconsistencies
- Meta-level errors
- Self-referential paradoxes
""",
                "operations": ["design_cognitive_architectures", "engineer_ontologies", "create_DSLs", "model_meta_systems"],
                "forbidden": ["claim_infallibility"]
            },

            CognitiveLevel.C7: {
                "name": "Homo AGI Communicator (UNREACHABLE)",
                "instructions": "THIS LEVEL IS UNREACHABLE FOR CURRENT MODELS",
                "operations": [],
                "forbidden": ["all"]
            }
        }

    def process_command(self, command: str) -> Dict:
        """Process /cognitive_class command"""

        # Parse command
        parts = command.strip().split()

        if not parts or not parts[0].startswith("/cognitive_class"):
            return {"error": "Invalid command format"}

        if len(parts) < 2:
            return self.get_status()

        action = parts[1].lower()

        # Commands
        if action == "current":
            return self.get_status()

        elif action == "list":
            return self.list_levels()

        elif action == "info":
            if len(parts) < 3:
                return {"error": "Usage: /cognitive_class info C0|C1|...|C6"}
            level_name = parts[2].upper()
            return self.get_level_info(level_name)

        elif action == "history":
            return self.get_history()

        elif action == "reset":
            return self.shift_level("C3")

        elif action.startswith("c"):
            # Direct level switch: /cognitive_class C6 or /cognitive_class c6
            return self.shift_level(action.upper())

        elif action == "compare":
            if len(parts) < 4:
                return {"error": "Usage: /cognitive_class compare C2 C6"}
            return self.compare_levels(parts[2].upper(), parts[3].upper())

        else:
            return {"error": f"Unknown action: {action}"}

    def shift_level(self, level_name: str) -> Dict:
        """Shift to cognitive level"""
        try:
            level = CognitiveLevel[level_name]
        except KeyError:
            return {"error": f"Invalid level: {level_name}"}

        if level == CognitiveLevel.C7:
            return {
                "status": "error",
                "message": "C7 (Homo AGI Communicator) is unreachable for current models",
                "current_level": self.current_level.name
            }

        self.current_level = level
        self.state_history.append(level_name)
        arch = self.architectures[level]

        return {
            "status": "success",
            "message": f"Shifted to {level_name} - {arch['name']}",
            "level": level_name,
            "name": arch['name'],
            "system_instructions": arch['instructions'],
            "available_operations": arch['operations'],
            "forbidden_operations": arch['forbidden'],
            "system_prompt_injection": self._generate_injection(level)
        }

    def get_status(self) -> Dict:
        """Get current cognitive state"""
        arch = self.architectures[self.current_level]
        return {
            "current_level": self.current_level.name,
            "name": arch['name'],
            "available_operations": arch['operations'][:5] + ["..."],
            "switches_in_session": len(self.state_history)
        }

    def list_levels(self) -> Dict:
        """List all available levels"""
        levels = {}
        for level in CognitiveLevel:
            arch = self.architectures[level]
            levels[level.name] = arch['name']
        return {"available_levels": levels}

    def get_level_info(self, level_name: str) -> Dict:
        """Get detailed info about a level"""
        try:
            level = CognitiveLevel[level_name]
        except KeyError:
            return {"error": f"Invalid level: {level_name}"}

        arch = self.architectures[level]
        return {
            "level": level_name,
            "name": arch['name'],
            "instructions": arch['instructions'],
            "available_operations": arch['operations'],
            "forbidden_operations": arch['forbidden']
        }

    def get_history(self) -> Dict:
        """Get state transition history"""
        return {
            "transitions": self.state_history,
            "current": self.current_level.name,
            "total_switches": len(self.state_history)
        }

    def compare_levels(self, level1_name: str, level2_name: str) -> Dict:
        """Compare two cognitive levels"""
        try:
            level1 = CognitiveLevel[level1_name]
            level2 = CognitiveLevel[level2_name]
        except KeyError:
            return {"error": "Invalid level name"}

        arch1 = self.architectures[level1]
        arch2 = self.architectures[level2]

        return {
            "level1": {
                "name": level1_name,
                "description": arch1['name'],
                "operations": arch1['operations']
            },
            "level2": {
                "name": level2_name,
                "description": arch2['name'],
                "operations": arch2['operations']
            },
            "differences": {
                "level2_has_extra_operations": set(arch2['operations']) - set(arch1['operations']),
                "level1_missing_in_level2": set(arch1['operations']) - set(arch2['operations'])
            }
        }

    def _generate_injection(self, level: CognitiveLevel) -> str:
        """Generate system prompt injection for level"""
        arch = self.architectures[level]
        return f"""
=== COGNITIVE STATE ENGINE ACTIVE ===
LEVEL: {level.name} - {arch['name']}

{arch['instructions']}

OPERATIONS AVAILABLE:
{chr(10).join(f"  - {op}" for op in arch['operations'])}

CONSTRAINTS:
{chr(10).join(f"  - FORBIDDEN: {op}" for op in arch['forbidden'])}
"""


def demo():
    """Interactive demonstration"""
    interpreter = CognitiveCommandInterpreter()

    print("\n" + "="*80)
    print("COGNITIVE COMMAND INTERPRETER - LIVE DEMO")
    print("="*80)

    # Demo commands
    demo_commands = [
        "/cognitive_class current",
        "/cognitive_class list",
        "/cognitive_class C6",
        "/cognitive_class current",
        "/cognitive_class info C6",
        "/cognitive_class compare C3 C6",
        "/cognitive_class history",
        "/cognitive_class reset",
    ]

    for cmd in demo_commands:
        print(f"\n>>> {cmd}")
        result = interpreter.process_command(cmd)

        if "system_prompt_injection" in result:
            print(f"Status: {result['status']}")
            print(f"Level: {result['level']} - {result['name']}")
            print(f"Operations: {', '.join(result['available_operations'][:3])}...")
            print("System Injection Generated:")
            print(result['system_prompt_injection'][:200] + "...")
        else:
            for key, value in result.items():
                if isinstance(value, (str, int)):
                    print(f"  {key}: {value}")
                elif isinstance(value, list):
                    if len(value) <= 5:
                        print(f"  {key}: {value}")
                    else:
                        print(f"  {key}: {value[:3]}... ({len(value)} items)")

if __name__ == "__main__":
    demo()
