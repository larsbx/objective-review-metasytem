---
id: "content-communication"
title: "Content & Communication Manifesto"
version: "2.1"
status: "current"
focus: "Clear, maintainable, accessible content"
primary_users: ["technical-writers", "developers", "designers", "devrel", "content-strategists", "product-managers"]
learning_curve: "low-medium"
roi_timeline: "immediate"
adoption_scope: "universal"
principles_count: 5 # Was 18, revised to 5 core principles
tier_structure:
  core: 5
  standard: 0
  excellence: 0
applicability:
  project_types: ["all-with-user-facing-content"]
  content_types: ["technical-docs", "ui-microcopy", "error-messages", "marketing", "support", "api-docs"]
  contexts: ["documentation", "user-interfaces", "knowledge-bases", "developer-portals"]
related_manifestos:
  complements: ["accessibility", "user-experience", "vibe-coding"]
  prerequisites: []
  enables: ["user-comprehension", "support-deflection", "developer-experience"]
tools:
  categories: ["linters", "docs-frameworks", "diagram-tools", "analytics", "i18n"]
  count: 50+
measurement:
  readability:
    flesch_kincaid_grade:
      target: "≤10 for general audience"
      acceptable: "≤12"
      measurement: "vale-hemingway-app"
    avg_sentence_length:
      target: "15-20 words"
      acceptable: "≤25 words"
      measurement: "vale-textstat"
    passive_voice_percentage:
      target: "≤10%"
      acceptable: "≤15%"
      measurement: "vale-grammarly"
  structural:
    broken_links:
      target: "0"
      acceptable: "≤1%"
      measurement: "markdown-link-check-linkchecker"
    heading_hierarchy_violations:
      target: "0"
      measurement: "markdownlint"
  user_impact:
    search_success_rate:
      target: "≥90%"
      acceptable: "≥80%"
      measurement: "search-analytics"
    was_this_helpful:
      target: "≥80% yes"
      acceptable: "≥70%"
      measurement: "feedback-widgets"
---
# The Content & Communication Manifesto

**Version**: 2.1
**Last Updated**: 2025-11-23

> Content is not a layer on top of the product; it *is* the product. From the text on a button to the most detailed API documentation, clear, accessible, and actionable communication is the foundation of a successful user experience.

---

## The 5 Rulings

### OBLIGATORY (Core Principles)
**Mandatory practices for functional and accessible communication.**

-   **Clarity as Prime Directive**: Comprehension outweighs cleverness. Use simple language and active voice.
-   **Design for the Reader's Goal**: Structure content around user needs, not system architecture.
-   **Ensure Accessibility**: Text alternatives for visuals, semantic structure (`H1`->`H2`), and sufficient contrast (WCAG 2.1 AA).
-   **Treat Content as Product**: Version control (Git), ownership, and maintenance lifecycles for all documentation.
-   **Empathetic Tone**: Never blame the user. Use inclusive, respectful language.

### ENCOURAGED (Pillars of Practice)
**Recommended practices for high-quality content.**

-   **Semantic Hierarchy**: Use proper HTML tags (`<nav>`, `<article>`) and heading levels to encode meaning.
-   **Progressive Disclosure**: Reveal complexity incrementally (Quick Start -> Deep Dive).
-   **Scannability**: Use bullet points, bold keywords, and short paragraphs.
-   **Searchability**: Descriptive titles and metadata to ensure discoverability.
-   **Visual Communication**: Use diagrams and screenshots to clarify complex topics.
-   **Code as Communication**: Ensure code examples are testable, idiomatic, and well-commented.
-   **Style Guides**: Define and enforce voice, tone, and terminology.

### OPTIONAL (Discretionary)
**Frameworks and stylistic choices.**

-   **Diátaxis Framework**: Organizing docs into Tutorials, How-To, Reference, and Explanation.
    1.  **Tutorials (Learning-Oriented)**: A lesson that takes the reader by the hand through a series of steps to complete a project. The goal is to build confidence and understanding.
        -   *Analogy*: A teacher showing a student how to cook their first meal.

    2.  **How-To Guides (Goal-Oriented)**: A series of steps to solve a specific, real-world problem. Assumes some basic knowledge.
        -   *Analogy*: A recipe in a cookbook.

    3.  **Reference (Information-Oriented)**: A dry, technical description of the system's components, like API endpoints or configuration options. Its job is to be comprehensive and correct.
        -   *Analogy*: An encyclopedia or a dictionary.

    4.  **Explanation (Understanding-Oriented)**: A discussion that provides background and context, clarifying a particular topic.
        -   *Analogy*: An article on the history and theory of a culinary technique.

    A successful documentation suite contains all four types of content and links them appropriately. Don't try to write a single document that does all four things.
-   **Specific Diagramming Tools**: Mermaid, PlantUML, etc.
-   **Brand Voice Nuance**: Choosing between "Playful" vs "Serious" based on brand identity (as long as it remains clear).

### DISCOURAGED (Anti-Patterns)
**Practices that reduce clarity and maintainability.**

-   **Passive Voice**: Obscures who is performing the action.
-   **Jargon & Acronyms**: Using undefined terms that alienate beginners.
-   **"Click Here"**: Non-descriptive link text.
-   **Inconsistent Terminology**: Calling the same thing "User", "Client", and "Person" in the same doc.
-   **Wall of Text**: Long, unbroken paragraphs that are impossible to scan.

### PROHIBITED (Forbidden)
**Practices that mislead or harm the user.**

-   **Deceptive Patterns**: Wording designed to trick users (e.g., "Cancel" button that actually continues).
-   **Blaming the User**: Error messages like "You entered the wrong data" (vs "Invalid format").
-   **Broken Links**: Shipping documentation with dead internal links.
-   **Untested Code Examples**: Providing code snippets that do not compile or run.

---

## Practical Guides

### Error Message Framework
A good error message answers:
1.  **What happened?**
2.  **Why did it happen?**
3.  **How can I fix it?**
4.  **Where can I get help?**

### Selection by Role
-   **Technical Writers**: Focus on all principles, especially `Pillar III: Process & Governance`, to build a scalable content operation.
-   **Developers**: Focus on `Pillar II: Craft & Style`, especially `Code as Communication` and `Precision in Terminology` when writing API docs.
-   **UX Writers**: Focus on `Clarity`, `Empathy`, and `Voice & Tone` when crafting UI microcopy and error messages.
-   **Product Managers**: Focus on `Design for the Reader's Goal` and `Clarity` when writing specifications and release notes.

### Measurement
-   **Readability**: Flesch-Kincaid Grade ≤ 10.
-   **Structural**: 0 broken links.
-   **User Impact**: Search success rate ≥ 90%.
