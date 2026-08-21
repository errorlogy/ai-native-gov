# Integration — MatrAIx Persona Cohorts

How AI Native Gov and Errorlogy may use **MatrAIx** simulated-persona infrastructure as an optional diversity / preference conditioning layer — without treating personas as citizens, voters, or sovereign substitutes.

**Epistemic label:** `INSTITUTIONAL_MODEL` for this contract document. Persona-conditioned runs that feed Errorlogy stay `OPERATIONAL` unless a NAMM `certificate_ref` upgrades a specific artifact to `COMPUTATIONAL_EVIDENCE`.

---

## Sources (authoritative)

| Source | Role |
|--------|------|
| [arXiv:2608.04205](https://arxiv.org/abs/2608.04205) / [HTML](https://arxiv.org/html/2608.04205v1) | Technical report — Persona 8B, DAG sampling, adherence study, limitations |
| [matraix.ai](https://matraix.ai) | Product / research site — eval infrastructure framing |
| [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | Open Playground + task library code |
| [MatrAIx_Persona_1M](https://huggingface.co/datasets/MatrAIx2026/MatrAIx_Persona_1M) / [Public Release](https://huggingface.co/datasets/MatrAIx2026/MatrAIx_Persona_1M_Public_Release) | Open ~1M coreset for research |

Numbers below are quoted from the report and dataset card. Re-check those URLs before any operational claim.

---

## What MatrAIx is / is not

### Is

| Fact | Accurate reading |
|------|------------------|
| **Persona 8B corpus** | ~**8.3 billion** persona *records* under a shared schema of **1,290** categorical dimensions (background, psychology, capability, behavior, lifestyle) |
| **Open coreset** | ~**1M** quality-filtered personas released publicly (**999,847** after under-18 removal): **599,847** human-grounded + **400,000** full-DAG synthetic |
| **Generation** | Synthetic records sampled via a **DAG** (directed acyclic graph) over dimensions: parents first, source-informed conditionals + compatibility masks |
| **Eval infra** | MatrAIx Playground environments: Survey, AI Chatbot, Web, App; **1,010** application task specs; **18,189** reported trials on eight representative tasks |
| **Adherence (controlled)** | In a **400-trial** study across ten behavioral attributes × four environments, declared behavior was expressed or correctly suppressed in **366/400 (91.5%)** — a conditioning / style probe, not identity with real humans |
| **Record → agent** | A record becomes a *persona agent* only when paired with a **model + interface + task**; evaluations instantiate only the **sampled cohort**, not the full 8.3B corpus |

### Is not

| Claim to reject | Why |
|-----------------|-----|
| “8.3B simultaneous agents” | Corpus size ≠ concurrent runtime; each study loads a cohort |
| “8.3B digital EU citizens” / “digital people replacing sovereignty” | Forbidden framing for this umbrella ([VISION.md](../../VISION.md), [GLOBAL_AI_GOVERNANCE.md](../institutions/GLOBAL_AI_GOVERNANCE.md)) |
| “Verified real humans” | Human-grounded = mapped from sources (Wiki, Amazon, Stack Overflow, GSS, PRISM, volunteer survey); extraction can err; not verified identity |
| “Representative probability sample” | Dataset card and Appendix M: not a probability sample of any real population; calibration is best-effort on selected **marginals** (age, region, gender identity, urbanicity), not full joint fidelity |
| “91.5% = people-like behavior” | Adherence measures whether assigned style appears/suppresses; paper states it does **not** establish disclosure/refusal/abandonment like real users |

**Language rule:** personas are **simulation instruments** and **cohort tags** for institutional MAS diversity — never “citizens,” “voters with standing,” or “legitimate public.”

---

## Mapping onto AI Native Gov constructs

Persona cohorts are **optional conditioning metadata** attached to institutional runs. They do not change charter, veto, or judicial-gate invariants.

| Our construct | MatrAIx role | Notes |
|---------------|--------------|-------|
| `NATIONAL_INSTANCE` (`state:{iso2}`) | Filter / stratify cohorts by region, language, legal-culture proxies in schema dims | Aligns with [EU_STATES.md](../institutions/EU_STATES.md) profiles; still `INSTITUTIONAL_MODEL` |
| EU citizen-analog (modeled public) | Sample EU-region / language / education strata for parliament or consultation scenarios | **Analog only** — not census replacement; never claim “EU digital demos” |
| `institution:party-coalition` / delegate diversity | Multi-persona cohorts behind party or EP-delegate agents | Diversity of *conditioned preferences*, not electoral mandates |
| Human oversight dials (`autonomy_dials`, `ai_readiness_level`) | Persona preference dims as scenario parameters when dials are mid/high | Oversight panel remains human (`HUMAN_DETERMINATION`); personas do not vote overrides |
| Institutional MAS (Parliament / Cabinet) | Persona-backed **agent conditioning** for deliberation variance | Agents remain layer role-players; see [AI_PARLIAMENT.md](../institutions/AI_PARLIAMENT.md) |

```text
Persona 1M (sample) → persona_cohort_id / filter recipe
        ↓
cross-layer-event (optional refs) + state_profile extension plan
        ↓
Institutional MAS roles (delegates, ministers, oversight scenarios)
        ↓
Errorlogy μ/α/PNO on persona-conditioned decision events
```

---

## Synergy with institutional MAS

**Intended use:** Parliament / council / consultation analogs can spawn **persona-backed agents** so coalition debate and citizen-analog feedback show preference diversity under a fixed policy proposal.

**Not intended use:**

- Replacing national sovereignty or EP electoral legitimacy with simulated majorities
- Treating cohort vote shares as public opinion polls of real jurisdictions
- Bypassing `human_override_always` / Human Oversight Panel

Recommended MAS pattern:

1. Fix the institutional question (bill, collision, dial change).
2. Sample a **declared** cohort (size, strata, seed, source mix).
3. Run persona-conditioned agents as **advisory / diversity probes**.
4. Aggregate as `INSTITUTIONAL_MODEL` signals into the same collision / synthesis path as other layers.
5. Keep human veto / appeal untouched.

---

## Synergy with Errorlogy

| Concern | Contract |
|---------|----------|
| Ownership | Umbrella: cohort refs + institutional framing. [Errorlogy](https://github.com/errorlogy/errorlogy): μ/α/PNO/FPD on **decision events** that may carry persona conditioning metadata |
| Measurement | Treat persona-conditioned outputs as events with stable `story_id` / `precedent_refs`; compute μ/α **on the institutional decision gap**, not “persona guilt” |
| Language | ACC = analytical contribution of roles (ministry, coalition, persona-backed delegate); never guilt |
| Model dependence | MatrAIx reports large outcome swings across persona-agent models on identical cohorts — always record **persona_agent_model** in run config before interpreting μ deltas |
| Epistemic upgrade | Persona telemetry alone stays `OPERATIONAL`; NAMM certificate required for `COMPUTATIONAL_EVIDENCE` |

See [ERRORLOGY.md](ERRORLOGY.md). Do not invent mode IDs; use taxonomy v16 only.

**MVP hook:** `ERRORLOGY_MVP` already exposes `POST /api/events/cross-layer` institutional stub. Future: accept optional `persona_cohort_id` / `persona_cohort_refs` once umbrella schema is extended (below). Until then, store cohort tags in adapter-side metadata **outside** the strict envelope or as free-text in `stream_refs` only if explicitly documented as temporary — prefer not to overload `stream_refs`.

---

## Synergy with symbolic visual / FIN_CRYPTO (optional dimensions)

Persona schema groups include lifestyle, media, risk tolerance, and related preference dims. Optional (non-blocking) mappings:

| Layer | Persona use |
|-------|-------------|
| [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md) | Preference for marks / lore clusters / merch aesthetics as **preference signals** in UI or NFT catalog A/B — not legitimacy |
| [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md) | Risk-tolerance / trust / finance-domain strata for market-signal reaction scenarios — still no investment advice |

Do not fold MatrAIx into fin-crypto adapters as a required dependency for Iteration 3.

---

## Recommended architecture

```text
┌─────────────────────┐     ┌──────────────────────────────┐
│ MatrAIx Persona 1M  │────►│ persona_cohort adapter       │
│ (HF / local shards) │     │ (ERRORLOGY_MVP, later)       │
└─────────────────────┘     │  - filter recipe + seed      │
                            │  - sample N personas         │
                            │  - emit persona_cohort_id    │
                            └──────────────┬───────────────┘
                                           │ refs only
                                           ▼
                            ┌──────────────────────────────┐
                            │ cross-layer-event (future)   │
                            │ + optional persona_cohort_*  │
                            │ activated_layers / epistemic │
                            └──────────────┬───────────────┘
                                           ▼
                            institutional framer → Errorlogy
```

**Adapter responsibilities (child repo, not umbrella):**

1. Respect HF / source licenses and MatrAIx responsible-use limits (Appendix M).
2. Sample from open **Persona 1M** (not claim full 8.3B local residency unless separately licensed/hosted).
3. Emit opaque `persona_cohort_id` + filter hash + counts (human-grounded vs synthetic share).
4. Never ship raw PII; MatrAIx human-grounded records are de-identified by design — preserve that posture.
5. Attach cohort refs to institutional envelopes; do not reimplement DAG generation inside AI Native Gov.

---

## Schema extension plan (do not break `additionalProperties: false` yet)

Current [`schemas/cross-layer-event.json`](../../schemas/cross-layer-event.json) and [`schemas/state-profile.json`](../../schemas/state-profile.json) set `additionalProperties: false`. **Do not** silently add fields without a coordinated schema + ERRORLOGY_MVP Pydantic bump.

### Phase A — stub only (this PR)

Standalone stub: [`schemas/persona-cohort-ref.json`](../../schemas/persona-cohort-ref.json). Documents the future object shape. Not yet `$ref`'d from cross-layer-event.

### Phase B — coordinated optional fields (later)

When MVP consumers are ready, add **optional** properties (still required list unchanged):

**On `cross-layer-event`:**

```json
"persona_cohort_id": { "type": "string", "description": "Opaque cohort id from MatrAIx adapter" },
"persona_cohort_refs": {
  "type": "array",
  "items": { "$ref": "persona-cohort-ref.json" },
  "description": "Optional multi-cohort tags for comparative runs"
}
```

**On `state-profile` (optional later):**

```json
"default_persona_filter": {
  "type": "object",
  "description": "Declared strata for citizen-analog sampling for this national instance (INSTITUTIONAL_MODEL)"
}
```

Until Phase B ships, adapters may keep cohort metadata in a **sidecar** JSON next to the event store row in ERRORLOGY_MVP (same `event_id`), without claiming schema compliance for those keys.

---

## Optimal plug order vs MVP iterations

Aligned with [MVP_ITERATIONS.md](../examples/MVP_ITERATIONS.md) and live stub `POST /api/events/cross-layer`:

| Order | When | What |
|-------|------|------|
| **0** | Now | Umbrella contract (this doc) + `persona-cohort-ref` stub |
| **1** | After Iteration 1 (events stub green) | Optional **cohort tags** on stored events / sidecar — no MatrAIx runtime |
| **2** | After Iteration 2 (topology UI) | Show cohort id on event feed if present (string badge only) |
| **3** | After Iteration 3 (fin-crypto) | Optional preference dims for market-reaction scenarios — still optional |
| **4** | Post-MVP | Full Persona 1M adapter + sampling + persona-backed parliament agents + μ on conditioned decision events |

**Do not** block Iterations 1–3 on MatrAIx downloads, Playground, or 8.3B corpus access.

---

## Risks and hard constraints

| Risk | Mitigation |
|------|------------|
| Demographic / stereotype bias | Declare strata; avoid claiming representativeness; audit synthetic vs human-grounded mix |
| Synthetic ≠ real | Always label `INSTITUTIONAL_MODEL` / simulation instrument; Appendix M language |
| Model self-preference | Record persona-agent model; prefer at least one backbone distinct from SUT when conclusions matter |
| ToS / license | Follow MatrAIx + HF dataset card; **source licenses still apply** to underlying human-grounded sources; no re-identification |
| Scale rhetoric | Never claim “8.3B digital citizens of the EU” or simultaneous agents |
| Sovereignty confusion | Persona-backed agents ≠ electoral mandate; human oversight remains non-bypassable |
| Under-18 | Public coreset removed under-18 survey records — keep age filters adult-only for gov scenarios |

Unsupported MatrAIx uses (echo Appendix M): impersonating named individuals; attributing opinions to real persons/communities; targeting protected groups for persuasion / exclusion / price discrimination.

---

## Related

- [GLOBAL_AI_GOVERNANCE.md](../institutions/GLOBAL_AI_GOVERNANCE.md) — three-tier world model; human dials
- [EU_TOPOLOGY.md](../institutions/EU_TOPOLOGY.md) / [EU_STATES.md](../institutions/EU_STATES.md) — national instances
- [PHILOSOPHY.md](../PHILOSOPHY.md) — Homo loquens; cognitive extension ≠ sovereignty
- [ERRORLOGY.md](ERRORLOGY.md) — engine contract
- [MVP_ITERATIONS.md](../examples/MVP_ITERATIONS.md) — plug order
- [FIN_CRYPTO_MARKETS.md](FIN_CRYPTO_MARKETS.md) / [SYMBOLIC_VISUAL_LAYER.md](SYMBOLIC_VISUAL_LAYER.md) — optional preference dimensions

---

*Phase classification: Phase 2 contract foreshadowing + Phase 4 optional adapter later. Umbrella stays docs/schemas only.*
