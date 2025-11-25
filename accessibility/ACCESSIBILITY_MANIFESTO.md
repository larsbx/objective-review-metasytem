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
  core: 4
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

**Version**: 2.1
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

## The 5 Rulings

### OBLIGATORY (Core Principles & Tier 1)
**Mandatory practices. These correspond to WCAG Level A and core POUR principles.**

-   **Perceivable - Text Alternatives**: All non-text content (images, icons) must have a text alternative (`alt` text).
-   **Perceivable - Captions**: All video must have synchronized captions; all audio must have transcripts.
-   **Operable - Keyboard Accessible**: All functionality must be operable via keyboard. No mouse required.
-   **Operable - No Keyboard Traps**: Focus must never get stuck in a component.
-   **Understandable - Error Identification**: Errors in forms must be clearly identified and described in text.
-   **Robust - Semantic HTML**: Use valid HTML (e.g., `<button>` for buttons, not `<div>`).

### ENCOURAGED (Standard - Tier 2)
**Highly recommended practices. These correspond to WCAG Level AA.**

-   **Color Contrast**: Minimum 4.5:1 for normal text, 3:1 for large text and UI components.
-   **Visible Focus**: Focus indicators must be clearly visible and have good contrast.
-   **Resize Text**: Text must resize up to 200% without loss of content or functionality.
-   **Consistent Navigation**: Navigation mechanisms should appear in the same order on every page.
-   **Descriptive Headings & Labels**: Headings and labels must describe the topic or purpose clearly.

### OPTIONAL (Excellence - Tier 3)
**Discretionary practices for inclusive excellence. WCAG Level AAA.**

-   **Sign Language**: Providing sign language interpretation for media.
-   **Extended Audio Description**: Detailed narration for video content.
-   **Target Size (Enhanced)**: Touch targets ≥ 44x44px (AAA level).
-   **No Interruptions**: Allowing users to suppress interruptions and alerts.

### DISCOURAGED (Anti-Patterns)
**Practices that degrade accessibility and should be avoided.**

-   **"Click Here" Links**: Use descriptive link text (e.g., "Read the report").
-   **Positive `tabindex`**: Manually setting `tabindex="1"` etc. disrupts logical flow.
-   **Removing Focus Outlines**: `outline: none` without a replacement style makes navigation impossible for many.
-   **Autoplay Media**: Audio/video playing automatically can be disorienting.
-   **Arbitrary Time Limits**: Requiring actions within a short time window without extension options.

### PROHIBITED (Forbidden)
**Practices that create absolute barriers or safety risks.**

-   **Flashing Content (>3 times/sec)**: Can trigger seizures. This is a critical safety violation.
-   **Keyboard Traps**: Locking a user inside a component so they cannot tab out.
-   **Color-Only Information**: Using color as the *only* visual means of conveying information (e.g., "Press the green button").
-   **Inaccessible CAPTCHAs**: Preventing users from accessing service due to visual-only challenges.

---

## Measurement Framework

-   **Automated Testing**: 100% pass rate on `axe-core` scanner.
-   **Manual Testing**: 100% keyboard operability check.
-   **User Testing**: ≥95% success rate for screen reader users.
