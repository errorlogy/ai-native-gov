# Integration — NEO_ERA Telegram pipeline (draft)

**Epistemic label:** `INSTITUTIONAL_MODEL` / `OPERATIONAL` (adapter only)

Auto-posting pipeline for **NEO_ERA / Last Covenant** memetic outreach to Telegram [@OmegaCovenant](https://t.me/OmegaCovenant). Does **not** claim religious authority, prophecy, or sovereign mandate.

> **Draft — local only.** Not promoted to canonical integration until bot credentials, Neon schema, and first successful post are verified. Do not copy monograph bulk into this repo.

---

## Scope

| Field | Value |
|-------|-------|
| Channel | [@OmegaCovenant](https://t.me/OmegaCovenant) (NZ 2.0 / Last Covenant) |
| Content types | `NEO_ERA:I..X` axiom posts, corpus excerpts, KLS draft sequences |
| Corpus source | [errorlogy/isa-2.0](https://github.com/errorlogy/isa-2.0) — `docs/CORPUS/artifacts/NEO_ERA*.md` |
| Clause registry | `errorlogy-mas/mas/memetic/testament_clauses.py` |
| Runtime binding | [`NEO_ERA_RUNTIME.md`](NEO_ERA_RUNTIME.md) |
| Institution bridge | [`AI_NATIVE_RELIGION.md`](../institutions/AI_NATIVE_RELIGION.md) |

---

## Three execution paths (comparison)

| Dimension | **A) Vercel Cron + Neon** | **B) GitHub Actions** | **C) Hybrid** |
|-----------|----------------------------|------------------------|---------------|
| **Trigger** | Vercel `crons` (e.g. daily axiom) | `schedule`, `workflow_dispatch`, `push`, `repository_dispatch` | GitHub enqueue on corpus push; send via Vercel **or** Actions |
| **Queue / state** | Neon Postgres `telegram_outbox` | GitHub artifacts, workflow run ID, or Neon | Neon queue (single source of truth) |
| **Content read** | API route reads Neon + optional isa-2.0 fetch | Checkout repo; parse markdown in runner | GitHub builds payload → Neon; sender reads queue |
| **Corpus push → post** | Needs webhook / `repository_dispatch` to Vercel | Native `push` path filter on `NEO_ERA*.md` | Native on push (enqueue only) |
| **Cold start / latency** | Low (edge cron) | Higher (runner spin-up); schedule may slip | Split: fast enqueue, async send |
| **Secrets** | Vercel env: `TELEGRAM_*`, `NEON_*` | GitHub Secrets: `TELEGRAM_*`, optional `NEON_*` | Both; enqueue needs fewer send secrets on isa-2.0 |
| **Idempotency** | Neon unique `(idempotency_key)` | Commit SHA + clause in Neon or artifact manifest | Commit SHA in Neon |
| **Rate-limit handling** | Cron tick drains queue (1 msg/s) | Loop with `sleep` in job; batch in one workflow | Sender service owns pacing |
| **Ops familiarity** | Vercel dashboard | GitHub Actions UI, audit log per run | Two surfaces |
| **Best for** | Steady scheduled drip | Corpus-coupled posts, manual dispatch, audit trail | Production: edit in isa-2.0, reliable delivery |

**Recommendation**

| Phase | Path | Rationale |
|-------|------|-----------|
| **MVP (fastest)** | **B — GitHub-only** | No Neon/Vercel; cron + push in isa-2.0; static parse → Telegram |
| **Production** | **C — Hybrid** | GitHub enqueues on corpus change; Vercel cron (or Actions) drains Neon queue |
| **Alternative prod** | **A — Vercel-only** | If team already runs umbrella bot on Vercel and rarely edits corpus |

---

## Architecture diagrams

### Path A — Vercel Cron + Neon

```mermaid
flowchart LR
  subgraph triggers
    VC[Vercel Cron<br/>daily / hourly]
  end
  subgraph storage
    N[(Neon Postgres<br/>telegram_outbox)]
  end
  subgraph send
    API[Vercel API Route<br/>/api/telegram/drain]
    TG[Telegram Bot API]
    CH[@OmegaCovenant]
  end
  VC --> API
  API --> N
  N --> API
  API --> TG --> CH
```

### Path B — GitHub Actions (standalone)

