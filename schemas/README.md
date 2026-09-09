# Schemas

Minimal JSON Schema stubs for cross-repo contracts. Implement parsers in child repositories.

| File | Purpose |
|------|---------|
| [`institution-layer-id.json`](institution-layer-id.json) | Enum of institutional layer IDs |
| [`cross-layer-event.json`](cross-layer-event.json) | Event envelope with layer activation |
| [`institution-graph.json`](institution-graph.json) | Topology nodes and typed edges |
| [`signal-envelope.json`](signal-envelope.json) | Graded stream item with memetic metrics |
| [`modeling-profile.json`](modeling-profile.json) | Reusable scenario template (ISR / Modeling Base) |
| [`modeling-run.json`](modeling-run.json) | Timestamped profile execution record |
| [`modeling-result.json`](modeling-result.json) | Run outcome with deltas and quality flags |

**Status:** v0 stubs — cross-layer and signal-envelope wired in errorlogy-mas (MVP iter 1–7). Modeling Base schemas are umbrella contracts; runtime store in child repos.

See [`ROADMAP.md`](../ROADMAP.md) Phase 2–3 for Modeling Base checkpoint and [`docs/architecture/MODELING_BASE.md`](../docs/architecture/MODELING_BASE.md).
