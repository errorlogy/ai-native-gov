# pack:parliament-ilp — Parliament & Deliberation

> **INSTITUTIONAL_MODEL** — This pack provides analytical modeling scaffolding only. It does not confer legal authority, electoral mandate, or sovereign standing. Outputs are legitimacy **signals (modeled)**, not verdicts. See [VISION.md](../../VISION.md).

**Pack ID:** `pack:parliament-ilp`  
**Modeling profile:** `eu-anticonsensus-settlements-2026`  
**Layer doc:** [parliament.md](../../docs/institutions/parliament.md)

---

## Scope

Parliament-layer starter kit for multi-actor deliberation — parties, coalitions, mandate-gap checks — without claiming legislative authority.

Covers:

- `gov_parliamentary_activity` and `discourse_fork_detected` event types
- Speaker → Party MAS → executive routing
- Dissent ratio and mandate-gap intersection signals

Does **not** include vote prediction or legal verdicts.

---

## Quick start

```powershell
.\packs\parliament-ilp\harness\run_profile.ps1
```

---

## Contents

| File | Purpose |
|------|---------|
| [`manifest.json`](manifest.json) | Pack metadata |
| [`topology-slice.md`](topology-slice.md) | Parliament topology excerpt |
| [`integration.md`](integration.md) | Child-repo wiring |
| [`examples/events/`](examples/events/) | Cross-layer envelope examples |

---

## Links

- [INSTITUTIONAL_LAYER_PACKS.md](../../docs/product/INSTITUTIONAL_LAYER_PACKS.md)
- [AI_PARLIAMENT.md](../../docs/institutions/AI_PARLIAMENT.md)
- [TOPOLOGY.md](../../docs/institutions/TOPOLOGY.md)
