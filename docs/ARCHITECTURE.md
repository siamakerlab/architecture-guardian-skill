# Architecture Template

## 1. System overview
- Architecture style (ex: layer architecture / modular monolith / etc.)
- 핵심 아키텍처 원칙

## 2. Module map
- Module list
- 각 module의 책임
- 허용/금지 의존성

## 3. Layer boundaries
- Domain
- Application
- Interface
- Infrastructure

## 4. Dependency direction
- 상위 정책이 하위 상세에만 의존
- 역방향 의존이 있는지

## 5. State and ownership
- 상태 소유 모듈
- 공유 상태 예외 여부
- lifecycle 규칙

## 6. Persistence boundary
- DB/캐시/스토리지 접근 위치
- 트랜잭션 범위

## 7. Network / external API boundary
- API client 위치
- DTO/adapter 분리 규칙

## 8. Public API map
- 외부 노출 API 목록
- 버전 및 호환성 전략

## 9. Testing architecture
- 단위/통합/회귀 테스트 전략
- 의존성 주입/Mock 전략

## 10. Evolution notes
- known technical debt
- planned refactor boundary
