# Contributing to fogsift-icarus

## Setup

```bash
git clone https://github.com/ctavolazzi/fogsift-icarus
cd fogsift-icarus
uv pip install -e ".[dev]"
```

## Running tests

```bash
uv run pytest tests/ -v
```

## Principles

1. **Never lose another thought** — every change should preserve or improve capture fidelity.
2. **Additive over destructive** — new files, not silent overwrites.
3. **Vault is source of truth** — changes to harness logic must reflect in vault state.
4. **Idempotent by default** — every tool that writes should be safe to run twice.

## Submitting changes

1. Fork the repo
2. Create a branch: `git checkout -b feat/your-idea`
3. Write tests for new behavior
4. Open a PR against `main`

## Style

- Python 3.10+ type hints
- stdlib-first — no heavy deps
- `--json` flag on all CLI tools
- No side effects at module import
