"""
Example fogsift-icarus configuration.

Copy this to `config.py` at the harness root and customize for your vault.
`config.py` is gitignored — it contains your local paths.
"""

from pathlib import Path

# Where your Obsidian vault lives.
VAULT_PATH = Path.home() / "Documents" / "Personal-Remote-Vault"

# Where your code workspaces live (used by git_audit + commit_summary).
WORKSPACE_PATH = Path.home() / "Code"

# Daily note template location (relative to vault).
DAILY_NOTE_TEMPLATE = "System/00-09_system_meta/02_templates/Daily_Note_Template.md"

# Author filter for commit_summary (`git log --author=...`).
GIT_AUTHOR = "Your Name"

# Optional: PocketBase / Daily API endpoints (set to None to skip).
POCKETBASE_URL = "http://127.0.0.1:8090"
DAILY_API_URL = None

# Idempotency thresholds.
WIP_THRESHOLD_HOURS = 24  # git_audit: dirty file → WIP if mtime within N hrs
ROLLOVER_LOOKBACK_DAYS = 7  # plan_rollover: scan N days for recurring blockers

# Permissions: sections Claude is allowed to auto-fill.
AI_WRITABLE = {
    "commits_today",
    "work_efforts",
    "tomorrows_top_3",
    "sitrep",
    "research_feed",
    "captured_urls",
    "claude_session_log",
    "session_recap",
}
