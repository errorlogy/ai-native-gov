# Roadmap

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

## Priorities (next 2 weeks)

1. Clone child repos and align integration docs
2. Define `signal-envelope` schema
3. Walk through trump-macron-cascade with real child repo hooks (if available)
