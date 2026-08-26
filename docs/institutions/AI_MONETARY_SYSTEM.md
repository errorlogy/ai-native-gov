# AI Monetary System — Central Bank, Treasury, and Agentic Economics

**Epistemic label:** `INSTITUTIONAL_MODEL` — all outputs from this layer are analytical contributions about monetary, fiscal, and market-coordination signals. No claim of legal tender authority, sovereign monetary policy, or operational central-banking capacity.

## Purpose

The **AI Monetary System** models national-level economic institutions that sit **beside** the Ministry of Finance and **below** Parliament and the Charter. It provides structured reasoning surfaces for:

- **Price stability and liquidity context** (central bank analog)
- **Fiscal capacity and spending posture** (treasury analog)
- **Market and platform oversight signals** (regulatory agency analog)
- **Agentic and on-chain coordination hypotheses** (agentic economics layer — blockchain, DeFi, AI-agent market behavior as *signals*, not policy mandates)

This layer does **not** issue currency, set real interest rates, or execute trades. It ingests normalized market and gov-data events (especially [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md)) and emits institutional framing for downstream synthesis.

> For ministry-level fiscal/trade posture, see [AI_MINISTRIES.md](AI_MINISTRIES.md) (Ministry of Finance).  
> For cabinet coordination, see [AI_CABINET.md](AI_CABINET.md).  
> For EU-level monetary coordination (ECB analog, eurozone rings), see [EU_TOPOLOGY.md](EU_TOPOLOGY.md).

---

## Role isomorphism

| Human analog | AI agent slot | Layer ID | Scope |
|--------------|---------------|----------|-------|
| Central bank | AI Central Bank analog | `institution:central-bank-analog` | Monetary stability *signals*, liquidity context, rate-path hypotheses |
| Treasury / finance ministry (fiscal) | AI Treasury analog | `institution:treasury-analog` | Fiscal capacity, debt issuance posture, budget execution signals |
| Securities / markets regulator | AI Regulatory agency | `institution:regulatory-agency` | Market conduct, listing oversight, crypto/platform rulemaking *posture* |
| Agent / on-chain economy | Agentic economics layer | `institution:agentic-economics` | AI-agent and blockchain coordination as uncertainty-tagged economic context |

**Modeling note:** Treasury and Ministry of Finance overlap in real states. In the simulator, **Finance Ministry** reports portfolio posture to Cabinet; **Treasury analog** holds fiscal-capacity and debt-sustainability signals that constrain Finance Ministry branches. Central bank analog is **independent** of Cabinet for monetary-signal synthesis (peer to Judiciary on independence norms — modeled, not legal fact).

---

## Layer relationships

```text
                    ┌─────────────────────────┐
                    │  Charter / Parliament   │
                    │  (mandate, legitimacy)  │
                    └───────────┬─────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
         ▼                      ▼                      ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────────┐
│ Central bank    │   │ Treasury analog │   │ Regulatory agency   │
│ analog          │   │                 │   │                     │
│ (monetary       │   │ (fiscal         │   │ (market/platform    │
│  signals)       │   │  capacity)      │   │  oversight posture) │
└────────┬────────┘   └────────┬────────┘   └──────────┬──────────┘
         │                     │                         │
         └─────────────────────┼─────────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Agentic economics   │
                    │ (on-chain + AI-agent│
                    │  coordination ctx)  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Ministry of Finance │
                    │ → AI Cabinet / PM   │
                    └─────────────────────┘
```

---

## Central bank analog

**Layer ID:** `institution:central-bank-analog`

### Scope

Models **monetary stability context**: inflation expectations, liquidity stress proxies, exchange-rate pressure, and central-bank communication as *signals* — not operational rate decisions.

### Inputs

| Source | Event types (examples) |
|--------|------------------------|
| [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md) | `fin_crypto_market_snapshot`, `fin_crypto_sentiment_momentum` |
| [GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md) | `gov_open_data_snapshot` (macro indicators) |
| Ministry of Finance | `portfolio_posture` (trade/currency sub-agent outputs) |

### Outputs

| Field | Description |
|-------|-------------|
| `monetary_stability_signal` | Aggregated stability context (float 0–1, uncertainty-tagged) |
| `liquidity_stress_hypothesis` | `HYPOTHESIS` — not a solvency verdict |
| `rate_path_posture` | Modeled reaction function as analytical contribution |
| `independence_constraint` | Flags when fiscal or executive pressure would *modeled* conflict with stability mandate |

