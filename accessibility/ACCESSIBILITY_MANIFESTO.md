---
id: "accessibility"
title: "Accessibility Manifesto"
version: "2.1"
status: "current"
focus: "Universal access & WCAG compliance"
primary_users: ["frontend-developers", "designers", "accessibility-specialists", "all-developers"]
learning_curve: "medium"
roi_timeline: "immediate"
adoption_scope: "universal-legally-required"
principles_count: 4 # Was 15, revised to 4 core POUR principles
tier_structure:
  core: 4 # All POUR principles are core
  standard: 0
  excellence: 0
applicability:
  project_types: ["all-web", "all-mobile", "government", "education", "ecommerce", "healthcare"]
  languages: ["html", "css", "javascript", "swift", "kotlin"]
  contexts: ["public-facing", "customer-facing", "regulated"]
related_manifestos:
  complements: ["user-experience", "content-communication"]
  prerequisites: []
  enables: ["inclusive-design", "legal-compliance"]
tools:
  categories: ["automated-testing", "screen-readers", "design-validation", "ci-cd"]
  count: 40+
standards:
  - "WCAG 2.1 AA/AAA"
  - "Section 508"
  - "ADA"
  - "EAA (EU)"
  - "AODA (Ontario)"
  - "EN 301 549"
measurement:
  automated_testing:
    axe_core_violations:
      wcag_a:
        target: "0 violations"
        blocking: true
      wcag_aa:
        target: "0 violations"
        blocking: true
      wcag_aaa:
        target: "≤5 violations"
        blocking: false
      measurement: "axe-devtools-cli"
    lighthouse_accessibility_score:
      target: "≥95"
      acceptable: "≥90"
      alert_threshold: "<90"
      measurement: "lighthouse-ci"
  manual_testing:
    keyboard_navigation:
      target: "100% functionality accessible"
      measurement: "manual-qa-checklist"
    screen_reader_task_completion:
      target: "≥95% success rate"
      acceptable: "≥90%"
      measurement: "user-testing-with-blind-users"
  color_contrast:
    text_normal:
      target: "≥4.5:1"
      wcag_level: "AA"
      measurement: "colour-contrast-analyser"
    text_large:
      target: "≥3:1"
      wcag_level: "AA"
      measurement: "colour-contrast-analyser"
    ui_components:
      target: "≥3:1"
      wcag_level: "AA"
      measurement: "colour-contrast-analyser"
  touch_targets:
    minimum_size:
      target: "≥44×44px"
      wcag_level: "AA"
      measurement: "manual-inspection-design-tools"
---
# The Accessibility Manifesto

**Version**: 2.0
**Last Updated**: 2025-11-23
**Conformance**: WCAG 2.1 Level AA

> Accessibility is not a feature, a burden, or an edge case. It is a fundamental human right, a legal requirement, and the mark of a quality product. We build for everyone, or we fail. This manifesto outlines the principles for creating universally accessible digital experiences.

---

## The Universal Design Mandate

Our guiding philosophy is **Universal Design**: the design of products to be usable by all people, to the greatest extent possible, without the need for adaptation.

-   **Curb cuts** built for wheelchairs benefit people with strollers, luggage, and bicycles.
-   **Captions** built for deaf users benefit people in noisy environments and language learners.
-   **High-contrast text** built for low-vision users benefits everyone in bright sunlight.

By designing for disability first, we create better products for everyone.

---

## The Four Core Principles (POUR)

Our work is grounded in the four principles of the Web Content Accessibility Guidelines (WCAG). For a product to be accessible, it must be **Perceivable, Operable, Understandable, and Robust.**

### 1. Perceivable
**Users must be able to perceive the information being presented; it can't be invisible to all of their senses.**

