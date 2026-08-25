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

## Agent Retrospective & Context Rules

This section exists so agents do not drift off context when working with historical versions (v0.6 sketches, taxonomy v16, etc.) and when switching between umbrella and child repositories.

### Multi-repository ownership (who stores which type of knowledge)

AI Native Gov (`ai-native-gov`) is the umbrella / supranational layer for **institutional topology & contracts**. Any "product" implementation (UI, pipelines, math engines) lives in child repositories and should be connected via links, not duplication.

Route by knowledge type:

| Knowledge type | Source (repo) | What to do |
|---|---|---|
| Institutional topology / courts, parliament, interpol framing, intersection tensions, checks & balances | `ai-native-gov` | Add / update docs in `docs/institutions/` and TOPOLOGY |
| Taxonomy v16 and μ/α/PNO/FPD engine math | `errorlogy/errorlogy` | Compute / generate in the child repo; in the umbrella — contracts / outputs only (e.g. `INSTITUTIONAL_MODEL`) |
| Error cards, politifi, signal/noise streams, UI layers | `errorlogy/politic-bar` | Rely on umbrella schema / integration documents |
| Verification-first certificates / Protocol v2 / experiments | `errorlogy/namm-experiments` | Link results in the umbrella; do not replace verifiable artifacts with metaphors |

### Milestones (phase / research-development as checkpoints)

Planned as a sequence Phase 0 → Phase 5 (see `ROADMAP.md`):

1. Phase 0 — umbrella foundation: structure, core docs, baseline topology and integration docs
2. Phase 1 — child repo linkage: verify actual child repository APIs and align shared schemas
3. Phase 2 — schema contracts: define and version ingress/egress (signal-envelope, institutional-output, forecast deltas)
4. Phase 3 — institutional depth: expand layers (ministry stubs) and "machine-readable" topology alongside `TOPOLOGY.md`
5. Phase 4 — pipeline integration: connect umbrella output to error detection / validatable streams in child repos
6. Phase 5 — agent automation: PR templates, lightweight validation scripts, playbooks for typical tasks

Rule: if you find "something unfinished", first record which Phase it resembles, and only then change code / documents.

### When reasoning: context checklist (reduce signal/noise)

Before writing a conclusion / decision:

1. **Ask yourself "which layer?"**
   - `INSTITUTIONAL_MODEL` — umbrella frame / model, not a legal verdict
   - `OPERATIONAL` — only what the child engine / certificate actually computes or confirms
2. **Check the taxonomy version.**
   Use taxonomy v16 in the umbrella. "v0.6" — only as a historical artifact for retrospective (and only in the appropriate context).
3. **Choose schema storage location.**
   - Stubs / contracts: `schemas/` inside the umbrella
   - Parsers / adapters / concrete validation formats: child repos
4. **Do not duplicate knowledge.**
   - Do not copy large JSON / taxonomies into the umbrella (example — `errorlogy_unified_taxonomy_v16.json`).
   - Do not copy product pipeline code into the umbrella.
5. **Reference child repos "as sources", not as copy-paste resources.**
   For links and orientation, update `docs/integrations/` and `docs/examples/` rather than moving architecture into umbrella code.

### Retrospective: how to look back and transfer insights

1. **Find the "comparison point".**
   Usually migrations / sketches: `v0.6 sketch (politic-bar)` → taxonomy v16 (see `docs/integrations/POLITIC_BAR.md` and `docs/integrations/ERRORLOGY.md`).
2. **Preserve invariants, not drafts.**
   - Transfer to umbrella: lessons on ownership, schema, responsibility boundaries, interpretation issues.
   - Do not transfer to umbrella: engine math, UI implementation, "new versions" of taxonomy.
3. **Collect "diff notes" in docs.**
   Better to add a couple of paragraphs in `docs/examples/` or `docs/integrations/` than to change interpretation mid-development.
4. **Verify the insight reaches the right Phase.**
   If the insight is about contracts — that is Phase 2. If about routing / ownership — Phase 1/4.
5. **Preserve epistemic humility.**
   Retrospective is for agent learning, not for "re-asserting" legal / moral verdicts.

### Common failure modes

- Mixing taxonomy versions: v0.6 elements treated as part of taxonomy v16 "by default".
- Using the umbrella as a replacement for "governments": the umbrella is a layer of models / contracts, not a sovereign replacement for real-world institutions.
- Copying code from child repositories into the umbrella instead of contract links.
- Auto-merge politic-bar v0.6 taxonomy with v16 (forbidden — see `Do not` above).
- Attempting to "embed" verification (NAMM certificates) in the umbrella as a legal verdict instead of labeling `COMPUTATIONAL_EVIDENCE`.

### Links (child repos / verification sources)

- umbrella: https://github.com/errorlogy/ai-native-gov
- errorlogy: https://github.com/errorlogy/errorlogy
- politic-bar: https://github.com/errorlogy/politic-bar
- errorlogy.com: https://errorlogy.com
- NAMM: https://github.com/errorlogy/namm-experiments

See also `RETROSPECTIVE.md` (checklist version of these instructions).

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
