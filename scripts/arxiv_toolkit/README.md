# arXiv Publication Toolkit & Academic Workflow

Комплексный инструментарий для генерации, верификации, компиляции и подготовки научных статей к публикации на **arXiv** (включая соответствие по содержанию и строгим требованиям к LaTeX-пакету).

---

## 📁 Структура

```text
AI_NATIVE_GOV/
├── paper_templates/
│   └── arxiv_template/           # Базовый чистый LaTeX-шаблон для препринтов
│       ├── main.tex              # Главный исходник (структурированные секции, математика, алгоритмы)
│       ├── references.bib        # Верифицированный BibTeX файл
│       └── figures/              # Папка для векторных (PDF) и растровых (PNG) иллюстраций
│
└── scripts/
    └── arxiv_toolkit/
        ├── fetch_literature.py   # Поиск литературы через arXiv API и генерация честного BibTeX
        ├── generate_figures.py   # Генерация векторных графиков (300+ DPI, serif шрифты)
        ├── compile_paper.py      # Автоматическая компиляция через latexmk / pdflatex
        ├── clean_and_package.py  # Очистка через Google's arxiv-latex-cleaner и упаковка в .tar.gz
        └── README.md
```

---

## 🚀 Быстрый старт

Виртуальное окружение проекта (`.venv`) уже содержит все необходимые библиотеки (`arxiv-latex-cleaner`, `paper-qa`, `arxiv`, `semanticscholar`, `matplotlib`, `seaborn`, `bibtexparser`, `pydantic`).

### 1. Поиск и сбор литературы без галлюцинаций
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\fetch_literature.py -q "cognitive game theory AGI" -n 5 -o paper_templates\arxiv_template\references.bib
```

### 2. Генерация академических векторных графиков
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\generate_figures.py
```

### 3. Компиляция и локальная проверка PDF
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\compile_paper.py -d paper_templates\arxiv_template
```

### 4. Очистка и создание архива для arXiv
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\clean_and_package.py -d paper_templates\arxiv_template
```
В результате будет создан готовый файл `arxiv_template_arXiv_submission.tar.gz`, готовый к прямой загрузке на [arXiv.org/submit](https://arxiv.org/submit).
