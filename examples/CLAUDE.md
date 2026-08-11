# CLAUDE.md 연결 예시

```text
이 프로젝트는 Architecture Guardian Policy를 적용합니다.
핵심 정책은 `core/policy/ARCHITECTURE_GUARDIAN_POLICY.md`를 기준으로 하며,
작업 시 반드시 다음을 수행합니다.
- PLAN -> REVIEW -> CHANGE-REVIEW -> FINAL REPORT
- REVIEW/CHANGE-REVIEW/REFACTOR/FULL-AUDIT 결과는 0-5/N-A Scorecard 포함
- formal report는 `core/reports/ARCHITECTURE_GUARDIAN_REPORT.md` 형식으로 기록
- 회귀 위험이 있는 변경은 테스트 없이 완료하지 않음
```

참조:
- [adapters/claude/CLAUDE.md](adapters/claude/CLAUDE.md)
