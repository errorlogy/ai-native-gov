# Example: Trump ↔ Macron meeting cascade

**Scenario type:** live bilateral summit  
**Purpose:** end-to-end walkthrough through **AI Native Gov lens** → streams → institutions → Errorlogy → politic.bar

> **Design scenario only** — not a published error card. Real cards require curated primary-source bundles and full pipeline gates.

Adapted from [politic-bar example](https://github.com/errorlogy/politic-bar/blob/main/docs/example-trump-macron-cascade.md) with institutional layer annotations.

---

## 0. AI Native Gov framing

Before ingest, activate institutional graph:

```text
Activated layers:
  executive (US, FR)
  interpol-analog (bilateral + NATO/EU follow-on)
  parliament (conditional — if ratification debate appears)
  judiciary (conditional — if legal interpretation conflict)

Topology intersections watched:
  executive-judiciary (communiqué vs domestic law)
  parliament-executive (mandate gap if no briefing)
  interpol-executive (coordination tempo)
```

---

## 1. Event anchor

| Field | Example value |
|-------|---------------|
| `story_id` | `2026-08-summit-trump-macron` |
| `event_type` | bilateral meeting + joint statements |
| `politifi_assets` | `brand:trump`, `brand:macron`, `agenda:nato-burden`, `agenda:ukraine`, `institution:white-house`, `institution:elysee` |
| `coordination_forum` | bilateral; optional NATO/EU Council follow-on |
| `mandated_outputs` | joint communiqué, press conferences, agreements |

---

## 2. Signal / noise stream (Side B)

Chronological ingest with evidence grade:

```text
T0  Agenda leak / pre-brief (media, grade: commentary)
T1  Official schedule (primary, grade: strong)
T2  Opening statements — Trump (primary transcript)
T3  Opening statements — Macron (primary transcript)
T4  Side meeting on trade (pool report, grade: medium)
T5  Joint statement draft circulated (primary / leak mix)
T6  Final communiqué published (primary, grade: strong)
T7  Domestic spin cycles (media, grade: weak–medium)
T8  Follow-on executive orders / EU council response (primary)
```

**Institutional tagging:**

| Timestamp | Primary layer | Notes |
|-----------|---------------|-------|
| T1–T6 | executive | Official records |
| T7 | — (weak) | Does not drive μ without corroboration |
| T8 | interpol-analog + executive | Cross-border follow-on |

EGD scores environment closure separately from WMS.

---

## 3. Parliament layer checkpoint

After T6, agent evaluates:

```json
{
  "layer": "institution:parliament",
  "deliberation_record_grade": "partial",
  "representation_map": {
    "US_congressional_briefing": "absent_in_stream",
    "FR_assemblee_debate": "not_yet_in_stream"
  },
  "mandate_gap_flag": "hypothesis",
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

If gap confirmed by primary records → ACC-relevant; not a verdict on legitimacy.

---

## 4. Decision-events (Side A — error cards)

| Card candidate | Layer | Recorded object |
|----------------|-------|-----------------|
| `US-EXEC-2026-TRADE-01` | executive | US tariff posture commitment |
| `FR-EXEC-2026-DEFENSE-01` | executive | FR NATO burden framing |
| `US-FR-2026-JOINT-01` | executive + interpol | Communiqué claims vs text |
| `EU-COUNCIL-2026-RESPONSE-01` | interpol-analog | Only if ≥2 reversals without new info |

Gap triplet per politic.bar METHODOLOGY §3: **claimed / known_or_knowable / decision / gap**.

---

## 5. Engine cascade (errorlogy-mas)

```text
source bundle
  → WMS (weak multisource signals)
  → μ over taxonomy v16
  → α propagation (prior summit, tariff policy cards)
  → ACC clusters
  → PNO regime
  → T4D / CAT (if series available)
  → FPD forecast
  → LBI alternatives
  → Red Team + Neutrality → public card
```

**Hypothetical weak signals:**

- Vertical asymmetry: briefing excludes dissent channel
- Horizontal asymmetry: trade vs security frame mismatch
- Temporal asymmetry: prior commitment without updated intelligence citation

**Topology → engine:** unresolved executive-judiciary tension surfaces as Red Team seed.

---

## 6. Interpol-analog layer (T8)

```json
{
  "layer": "institution:interpol-analog",
  "jurisdiction_set": ["US", "FR", "EU"],
  "coordination_forum": "EU Council",
  "cross_border_alpha_edges": ["US-FR-2026-JOINT-01", "EU-COUNCIL-2026-RESPONSE-01"],
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## 7. Politifi asset updates

| Asset | Update |
|-------|--------|
| `brand:trump` | +N card refs, actor profile delta |
| `brand:macron` | +N card refs, foreseeability distribution |
| `agenda:ukraine` | FPD snapshot pointer |
| `agenda:nato-burden` | ACC cluster on burden-sharing gap |
| `institution:white-house` | stream_refs + institutional metadata |

No moral scores — links only.

---

## 8. Public surface (dashboard vNext)

1. Story timeline — graded sources
2. Error cards — neutrality-audited
3. **Institutional topology view** — activated layers + intersection tensions
4. Topology view — α-links to prior events
5. Forecast panel — FPD with uncertainty labels
6. Politifi profiles — AP1–AP3

---

## 9. Publication blockers

- Unlocatable primary record
- Neutrality veto (verdict language, including "AI Court" phrasing)
- Verifier failure
- Weak-evidence μ above guard cap
- Hidden unresolved institutional conflict (topology transparency rule)

---

## 10. Implementation checklist

- [ ] Institutional context envelope in Scout output
- [ ] Ingest adapter for transcripts + communiqués
- [ ] errorlogy-mas adapter (`GovernanceCase` from stream bundle)
- [ ] Politifi registry CRUD with `institution:*`
- [ ] Dashboard: story + cards + **institutional graph** + α graph
- [ ] Optional NAMM certificate link on FPD panel

---

## Links

- [`../integrations/POLITIC_BAR.md`](../integrations/POLITIC_BAR.md)
- [`../integrations/ERRORLOGY.md`](../integrations/ERRORLOGY.md)
- [`../institutions/TOPOLOGY.md`](../institutions/TOPOLOGY.md)
