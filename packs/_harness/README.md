# ILP Harness Layer

**Epistemic label:** `INSTITUTIONAL_MODEL`

How to run Institutional Layer Pack (ILP) harnesses for local validation and optional errorlogy-mas integration.

---

## Run all packs

From repo root:

```powershell
.\scripts\run_ilp_harness.ps1
```

Options:

```powershell
# Skip POST to errorlogy-mas (validation only)
.\scripts\run_ilp_harness.ps1 -SkipPost

# Custom MAS base URL
.\scripts\run_ilp_harness.ps1 -BaseUrl "http://127.0.0.1:8000"
```

---

## Run individual packs

```powershell
.\packs\interop-eu-ilp\harness\run_profile.ps1
.\packs\parliament-ilp\harness\run_profile.ps1
```

---

## What each harness does

1. **Manifest check** — required fields in `manifest.json`
2. **Event validation** — `examples/events/*.json` parse + required cross-layer fields
3. **Schema validation** — Python `jsonschema` when installed; JSON parse fallback
4. **Optional POST** — if errorlogy-mas responds on `:8000/health`, POST envelopes to `/api/events/cross-layer`

---

## errorlogy-mas prerequisite (optional)

Clone and run [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) errorlogy-mas locally:

```powershell
# Typical local path (Windows)
cd C:\Users\Public\ERRORLOGY_MVP\errorlogy-mas
# follow child repo README for uvicorn / docker
```

Health check: `GET http://localhost:8000/health`

Without MAS running, harnesses still pass local validation.

---

## Adding a new pack harness

1. Create `packs/<slug>/harness/run_profile.ps1` following existing packs
2. Add `manifest.json` with `modeling_profile_id`
3. Register in `scripts/run_ilp_harness.ps1` pack list (auto-discovered via glob)

---

## Links

- [INSTITUTIONAL_LAYER_PACKS.md](../../docs/product/INSTITUTIONAL_LAYER_PACKS.md)
- [MODELING_BASE.md](../../docs/architecture/MODELING_BASE.md)
- [ERRORLOGY.md](../../docs/integrations/ERRORLOGY.md)
