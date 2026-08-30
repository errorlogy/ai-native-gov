#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Execution & Verification Suite for Cognitive Classes & Cognitive Economics
Runs all 13 Python modules in cognitive_classes/ and generates a comprehensive report.
"""

import sys
import os
import time
import subprocess
import json
from typing import Dict, List, Any

SCRIPTS_TO_RUN = [
    # 1. Base Cognitive Simulator & Manager
    ("cognitive_simulator.py", "70-Task Multi-Mode Reasoning Simulator"),
    ("cognitive_state_engine.py", "Architectural Cognitive State Restructuring Engine"),
    ("cognitive_command_interpreter.py", "Cognitive Command Interpreter (/cognitive_class C0-C7)"),
    ("demo_cognitive_command.py", "Demo of Cognitive State Transformations"),
    ("hypothesis_testing_simulator.py", "Cognitive State Transition Hypothesis Tester"),
    ("real_world_simulation.py", "Real-World Engineering Problem Solving across C2-C6"),
    
    # 2. Cognitive Economics & Mathematics Suite
    ("cognitive_economics_simulator.py", "Cognitive Capital (Kc) Dynamics & Gini Drift (Theorem 1)"),
    ("topos_sheaf_engine.py", "Topos Theory & Cech Cohomology H^1 Sheaf Gluing Engine (Theorem 3)"),
    ("consensus_loss_simulator.py", "Democratic Consensus Limit & Civilizational Complexity Drift (Theorem 2)"),
    ("dsl_compiler.py", "Cognitive Classes Domain-Specific Language (DSL) Compiler & AST Interpreter"),
    ("embedding_shift_benchmark.py", "Calibrated 3-Sigma Mahalanobis Embedding Shift Benchmark (H1-H6)"),
    ("selective_contact_simulator.py", "6D Cognitive Space & Thermodynamic Contact Gating Engine"),
    ("cognitive_game_theory_engine.py", "Cognitive Game Theory 2.0 (CGT 2.0) & AGI Risk Topology Simulator"),
]

def run_all_tests() -> Dict[str, Any]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    results = []
    total_start_time = time.time()

    print("================================================================================")
    print("      MASTER EXECUTION SUITE: COGNITIVE CLASSES & COGNITIVE ECONOMICS           ")
    print("================================================================================")
    print(f"Base Directory: {base_dir}\n")

    all_passed = True
    for filename, description in SCRIPTS_TO_RUN:
        script_path = os.path.join(base_dir, filename)
        if not os.path.exists(script_path):
            print(f" [MISSING] {filename:35} -> File not found!")
            results.append({
                "script": filename,
                "description": description,
                "status": "MISSING",
                "duration_sec": 0.0,
                "stdout_sample": "",
                "stderr": "File not found"
            })
            all_passed = False
            continue

        print(f"[*] Running: {filename:35} ({description})...", end="", flush=True)
        t0 = time.time()
        proc = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(base_dir)
        )
        duration = round(time.time() - t0, 3)

        if proc.returncode == 0:
            print(f" [ OK ] ({duration}s)")
            status = "PASSED"
        else:
            print(f" [FAIL] ({duration}s) Exit code: {proc.returncode}")
            status = "FAILED"
            all_passed = False

        # Extract last 4 non-empty lines of stdout as summary
        stdout_lines = [l for l in proc.stdout.splitlines() if l.strip()]
        sample = stdout_lines[-4:] if len(stdout_lines) >= 4 else stdout_lines

        results.append({
            "script": filename,
            "description": description,
            "status": status,
            "exit_code": proc.returncode,
            "duration_sec": duration,
            "stdout_summary": sample,
            "stderr": proc.stderr.strip()
        })

    total_duration = round(time.time() - total_start_time, 3)

    summary_report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "total_scripts": len(SCRIPTS_TO_RUN),
        "passed_count": sum(1 for r in results if r["status"] == "PASSED"),
        "failed_count": sum(1 for r in results if r["status"] != "PASSED"),
        "all_passed": all_passed,
        "total_duration_sec": total_duration,
        "results": results
    }

    report_path = os.path.join(base_dir, "ALL_EXECUTIONS_REPORT.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(summary_report, f, indent=2)

    print("\n================================================================================")
    print(f" EXECUTION SUMMARY: {summary_report['passed_count']}/{summary_report['total_scripts']} PASSED in {total_duration}s")
    print(f" Status: {'>>> ALL SUITES VERIFIED AND GREEN <<<' if all_passed else '>>> SOME MODULES FAILED <<<'}")
    print(f" Full JSON report saved to: {report_path}")
    print("================================================================================")

    return summary_report

if __name__ == "__main__":
    run_all_tests()
