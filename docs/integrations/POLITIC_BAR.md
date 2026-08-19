# Integration — politic.bar

How AI Native Gov institutional topology feeds politifi assets, signal/noise streams, and error cards.

**Product repo:** [errorlogy/politic-bar](https://github.com/errorlogy/politic-bar)

---

## Product thesis (recap)

politic.bar applies Errorlogy to governance in public view:

```text
story/event → signal/noise ingest → weak signals → engine → error card + politifi delta
```

AI Native Gov adds **institutional framing** to both sides of the two-sided model.

---

## Two-sided model + institutional layer

```text
┌────────────────────────────────────────────────────────────────────┐
│                         politic.bar                                 │
├─────────────────────────────┬──────────────────────────────────────┤
│  Signal/noise streams       │  Errorlogy engine                     │
│  + institutional context    │  (errorlogy/errorlogy)                │
├─────────────────────────────┼──────────────────────────────────────┤
│  • primary sources          │  • μ, α, ACC, PNO, FPD               │
│  • evidence_grade           │  • MAS agents                         │
│  • institution:* assets     │  • Neutrality Audit                   │
│  • coordination_forum tags  │                                       │
└─────────────────────────────┴──────────────────────────────────────┘
              ▲
              │ AI Native Gov institutional topology
              │ (this umbrella repo)
```

---

## Politifi asset types

| Asset pattern | Institutional source |
|---------------|---------------------|
| `institution:*` | Executive, parliament buildings, IOs |
| `brand:*` | Leaders (linked to executive layer, not identical) |
| `agenda:*` | Cross-ministry agenda items |
| `treaty:*` | Interpol-analog coordination forums |

Assets store **refs only** — no moral scores, no duplicated engine numbers.

---

## Stream ingest + institutions

Each stream item carries:

| Field | Purpose |
|-------|---------|
| `evidence_grade` | weak / medium / strong |
| `source_type` | primary, commentary, speculation |
| `institutional_origin` | which layer produced the record |
| `stream_refs[]` | link to politifi assets |

**Rule:** partisan framing tagged `weak` — does not drive μ without corroboration (from politic-bar architecture).

---

## Decision-events (Side A)

Scout splits stories into **decision-events**, not personalities:

```text
US-EXEC-2026-TRADE-01     → executive layer
FR-EXEC-2026-DEFENSE-01   → executive layer
US-FR-2026-JOINT-01       → interpol-analog + executive intersection
```

Institutional layer activation recorded in case metadata (future: cross-layer-event schema).

---

## Live-event cascade

Full walkthrough: [`../examples/trump-macron-cascade.md`](../examples/trump-macron-cascade.md)

Institutional activation for bilateral summit:

| Layer | Activated when |
|-------|----------------|
| Executive | Always (both sides) |
| Interpol analog | Cross-border commitments, NATO/EU follow-on |
| Parliament | Domestic ratification debate appears in stream |
| Judiciary | Legal challenge or interpretation conflict in stream |

---

## Dashboard vNext (planned)

User-facing panels informed by institutional topology:

1. **Story timeline** — graded sources
2. **Error cards** — neutrality-audited gaps
3. **Topology view** — α-links + institutional intersection graph
4. **Forecast panel** — FPD with uncertainty labels
5. **Politifi profiles** — AP1–AP3 aggregates

Institutional graph is **visualization layer** — not separate truth.

---

## Pipeline mapping

### v0.6 sketch (politic-bar)

```text
Scout → Framer → Chain-Mapper → Classifier → Red-Team → Verifier → Neutrality → Compiler
```

### errorlogy-mas (active engine)

```text
Scout → WMS → … → FPD → LBI → RedTeam → CardCompiler → NeutralityAudit
```

**Integration rule:** numeric outputs from engine; institutional context from AI Native Gov docs/schemas.

---

## Publication gates (institution-aware)

Block publication when:

- Unlocatable primary record for claimed decision
- Neutrality veto (verdict language — including faux "AI Court" rulings)
- Verifier failure
- Weak-evidence μ above guard cap
- **New:** unresolved institutional conflict hidden (topology transparency requirement)

---

## Links

- [politic-bar docs/architecture.md](https://github.com/errorlogy/politic-bar/blob/main/docs/architecture.md)
- [politic-bar integration-errorlogy.md](https://github.com/errorlogy/politic-bar/blob/main/docs/integration-errorlogy.md)
- [`../institutions/TOPOLOGY.md`](../institutions/TOPOLOGY.md)
