# Playbook — Modeling Self-Improve Loop

**Epistemic label:** `INSTITUTIONAL_MODEL` — agent procedure for bounded profile refinement. Not autonomous sovereignty or verdict authority.

**Related:** [`docs/architecture/MODELING_BASE.md`](../architecture/MODELING_BASE.md) · [`RETROSPECTIVE.md`](../../RETROSPECTIVE.md) · [errorlogy-multi-repo-loop skill](../../.cursor/skills/errorlogy-multi-repo-loop/SKILL.md)

---

## When to use

- After executing a modeling profile against errorlogy-mas, gui-v2, or cognitive_classes harness
- When a scenario doc (e.g. eu-anticonsensus) reveals missing layers or intersections
- When comparing a new run to baseline and quality flags fail

**One iteration per agent invocation** unless user explicitly chains (`/loop` or repeated ask).

---

## Loop steps

| Step | Action | Output artifact |
|------|--------|-----------------|
| 1. **Observe** | Run profile: `POST /api/events/cross-layer` or load seed envelope | Harness response |
| 2. **Capture** | Write `modeling_run.json`; derive `modeling_result` with quality flags | Run + result records |
| 3. **Compare** | Diff `activated_layers_union` and intersections vs `baseline_run_id` | `delta_vs_baseline` |
| 4. **Propose** | Draft patch using routing table below | PR diff or retrospective note |
| 5. **Verify** | JSON Schema validate; pytest; cross-links resolve | Green checks |
| 6. **Stop** | Report status; hand off if next slice is different repo | Status message |

### Stop conditions

Stop immediately when:

- Verification fails (schema, pytest, broken links)
- Next action belongs to a different repo (hand off — do not chain)
- Scope ambiguous (ask user)
- User did not request commit/push

---

## Routing table — what to update

| Observation | Update target | Repo | Phase |
|-------------|---------------|------|-------|
| Wrong or missing `activated_layers` for `event_type` | `mas/institutional/activation.py` route table | errorlogy-mas | 4 |
| Profile `default_activated_layers` outdated vs scenario doc | `modeling_profile` + scenario doc | ai-native-gov | 2–3 |
| New intersection tension type | `TOPOLOGY.md` / `EU_TOPOLOGY.md` | ai-native-gov | 3 |
| New institution layer ID needed | `schemas/institution-layer-id.json` + activation enum | ai-native-gov → sync child | 2–3 |
| Engine μ/α/PNO values wrong or missing | Errorlogy engine / analyze pipeline | errorlogy-mas | 4 |
| Stream half-life / memetic metrics | politic-bar indexer | politic-bar | 4 |
| UI map does not highlight layers | gui-v2 `/layers` | errorlogy-gui-v2 | 4 |
| NAMM certificate available | Add `certificate_ref`; upgrade label | namm-experiments + umbrella schema note | 4 |
| Taxonomy version confusion (v0.6 vs v16) | Retrospective note only — **do not merge** | ai-native-gov | 1 |
| Research simulator output linkage | `engine_ref` on run; no math in umbrella | ai-native-gov + cognitive_classes | 3 |

---

## Profile patch vs topology vs engine

```text
Quality flag failed?
│
├─ layers_match_profile = false
│   ├─ Stub routing wrong?        → errorlogy-mas activation.py
│   └─ Profile definition wrong?  → modeling_profile.json (umbrella)
│
├─ intersections_captured = false
│   └─ Topology doc gap?          → docs/institutions/*.md
│
├─ engine_not_run = true
│   └─ Expected — do NOT patch profile with fake μ/α
│       → Route to errorlogy analyze when user requests engine run
│
└─ publication_blocker = true
    └─ Retrospective note + epistemic_constraints on profile
```

---

## Retrospective note template

Save to `docs/examples/modeling-base/retrospectives/` or append to result `retrospective_refs`:

```markdown
## Retrospective — {run_id}

- **Comparison:** {prior state} → {new state}
- **Phase:** Phase X (ROADMAP.md)
- **Ownership:** {umbrella | errorlogy-mas | politic-bar}
- **Schema action:** {none | modeling-profile patch | institution-layer-id}
- **Next action:** {one concrete step}
- **Epistemic label:** INSTITUTIONAL_MODEL
```

Follow full checklist in [`RETROSPECTIVE.md`](../../RETROSPECTIVE.md).

---

## Verification checklist

- [ ] `modeling_profile.json` validates against umbrella schema
- [ ] `modeling_run.json` validates; embedded envelopes match `cross-layer-event.json`
- [ ] `story_ids` in profile match scenario doc anchors
- [ ] `epistemic_label` present on all public artifacts
- [ ] No μ/α/PNO values invented in umbrella docs
- [ ] No guilt/criminal/sovereignty language introduced
- [ ] Cross-repo change routed to correct repo (one repo per iteration)

---

## Compose with other skills

| Skill | Use |
|-------|-----|
| `errorlogy-multi-repo-loop` | Single-repo bounded iteration |
| `loop` | User-triggered recurring ticks |
| `loop-library` | Audit weak stop conditions |
| `babysit` | Keep modeling-base PR merge-ready |

---

## Links

- [`MODELING_BASE.md`](../architecture/MODELING_BASE.md)
- [`docs/examples/modeling-base/`](../examples/modeling-base/)
- [`MVP_ITERATIONS.md`](../examples/MVP_ITERATIONS.md)
