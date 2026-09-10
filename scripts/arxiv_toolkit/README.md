# arXiv Publication Toolkit & Academic Workflow

Comprehensive toolkit for generating, verifying, compiling, and preparing scientific papers for publication on **arXiv** (including content alignment and strict LaTeX package requirements).

---

## Structure

```text
AI_NATIVE_GOV/
├── paper_templates/
│   └── arxiv_template/           # Base clean LaTeX template for preprints
│       ├── main.tex              # Main source (structured sections, math, algorithms)
│       ├── references.bib        # Verified BibTeX file
│       └── figures/              # Folder for vector (PDF) and raster (PNG) illustrations
│
└── scripts/
    └── arxiv_toolkit/
        ├── fetch_literature.py   # Literature search via arXiv API and honest BibTeX generation
        ├── generate_figures.py   # Vector figure generation (300+ DPI, serif fonts)
        ├── compile_paper.py      # Automatic compilation via latexmk / pdflatex
        ├── clean_and_package.py  # Cleanup via Google's arxiv-latex-cleaner and .tar.gz packaging
        └── README.md
```

---

## Quick start

The project virtual environment (`.venv`) already includes all required libraries (`arxiv-latex-cleaner`, `paper-qa`, `arxiv`, `semanticscholar`, `matplotlib`, `seaborn`, `bibtexparser`, `pydantic`).

### 1. Literature search and collection without hallucinations
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\fetch_literature.py -q "cognitive game theory AGI" -n 5 -o paper_templates\arxiv_template\references.bib
```

### 2. Generate academic vector figures
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\generate_figures.py
```

### 3. Compile and verify PDF locally
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\compile_paper.py -d paper_templates\arxiv_template
```

### 4. Clean and create arXiv archive
```powershell
.venv\Scripts\python scripts\arxiv_toolkit\clean_and_package.py -d paper_templates\arxiv_template
```
This produces a ready-to-upload `arxiv_template_arXiv_submission.tar.gz` file for direct submission at [arXiv.org/submit](https://arxiv.org/submit).
