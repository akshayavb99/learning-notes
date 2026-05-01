---
title: Conventional Commits Quick Reference
tags:
  - git
  - github
  - version-control
  - best-practices
---

# Conventional Commits Quick Reference

## Changelog

| Date        | Change Description                                                  |
| ----------- | ------------------------------------------------------------------- |
| May 1, 2026 | Added the notes about conventional commits rules and best practices |

## Commit Structure

| Part        | Required | Description                  | Example            |
| ----------- | -------- | ---------------------------- | ------------------ |
| Type        | Yes      | Nature of change             | `feat`, `fix`      |
| Scope       | No       | Area/module affected         | `(auth)`, `(ui)`   |
| Description | Yes      | Short summary (imperative)   | `add login flow`   |
| Body        | No       | Why + context                | Explains reasoning |
| Footer      | Yes      | Metadata / breaking / issues | `Closes #12`       |

**Commit Message Template**

```
<type>[scope]: <description>

[body]

[footer]
```

---

## Commit Types

| Type       | Use Case         | Example                         |
| ---------- | ---------------- | ------------------------------- |
| `feat`     | New feature      | `feat: add search bar`          |
| `fix`      | Bug fix          | `fix: handle null response`     |
| `docs`     | Docs only        | `docs: update README`           |
| `style`    | Formatting       | `style: fix indentation`        |
| `refactor` | Code restructure | `refactor: simplify auth logic` |
| `perf`     | Performance      | `perf: optimize query`          |
| `test`     | Tests            | `test: add login tests`         |
| `build`    | Build/deps       | `build: upgrade webpack`        |
| `ci`       | CI/CD            | `ci: add GitHub Actions`        |
| `chore`    | Maintenance      | `chore: clean temp files`       |

---

## Scope Examples

| Scope  | Meaning               | Example                   |
| ------ | --------------------- | ------------------------- |
| `auth` | Authentication module | `feat(auth): add OAuth`   |
| `ui`   | Frontend UI           | `fix(ui): align button`   |
| `api`  | Backend/API           | `feat(api): add endpoint` |

---

## Description Rules

| Rule              | Example to Follow   | Example to Avoid      |
| ----------------- | ------------------- | --------------------- |
| Imperative mood   | `add login feature` | `added login feature` |
| Short (~50 chars) | `fix crash on load` | Too long              |
| No period         | `update config`     | `update config.`      |
| Lowercase         | `fix typo`          | `Fix Typo`            |

---

## Body Guidelines

Use the body to explain **why**, not just what. For example:

```
fix: prevent crash on empty input

Check for null values before parsing to avoid runtime errors.
```

---

## Breaking Changes

Two ways to indicate breaking changes:

**1. `!` after type/scope**

`feat!: drop v1 API`

**2. Footer**

```
feat(api): change response format

BREAKING CHANGE: response is now an object instead of array
```

---

## 🔗 Footer Examples

| Purpose     | Example                |
| ----------- | ---------------------- |
| Close issue | `Closes #123`          |
| Reference   | `Refs #456`            |
| Breaking    | `BREAKING CHANGE: ...` |

---

## 🧠 Best Practices

- One logical change per commit
- Use consistent types
- Use scopes when helpful
- Avoid vague messages like `update stuff`
- Write messages that make sense in changelogs

## References

1. https://www.conventionalcommits.org/en/v1.0.0/
