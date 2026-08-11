---
name: architecture-guardian
description: Architecture governance for AI-assisted software development. Use when Codex or Claude Code needs to plan, implement, review, refactor, audit, or analyze changes for architecture impact, dependency direction, encapsulation, module boundaries, regression risk, state ownership, public contracts, or project architecture drift.
---

# Architecture Guardian

Use this skill to keep a project's architecture stable while features, fixes, reviews, and refactors continue over time.

Treat this file as the runtime entry point. Treat `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md` as the authoritative policy reference.

## Operating Rule

Prefer the project's explicit architecture rules over this skill's defaults. If project rules create severe risk such as circular dependencies, uncontrolled global state, data corruption, lifecycle hazards, concurrency hazards, API breakage, or boundary collapse, report the conflict instead of silently following it.

## Required First Pass

Before planning or reviewing a change, inspect existing project guidance if present:

- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `CONTRIBUTING.md`
- `docs/ARCHITECTURE.md`
- `docs/CODING_STYLE.md`
- `docs/MODULE_RULES.md`
- `docs/DEPENDENCY_RULES.md`

Also check similarly named architecture, module, dependency, or contribution documents. Do not invent project rules when documents are missing.

## Core Priority

Apply these in order:

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

Implementation convenience never overrides a higher priority.

## Mode Selection

Use one mode per request:

- PLAN: before implementing a new feature, bug fix, behavior change, or architecture change.
- REVIEW: when asked to review current implementation.
- CHANGE-REVIEW: when analyzing a diff, commit, or PR.
- REFACTOR: when proposing structure changes while preserving behavior.
- FULL-AUDIT: when auditing the whole repository for drift, coupling, and boundary violations.

Mode templates live in `core/modes/`. Read only the relevant mode file unless the task requires more.

Read the full core policy when:

- the request is a formal architecture audit
- project rules conflict with implementation
- a finding may be HIGH severity
- dependency direction, state ownership, or public contract impact is ambiguous

## Required Output

Every mode must include:

- Architecture Impact
- Scorecard for REVIEW, CHANGE-REVIEW, REFACTOR, and FULL-AUDIT
- Findings, if any
- Regression Risk
- Tests Required
- Architecture Verdict: `PASS`, `PASS WITH WARNINGS`, or `CHANGES REQUIRED`

Use `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md` as the report shape when the user asks for a formal report.

## Scoring

When a mode requires a scorecard, score each applicable item with the fixed rubric:

- `5`: Verified pass. Evidence shows no violation and the relevant test, contract, or enforcement boundary is present where applicable.
- `4`: Pass. Evidence shows no violation, but enforcement or documentation is incomplete.
- `3`: Warning. Evidence shows a localized weakness without boundary, contract, lifecycle, state ownership, or regression breakage.
- `2`: Risk. Evidence shows material architecture risk or missing verification in a medium-risk affected area.
- `1`: Serious risk. Evidence shows a localized violation or partial verification of a high-risk affected area.
- `0`: Fail. Evidence shows a severe violation, or a high-risk affected area is unverified.
- `N-A`: Not scored. The item is outside the change or review scope.

Do not use decimal scores, confidence scores, or subjective estimates. Each numeric score must cite concrete evidence such as a file, module, dependency edge, public contract, state owner, test, or missing verification.

High-risk affected area means any affected area with a HIGH finding, regression risk HIGH, or changes to public contract, state ownership, persistence format, concurrency behavior, lifecycle behavior, security boundary, or cross-feature dependency. Medium-risk affected area means a changed area with MEDIUM finding, dependency broadening, public API growth, shared/common code growth, reduced testability, or unclear side effects.

Use the evidence matrix in `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md` when a score is disputed or ambiguous.

Show scorecards as a table with columns: `Criterion`, `Score`, `Status`, `Evidence`, `Action`. Include a short score summary before the table: `5`, `4`, `3`, `2`, `1`, `0`, `N-A` counts. Do not show an average unless explicitly requested.

## Findings Policy

Always report all HIGH findings. Report MEDIUM findings that materially affect design, regression risk, or maintainability. LOW findings should not drive broad refactors and may be omitted unless requested.

HIGH examples:

- module or layer boundary violation
- feature-to-feature implementation dependency
- circular dependency
- leaked mutable state
- dependency inversion violation
- unexpected public contract change
- state ownership ambiguity
- lifecycle or concurrency hazard

MEDIUM examples:

- excessive coupling
- low cohesion
- duplicated responsibility
- hidden dependency
- overly broad interface
- unnecessary shared/common abstraction
- difficult-to-test structure
- unclear side effects

## Architecture Impact Checklist

For each change, evaluate:

- affected modules, classes, interfaces, and public contracts
- new, removed, or redirected dependencies
- direct and transitive dependency effects
- state ownership and lifecycle effects
- persistence, network, external API, UI, and test impact
- existing consumers and backward compatibility
- migration need and regression surface

If there is no meaningful impact, state: `No meaningful architecture impact`.

## Management Document Guidance

When applying this skill to a project, add only a short pointer in the project's management documents:

- `AGENTS.md` for Codex
- `CLAUDE.md` for Claude Code
- `docs/ARCHITECTURE.md`, `docs/MODULE_RULES.md`, and `docs/DEPENDENCY_RULES.md` for project-specific rules

The pointer should reference this skill's single policy source instead of copying the full policy. Use adapter examples from `adapters/` when creating those pointers.

Recommended pointer:

```text
Use Architecture Guardian for architecture-sensitive work.
Policy source: core/policy/ARCHITECTURE_GUARDIAN_POLICY.md
Required flow: PLAN before implementation, REVIEW during/after implementation, CHANGE-REVIEW for diffs or PRs.
Review results must include Architecture Impact, Scorecard, Findings, Tests Required, and Architecture Verdict.
```

## Resource Map

- Core policy: `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md`
- Machine-readable rules: `core/policy/ARCHITECTURE_GUARDIAN_RULESET.json`
- Modes: `core/modes/`
- Report template: `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md`
- Project document templates: `docs/`
- Claude and Codex adapters: `adapters/`
