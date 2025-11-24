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

## The Five Core Principles

These five principles are the foundation of effective communication. They apply to all forms of content, from UI microcopy to technical manuals.

### 1. Clarity is the Prime Directive.
Comprehension outweighs cleverness, brevity, or stylistic flair. Your primary duty is to be understood. Use simple language, active voice, and concrete examples. If the reader is confused, the content has failed.

### 2. Design for the Reader's Goal.
Structure content to help the reader achieve their objective as quickly as possible. Don't organize by what *you* want to say; organize by what *they* need to do. An effective structure anticipates the user's journey and provides the right information at the right time.

### 3. Be Empathetic and Respectful.
Your reader may be frustrated, stressed, or new to the topic. Write with patience and respect. Acknowledge potential confusion, use inclusive language, and never blame the user for errors. Good content builds trust.

### 4. Ensure Accessibility for All.
Content must be usable by everyone, including people with disabilities. This is a legal, moral, and business imperative. Adhere to WCAG 2.1 AA as a minimum baseline. Use semantic structure, provide text alternatives for visuals, and ensure sufficient color contrast.

### 5. Treat Content as a Product.
Content requires the same rigor as code. It must be versioned, tested, owned, and maintained. It has a lifecycle, requires a strategy, and its performance must be measured. "Docs or it didn't happen" applies to features and the content that describes them.

---

## The Pillars of Practice

These pillars provide the practical framework for implementing the core principles.

### Pillar I: Architecture & Structure
*(How to organize content for user success)*

-   **Semantic Hierarchy**: Structure must encode meaning. Use headings sequentially (`H1` → `H2` → `H3`). Use semantic HTML (`<nav>`, `<button>`, `<article>`) to enable accessibility and machine readability.
-   **Progressive Disclosure**: Reveal complexity incrementally. Start with a "Quick Start" guide, then provide paths to deeper knowledge. In UI, hide advanced settings behind an explicit user action.
-   **Scannability**: Users scan before they read. Optimize for scanning with clear headings, short paragraphs, bulleted lists, and bolded keywords. Front-load the most important information.
-   **Searchability & Discoverability**: Use descriptive titles, relevant keywords, and rich metadata to ensure content can be found via internal and external search. Use internal links to create a connected web of knowledge.

### Pillar II: Craft & Style
*(How to write clear, consistent, and effective content)*

-   **Precision in Terminology**: Use a consistent, defined set of terms. Avoid synonyms for the same concept. A "user" should always be a "user," not sometimes a "person" or "client." Create and maintain a glossary.
-   **Voice & Tone Consistency**: Define a consistent brand voice (your personality) and adapt the tone for the context (e.g., celebratory for success messages, apologetic for critical errors).
-   **Visual Communication**: Use diagrams, screenshots, and tables to clarify complex relationships and procedures. A good diagram is worth a thousand words. Ensure all visuals have text alternatives.
-   **Code as Communication**: Code examples must be correct, complete, and testable. They should be idiomatic to the language and commented to explain the *why*, not the *what*.

### Pillar III: Process & Governance
*(How to manage content at scale)*

-   **Version Control & Docs-as-Code**: Treat documentation like code. Store it in Git, review changes via pull requests, and deploy it with automated checks.
-   **Maintenance & Ownership**: All content must have a designated owner. Implement a process for regular reviews, link checking, and flagging of stale content. Content without an owner will rot.
-   **Content Strategy & Governance**: Define workflows for creating, reviewing, publishing, and archiving content. A clear strategy ensures consistency and quality as the team grows.
-   **Continuous Measurement**: Content effectiveness must be measured. Track metrics like page views, search success rate, task completion, and user satisfaction ("Was this page helpful?"). Use this data to drive improvements.

---

## Content in Practice: The Diátaxis Framework

To implement the principle of "Design for the Reader's Goal," organize technical documentation according to the user's immediate need. The Diátaxis framework proposes four distinct types of content:

1.  **Tutorials (Learning-Oriented)**: A lesson that takes the reader by the hand through a series of steps to complete a project. The goal is to build confidence and understanding.
    -   *Analogy*: A teacher showing a student how to cook their first meal.

2.  **How-To Guides (Goal-Oriented)**: A series of steps to solve a specific, real-world problem. Assumes some basic knowledge.
    -   *Analogy*: A recipe in a cookbook.

3.  **Reference (Information-Oriented)**: A dry, technical description of the system's components, like API endpoints or configuration options. Its job is to be comprehensive and correct.
    -   *Analogy*: An encyclopedia or a dictionary.

4.  **Explanation (Understanding-Oriented)**: A discussion that provides background and context, clarifying a particular topic.
    -   *Analogy*: An article on the history and theory of a culinary technique.

A successful documentation suite contains all four types of content and links them appropriately. Don't try to write a single document that does all four things.

---

## Practical Guides

### Selection by Role
-   **Technical Writers**: Focus on all principles, especially `Pillar III: Process & Governance`, to build a scalable content operation.
-   **Developers**: Focus on `Pillar II: Craft & Style`, especially `Code as Communication` and `Precision in Terminology` when writing API docs.
-   **UX Writers**: Focus on `Clarity`, `Empathy`, and `Voice & Tone` when crafting UI microcopy and error messages.
-   **Product Managers**: Focus on `Design for the Reader's Goal` and `Clarity` when writing specifications and release notes.

### Error Message Framework
A good error message is empathetic and actionable. It should answer four questions:
1.  **What happened?**: "Save Failed."
2.  **Why did it happen?**: "You are not connected to the internet."
3.  **How can I fix it?**: "Please check your connection and try again."
4.  **Where can I get more help?**: "Contact support if the problem persists."

---

## Appendices

*(This section would link to the detailed content from the original manifesto, reformatted as appendices.)*

-   **Appendix A: Detailed Implementation Guides for all 18 Original Principles**
-   **Appendix B: Content Tooling Ecosystem Map**
-   **Appendix C: Content Maturity Model**
-   **Appendix D: Checklists and Measurement Frameworks**
