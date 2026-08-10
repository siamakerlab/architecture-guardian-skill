# Architecture Guardian MVP

## 1) 목표
- AI 작업(Claude Code / Codex 공통)에서 
  - 변경 전 설계 영향 분석이 누락되지 않도록 하는 최소 운영 프레임을 제공한다.
  - 회귀 위험이 높은 변경을 감지해 리뷰 단계에서 차단한다.
  - 단일한 Architecture Policy를 통해 도구 간 해석 차이를 줄인다.

## 2) MVP 범위 (In-Scope)
- 공통 정책(Single Source) 사용: `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md`
- 모드 템플릿 운영:
  - PLAN
  - REVIEW
  - CHANGE-REVIEW
  - FULL-AUDIT
- 공통 보고서 형식 고정: `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md`
- Claude/Codex 어댑터 최소 동기화:
  - CLAUDE: `adapters/claude/CLAUDE.md`
  - Codex: `adapters/codex/AGENTS.md`
- 프로젝트 규칙 문서 탐색 체크리스트 (기존 문서 존재 여부 + 충돌 탐지)
- 회귀 위험이 높은 변경에 대한 최소 테스트 요구사항 강제 규칙

## 3) MVP 제외(Out of Scope)
- CI/CD 자동 게이트 완전 연동(후속 버전에서 확대)
- 언어/프레임워크별 정교한 규칙 자동 파서(Gradle, tsconfig graph, kotlin detekt 등)
- PR 봇/자동 코멘트봇(현재는 수동 워크플로우 우선)

## 4) 성공 기준 (Acceptance Criteria)
- 새 작업 시작 시 PLAN 문서에서 다음이 항상 생성됨
  - 변경 대상 모듈/계약/의존성 변화
  - 상태 소유권/사이클 리스크
  - 회귀 분석 + 테스트 요구사항
- REVIEW/CHANGE-REVIEW 보고서가 정책 형식으로 작성됨
- 최소 아래 항목 중 하나라도 발견 시 `CHANGES REQUIRED`로 판단
  - Feature간 구현체 직접 의존
  - 순환 의존
  - global mutable state 도입
  - public contract 의미 변경
- `Architecture Impact` 섹션이 누락되지 않음

## 5) 핵심 원칙(강제)
우선순위 고정:
1. Encapsulation
2. Low Coupling
3. High Cohesion
4. Explicit Dependencies
5. Single Responsibility
6. Dependency Inversion
7. Testability

- 구현 편의성은 7순위 이슈 이전에 우선순위를 바꾸지 못한다.

## 6) 사용자 플로우 (MVP)
1. 작업 제안 수신
2. PLAN 실행
3. 코드 탐색 후 영향도 분석
4. 구현(가능하면 최소 변경)
5. REVIEW 실행
6. 변경 요약 + 아키텍처 리스크/테스트 요구 정리
7. 완료 시 CHANGE-REVIEW로 최종 검증

## 7) MVP 산출물
- `MVP.md` (현재 문서)
- 모드 템플릿 4종
- 공통 보고서 템플릿 1종
- Claude/Codex 어댑터 2종
- 프로젝트 문서 템플릿 4종

## 8) 단계별 구현 로드맵
### Phase 1 (현재)
- 템플릿 적용 및 문서 기반 운영 시작
- 팀/AI 작업에서 PLAN-REVIEW-CHANGE-REVIEW 의무화

### Phase 2
- 프로젝트별 ARCHITECTURE / MODULE / DEPENDENCY 문서를 실제 프로젝트 규칙으로 채움
- drift 점검 체크리스트 정기화

### Phase 3
- CI 연동 규칙 초안(커스텀 체크/아키텍처 테스트) 추가
- 규칙 자동화 PoC

## 9) 실패 모드(Failure Modes)
- PLAN을 생략한 구현 착수
- 모드별 `Architecture Impact` 미작성
- 영향 분석 없이 구현된 직접 의존 추가
- 문서와 코드 충돌 미보고

이 경우 처리: 즉시 작업 중단 + 해당 Finding 제출 + 수정 계획 수립 후 재개.

## 10) 운영 규칙(한 줄)
- 작은 변경 하나도 향후 아키텍처 선례가 될 수 있으므로, 모든 변경은 `영향-검토-검증` 순서로 처리한다.
- 스타일 정리보다 회귀 안전성과 경계 안정성을 우선한다.
