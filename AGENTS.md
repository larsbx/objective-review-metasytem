<!--
Derived from templates/docs/AGENTS.md in larsbx/agent-icm @ sha256:e0ea75600e3d136a
Edit the canonical template or estate.toml, then re-render: make estate
Hand-edits here are drift and `make estate-check` fails on them.
-->

# Agent policy — objective-review-metasytem

The estate's review manifestos: ethics, security, accessibility, formal
verification, research hygiene and the rest, compiled into rulings.

**Language / toolchain:** Markdown, with Python tooling under scripts/
**CI:** GitHub Actions (`.github/workflows/docs-health.yml`): lychee link check,
  content freshness, markdownlint-cli2, typos

This file is for whoever is working here next, human or otherwise. It states
what is settled, so that it does not get re-litigated by someone reading only
the code.

## Read first

- `CONTRIBUTING.md`
- `STYLE_GUIDE.md`
- `5-RULINGS.md`
- `.agents/README.md`

## Gates

Before proposing a change as finished, run:

1. broken links —

   ```sh
   markdown-link-check **/*.md
   ```

2. markdown lint —

   ```sh
   markdownlint-cli2 "**/*.md"
   ```

3. spelling —

   ```sh
   typos
   ```

4. prose quality (optional) —

   ```sh
   vale **/*.md
   ```

Report honestly which ran. A partial environment that reports a skip is worth
more than one that passes vacuously.

## What this repository treats as evidence

- A new or changed principle shows the anti-pattern and the correct pattern,
  both.
- `5-RULINGS.md` compiles every manifesto's rulings into OBLIGATORY /
  ENCOURAGED / OPTIONAL / DISCOURAGED / PROHIBITED. A new ruling lands there
  too, or the compilation is already stale.
- A version bump updates the manifesto's `CHANGELOG.md` in Keep a Changelog
  form.
- Review is by code owner (`.github/CODEOWNERS`); one or more approvals are
  required.

## Standing prohibitions

- Never raise authority in translation. A translation preserves or lowers it.
- Never report a bounded failure as an absence, or let a refusal read as a
  clean answer.
- Never write an unqualified "verified".
- Never duplicate a status surface with nothing keeping the copies in step.
- Never ship a control that cannot fail.

## Scope discipline

- Make the change that was asked for. If the surrounding code is wrong in a way
  the task did not name, say so — do not widen the diff to fix it.
- If something is blocked, finish everything that is not, and say precisely what
  was left and why.
- Where a decision is already recorded, follow it or reopen it explicitly. Do
  not route around it in code.
