---
id: "user-experience"
title: "The User Experience Manifesto"
version: "2.1"
status: "current"
focus: "User success, satisfaction, and ethical design"
primary_users: ["designers", "product-managers", "frontend-developers", "ux-researchers"]
learning_curve: "medium"
roi_timeline: "immediate-medium"
adoption_scope: "universal-product-focused"
principles_count: 15 # As revised
tier_structure:
  core: 5
  standard: 6
  excellence: 4
applicability:
  project_types: ["web-apps", "mobile-apps", "voice-ui", "ar-vr", "iot", "design-systems"]
  languages: ["javascript", "swift", "kotlin", "html", "css"]
  contexts: ["user-facing", "b2c", "b2b", "consumer", "enterprise"]
related_manifestos:
  complements: ["accessibility", "content-communication", "security-hardening"]
  prerequisites: []
  enables: ["user-satisfaction", "conversion", "retention"]
tools:
  categories: ["testing", "analytics", "design", "prototyping"]
  count: 30+
standards:
  - "Nielsen Heuristics"
  - "WCAG 2.1 AA"
  - "Core Web Vitals"
  - "Privacy-by-Design"
measurement:
  usability_testing:
    task_success_rate:
      target: "≥95%"
      acceptable: "≥90%"
    time_on_task:
      target: "≤expected-time"
    error_rate:
      target: "≤5%"
  user_satisfaction:
    nps: # Net Promoter Score
      target: "≥50"
    csat: # Customer Satisfaction
      target: "≥4.5/5"
    sus: # System Usability Scale
      target: "≥80"
  performance:
    lcp: # Largest Contentful Paint
      target: "≤2.5s"
    fid: # First Input Delay
      target: "≤100ms"
    cls: # Cumulative Layout Shift
      target: "≤0.1"
---
# User Experience Manifesto: 15 Foundational Principles

**Version**: 2.1
**Last Updated**: 2025-11-23
**Conformance**: WCAG 2.1 Level AA

---

## Introduction

The goal of user experience (UX) design is to create products and services that are effective, efficient, and enjoyable to use. This manifesto codifies a set of foundational principles to guide teams in creating user-centric experiences. It asserts that good UX is not a luxury; it is a fundamental requirement for success.

The ultimate measure of quality is the user's ability to achieve their goals with minimum friction and maximum satisfaction. These principles are a framework for achieving that outcome.

---

## Guiding Philosophies

These mindsets should inform every decision, providing the context in which the following principles are applied.

-   **Simplicity is Hard-Won**: The first draft is never simple enough. True simplicity is achieved by iteratively removing the non-essential until only clarity remains.
-   **Content-First Design**: The interface serves the content. Design in the absence of content is decoration. The structure, hierarchy, and clarity of the information is paramount.
-   **Mobile-First & Progressive Enhancement**: Design for the most constrained context first (e.g., small screens, slow networks), then progressively add features and complexity for more capable environments.
-   **Localization by Design**: Plan for a global audience from day one. Accommodate text expansion, right-to-left (RTL) layouts, and diverse cultural conventions for formats and symbols.
-   **Respect User Agency**: The user is in control. Your design should respect their choices, system-level preferences (like font size or reduced motion), and provide customization where appropriate.

---

## Core Principles (Non-negotiable Fundamentals)

These are the absolute foundations of a good user experience. A failure in any of these areas represents a fundamental failure of the design.

### 1. User Primacy
**Design must serve user goals, not organizational convenience or technical elegance.**

Every decision must be justified by its benefit to the user. The user's mental model of the task should shape the interface, not the system's underlying architecture.

-   **Metrics**: Task completion rate, error rate, and user satisfaction are the primary measures of success.
-   **Invalid Rationale**: "It's easier to implement this way" is not a valid reason to compromise the user experience.

---

### 2. Accessibility as Foundation
**Interfaces must be perceivable, operable, understandable, and robust for all users, including those with disabilities.**

Accessibility is a legal and moral imperative that benefits everyone. It is not an add-on, but a core requirement.

-   **Standard**: WCAG 2.1 AA is the minimum baseline.
-   **Key Practices**: Ensure full keyboard navigation, screen reader compatibility, sufficient color contrast (≥4.5:1), and that color is not the only means of conveying information.
-   **Respect Preferences**: The system must respect user settings like `prefers-reduced-motion` and system font sizes.

