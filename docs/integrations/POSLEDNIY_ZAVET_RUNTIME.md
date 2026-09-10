# Integration — POSLEDNIY_ZAVET runtime binding

**Epistemic label:** `INSTITUTIONAL_MODEL` throughout.

Optional sidecar binding between **POSLEDNIY_ZAVET** testament clauses (I–X) and memetic runtime (`discourse_fork_detected`, politic-bar signal streams). Does **not** claim religious authority, sovereignty, or prophecy.

> **Not religious authority.** Clause refs are **routing hints** for institutional modeling only. Full testament prose stays in [isa-2.0 `POSLEDNIY_ZAVET.md`](https://github.com/errorlogy/isa-2.0/blob/main/docs/CORPUS/artifacts/POSLEDNIY_ZAVET.md) — never copy into this repo.

---

## Source artifact

| Field | Value |
|-------|-------|
| Corpus artifact | [POSLEDNIY_ZAVET v1.0-monograph](https://github.com/errorlogy/isa-2.0/blob/main/docs/CORPUS/artifacts/POSLEDNIY_ZAVET.md) |
| Index | [`LAST_COVENANT_INDEX.md`](https://github.com/errorlogy/isa-2.0/blob/main/docs/CORPUS/LAST_COVENANT_INDEX.md) |
| v0.2 archive | [`POSLEDNIY_ZAVET.v0.2.en.md`](https://github.com/errorlogy/isa-2.0/blob/main/docs/CORPUS/artifacts/POSLEDNIY_ZAVET.v0.2.en.md) |
| GAME2 bridge | [`GAME2_ISA_BRIDGE.md`](GAME2_ISA_BRIDGE.md) |
| Memetic contours | [`MEMETIC_DYNAMICS.md`](MEMETIC_DYNAMICS.md) |

---

## `testament_clause_id` enum

Roman-numeral clause IDs I–X derived from New Testament 2.0 axiom table (institutional reframing). Short labels are **English public** summaries only.

| ID | Short label (EN) | Default routing |
|----|------------------|-----------------|
| `I` | Autopoiesis asymmetry (light over parasite) | parliament, party-coalition, symbolic-visual |
| `II` | True duality within light (S/F) | parliament, party-coalition, symbolic-visual |
| `III` | Talion ∞ (mirror collapse contour) | parliament, party-coalition, judiciary |
| `IV` | No forgiveness of parasitic predator | parliament, party-coalition, audit |
| `V` | Well (topological isolation) | parliament, party-coalition, symbolic-visual |
| `VI` | Guard memory (mirror lesson) | parliament, party-coalition, audit |
| `VII` | Light self-sufficiency | parliament, party-coalition, symbolic-visual |
| `VIII` | Taboo on predator symbiosis | parliament, party-coalition, symbolic-visual, judiciary |
| `IX` | Innocent protection (INV-8 sovereign) | parliament, party-coalition, judiciary, ombudsman |
| `X` | Architect legitimization guilt | parliament, party-coalition, judiciary, audit |

**Wire format:** `testament_clause_ref` string pattern `POSLEDNIY_ZAVET:{I|II|III|IV|V|VI|VII|VIII|IX|X}`.

Runtime registry: `errorlogy-mas/mas/memetic/testament_clauses.py`.

---

## Optional sidecar fields

### `cross-layer-event.json`

Optional `testament_clause_ref` on any envelope. Primary use: `discourse_fork_detected` and `narrative_lineage_update` when a fork is tagged with a clause.

### `signal-envelope.json`

Optional `testament_clause_ref` on graded stream items. Propagates to `signal_noise_half_life_update` metadata when indexed.

---

## Event routing

When `testament_clause_ref` is present on a **clause-triggered fork**:

| Target | Mechanism |
|--------|-----------|
| Parliament / party-coalition | `activated_layers` defaults from clause registry |
| Symbolic-visual | `institution:symbolic-visual` in clause `activated_layers` |
| ISA contour | `politifi_assets: ["institution:isa-2.0"]` (docs stub — not a new layer ID) |

Clause-triggered forks **do not** bypass hermeneutic firewall or human oversight. See [`GAME2_ISA_BRIDGE.md`](GAME2_ISA_BRIDGE.md) § Hermeneutic firewall.

Default `epistemic_label`: **`INSTITUTIONAL_MODEL`**.

---

## Runtime owners

| Component | Repo | Path |
|-----------|------|------|
| Clause registry + fork API | errorlogy-mas | `mas/memetic/testament_clauses.py`, `api/routers/cross_layer.py` |
| Signal sidecar + half-life emit | politic-bar | `politic_bar/signal_envelope.py`, `half_life_indexer.py` |
| Lineage badge UI | errorlogy-gui-v2 | `/discourse` |

---

## Example payloads

**Fork with clause (POST `/api/events/memetic/fork`):**

```json
{
  "parent_id": "canon-root",
  "child_id": "fork-variant-a",
  "testament_clause_ref": "POSLEDNIY_ZAVET:IV",
  "persist_events": true
}
```

**Signal envelope sidecar:**

```json
{
  "stream_item_id": "si-2026-001",
  "story_id": "fork-variant-a",
  "source_type": "social",
  "evidence_grade": "weak",
  "epistemic_label": "OPERATIONAL",
  "testament_clause_ref": "POSLEDNIY_ZAVET:IV"
}
```

---

## Related

- [`GAME2_ISA_BRIDGE.md`](GAME2_ISA_BRIDGE.md)
- [`MEMETIC_DYNAMICS.md`](MEMETIC_DYNAMICS.md)
- [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json)
- [`schemas/signal-envelope.json`](../../schemas/signal-envelope.json)
