# fogsift-icarus

[![PyPI version](https://img.shields.io/pypi/v/fogsift-icarus.svg)](https://pypi.org/project/fogsift-icarus/)
[![Python](https://img.shields.io/pypi/pyversions/fogsift-icarus.svg)](https://pypi.org/project/fogsift-icarus/)
[![Downloads](https://img.shields.io/pypi/dm/fogsift-icarus.svg)](https://pypi.org/project/fogsift-icarus/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/ctavolazzi/fogsift-icarus/actions/workflows/ci.yml/badge.svg)](https://github.com/ctavolazzi/fogsift-icarus/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

> An AI-augmented daily workflow system.  
> Never lose another thought.

**v0.0.1 — Initial Release** · [Changelog](CHANGELOG.md) · [PyPI](https://pypi.org/project/fogsift-icarus/)

---

## Install

```bash
pip install fogsift-icarus
```

```bash
icarus --version   # fogsift-icarus 0.0.1
icarus info        # links + harness location
```

---

## What It Is

**fogsift-icarus** is the harness that runs your day alongside Claude.

It's a set of Python tools that connect your Obsidian vault, your git repos, and Claude Code into a single daily ritual. Morning to evening: gather context, fill your note, plan your work, build things, crystallize session state, lock the plan, commit the vault.

The core idea: **your vault is a faithful representation of your working mind**. The harness keeps it that way automatically.

---

## The Daily Ritual

```text
Morning                         Evening
───────                         ───────
/spin-up                        /wrap-up
  ↓                               ↓
preflight.py         →    fill_sections.py
spin_up.py           →    vault_commit.py
plan_rollover.py     →    daily_plan.lock()

                 Work
                 ────
            /wagonwheel (anytime)
                 ↓
              Hub + Spokes
              (session state crystallized to vault)
```

**Morning:** `/spin-up` runs a preflight check across 7 categories (harness integrity, vault state, data sources, epistemic health, environment, work context, readiness gate), then populates today's daily note with weather, news, arXiv feed, music pick, git status, and waft being state. Today's plan seeds from yesterday's unchecked items.

**During the day:** Paste a URL → `capture_url.py` saves it to the vault. Run `/wagonwheel` anytime a stretch of work is worth preserving — it writes a hub doc + spoke docs to the vault so a fresh Claude chat can resume from the daily note alone.

**Evening:** `/wrap-up` writes commits and tomorrow's top 3, locks the plan (read-only from here), and commits the vault.

---

## Components

| Module | Does |
| --- | --- |
| `preflight.py` | 7-category readiness check. HALT/FAIL/WARN/PASS per check. |
| `spin_up.py` | Morning orchestrator. Populates daily note. Creates today's plan. |
| `wrap_up.py` | Evening orchestrator. Fills commits section, locks plan, vault backup. |
| `daily_note.py` | Section read/write API for the daily note. Permission model (AI_WRITABLE). |
| `daily_plan.py` | Plan lifecycle: create, lock, unlock, rollover extraction. |
| `plan_rollover.py` | Analyze N days of locked plans. Detect recurring blockers. Seed today. |
| `fill_sections.py` | Fill empty daily note sections on demand (commits, work efforts, top 3). |
| `vault_commit.py` | One-shot vault commit with smart message heuristic. |
| `git_audit.py` | Categorize dirty paths across all ~/Code repos as WIP vs. stale. |
| `capture_url.py` | URL → vault capture. GitHub-aware. Appends wikilink to daily note. |
| `claude_journal.py` | Claude's inner-voice journal. Realizations, open questions, threads. |
| `harness_lib.py` | Shared: `discover_repos()`, `classify_mtime()`, `iso_now()`. |

---

## Architecture

```text
Obsidian Vault (Personal-Remote-Vault/)
├── Daily Notes/YYYY-MM-DD.md        ← entry point
│   ├── plan: [[Plans/...]]
│   ├── journal: [[Claude Journal/...]]
│   └── hub: [[Hubs/YYYY-MM-DD_hub]]
│
├── Hubs/
│   ├── YYYY-MM-DD_hub.md            ← session state (hub)
│   └── 10_hub.md … 90_hub.md       ← JD domain orientation docs
│
├── Plans/YYYY-MM-DD_daily_plan.md   ← active today, locked at EOD
├── Claude Journal/YYYY-MM-DD.md     ← inner voice, realizations
├── Captured/                        ← URL captures
└── _work_efforts_/                  ← Johnny Decimal work tracking
    ├── 10-19_development/
    ├── 20-29_testing/
    ├── 30-39_security/
    └── 40-49_creative_assets/

SimpleAgentOS/ (harness code)
├── preflight.py
├── spin_up.py
├── wrap_up.py
├── daily_note.py        ← section API + permission model
├── daily_plan.py
├── plan_rollover.py
├── fill_sections.py
├── vault_commit.py
├── git_audit.py
├── capture_url.py
├── claude_journal.py
├── harness_lib.py
├── atomic_io.py         ← vault_lock() + atomic_write()
├── harness_log.py       ← telemetry to state.db
└── tests/
```

**Parent chain:** Every vault doc has `parent:` pointing up to the daily note → vault index. No orphans. Walk up from any spoke to reach the entry point.

**Epistemic gate:** `empirica` sentinel gates (PROCEED/HALT/BRANCH/REVISE) wrap write operations. Every session opens a transaction with self-assessed vectors (know, uncertainty). Unmeasured work is logged as epistemic dark matter.

---

## Plan Lifecycle

```text
spin_up.py creates today's plan
    ↓
plan is ACTIVE — editable, living document
    ↓ (all day)
Work happens. Thoughts captured in ## Preserved Thoughts.
Artifacts linked in ## Satellites Spun Off.
    ↓
wrap_up.py locks plan at EOD
    ↓
Plan is READ-ONLY. Rollover report written into file.
    ↓ (next morning)
plan_rollover.py seeds tomorrow's plan from unchecked items.
Recurring blockers (3+ days same item) flagged.
```

The plan is a container for one day only. After lock it's a source — never a destination.

---

## Hub & Spoke Session State

`/wagonwheel` crystallizes the current chat session into the vault:

- **Hub** (`Hubs/YYYY-MM-DD_hub.md`) — continuation brief. One per day. Idempotent — multiple runs update the same file, incrementing `hub_count`.
- **Spokes** (`_work_efforts_/10-19_development/10_core/`) — one doc per active thread, with `parent:` + `hub:` frontmatter.
- **Rim** — wikilinks between related spokes in their `related:` fields.
- **Daily note** wired: `hub:` field + Container callout link + Quick Links entry.

A fresh Claude chat reading the daily note can follow links to the hub, read "Where We Are" in under 2 minutes, and be productive.

---

## Preflight Categories

| ID | Category | Covers |
| --- | --- | --- |
| A | Harness Integrity | imports, deps, cache/runs dirs, PocketBase, Daily API |
| B | Vault & Daily Note | vault exists, repo privacy, section fill ratio, dirty status |
| C | Data Sources | weather/news/music/arxiv module health + cache freshness |
| D | Epistemic | open empirica transactions, memory freshness, reflex checkpoint |
| E | Environment | disk, git dirty, branch, MCP, Python |
| F | Work Context | devlog tail, active work efforts, commits today |
| G | Readiness Gate | synthesized score + next-action recommendation |

---

## Philosophy

1. **Never lose another thought.** Captured URLs, preserved thoughts, satellites, journal entries — all routes lead to the vault.
2. **The vault is a faithful representation of the working mind.** Spin-up gathers external state into the vault. `/wagonwheel` crystallizes internal session state. Both maintain the invariant.
3. **Additive, not destructive.** Plans lock, never delete. Rollover preserves. The trail is always walkable backwards.
4. **The harness IS the product.** fogsift-icarus is not a note-taking app. It's the scaffolding that keeps Claude and human in sync across sessions.

---

## Status

`v0.0.1` — **released**. In daily active use.  
Packaging for general install is live. Full harness extraction and config system coming in v0.1.0.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

*fogsift-icarus · [FogSift](https://fogsift.com) · [ctavolazzi](https://github.com/ctavolazzi)*
