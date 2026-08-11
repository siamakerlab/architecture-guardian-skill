# Changelog

This project follows Semantic Versioning for release tags.

## Unreleased

No unreleased changes.

## v1.0.2

Patch release for standalone skill validation.

- Removes dependency on external skill validators from install and release guidance.
- Adds `scripts/validate.py` as the repository-owned validation command.
- Updates GitHub Actions to use the repository-owned validator.

## v1.0.1

Patch release for public distribution cleanup.

- Excludes local Codex and Claude management files from the repository package.
- Adds `.gitignore` rules for local `.codex/`, `.claude/`, `AGENTS.md`, and `CLAUDE.md`.

## v1.0.0

Initial stable release.

- Provides the Architecture Guardian runtime skill entry point.
- Provides reusable architecture policy, mode templates, report template, and machine-readable ruleset.
- Provides Codex and Claude Code adapter examples.
- Provides project architecture document templates.
- Provides install, update, and versioning guidance.
