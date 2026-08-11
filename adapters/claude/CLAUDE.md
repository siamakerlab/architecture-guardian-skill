# CLAUDE.md (Architecture Guardian Adapter)

Use this as a short pointer in a project's top-level `CLAUDE.md`.

## Mandatory behavior
1. Load core policy from `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md` in this repository.
2. Before any code/task proposal, perform PLAN mode using `core/modes/PLAN.md`.
3. During implementation, run REVIEW checkpoints from `core/modes/REVIEW.md`.
4. After significant change, run `core/modes/CHANGE-REVIEW.md`.
5. Weekly or release boundary checkpoint: run FULL-AUDIT mode template.
6. Every report must follow `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md`.
7. REVIEW, CHANGE-REVIEW, REFACTOR, and FULL-AUDIT outputs must include evidence-based Scorecard with `0-5` or `N-A`.
8. Keep output focused on required architecture judgment: impact, scorecard, findings, required tests, and verdict.

## Do not copy
Do not paste the full Architecture Guardian policy into `CLAUDE.md`. Keep the project management document short and point to the single policy source.

## Scope rule
Do not create tool-specific patterns. Apply only shared architectural rules from the policy and defer stack-specific rules to project docs when present.

## Priority override
Use higher-level policy priorities before project convenience, except when project policy explicitly and safely defines different priorities.
