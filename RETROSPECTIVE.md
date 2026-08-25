# Agent Retrospective Checklist (umbrella → child)

This checklist helps agents review prior work and carry insights into `AI_NATIVE_GOV` without breaking context (ownership, taxonomy versions, signal/noise).

## 1) Before you start (required context labeling)

1. Record what exactly was the "previous version":
   - `v0.6 sketch` (often found in politic-bar docs / integrations)
   - or the current "canonical" baseline — `taxonomy v16` (umbrella)
2. Note the likely Phase from `ROADMAP.md`:
   - contract / schema gap → Phase 2
   - routing / ownership gap → Phase 1 or 4
   - new topology layers → Phase 3
3. Build a source list (as links, not as "copy from"):
   - `docs/integrations/POLITIC_BAR.md` (for v0.6 sketch → migrations)
   - `docs/integrations/ERRORLOGY.md` (for v16 / engine binding)
   - (optional) `docs/integrations/NAMM.md` for verification-first math

## 2) During retrospective (reduce signal/noise)

1. Separate invariants from drafts:
   - invariants can move into the umbrella as rules / contracts / interpretations
   - drafts stay in examples / history and do not become the "default"
2. Label the output layer:
   - `INSTITUTIONAL_MODEL` = framing, hypothesis, not a "legal verdict"
   - `OPERATIONAL` / `COMPUTATIONAL_EVIDENCE` = what can be confirmed by computation / certificate
3. If "auto-merge" ideas appear:
   - stop
   - verify that "v0.6 taxonomy" is not being mixed with v16 (forbidden)

## 3) Where to apply insights

### Transfer into `AI_NATIVE_GOV` (umbrella)

- `docs/institutions/` and TOPOLOGY: when institutional topology, intersection tensions, or checks & balances change
- `docs/integrations/`: when the contract / interface between umbrella and child repos changes
- `schemas/`: when a new "stubs / contracts" format appears that child repos must be able to parse
- `docs/examples/`: when you need to describe a migration / cascade "as it happened" without rewriting engine math

### Do not transfer into `AI_NATIVE_GOV`

- engine math / numeric outputs / μ/α/PNO/FPD computation (lives in `errorlogy/errorlogy`)
- UI implementation, politifi rendering, signal stream pipeline code (lives in `errorlogy/politic-bar`)
- verification certificates as verdict (lives in `namm-experiments`; umbrella only gets correct output-type labeling)

## 4) Mini summary note template (one paragraph)

Copy and fill in:

- **Comparison:** `v0.6 sketch` → `taxonomy v16` / or another version pair
- **Phase:** Phase X (`ROADMAP.md`)
- **Ownership change:** what the umbrella now holds vs which child repo owns computation / UI
- **Schema action:** what was updated / should be updated in `schemas/` (or "nothing")
- **Next action:** which doc / example / contract to update and where

## 5) Common anti-patterns (quick self-check)

- Mixing taxonomy versions (v0.6 treated as v16 "by default")
- Treating the umbrella as a replacement for "governments" instead of a reasoning / contract layer
- Copying code from child repos into the umbrella instead of linking / integration contracts
- Using verification as a legal verdict instead of epistemic labels (`COMPUTATIONAL_EVIDENCE`)
