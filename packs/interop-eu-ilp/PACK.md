# pack:interop-eu-ilp — EU Interop & Anticonsensus

> **INSTITUTIONAL_MODEL** — This pack provides analytical modeling scaffolding only. It does not confer legal authority, electoral mandate, or sovereign standing. Outputs are legitimacy **signals (modeled)**, not verdicts. See [VISION.md](../../VISION.md).

**Pack ID:** `pack:interop-eu-ilp`  
**Modeling profile:** `eu-anticonsensus-settlements-2026`  
**Priority scenario:** [eu-anticonsensus-israel-uk-sanctions-2026.md](../../docs/examples/eu-anticonsensus-israel-uk-sanctions-2026.md)

---

## Scope

Cross-layer event wiring for **EU anticonsensus** contours — member-state divergence that prevents supranational output while national instances act in variable geometry.

Covers:

- `sanctions_coordination` and `discourse_fork_detected` event types
- EU Council ↔ national-instance intersections
- ERRORLOGY / politic-bar integration pointers

Does **not** include μ/α/PNO computation.

---

## Quick start

```powershell
# Validate examples + manifest
.\packs\interop-eu-ilp\harness\run_profile.ps1

# Or run all ILP harnesses
.\scripts\run_ilp_harness.ps1
```

When errorlogy-mas is on `:8000`, the harness POSTs example envelopes to `/api/events/cross-layer`.

---

## Contents

| File | Purpose |
|------|---------|
| [`manifest.json`](manifest.json) | Pack metadata |
| [`topology-slice.md`](topology-slice.md) | EU anticonsensus topology excerpt |
| [`integration.md`](integration.md) | Child-repo wiring |
| [`examples/events/`](examples/events/) | Cross-layer envelope examples |

---

## Links

- [INSTITUTIONAL_LAYER_PACKS.md](../../docs/product/INSTITUTIONAL_LAYER_PACKS.md)
- [MODELING_BASE.md](../../docs/architecture/MODELING_BASE.md)
- [EU_TOPOLOGY.md](../../docs/institutions/EU_TOPOLOGY.md)
- [ERRORLOGY.md](../../docs/integrations/ERRORLOGY.md)