-   **Provide Text Alternatives**: All non-text content (images, icons, diagrams) must have a text alternative (`alt` text) that serves the equivalent purpose.
-   **Provide Alternatives for Time-Based Media**: All video must have synchronized captions, and all audio must have a transcript. Provide audio descriptions for important visual information in videos.
-   **Create Adaptable Content**: Use semantic structure (see Principle 4) so that content can be presented in different ways (e.g., a screen reader's simplified layout) without losing information.
-   **Ensure Content is Distinguishable**: Make it easy for users to see and hear content. This includes ensuring a minimum color contrast of **4.5:1 for text** and **3:1 for UI components**, and not using color as the *only* way to convey information.

### 2. Operable
**Users must be able to operate the interface; the interface cannot require interaction that a user cannot perform.**

-   **Ensure Full Keyboard Accessibility**: All functionality must be operable through a keyboard, without requiring a mouse. The tab order must be logical, and focus states must be clearly visible.
-   **Provide Enough Time**: Give users enough time to read and use content. Avoid arbitrary time limits, and if a session must expire, provide a warning with an option to extend it.
-   **Do Not Cause Seizures or Physical Reactions**: Do not design content that flashes more than three times per second. Respect the `prefers-reduced-motion` media query.
-   **Make Navigation Easy**: Provide users with ways to navigate, find content, and determine where they are. A "skip to main content" link should be the first focusable element on a page.

### 3. Understandable
**Users must be able to understand the information as well as the operation of the user interface.**

-   **Make Text Readable and Comprehensible**: Use plain language appropriate for your audience. Avoid jargon and define acronyms on first use.
-   **Make Content Appear and Operate in Predictable Ways**: Navigation and component behavior should be consistent throughout the product.
-   **Help Users Avoid and Correct Mistakes**: Provide clear error messages that identify the problem and suggest a solution. Required fields in forms should be clearly marked.

### 4. Robust
**Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.**

-   **Use Valid, Semantic HTML**: Write code that conforms to web standards. Use `<button>` for buttons, `<nav>` for navigation, and `<main>` for the main content area. A `<div>` is not a button.
-   **Use ARIA Correctly**: Use ARIA (Accessible Rich Internet Applications) attributes to enhance semantics where necessary, but never in place of correct native HTML.
-   **Communicate Name, Role, and Value**: Ensure that all custom components report their name, role (e.g., "button"), and state (e.g., "checked") to assistive technologies.

---

## Getting Started: What You Can Do in 5 Minutes

Accessibility can feel overwhelming. Here are three simple checks you can perform on any web page right now to find high-impact issues.

1.  **Unplug Your Mouse**: Can you use every single feature of the page using only the `Tab`, `Shift+Tab`, `Enter`, `Space`, and arrow keys? Is it always clear where your focus is? If not, you have keyboard accessibility issues.
2.  **Install an `axe-core` Browser Extension** (like `axe DevTools`): Run the automated scanner. It will catch ~30-50% of WCAG issues, such as missing alt text and insufficient color contrast.
3.  **Enable a Screen Reader**: Turn on your operating system's built-in screen reader (VoiceOver on Mac, Narrator on Windows) and try to navigate your page. Can you understand the content? Can you operate the controls? This will quickly reveal issues with semantic structure and labeling.

---

## A Practical Guide to Implementation

### Conformance Tiers
Adopt accessibility in progressive stages.

-   **Tier 1: Core (WCAG Level A)**
    -   **Goal**: Meet the legal minimum and remove the most severe barriers.
    -   **Key Actions**: Ensure keyboard accessibility, provide text alternatives for all images, add captions to videos, and avoid keyboard traps.
-   **Tier 2: Standard (WCAG Level AA)**
    -   **Goal**: Achieve the industry-standard baseline for accessibility.
    -   **Key Actions**: Meet color contrast requirements, ensure all UI components have visible focus states, and provide descriptive error messages.
-   **Tier 3: Excellence (WCAG Level AAA & Inclusive Design)**
    -   **Goal**: Provide a best-in-class, fully inclusive experience.
    -   **Key Actions**: Test with a diverse group of users with disabilities, provide sign language interpretation for videos, and ensure exceptionally high color contrast.

### Measurement Framework
-   **Automated Testing**: 100% pass rate on an `axe-core` based scanner in your CI/CD pipeline.
-   **Manual Testing**: 100% keyboard operability for all features.
-   **User Testing**: Task completion rates for users of assistive technology should be ≥90% of the rate for users without disabilities.
-   **Bug Tracking**: Treat accessibility issues with the same severity as functional bugs. A WCAG Level A violation is a "critical" bug.

---

## Appendices

*(This section would link to the detailed content from the original manifesto, reformatted as appendices.)*

-   **Appendix A: Detailed Implementation Guides for All 15 Original Principles**
-   **Appendix B: Accessibility Tooling Ecosystem**
-   **Appendix C: WCAG 2.1 Quick Reference Guide**
-   **Appendix D: Legal & Compliance Context (ADA, Section 508, EAA)**
