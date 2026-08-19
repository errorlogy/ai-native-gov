# WORKSPACE — Primary Onboarding

This document is the **main project guide**. AI Native Gov is the root context; child repos are referenced, not duplicated.

## Philosophy

- **Work FROM** `C:\Users\Public\AI_NATIVE_GOV` in Cursor — strategy, topology, schemas, integration contracts live here.
- **Implement IN** child repos (`repos/errorlogy`, `repos/politic-bar`, etc.) — code, pipelines, UI.
- **Agents** should treat this folder as home base; open child repos only when implementation requires it.

## Folder roles

| Path | Role |
|------|------|
| Root (`*.md`) | Vision, architecture, roadmap, agent instructions |
| `docs/institutions/` | Institutional models — parliament, courts, interpol, topology |
| `docs/integrations/` | Contracts with Errorlogy, politic.bar, NAMM |
| `docs/examples/` | End-to-end scenario walkthroughs |
| `schemas/` | Shared JSON/YAML contracts (cross-repo) |
| `repos/` | Optional local clones of child repos |
| `.cursor/rules/` | Cursor agent context rules |

## Clone child repos

From PowerShell:

```powershell
cd C:\Users\Public\AI_NATIVE_GOV
mkdir repos -Force
git clone https://github.com/errorlogy/errorlogy.git repos/errorlogy
git clone https://github.com/errorlogy/politic-bar.git repos/politic-bar
```

Alternative: keep siblings outside `repos/`:

```
C:\Users\Public\
├── AI_NATIVE_GOV/     ← umbrella (this repo)
├── errorlogy/         ← sibling clone
└── politic-bar/       ← sibling clone
```

Both layouts work. Document which you use in your local notes; agents should check both `repos/` and `C:\Users\Public\` siblings.

## Agent session workflow

### Starting a session

1. Open **this folder** in Cursor (`AI_NATIVE_GOV`).
2. Agent reads `AGENTS.md` + this file (via `.cursor/rules/`).
3. State the task domain: institutions / integration / child repo implementation.

### Umbrella work (stay here)

- Institutional topology changes → `docs/institutions/`
- Integration contracts → `docs/integrations/`
- Shared schemas → `schemas/`
- Architecture decisions → `ARCHITECTURE.md`, `ROADMAP.md`

### Implementation work (child repos)

- Error pipelines, forecast models → `repos/errorlogy` or sibling
- Politifi UI, signal streams → `repos/politic-bar` or sibling
- When editing child code, **reference** umbrella contracts; don't copy topology docs into child repos.

### Cross-repo changes

1. Update contract/schema in umbrella first.
2. Implement in child repo.
3. Link both in commit messages or PR descriptions.

## Git remotes

| Repo | Remote |
|------|--------|
| Umbrella | `https://github.com/errorlogy/ai-native-gov` (private) |
| Errorlogy | `https://github.com/errorlogy/errorlogy` |
| politic.bar | `https://github.com/errorlogy/politic-bar` |

## Daily commands

```powershell
# Status
cd C:\Users\Public\AI_NATIVE_GOV
git status
git pull

# Pull child repo
git -C repos/errorlogy pull

# Push umbrella changes
git add -A
git commit -m "docs: update institution topology"
git push origin main
```

## What not to do

- Don't duplicate `docs/institutions/` into child repos.
- Don't store secrets in this repo (.env, tokens, credentials).
- Don't force-push `main`.

## Next steps after setup

1. Clone child repos (commands above).
2. Read [VISION.md](VISION.md) and [docs/institutions/TOPOLOGY.md](docs/institutions/TOPOLOGY.md).
3. Pick a roadmap item from [ROADMAP.md](ROADMAP.md).
4. Run an agent session from this window with a concrete task.
