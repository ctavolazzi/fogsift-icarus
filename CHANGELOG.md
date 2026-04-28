# Changelog

All notable changes to fogsift-icarus will be documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

---

## [0.0.1] — 2026-04-27

### Added

- Initial README documenting the full harness architecture
- Daily ritual flow: `spin_up` → `/wagonwheel` → `wrap_up`
- Plan lifecycle documentation (create → active → lock → rollover)
- Hub-and-spoke session state system (`/wagonwheel` command)
- Preflight battery (7 categories: A–G)
- Core modules documented:
  - `preflight.py` — 7-category readiness gate
  - `spin_up.py` / `wrap_up.py` — morning/evening orchestrators
  - `daily_note.py` — section read/write API with AI permission model
  - `daily_plan.py` / `plan_rollover.py` — plan lifecycle
  - `fill_sections.py` — fill empty daily note sections on demand
  - `vault_commit.py` — one-shot vault commit with smart message heuristic
  - `git_audit.py` — categorize dirty paths as WIP vs. stale
  - `capture_url.py` — URL-to-vault capture (GitHub-aware)
  - `claude_journal.py` — inner-voice journal for Claude
  - `harness_lib.py` — shared helpers (discover_repos, classify_mtime, iso_now)
- Architectural philosophy: vault as faithful representation of the working mind
- Parent-chain schema: every vault doc traces to `[[00.00_vault_index]]`
- JD domain hubs 10–90 for work effort orientation

### Notes

This is a documentation-first release. The harness code lives in  
`_experiments/SimpleAgentOS/` and `active/waft/src/waft/` and is in  
daily active use. Packaging for general install is planned for v0.1.0.
