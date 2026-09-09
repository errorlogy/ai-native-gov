# Integration — interop-eu-ilp

**Epistemic label:** `INSTITUTIONAL_MODEL`

---

## errorlogy-mas

| Step | Action |
|------|--------|
| Endpoint | `POST http://localhost:8000/api/events/cross-layer` |
| Activation | [`mas/institutional/activation.py`](https://github.com/errorlogy/errorlogy/tree/main/errorlogy-mas/mas/institutional) |
| Verify | `GET /api/events/cross-layer?story_id=2026-09-settlements-uk-fr-coalition` |

Example body: [`examples/events/2026-09-settlements-uk-fr-coalition.json`](examples/events/2026-09-settlements-uk-fr-coalition.json)

Contract: [ERRORLOGY.md](../../docs/integrations/ERRORLOGY.md)

---

## politic-bar

Stream template (YAML sketch):

```yaml
story_id: "2026-09-settlements-uk-fr-coalition"
stream:
  - source_type: primary
    evidence_grade: strong
    institution_tags:
      - "institution:eu-council"
      - "institution:national-instance"
politifi_assets:
  - "agenda:west-bank-settlements"
  - "institution:eu-council"
  - "institution:uk-fcdo"
epistemic_label: INSTITUTIONAL_MODEL
```

Contract: [POLITIC_BAR.md](../../docs/integrations/POLITIC_BAR.md)

---

## Modeling Base (ISR)

| Artifact | Path |
|----------|------|
| Profile | [`docs/examples/modeling-base/profiles/eu-anticonsensus-settlements-2026.json`](../../docs/examples/modeling-base/profiles/eu-anticonsensus-settlements-2026.json) |
| Seed run | [`docs/examples/modeling-base/runs/2026-09-scenario-a-uk-coalition.json`](../../docs/examples/modeling-base/runs/2026-09-scenario-a-uk-coalition.json) |

Profile declares `institutional_pack_refs: ["pack:interop-eu-ilp", "pack:parliament-ilp"]`.

---

## Schemas (pinned)

- [`cross-layer-event.json`](../../schemas/cross-layer-event.json)
- [`signal-envelope.json`](../../schemas/signal-envelope.json)
- [`modeling-profile.json`](../../schemas/modeling-profile.json)
