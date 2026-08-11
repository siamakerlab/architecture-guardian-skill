# FULL-AUDIT Mode Template

### 1) Repository Map
- module/package/feature/layer 핵심 지도
- public API, persistence, network 경계

### 2) Drift Sweep
- reversed dependency
- cross-feature coupling 증가
- public API/공통 코드 비대
- domain-infra 혼합
- cycle 존재

### 3) Rule Conformance
- `MODULE_RULES`/`DEPENDENCY_RULES` 반영 여부
- `AGENTS.md`/`CLAUDE.md` 일관성
- 템플릿 문서 최신성

### 4) Enforcement Suggestion
- 가능 시 CI 체크 1~3개만 제안
- architecture tests / dependency check / static rules

### 5) Findings
- High/Medium 우선 제시
- Low는 요약 생략 가능

### 6) Scorecard
- repository-level 기준별 `0~5`, 범위 밖 항목은 `N-A`
- 표는 `Criterion | Score | Status | Evidence | Action` 형식
- 표 위에 `5/4/3/2/1/0/N-A` count summary 표시
- 숫자 점수는 발견된 dependency, boundary, contract, state, test evidence와 연결
- 증거 없는 추정 점수 금지

### 7) Architecture Impact
- repository-wide 영향 요약

최종: `PASS` / `PASS WITH WARNINGS` / `CHANGES REQUIRED`
