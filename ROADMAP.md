# Roadmap

## Research specifications (published)

- [`cognitive_classes/`](cognitive_classes/) — Proto-AGI cognitive classes theory, simulators, and benchmarks (`RESEARCH_SPECIFICATION`; epistemic status `INSTITUTIONAL_MODEL`, not legal or sovereignty claims)
- [`paper_templates/`](paper_templates/) + [`scripts/arxiv_toolkit/`](scripts/arxiv_toolkit/) — arXiv preprint pipeline for cognitive-classes research

## Phase 0 — Umbrella foundation ✅ (current)

- [x] `AI_NATIVE_GOV` workspace structure
- [x] Core docs: README, WORKSPACE, VISION, ARCHITECTURE, REPOS, AGENTS
- [x] Institution docs: parliament, executive, judiciary, interpol, topology
- [x] Integration docs: Errorlogy, politic.bar, NAMM
- [x] Example cascade: Trump–Macron
- [x] Cursor rules for agent context
- [x] Private GitHub repo `errorlogy/ai-native-gov`

## Phase 1 — Child repo linkage

- [ ] Clone `errorlogy` and `politic-bar` into `repos/`
- [ ] Verify integration docs match actual child repo APIs
- [ ] Initial shared schemas in `schemas/` (signal envelope, institutional output)

## Phase 2 — Schema contracts

- [ ] `schemas/signal-envelope.json` — ingress format
- [ ] `schemas/institutional-output.json` — layer output format
- [ ] `schemas/forecast-patch.json` — Errorlogy forecast delta
- [ ] Versioning policy documented

## Phase 3 — Institutional depth

- [ ] Ministry stubs (defense, finance, climate, tech)
- [ ] Topology graph (machine-readable) alongside TOPOLOGY.md
- [ ] Additional cascade examples (2–3 scenarios)

## Phase 4 — Pipeline integration

- [ ] Errorlogy consumes institutional outputs per contract
- [ ] politic.bar publishes validated politifi streams
- [ ] NAMM experimental ingress path documented and tested

## Phase 5 — Agent automation

- [ ] Cross-repo PR templates linking umbrella + child changes
- [ ] Optional: lightweight validation script for schema conformance
- [ ] Agent playbooks for common tasks (topology update, new integration)

## Global AI governance simulator (cross-cutting)

World-scale framing: national AI instances → regional blocs → planned global coordination layer. Master doc: [`docs/institutions/GLOBAL_AI_GOVERNANCE.md`](docs/institutions/GLOBAL_AI_GOVERNANCE.md).

| Stage | Deliverable | Phase alignment |
|-------|-------------|-----------------|
| **A — EU reference bloc** | 27 national profiles, EU supranational topology, collision taxonomy, mermaid schema | Phase 3 ✅ (docs) |
| **B — Regional bloc stubs** | ASEAN, AU, Mercosur shells reusing EU two-tier template | Phase 3 |
| **C — Global coordination layer** | `GLOBAL_LAYER` role IDs, bloc-to-bloc collision paths, global charter stub | Phase 3 → 4 |
| **D — Cross-cutting ingress** | Fin-crypto and other adapters routing to multi-jurisdiction layers | Phase 4 |
| **E — World-scale scenarios** | 2–3 cascades spanning national + regional + integration ingress | Phase 3–4 |
| **F — Agent playbooks** | Topology update, new bloc stub, heterogeneous dial orchestration | Phase 5 |

### Checklist (rolling)

- [x] EU topology, schema, and member-state docs ([EU_TOPOLOGY.md](docs/institutions/EU_TOPOLOGY.md), [EU_SCHEMA.md](docs/institutions/EU_SCHEMA.md), [EU_STATES.md](docs/institutions/EU_STATES.md))
- [x] Global framing doc ([GLOBAL_AI_GOVERNANCE.md](docs/institutions/GLOBAL_AI_GOVERNANCE.md))
- [ ] `schemas/state-profile.json` validated against EU_STATES fields
- [ ] ASEAN / AU / Mercosur bloc stub docs (minimal)
- [ ] `GLOBAL_LAYER` entries in `schemas/institution-layer-id.json`
- [ ] Fin-crypto adapter MVP wired to institutional framer ([FIN_CRYPTO_MARKETS.md](docs/integrations/FIN_CRYPTO_MARKETS.md))
- [ ] World-scale cascade example (e.g. market shock → EU + US national instances)

Human involvement remains **per-country** via `autonomy_dials` and `ai_readiness_level`; the simulator does not claim sovereignty at any tier (`INSTITUTIONAL_MODEL` only).

## Priorities (next 2 weeks)

1. Clone child repos and align integration docs
2. Define `signal-envelope` schema
3. Walk through trump-macron-cascade with real child repo hooks (if available)
4. Validate `state-profile.json` against EU_STATES; sketch first ASEAN bloc stub
