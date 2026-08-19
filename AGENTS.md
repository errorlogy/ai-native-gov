# Agent Instructions — AI Native Gov

## Mission

Navigate the **AI Native Gov umbrella** and route work to the correct child repository. This repo holds **vision, institutional topology, and integration contracts** — not product code.

---

## Repository roles

| Question | Go to |
|----------|-------|
| Taxonomy v16, μ/α/PNO/FPD engine | [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) |
| Error cards, politifi, signal/noise streams | [errorlogy/politic-bar](https://github.com/errorlogy/politic-bar) |
| Certificates, Protocol v2, experiments | [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) |
| Institutional layers, topology, checks & balances | **this repo** |

---

## Read order (new agent)

1. [`README.md`](README.md) — scope and child repo map
2. [`VISION.md`](VISION.md) — epistemic humility, non-sovereignty
3. [`ARCHITECTURE.md`](ARCHITECTURE.md) — mermaid diagrams, data flows
4. [`docs/institutions/OVERVIEW.md`](docs/institutions/OVERVIEW.md) — framework
5. [`docs/institutions/TOPOLOGY.md`](docs/institutions/TOPOLOGY.md) — intersections
6. Relevant [`docs/integrations/`](docs/integrations/) for your task

---

## Institutional modeling rules

| Do | Don't |
|----|-------|
| Treat institutions as **reasoning layers** | Claim real-world legal authority |
| Document constraints and counter-institutions | Invent mode IDs (CB-xxx, PNO-x, …) |
| Label outputs `INSTITUTIONAL_MODEL` | Present modeling as verdict |
| Reference Errorlogy engine for numeric outputs | Reimplement μ/α/PNO in umbrella docs |

---

## Language rules (shared with Errorlogy / politic.bar)

| Use | Never use |
|-----|-----------|
| analytical contribution | guilty, criminal |
| fuzzy membership μ | proven guilt |
| legitimacy **signals** (modeled) | legitimate ruler (verdict) |
| institutional framing | sovereign AI government |
| possible / consistent with | "this proves" |

---

## Work routing

```text
Changing engine math        → errorlogy/errorlogy
Changing card schema/UI     → politic-bar
Adding certificate experiment → namm-experiments
New institution layer doc   → ai-native-gov/docs/institutions/
Integration contract update → ai-native-gov/docs/integrations/
Cross-repo scenario         → ai-native-gov/docs/examples/
```

---

## Schemas

Minimal stubs in [`schemas/`](../schemas/):

- `institution-layer-id.json` — institution type identifiers
- `cross-layer-event.json` — event envelope with institutional activation

Extend schemas here; implement parsers in child repos.

---

## Do

- Keep umbrella docs curated (quality over quantity)
- Cross-link child repos instead of copying large JSON
- Update TOPOLOGY.md when adding institutions
- Mark epistemic level on every institutional claim

## Do not

- Commit secrets, `.env`, credentials
- Copy `errorlogy_unified_taxonomy_v16.json` into this repo
- Merge product code from child repos
- Auto-merge politic-bar v0.6 taxonomy with v16

---

## Local clones (Windows)

```powershell
# Umbrella
git clone git@github.com:errorlogy/ai-native-gov.git C:\Users\Public\AI_NATIVE_GOV

# Products (side-by-side)
git clone git@github.com:errorlogy/errorlogy.git C:\Users\Public\ERRORLOGY_MVP
git clone git@github.com:errorlogy/politic-bar.git C:\Users\Public\POLITIC_BAR
git clone git@github.com:errorlogy/namm-experiments.git C:\Users\Public\NAMM
```

---

## Example task: live-event cascade

Follow [`docs/examples/trump-macron-cascade.md`](docs/examples/trump-macron-cascade.md):

1. Anchor event in politic-bar stream model
2. Activate institutional layers (this repo)
3. Run Errorlogy engine on decision-events
4. Update politifi assets
5. Optional NAMM verification link in card metadata

---

## Links

- [errorlogy.com](https://errorlogy.com)
- [politic-bar AGENTS.md](https://github.com/errorlogy/politic-bar/blob/main/AGENTS.md)
- [errorlogy-mas AGENTS.md](https://github.com/errorlogy/errorlogy/blob/main/errorlogy-mas/AGENTS.md) (if present)