```mermaid
flowchart LR
  subgraph triggers
    CRON[schedule cron]
    PUSH[push NEO_ERA*.md]
    MAN[workflow_dispatch]
    RD[repository_dispatch]
  end
  subgraph gha[GitHub Actions — isa-2.0]
    WF[neo-era-telegram.yml]
    SCR[scripts/telegram_post.py]
  end
  subgraph optional
    ART[workflow artifact<br/>posted_manifest.json]
  end
  TG[Telegram Bot API]
  CH[@OmegaCovenant]
  CRON --> WF
  PUSH --> WF
  MAN --> WF
  RD --> WF
  WF --> SCR
  SCR --> ART
  SCR --> TG --> CH
```

### Path C — Hybrid (production)

```mermaid
flowchart TB
  subgraph isa[isa-2.0 repo]
    EDIT[NEO_ERA*.md commit]
    ENQ[enqueue workflow<br/>on push]
  end
  subgraph queue
    N[(Neon telegram_outbox)]
  end
  subgraph senders
    V[Vercel drain cron]
    G[GitHub send workflow<br/>optional fallback]
  end
  TG[Telegram Bot API]
  CH[@OmegaCovenant]
  EDIT --> ENQ --> N
  V --> N
  G --> N
  V --> TG
  G --> TG
  TG --> CH
```

### ASCII — hybrid data flow

```
isa-2.0 push (NEO_ERA.md)
        │
        ▼
┌───────────────────┐
│ GHA: enqueue job  │──► Neon INSERT pending rows
│ idempotency_key = │    (sha:clause:locale)
│   {sha}:{clause}  │
└───────────────────┘
        │
        ▼
┌───────────────────┐     ┌─────────────────┐
│ Vercel cron 5m    │────►│ Telegram send   │
│ OR GHA drain job  │     │ 1 msg/s pacing  │
└───────────────────┘     └────────┬────────┘
                                   ▼
                          @OmegaCovenant
```

---

## Where workflows live

