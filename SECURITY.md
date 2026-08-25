# Security Policy

## Reporting a vulnerability

Open a [GitHub issue](https://github.com/errorlogy/ai-native-gov/issues) with the
**security** label. Do not commit secrets, API keys, or live credentials in issues
or pull requests.

This repository holds **institutional topology, integration contracts, and schema
stubs** — not production runtime. Report issues that affect contract integrity,
misleading institutional framing, or accidental secret exposure in documentation.

## Secrets and documentation hygiene

- **Never commit** `.env`, API keys, OAuth client secrets, JWT signing keys, or
  personal access tokens.
- Do not paste live credentials into `docs/`, `schemas/`, or example curl blocks.
- Use placeholders (`YOUR_TOKEN`, `localhost`) in integration guides; link to child
  repos for runtime `.env.example` files.
- If a secret was ever committed, **rotate/revoke** it with the provider immediately
  and redact from history per GitHub guidance.

## Integration contract safety

When editing cross-repo contracts (`schemas/`, `docs/integrations/`):

1. Keep `epistemic_label` requirements explicit — institutional outputs are
   `INSTITUTIONAL_MODEL`, not legal verdicts.
2. Do not copy large taxonomy JSON from [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy)
   into this repo; reference child repos instead.
3. Document auth expectations in integration guides; runtime auth lives in child
   repos (see [ERRORLOGY.md](docs/integrations/ERRORLOGY.md)).

## Supported versions

Security fixes for documentation and schema contracts are applied on `main`.
Older tags may not receive backports.
