# Security Policy

## Supported Versions

`fogsift-icarus` is pre-release software (v0.0.1, not yet on PyPI). The `main` branch is the only supported version. No stable release has been published.

| Version       | Supported          |
| ------------- | ------------------ |
| main          | :white_check_mark: |
| v0.0.1        | :white_check_mark: |
| anything else | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, **please do not open a public issue**.

Email: **info@fogsift.com** with subject line `[fogsift-icarus security]`.

Include:
- Description of the vulnerability
- Steps to reproduce
- Affected version(s)
- Suggested fix (if known)

You'll receive an acknowledgment within 72 hours. Patched releases are typically published within 7 days for confirmed issues.

## Scope

`fogsift-icarus` reads and writes to a local Obsidian vault and runs git commands. Vulnerabilities of interest include:

- Path traversal in vault writes
- Command injection in git invocations
- Arbitrary file read via section-fill heuristics
- Tampering with locked plan documents

Out of scope: Obsidian itself, git, your operating system, your editor, third-party MCP servers.
