# Integration — parliament-ilp

**Epistemic label:** `INSTITUTIONAL_MODEL`

---

## errorlogy-mas

| Step | Action |
|------|--------|
| Endpoint | `POST http://localhost:8000/api/events/cross-layer` |
| Event types | `gov_parliamentary_activity`, `discourse_fork_detected` |
| Default layers | `parliament`, `party-coalition`, `executive` |

Example: [`examples/events/2026-09-uk-commons-settlements-debate.json`](examples/events/2026-09-uk-commons-settlements-debate.json)

---

## politic-bar

```yaml
story_id: "2026-09-settlements-discourse-fork"
stream:
  - stream_item_id: "2026-09-08-miliband-commons-settlements"
    source_type: primary
    evidence_grade: strong
    memetic_metrics:
      platform_contour: uk-parliamentary-record
politifi_assets:
  - "brand:miliband"
epistemic_label: OPERATIONAL
```

Signal envelope contract: [POLITIC_BAR.md](../../docs/integrations/POLITIC_BAR.md)

---

## Composed with interop-eu-ilp

Parliament-ilp handles deliberation slices; interop-eu-ilp handles EU Council cross-layer wiring. Both reference profile `eu-anticonsensus-settlements-2026`.

```powershell
.\scripts\run_ilp_harness.ps1
```

---

## Schemas (pinned)

- [`cross-layer-event.json`](../../schemas/cross-layer-event.json)
- [`signal-envelope.json`](../../schemas/signal-envelope.json)
