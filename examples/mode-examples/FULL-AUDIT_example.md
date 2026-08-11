# FULL-AUDIT Mode Example

## Drift summary
- 발견된 신규 역방향 의존성: 없음
- cycle: 없음
- API sprawl: `admin` 모듈에서 공용 API 3개 증가
- shared/common bloat: `utils/formatting` 내 feature 의존 로직 혼재

## Scorecard

| Criterion | Score | Evidence |
|---|---:|---|
| Encapsulation | 5 | no cross-module state leak found |
| Coupling | 3 | shared formatting contains feature-specific logic |
| Cohesion | 3 | formatting responsibility is mixed across feature concerns |
| Boundary Integrity | 5 | no reversed dependency or cycle found |
| Contract Compatibility | 3 | admin public API increased by 3 entries |
| Regression Safety | 2 | smoke regression required for shared formatting split |

## Findings

- Severity: MEDIUM
- Location: `shared/formatting`
- Problem: feature A/B 간 유사하지만 다른 비즈니스 규칙이 공유 모듈에 섞임.
- Risk: 기능 간 coupling 증가
- Recommendation: feature-local 포맷터로 분리 후 공통 원시 포맷만 남김
- Regression Risk: LOW
- Tests Required: 회귀 스모크 + 모듈 단위 테스트

- Severity: LOW
- Location: `docs/STYLE.md` vs `docs/CODING_STYLE.md`
- Problem: 문서 규칙 중복 및 일치하지 않는 명명 규칙
- Risk: 운영자 해석 혼선
- Recommendation: 단일 템플릿으로 병합하고 references 정리
- Regression Risk: LOW
- Tests Required: 없음

## Architecture Verdict
PASS WITH WARNINGS
