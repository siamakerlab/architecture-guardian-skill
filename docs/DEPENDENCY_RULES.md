# Dependency Rules Template

## 1. Dependency direction
- 정책: 상위 정책이 하위 구현에 의존하지 않음
- 허용 예외와 승인 기준

## 2. Direct implementation dependency 금지
- feature 내부 구현 객체 직접 참조 금지
- Repository 구현체 직접 사용 금지

## 3. Interface-first policy
- contract 우선 의존
- 구현체는 adapter 경계 내부에 둠

## 4. Infrastructure leakage
- infrastructure 객체가 domain 로직으로 침투 금지
- UI가 persistence/network 구현을 직접 참조 금지

## 5. Cycle prevention
- module 단위 cycle 점검 방법
- cycle 발견 시 조치안

## 6. Detection and enforcement
- 수동 점검 체크리스트
- CI 자동화 가능 체크 (dependency matrix, architecture tests)
