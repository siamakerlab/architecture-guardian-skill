# REVIEW Mode Example

## Scope
- 대상: auth 모듈 서비스 계층

## Scorecard

Summary: `5:0 4:0 3:1 2:2 1:0 0:3 N-A:0`

| Criterion | Score | Status | Evidence | Action |
|---|---:|---|---|---|
| Encapsulation | 0 | Fail | `AuthOrchestrator` receives `UserRepositoryImpl` directly | Introduce feature contract |
| Coupling | 0 | Fail | auth feature depends on user feature implementation | Replace with port dependency |
| Cohesion | 3 | Warning | formatting and caching are mixed without confirmed boundary breakage | Split if change continues |
| Explicit Dependencies | 2 | Risk | dependency exists but contract boundary is not explicit | Define dependency contract |
| Dependency Inversion | 0 | Fail | implementation is injected instead of port/interface | Invert dependency |
| Regression Safety | 2 | Risk | adapter integration test is required before completion | Add integration test |

## Findings

- Severity: HIGH
- Location: `auth/service/AuthOrchestrator`
- Problem: 다른 feature(`user`)의 구현 클래스 `UserRepositoryImpl`을 직접 주입.
- Risk: feature 간 직접 구현 결합 및 테스트 대역 교체 어려움.
- Recommendation: `UserRepositoryPort` 인터페이스를 통해 의존성 반전.
- Regression Risk: MEDIUM
- Tests Required: 계약 기반 단위 테스트 + adapter 통합 테스트

- Severity: MEDIUM
- Location: `auth/service/AuthOrchestrator`
- Problem: 공용 유틸에서 사용자 메시지 포맷 변환과 로컬 캐싱을 함께 처리.
- Risk: 책임 혼재 및 변경 비용 증가.
- Recommendation: formatting, caching 분리.
- Regression Risk: LOW
- Tests Required: formatting 전환 테스트

## Architecture Verdict
CHANGES REQUIRED
