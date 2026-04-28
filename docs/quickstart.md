# Quickstart

Get fogsift-icarus running in under 5 minutes.

## Install

```bash
pip install fogsift-icarus
```

Verify:

```bash
icarus --version
icarus info
```

## Concept

`fogsift-icarus` is a daily ritual. Three commands form the loop:

| Command | When | Does |
| --- | --- | --- |
| `/spin-up` | Morning | Preflight + populate today's daily note |
| `/wagonwheel` | Anytime | Crystallize current chat state into vault |
| `/wrap-up` | Evening | Lock plan, fill commits, tomorrow's top 3 |

These slash commands live in your Claude Code config and invoke the harness Python modules.

## Vault Structure

Set up an Obsidian vault with this layout:

```text
YourVault/
├── Daily Notes/YYYY-MM-DD.md
├── Plans/YYYY-MM-DD_daily_plan.md
├── Hubs/YYYY-MM-DD_hub.md
├── Claude Journal/YYYY-MM-DD.md
├── Captured/
└── _work_efforts_/
    ├── 10-19_development/
    ├── 20-29_testing/
    └── ...
```

Point the harness at it via a `config.py` (see [example](../examples/config.example.py)).

## First Run

1. Open today's daily note (use the template in `System/00-09_system_meta/02_templates/`).
2. Run `python3 -m fogsift_icarus.preflight` to verify all subsystems.
3. Run `python3 -m fogsift_icarus.spin_up` to populate sections.
4. Work normally. Capture URLs as they come up. Run `/wagonwheel` when productive.
5. End the day with `/wrap-up`.

## Next

- Read [the architecture overview](../README.md#architecture) for the full picture.
- Browse [examples/](../examples/) for working configurations.
- Open a [discussion](https://github.com/ctavolazzi/fogsift-icarus/discussions) with questions.
