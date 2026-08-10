# REFACTOR Mode Template

1) Trigger
- 구조적 악화가 실제로 증명되는지
- 단기/장기 성격 정의

2) Safe decomposition
- 동작 보존 기준 정의
- 단계별 의존성 위험 분리

3) Plan (최소 단계)
- 테스트 기반 1차 보존
- 소규모 구조 개선
- 검증/재평가 반복

4) Dependency simplification
- 과도한 결합/중복 축소
- 필요 시 contract 정제

5) Rollback criteria
- 실패 조건과 되돌리기 기준

6) Finalization
- coupling 감소 여부
- boundary 안정화
- 테스트 비용 대비 효과

원칙: adapter/wrapper 과잉 추가 금지
