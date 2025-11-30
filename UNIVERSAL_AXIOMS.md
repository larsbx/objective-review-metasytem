# The Universal Axioms of System Design

This document expands the **Objective Review Metasystem** by drawing wisdom from a systematic taxonomy of human knowledge. It maps principles from diverse domains—from Physics to Philosophy, Martial Arts to Mysticism—into actionable maxims for software engineering.

---

## I. Formal Sciences & Logic
*Foundational truths and structural integrity.*

*   **Mathematics (Axioms)**: **Invariant Maintenance**. Identify the properties of your system that must *always* be true (e.g., "Account balance cannot be negative") and enforce them at the database level.
*   **Logic (Inference)**: **Boolean Clarity**. Avoid complex nested conditionals. Simplify logic to its most reducible truth tables.
*   **Statistics (Inference)**: **P99 Observability**. Do not judge performance by averages; judge it by the outliers (99th percentile latency).
*   **Information Theory (Entropy)**: **Signal-to-Noise Ratio**. In code and logs, maximize information density. Delete comments that merely repeat the code.

## II. Natural Sciences
*Laws of the physical universe applied to the digital.*

*   **Physics (Thermodynamics)**: **Conservation of Complexity**. Complexity cannot be destroyed, only moved. Choose consciously whether to burden the developer (implementation complexity) or the user (interface complexity).
*   **Chemistry (Reactivity)**: **Atomic Design**. Build UIs from fundamental, indivisible elements (atoms) that combine into molecules (components) and organisms (pages).
*   **Biology (Evolution)**: **Evolutionary Architecture**. Architectures must support incremental change. Monoliths that cannot evolve will go extinct.
*   **Geology (Superposition)**: **Immutable Logs**. Treat system history like sediment. Never overwrite the past; only append new layers of facts.
*   **Medicine (Hippocratic Oath)**: **Do No Harm**. A deployment should never leave the system in a worse state than it found it. Implement rollbacks and circuit breakers.

## III. Social Sciences
*Human dynamics in technical systems.*

*   **Economics (Rational Choice)**: **Technical Debt Interest**. Bad code is a loan. You pay interest in the form of slower velocity. Pay down the principal regularly.
*   **Psychology (Cognitive Load)**: **Miller’s Law**. Interfaces (and APIs) should not demand the user hold more than 7 (±2) items in working memory.
*   **Sociology (Conway’s Law)**: **Mirroring**. Your software architecture will inevitably resemble your organizational communication structure. Reverse-engineer this: structure your teams to get the architecture you want.
*   **Anthropology (Tribal Knowledge)**: **Explicit Documentation**. Move knowledge from oral tradition (Slack/Zoom) to written history (Markdown/Wikis).
*   **Linguistics (Semantics)**: **Ubiquitous Language**. The code must use the same vocabulary as the business experts (Domain-Driven Design).

## IV. Philosophy & Metaphysics
*Reasoning about the nature of the system.*

*   **Epistemology (Falsifiability)**: **Red-Green Refactor**. We only "know" code works if we have seen it fail. A test that never fails proves nothing.
*   **Metaphysics (Ontology)**: **Domain Modeling**. Spend time defining *what exists* in your system. A confused data model leads to confused code.
*   **Stoicism (Dichotomy of Control)**: **Error Handling**. Distinguish between errors you can control (validation) and those you cannot (network failure). Handle the former with logic, the latter with resilience.
*   **Philosophy of Science (Parsimony)**: **Occam’s Razor**. Among competing solutions, the one with the fewest moving parts is usually correct.

## V. Religious & Spiritual Traditions (Abrahamic)
*Law, Covenant, and Structure.*

*   **Islamic Jurisprudence (Qiyas)**: **Pattern Matching**. Solve new problems by drawing analogies to established patterns (Design Patterns).
*   **Islamic Theology (Tawhid)**: **Single Source of Truth**. Data must have a single, unified representation; avoid split-brain scenarios and data duplication.
*   **Christian Theology (Grace vs Works)**: **Declarative vs Imperative**. Grace is Declarative (what you are); Works is Imperative (what you do). Prefer Declarative (SQL/React) over Imperative (jQuery).
*   **Jewish Thought (Pilpul)**: **Code Review**. The rigorous, dialectical analysis of code to uncover edge cases and deeper truths.
*   **Jewish Thought (Tikkun Olam)**: **Refactoring**. The continuous process of repairing the world (the codebase) and restoring it to its intended state.

## VI. Religious & Spiritual Traditions (Eastern)
*Flow, Awareness, and Interconnection.*