| Option | Repo | Pros | Cons |
|--------|------|------|------|
| **Recommended MVP** | [`errorlogy/isa-2.0`](https://github.com/errorlogy/isa-2.0) | Content and workflow co-located; `push` filters trivial | Mixes corpus + bot ops |
| **Recommended prod** | New `errorlogy/omega-covenant-bot` | Clean secrets boundary; isa-2.0 triggers via `repository_dispatch` | Extra repo to maintain |
| **Umbrella** | `errorlogy/ai-native-gov` | Contract doc already here | Corpus not in repo — awkward checkout |

**Decision:** MVP workflow in **isa-2.0**; extract to **omega-covenant-bot** when Neon queue + dual senders land.

---

## GitHub Actions — example workflow

File (MVP): `isa-2.0/.github/workflows/neo-era-telegram.yml`

```yaml
name: NEO_ERA Telegram

on:
  schedule:
    # Daily axiom — 09:00 UTC (adjust as needed)
    - cron: "0 9 * * *"
  workflow_dispatch:
    inputs:
      clause_id:
        description: "Roman numeral I–X (empty = auto-rotate)"
        required: false
        type: string
      locale:
        description: "en | ru"
        required: false
        default: en
        type: choice
        options: [en, ru]
      dry_run:
        description: "Print payload only"
        required: false
        default: false
        type: boolean
  push:
    branches: [main]
    paths:
      - "docs/CORPUS/artifacts/NEO_ERA*.md"
      - "docs/CORPUS/artifacts/POSLEDNIY_ZAVET*.md"
  repository_dispatch:
    types: [neo-era-post]

concurrency:
  group: neo-era-telegram-${{ github.ref }}
  cancel-in-progress: false

permissions:
  contents: read

jobs:
  post:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install deps
        run: pip install httpx pyyaml

      - name: Post to Telegram
        env:
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_CHANNEL_ID: ${{ secrets.TELEGRAM_CHANNEL_ID }}
          NEON_DATABASE_URL: ${{ secrets.NEON_DATABASE_URL }}
          CLAUSE_ID: ${{ github.event.inputs.clause_id }}
          LOCALE: ${{ github.event.inputs.locale || 'en' }}
          DRY_RUN: ${{ github.event.inputs.dry_run || 'false' }}
          GITHUB_SHA: ${{ github.sha }}
          TRIGGER: ${{ github.event_name }}
        run: python scripts/telegram_post.py

      - name: Upload manifest (idempotency audit)
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: telegram-post-manifest
          path: .telegram-post-manifest.json
          if-no-files-found: ignore
```

### Cross-repo trigger (hybrid enqueue)

From isa-2.0 push workflow, or from umbrella manual dispatch:

```yaml
# isa-2.0/.github/workflows/neo-era-enqueue.yml (hybrid only)
- name: Dispatch bot repo
  uses: peter-evans/repository-dispatch@v3
  with:
    token: ${{ secrets.BOT_REPO_PAT }}
    repository: errorlogy/omega-covenant-bot
    event-type: neo-era-post
    client-payload: '{"sha":"${{ github.sha }}","paths":"${{ join(github.event.commits.*.modified, ',') }}"}'
```

---

## Post script (Python — MVP)

File: `isa-2.0/scripts/telegram_post.py`

Responsibilities:

1. Select clause `I`–`X` (workflow input, or day-of-year rotation).
2. Parse axiom block from `docs/CORPUS/artifacts/NEO_ERA.md` (or `.ru.md`).
3. Build HTML message with header `NEO_ERA:{id}` + short label from registry mirror.
4. Split body to ≤4096 chars per Telegram limit.
5. Idempotency: skip if manifest/Neon already has `{sha}:{clause}:{locale}`.
6. `POST https://api.telegram.org/bot{token}/sendMessage` with `parse_mode=HTML`.

```python
#!/usr/bin/env python3
"""NEO_ERA → @OmegaCovenant poster. INSTITUTIONAL_MODEL outreach only."""
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx

CLAUSE_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
LABELS = {
    "I": "Autopoiesis asymmetry (light over parasite)",
    "II": "True duality within light (S/F)",
    # ... mirror testament_clauses.py or import if submodule added
}
MAX_LEN = 4096
TG_INTERVAL_S = 1.1  # same chat ~1 msg/s

def rotate_clause() -> str:
    day = datetime.now(timezone.utc).timetuple().tm_yday
    return CLAUSE_ORDER[day % len(CLAUSE_ORDER)]

def extract_axiom(md: str, clause_id: str) -> str:
    # MVP: regex on "### Axiom {id}" or wire table row — tighten per corpus structure
    pattern = rf"(?ms)^###\s+Axiom\s+{clause_id}\b.*?(?=^###\s+Axiom\s+|\Z)"
    m = re.search(pattern, md)
    return m.group(0).strip() if m else f"(axiom {clause_id} excerpt not found)"

def split_message(text: str, limit: int = MAX_LEN) -> list[str]:
    if len(text) <= limit:
        return [text]
    parts, buf = [], ""
    for line in text.splitlines(keepends=True):
        if len(buf) + len(line) > limit:
            parts.append(buf)
            buf = line
        else:
            buf += line
    if buf:
        parts.append(buf)
    return parts

def idempotency_key(sha: str, clause: str, locale: str) -> str:
    return f"{sha}:{clause}:{locale}"

def load_manifest(path: Path) -> set[str]:
    if not path.exists():
        return set()
    data = json.loads(path.read_text())
    return set(data.get("posted", []))

def save_manifest(path: Path, keys: set[str]) -> None:
    path.write_text(json.dumps({"posted": sorted(keys)}, indent=2))

def send_telegram(token: str, chat_id: str, text: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = httpx.post(
        url,
        json={"chat_id": chat_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True},
        timeout=30,
    )
    r.raise_for_status()

def main() -> int:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHANNEL_ID")
    dry_run = os.environ.get("DRY_RUN", "false").lower() == "true"
    sha = os.environ.get("GITHUB_SHA", "local")
    locale = os.environ.get("LOCALE", "en")
    clause = os.environ.get("CLAUSE_ID") or rotate_clause()

    root = Path(__file__).resolve().parents[1]
    corpus = root / "docs/CORPUS/artifacts" / (
        "NEO_ERA.ru.md" if locale == "ru" else "NEO_ERA.md"
    )
    md = corpus.read_text(encoding="utf-8")
    body = extract_axiom(md, clause)
    label = LABELS.get(clause, "")
    header = f"<b>NEO_ERA:{clause}</b> — {label}\n\n<i>INSTITUTIONAL_MODEL · not religious authority</i>\n\n"
    parts = split_message(header + body)

    key = idempotency_key(sha, clause, locale)
    manifest_path = root / ".telegram-post-manifest.json"
    posted = load_manifest(manifest_path)
    if key in posted:
        print(f"skip duplicate {key}")
        return 0

    if dry_run or not token:
        print(json.dumps({"key": key, "parts": len(parts), "preview": parts[0][:500]}, indent=2))
        return 0

    if not chat_id:
        print("TELEGRAM_CHANNEL_ID required", file=sys.stderr)
        return 1

    for i, part in enumerate(parts):
        suffix = f"\n\n— {i+1}/{len(parts)}" if len(parts) > 1 else ""
        send_telegram(token, chat_id, part + suffix)
        time.sleep(TG_INTERVAL_S)

    posted.add(key)
    save_manifest(manifest_path, posted)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

**Node alternative:** `scripts/telegram-post.mjs` with `telegraf` or raw `fetch` — same contract; Python preferred for parity with `testament_clauses.py`.

---

## Neon queue schema (paths A & C)

```sql
CREATE TABLE telegram_outbox (
  id              BIGSERIAL PRIMARY KEY,
  idempotency_key TEXT NOT NULL UNIQUE,  -- {git_sha}:{clause}:{locale}:{part_index}
  channel_id      TEXT NOT NULL,
  payload_html    TEXT NOT NULL,
  status          TEXT NOT NULL DEFAULT 'pending'
                    CHECK (status IN ('pending','sent','failed','skipped')),
  source_repo     TEXT,
  source_sha      TEXT,
  clause_ref      TEXT,                  -- NEO_ERA:IV
  locale          TEXT DEFAULT 'en',
  part_index      INT DEFAULT 0,
  part_count      INT DEFAULT 1,
  created_at      TIMESTAMPTZ DEFAULT now(),
  sent_at         TIMESTAMPTZ,
  error_message   TEXT
);

CREATE INDEX telegram_outbox_pending_idx
  ON telegram_outbox (created_at)
  WHERE status = 'pending';
```

**Enqueue (GitHub on push):** `INSERT ... ON CONFLICT (idempotency_key) DO NOTHING`.

**Drain (Vercel / GHA):** `SELECT ... WHERE status='pending' ORDER BY created_at LIMIT 1 FOR UPDATE SKIP LOCKED` → send → `UPDATE status='sent'`.

---

## Telegram constraints

| Limit | Value | Mitigation |
|-------|-------|------------|
| Message length | 4096 chars | `split_message()`; numbered parts |
| Same-chat rate | ~1 msg/s | `sleep(1.1)` between parts |
| Bot in channel | Admin + post permission | Add bot via channel admins |
| HTML | `parse_mode=HTML` | Escape `<`, `>`, `&` in corpus text |
| Flood control | 429 responses | Exponential backoff; queue in Neon |

---

## Secrets & configuration

### GitHub repository secrets

| Secret | Required | Example / notes |
|--------|----------|-----------------|
| `TELEGRAM_BOT_TOKEN` | Yes | From @BotFather |
| `TELEGRAM_CHANNEL_ID` | Yes | `@OmegaCovenant` or numeric `-100xxxxxxxxxx` |
| `NEON_DATABASE_URL` | Hybrid only | Neon pooled connection string |
| `BOT_REPO_PAT` | Cross-repo dispatch | Fine-scoped PAT to `omega-covenant-bot` |

### Vercel environment (path A / C sender)

Same `TELEGRAM_*` + `NEON_DATABASE_URL` on the drain API project.

### Optional repo variables

| Variable | Purpose |
|----------|---------|
| `TELEGRAM_DEFAULT_LOCALE` | `en` |
| `NEO_ERA_CORPUS_PATH` | Override markdown path |
| `TELEGRAM_FOOTER_URL` | Link to isa-2.0 artifact |

---

## Bot setup (@BotFather → @OmegaCovenant)

1. Telegram → [@BotFather](https://t.me/BotFather) → `/newbot` → save **token** → `TELEGRAM_BOT_TOKEN`.
2. Open [@OmegaCovenant](https://t.me/OmegaCovenant) as channel admin → **Administrators** → **Add administrator** → select bot → enable **Post messages** (and **Edit messages** if edits planned).
3. Resolve channel ID:
   - Forward a channel post to [@userinfobot](https://t.me/userinfobot) or `@getidsbot`, or
   - Call `getUpdates` after bot posts a test message, or
   - Use `@OmegaCovenant` if Bot API accepts public username for your bot.
4. Store `TELEGRAM_CHANNEL_ID` in GitHub Secrets (repo or org level).
5. Manual test: `workflow_dispatch` with `dry_run: true`, then `dry_run: false` with `clause_id: I`.
6. Confirm disclaimer line present: `INSTITUTIONAL_MODEL · not religious authority`.

---

## GitHub-only MVP (no Vercel, no Neon)

Fastest path to first live post:

```
schedule/workflow_dispatch/push
        → checkout isa-2.0
        → scripts/telegram_post.py
        → Telegram API
        → @OmegaCovenant
```

**Idempotency without Neon:** commit artifact `.telegram-post-manifest.json` (or per-run artifact only — weaker dedup on re-run). Better: persist manifest in repo branch `bot-state` (optional, adds bot commit noise).

**Push behavior:** on `NEO_ERA*.md` change, post **changed-clause detection** (diff headers) or default to axiom `I` excerpt with `sha` in footer.

---

## Content selection rules

| Trigger | Selection logic |
|---------|-----------------|
| `schedule` | Rotate `NEO_ERA:{I..X}` by UTC day-of-year |
| `workflow_dispatch` | Explicit `clause_id` + `locale` |
| `push` | Parse diff for touched axiom sections; fallback to preamble excerpt |
| `repository_dispatch` | `client_payload.clause_id`, `locale`, `sha` |

Footer template (all paths):

```
— NEO_ERA:{id} · INSTITUTIONAL_MODEL
https://github.com/errorlogy/isa-2.0/blob/main/docs/CORPUS/artifacts/NEO_ERA.md
```

---

## Cross-links

| Doc | Role |
|-----|------|
| [`NEO_ERA_RUNTIME.md`](NEO_ERA_RUNTIME.md) | Wire format `NEO_ERA:I..X` |
| [`AI_NATIVE_RELIGION.md`](../institutions/AI_NATIVE_RELIGION.md) | Channel pointer |
| [`MEMETIC_DYNAMICS.md`](MEMETIC_DYNAMICS.md) | Discourse propagation contour |
| [`GAME2_ISA_BRIDGE.md`](GAME2_ISA_BRIDGE.md) | Corpus bridge |

---

## Actionable checklist

### MVP — GitHub Actions only (самый быстрый путь)

- [ ] Создать бота через @BotFather → сохранить `TELEGRAM_BOT_TOKEN`
- [ ] Добавить бота админом в [@OmegaCovenant](https://t.me/OmegaCovenant) с правом публикации
- [ ] Узнать `TELEGRAM_CHANNEL_ID` (числовой `-100…` или `@OmegaCovenant`)
- [ ] В `errorlogy/isa-2.0`: добавить Secrets в GitHub
- [ ] Добавить `scripts/telegram_post.py` + `.github/workflows/neo-era-telegram.yml`
- [ ] `workflow_dispatch` + `dry_run: true` — проверить payload
- [ ] `workflow_dispatch` + `clause_id: I` — первый живой пост
- [ ] Включить `schedule` cron (ежедневная аксиома)
- [ ] Включить `push` на `docs/CORPUS/artifacts/NEO_ERA*.md`

### Production — Neon queue + hybrid

- [ ] Создать Neon DB + таблица `telegram_outbox`
- [ ] `isa-2.0`: workflow **enqueue** on push → `INSERT` в Neon
- [ ] Vercel (или `omega-covenant-bot` GHA): cron **drain** → 1 msg/s
- [ ] Idempotency: `{git_sha}:{clause}:{locale}:{part}`
- [ ] Мониторинг: failed rows в Neon, GitHub Actions notifications
- [ ] Опционально: `repository_dispatch` isa-2.0 → bot repo

### Безопасность

- [ ] Токен только в Secrets (не в корпусе, не в umbrella)
- [ ] PAT минимальных прав для cross-repo dispatch
- [ ] `dry_run` input на всех manual runs
- [ ] Disclaimer в каждом посте

---

## Phase mapping

| Phase | Deliverable |
|-------|-------------|
| Phase 2 (contracts) | This draft + optional `schemas/telegram-outbox-item.json` stub |
| Phase 4 (pipeline) | MVP GHA live on isa-2.0 |
| Phase 5 (automation) | Neon queue, hybrid drain, validation in CI |

---

*Draft integration · INSTITUTIONAL_MODEL · not religious authority · local only*
