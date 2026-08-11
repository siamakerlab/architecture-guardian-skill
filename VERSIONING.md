# Versioning

This repository uses git tags as the release source of truth.

The skill runtime does not store a release version in `SKILL.md`. Codex skill frontmatter should stay limited to `name` and `description`.

## Version Sources

- Repository release version: git tag, formatted as `vMAJOR.MINOR.PATCH`
- Release notes: GitHub Releases and `CHANGELOG.md`
- Policy semantics version: `core/policy/ARCHITECTURE_GUARDIAN_RULESET.json` field `policy_version`
- Runtime entry point: `SKILL.md`, without a separate version field

The repository release version and `policy_version` do not have to change together.

## Current Version State

- Released tag: check with `git tag --list --sort=-version:refname | head -1`
- Current policy version: check `core/policy/ARCHITECTURE_GUARDIAN_RULESET.json` field `policy_version`

Create the first release tag when the skill is ready to be consumed as a stable external dependency.

Do not treat this document as the source of the current released version. Tags and the ruleset file are the source of truth.

## Versioning Rules

Use Semantic Versioning for repository tags.

### MAJOR

Bump `MAJOR` when a change can break existing users or automation.

Examples:

- Required report sections are removed or renamed.
- Mode names or required mode behavior become incompatible.
- Score meanings change in a non-compatible way.
- Install path, update behavior, or adapter contract changes in a way that requires user action.
- Public policy guarantees are weakened or redefined.

### MINOR

Bump `MINOR` when functionality is added without breaking existing users.

Examples:

- A new operating mode is added.
- A new scorecard criterion is added without changing existing score meanings.
- New templates, adapters, or examples are added.
- Existing policy guidance is expanded while preserving behavior.
- New validation or enforcement recommendations are added.

### PATCH

Bump `PATCH` for compatible corrections.

Examples:

- Documentation wording is clarified.
- Examples are corrected.
- Typos, broken links, or formatting issues are fixed.
- Validation compatibility is improved without changing policy behavior.

### Pre-release

Use pre-release tags only when a release should be tested before being considered stable.

Format:

```text
vMAJOR.MINOR.PATCH-rc.N
```

Example:

```text
v1.1.0-rc.1
```

## Policy Version Rules

Update `policy_version` only when the machine-readable policy semantics change.

Bump `policy_version` when:

- Score criteria change.
- Verdict rules change.
- Risk tier definitions change.
- Required report fields change.
- Rule identifiers or enforcement semantics change.

Do not bump `policy_version` for:

- README-only changes.
- License changes.
- Example-only changes.
- Typo fixes that do not alter policy meaning.
- Adapter wording that does not change runtime behavior.

## Release Checklist

Before creating a release tag:

1. Confirm `SKILL.md` frontmatter contains only `name` and `description`.
2. Confirm `README.md` documents the repository purpose, install path, update path, and usage.
3. Confirm `VERSIONING.md` reflects the intended release and policy version state.
4. If policy semantics changed, update `core/policy/ARCHITECTURE_GUARDIAN_RULESET.json` `policy_version`.
5. Validate the skill package:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

6. Validate the machine-readable rules:

```bash
python3 -m json.tool core/policy/ARCHITECTURE_GUARDIAN_RULESET.json >/dev/null
```

7. Check for obsolete mode names or banned wording:

```bash
rg -n 'CHANGE_REVIEW|FULL_AUDIT|compact|경량|concise mode' . -g '!/.git/**' -g '!.github/**' -g '!VERSIONING.md'
```

8. Commit the release changes.
9. Create an annotated tag:

```bash
git tag -a vMAJOR.MINOR.PATCH -m "vMAJOR.MINOR.PATCH"
```

10. Push the branch and tags to the canonical GitHub remote:

```bash
git push github main
git push github --tags
```

11. Confirm the local branch and canonical remote point to the same release commit:

```bash
git fetch github --prune
git rev-list --left-right --count main...github/main
```

The command should return `0 0`.

12. Publish GitHub Release notes using `CHANGELOG.md` as the source.

## Update Rules For Agents

When a user asks an agent to update this skill:

1. Use the canonical repository:

```text
git@github.com:siamakerlab/architecture-guardian-skill.git
```

2. Locate the installed skill directory.
3. If the installed skill is a git checkout, confirm its remote matches the canonical repository.
4. Run `git status --short`.
5. If local changes exist, report them and stop before updating unless the user explicitly approves overwrite or merge work.
6. If the checkout is clean, update with `git pull --ff-only`.
7. Validate the skill when a validator is available.
8. Report the resulting commit and latest tag if available.

Do not overwrite user-local modifications silently.

This repository uses GitHub as the single canonical remote. Do not introduce a mirror remote unless the user explicitly requests one.

## Recommended User Prompts

Install:

```text
Install Architecture Guardian Skill from git@github.com:siamakerlab/architecture-guardian-skill.git and validate it.
```

Update:

```text
Update Architecture Guardian Skill from git@github.com:siamakerlab/architecture-guardian-skill.git and validate it.
```

Install a specific version:

```text
Install Architecture Guardian Skill version v1.0.0 from git@github.com:siamakerlab/architecture-guardian-skill.git and validate it.
```

Update to a specific version:

```text
Update Architecture Guardian Skill to version v1.0.0 from git@github.com:siamakerlab/architecture-guardian-skill.git and validate it.
```
