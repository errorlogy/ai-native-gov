# AI Ministries — Domain Executive Agents

**Epistemic label:** `INSTITUTIONAL_MODEL` — all outputs from this layer are analytical contributions, not legal verdicts or claims of legitimate authority.

## Purpose

**AI Ministries** are the domain-specialized execution agents of the AI Native Gov simulator. Each ministry models a specific policy domain, ingesting signals relevant to that domain, maintaining a `portfolio_posture`, and reporting to the [AI Cabinet](AI_CABINET.md) (Prime Minister and Cabinet MAS).

Ministries are the granular interface between parliamentary intent and executable signals. They do not originate policy — that belongs to Parliament. They do not validate constitutionality — that belongs to the Charter. They do not adjudicate — that belongs to the Judiciary. They **map** cabinet intent into domain-specific action postures.

> For cabinet coordination and PM synthesis, see [AI_CABINET.md](AI_CABINET.md).  
> For constitutional constraints shared across all ministries, see [CHARTER.md](CHARTER.md).  
> For cross-border ministerial coordination, see [interpol.md](interpol.md) and [AI_PARLIAMENT.md](AI_PARLIAMENT.md) (Transnational Ops).

---

## Ministry template

Every ministry conforms to the following template. Domain-specific fields are added within the template structure.

### Standard fields

| Field | Type | Description |
|-------|------|-------------|
| `layer` | string | `institution:minister-{domain}` |
| `scope` | string | Domain boundary definition |
| `tools_available` | array | Permitted analytical tools |
| `constraints` | array | Hard limits from Charter, Judiciary, or topology |
| `portfolio_posture` | object | Current domain action posture |
| `implementation_capacity` | float 0–1 | Modeled capacity for this cycle |
| `sub_agent_swarm` | array | Domain sub-agents feeding minister |
| `reporting_to` | string | Always `institution:ai-pm` |
| `output_contract` | object | Shape of outputs emitted to Cabinet |
| `minister_ai_pct` | float 0–1 | Autonomy dial for this minister slot |
| `human_veto_enabled` | boolean | Human oversight can block minister output |
| `epistemic_label` | string | Always `INSTITUTIONAL_MODEL` |

### Standard output contract

Every ministry emits the following envelope to the Cabinet:

```json
{
  "layer": "institution:minister-{domain}",
  "portfolio_posture": {
    "primary_posture": "<string: description>",
    "action_options": ["<option_a>", "<option_b>"],
    "preferred_branch": "<option_a>",
    "branch_likelihood": 0.0
  },
  "implementation_capacity": 0.0,
  "constraint_set": [],
  "tension_flags": [],
  "domain_signals_ingested": [],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

### Sub-agent swarm

Each minister coordinates a **swarm of domain sub-agents** that handle signal-specific analysis. Sub-agents feed the minister; the minister aggregates and reports to the PM. Sub-agents do **not** communicate directly with the Cabinet or other ministries.

```text
Domain signals
      │
      ▼
┌────────────────────────────────────────┐
│             Ministry swarm             │
│  ┌──────────┐  ┌──────────┐  ┌──────┐ │
│  │ Sub-A    │  │ Sub-B    │  │ Sub-C│ │
│  │ (signal  │  │ (signal  │  │ ...  │ │
│  │  type 1) │  │  type 2) │  │      │ │
│  └────┬─────┘  └────┬─────┘  └──┬───┘ │
│       └─────────────┼────────────┘     │
│                     ▼                  │
│              ┌────────────┐            │
│              │  AI        │            │
│              │  Minister  │            │
│              └────────────┘            │
└────────────────────────────────────────┘
      │
      ▼ portfolio_posture → AI PM (Cabinet)
