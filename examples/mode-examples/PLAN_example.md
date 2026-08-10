# PLAN Mode Example

## Requirement
- 사용자 권한 정책 변경으로 감사 로그 저장 이벤트를 확장.

## Existing Architecture Discovery
- Feature: auth, audit
- Audit 저장은 `audit` module의 repository boundary에서 관리
- DI graph는 feature-level container에서 구성

## Relevant Code Discovery
- 후보: `auth/usecase/`, `audit/service/`
- 간접 영향: `notification` 모듈

## Change Impact Analysis
- 변경 모듈: auth, audit
- 계약 변경: AuditEvent schema v2 확장
- 추가 dependency: 없음
- 삭제 dependency: 없음

## Dependency Analysis
- 기존 abstraction으로 변경 가능: Contract 중심 유지
- 새 abstraction 불필요

## Contract Design
- 기존 contract backward compatible 필드 추가
- optional field로 migration 안전성 확보

## State Ownership
- 이벤트 저장 소유권은 audit 도메인 유지
- auth는 입력만 전달

## Regression Analysis
- 기존 로그 조회 동작 영향 없음
- API 버전 하위 호환 유지

## Test Strategy
- 단위 테스트: AuditEventSerializer
- 통합 테스트: auth -> audit pipeline
- 회귀 테스트: 기존 감사 조회 케이스

## Implementation Plan
1) schema 확장
2) contract 버전화
3) adapter 전파
4) 테스트 추가

## Architecture Impact
- affected modules: auth, audit
- affected contracts: `AuditEvent` public DTO
- changed dependencies: 없음
- dependency direction: 유지
- state ownership: unchanged
- regression surface: low
- compatibility: high
- testing requirements: 추가 회귀 테스트 3건
