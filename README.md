# Architecture Guardian Skill

## 한 줄 정의
Architecture Guardian은 Claude Code와 Codex 모두에서 동작하는 아키텍처 거버넌스 Skill입니다.  
목표는 새로운 기능/리팩터링/수정/리뷰에서 변경 영향 분석, 의존성 방향, 회귀 위험을 기본 프로세스로 강제하는 것입니다.

## 핵심 구조
- [core/policy/ARCHITECTURE_GUARDIAN_POLICY.md](core/policy/ARCHITECTURE_GUARDIAN_POLICY.md): Single Source of Truth
- [core/policy/ARCHITECTURE_GUARDIAN_RULESET.json](core/policy/ARCHITECTURE_GUARDIAN_RULESET.json): 기계 판독용 규칙 스키마
- [core/reports/ARCHITECTURE_GUARDIAN_REPORT.md](core/reports/ARCHITECTURE_GUARDIAN_REPORT.md): 공통 보고서 템플릿
- [core/modes/PLAN.md](core/modes/PLAN.md): PLAN 모드 템플릿
- [core/modes/REVIEW.md](core/modes/REVIEW.md): REVIEW 모드 템플릿
- [core/modes/REFACTOR.md](core/modes/REFACTOR.md): REFACTOR 모드 템플릿
- [core/modes/CHANGE-REVIEW.md](core/modes/CHANGE-REVIEW.md): CHANGE-REVIEW 모드 템플릿
- [core/modes/FULL-AUDIT.md](core/modes/FULL-AUDIT.md): FULL-AUDIT 모드 템플릿

## 프로젝트 문서 템플릿
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/CODING_STYLE.md](docs/CODING_STYLE.md)
- [docs/MODULE_RULES.md](docs/MODULE_RULES.md)
- [docs/DEPENDENCY_RULES.md](docs/DEPENDENCY_RULES.md)

## 어댑터
- [adapters/claude/CLAUDE.md](adapters/claude/CLAUDE.md)
- [adapters/codex/AGENTS.md](adapters/codex/AGENTS.md)

## 실행 예시
- [examples/CLAUDE.md](examples/CLAUDE.md): Claude 연결 예시
- [examples/AGENTS.md](examples/AGENTS.md): Codex 연결 예시
- [examples/mode-examples/PLAN_example.md](examples/mode-examples/PLAN_example.md)
- [examples/mode-examples/REVIEW_example.md](examples/mode-examples/REVIEW_example.md)
- [examples/mode-examples/FULL-AUDIT_example.md](examples/mode-examples/FULL-AUDIT_example.md)

## Claude Code 적용
1. 프로젝트 루트 `CLAUDE.md`에 `adapters/claude/CLAUDE.md` 수준의 짧은 pointer만 둔다.
2. 프로젝트 코어 정책은 한 곳에서 관리: `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md`.
3. 작업 전 PLAN, 구현 중 REVIEW, 완료 전 CHANGE-REVIEW, 릴리스 경계에서 FULL-AUDIT를 실행.
4. 결과는 `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md` 형식으로 제출.

## Codex 적용
1. 프로젝트 루트 `AGENTS.md`에 `adapters/codex/AGENTS.md` 수준의 짧은 pointer만 둔다.
2. 동일 정책 파일(`core/policy/ARCHITECTURE_GUARDIAN_POLICY.md`)을 공통 참조.
3. PR/Diff 리뷰에서는 CHANGE-REVIEW 템플릿 적용 후 보고서를 생성.
4. 회귀 위험이 높은 변경은 테스트 계획이 확정될 때까지 완료로 간주하지 않음.

## MVP
- [MVP.md](MVP.md)

## 제약 준수 사유
- 도구별 규칙 과도 적용을 피하기 위해 아키텍처 정책은 공통(`core/policy`)에만 둠.
- 모든 모드에서 공통 보고서/검사 항목을 강제해 해석 차이를 축소.
- 기능 추가보다 경계 유지, 결합 저감, 회귀 억제를 우선.
