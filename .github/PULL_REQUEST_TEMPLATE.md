## What this changes

<!-- One-line summary. -->

## Why

<!-- The problem this solves or the capability it adds. -->

## How to verify

<!-- Steps to test. Include test commands if applicable. -->

```bash
# example
uv run pytest tests/ -v
```

## Checklist

- [ ] Tests added or updated
- [ ] CHANGELOG.md updated under `[Unreleased]`
- [ ] No new heavy dependencies (stdlib-first)
- [ ] CLI tools have `--json` flag (if applicable)
- [ ] Idempotent — safe to run twice (if write operation)
