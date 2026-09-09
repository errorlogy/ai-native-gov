# Institutional Layer Packs (ILP)

**Epistemic label:** `INSTITUTIONAL_MODEL` — modeling scaffolding only. Not sovereign authority.

Product spec: [docs/product/INSTITUTIONAL_LAYER_PACKS.md](../docs/product/INSTITUTIONAL_LAYER_PACKS.md)

Harness guide: [`_harness/README.md`](_harness/README.md)

---

## Available packs

| Pack ID | Slug | Status |
|---------|------|--------|
| `pack:interop-eu-ilp` | [`interop-eu-ilp/`](interop-eu-ilp/) | Starter — EU anticonsensus cross-layer wiring |
| `pack:parliament-ilp` | [`parliament-ilp/`](parliament-ilp/) | Starter — deliberation & mandate-gap |

---

## Planned packs (Phase 3+)

| Pack ID | Scope |
|---------|-------|
| `pack:executive-ilp` | Cabinet MAS, PM synthesis |
| `pack:judiciary-ilp` | Constraint model, dispute surfaces |
| `pack:electoral-ilp` | Representation maps, mandate-gap checks |
| `pack:central-bank-analog-ilp` | Monetary independence signals |

---

## Quick start

```powershell
# Run all pack harnesses
.\scripts\run_ilp_harness.ps1

# Single pack
.\packs\interop-eu-ilp\harness\run_profile.ps1
```

Priority scenario: [eu-anticonsensus-israel-uk-sanctions-2026.md](../docs/examples/eu-anticonsensus-israel-uk-sanctions-2026.md)

Modeling profile: [`docs/examples/modeling-base/profiles/eu-anticonsensus-settlements-2026.json`](../docs/examples/modeling-base/profiles/eu-anticonsensus-settlements-2026.json)
