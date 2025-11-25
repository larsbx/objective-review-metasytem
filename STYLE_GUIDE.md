# Style Guide for Objective Review Metasystem

This guide documents voice, tone, formatting, and terminology standards for all manifestos in this repository.

**Purpose**: Ensure consistency, clarity, and professionalism across all content.

**Applies to**: All manifestos, README, CONTRIBUTING, and supporting documentation.

---

## Table of Contents

- [Voice & Tone](#voice--tone)
- [Formatting Standards](#formatting-standards)
- [Terminology & Glossary](#terminology--glossary)
- [Code Examples](#code-examples)
- [Accessibility Requirements](#accessibility-requirements)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## Voice & Tone

### Voice (Constant Across All Content)

**Personality**: Professional, prescriptive, empathetic

**Characteristics**:
- **Authoritative**: Principles are stated as requirements, not suggestions
- **Educational**: Explains the "why", not just the "what"
- **Empathetic**: Acknowledges difficulty, provides support
- **Pragmatic**: Includes "when to violate" guidance

**Person**:
- ✅ **Second person** for implementation guidance: "You should...", "Your code..."
- ✅ **First person plural** for shared context: "We recommend...", "Our approach..."
- ❌ **Third person** for users: "The developer..." → "You..."

**Tense**:
- ✅ **Present** for current state: "Code is read 10× more than written"
- ✅ **Imperative** for instructions: "Use semantic HTML", "Avoid clever tricks"
- ❌ **Future** for instructions: "You will click..." → "Click..."

**Mood**:
- ✅ **Imperative** for requirements: "Code shall read as prose"
- ✅ **Indicative** for explanations: "Semantic HTML improves accessibility"

### Tone (Adjusts by Context)

| Context | Tone | Example |
|---------|------|---------|
| **Principle statements** | Prescriptive, authoritative | "Code shall read as prose; visual structure mirrors logical structure" |
| **Security manifesto** | Urgent, serious | "System failure shall not compromise security posture" |
| **Accessibility manifesto** | Inclusive, legally-aware | "Universal access is a legal requirement and moral imperative" |
| **Error guidance** | Helpful, solution-focused | "If you encounter this error, try..." |
| **Examples** | Neutral, demonstrative | "Anti-pattern: verbose, passive" / "✓ Clear, concise" |
| **"When to violate"** | Pragmatic, understanding | "Violate this principle when performance profiling justifies..." |

---

## Formatting Standards

### Headings

**H1 (Page Title)**: Used once per document
```markdown
# Manifesto Name: N Foundational Principles
```

**H2 (Major Sections)**: Tier groupings, major concepts
```markdown
## Core Tier: Foundation
## Implementation Guide
```

**H3 (Principles)**: Individual principles
```markdown
### I. Principle Name
### II. Another Principle
```

**H4 (Subsections)**: Implementation details, examples
```markdown
#### Guidelines
#### Example (Anti-pattern)
```

**Rules**:
- ✅ Sequential heading levels (H1 → H2 → H3, no skips)
- ✅ Sentence case for headings: "User experience principles"
- ❌ Title Case For Headings: "User Experience Principles"
- ✅ Use colons for H1/H2 labels: "Core Tier: Foundation"
- ❌ Use colons in H3/H4: "Example: Anti-pattern" → "Example (Anti-pattern)"

### Emphasis

**Bold (`**text**`)**: Key terms, UI elements, warnings
- ✅ First use of principle names: "**Clarity as Prime Directive**"
- ✅ UI elements in instructions: "Click **Save**"
- ✅ Warnings/emphasis: "**Critical**: Never fail open"
- ❌ Entire sentences: "**This is very important.**" → Use sparingly

**Italic (`*text*`)**: Stress, quotes, metaprinciples
- ✅ Metaprinciples: "*Code optimizes for human cognition*"
- ✅ Gentle stress: "Remember to *test* your changes"
- ❌ Emphasis overuse: "This is *really* *very* important"

**Code (`\`text\``)**: Inline code, commands, file paths, technical terms
- ✅ Inline code: "Use `const` instead of `let`"
- ✅ Commands: "Run `npm install`"
- ✅ File paths: ` /etc/config.yml`
- ✅ Technical terms first use: "WCAG 2.1 AA (`WCAG` = Web Content Accessibility Guidelines)"

### Lists

**Unordered Lists**: Use `-` (dash), not `*` or `+`
```markdown
- First item
- Second item
  - Nested item (2-space indent)
```

**Ordered Lists**: Use `1.` for all items (auto-numbering)
```markdown
1. First step
1. Second step
1. Third step
```

**Checklist**: Use `- [ ]` and `- [x]`
```markdown
- [ ] Incomplete task
- [x] Completed task
```

**Parallel structure**: List items should have consistent grammatical structure
- ✅ All verbs: "Add tests", "Run build", "Fix errors"
- ✅ All nouns: "Test coverage", "Build status", "Error count"
- ❌ Mixed: "Add tests", "Build", "Fixing errors"

### Code Blocks

**Fenced code blocks**: Always specify language
````markdown
```python
def example():
    return True
```

```bash
npm install
```

```markdown
# Example markdown
```
````

**Language identifiers**:
- Use specific: `python`, `javascript`, `typescript`, `rust`, `yaml`, `json`, `bash`
- ❌ Generic: `code`, `text` (unless truly language-agnostic)

**Comments**: Explain **why**, not **what**
```python
# ❌ Increment counter by 1
counter += 1

# ✅ Track retry attempts for exponential backoff
counter += 1
```

### Tables

**Markdown tables**: Align headers for readability in source
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value    | Value    | Value    |
```

**Headers**: Always include header row
**Alignment**: Use `:` for alignment (`:---` left, `:---:` center, `---:` right)

### Links

**Descriptive link text**: Describe destination, not "click here"
- ✅ `[Accessibility Manifesto](./accessibility/)`
- ✅ `See [Principle III](./vibe_coding/#iii-precision) for details`
- ❌ `[Click here](./accessibility/) for accessibility`
- ❌ `More info [here](./link)`

**Relative links**: Use relative paths for internal links
- ✅ `./vibe_coding/VIBE_CODING_MANIFESTO.md`
- ❌ `https://github.com/user/repo/blob/main/vibe_coding/...`

**Anchor links**: Use lowercase with hyphens
- ✅ `#core-tier-foundation`
- ❌ `#Core_Tier_Foundation`

### Visual Markers

**Emoji**: Use for visual anchoring in README, sparingly elsewhere
- Manifestos: 🔬 🔒 📊 ✨ 🎨 ♿ 📝
- Status: ✅ ⚠️ ❌
- Other: 🔴 🟡 🟢 🔵

**Symbols in examples**:
- Anti-pattern: `# Anti-pattern:` or `❌`
- Correct pattern: `# ✓` or `✅`
- Warning: `⚠️` or `**Warning**:`

---

## Terminology & Glossary

### Controlled Vocabulary

Use these terms consistently. Do not use synonyms.

| **Use This** | **Not This** | **Context** |
|--------------|--------------|-------------|
| Manifesto | Guide, Document, Specification | Referring to principle collections |
| Principle | Rule, Guideline, Practice | Individual foundational rules |
| Tier | Level, Phase, Stage | Principle groupings (Core/Standard/Excellence) |
| Implementation Guide | How-to, Instructions, Steps | Actionable implementation section |
| Anti-pattern | Bad practice, Wrong way | Incorrect example |
| Pattern | Good practice, Right way, Best practice | Correct example |
| Code example | Code snippet, Sample code | Executable code demonstration |
| Changelog | Change log, Version history | Document tracking changes |

### Tier Naming (Standardized)

All manifestos use this three-tier structure:

1. **Core** (Non-negotiable, universal, start here)
2. **Standard** (Production-required, professional quality)
3. **Excellence** (Differentiation, advanced practices)

❌ Do not use: Basic, Intermediate, Advanced (except in context-specific progressions like "Basic types → Intermediate types → Advanced types")

### Technical Terms

**First use**: Define or link to definition
```markdown
We follow WCAG 2.1 AA (Web Content Accessibility Guidelines, Level AA conformance).
```

**Abbreviations**: Spell out first use, abbreviation in parentheses
```markdown
Use a Content Delivery Network (CDN) to improve performance. The CDN caches...
```

**Jargon**: Justify or avoid
- ✅ "Use semantic HTML (HTML elements that describe their meaning)"
- ❌ "Leverage synergistic paradigms" (meaningless jargon)

---

## Code Examples

### Structure

Every code example should follow this pattern:

````markdown
```language
# Anti-pattern: [concise description]
[incorrect code]

# ✓ [Correct approach]
[correct code]
```
````

### Requirements

- ✅ **Complete**: Include necessary imports, context
- ✅ **Executable**: Code should compile/run
- ✅ **Idiomatic**: Follow language conventions
- ✅ **Comments**: Explain *why*, not *what*
- ✅ **Syntax highlighting**: Specify language
- ✅ **Progressive complexity**: Simple → Intermediate → Advanced

### Example Format

````markdown
```python
# Anti-pattern: Vague naming, no error handling
def process(data):
    return data * 2

# ✓ Clear naming, explicit error handling
def calculate_double_price(price: Decimal) -> Decimal:
    if price < 0:
        raise ValueError(f"Price cannot be negative: {price}")
    return price * Decimal('2.0')
```
````

---

## Accessibility Requirements

### Semantic HTML/Markdown

- ✅ Use proper heading hierarchy (H1 → H2 → H3)
- ✅ Use semantic list markup (`-`, `1.`)
- ✅ Use tables for tabular data
- ❌ Use `<div>` styling to fake headings

### Alt Text

**Images**: Describe content and function
```markdown
![Architecture diagram showing client, API gateway, and database with request flow](./diagram.png)
```

Not:
```markdown
![diagram](./diagram.png)
```

### Link Text

**Descriptive**, not generic
- ✅ `[Accessibility testing guide](./testing.md)`
- ❌ `[Click here](./testing.md) for testing`

### Color

**Never use color alone** to convey meaning
- ✅ ❌ Red X + "Anti-pattern" text
- ❌ Red text alone (invisible to colorblind users)

---

## Anti-Patterns to Avoid

### Writing Anti-Patterns

| Anti-Pattern | Why Bad | Fix |
|--------------|---------|-----|
| **"Obviously..."** | Condescending, assumes knowledge | State directly without judgment |
| **"Simply..."** | Dismisses difficulty | Acknowledge complexity, provide support |
| **"Just..."** | Minimizes legitimate challenges | "To solve this, first..." |
| **Passive voice overuse** | Vague, weak | "The system validates" not "Validation is performed" |
| **Walls of text** | Hard to scan | Use headings, lists, whitespace |
| **Clever wordplay** | Obscures meaning | Prioritize clarity over cleverness |
| **Feature vomit** | Lists capabilities without use cases | Show how to *use* features |
| **Jargon without definition** | Excludes readers | Define or link to glossary |

### Formatting Anti-Patterns

| Anti-Pattern | Why Bad | Fix |
|--------------|---------|-----|
| **Heading level skips** | Breaks semantic structure | H1 → H2 → H3 (no H1 → H3) |
| **Non-descriptive links** | "Click here", "this page" | Describe destination |
| **Missing alt text** | Inaccessible to screen readers | Describe image content |
| **Code without language** | No syntax highlighting | Specify language in fence |
| **Inconsistent terminology** | Confuses readers | Use controlled vocabulary |

---

## Version History

**Version**: 1.0
**Last Updated**: 2025-11-20
**Status**: Current

---

## Questions?

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines.

For style questions not covered here, refer to:
- [Content & Communication Manifesto](./content_communication/CONTENT_COMMUNICATION_MANIFESTO.md)
- [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [Google Developer Documentation Style Guide](https://developers.google.com/style)
