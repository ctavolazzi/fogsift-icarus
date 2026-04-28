# Architecture

fogsift-icarus is a harness that maintains an invariant: **the vault is a faithful representation of the working mind**.

## The Three Loops

```text
┌─────────────────────────────────────────────────────────┐
│  Morning Loop (/spin-up)                                │
│  ────────────────────────                               │
│  preflight.py  →  spin_up.py  →  plan_rollover.py       │
│  (7-cat check)   (fill note)     (seed today's plan)    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  Day Loop (/wagonwheel — anytime)                       │
│  ────────────────────────────────                       │
│  hub.update()  →  spokes.upsert()  →  rim.link()        │
│  (session state)  (per thread)        (cross-references)│
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  Evening Loop (/wrap-up)                                │
│  ────────────────────────                               │
│  fill_sections.py  →  vault_commit.py  →  daily_plan.lock()│
│  (commits, top 3)    (smart message)     (read-only)    │
└─────────────────────────────────────────────────────────┘
```

## Modules

| Module | Single Responsibility |
| --- | --- |
| `daily_note.py` | Section read/write API with `AI_WRITABLE` permission set |
| `daily_plan.py` | Plan lifecycle: create / lock / unlock / extract unchecked |
| `plan_rollover.py` | Analyze N days of locked plans; detect 3+ day blockers |
| `fill_sections.py` | Idempotent section filler for `commits_today`, `work_efforts`, etc. |
| `vault_commit.py` | Smart-message vault commit, wrapped in `vault_lock()` |
| `git_audit.py` | Cross-repo dirty scan, classify WIP vs. stale by mtime |
| `capture_url.py` | URL → vault doc, GitHub-aware metadata extraction |
| `claude_journal.py` | Inner-voice journal append for realizations + open questions |
| `preflight.py` | 7-category readiness battery (HALT/FAIL/WARN/PASS) |
| `harness_lib.py` | Shared helpers: `discover_repos`, `classify_mtime`, `iso_now` |
| `atomic_io.py` | `vault_lock()` ctx + `atomic_write()` for concurrency safety |
| `harness_log.py` | SQLite telemetry to `state.db` |

## Invariants

1. **Parent chain.** Every doc has `parent:` pointing up. Walk up from any spoke → daily note → vault index. No orphans.
2. **Plan lock.** Once `wrap_up.py` locks today's plan, it's read-only. Rollover reads it as a source.
3. **Hub idempotency.** `Hubs/<date>_hub.md` is one file per day. Re-runs increment `hub_count`, never duplicate.
4. **Section permission.** `write_section(actor="claude")` rejects sections not in `AI_WRITABLE`. Only manual sections need human edit.
5. **Atomic writes.** All vault writes go through `atomic_write()` (write to `.tmp`, fsync, rename).

## Epistemic Gate

Write operations open an `empirica` transaction with self-assessed vectors (`know`, `uncertainty`). Operations that bypass the gate are logged as **epistemic dark matter** — work performed without a measured confidence level. The transaction closes with a `PROCEED / HALT / BRANCH / REVISE` decision.

## Telemetry

Every `harness_log.log_op(action, actor, target, result)` call writes a row to `state.db`. The preflight battery reads recent rows to compute the readiness score. The score gates whether spin-up should auto-proceed or HALT for review.

## Why Stdlib-First

Heavy dependencies break in three places: install time (slow), upgrade time (security), and offline time (impossible). The harness chooses Python stdlib for I/O, subprocess for git, file globs for vault traversal. Three optional integrations (PocketBase, Daily API, Open-Meteo) are network probes only — failures degrade gracefully to WARN.
