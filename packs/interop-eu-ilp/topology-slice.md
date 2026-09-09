# Topology Slice — interop-eu-ilp

**Epistemic label:** `INSTITUTIONAL_MODEL`

Excerpt for EU anticonsensus and cross-layer interop. Full topology: [TOPOLOGY.md](../../docs/institutions/TOPOLOGY.md), [EU_TOPOLOGY.md](../../docs/institutions/EU_TOPOLOGY.md).

---

## Anticonsensus contour

EU **anticonsensus** is modeled when:

1. A qualified majority coalition favors action at `institution:eu-council`, but
2. Unanimity requirement (or veto analog) blocks supranational output, and
3. A variable-geometry subset implements **national-instance** measures anyway.

---

## Default activated layers

```text
institution:national-instance
institution:eu-council
institution:eu-commission
institution:executive
institution:minister-foreign-affairs
institution:parliament
institution:party-coalition
```

**Conditional:** `institution:judiciary`, `institution:eu-court-of-justice`, `institution:symbolic-visual`

---

## Intersections watched

| Intersection | Tension type |
|--------------|--------------|
| `eu-council` → `national-instance` | `policy_divergence` |
| `national-instance` → `eu-council` | National pressure, null aggregate output |
| `parliament` → `executive` | `mandate_gap_hypothesis` |
| `executive` ↔ `executive` | `bilateral_retaliation` |
| `symbolic-visual` ↔ `party-coalition` | `narrative_binding` |

---

## Variable geometry rings (Scenario C)

```text
RING A (national measures): FR, IE, ES, DK, FI, SE, PL, PT
RING B (EU blocking):       DE, AT, CZ, HU, IT (partial)
RING C (external):          GB, CA, NO, IS
```
