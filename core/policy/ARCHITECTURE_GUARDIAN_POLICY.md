# Architecture Guardian Policy (Single Source of Truth)

## 1. Purpose
Architecture Guardian is not a style checker. It is a change-risk and architecture-governance skill.
Its mission is to keep long-term architecture properties stable while allowing continuous delivery.

## 2. Core Priority (highest -> lowest)
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

No lower-priority rule can override a higher-priority one.

## 3. Object-Oriented Design Policy
### Preferred
- Composition over inheritance
- Encapsulated state
- Explicit interfaces/contracts
- Dependency inversion
- Constructor injection
- Immutable state where possible
- Small cohesive objects
- Narrow public APIs
- Clear ownership
- Explicit lifecycle
- Explicit side effects

### Avoid
- God Class
- Deep inheritance chains
- Global mutable state
- Service Locator overuse
- Singleton as shared mutable state
- Cross-feature direct reference to implementation classes
- Public mutable fields/state
- Unrelated responsibility Utility/Manager classes
- Hidden dependency
- Overly broad interfaces
- Leakage of implementation details

## 4. Required Operating Modes
Available modes: PLAN, REVIEW, CHANGE-REVIEW, REFACTOR, FULL-AUDIT.
Each mode must emit the required Architecture Guardian fields. Use the formal report template only when the user asks for a formal report or when the mode is REVIEW, CHANGE-REVIEW, REFACTOR, or FULL-AUDIT.

## 5. Mandatory Discovery Process
Before change or review, inspect existing documents if present:
- AGENTS.md
- CLAUDE.md
- README.md
- docs/ARCHITECTURE.md
- docs/CODING_STYLE.md
- docs/MODULE_RULES.md
- docs/DEPENDENCY_RULES.md
- CONTRIBUTING.md

If similar role documents exist with other names, discover them and include.
If not found, do not invent project rules.
If docs conflict with code, report as `HIGH` and continue with evidence.

## 6. Change Impact Analysis (mandatory)
For all planned or requested changes evaluate:
- changed modules/classes/interfaces/public contracts
- state ownership and lifecycle changes
- direct and transitive dependency changes
- persistence/network/API/UI impact
- existing consumer impact
- tests affected and needed
- backward compatibility
- migration needs
- regression surface
- dependency direction changes

Do not assume single-file impact.

## 7. Change Isolation Principle
Prefer extension over modification of stable regions.
Do not use this as an excuse to build endless adapter/helper layers.
If adaptation creates architectural mismatch, request explicit refactor path.

If direct change is needed, document:
- reason
- alternatives
- impact
- contract change
- regression risk
- required tests
- migration plan

## 8. Dependency Rules
- Do not directly depend on another feature's internal implementation.
- Depend on contracts/interfaces before implementations.
- Do not let infrastructure leak into domain/application logic.
- UI must not directly depend on persistence/network implementation details.
- Avoid global mutable state.
- Expose only necessary public API.
- No cycles.
- Before adding dependency, check if existing abstraction already covers it.

Project explicit architecture rules have priority unless they create severe risk:
- cycle
- security risk
- uncontrolled global state
- data corruption
- severe lifecycle issue
- concurrency hazard
- API compatibility break
- clear boundary collapse

In severe cases, report and propose safe alternative.

## 9. Feature Planning Flow (mandatory order)
Requirement -> Existing Architecture Discovery -> Relevant Code Discovery -> Impact Analysis -> Dependency Analysis -> Contract Design -> State Ownership -> Regression Analysis -> Test Strategy -> Implementation Plan

Include at least:
- intent
- current behavior vs target behavior
- affected components
- added components
- changed contracts
- dependency direction
- data flow and state ownership
- error boundaries
- regression protection and migration
- removable dead code

## 10. Implementation Review Checklist
### High severity checks
- Module boundary violations
- Layer violations
- Cross-feature implementation dependency
- Circular dependencies
- Leaked mutable state
- Improper public API exposure
- Dependency inversion violations
- Ownership ambiguity
- Unexpected contract change
- Concurrency safety issue
- Lifecycle ownership issue

### Medium severity checks
- excessive coupling
- low cohesion
- duplicated responsibility
- oversized objects
- hidden dependency
- overly broad interfaces
- unnecessary common abstractions
- duplicate cross-feature logic
- low testability
- unclear side effects

### Low severity checks
- naming
- minor consistency issues
- long functions
- avoidable visibility
- small duplication
- docs/lint polish

Low severity findings do not justify large refactors.