### Constraints

- Cannot authorize market execution (see FIN_CRYPTO execution gate)
- Cannot label actors as fraudulent or criminal — use `risk_hypothesis` only
- Charter prohibits presenting modeled rate paths as binding policy
- EU national instances: eurozone members route ECB-level signals via `bloc:eu` collision paths ([EU_TOPOLOGY.md](EU_TOPOLOGY.md))

---

## Treasury analog

**Layer ID:** `institution:treasury-analog`

### Scope

Models **fiscal capacity and debt sustainability** separately from monetary signals. Treasury analog constrains Finance Ministry `preferred_branch` options when fiscal headroom is low.

### Inputs

- `gov_open_data_snapshot` (budget, debt ratios)
- `gov_executive_publication` (fiscal announcements)
- Central bank analog `liquidity_stress_hypothesis` (peer input, not instruction)

### Outputs

| Field | Description |
|-------|-------------|
| `fiscal_capacity_score` | Modeled headroom (0–1) |
| `debt_sustainability_signal` | Weak/medium evidence context |
| `spending_constraint_set` | Branches Finance Ministry must flag to PM |

### Cabinet interface

Treasury analog feeds **constraints** into PM synthesis; it does not replace Finance Minister `portfolio_posture`. PM merges both with `tension_flag` when fiscal and monetary signals diverge.

---

## Regulatory agency analog

**Layer ID:** `institution:regulatory-agency`

### Scope

Models **market and platform oversight posture** — securities-style registration, crypto exchange supervision, stablecoin disclosure, AI-agent trading surface rules — as *regulatory posture signals*, not enforcement verdicts.

### Inputs (FIN_CRYPTO routing)

| Event type | Simulator intent |
|------------|------------------|
| `fin_crypto_technical_indicator` | Weak evidence for market-structure attention |
| `fin_crypto_screener_rank_update` | Agenda-level attention (no buy/sell language) |
| `fin_crypto_onchain_risk` | Dispute surface for cross-border coordination |
| `fin_crypto_backtest_result` / `walk_forward_validation` | Methodological context for audit layer |
| `gov_executive_publication` | Rulemaking notices |

### Outputs

| Field | Description |
|-------|-------------|
| `regulatory_posture` | e.g. `monitoring`, `rulemaking_hypothesis`, `enforcement_posture_signal` |
| `market_integrity_hypothesis` | Uncertainty-tagged; never accusatory |
| `platform_scope` | Asset class / venue tags from adapter `instrument` |

### Judiciary and Transnational Ops

On-chain risk events may activate Judiciary and Transnational Ops per [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md). Regulatory agency provides **domestic oversight context**; cross-border enforcement flows through Transnational Ops, not unilateral regulatory posture.

---

## Agentic economics layer

**Layer ID:** `institution:agentic-economics`

### Purpose

Models **AI-agent and blockchain-mediated economic coordination** as an institutional reasoning layer — agent wallets, automated market makers, DeFi protocol health, NFT market microstructure, and multi-agent trading *behaviors* — without claiming sovereignty over money or smart contracts.

This is **not** a central bank and **not** a blockchain validator. It is a **signal synthesis layer** that:

1. Aggregates fin-crypto and symbolic-layer context ([SYMBOLIC_VISUAL_LAYER.md](../integrations/SYMBOLIC_VISUAL_LAYER.md) for catalog; market data stays in FIN_CRYPTO)
2. Surfaces **coordination hypotheses** (liquidity migration, agent herd behavior, protocol stress)
3. Routes high-risk execution surfaces to Human Oversight and audit (execution disabled in simulator by default)

### Non-sovereignty guarantees

| Claim type | Allowed label | Forbidden |
|------------|---------------|-----------|
| Protocol TVL drop | `liquidity_stress_hypothesis` | "bank run verdict" |
| Agent wallet cluster activity | `coordination_signal` | "money laundering finding" |
| Stablecoin depeg proxy | `peg_stress_hypothesis` | "fraud proven" |
| Smart contract exploit news | `dispute_surface` → Judiciary | criminal attribution |

