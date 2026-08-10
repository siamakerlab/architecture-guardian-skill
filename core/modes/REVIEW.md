# REVIEW Mode Template

### 1) Scope
- 대상: `<module/feature/file>`
- 현재 문서 준수 상태 확인

### 2) Boundary / Dependency
- module & layer boundary
- feature 간 직접 구현 의존 여부
- circular dependency
- public API 노출 범위
- mutable state / lifecycle 위반

### 3) Contract & Cohesion
- interface 폭
- 책임 분리 실패
- 공통 코드 남용
- testability 영향

### 4) Regression
- API/상태/동시성/에러 처리 영향 가능성

### 5) Findings
- 각 finding: Severity/Location/Problem/Risk/Recommendation/Regression Risk/Tests Required
- High, Medium는 우선 출력(낮은 등급은 생략 가능)

### 6) Self-review 체크
- coupling 증가? boundary 침범? 내부 구현 종속? API 확장 과다?

최종: `PASS` / `PASS WITH WARNINGS` / `CHANGES REQUIRED`
