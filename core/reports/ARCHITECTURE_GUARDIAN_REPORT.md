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