### Sub-agent swarm (modeled)

| Sub-agent | Specialization |
|-----------|----------------|
| `onchain-metrics-sub` | DefiLlama/CoinGecko-style context (via FIN_CRYPTO adapters) |
| `agent-behavior-sub` | AI-agent trading pattern hypotheses (weak evidence) |
| `stablecoin-sub` | Peg and reserve disclosure *signal* ingest |
| `execution-guard-sub` | Refuses execution-surface MCP tools in simulator mode |

### Intersections

| From → To | Relationship |
|-----------|--------------|
| Agentic economics → Central bank analog | Liquidity and peg stress feed monetary stability context |
| Agentic economics → Regulatory agency | Platform and listing context for oversight posture |
| Agentic economics → Judiciary | On-chain dispute surfaces (hypotheses only) |
| Agentic economics → Audit | Provider health, execution-surface blocks |
| Finance Ministry → Agentic economics | Trade/sanctions context constrains on-chain coordination hypotheses |

---

## FIN_CRYPTO event routing (this layer)

Cross-reference: full table in [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md).

| Event type | Primary monetary layers | Secondary |
|------------|-------------------------|-----------|
| `fin_crypto_market_snapshot` | central-bank-analog, regulatory-agency | treasury-analog, executive |
| `fin_crypto_sentiment_momentum` | central-bank-analog | parliament |
| `fin_crypto_onchain_risk` | agentic-economics, regulatory-agency | judiciary, transnational-ops |
| `fin_crypto_technical_indicator` | regulatory-agency | ai-minister (science-tech / finance) |
| `fin_crypto_data_unavailable` | audit | agentic-economics (observability) |

All adapter outputs default to `epistemic_label=OPERATIONAL` until NAMM `certificate_ref` present.

---

## Autonomy dial parameters

| Layer | Parameter | Default | Human control |
|-------|-----------|---------|---------------|
| Central bank analog | `monetary_ai_pct` | 0.5 | Rollback via Human Oversight |
| Treasury analog | `treasury_ai_pct` | 0.4 | Rollback via Human Oversight |
| Regulatory agency | `regulatory_ai_pct` | 0.55 | Rollback via Human Oversight |
| Agentic economics | `agentic_economics_ai_pct` | 0.6 | Rollback; execution tools always gated |
| All slots | `human_veto_enabled` | `true` | Human-set |

**Hard constraint:** `execution_surface` MCP tools must not emit policy outcomes into μ/α/PNO ([FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md)).

---

## Sample envelope

```json
{
  "event_id": "2026-MON-03",
  "layer": "institution:central-bank-analog",
  "trigger_event_type": "fin_crypto_market_snapshot",
  "monetary_stability_signal": 0.68,
  "liquidity_stress_hypothesis": {
    "active": true,
    "confidence": 0.42,
    "notes": "Cross-venue BTC depth thinning; OPERATIONAL ingest only"
  },
  "peer_inputs": {
    "treasury_analog": { "fiscal_capacity_score": 0.55 },
    "regulatory_agency": { "regulatory_posture": "monitoring" },
    "agentic_economics": { "coordination_signal": "defi_tvl_concentration_shift" }
  },
  "cabinet_constraint": "Finance Ministry branch_likelihood capped at 0.6 pending Parliament review",
  "epistemic_label": "INSTITUTIONAL_MODEL"
}
```

---

## Related docs

- [FIN_CRYPTO_MARKETS.md](../integrations/FIN_CRYPTO_MARKETS.md) — market adapter contract and routing
- [GOV_DATA_SOURCES.md](../integrations/GOV_DATA_SOURCES.md) — fiscal and legislative ingress
- [AI_MINISTRIES.md](AI_MINISTRIES.md) — Ministry of Finance portfolio posture
- [AI_CABINET.md](AI_CABINET.md) — PM synthesis with fiscal/monetary tensions
- [AI_NATIONAL_INSTANCE.md](AI_NATIONAL_INSTANCE.md) — per-country stack template
- [EU_TOPOLOGY.md](EU_TOPOLOGY.md) — eurozone / ECB collision paths
- [TOPOLOGY.md](TOPOLOGY.md) — intersection matrix
- [ERRORLOGY.md](../integrations/ERRORLOGY.md) — downstream μ/α/PNO validation
