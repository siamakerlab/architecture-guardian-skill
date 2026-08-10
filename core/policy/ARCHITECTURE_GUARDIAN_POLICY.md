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
Each mode must emit `Architecture Guardian Report` format.

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
Every output report must follow report template (Location, Problem, Risk, Recommendation, Regression Risk, Tests Required, Severity, and final verdict).

## 18. Mode requirements
- PLAN: pre-change planning with explicit architecture impact section.
- REVIEW: detect violations in current implementation against local architecture.
- CHANGE-REVIEW: analyze diff/commit/PR impact.
- REFACTOR: suggest safe phased refactoring candidates.
- FULL-AUDIT: repository-scale drift and boundary sweep.

The report verdict must be:
- PASS
- PASS WITH WARNINGS
- CHANGES REQUIRED

## 19. Output Discipline

모든 모드 출력은 판단에 필요한 정보만 포함한다. 목표는 축약 버전과 상세 버전을 나누는 것이 아니라, 처음부터 운영 가능한 기본 형식을 유지하는 것이다.

- 먼저 결론을 낸다: `Architecture Verdict`, 핵심 영향, blocking finding.
- 배경 설명은 판단에 필요한 경우에만 쓴다.
- HIGH finding은 모두 보고한다.
- MEDIUM finding은 아키텍처 결정이나 회귀 위험에 영향을 주는 항목을 우선 보고한다.
- LOW finding은 넓은 리팩터링의 근거로 사용하지 않는다.
- 동일한 규칙을 여러 섹션에서 반복하지 않는다.
- formal report가 필요한 경우에만 `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md` 전체 형식을 사용한다.

1. 필수 우선순위: `Architecture Impact` → `Findings` → `Tests Required` → `Verdict`
2. finding 정리
- HIGH: 모두 포함(필수)
- MEDIUM: 중요도 높은 순으로 최대 10개
- LOW: 기본 생략, `LOW findings omitted`로 요약 가능
3. 형식 제한
- Markdown table 또는 짧은 bullet 사용
- each finding: 1~2줄로 축약
4. 길이 제어
- 핵심 근거 없이는 배경설명·장식 문장 금지
- 동일 내용 반복 금지
5. 품질 게이트
- High가 하나라도 있으면 PASS 불가
- High/MEDIUM은 사유를 짧게라도 반드시 명시
