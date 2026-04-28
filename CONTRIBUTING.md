# Contributing to fogsift-icarus

Thanks for your interest in contributing! Here's how to help.

## Pull Request Flow

1. Fork the repo and create a branch: `git checkout -b feature/my-feature`
2. Make your changes. Ensure code passes `ruff check .` and `ruff format --check .`
3. Write or update tests in `tests/`
4. Commit with a [Conventional Commit](https://www.conventionalcommits.org/) message:
   - `feat(engine): add version_cache eviction`
   - `fix(cli): handle write timeout`
   - `docs: update API reference`
5. Push to your fork and open a PR against `main`
6. Ensure CI passes (lint, test)
7. Wait for review and approval before merge

## Labels

Use these labels when filing issues or PRs:

**Areas:**
- `area:engine` — Core engine (atomic_io, yaml_io, daily_note, version_cache, diff)
- `area:cli` — CLI commands
- `area:plugin` — Obsidian plugin
- `area:docs` — Documentation
- `area:ci` — CI/CD and workflows

**Types:**
- `type:feat` — New feature
- `type:fix` — Bug fix
- `type:chore` — Dependencies, maintenance
- `type:refactor` — Code refactor
- `type:test` — Test improvements

**Priority:**
- `priority:p0` — Critical
- `priority:p1` — High
- `priority:p2` — Medium

**Status:**
- `status:blocked` — Blocked
- `status:in-progress` — In progress
- `status:needs-review` — Needs review

## Development Setup

```bash
# Clone and enter directory
git clone https://github.com/ctavolazzi/fogsift-icarus.git
cd fogsift-icarus

# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dev dependencies
uv pip install -e ".[dev]"

# Run lints
uv run ruff check .
uv run ruff format --check .

# Run tests
uv run pytest tests/ -v
```

## Code Style

- Use [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Follow [PEP 8](https://pep8.org/) and [Conventional Commits](https://www.conventionalcommits.org/)
- Write docstrings for public functions (Google style)
- Keep line length ≤100 characters

## Testing

- Write tests for new features in `tests/`
- Run `uv run pytest tests/ -v --cov=fogsift_icarus` before submitting
- Aim for >80% coverage on new code

## Questions?

Open an issue with the `help-wanted` label or check [GitHub Discussions](https://github.com/ctavolazzi/fogsift-icarus/discussions).

---

**Code of Conduct:** This project adheres to the [Contributor Covenant](CODE_OF_CONDUCT.md).
