---
name: content-communication-review
description: Draft, review, and improve documentation, interface copy, error messages, API docs, and other user-facing content for clarity, accessibility, maintainability, and reader success.
---
# Content and Communication Review

Identify the audience and their intended task before editing. Review structure, terminology, accessibility, maintenance ownership, and actionability. Preserve technical meaning, distinguish factual defects from style preferences, and return replacement text or concrete edits when the user asks for remediation.

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

### Process and Governance

Apply **Treat Content as Product** throughout the content lifecycle:

- Assign an owner and define who creates, reviews, and approves publication for each content type.
- Keep content in version control. Review changes for technical accuracy, working links, tested examples, accessibility, and current screenshots before publication.
- Set a review cadence and update version-specific guidance with each release. Track reader feedback and correct stale content.
- When retiring content, announce the change, provide migration guidance, and archive or redirect obsolete pages.

### Craft and Style

Apply **Code as Communication** and **Style Guides** when drafting technical content:

- Provide complete, idiomatic examples with prerequisites and expected results. Test them in the stated environment; explain intent in comments and progress from simple to complex examples.
- Define domain terms before use, expand acronyms on first use, and maintain a glossary for ambiguous terms. Use one term for each concept consistently across documentation and UI labels.
- Preserve technical distinctions. Do not substitute a familiar word for a different technical concept merely for stylistic variety.

### Voice and Tone

Apply **Clarity as Prime Directive** and **Empathetic Tone** across touchpoints:

- Keep the product's voice consistent while adapting tone to context: encouraging for onboarding, precise for reference material, and calm and solution-focused for errors.
- Use inclusive, respectful language. Acknowledge frustration without blaming, condescending to, or joking at the reader's expense.
- Document terminology, voice, and tone choices with examples. Keep instructions actionable and never let brand personality obscure consequences or recovery steps.

### Error Message Framework
A good error message answers:
1.  **What happened?**
2.  **Why did it happen?**
3.  **How can I fix it?**
4.  **Where can I get help?**

### Selection by Role
-   **Technical Writers**: Apply all principles, emphasizing [Process and Governance](#process-and-governance) to build a maintainable content operation.
-   **Developers**: Apply [Craft and Style](#craft-and-style) to API documentation, terminology, and executable examples.
-   **UX Writers**: Apply [Voice and Tone](#voice-and-tone) and the [Error Message Framework](#error-message-framework) to interface copy and recovery instructions.
-   **Product Managers**: Apply **Design for the Reader's Goal** and **Clarity as Prime Directive** under [OBLIGATORY (Core Principles)](#obligatory-core-principles) to specifications and release notes.

### Measurement
-   **Readability**: Flesch-Kincaid Grade ≤ 10.
-   **Structural**: 0 broken links.
-   **User Impact**: Search success rate ≥ 90%.
