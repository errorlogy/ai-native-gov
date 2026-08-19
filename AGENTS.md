# Agent Instructions — AI Native Gov

## Mission

Navigate the **AI Native Gov umbrella** and route work to the correct child repository. This repo holds **vision, institutional topology, and integration contracts** — not product code.

---

## Repository roles

| Question | Go to |
|----------|-------|
| Taxonomy v16, μ/α/PNO/FPD engine | [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) |
| Error cards, politifi, signal/noise streams | [errorlogy/politic-bar](https://github.com/errorlogy/politic-bar) |
| Certificates, Protocol v2, experiments | [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) |
| Institutional layers, topology, checks & balances | **this repo** |

---

## Read order (new agent)

1. [`README.md`](README.md) — scope and child repo map
2. [`VISION.md`](VISION.md) — epistemic humility, non-sovereignty
3. [`ARCHITECTURE.md`](ARCHITECTURE.md) — mermaid diagrams, data flows
4. [`docs/institutions/OVERVIEW.md`](docs/institutions/OVERVIEW.md) — framework
5. [`docs/institutions/TOPOLOGY.md`](docs/institutions/TOPOLOGY.md) — intersections
6. Relevant [`docs/integrations/`](docs/integrations/) for your task

---

## Institutional modeling rules

| Do | Don't |
|----|-------|
| Treat institutions as **reasoning layers** | Claim real-world legal authority |
| Document constraints and counter-institutions | Invent mode IDs (CB-xxx, PNO-x, …) |
| Label outputs `INSTITUTIONAL_MODEL` | Present modeling as verdict |
| Reference Errorlogy engine for numeric outputs | Reimplement μ/α/PNO in umbrella docs |

---

## Language rules (shared with Errorlogy / politic.bar)

| Use | Never use |
|-----|-----------|
| analytical contribution | guilty, criminal |
| fuzzy membership μ | proven guilt |
| legitimacy **signals** (modeled) | legitimate ruler (verdict) |
| institutional framing | sovereign AI government |
| possible / consistent with | "this proves" |

---

## Work routing

```text
Changing engine math        → errorlogy/errorlogy
Changing card schema/UI     → politic-bar
Adding certificate experiment → namm-experiments
New institution layer doc   → ai-native-gov/docs/institutions/
Integration contract update → ai-native-gov/docs/integrations/
Cross-repo scenario         → ai-native-gov/docs/examples/
```

---

## Schemas

Minimal stubs in [`schemas/`](../schemas/):

- `institution-layer-id.json` — institution type identifiers
- `cross-layer-event.json` — event envelope with institutional activation

Extend schemas here; implement parsers in child repos.

---

## Do

- Keep umbrella docs curated (quality over quantity)
- Cross-link child repos instead of copying large JSON
- Update TOPOLOGY.md when adding institutions
- Mark epistemic level on every institutional claim

## Do not

- Commit secrets, `.env`, credentials
- Copy `errorlogy_unified_taxonomy_v16.json` into this repo
- Merge product code from child repos
- Auto-merge politic-bar v0.6 taxonomy with v16

---

## Agent Retrospective & Context Rules

Эта секция нужна, чтобы агенты не «съезжали» по контексту при работе над историческими версиями (v0.6 sketches, taxonomy v16 и т.д.) и при переключении между umbrella и child репозиториями.

### Мульти-репозитории и ownership (кто хранит какой тип знаний)

AI Native Gov (`ai-native-gov`) — это umbrella / наднациональный слой **institutional topology & contracts**. Любая “продуктовая” реализация (UI/пайплайны/математические движки) живет в child репозиториях и должна подключаться ссылками, а не дублированием.

Ориентируйся по типу знания:

| Тип знания | Источник (repo) | Что делать |
|---|---|---|
| Institutional topology / рамки судов/парламента/интерпола, intersection tensions, checks & balances | `ai-native-gov` | Добавляй/обновляй docs в `docs/institutions/` и TOPOLOGY |
| Taxonomy v16 и μ/α/PNO/FPD engine math | `errorlogy/errorlogy` | Считай/генерируй в child репо, а в umbrella — только контракты/выводы (например `INSTITUTIONAL_MODEL`) |
| Error cards, politifi, signal/noise streams, UI-слои | `errorlogy/politic-bar` | Полагайся на schema/интеграционные документы umbrella |
| Verification-first сертификаты / Protocol v2 / эксперименты | `errorlogy/namm-experiments` | Ставь ссылки на результаты в umbrella, не подменяй verifiable артефакты метафорами |

### Milestones (phase / research-development как “контрольная точка”)

Планируется как последовательность Phase 0 → Phase 5 (см. `ROADMAP.md`):

1. Phase 0 — umbrella foundation: структура, core docs, baseline topology и integration docs
2. Phase 1 — child repo linkage: проверить фактические API child репозиториев и привести shared schemas в соответствие
3. Phase 2 — schema contracts: определить и версионировать ingress/egress (signal-envelope, institutional-output, forecast deltas)
4. Phase 3 — institutional depth: расширение layer’ов (ministry stubs), и “machine-readable” topology рядом с `TOPOLOGY.md`
5. Phase 4 — pipeline integration: связать umbrella output с ошибко-детекцией/валидируемыми потоками в child репах
6. Phase 5 — agent automation: PR templates, lightweight validation scripts, playbooks для типовых задач

Правило: если ты находишь “что-то недоделанное”, сначала зафиксируй какой Phase это похоже, и только потом меняй код/документы.

### Когда ты рассуждаешь: контекстный чеклист (уменьшай signal/noise)

Перед тем как писать вывод/решение:

1. **Спроси себя “какой слой?”**
   - `INSTITUTIONAL_MODEL` — umbrella фрейм/модель, не судебный приговор
   - `OPERATIONAL` — только то, что child-движок/сертификат реально считает или подтверждает
2. **Сверь версию taxonomy.**
   Используй taxonomy v16 в umbrella. “v0.6” — только как исторический артефакт для retrospective (и только в соответствующем контексте).
3. **Выбирай schema место хранения.**
   - Stubs/контракты: `schemas/` внутри umbrella
   - Парсеры/адаптеры/конкретные форматы валидации: child репы
4. **Не дублируй знания.**
   - Не копируй большие JSON/таксономии в umbrella (пример — `errorlogy_unified_taxonomy_v16.json`).
   - Не копируй код product pipeline’ов в umbrella.
5. **Ссылайся на child репы “как на источник”, а не как на ресурс для копипаста.**
   Для ссылок и ориентира обновляй `docs/integrations/` и `docs/examples/`, а не переносить архитектуру в код umbrella.

### Retrospective: как смотреть назад и переносить инсайты

1. **Найди “точку сравнения”.**
   Обычно это миграции/наброски: `v0.6 sketch (politic-bar)` → taxonomy v16 (см. `docs/integrations/POLITIC_BAR.md` и `docs/integrations/ERRORLOGY.md`).
2. **Сохрани инварианты, а не черновики.**
   - Переноси в umbrella: уроки по ownership, схеме, границам ответственности, проблемам интерпретации.
   - Не переноси в umbrella: engine math, UI реализацию, “новые версии” таксономии.
3. **Собирай “diff notes” в docs.**
   Лучше добавить пару абзацев в `docs/examples/` или `docs/integrations/`, чем менять интерпретацию в середине разработки.
4. **Проверь, что insight доходит до нужной Phase.**
   Если insight про контракт — это Phase 2. Если про routing/ownership — Phase 1/4.
5. **Сохраняй эпистемическую скромность.**
   Retrospective — для обучения агенту, а не для “повторного утверждения” юридических/моральных вердиктов.

### Common failure modes (частые ошибки)

- Смешивание taxonomy версий: v0.6 элементы трактуются как часть taxonomy v16 “по умолчанию”.
- Употребление umbrella как замены “правительств”: umbrella — это layer моделей/контрактов, а не суверенная замена институтам в реальном мире.
- Копирование кода из child репозиториев в umbrella вместо контрактных ссылок.
- Auto-merge politic-bar v0.6 taxonomy с v16 (запрещено — см. `Do not` выше).
- Попытка “встроить” verification (NAMM сертификаты) в umbrella как юридический приговор вместо маркировки `COMPUTATIONAL_EVIDENCE`.

### Ссылки (child repos / verification sources)

- umbrella: https://github.com/errorlogy/ai-native-gov
- errorlogy: https://github.com/errorlogy/errorlogy
- politic-bar: https://github.com/errorlogy/politic-bar
- errorlogy.com: https://errorlogy.com
- NAMM: https://github.com/errorlogy/namm-experiments

См. также `RETROSPECTIVE.md` (чеклист-версия инструкции).

---
## Local clones (Windows)

```powershell
# Umbrella
git clone git@github.com:errorlogy/ai-native-gov.git C:\Users\Public\AI_NATIVE_GOV

# Products (side-by-side)
git clone git@github.com:errorlogy/errorlogy.git C:\Users\Public\ERRORLOGY_MVP
git clone git@github.com:errorlogy/politic-bar.git C:\Users\Public\POLITIC_BAR
git clone git@github.com:errorlogy/namm-experiments.git C:\Users\Public\NAMM
```

---

## Example task: live-event cascade

Follow [`docs/examples/trump-macron-cascade.md`](docs/examples/trump-macron-cascade.md):

1. Anchor event in politic-bar stream model
2. Activate institutional layers (this repo)
3. Run Errorlogy engine on decision-events
4. Update politifi assets
5. Optional NAMM verification link in card metadata

---

## Links

- [errorlogy.com](https://errorlogy.com)
- [politic-bar AGENTS.md](https://github.com/errorlogy/politic-bar/blob/main/AGENTS.md)
- [errorlogy-mas AGENTS.md](https://github.com/errorlogy/errorlogy/blob/main/errorlogy-mas/AGENTS.md) (if present)
