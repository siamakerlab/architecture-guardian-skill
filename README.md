# Architecture Guardian Skill

Architecture Guardian is a reusable architecture governance skill for AI-assisted software development with Claude Code and OpenAI Codex.

It is not a code style checker. Its job is to make architecture impact, dependency direction, module boundaries, state ownership, and regression risk visible before and after changes.

## Purpose

Modern AI-assisted projects can drift when many small changes accumulate. A feature patch may introduce a cross-feature dependency, expose internal state, widen a public API, or move infrastructure concerns into domain logic without anyone explicitly deciding to do so.

Architecture Guardian exists to prevent that drift. It keeps development focused on:

1. Encapsulation
2. Low Coupling
3. High Cohesion
4. Explicit Dependencies
5. Single Responsibility
6. Dependency Inversion
7. Testability
8. Maintainability
9. Extensibility
10. Implementation Convenience

Implementation convenience does not override the higher priorities.

## When To Use

Use this skill for architecture-sensitive work:

- planning a new feature
- changing existing behavior
- fixing a bug with non-trivial impact
- refactoring
- reviewing implementation
- reviewing a diff, commit, or PR
- auditing a repository for architecture drift
- deciding whether a new abstraction, dependency, module, or public API is justified

## Operating Modes

- `PLAN`: before implementation
- `REVIEW`: during or after implementation review
- `CHANGE-REVIEW`: for a diff, commit, or PR
- `REFACTOR`: for behavior-preserving structure changes
- `FULL-AUDIT`: for repository-wide drift and boundary checks

Mode templates:

- [PLAN.md](core/modes/PLAN.md)
- [REVIEW.md](core/modes/REVIEW.md)
- [CHANGE-REVIEW.md](core/modes/CHANGE-REVIEW.md)
- [REFACTOR.md](core/modes/REFACTOR.md)
- [FULL-AUDIT.md](core/modes/FULL-AUDIT.md)

## Required Output

Every Architecture Guardian result should include:

- `Architecture Impact`
- `Scorecard` for reviews, change reviews, refactors, and audits
- `Findings`, if any
- `Regression Risk`
- `Tests Required`
- `Architecture Verdict`: `PASS`, `PASS WITH WARNINGS`, or `CHANGES REQUIRED`

## Scorecard

Reviews use a fixed evidence-based scorecard, not subjective ratings:

- `5`: verified pass, with evidence and relevant test, contract, or enforcement boundary
- `4`: pass, with no violation but incomplete enforcement or documentation
- `3`: localized warning without boundary, contract, lifecycle, state ownership, or regression breakage
- `2`: material architecture risk or missing verification in a medium-risk affected area
- `1`: localized violation or partial verification of a high-risk affected area
- `0`: severe violation, or an unverified high-risk affected area
- `N-A`: not scored because the item is outside scope

Scores must cite concrete evidence such as files, modules, dependency edges, public contracts, state owners, tests, or missing verification. Decimal scores, percentages, confidence scores, and subjective estimates are not used.

Scorecards are shown as a table with `Criterion`, `Score`, `Status`, `Evidence`, and `Action`, preceded by a short count summary. Averages are not shown unless explicitly requested.

Formal report template:

- [ARCHITECTURE_GUARDIAN_REPORT.md](core/reports/ARCHITECTURE_GUARDIAN_REPORT.md)

## Repository Structure

- [SKILL.md](SKILL.md): Codex skill entry point
- [agents/openai.yaml](agents/openai.yaml): Codex UI metadata
- [core/policy/ARCHITECTURE_GUARDIAN_POLICY.md](core/policy/ARCHITECTURE_GUARDIAN_POLICY.md): single source of truth
- [core/policy/ARCHITECTURE_GUARDIAN_RULESET.json](core/policy/ARCHITECTURE_GUARDIAN_RULESET.json): machine-readable rules
- [core/modes](core/modes): operating mode templates
- [core/reports](core/reports): report template
- [docs](docs): project architecture document templates
- [adapters](adapters): Claude Code and Codex management document pointers
- [examples](examples): connection and mode examples

Runtime skill package:

- Required: [SKILL.md](SKILL.md), [agents](agents), [core](core)
- Recommended: [adapters](adapters), [docs](docs), [examples](examples)
- Repository-only documentation: [README.md](README.md), [MVP.md](MVP.md), [LICENSE](LICENSE)

## Codex Usage

Install or place this repository where Codex can load it as a skill, then invoke:

```text
Use $architecture-guardian to analyze this change for architecture impact, dependency direction, and regression risk.
```

For project-level continuous use, add a short pointer to the target project's `AGENTS.md`:

```text
Use Architecture Guardian for architecture-sensitive work.
Policy source: core/policy/ARCHITECTURE_GUARDIAN_POLICY.md
Required flow: PLAN before implementation, REVIEW during/after implementation, CHANGE-REVIEW for diffs or PRs.
Review results must include Architecture Impact, Scorecard, Findings, Tests Required, and Architecture Verdict.
```

Adapter:

- [adapters/codex/AGENTS.md](adapters/codex/AGENTS.md)

## Claude Code Usage

For Claude Code, add a short pointer to the target project's `CLAUDE.md` instead of copying the full policy:

```text
Use Architecture Guardian for architecture-sensitive work.
Policy source: core/policy/ARCHITECTURE_GUARDIAN_POLICY.md
Required flow: PLAN before implementation, REVIEW during/after implementation, CHANGE-REVIEW for diffs or PRs.
Review results must include Architecture Impact, Scorecard, Findings, Tests Required, and Architecture Verdict.
```

Adapter:

- [adapters/claude/CLAUDE.md](adapters/claude/CLAUDE.md)

## Project Policy Templates

Use these in target repositories to make project-specific architecture rules explicit:

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/CODING_STYLE.md](docs/CODING_STYLE.md)
- [docs/MODULE_RULES.md](docs/MODULE_RULES.md)
- [docs/DEPENDENCY_RULES.md](docs/DEPENDENCY_RULES.md)

The skill prefers explicit project rules over its defaults unless those rules introduce severe risk such as circular dependencies, uncontrolled global state, data corruption, lifecycle hazards, concurrency hazards, API compatibility breaks, or architecture boundary collapse.

## Examples

- [PLAN_example.md](examples/mode-examples/PLAN_example.md)
- [REVIEW_example.md](examples/mode-examples/REVIEW_example.md)
- [FULL-AUDIT_example.md](examples/mode-examples/FULL-AUDIT_example.md)
- [examples/AGENTS.md](examples/AGENTS.md)
- [examples/CLAUDE.md](examples/CLAUDE.md)

## License

MIT. See [LICENSE](LICENSE).
