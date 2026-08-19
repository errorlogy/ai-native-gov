# Agent Retrospective Checklist (umbrella → child)

Этот чеклист помогает агентам безопасно “смотреть назад” и переносить инсайты в `AI_NATIVE_GOV`, не ломая контекст (ownership, версии taxonomy, signal/noise).

## 1) Перед началом (обязательная разметка контекста)

1. Зафиксируй, что именно было “прошлой версией”:
   - `v0.6 sketch` (часто встречается в документах politic-bar / интеграциях)
   - или текущая “каноническая” база — `taxonomy v16` (umbrella)
2. Отметь предполагаемую Phase по `ROADMAP.md`:
   - contract / schema gap → Phase 2
   - routing / ownership gap → Phase 1 или 4
   - новые layer’ы topology → Phase 3
3. Составь список источников (как ссылок, а не как “копировать”):
   - `docs/integrations/POLITIC_BAR.md` (для v0.6 sketch → миграции)
   - `docs/integrations/ERRORLOGY.md` (для привязки к v16/движку)
   - (опционально) `docs/integrations/NAMM.md` для verification-first математики

## 2) Во время retrospective (уменьшаем signal/noise)

1. Разделяй инварианты и черновики:
   - инварианты можно переносить в umbrella как правила/контракты/интерпретации
   - черновики остаются в примерах/истории, а не становятся “по умолчанию”
2. Маркируй слой выходов:
   - `INSTITUTIONAL_MODEL` = framing, гипотеза, не “юридический приговор”
   - `OPERATIONAL` / `COMPUTATIONAL_EVIDENCE` = то, что можно подтвердить вычислением/сертификатом
3. Если появляются “auto-merge” идеи:
   - остановись
   - проверь, что это не “v0.6 taxonomy” смешивается с v16 (запрещено)

## 3) Как переносить insights в правильные места

### Переносить в `AI_NATIVE_GOV` (umbrella)

- `docs/institutions/` и TOPOLOGY: когда меняется institutional topology, intersection tensions, checks & balances
- `docs/integrations/`: когда меняется контракт/интерфейс между umbrella и child репами
- `schemas/`: когда появляется новый “stubs / contracts” формат, который должны уметь парсить child репозитории
- `docs/examples/`: когда нужно описать migration/cascade “как получилось”, без переписывания engine math

### Не переносить в `AI_NATIVE_GOV`

- engine math / numeric outputs / μ/α/PNO/FPD computation (это в `errorlogy/errorlogy`)
- UI-реализацию, politifi rendering, signal stream pipeline code (это в `errorlogy/politic-bar`)
- verification certificates как verdict (это в `namm-experiments`, а в umbrella только корректная маркировка типа выхода)

## 4) Мини-шаблон заметки по итогам (в один абзац)

Скопируй и заполни:

- **Сравнение:** `v0.6 sketch` → `taxonomy v16` / или другая пара версий
- **Phase:** Phase X (`ROADMAP.md`)
- **Ownership change:** что теперь хранит umbrella vs какой child repo отвечает за computation/UI
- **Schema action:** что обновилось/должно обновиться в `schemas/` (или “ничего”)
- **Next action:** какой doc/example/contract нужно обновить и где именно

## 5) Common anti-patterns (быстрое самопроверка)

- Смешивание taxonomy версий (v0.6 трактуется как v16 “по умолчанию”)
- Umbrella воспринимается как замена “правительств” вместо reasoning/contract layer
- Код копируется из child реп в umbrella вместо ссылки/интеграционного контракта
- Verification используется как юридический приговор вместо эпистемических labels (`COMPUTATIONAL_EVIDENCE`)

