# AGENTS.md (Architecture Guardian Adapter)

Use this as a short pointer in a project's top-level `AGENTS.md`.

## Mandatory behavior
1. Read and apply shared policy from `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md`.
2. For each change, execute at least:
- PLAN checklist
- Architecture Impact section
- post-change self-review questions
3. For reviews of diffs, follow `core/modes/CHANGE-REVIEW.md`.
4. For architecture risk, use `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md` format with Severity, Risk, Recommendation, Regression Risk, Tests Required.
5. REVIEW, CHANGE-REVIEW, REFACTOR, and FULL-AUDIT outputs must include evidence-based Scorecard with `0-5` or `N-A`.
6. Keep output focused on required architecture judgment: impact, scorecard, findings, required tests, and verdict.

## Do not copy
Do not paste the full Architecture Guardian policy into `AGENTS.md`. Keep the project management document short and point to the single policy source.

## Governance rule
Avoid project-specific hardcoded assumptions about framework internals.
Favor explicit dependencies, narrow APIs, ownership clarity, and regression-safe changes.
