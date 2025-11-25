# Contributing to Objective Review Metasystem

Thank you for your interest in improving these manifestos! This document provides guidelines for contributing.

## Quick start

1. **Fork** this repository
2. **Create a feature branch**: `git checkout -b feature/improve-security-principle-3`
3. **Make your changes** following our [Style guide](./STYLE_GUIDE.md)
4. **Run quality checks** (see below)
5. **Submit a pull request** with a clear description

---

## Content standards

All contributions must follow the [Content & Communication Manifesto](./content_communication/CONTENT_COMMUNICATION_MANIFESTO.md) principles:

### Core requirements (must have)
- ✅ **Clarity**: Simple, direct language; active voice; concrete examples
- ✅ **Semantic Hierarchy**: Proper heading structure (H1 → H2 → H3, no skips)
- ✅ **Precision**: Consistent terminology; define jargon; use glossary terms
- ✅ **Accessibility**: WCAG 2.1 AA compliance; semantic markup; descriptive links
- ✅ **Empathy**: Inclusive language; blame-free; respectful tone

### Standard requirements (production quality)
- ✅ **Examples**: Show anti-pattern AND correct pattern for each principle
- ✅ **Actionability**: Provide concrete guidance, not abstract theory
- ✅ **Scannability**: Use headings, lists, tables, code blocks
- ✅ **Cross-references**: Link to related principles and manifestos
- ✅ **Version control**: Update CHANGELOG.md for significant changes

---

## Types of contributions

### 1. Typos and minor fixes
**No issue needed** — just submit a PR with clear description.

**Examples**:
- Fix spelling/grammar errors
- Correct broken links
- Update outdated tool versions
- Fix code example syntax errors

### 2. Clarifications and examples
**Create an issue first** to discuss approach.

**Examples**:
- Add missing code examples
- Expand unclear explanations
- Add "when to violate" guidance
- Provide additional context

### 3. New principles or manifestos
**Create an issue with detailed proposal** before implementation.

**Include in proposal**:
- Problem statement (what gap does this fill?)
- Target audience (who benefits?)
- Related manifestos (how does it complement existing ones?)
- Outline of principles (high-level structure)
- Differentiation (why not add to existing manifesto?)

---

## Quality checks

Before submitting your PR, run these checks:

### Automated checks (run locally)

```bash
# 1. Check for broken links
# Install: npm install -g markdown-link-check
markdown-link-check **/*.md

# 2. Lint markdown files
# Install: npm install -g markdownlint-cli2
markdownlint-cli2 "**/*.md"

# 3. Check spelling
# Install: cargo install typos-cli
typos

# Optional: Prose quality linting
# Install: brew install vale (macOS) or see https://vale.sh/docs/vale-cli/installation/
vale **/*.md
```

### Manual review checklist

Before submitting, verify:

- [ ] **Clarity**: Can a junior developer understand this?
- [ ] **Examples**: Do code examples compile/run?
- [ ] **Links**: Are all internal/external links functional?
- [ ] **Formatting**: Is semantic HTML/Markdown used correctly?
- [ ] **Consistency**: Does terminology match existing usage?
- [ ] **Changelog**: Is CHANGELOG.md updated (if version change)?
- [ ] **Cross-references**: Are related manifestos linked?
- [ ] **Accessibility**: Are images described with alt text?

---

## Review process

1. **Submit PR**: Include clear title and description
2. **Automated checks**: CI runs link checking, markdown linting, spell check
3. **Code owner review**: Manifesto owner(s) review (see [CODEOWNERS](./.github/CODEOWNERS))
4. **Address feedback**: Make requested changes
5. **Approval**: Requires 1+ approvals from code owners
6. **Merge**: Maintainer merges to main branch

**Response time**: Expect initial review within 5 business days.

---

## Versioning and changelogs

We follow [Semantic Versioning](https://semver.org/):

- **Major version** (X.0.0): Breaking changes, restructuring, principle additions/removals
- **Minor version** (1.X.0): New examples, significant clarifications, new sections
- **Patch version** (1.0.X): Typo fixes, link updates, minor clarifications

### Updating CHANGELOG.md

For changes requiring version bumps, update `CHANGELOG.md` in the manifesto directory:

```markdown
## [Unreleased]

### Added
- New example for Principle VIII demonstrating error handling patterns

### Changed
- Expanded "When to Violate" section for Principle III

### Fixed
- Corrected code example in Principle V (missing import statement)
```

**Format**: Follow [Keep a Changelog](https://keepachangelog.com/) conventions.

---

## Style guidelines

See [STYLE_GUIDE.md](./STYLE_GUIDE.md) for detailed guidance on:

- Voice & tone (professional, prescriptive, empathetic)
- Formatting standards (code blocks, emphasis, lists)
- Terminology (use controlled vocabulary)
- Examples (anti-pattern vs. pattern format)

### Quick style reference

**Voice**:
- ✅ Second person: "You should...", "Your code..."
- ✅ Imperative: "Use semantic HTML", "Avoid clever tricks"
- ✅ Active voice: "The system validates..." not "Validation is performed..."

**Tone**:
- ✅ Professional, helpful, patient
- ❌ Condescending, sarcastic, cute

**Formatting**:
- Code: \`inline code\` or \`\`\`language blocks
- UI elements: **Bold** ("Click **Save**")
- File paths: \`/path/to/file\`
- Emphasis: **strong** (important), *emphasis* (stress)

---

## Contribution recognition

Contributors are recognized in:
- PR description and commit messages
- GitHub contributor graph
- Manifesto CHANGELOG.md (for significant contributions)

We may add a CONTRIBUTORS.md file in the future to highlight major contributions.

---

## Code of conduct

### Expected behavior
- Be respectful and inclusive
- Provide constructive feedback
- Accept constructive criticism gracefully
- Focus on what is best for the community

### Unacceptable behavior
- Harassment, discrimination, or personal attacks
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information

**Enforcement**: Violations will result in warnings, temporary bans, or permanent bans at maintainer discretion.

**Contact**: Report issues to repository maintainers via GitHub issues (mark as private/security issue if needed).

---

## Questions?

- **General questions**: [Open a discussion](../../discussions)
- **Bug reports**: [Open an issue](../../issues) with "Bug:" prefix
- **Feature requests**: [Open an issue](../../issues) with "Feature:" prefix
- **Clarifications**: [Open an issue](../../issues) with "Question:" prefix

---

## License

By contributing, you agree that your contributions will be licensed under the same [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/) license that covers the project.

Your contributions become part of the public domain and can be freely used by anyone without restriction.

---

**Thank you for helping improve these manifestos!** 🙏

Your contributions help engineering teams worldwide build better, more maintainable, and more secure software.
