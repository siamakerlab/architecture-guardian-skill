# Architecture Guardian Report

## Scope
- 대상: `<module/feature/task>`
- 모드: `<PLAN | REVIEW | REFACTOR | CHANGE-REVIEW | FULL-AUDIT>`
- 생성일: `<YYYY-MM-DD>`

## Existing Architecture
- 요약 1~2줄

## Changes
- 변경 1~3줄

## Dependency Impact
- 추가/제거 dependency, 방향성, cycle

## Scorecard (review modes)

Required for REVIEW, CHANGE-REVIEW, REFACTOR, and FULL-AUDIT. For PLAN formal reports, omit this section unless the user explicitly asks for a planning scorecard.

Summary: `5:<n> 4:<n> 3:<n> 2:<n> 1:<n> 0:<n> N-A:<n>`

| Criterion | Score | Status | Evidence | Action |
|---|---:|---|---|---|
| Encapsulation | `<0-5/N-A>` | `<Verified/Pass/Warning/Risk/Serious/Fail/Not scored>` | `<file/module/contract/state evidence>` | `<none/fix/test/document>` |
| Coupling | `<0-5/N-A>` | `<status>` | `<dependency evidence>` | `<action>` |
| Cohesion | `<0-5/N-A>` | `<status>` | `<responsibility evidence>` | `<action>` |
| Explicit Dependencies | `<0-5/N-A>` | `<status>` | `<DI/import/contract evidence>` | `<action>` |
| Single Responsibility | `<0-5/N-A>` | `<status>` | `<responsibility evidence>` | `<action>` |
| Dependency Inversion | `<0-5/N-A>` | `<status>` | `<interface/implementation evidence>` | `<action>` |
| Testability | `<0-5/N-A>` | `<status>` | `<test seam/coverage evidence>` | `<action>` |
| Boundary Integrity | `<0-5/N-A>` | `<status>` | `<module/layer/feature evidence>` | `<action>` |
| Contract Compatibility | `<0-5/N-A>` | `<status>` | `<API/public contract evidence>` | `<action>` |
| State and Lifecycle Ownership | `<0-5/N-A>` | `<status>` | `<state/lifecycle evidence>` | `<action>` |
| Regression Safety | `<0-5/N-A>` | `<status>` | `<test/regression evidence>` | `<action>` |
| Abstraction Fit | `<0-5/N-A>` | `<status>` | `<abstraction/YAGNI evidence>` | `<action>` |

Scoring: `5` verified pass, `4` pass with incomplete enforcement/docs, `3` localized warning, `2` material risk, `1` serious risk, `0` fail, `N-A` outside scope and not scored. Do not use subjective, decimal, percentage, or confidence scores.

## Findings

| Severity | Location | Problem | Risk | Recommendation | Regression Risk | Tests Required |
|---|---|---|---|---|---|---|
| `<HIGH/MEDIUM/LOW>` | `<file|module|class>` | `<문제 요약>` | `<영향 요약>` | `<수정안>` | `<LOW/MEDIUM/HIGH>` | `<테스트 목록>` |

필수: High는 모두 기재, Medium은 상위 우선순위 10개, Low는 선택.

## Architecture Impact
- affected modules: `<modules>`
- affected contracts: `<contracts>`
- dependency direction: `<변경/불변>`
- state ownership: `<변경 유무>`
- regression surface: `<low|medium|high>`
- compatibility: `<유지|변경>`
- testing requirements: `<간략>`

## Architecture Verdict
- PASS / PASS WITH WARNINGS / CHANGES REQUIRED

## Open Questions
- `<판단 필요 항목>`