*   **Buddhist Philosophy (Dependent Origination)**: **Causal Graphs**. Nothing exists in isolation; every bug has a chain of causality. Trace the root cause, not just the symptom.
*   **Buddhist Philosophy (Impermanence)**: **Chaos Engineering**. Everything fails. Servers die. Networks partition. Design for failure.
*   **Hindu Philosophy (Karma)**: **Technical Debt**. Every action (hack) generates a reaction (bug) that must eventually be resolved.
*   **Taoism (Wu Wei)**: **Serverless**. The ultimate action is non-action. Let the platform handle the infrastructure.
*   **Confucianism (Rectification of Names)**: **Naming Conventions**. If names are incorrect, language is not in accordance with the truth of things. Use precise, agreed-upon terminology.

## VII. Esoteric & Occult Sciences
*Hidden knowledge, transformation, and systems.*

*   **Hermeticism (Correspondence)**: **Fractal Architecture**. "As above, so below." The structure of the function mirrors the class, which mirrors the module, which mirrors the system.
*   **Kabbalah (Tzimtzum)**: **YAGNI/Minimalism**. The creator must contract (limit scope) to make space for the creation (the MVP) to exist.
*   **Alchemy (Solve et Coagula)**: **Refactoring**. Dissolve the code (break it down) and coagulate it (reassemble it) into a purer form.
*   **Astrology (Transits)**: **Scheduled Maintenance**. Understand the temporal cycles of your system (daily peaks, weekly batch jobs) and align operations accordingly.
*   **Tarot (The Fool)**: **Greenfield Projects**. The beginning of the journey requires a leap of faith into the unknown, but with readiness for the fall.
*   **Chakra System (Energy Flow)**: **Data Pipelines**. Ensure the flow of data (Qi) is unblocked from ingestion (Root) to analytics (Crown).

## VIII. Applied Arts & Crafts
*Form, function, and beauty.*

*   **Architecture (Form Follows Function)**: **API Design**. The shape of the interface should be determined by how it is used, not how it is implemented.
*   **Music (Rhythm)**: **Code Cadence**. Good code has a visual rhythm (indentation, spacing) that aids reading.
*   **Literature (Narrative)**: **Commit Messages**. The git log is a story. Write it so the reader can follow the plot twist of a bug fix.
*   **Culinary Arts (Mise en place)**: **Environment Setup**. Have all your tools and dependencies ready and organized before you start cooking (coding).

## IX. Professional & Technical Domains
*Operational excellence.*

*   **Law (Precedent)**: **Patterns**. Do not invent new legal theories (algorithms) when established precedents (design patterns) exist.
*   **Military Strategy (OODA Loop)**: **Observability**. Observe, Orient, Decide, Act. The faster your feedback loop (CI/CD), the more likely you are to win.
*   **Journalism (Verification)**: **Post-Mortems**. Report the truth of an incident without bias or blame. Verify facts before publishing.
*   **Diplomacy (Protocol)**: **API Versioning**. Changes must be negotiated. Do not break treaties (contracts) without a transition period.

## X. Physical & Combative Arts
*Training and execution.*

*   **Martial Arts (Kata)**: **Code Katas**. Practice the basics (refactoring, TDD) until they are muscle memory.
*   **Yoga (Flexibility)**: **Configurability**. The system should be able to stretch to meet new requirements without breaking.

## XI. Life Skills & Practical Wisdom
*Navigating the day-to-day.*

*   **Personal Finance (Budgeting)**: **Performance Budgets**. Set strict limits on bundle size and latency. Do not spend more milliseconds than you can afford.
*   **Parenting (Development)**: **Process Management**. Spawning child processes requires supervision. Ensure they exit gracefully and don't become zombies.

## XII. Games & Strategic Thinking
*Competition and optimization.*

*   **Chess (Endgame)**: **Exit Strategy**. Plan for how your system will be decommissioned or migrated before you build it.
*   **Go (Shape)**: **Code Shape**. Recognize "good shape" (clean patterns) and "bad shape" (anti-patterns) intuitively.

## XIII. Specialized Philosophical Schools
*Frameworks for thought.*

*   **Pragmatism**: **YAGNI**. "You Ain't Gonna Need It." Truth is what works. Do not build for hypothetical futures.
*   **Existentialism**: **Ownership**. The code has no meaning but what you give it. You are responsible for your creation.
*   **Utilitarianism**: **Performance Optimization**. The greatest good (speed) for the greatest number (users).

## XIV. Environmental & Systems Thinking
*Holistic interconnection.*

*   **Permaculture (Zones)**: **Caching Strategies**. Keep frequently accessed data close (Zone 1: Memory), and less frequent data further away (Zone 5: Cold Storage).
*   **Sustainability (Circular Economy)**: **Resource Pooling**. Reuse connections and threads. Do not waste resources on setup/teardown.

## XV. Healing & Therapeutic Arts
*Restoration and care.*

*   **Psychotherapy (Alliance)**: **Blameless Culture**. Create a safe space for reporting errors. Psychological safety is a prerequisite for system safety.
*   **Physical Therapy (Rehab)**: **Technical Debt Repayment**. Consistent, small exercises (refactoring) prevent the need for major surgery (rewrites).