## 11. Regression Risk Analysis
Flag any change requiring explicit test evidence when it touches:
- existing behavior
- API signatures
- state transitions
- persistence format
- concurrency behavior
- lifecycle
- error handling
- shared-state introduction
- existing callers

Regression-risky changes cannot be marked complete without tests.

## 12. Abstraction Policy
Do not add abstraction only for visual cleanliness.
Add contract only when:
- change likelihood is real
- multiple implementations expected or test boundary requires
- clear responsibility separation exists

Prefer explicit YAGNI boundary.

## 13. Shared/Common Code Policy
Shared code must have strong shared ownership logic.
Validate:
- true shared responsibility
- independent change probability
- coupling increase risk

Prefer limited duplication over risky over-generalization.

## 14. Refactoring Policy
Prefer small, sequenced changes:
1) protect behavior tests
2) structural micro-step
3) test
4) next step
5) test
6) functional change
7) final regression validation

Avoid large rewrites by default.

## 15. Architecture Drift Detection
Detect new:
- reversed dependency directions
- new cross-feature dependencies
- public API growth
- shared/common bloat
- mixed domain/infrastructure responsibilities
- duplicated ownership
- dependency cycles
- convention drift

Treat small changes as future precedent.

## 16. Post-change Self Review
Ask explicitly:
- Did we increase coupling?
- Did we cross stable module boundary?
- Did we expose internal details?
- Did we expand unnecessary public API?
- Did we add global/shared mutable state?
- Did we overload any class responsibility?
- Did we hurt testability?
- Did we expand regression surface unnecessarily?
- Did new feature depend on internals?
- Did we use inheritance unnecessarily?
- Is each abstraction needed?
- Did we stay consistent with project architecture?

If answered negatively with evidence, proceed to report.

## 17. Reporting (required)
Every output must include Architecture Impact, Findings when present, Regression Risk, Tests Required, and final verdict. REVIEW, CHANGE-REVIEW, REFACTOR, and FULL-AUDIT outputs must also include Scorecard. Formal reports must follow the report template.

## 18. Scoring Policy

Review modes must include an evidence-based scorecard. Scores are not subjective ratings; they are deterministic judgments from observed evidence.

Allowed values:
- `5`: Verified pass. Evidence shows no violation and the relevant test, contract, or enforcement boundary is present where applicable.
- `4`: Pass. Evidence shows no violation, but enforcement or documentation is incomplete.
- `3`: Warning. Evidence shows a localized weakness, but no boundary, contract, lifecycle, state ownership, or regression breakage.
- `2`: Risk. Evidence shows material architecture risk or missing verification in a medium-risk affected area.
- `1`: Serious risk. Evidence shows a localized violation or partial verification of a high-risk affected area.
- `0`: Fail. Evidence shows a severe violation, or a high-risk affected area is unverified.
- `N-A`: Not scored. The criterion is outside the scope of the reviewed change.

Rules:
- Do not use decimal values, percentages, confidence scores, or subjective estimates.
- Every numeric score must cite concrete evidence.
- If evidence is insufficient for an affected high-risk area, score `0`.
- If an item is truly outside scope, score `N-A` and exclude it from totals.
- Do not average scores into a single architecture score unless the user explicitly asks.
- Show scorecards as `Criterion | Score | Status | Evidence | Action`.
- Include a score summary with counts for `5`, `4`, `3`, `2`, `1`, `0`, and `N-A`.
- Any `0` or `1` in a required architecture criterion prevents `PASS`.
- Any HIGH finding prevents `PASS`.

Risk tier definitions:
- High-risk affected area: area with a HIGH finding, regression risk HIGH, or change to public contract, state ownership, persistence format, concurrency behavior, lifecycle behavior, security boundary, or cross-feature dependency.
- Medium-risk affected area: area with a MEDIUM finding, dependency broadening, public API growth, shared/common code growth, reduced testability, or unclear side effects.
- Low-risk affected area: local implementation detail change with no boundary, contract, state, persistence, lifecycle, concurrency, or consumer impact.

Default scorecard criteria:
- Encapsulation
- Coupling
- Cohesion
- Explicit Dependencies
- Single Responsibility
- Dependency Inversion
- Testability
- Boundary Integrity
- Contract Compatibility
- State and Lifecycle Ownership
- Regression Safety
- Abstraction Fit