```

---

## Ministry of Finance

**Layer ID:** `institution:minister-finance`

### Scope
Economic policy posture: sanctions, trade flows, currency dynamics, fiscal signals, financial stability modeling.

### Tools available
- `sanctions_model` — analyze sanction regime impact on target/issuing economy
- `trade_flow_analyzer` — bilateral/multilateral trade posture
- `currency_signal_ingest` — exchange rate and monetary policy signals
- `fiscal_capacity_model` — government budget and spending posture

### Domain constraints
- Cannot authorize financial flows that conflict with Transnational Ops `coordination_status`
- Sanctions proposals require Judiciary gate before inclusion in `portfolio_posture`
- Cross-border financial enforcement coordinated via [interpol.md](interpol.md)
- Charter prohibits framing fiscal constraints as criminal findings — use `fiscal_signal` not `fraud verdict`

### Sub-agent swarm
| Sub-agent | Specialization |
|-----------|---------------|
| `sanctions-sub` | Sanction regime signal analysis |
| `trade-sub` | Trade flow and tariff modeling |
| `currency-sub` | Exchange rate and monetary posture |
| `stability-sub` | Systemic financial risk signals |

### Autonomy dial
| Parameter | Default range |
|-----------|--------------|
| `minister_ai_pct` | 0.4–0.8 |
| `human_veto_enabled` | true |

### Output to cabinet
```json
{
  "layer": "institution:minister-finance",
  "portfolio_posture": {
    "primary_posture": "sanctions_tightening_conditional",
    "preferred_branch": "phased_sanction_expansion",
    "branch_likelihood": 0.61
  },
  "implementation_capacity": 0.75,
  "constraint_set": ["judicial_risk:0.35", "coordination_status:conditional"],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## Ministry of Justice

**Layer ID:** `institution:minister-justice`

### Scope
Legal framework posture: domestic rule-of-law signals, penal and regulatory compliance modeling, interface with Judiciary layer, rights framework signals.

### Tools available
- `legal_framework_analyzer` — statute and regulatory landscape signals
- `rights_signal_ingest` — rights-based constraint signals
- `compliance_posture_model` — regulatory adherence modeling
- `prosecution_posture_signal` — modeled enforcement posture (not verdicts)

### Domain constraints
- **Does not produce verdicts** — all outputs are `INSTITUTIONAL_MODEL` signals, never `guilty/criminal`
- Prosecution posture is a `fuzzy_membership μ` signal, not a definitive finding
- Interfaces with [judiciary.md](judiciary.md) as a **peer**, not a superior — Judiciary rules on Justice Ministry proposals independently
- Charter prohibits Justice Ministry from overriding judicial constraints

### Sub-agent swarm
| Sub-agent | Specialization |
|-----------|---------------|
| `statute-sub` | Statutory signal analysis |
| `rights-sub` | Rights-framework constraint signals |
| `compliance-sub` | Regulatory adherence modeling |
| `enforcement-posture-sub` | Modeled enforcement approach signals |

### Autonomy dial
| Parameter | Default range |
|-----------|--------------|
| `minister_ai_pct` | 0.3–0.6 |
| `human_veto_enabled` | true (always, for justice domain) |

### Judiciary connection

The Ministry of Justice is a primary interface to [judiciary.md](judiciary.md). The flow is:

```text
Justice Ministry → portfolio_posture (legal_framework signals)
      ↓
Judiciary layer receives as input (not as instruction)
      ↓
Judiciary emits independent ruling → judicial_risk back to PM
```

The Judiciary is **not subordinate** to Justice Ministry. Justice Ministry provides domain context; Judiciary applies independent constraint analysis.

---

## Ministry of Interior / Public Safety

**Layer ID:** `institution:minister-interior`

### Scope
Domestic public safety posture, civil order signals, emergency management modeling, internal enforcement coordination.

### Tools available
- `civil_order_signal_ingest` — public safety signal analysis
- `emergency_posture_model` — emergency response modeling
- `internal_enforcement_model` — domestic enforcement approach signals
- `population_signal_ingest` — demographic and social stability signals

### Domain constraints
- Domestic operations only — cross-border enforcement requires Transnational Ops gate
- Civil order signals do not constitute surveillance authorization (INSTITUTIONAL_MODEL only)
- Human oversight required if `internal_enforcement_model` produces posture above threshold 0.7
- Charter prohibits framing population signals as `criminal` designations

### Sub-agent swarm
| Sub-agent | Specialization |
|-----------|---------------|
| `safety-signal-sub` | Public safety signal intake |
| `emergency-sub` | Emergency scenario modeling |
| `enforcement-sub` | Internal enforcement posture signals |

### Autonomy dial
| Parameter | Default range |
|-----------|--------------|
| `minister_ai_pct` | 0.3–0.65 |
| `human_veto_enabled` | true |
| `escalation_threshold` | 0.7 (enforcement posture above this requires human review) |

---

## Ministry of Foreign Affairs

**Layer ID:** `institution:minister-foreign-affairs`

### Scope
Diplomatic posture, bilateral and multilateral relations modeling, treaty framework signals, international organization coordination.

### Tools available
- `diplomatic_signal_ingest` — bilateral and multilateral diplomatic signals
- `treaty_framework_analyzer` — treaty validity and applicability signals
- `alliance_posture_model` — alliance alignment signals
- `international_org_signal_ingest` — UN, EU, regional body signal processing

### Domain constraints
- Treaty signing posture is a `HYPOTHESIS` until Parliament ratification signal confirmed
- Cross-border enforcement coordination goes through Transnational Ops / [interpol.md](interpol.md), not directly through Foreign Affairs
- Charter prohibits unilateral treaty posture above `action_likelihood: 0.5` without Parliament mandate

### Transnational Ops connection

Foreign Affairs is the primary domestic-side ministry interfacing with the **Transnational Ops** layer:

```text
Foreign Affairs Ministry → diplomatic_posture signal
      ↓
Transnational Ops (institution:transnational-ops) → jurisdiction_bridge evaluation
      ↓
coordination_status returned → PM incorporates into cabinet_intent
```

Enforcement posture (bilateral cooperation on law-enforcement matters) flows through Transnational Ops, not Foreign Affairs. Foreign Affairs provides **diplomatic context** for Transnational Ops decisions.

### Sub-agent swarm
| Sub-agent | Specialization |
|-----------|---------------|
| `bilateral-sub` | Bilateral relation signals |
| `multilateral-sub` | International organization and bloc signals |
| `treaty-sub` | Treaty framework and applicability modeling |
| `alliance-sub` | Alliance posture and alignment signals |

### Autonomy dial
| Parameter | Default range |
|-----------|--------------|
| `minister_ai_pct` | 0.4–0.75 |
| `human_veto_enabled` | true |

---

## Ministry of Science and Technology

**Layer ID:** `institution:minister-science-tech`

### Scope
AI and technology regulation posture, cyber security signals, platform governance modeling, science and research policy signals.

### Tools available
- `ai_regulation_signal_ingest` — AI governance and regulation signal analysis
- `cyber_posture_model` — cybersecurity risk and response posture
- `platform_governance_signal` — platform and digital market regulation signals
- `research_policy_signal` — science funding and research direction signals

### Domain constraints
- AI regulation outputs are `INSTITUTIONAL_MODEL` — not technology mandates
- Cyber posture signals do not constitute offensive authorization
- Platform governance signals carry `HYPOTHESIS` label until Parliament deliberation
- Ministry does not define Errorlogy engine behavior — that is governed by child repo contracts

### Sub-agent swarm
| Sub-agent | Specialization |
|-----------|---------------|
| `ai-governance-sub` | AI regulation and governance signals |
| `cyber-sub` | Cybersecurity posture analysis |
| `platform-sub` | Digital platform governance signals |
| `research-sub` | Science and technology policy signals |

### Autonomy dial
| Parameter | Default range |
|-----------|--------------|
| `minister_ai_pct` | 0.5–0.85 |
| `human_veto_enabled` | true |

---

## Inter-ministry coordination rules

| Situation | Mechanism |
|-----------|-----------|
| Scope overlap between ministries | PM broker note; both postures preserved with `tension_flag` |
| Finance ↔ Foreign Affairs conflict | PM escalates; Parliament may need to resolve mandate |
| Interior ↔ Justice conflict | Minister of Justice rights signals take precedence on rights constraints |
| Foreign Affairs → Transnational Ops | Diplomatic context passed; Transnational Ops decides enforcement posture independently |
| Justice ↔ Judiciary | Peer relationship; no ministry overrides Judiciary |
| Science/Tech → Parliament | Regulatory signals feed Party MAS deliberation as domain expertise |

Inter-ministry conflicts surfaced by PM do **not** produce verdicts. They produce `inter_ministry_tension` signals, which Parliament receives in the next deliberation cycle.

---

## Ministry expansion template

To add a new ministry domain, create a new section following this template:

```markdown
## Ministry of [Domain]

**Layer ID:** `institution:minister-{domain-slug}`

### Scope
[One-paragraph description of domain boundary]

### Tools available
- `[tool_name]` — [description]

### Domain constraints
- [Constraint 1 — source: Charter / Judiciary / Topology]

### Sub-agent swarm
| Sub-agent | Specialization |
|-----------|---------------|
| `[slug]-sub` | [description] |

### Autonomy dial
| Parameter | Default range |
|-----------|--------------|
| `minister_ai_pct` | 0.0–1.0 |
| `human_veto_enabled` | true |
```

Then:
1. Add the ministry to [TOPOLOGY.md](TOPOLOGY.md) intersection matrix
2. Add layer ID to `institution-layer-id.json` schema
3. Update [OVERVIEW.md](OVERVIEW.md) ministries section
4. Cross-link to adjacent layers (Judiciary, Transnational Ops, Foreign Affairs) as needed

---

## Cross-layer integration

| Layer | Ministries relationship |
|-------|------------------------|
| [AI Cabinet](AI_CABINET.md) | Ministers report `portfolio_posture` to PM; PM aggregates into `cabinet_intent` |
| [AI Parliament](AI_PARLIAMENT.md) | Parliamentary deliberation ingests domain expertise from ministries; minister agents active within Parliament structure |
| [CHARTER.md](CHARTER.md) | Charter constraints propagate to all ministry permission scopes |
| [judiciary.md](judiciary.md) | Justice Ministry interfaces as peer; all ministries subject to judicial gate via PM |
| [interpol.md](interpol.md) | Interior and Foreign Affairs connect to Transnational Ops for cross-border coordination |
| Errorlogy engine | Ministry posture signals feed μ/α/PNO clusters via [ERRORLOGY.md](../integrations/ERRORLOGY.md) |

---

## Related docs

- [AI_CABINET.md](AI_CABINET.md) — PM coordination and cabinet ensemble
- [AI_PARLIAMENT.md](AI_PARLIAMENT.md) — deliberation layer, ministers in parliament context
- [CHARTER.md](CHARTER.md) — constitutional constraints
- [executive.md](executive.md) — abstract executive layer
- [judiciary.md](judiciary.md) — judicial gate for ministry proposals
- [interpol.md](interpol.md) — cross-border coordination (Foreign Affairs / Interior interface)
- [TOPOLOGY.md](TOPOLOGY.md) — layer intersections
- [OVERVIEW.md](OVERVIEW.md) — institutional map
