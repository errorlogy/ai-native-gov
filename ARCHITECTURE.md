# Architecture

## Layer model

```
                    ┌─────────────────────────────────────┐
                    │         Signal ingress            │
                    │  (news, social, official, NAMM)   │
                    └─────────────────┬─────────────────┘
                                      │
                    ┌─────────────────▼─────────────────┐
                    │      AI Native Gov (umbrella)       │
                    │  institutional topology + contracts │
                    └─────────────────┬─────────────────┘
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         │                            │                            │
         ▼                            ▼                            ▼
┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
│  Institutions   │        │    Schemas      │        │   Examples      │
│  parliament     │        │  shared contracts│        │  cascade docs   │
│  executive      │        │  cross-repo      │        │                 │
│  judiciary      │        │                  │        │                 │
│  interpol       │        │                  │        │                 │
└────────┬────────┘        └────────┬────────┘        └─────────────────┘
         │                          │
         └──────────────┬───────────┘
                        │
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
┌─────────────────┐          ┌─────────────────┐
│   Errorlogy     │          │  politic.bar    │
│ errors/forecasts│          │ politifi/streams│
│ validation      │          │ UI + APIs       │
└─────────────────┘          └─────────────────┘
```

## Institutional stack

| Layer | Function | Output |
|-------|----------|--------|
| Parliament | Deliberation, multi-party synthesis | Legislative posture, consensus/dissent |
| Executive | Policy execution modeling | Action likelihood, implementation paths |
| Judiciary | Dispute, precedent, legitimacy | Rulings, constraint signals |
| Interpol | Cross-border coordination | Jurisdiction bridges, enforcement posture |
| Ministries | Domain models (defense, finance, etc.) | Sector-specific forecasts |

Layers **intersect** — see [docs/institutions/TOPOLOGY.md](docs/institutions/TOPOLOGY.md). A signal may enter Parliament, be challenged in Judiciary, and trigger Interpol coordination.

## Data flow

1. **Ingress** — raw signals (manual, API, NAMM experiments)
2. **Routing** — topology determines which institutions process the signal
3. **Synthesis** — institutional outputs merged with checks & balances
4. **Validation** — Errorlogy checks errors, confidence, forecast drift
5. **Publication** — politic.bar surfaces politifi streams and narratives

## Repo boundaries

| Repo | Owns | Does not own |
|------|------|--------------|
| `ai-native-gov` (this) | Topology, contracts, vision, schemas | Production pipelines, UI |
| `errorlogy` | Error detection, forecast models, validation | Institutional topology docs |
| `politic-bar` | Politifi UI, signal streams, APIs | Architecture strategy |
| NAMM (experiments) | Experimental models | Production contracts |

## Schema layer

`schemas/` holds shared contracts (JSON Schema, YAML) referenced by both umbrella and child repos. Changes here are **versioned** and drive integration updates.

## Agent architecture

- **Umbrella agents** — edit docs, topology, contracts from `AI_NATIVE_GOV`
- **Implementation agents** — open child repos for code; reference umbrella contracts
- **Cross-repo agents** — contract first in umbrella, then implement in child

See [AGENTS.md](AGENTS.md) and [WORKSPACE.md](WORKSPACE.md).

## Security

- Private GitHub repos
- No secrets in umbrella or child repos
- Integration auth documented in child repos only
