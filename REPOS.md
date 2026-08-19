# Repos — Child Repository Map

## Umbrella (this repo)

| Field | Value |
|-------|-------|
| Name | `ai-native-gov` |
| GitHub | https://github.com/errorlogy/ai-native-gov |
| Local | `C:\Users\Public\AI_NATIVE_GOV` |
| Visibility | Private |
| Role | Strategy, institutions, integrations, schemas |

## Child repos

### errorlogy

| Field | Value |
|-------|-------|
| GitHub | https://github.com/errorlogy/errorlogy |
| Clone | `git clone https://github.com/errorlogy/errorlogy.git repos/errorlogy` |
| Role | Error detection, forecasts, signal validation |
| Integration doc | [docs/integrations/ERRORLOGY.md](docs/integrations/ERRORLOGY.md) |

### politic-bar

| Field | Value |
|-------|-------|
| GitHub | https://github.com/errorlogy/politic-bar |
| Clone | `git clone https://github.com/errorlogy/politic-bar.git repos/politic-bar` |
| Role | Politifi surfaces, real-time signal streams |
| Integration doc | [docs/integrations/POLITIC_BAR.md](docs/integrations/POLITIC_BAR.md) |

### NAMM experiments

| Field | Value |
|-------|-------|
| Location | Variable — see [docs/integrations/NAMM.md](docs/integrations/NAMM.md) |
| Role | Experimental modeling, prototype ingress |
| Clone | Document when repo is formalized |

## Clone all (PowerShell)

```powershell
cd C:\Users\Public\AI_NATIVE_GOV
mkdir repos -Force
git clone https://github.com/errorlogy/errorlogy.git repos/errorlogy
git clone https://github.com/errorlogy/politic-bar.git repos/politic-bar
```

## Sibling layout (alternative)

```
C:\Users\Public\
├── AI_NATIVE_GOV/
├── errorlogy/          ← git clone https://github.com/errorlogy/errorlogy.git
└── politic-bar/        ← git clone https://github.com/errorlogy/politic-bar.git
```

## Dependency direction

```
ai-native-gov (contracts, topology)
        │
        ├──► errorlogy (implements validation/forecast)
        └──► politic-bar (implements streams/UI)
```

Child repos depend on umbrella **contracts**, not vice versa. Umbrella does not import child code.

## Adding a new child repo

1. Document here and in [WORKSPACE.md](WORKSPACE.md)
2. Add integration doc under `docs/integrations/`
3. Add schema under `schemas/` if shared data is involved
4. Update [ROADMAP.md](ROADMAP.md)
