# Module Rules Template

## 1. Module responsibility
- 모듈별 목적 1줄 요약
- 금지된 책임

## 2. Allowed dependencies
- module A -> module B (allowed)
- 금지 dependency 목록

## 3. Imports/usage policy
- 상위/하위 의존성 규칙
- external package 정책

## 4. Cross-feature policy
- feature 간 접근 허용 기준
- implementation 직접 참조 금지 규칙

## 5. API boundary policy
- 공개 API 최소 범위
- 내부 구현 숨김 규칙

## 6. State ownership policy
- 전역 상태 불허 여부
- 소유자-소비자 책임

## 7. Change guardrails
- 변경 사전 승인 기준
- 위험도 임계치