---

### 3. Privacy & Ethical Design
**User data is sacred. The design must be transparent, consensual, and free of manipulative patterns.**

Trust is hard-won and easily lost. Ethical design respects the user's attention, data, and autonomy.

-   **Minimal Data**: Collect only the data necessary to perform the task.
-   **Explicit Consent**: Use clear, plain language to explain why data is needed. Opt-in is required.
-   **No Dark Patterns**: Never use deceptive UI to trick users into actions they did not intend (e.g., hidden costs, confusing subscription flows).
-   **Explainability**: Algorithmic decisions that affect the user should be explainable. Provide a "Why am I seeing this?" feature for recommendations.

---

### 4. Clarity and Recognition
**Interfaces must be immediately comprehensible. Minimize the user's memory load by making objects, actions, and options visible.**

Users should not have to remember information from one part of the interface to another. Strive for recognition over recall.

-   **Use Conventions**: Employ standard icons, conventional placements, and predictable behaviors. Novelty must provide a significant benefit to justify its cognitive cost.
-   **Show, Don't Tell**: Use dropdowns instead of requiring users to recall and type specific options. Provide auto-complete and lists of recently used items.
-   **Contextual Help**: Place help and instructions adjacent to the controls they describe.

**Example**: A booking website should show the selected dates and times throughout the entire checkout flow, rather than requiring the user to remember them.

---

### 5. Consistency & Coherence
**Similar elements must look and behave in similar ways. Patterns must be applied system-wide.**

A consistent design creates a predictable and learnable experience. This "internal consistency" allows users to transfer knowledge from one part of your product to another.

-   **Vocabulary**: Establish and consistently apply a vocabulary for colors, terminology, icons, and layout (e.g., the primary action button is always in the same location).
-   **Platform Standards**: Adhere to the conventions of the platform (iOS, Android, Web) to ensure "external consistency."
-   **Touch Targets**: Ensure all interactive elements have a minimum touch target of 44x44px.

---

## Standard Principles (Required for a Professional Product)

Once the core principles are met, these standards elevate the experience from merely functional to efficient and user-friendly.

### 6. Immediate Feedback
**Every user action must produce a perceptible response within 100ms.**

The interface must immediately acknowledge all user input. Silence and inaction breed uncertainty and frustration.

-   **< 100ms**: The response feels instantaneous (e.g., a button press highlights immediately).
-   **100ms - 1s**: A progress indicator (like a spinner) is needed to show the system is working.
-   **> 1s**: A detailed progress bar with a percentage and a cancellation option is required.
-   **Failure**: Failed operations must provide an explicit error message with a clear path to resolution.

---

### 7. Error Prevention
**Design to make errors difficult to commit in the first place.**

A great design anticipates potential mistakes and guides the user away from them. It is always better to prevent an error than to write a good error message.

-   **Constraints**: Use constraints to prevent invalid input (e.g., disable future dates in a birthdate picker).
-   **Smart Defaults**: Provide sensible defaults that align with the most common user goals.
-   **Confirmation**: Require confirmation for destructive actions, and make the confirmation dialog specific (e.g., "Permanently delete this file?").

---

### 8. Forgiveness & Reversibility
**Users must be able to easily recover from errors without significant cost or data loss.**

Assume users will make mistakes. Empower them to explore the interface without fear by making actions easily reversible.

-   **Undo**: A universal "Undo" (`Ctrl+Z`) should be available for most actions.
-   **Non-Destructive Actions**: Deleting an item should move it to a "Trash" or "Archive" from which it can be recovered, rather than deleting it permanently.
-   **Autosave**: Preserve the user's work automatically to protect against crashes or accidental closures.

**Example**: An email client that offers a 10-second "Undo Send" window after an email is sent.

---

### 9. Progressive Disclosure
**Reveal complexity incrementally. Present the minimum viable interface first.**

Avoid overwhelming users with too many options. Show the most common features by default and allow users to discover advanced functionality as they become more familiar with the product.

-   **Initial View**: The default view should contain only the 3-5 most critical actions.
-   **Secondary Features**: Advanced features should be accessible but not prominent (e.g., in an "Advanced" panel or settings menu).
-   **Expert Paths**: Provide shortcuts, command palettes, and bulk operations for power users to bypass novice workflows.

