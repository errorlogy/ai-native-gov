# Topology Slice — parliament-ilp

**Epistemic label:** `INSTITUTIONAL_MODEL`

Excerpt for parliament deliberation layer. Full doc: [parliament.md](../../docs/institutions/parliament.md).

---

## Functions modeled

| Function | Output (modeled) |
|----------|------------------|
| Deliberation | Aggregate positions from parties/blocs |
| Consensus mapping | Agreement zones and fault lines |
| Dissent tracking | Minority positions for confidence caps |
| Mandate gap | Parliament ↔ executive tension when action precedes debate |

---

## Default activated layers

```text
institution:parliament
institution:party-coalition
institution:executive
institution:national-instance
```

**Conditional:** `institution:symbolic-visual` (when discourse fork binds party positions)

---

## Intersections watched

| Intersection | Tension type |
|--------------|--------------|
| `parliament` → `executive` | `mandate_gap_hypothesis`, `framing_mismatch` |
| `party-coalition` → `executive` | Dissent ratio cap on confidence |
| `symbolic-visual` ↔ `party-coalition` | `narrative_binding` |

---

## EU anticonsensus parliament contour (Sep 2026)

| Chamber | Modeled status |
|---------|----------------|
| UK Commons | Statement on settlements; partial deliberation record |
| EU Parliament | Delegate split; non-binding resolutions possible |
| National chambers (DE, FR, IE) | Fracture on Israel policy; grand coalition caution |
