# Institutional Layer Packs (ILP)

**Epistemic label:** `INSTITUTIONAL_MODEL` — downloadable starter bundles for AI-assisted governance **simulation and integration**. Not sovereign authority, not a replacement government, not a legal framework.

**Status:** Phase 2–3 starter packs (Sep 2026). See [ROADMAP.md](../../ROADMAP.md).

Tagline: *"Model institutions. Don't claim them."*

---

## 1. What is an ILP?

An **Institutional Layer Pack (ILP)** is a curated, sovereignty-agnostic starter kit that wires a slice of AI Native Gov topology into child repositories:

| Consumer | Role |
|----------|------|
| **ai-native-gov** (umbrella) | Topology slice, schemas, example envelopes, harness |
| **errorlogy-mas** | Cross-layer activation stubs (`POST /api/events/cross-layer`) |
| **politic-bar** | Stream templates keyed by `story_id` |

ILPs do **not** contain engine math (μ/α/PNO). Numeric outputs stay in [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy).

---

## 2. Pack layout

Each pack is a self-contained directory under `packs/`:

```text
packs/<pack-slug>/
├── PACK.md                 # Scope, disclaimer, quick start
├── manifest.json           # Machine-readable pack metadata
├── topology-slice.md       # Excerpt from docs/institutions/ for this pack
├── integration.md          # Child-repo wiring (ERRORLOGY, POLITIC_BAR)
├── examples/events/*.json  # cross-layer-event.json examples
└── harness/
    └── run_profile.ps1     # Local validation + optional POST to errorlogy-mas
```

### manifest.json (required fields)

| Field | Description |
|-------|-------------|
| `pack_id` | Stable ID, e.g. `pack:interop-eu-ilp` |
| `pack_slug` | Directory slug, e.g. `interop-eu-ilp` |
| `institution_layers` | Default layer IDs activated by this pack |
| `schema_refs` | Pinned umbrella schema `$id` URLs |
| `min_errorlogy_ref` | Minimum errorlogy-mas git ref or semver |
| `modeling_profile_id` | Link to ISR profile in `docs/examples/modeling-base/` |
| `epistemic_label` | Default label (always `INSTITUTIONAL_MODEL` for packs) |

---

## 3. First-wave packs

| Pack ID | Slug | Scope | Priority scenario |
|---------|------|-------|-------------------|
| `pack:interop-eu-ilp` | `interop-eu-ilp` | Cross-layer events, EU anticonsensus, signal-envelope wiring | [eu-anticonsensus-israel-uk-sanctions-2026.md](../examples/eu-anticonsensus-israel-uk-sanctions-2026.md) |
| `pack:parliament-ilp` | `parliament-ilp` | Deliberation, party-coalition, mandate-gap checks | Same scenario (Scenarios A & B) |

**Planned (Phase 3+):** `pack:executive-ilp`, `pack:judiciary-ilp`, `pack:electoral-ilp`, `pack:central-bank-analog-ilp`.

Index: [`packs/README.md`](../../packs/README.md)

---

## 4. Modeling Base (ISR) integration

ILPs link to the [Institutional Scenario Registry (ISR)](../architecture/MODELING_BASE.md) via `modeling_profile_id` in each manifest.

| Artifact | Path |
|----------|------|
| Architecture | [`docs/architecture/MODELING_BASE.md`](../architecture/MODELING_BASE.md) |
| Schemas | [`schemas/modeling-profile.json`](../../schemas/modeling-profile.json), [`modeling-run.json`](../../schemas/modeling-run.json), [`modeling-result.json`](../../schemas/modeling-result.json) |
| Seed profile | [`docs/examples/modeling-base/profiles/eu-anticonsensus-settlements-2026.json`](../examples/modeling-base/profiles/eu-anticonsensus-settlements-2026.json) |
| Self-improve playbook | [`docs/playbooks/MODELING_SELF_IMPROVE.md`](../playbooks/MODELING_SELF_IMPROVE.md) |

Profiles declare `institutional_pack_refs[]` pointing back to ILP `pack_id` values.

---

## 5. Harness layer

Run all pack harnesses from the repo root:

```powershell
.\scripts\run_ilp_harness.ps1
```

Per-pack harness:

```powershell
.\packs\interop-eu-ilp\harness\run_profile.ps1
.\packs\parliament-ilp\harness\run_profile.ps1
```

See [`packs/_harness/README.md`](../../packs/_harness/README.md) for details.

When errorlogy-mas is running on `:8000`, harness scripts POST example envelopes to `/api/events/cross-layer`. Otherwise they validate JSON locally.

---

## 6. Mandatory disclaimer (every PACK.md)

> **INSTITUTIONAL_MODEL** — This pack provides analytical modeling scaffolding only. It does not confer legal authority, electoral mandate, or sovereign standing. Outputs are legitimacy **signals (modeled)**, not verdicts. See [VISION.md](../../VISION.md).

---

## 7. Distribution

**MVP:** Monorepo `packs/` folder in [ai-native-gov](https://github.com/errorlogy/ai-native-gov). Pack version tracks umbrella git tag.

**Phase 4+:** Optional GitHub template repos per pack; validation in CI via `scripts/run_ilp_harness.ps1`.

---

## 8. Example workflow — EU anticonsensus

1. Install `pack:interop-eu-ilp` + `pack:parliament-ilp` (clone umbrella; paths already present)
2. Load ISR profile `eu-anticonsensus-settlements-2026`
3. Run harness: `.\scripts\run_ilp_harness.ps1`
4. POST envelopes to errorlogy-mas when runtime available
5. Seed politic.bar stream from `integration.md` templates

No pack claims EU legal authority — only **modeled** layer activation.

---

## Links

- [VISION.md](../../VISION.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [TOPOLOGY.md](../institutions/TOPOLOGY.md)
- [ERRORLOGY.md](../integrations/ERRORLOGY.md)
- [POLITIC_BAR.md](../integrations/POLITIC_BAR.md)
- [MODELING_BASE.md](../architecture/MODELING_BASE.md)
- [eu-anticonsensus-israel-uk-sanctions-2026.md](../examples/eu-anticonsensus-israel-uk-sanctions-2026.md)

---

*Public product spec — feedback via umbrella issues.*