---

### 10. Efficiency & Flow
**Frequent tasks must be achievable with minimal interaction. The design should facilitate a state of deep focus.**

Optimize the paths for the most common user journeys. Remove every possible point of friction from repetitive workflows.

-   **Reduce Clicks**: The core user journey should be achievable in 3 clicks/taps or fewer.
-   **Keyboard Shortcuts**: Allow power users to perform any primary action without using a mouse.
-   **Bulk Operations**: If a user can do something once, they should be able to do it to 100 items at once (e.g., bulk-tagging files).

---

### 11. Navigation & Findability
**Users must be able to locate content and orient themselves within the product through multiple, intuitive paths.**

A user should never feel lost. The product's structure should be predictable, and their current location should always be clear.

-   **Clear Hierarchy**: Keep navigation structures shallow (ideally <3 levels deep).
-   **Search**: A robust search function is essential for any product with more than ~20 items of content.
-   **Wayfinding Cues**: Use breadcrumbs, clear headings, and visual landmarks to indicate the user's location.
-   **Multiple Paths**: Allow users to reach content via navigation, search, and contextual links.

---

## Excellence Principles (The Differentiators)

These principles distinguish a good product from a great one. They focus on craft, delight, and continuous improvement.

### 12. Aesthetic Integrity
**The visual design must reinforce the product's structure, function, and brand identity. Decoration should be purposeful.**

Beauty and usability are not in conflict; beauty emerges from clarity and purpose. Every visual element should serve a function.

-   **Hierarchy**: Use typography, color, and spacing to create a clear visual hierarchy that guides the user's attention.
-   **Whitespace**: Use negative space intentionally to group related items and separate unrelated ones.
-   **Animation**: Use animation to communicate state changes and guide the user, not for decoration. Keep transitions swift (200-400ms).

---

### 13. Performance as a Feature
**The perceived speed of the product is a critical design element. Responsiveness is non-negotiable.**

A slow interface feels broken. Performance directly impacts user satisfaction and is a form of accessibility, as it disproportionately affects users with older devices or slower connections.

-   **Core Web Vitals**: Aim for LCP <2.5s, FID <100ms, CLS <0.1.
-   **Interaction Latency**: Interactions must be acknowledged in <100ms.
-   **Optimistic UI**: Update the UI immediately in response to user actions, and handle the background state change asynchronously. Show a success state by default and roll back only if an error occurs.

---

### 14. Contextual Relevance
**The interface should adapt to present the most relevant information and actions based on the user's current goal and context.**

The system should be smart enough to anticipate the user's needs based on their state, location, time, and history.

-   **Empty States**: An empty screen is a design opportunity. Guide the user on what to do next.
-   **Adaptive Actions**: Show "Add to Album" when an album is open; show "Create New Album" when one isn't.
-   **Location & Time**: A map app should suggest navigating home at the end of the workday.

---

### 15. Continuous Validation
**Designs are hypotheses that must be validated with real users. The team must be committed to learning and iteration.**

You are not the user. Your assumptions, however well-intentioned, must be tested against reality.

-   **Qualitative & Quantitative**: Use analytics to understand *what* users are doing, and use user research (e.g., interviews, usability tests) to understand *why*.
-   **Usability Testing**: Test with at least 5 users per iteration to uncover the most significant issues.
-   **Inclusive Research**: Your participant pool must be diverse and include users with disabilities.

---

## Principle Precedence & Conflict Resolution

When principles conflict, use this hierarchy to make decisions:

1.  **Accessibility (2) & Privacy/Ethics (3)**: These are non-negotiable and trump all other considerations.
2.  **User Primacy (1)**: Use user goals and data from user research to arbitrate conflicts between other principles.
3.  **Clarity (4)**: When in doubt, choose the clearest and most obvious option.

**Example Conflict**: `Consistency (5)` vs. `Contextual Relevance (14)`. The standard navigation pattern is on the top, but for a mobile app, it might be more contextually relevant at the bottom for thumb reachability.
**Resolution**: Defer to `User Primacy (1)`. Does user data show a significant improvement in task completion with the adaptive, context-relevant UI? If so, the deviation from consistency is justified. Document the decision.
