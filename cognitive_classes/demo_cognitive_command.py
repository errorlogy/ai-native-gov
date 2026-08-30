#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cognitive Command Interpreter - Live Demo
Run this locally on your PC to see the system working
"""

class CognitiveLevel:
    levels = {
        "C0": "Reactive Homo - Direct stimulus response",
        "C1": "Informational Homo - Organization and cataloging",
        "C2": "Analytical Homo - Single-domain analysis (2 layers)",
        "C3": "Systemic Homo - Systems thinking (3 layers)",
        "C4": "Fractal-Polymathic - Cross-domain synthesis (4 layers)",
        "C5": "Agentically-Augmented - Coordinate agents (4 layers)",
        "C6": "Meta-Architectural - Design architectures (5 layers)",
        "C7": "AGI Communicator - UNREACHABLE"
    }

    capabilities = {
        "C0": ["respond_to_stimulus", "recall_fact", "execute_command"],
        "C1": ["organize", "categorize", "search", "compare", "list"],
        "C2": ["deduce", "induce", "verify_hypothesis", "analyze_causality"],
        "C3": ["model_systems", "detect_feedback_loops", "trace_causal_chains", "model_emergence"],
        "C4": ["cross_domain_synthesis", "transfer_models", "create_isomorphisms", "ontology_engineering"],
        "C5": ["delegate_to_agents", "compose_agent_teams", "orchestrate_workflows"],
        "C6": ["design_cognitive_architectures", "engineer_ontologies", "create_DSLs", "model_meta_systems", "reflect_on_reflection"],
        "C7": []
    }


class CognitiveCommandInterpreter:
    def __init__(self):
        self.current = "C3"
        self.history = []

    def execute(self, cmd):
        """Process /cognitive_class command"""
        parts = cmd.strip().split()

        if not parts or "/cognitive_class" not in parts[0]:
            return "ERROR: Use format: /cognitive_class C0|C1|...|C6"

        if len(parts) < 2:
            return self.show_current()

        action = parts[1].upper()

        if action == "CURRENT":
            return self.show_current()
        elif action == "LIST":
            return self.list_all()
        elif action == "HISTORY":
            return self.show_history()
        elif action in CognitiveLevel.levels:
            return self.shift_to(action)
        else:
            return f"ERROR: Unknown level or action: {action}"

    def shift_to(self, level):
        """Shift to cognitive level"""
        if level == "C7":
            return f"ERROR: C7 (Homo AGI Communicator) is unreachable for current models\nCurrent level: {self.current}"

        self.history.append(self.current)
        self.current = level

        result = f"\n{'='*80}\n"
        result += f"COGNITIVE STATE SHIFTED TO: {level}\n"
        result += f"{'='*80}\n\n"
        result += f"Level Name: {CognitiveLevel.levels[level]}\n\n"
        result += f"Available Operations:\n"
        for op in CognitiveLevel.capabilities[level]:
            result += f"  • {op}\n"
        result += f"\n{'='*80}\n"

        return result

    def show_current(self):
        """Show current state"""
        result = f"\nCurrent Cognitive Level: {self.current}\n"
        result += f"Description: {CognitiveLevel.levels[self.current]}\n"
        result += f"Available operations: {len(CognitiveLevel.capabilities[self.current])}\n"
        result += f"Transitions in session: {len(self.history)}\n"
        return result

    def list_all(self):
        """List all levels"""
        result = "\nAVAILABLE COGNITIVE LEVELS:\n"
        result += "-" * 80 + "\n"
        for level in ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7"]:
            marker = " [CURRENT]" if level == self.current else ""
            result += f"{level}: {CognitiveLevel.levels[level]}{marker}\n"
        return result

    def show_history(self):
        """Show transition history"""
        result = "\nCognitive State Transition History:\n"
        result += "-" * 80 + "\n"
        if not self.history:
            result += "No transitions yet (still at C3)\n"
        else:
            for i, level in enumerate(self.history, 1):
                result += f"{i}. {level}\n"
        result += f"\nCurrent: {self.current}\n"
        return result


def demo():
    """Run interactive demo"""
    print("\n" + "="*80)
    print("COGNITIVE COMMAND INTERPRETER - LIVE DEMO")
    print("="*80)
    print("\nThis system allows you to shift the model's cognitive state")
    print("through the /cognitive_class command.\n")

    interpreter = CognitiveCommandInterpreter()

    # Demo commands
    demo_commands = [
        ("/cognitive_class current", "Check current state"),
        ("/cognitive_class list", "List all available levels"),
        ("/cognitive_class C6", "Shift to Meta-Architectural level"),
        ("/cognitive_class current", "Check state after shift"),
        ("/cognitive_class C4", "Shift to Fractal-Polymathic level"),
        ("/cognitive_class C2", "Shift to Analytical level"),
        ("/cognitive_class history", "Show transition history"),
        ("/cognitive_class C7", "Try unreachable C7"),
        ("/cognitive_class C3", "Back to default Systemic level"),
    ]

    import sys
    is_interactive = sys.stdin.isatty() and "--non-interactive" not in sys.argv

    for cmd, description in demo_commands:
        print(f"\n>>> {description}")
        print(f"Command: {cmd}")
        print("-" * 80)
        result = interpreter.execute(cmd)
        print(result)
        if is_interactive:
            input("Press Enter to continue...")

    if not is_interactive:
        print("\n[Non-interactive demo complete]")
        return

    print("\n" + "="*80)
    print("INTERACTIVE MODE")
    print("="*80)
    print("\nYou can now enter commands directly.")
    print("Type 'quit' to exit, 'help' for commands\n")

    while True:
        cmd = input(">>> ").strip()

        if cmd.lower() == "quit":
            print("Goodbye!")
            break
        elif cmd.lower() == "help":
            print("\nAvailable commands:")
            print("  /cognitive_class C0-C6        - Shift to level")
            print("  /cognitive_class current      - Show current state")
            print("  /cognitive_class list         - List all levels")
            print("  /cognitive_class history      - Show history")
            print("  quit                          - Exit")
            print()
        elif cmd:
            result = interpreter.execute(cmd)
            print(result)
        else:
            continue


if __name__ == "__main__":
    demo()
