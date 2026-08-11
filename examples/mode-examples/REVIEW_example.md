# REVIEW Mode Example

## Scope
- 대상: auth 모듈 서비스 계층

## Scorecard

| Criterion | Score | Evidence |
|---|---:|---|
| Encapsulation | 0 | `AuthOrchestrator` receives `UserRepositoryImpl` directly |
| Coupling | 0 | auth feature depends on user feature implementation |
| Cohesion | 3 | formatting and caching responsibility are mixed in shared utility without confirmed boundary breakage |
| Explicit Dependencies | 2 | dependency exists but contract boundary is not explicit |
| Dependency Inversion | 0 | implementation is injected instead of port/interface |
| Regression Safety | 2 | adapter integration test is required before completion |

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
