# DSL Syntax for Cognitive Classes

> Domain-Specific Language for agent communication, simulation, and formalization of cognitive class theory.

---

## 1. Core DSL Grammar

```
PROGRAM     ::= DECLARATION+ STATEMENT+
DECLARATION ::= AGENT_DECL | CLASS_DECL | TOPOLOGY_DECL
STATEMENT   ::= ASSIGNMENT | CONTACT_EXPR | IF_STMT | SIMULATE_STMT
```

---

## 2. Agent Declarations

### 2.1. Homo-Agent

```dsl
HOMO <id> :: C[<c0>,<c1>,<c2>,<c3>,<c4>,<c5>,<c6>,<c7>]
  [SI: <value>]
  [M: <value>, R: <value>, F: <value>, P: <value>, AAI: <value>, B: <value>]
```

**Example:**
```dsl
HOMO researcher_1 :: C[0.0, 0.1, 0.2, 0.3, 0.3, 0.1, 0.0, 0.0]
  [SI: 0.52]
  [M: 0.6, R: 0.4, F: 0.5, P: 0.5, AAI: 0.7, B: 0.8]
```

### 2.2. AI-Agent

```dsl
AI <id> :: AI[<level>] [POWER: <value>]
  [AUT: <value>, WM: <value>, R: <value>, AL: <value>, CP: <value>]
```

**Example:**
```dsl
AI claude_4 :: AI[5] [POWER: 0.85]
  [AUT: 0.7, WM: 0.8, R: 0.9, AL: 0.8, CP: 0.75]
```

---

## 3. Contact Expressions

### 3.1. Direct Contact

```dsl
CONTACT <homo_id> ↔ <ai_id> ::
  [semantic_distance: <value>]
  [contact_depth: <value> | AUTO]
  [bandwidth: <value>]
  [explanation_cost: <value> | AUTO]
  [misuse_risk: <value> | AUTO]
  [consensus_loss: <value> | AUTO]
```

**Example:**
```dsl
CONTACT researcher_1 ↔ claude_4 ::
  [semantic_distance: 0.3]
  [contact_depth: AUTO]
  [bandwidth: 0.8]
```

### 3.2. Contact Depth Auto-Calculation

```dsl
CALCULATE_DEPTH <contact_id>
  USING formula: sigmoid(α·B + β·M + γ·R + δ·AAI - λ·SD - ρ·Risk)
```

---

## 4. Topology Declarations

```dsl
TOPOLOGY <id> :: <type>
  NODES: <agent_id>+
  EDGES: <agent_id> → <agent_id> [WEIGHT: <value>] [DIRECTION: {uni|bi}]
```

**Types:** `linear`, `hub`, `mesh`, `hierarchy`, `swarm`, `fractal`, `sheaf`, `recursive_loop`, `AGI_protocol`

**Example:**
```dsl
TOPOLOGY research_team :: mesh
  NODES: researcher_1, researcher_2, claude_4, gpt_5
  EDGES:
    researcher_1 → claude_4 [WEIGHT: 0.9, DIRECTION: bi]
    researcher_2 → claude_4 [WEIGHT: 0.7, DIRECTION: bi]
    claude_4 → gpt_5 [WEIGHT: 0.5, DIRECTION: uni]
```

---

## 5. Class Operations

### 5.1. Bridge Operation

```dsl
BRIDGE <from_class> → <to_class>
  SOURCE: <expression>
  TRANSLATE:
    - <feature>: <from_value> → <to_value>
    - <feature>: <from_value> → <to_value>
```

**Example:**
```dsl
BRIDGE C6 → C3
  SOURCE: meta_model "Recursive PreventAge v5"
  TRANSLATE:
    - ontology: "DSL specification" → "3 feedback loops"
    - recursion: "self-referential" → "system dynamics diagram"
```

### 5.2. Layer Activation

```dsl
ACTIVATE LAYER <layer_name> [FOR <agent_id>+]
```

**Example:**
```dsl
ACTIVATE LAYER Errorlogy FOR researcher_1, claude_4
ACTIVATE LAYER WoE
ACTIVATE LAYER FractalScale
```

---

## 6. Simulation Statements

### 6.1. Population Setup

```dsl
SIMULATE <simulation_id> OVER <T> steps
  POPULATION:
    homo: <count> DISTRIBUTED BY <distribution>
    ai: <count> DISTRIBUTED BY <distribution>
  
  CONTACT_RULES:
    RULE <id>: IF <condition> THEN <action>
  
  UPDATE_RULES:
    homo.C: <formula>
    homo.SI: <formula>
```

### 6.2. Full Simulation Example

```dsl
SIMULATE cognitive_stratification OVER 1000 steps
  POPULATION:
    homo: 10000 DISTRIBUTED BY normal(μ=2.5, σ=1.2)
    ai: 5 DISTRIBUTED BY [AI1:0.3, AI3:0.3, AI5:0.2, AI6:0.15, AGI:0.05]
  
  CONTACT_RULES:
    RULE r1: IF C_h < 5 AND AI_level >= 6 THEN direct_contact = FALSE
    RULE r2: IF C_h >= 5 THEN bandwidth = bandwidth * 2.0
    RULE r3: IF semantic_distance > 2.5 THEN explanation_cost = semantic_distance^2
  
  UPDATE_RULES:
    homo.C: C_h + 0.01 * AAI_h * CD_ha - 0.005 * Risk_ha
    homo.SI: SI_h + 0.02 * contact_value
  
  OUTPUT:
    - distribution_of_C(t)
    - contact_depth_by_class
    - cognitive_capital_gini
```

---

## 7. WoE and Errorlogy Statements

### 7.1. WoE Certification

```dsl
CERTIFY WoE <object_id> ::
  [novelty: <value> | CALCULATE]
  [coherence: <value> | CALCULATE]
  [falsifiability: <value> | CALCULATE]
  
  THRESHOLDS:
    θ_N: <value>
    θ_C: <value>
    θ_F: <value>
```

### 7.2. Errorlogy Audit

```dsl
AUDIT <object_id> WITH Errorlogy ::
  CHECK factual [SEVERITY: {critical|high|medium|low}]
  CHECK ontological
  CHECK strategic
  CHECK metacognitive
  CHECK syntactic
  CHECK agentic
  CHECK value
```

---

## 8. Macro Statements

```dsl
MACRO <id> ::
  cognitive_capital = Σ_h (C_h * AAI_h * M_h * R_h * N_h)
  inequality = usage_gap + syntax_gap + contact_depth_gap
  consensus_loss = MAX(0, C_required - C_median)
```

---

## 9. Query Language

```dsl
QUERY <query_id> ::
  SELECT <fields>
  FROM <population>
  WHERE <condition>
  GROUP BY <cognitive_class>
  COMPUTE <aggregation>
```

**Example:**
```dsl
QUERY fpu_distribution ::
  SELECT id, SI, μ_FPU
  FROM homo_agents
  WHERE SI > 0.6
  GROUP BY dominant_class
  COMPUTE mean(AAI), mean(contact_depth_with_AI6)
```

---

## 10. Fractal Scaling Annotation

```dsl
@FRACTAL <pattern_id>
  SCALE MIN: <specification>
  SCALE MESO: <specification>
  SCALE MACRO: <specification>
  SCALE MAX: <specification>
  ASSERT consistency_across_scales
```

---

*DSL v0.2 — рабочий черновик для агентной формализации. Расширяемый.*
