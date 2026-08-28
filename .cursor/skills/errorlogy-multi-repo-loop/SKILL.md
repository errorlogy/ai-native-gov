---
name: errorlogy-multi-repo-loop
description: >-
  Bounded multi-repo loop for Errorlogy umbrella and sibling repos on Windows.
  Routes contracts to AI_NATIVE_GOV and runtime to child repos. Use when
  executing MVP iterations, Phase B memetic work, cross-repo integration, or
  when the user asks for an errorlogy loop across repos.
---

# Errorlogy Multi-Repo Loop

One bounded iteration per invocation: pick one incomplete task, implement in **one** repo, verify, stop.

## Sibling repo map (Windows)

| Repo | Path | Role |
|------|------|------|
| AI Native Gov (umbrella) | `C:\Users\Public\AI_NATIVE_GOV` | Contracts, topology, integration docs, schemas |
| errorlogy-mas | `C:\Users\Public\ERRORLOGY_MVP\errorlogy-mas` | FastAPI runtime, μ/α engine, institutional activation |
| errorlogy-gui-v2 | `C:\Users\Public\ERRORLOGY_MVP\errorlogy-gui-v2` | Browser UI (Vite/React) |
| politic-bar | `C:\Users\Public\POLITIC_BAR` | Error cards, signal/noise streams, politifi |
| ISA 2.0 | `C:\Users\Public\ISA_2_0` | Institutional–Symbolic Alignment corpus (sibling) |

## Routing rules (from AGENTS.md)

| Change type | Target |
|-------------|--------|
| Integration contracts, institution docs, schemas | `AI_NATIVE_GOV` |
| Engine math, FastAPI routers, adapters | `errorlogy-mas` |
| UI pages, API client | `errorlogy-gui-v2` |
| Stream ingest, half-life, cards | `politic-bar` |
| Cross-repo scenario write-up | `AI_NATIVE_GOV/docs/examples/` |

**Hard constraints:**
- Contracts in umbrella; runtime in child repos — never host product code in umbrella.
- Do **not** copy `errorlogy_unified_taxonomy_v16.json` into umbrella.
- Do not auto-merge politic-bar v0.6 taxonomy with v16.
- Do not invent mode IDs (CB-xxx, PNO-x, HM-xxx).
- Reference child repos via links in `docs/integrations/`, not duplication.

## Bounded loop

```
1. READ   docs/examples/MVP_ITERATIONS.md — find first incomplete iteration slice
2. ROUTE  pick exactly ONE repo from the map above
3. IMPLEMENT  minimal diff for that slice only
4. VERIFY  run applicable checks (see below)
5. STOP   report status; do not auto-continue to next slice unless user asks
```

### Verification by repo

| Repo | Checks |
|------|--------|
| umbrella | Schema JSON valid; cross-links resolve; epistemic labels present |
| errorlogy-mas | `pytest` for touched modules; `GET /api/health`; curl cross-layer endpoints |
| errorlogy-gui-v2 | `npm run build` or lint if UI changed |
| politic-bar | `pytest` or schema validation if ingest stub added |

### Stop conditions

Stop and report when **any** of:
- The chosen slice is done and verified
- Blocked (missing auth, network push failure, ambiguous scope)
- User did not request commit/push
- Next slice belongs to a different repo (hand off, do not chain)

## Git rules

- Commit and push **only when the user asks**
- Never force-push `main` / `master`
- Never add `Co-authored-by` trailers
- No secrets, no `.env` commits
- Warn if working tree dirty before starting

## Phase B memetic pointers

Phase A contracts live in umbrella; Phase B runtime ships in child repos.

| Contour | Umbrella contract | Runtime owner |
|---------|-------------------|---------------|
| Discourse lineage / narrative forks | [`docs/integrations/MEMETIC_DYNAMICS.md`](../../docs/integrations/MEMETIC_DYNAMICS.md) | `errorlogy-mas` — `mas/memetic/discourse_graph.py` |
| Signal/noise half-life | [`schemas/signal-envelope.json`](../../schemas/signal-envelope.json) | `politic-bar` — ingest stub + `decay_tau_hours` indexer |
| EGD+HM bridge, variant edges | cross-layer event types in schema | `errorlogy-mas` thin adapter |
| Narrative fork UI | — | `errorlogy-gui-v2` `/discourse` or panel on `/layers` |

Iteration 4 checklist: see `MVP_ITERATIONS.md` (when present). Cross-link `MEMETIC_DYNAMICS.md`; never claim verdict authority.

## Epistemic labels

Default umbrella outputs to **`INSTITUTIONAL_MODEL`**. Use:

| Label | When |
|-------|------|
| `INSTITUTIONAL_MODEL` | Topology, framing, integration docs |
| `OPERATIONAL` | Adapter output, API responses, computed metrics |
| `COMPUTATIONAL_EVIDENCE` | NAMM certificate-linked only |

Language: analytical contribution, fuzzy membership μ, legitimacy **signals** — never guilty/criminal/proven guilt.

## Native Cursor skills (compose, do not duplicate)

| Skill | Use for |
|-------|---------|
| `loop` | Recurring tick (`/loop 5m …`) in local or cloud sessions |
| `subscribe` | Cloud Agent timer-based wake (via subscriptions MCP) |
| `babysit` | Keep a PR merge-ready: triage comments, fix CI |
| `loop-library` | Audit/design bounded loops; weak checks, stale state, unclear stops |

When chaining work, prefer explicit user `/loop` over autonomous multi-slice runs.
