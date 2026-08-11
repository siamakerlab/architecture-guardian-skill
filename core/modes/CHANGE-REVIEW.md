# CHANGE-REVIEW Mode Template

### 1) Baseline
- baseline architecture 1~2줄 요약
- 주요 계약/의존성 상태

### 2) Diff Impact Map
- 변경 파일 → 영향 모듈
- 직접/간접 dependency 변경
- 상태 소유권/퍼시스턴스/네트워크/UI 영향

### 3) Contract Risk
- signature/호출자 영향
- 호환성 판단

### 4) Regression Risk
- 기존 동작 훼손 포인트
- 사이드 이펙트 범위
- migration 필요 여부

### 5) Required Tests
- 최소 필수 테스트 1순위부터 작성

### 6) Findings
- Severity/Location/Problem/Risk/Recommendation/Regression Risk/Tests Required
- High/Medium 우선 상위 정리

### 7) Scorecard
- 각 기준은 `0~5`만 사용하고, 범위 밖 항목은 `N-A`
- 표는 `Criterion | Score | Status | Evidence | Action` 형식
- 표 위에 `5/4/3/2/1/0/N-A` count summary 표시
- 숫자 점수는 diff/commit/PR 증거와 연결
- 고위험 영향 영역의 검증 근거가 없으면 `0`
- 기준: Encapsulation, Coupling, Cohesion, Explicit Dependencies, Single Responsibility, Dependency Inversion, Testability, Boundary Integrity, Contract Compatibility, State and Lifecycle Ownership, Regression Safety, Abstraction Fit

### 8) Architecture Impact
- 아키텍처 영향 섹션이 비어있으면 실격

최종: `PASS` / `PASS WITH WARNINGS` / `CHANGES REQUIRED`
