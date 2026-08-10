# PLAN Mode Template

### 1) Requirement
- 변경 목적: `<summary>`
- 현재 동작: `<baseline>`
- 목표 동작: `<target>`
- 제약/성공/실패 조건

### 2) Existing Architecture Discovery
- module/package/layer/feature: 핵심 1줄
- interface/implementation, DI, state ownership
- boundary 문서 존재: `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/ARCHITECTURE.md`, `docs/CODING_STYLE.md`, `docs/MODULE_RULES.md`, `docs/DEPENDENCY_RULES.md`, `CONTRIBUTING.md`
- 코드-문서 불일치 존재 시 명시

### 3) Relevant Code Discovery
- 직접 변경 후보
- 간접 영향 후보
- public API 영향 후보

### 4) Change Impact Analysis
- affected modules/class/interface
- contract/dependency/state 영향
- persistence/network/UI/API 영향
- regression surface

### 5) Dependency Analysis
- 기존 abstraction 대체 가능성
- cycle/역방향 의존 위험

### 6) Contract & State
- public contract 변경 여부
- 하위 호환성/마이그레이션 방안
- 소유권 변경 여부

### 7) Regression & Test Strategy
- 기존 동작 훼손 포인트
- 회귀 테스트 우선순위

### 8) Implementation Plan
- 단계(소규모) 3개 이내
- Adapter/Wrapper 과잉 금지 계획
- 최소 변경안 선택 근거

### 9) Architecture Impact (필수)
- affected modules
- affected contracts
- new/changed dependencies
- dependency direction
- state ownership
- compatibility
- regression surface
- testing requirements
- 해당없음: `No meaningful architecture impact`

출력은 요약 중심으로 제출하고, High/Medium 우선순위 근거를 함께 제시한다.