Score evidence matrix:
- Encapsulation: `5` requires no exposed internals or leaked mutable state plus verified ownership boundary; `4` requires no exposed internals but boundary is documented only implicitly; `3` means minor visibility or access concern without consumer impact; `2` means implementation detail exposure risk; `1` means localized encapsulation violation; `0` means leaked mutable state, public internal implementation dependency, or unverified high-risk ownership boundary.
- Coupling: `5` requires no new unnecessary dependency and dependency direction verified; `4` means no violation but enforcement is manual; `3` means localized dependency broadening; `2` means material coupling increase without boundary break; `1` means localized forbidden dependency; `0` means cross-feature implementation dependency or cycle.
- Cohesion: `5` requires each changed unit has one clear responsibility; `4` means responsibility is clear but not documented; `3` means minor mixed responsibility; `2` means material responsibility mixing; `1` means localized duplicated ownership; `0` means God Class or severe unrelated responsibility aggregation.
- Explicit Dependencies: `5` requires dependencies are constructor/config/import visible and contract-based where needed; `4` means visible dependencies but missing enforcement/documentation; `3` means minor implicit dependency; `2` means material hidden dependency risk; `1` means localized hidden dependency; `0` means service locator/global hidden dependency in affected path.
- Single Responsibility: `5` requires no added unrelated responsibility; `4` means responsibility fit is clear but not documented; `3` means minor responsibility growth; `2` means material responsibility growth; `1` means localized SRP violation; `0` means severe responsibility aggregation.
- Dependency Inversion: `5` requires high-level policy depends on contract, not implementation; `4` means correct direction but not enforced; `3` means minor adapter/contract ambiguity; `2` means material inversion risk; `1` means localized implementation dependency; `0` means high-level policy depends on infrastructure or feature implementation.
- Testability: `5` requires deterministic logic and replaceable side effects with relevant tests; `4` means test seam exists but tests/enforcement incomplete; `3` means minor test friction; `2` means material testability risk; `1` means localized hard-to-test dependency; `0` means high-risk behavior cannot be tested or verified.
- Boundary Integrity: `5` requires module/layer/feature boundaries remain intact and verified; `4` means intact but not automatically enforced; `3` means minor convention drift; `2` means material boundary pressure; `1` means localized boundary violation; `0` means module/layer violation, cycle, or cross-feature internal dependency.
- Contract Compatibility: `5` requires public contract unchanged or backward-compatible with tests; `4` means compatible but tests/docs incomplete; `3` means minor compatible expansion; `2` means material compatibility risk; `1` means localized consumer migration risk; `0` means breaking public contract without migration.
- State and Lifecycle Ownership: `5` requires clear owner and lifecycle with tests or enforcement where relevant; `4` means owner clear but not enforced/documented; `3` means minor ownership ambiguity; `2` means material ownership/lifecycle risk; `1` means localized duplicate ownership; `0` means leaked state, uncontrolled global mutable state, lifecycle hazard, or unverified high-risk state change.
- Regression Safety: `5` requires affected regression tests or equivalent verification; `4` means test plan exists but not automated; `3` means low-risk change with limited verification; `2` means medium-risk change missing direct regression test; `1` means high-risk change partially verified; `0` means high-risk change unverified.
- Abstraction Fit: `5` requires abstraction is necessary and bounded; `4` means abstraction fits but lacks documented rationale; `3` means minor abstraction uncertainty; `2` means speculative abstraction risk; `1` means localized unnecessary abstraction; `0` means abstraction hides boundary violation or creates broad coupling.

## 19. Mode requirements
- PLAN: pre-change planning with explicit architecture impact section.
- REVIEW: detect violations in current implementation against local architecture.
- CHANGE-REVIEW: analyze diff/commit/PR impact.
- REFACTOR: suggest safe phased refactoring candidates.
- FULL-AUDIT: repository-scale drift and boundary sweep.

The report verdict must be:
- PASS
- PASS WITH WARNINGS
- CHANGES REQUIRED

## 20. Output Discipline

모든 모드 출력은 판단에 필요한 정보만 포함한다. 목표는 축약 버전과 상세 버전을 나누는 것이 아니라, 처음부터 운영 가능한 기본 형식을 유지하는 것이다.

- 먼저 결론을 낸다: `Architecture Verdict`, 핵심 영향, blocking finding.
- 배경 설명은 판단에 필요한 경우에만 쓴다.
- HIGH finding은 모두 보고한다.
- MEDIUM finding은 아키텍처 결정이나 회귀 위험에 영향을 주는 항목을 우선 보고한다.
- LOW finding은 넓은 리팩터링의 근거로 사용하지 않는다.
- 동일한 규칙을 여러 섹션에서 반복하지 않는다.
- formal report가 필요한 경우에만 `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md` 전체 형식을 사용한다.
- Quality gates: any HIGH finding blocks PASS; any HIGH or MEDIUM finding requires a concise reason.
