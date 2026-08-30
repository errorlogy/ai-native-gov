# Cognitive Classes Model

## Hypothesis
An AI model can operate in different cognitive classes that vary reasoning depth, approach, and effectiveness. Switching via `/cognitive_class <class>` should produce measurable behavioral differences.

## Defined Cognitive Classes

### 1. **Fast/Tactical** (fast)
- **Characteristics**: Quick decisions, pattern matching, minimal deep analysis
- **Speed**: ~50% of standard
- **Depth**: Shallow - heuristic-based
- **Best for**: Simple problems, rapid iteration, time-constrained decisions
- **Communication**: Terse, direct, action-oriented
- **Analysis depth**: 1-2 levels

### 2. **Standard/Balanced** (standard)
- **Characteristics**: Normal operation, balanced reasoning
- **Speed**: 100% baseline
- **Depth**: Medium - contextual analysis
- **Best for**: General-purpose problem solving
- **Communication**: Clear, structured, proportional
- **Analysis depth**: 2-3 levels

### 3. **Deep/Analytical** (deep)
- **Characteristics**: Comprehensive analysis, multiple angles, exhaustive reasoning
- **Speed**: ~150% of standard (more tokens/time)
- **Depth**: Deep - multi-perspective analysis
- **Best for**: Complex problems, design decisions, research
- **Communication**: Detailed, nuanced, exploring trade-offs
- **Analysis depth**: 4+ levels

### 4. **Creative/Divergent** (creative)
- **Characteristics**: Novel connections, lateral thinking, unconventional solutions
- **Speed**: Variable
- **Depth**: Exploratory
- **Best for**: Ideation, novel problems, breakthrough thinking
- **Communication**: Associative, exploratory, speculative
- **Analysis depth**: Cross-domain synthesis

### 5. **Rigorous/Formal** (rigorous)
- **Characteristics**: Strict logic, formal methods, verification-focused
- **Speed**: ~120% of standard
- **Depth**: Structural - proof-oriented
- **Best for**: Safety-critical code, formal verification, correctness proofs
- **Communication**: Formal, precise, constraint-aware
- **Analysis depth**: Exhaustive validation

## Implementation Plan

1. **Phase 1**: Define class behaviors and decision trees
2. **Phase 2**: Create simulation framework with test cases
3. **Phase 3**: Measure effectiveness metrics
4. **Phase 4**: Analyze results and optimize

## Effectiveness Metrics

- **Task Success Rate**: % of tasks completed correctly
- **Reasoning Efficiency**: Solution quality per token spent
- **Adaptation Speed**: How quickly class finds good approach
- **Error Detection**: False positives/negatives in validation
- **User Satisfaction**: Alignment with expectations

## Current Status
- [ ] Framework designed
- [ ] Simulation system built
- [ ] Test cases created
- [ ] Metrics collected
- [ ] Analysis complete
