# Integration — Errorlogy

How AI Native Gov institutional layers feed the Errorlogy ontology and MAS engine.

**Source of truth for engine:** [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) → `errorlogy-mas/`

---

## Division of labor

| AI Native Gov | Errorlogy |
|---------------|-----------|
| Institutional framing (which layers active) | Observable error objects (gap triplets) |
| Topology intersections | α propagation graph |
| Legitimacy **signals** (modeled) | μ fuzzy membership over 381 modes |
| Checks & balances vocabulary | PNO regime, ACC clusters, FPD forecasts |
| Agent reasoning scaffolding | Deterministic engine + MAS orchestration |

---

## Engine pipeline (reference)

```text
DATA → WMS → μ → α → ACC → PNO → (T4D → CAT) → FPD → LBI → public card
         └──────────── engine (deterministic) ────────────┘
```

Institutional context enters **before and alongside** WMS — not as replacement for μ.

---

## Institutional → Scout mapping

| Institutional output | Scout / case field |
|---------------------|-------------------|
| `decision_owner` (executive) | event jurisdiction + org role |
| `representation_map` (parliament) | `constitutive_roles[]` |
| `jurisdiction_set` (interpol) | cross-border tags |
| `dispute_surfaces` (judiciary) | Red Team seeds |
| `precedent_refs` | α edge proposals |

**Envelope:** [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json) →
`errorlogy-mas` adapter (`mas/institutional/activation.py`).

### Cross-layer API (live stub)

Institutional activation ingress — **no μ/analyze**; framing stub only:

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/events/cross-layer` | Frame & persist cross-layer event |
| `GET` | `/api/events/cross-layer` | List events (`?story_id=`, `?event_type=`, `?limit=`) |
| `GET` | `/api/events/cross-layer/layers` | Valid `institution:*` layer enum |
| `GET` | `/api/events/cross-layer/{event_id}` | Single event |

OpenAPI: `http://127.0.0.1:8000/docs` when `errorlogy-mas` is running.

---

## Institutional → engine layer mapping

| Institution tension | Likely mode families (v16) |
|--------------------|---------------------------|
| Mandate gap (Parliament ↔ Executive) | Vertical asymmetry, EGD |
| Inter-ministry conflict | Horizontal asymmetry |
| Outdated citation | Temporal asymmetry |
| Cross-border info asymmetry | WMS weak signal patterns |
| Unresolved dispute | PNO unstable regime |

Agents must use **existing mode IDs** from taxonomy v16 — no invented CB/SF/MP codes.

---

## Taxonomy formalization gap

From Errorlogy concept notes: ~80–90% of v16 is semantic ontology; engine v1 implements thin formal layer.

AI Native Gov institutional docs are **semantic layer** — they do not close the formalization gap. They provide:

- structured cues for Classifier / LLM agents;
- topology metadata for future α edge typing;
- research queue items for METHODS plugins and calibrated μ.

See ERRORLOGY_MVP Obsidian: "Taxonomy vs Engine — formalization gap".

---

## ACC and institutional contribution

ACC clusters identify **who contributed most to the gap** — mapped to institutional actors, not moral blame:

```text
ACC highlight → ministry:defense + agency:intelligence
Label: analytical contribution to gap (not guilt)
```

Parliament layer absence may appear as ACC contributor: "deliberation channel missing".

---

## FPD under institutional constraints

FPD forecasts near-term governance trajectories. Institutional topology constrains **scenario plausibility**:

- Executive bypass of parliament → higher weight on backlash / reversal scenarios
- Active judiciary dispute → bifurcation in CAT hypothesis
- Cross-border coordination failure → α-linked cards in multiple jurisdictions

FPD numbers remain **`OPERATIONAL`** only from engine — institutional layer adds narrative scenario labels.

---

## NAMM verification (optional)

| Claim type | Verification path |
|------------|---------------------|
| α-graph invariant | NAMM graph certificate experiment |
| FPD holdout | NAMM generative holdout on retrospective corpus |
| Aggregation rule | NAMM meta-operator fixed point |

Label: `COMPUTATIONAL_EVIDENCE` when certificate linked.

---

## Development setup

```powershell
git clone git@github.com:errorlogy/errorlogy.git C:\Users\Public\ERRORLOGY_MVP
cd C:\Users\Public\ERRORLOGY_MVP\errorlogy-mas
python -m pip install -e ".[dev]"
python -m pytest tests/ -v
python examples/run_challenger.py --engine-only
```

---

## Do not

- Duplicate `errorlogy_unified_taxonomy_v16.json` in ai-native-gov
- Treat institutional model as engine input without adapter contract
- Auto-merge politic-bar v0.6 taxonomy slice with v16

---

## Links

- [politic-bar integration-errorlogy](https://github.com/errorlogy/politic-bar/blob/main/docs/integration-errorlogy.md)
- [`../institutions/OVERVIEW.md`](../institutions/OVERVIEW.md)
- [errorlogy.com](https://errorlogy.com)
