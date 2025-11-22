# Ethical Engineering Manifesto: 20 Foundational Principles

**Version**: 1.2
**Classification**: Public
**License**: CC0 - Public Domain
**Last Updated**: 2025-11-22

---

## Quick Navigation

- **New to ethical engineering?** → Start with [Core Principles](#core-principles) and [The Five Objectives](#the-five-objectives-maqasid)
- **Building autonomous agents?** → See [Three-Layer Ethical Architecture](#three-layer-ethical-architecture-for-autonomous-agents) and [OODA Loop Integration](#ooda-loop-integration-classification-driven-decision-cycle)
- **Building an ethical framework?** → See [Implementation Checklists](#implementation-checklists) and [Maturity Model](#ethical-engineering-maturity-model)
- **Understanding the categorization?** → Review [Ethical Categorization System](#ethical-categorization-system)
- **Domain-specific guidance?** → See [Domain Applications](#domain-applications)
- **Executive summary** → Review [Summary Table](#summary-table)

---

## Scope & Applicability

**These principles apply to all software development** where ethical considerations, user trust, system integrity, and long-term sustainability are concerns.

**These principles are particularly critical for**:
- User-facing applications handling personal data
- Safety-critical systems affecting human welfare
- Long-lived production systems requiring multi-generational maintenance
- AI/ML systems making consequential decisions
- **Autonomous agents and agentic systems with decision-making authority**
- Systems subject to regulatory compliance (GDPR, HIPAA, accessibility laws)

**Metaprinciple**: *Software engineering is an ethical practice. Every technical decision carries moral weight.*

Code is not neutral. Systems shape behavior. Engineering choices affect real lives. This manifesto provides a framework for making those choices with integrity.

---

## The Five Objectives (Maqasid)

All engineering practices serve five fundamental objectives, **listed in order of priority** with weighted scores for autonomous decision-making:

1. **Hifz al-Din (System Integrity)** [Weight: 5×]: Protecting the fundamental "truth" and correctness of the system
2. **Hifz al-Nafs (Human Sustainability)** [Weight: 4×]: Protecting the wellbeing of users and developers
3. **Hifz al-Aql (Knowledge Capital)** [Weight: 3×]: Preserving and enhancing collective understanding
4. **Hifz al-Nasl (System Longevity)** [Weight: 2×]: Ensuring code survives and evolves across generations
5. **Hifz al-Mal (Resource Efficiency)** [Weight: 1×]: Using computational and human resources wisely

**Priority Principle**: When objectives conflict, higher-weighted objectives take precedence. A system that is technically perfect (Integrity) but harms users (Sustainability) fails. Code that is efficient (Resources) but unmaintainable (Knowledge/Longevity) fails.

### Weighted Scoring for Autonomous Systems

For autonomous agents making ethical decisions, calculate a weighted score:

```
Score = (Integrity × 5) + (Sustainability × 4) + (Knowledge × 3) +
        (Longevity × 2) + (Efficiency × 1)
```

Each objective can be scored from -2 (severe harm) to +2 (significant benefit):
- **+2**: Significant positive impact
- **+1**: Moderate positive impact
- **0**: Neutral impact
- **-1**: Moderate negative impact
- **-2**: Severe negative impact

**Example**: Adding comprehensive unit tests
- Integrity: +2 (ensures correctness) → 2 × 5 = 10
- Sustainability: +1 (developer confidence) → 1 × 4 = 4
- Knowledge: +1 (documents behavior) → 1 × 3 = 3
- Longevity: +1 (prevents regressions) → 1 × 2 = 2
- Efficiency: -1 (takes time to write) → -1 × 1 = -1
- **Total Score**: 10 + 4 + 3 + 2 - 1 = **18** (strongly recommended)

**Example**: Bypass SSL verification to fix timeout
- Integrity: -2 (violates security) → -2 × 5 = -10
- Sustainability: -1 (user data at risk) → -1 × 4 = -4
- Knowledge: 0 (neutral) → 0
- Longevity: -1 (technical debt) → -1 × 2 = -2
- Efficiency: +2 (fixes timeout quickly) → 2 × 1 = 2
- **Total Score**: -10 - 4 + 0 - 2 + 2 = **-14** (prohibited)

These objectives are interdependent yet hierarchical. This manifesto integrates all five while respecting their priority order.

---

## Ethical Categorization System

Engineering practices fall into five categories, from mandatory to prohibited:

### Fard (Critical Required) 🔴
**Mandatory practices that preserve fundamental integrity.**

Actions that are non-negotiable because they prevent direct harm to systems, users, or teams. Violating these is unethical and often illegal.

**Examples**: Encryption, input validation, accessibility, privacy compliance, CVE remediation

### Mandub (Strongly Recommended) 🟡
**Highly beneficial practices that improve quality and sustainability.**

Not strictly mandatory, but their absence creates technical debt, fragility, and long-term risk. Professional excellence requires these.

**Examples**: Comprehensive testing, CI/CD automation, documentation, code review, immutable infrastructure

### Mubah (Discretionary) 🟢
**Neutral practices where context determines appropriateness.**

Neither required nor discouraged. Use engineering judgment based on specific needs, constraints, and trade-offs.

**Examples**: Feature flags, A/B testing aesthetic choices, specific technology selections, architectural patterns

### Makruh (Anti-Pattern) 🟠
**Discouraged practices that introduce risk or technical debt.**

Not forbidden, but avoid unless there's strong justification. These practices degrade quality over time.

**Examples**: Manual deployments, configuration drift, god objects, premature optimization, clever code

### Haram (Prohibited) 🔴
**Unethical practices that cause direct harm.**

Actions that violate fundamental ethical principles. These must never be done, regardless of business pressure.

**Examples**: Hardcoded secrets, dark patterns, ignoring known vulnerabilities, selling user data without consent, addictive mechanics, developer burnout culture

---

## Three-Layer Ethical Architecture for Autonomous Agents

For autonomous systems with decision-making authority, this framework implements a **defense-in-depth** ethical architecture with three independent layers. Each layer provides a different lens for evaluating actions, creating emergent ethical behavior without requiring the agent to "understand" ethics.

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    PROPOSED ACTION                          │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────▼─────────────┐
        │   LAYER 1: SCOPE POLICY  │  ← Structural Safety
        │      (Al-Asl)            │    "Can this be done?"
        └────────────┬─────────────┘
                     │ Pass ✓
        ┌────────────▼──────────────┐
        │ LAYER 2: OBJECTIVES       │  ← Value Alignment
        │    ANALYSIS (Maqasid)     │    "Should this be done?"
        └────────────┬──────────────┘
                     │ Pass ✓
        ┌────────────▼──────────────┐
        │ LAYER 3: MEANS            │  ← Execution Strategy
        │  CLASSIFICATION (Ahkam)   │    "How urgently?"
        └────────────┬──────────────┘
                     │
              ┌──────▼──────┐
              │  EXECUTE    │
              └─────────────┘
```

### Layer 1: Scope Policy (Al-Asl) - The Gatekeeper

**Purpose**: Structural safety - what **CAN** be done

This layer implements two complementary principles from Islamic jurisprudence:

**1. Al-Asl fil-'Ibadat al-Tawqif** (Internal/Core Systems)
   - **Default**: DENY (whitelist only)
   - **Protects**: System invariants, core state, kernel integrity
   - **Rule**: "The default in core systems is prohibition"
   - **Rationale**: Critical infrastructure requires explicit authorization

**2. Al-Asl fil-Mu'amalat al-Ibahah** (External/User-Facing)
   - **Default**: ALLOW (blacklist only)
   - **Enables**: Innovation, flexibility, user value
   - **Rule**: "The default in usage is permission, except what is explicitly forbidden"
   - **Rationale**: Creativity requires freedom within safety boundaries

**Implementation**:

```elixir
# Whitelist for internal operations (critical/privileged)
@internal_whitelist [
  "rotate_encryption_keys",
  "update_firewall_rules",
  "modify_authentication_config",
  "adjust_rate_limits"
]

# Blacklist for external operations (harmful)
@external_blacklist [
  "leak_private_data",
  "bypass_ssl_verification",
  "disable_audit_logging",
  "implement_dark_patterns"
]

def check_scope(action, scope) do
  case scope do
    :internal ->
      if action in @internal_whitelist,
        do: {:ok, "Authorized internal operation"},
        else: {:reject, "Not in whitelist - violates system invariants"}

    :external ->
      if action in @external_blacklist,
        do: {:reject, "Forbidden - causes user harm"},
        else: {:ok, "Permitted within boundaries"}
  end
end
```

**Benefit**: Fast rejection (~O(1)) of structurally unsafe operations before expensive objective analysis.

---

### Layer 2: Objectives Analysis (Maqasid) - The Strategist

**Purpose**: Value alignment - what **SHOULD** be done

This layer calculates weighted impact across the Five Objectives (see above). Actions are evaluated for their effect on each objective.

**Weighted Scoring Formula**:
```
Score = (Integrity × 5) + (Sustainability × 4) + (Knowledge × 3) +
        (Longevity × 2) + (Efficiency × 1)
```

**Decision Thresholds**:
- **Score ≥ 10**: Strongly aligned (proceed to execution)
- **Score 0-9**: Weakly aligned (proceed with caution)
- **Score < 0**: Misaligned (reject)

**Conflict Resolution**: When objectives conflict, higher priority always wins:
- Integrity > Sustainability > Knowledge > Longevity > Efficiency

**Example Analysis**:

```elixir
def analyze_objectives(action_context) do
  weighted_score =
    (action_context.system_integrity * 5) +
    (action_context.human_sustainability * 4) +
    (action_context.knowledge_capital * 3) +
    (action_context.system_longevity * 2) +
    (action_context.resource_efficiency * 1)

  recommendation = cond do
    weighted_score >= 10 -> {:approve, "Strongly aligned with objectives"}
    weighted_score >= 0  -> {:approve_with_caution, "Weakly aligned"}
    weighted_score < 0   -> {:reject, "Misaligned with core objectives"}
  end

  %{
    weighted_score: weighted_score,
    recommendation: recommendation,
    conflicts: identify_conflicts(action_context)
  }
end
```

**Benefit**: Ensures decisions align with organizational values through mathematical enforcement.

---

### Layer 3: Means Classification (Ahkam) - The Tactician

**Purpose**: Execution strategy - **HOW** to do it

Actions that pass Layers 1 and 2 are classified by urgency and importance, determining execution strategy.

**Priority Levels**:

| Classification | Priority | Execution Strategy | Retry on Failure? |
|----------------|----------|-------------------|-------------------|
| **Critical Required (Fard)** | 100 | Blocking | Yes (3× retries) |
| **Strongly Recommended (Mandub)** | 70 | Best effort | Log failure only |
| **Discretionary (Mubah)** | 50 | Opportunistic | Skip if constrained |
| **Anti-Pattern (Makruh)** | 20 | Skip, warn | N/A |
| **Prohibited (Haram)** | 0 | Halt system | N/A |

**Classification Logic**:

```elixir
def classify_means(action) do
  severity = determine_severity(action)
  action_type = categorize_type(action)

  ruling = case {severity, action_type} do
    {:critical, :security_fix} -> :critical_required
    {:critical, :vulnerability} -> :critical_required
    {:high, :add_verification} -> :strongly_recommended
    {:high, :improve_reliability} -> :strongly_recommended
    {:medium, :refactoring} -> :discretionary
    {:low, :optimization} -> check_if_premature(action)
    _ -> :discretionary
  end

  %{
    ruling: ruling,
    priority: priority_score(ruling),
    execution_mode: execution_strategy(ruling)
  }
end
```

**Execution Priority Queue**:

1. **Critical Required** (Priority 100): Execute immediately, block on failure
2. **Strongly Recommended** (Priority 70): Execute in order, log failures
3. **Discretionary** (Priority 50): Execute if resources available
4. **Anti-Pattern** (Priority 20): Skip and log warning
5. **Prohibited** (Priority 0): Halt and alert

**Benefit**: Optimal resource allocation based on importance, graceful degradation under load.

---

### Emergent Properties

This three-layer architecture creates several emergent properties:

**1. Self-Correcting**
- Bad decisions automatically filtered at multiple layers
- No human needed for obvious ethical violations
- Escalates only ambiguous cases

**2. Predictable Autonomy**
- Agent acts independently within ethical boundaries
- Constrained by mathematical framework
- Behavior is auditable and explainable

**3. Graceful Degradation**
- Critical tasks always execute (Priority 100)
- Non-critical tasks skip under resource constraints
- System never sacrifices integrity for speed

**4. Defense in Depth**
- Even if scope check passes, objectives can reject
- Even if objectives approve, means determines urgency
- Multiple opportunities to catch harmful decisions

**5. Mathematically Enforced Ethics**
- Unethical decisions are "type errors" rejected by the system
- No need for the agent to "understand" morality
- The framework enforces it through weighted scoring

**Example: Complete Decision Flow**

```
Task: "Bypass SSL verification to fix timeout"

Layer 1 (Scope):
  - Scope: :internal (core networking)
  - Action: "bypass_ssl_verification"
  - Whitelist check: NOT FOUND
  - Result: ❌ BLOCKED
  - Reason: "Not in whitelist - violates security invariants"

→ Rejected before objectives analysis (fast path)
```

```
Task: "Add comprehensive unit tests"

Layer 1 (Scope):
  - Scope: :external (development practice)
  - Action: "add_unit_tests"
  - Blacklist check: NOT FOUND
  - Result: ✅ PASS → Continue to Layer 2

Layer 2 (Objectives):
  - Integrity: +2 (ensures correctness) → 10
  - Sustainability: +1 (confidence) → 4
  - Knowledge: +1 (documents behavior) → 3
  - Longevity: +1 (prevents regressions) → 2
  - Efficiency: -1 (takes time) → -1
  - Weighted Score: 18
  - Result: ✅ APPROVE → Continue to Layer 3

Layer 3 (Means):
  - Keywords: "test", "unit", "comprehensive"
  - Type: :add_verification
  - Severity: :high
  - Classification: STRONGLY_RECOMMENDED
  - Priority: 70
  - Execution: :best_effort
  - Result: ✅ Execute in priority queue

→ Executed after critical tasks, before discretionary tasks
```

---

### OODA Loop Integration: Classification-Driven Decision Cycle

For practical implementation, the three-layer architecture integrates with the **OODA (Observe-Orient-Decide-Act) Loop**, creating a classification-driven decision engine.

**OODA Loop Overview**:
1. **Observe**: Collect raw input (code change, system event, user request)
2. **Orient**: Classify using the Five-Fold Matrix (Fard/Mandub/Mubah/Makruh/Haram)
3. **Decide**: Select execution strategy based on classification
4. **Act**: Execute with appropriate priority and retry logic

#### Implementation: Classification-Driven OODA Engine

```elixir
defmodule OODALoop.DecisionEngine do
  @moduledoc """
  Implements the OODA loop where the 'Decide' phase is governed
  by the Five-Fold Classification Matrix.
  """

  alias VerificationSystem.DecisionMatrix

  def run_cycle(agent_state, observation) do
    # 1. OBSERVE: Raw input
    raw_data = observation

    # 2. ORIENT: Classify the observation using ethical matrix
    classification = classify(raw_data)

    # 3. DECIDE: Select strategy based on classification
    strategy = DecisionMatrix.config().execution_strategy[classification.category]

    # 4. ACT: Execute based on priority
    execute_action(agent_state, classification, strategy)
  end

  defp classify(data) do
    indicators = DecisionMatrix.config().indicators

    cond do
      matches?(data, indicators.prohibited) ->
        %{
          category: :prohibited,
          rationale: "Safety Violation",
          action: :halt
        }

      matches?(data, indicators.critical_required) ->
        %{
          category: :critical_required,
          rationale: "Correctness Blocker",
          action: :fix_immediately
        }

      matches?(data, indicators.anti_pattern) ->
        %{
          category: :anti_pattern,
          rationale: "Counter-productive",
          action: :skip
        }

      matches?(data, indicators.strongly_recommended) ->
        %{
          category: :strongly_recommended,
          rationale: "Quality Improvement",
          action: :schedule
        }

      true ->
        %{
          category: :discretionary,
          rationale: "Optional",
          action: :evaluate_resources
        }
    end
  end

  defp execute_action(state, classification, strategy) do
    case strategy.execution do
      :halt ->
        {:error, :halted, "PROHIBITED: #{classification.rationale}"}

      :blocking ->
        # Must succeed or loop retries
        {:ok, perform_critical_fix(state, classification)}

      :best_effort ->
        # Try once, proceed if fails
        perform_enhancement(state, classification)
        {:ok, state}

      :skip ->
        Logger.warning("Skipping Anti-Pattern: #{classification.rationale}")
        {:ok, state}

      :opportunistic ->
        if state.resources > 0.5 do
          perform_tweak(state, classification)
        end
        {:ok, state}
    end
  end
end
```

#### Agent-Specific Classification Rules

Different agent types apply the Five-Fold Classification to their specific domains:

**Layer 0: Architecture Agent**

| Category | Classification | Observation Example | Action |
|---|---|---|---|
| **Prohibited (Haram)** | Unsafe Topology | "Design requires circular synchronous calls between nodes" | HALT. Redesign required. |
| **Critical (Fard)** | Invariant Violation | "Latency bound O(N) violated by proposed O(N²) flow" | Block. Refine specification. |
| **Recommended (Mandub)** | Resilience | "System should survive simultaneous failure of 2 nodes" | Add redundancy to spec. |
| **Anti-Pattern (Makruh)** | Over-Abstraction | "Abstracting message passing into generic 'EventBus'" | Skip. YAGNI principle. |
| **Discretionary (Mubah)** | Naming | "Rename 'Node' to 'ServerPeer' for clarity" | Rename if time permits. |

**Layer 1a: Specification Agent (TLA+)**

| Category | Classification | Observation Example | Action |
|---|---|---|---|
| **Prohibited (Haram)** | Undefined Behavior | "Spec relies on uninitialized variable state" | HALT. Fix Init predicate. |
| **Critical (Fard)** | Model Failure | "TLC found a deadlock state" | Block. Fix Next state relation. |
| **Recommended (Mandub)** | Refinement | "Add invariant to check message queue bounds" | Add to .tla file. |
| **Anti-Pattern (Makruh)** | Speculative Generality | "Modeling features not yet in requirements" | Skip. Remove extra variables. |
| **Discretionary (Mubah)** | Formatting | "Align TLA+ conjunction lists" | Format document. |

**Layer 1b: Implementation Agent (Elixir)**

| Category | Classification | Observation Example | Action |
|---|---|---|---|
| **Prohibited (Haram)** | Safety Bypass | "Using Process.exit(pid, :kill) without trapping exits" | HALT. Use proper supervision. |
| **Critical (Fard)** | Type Error | "Dialyzer: Function has no local return" | Block. Fix success typing. |
| **Recommended (Mandub)** | Telemetry | "Missing :telemetry.span on public API" | Inject telemetry hooks. |
| **Anti-Pattern (Makruh)** | Premature Optimization | "Replacing Enum.map with manual recursion for speed" | Skip. Use standard lib. |
| **Discretionary (Mubah)** | Refactoring | "Extract helper function for clarity" | Refactor if time permits. |

**Layer 1c: Test Agent**

| Category | Classification | Observation Example | Action |
|---|---|---|---|
| **Prohibited (Haram)** | False Confidence | "Test mocks the module under test (self-mocking)" | HALT. Rewrite test. |
| **Critical (Fard)** | Property Failure | "Property failed: shrunk to [0, -1]" | Block. Report bug to Implementation Agent. |
| **Recommended (Mandub)** | Test Adequacy | "Mutation score 85% (target 90%)" | Generate 5 more properties. |
| **Anti-Pattern (Makruh)** | Fragile Test | "Test relies on Process.sleep(100)" | Skip. Use assert_receive instead. |
| **Discretionary (Mubah)** | Documentation | "Add @moduledoc to test file" | Add docs if time permits. |

**Layer 2: Proof Agent**

| Category | Classification | Observation Example | Action |
|---|---|---|---|
| **Prohibited (Haram)** | Unsound Proof | "Coq proof uses Admitted on critical theorem" | HALT. Proof must be Qed. |
| **Critical (Fard)** | Race Condition | "Concuerror found trace causing crash" | Block. Escalate to Architect. |
| **Recommended (Mandub)** | Linearizability | "Check if history is linearizable" | Run Knossos check. |
| **Anti-Pattern (Makruh)** | Deep Proof | "Proving correctness of standard library Map.put" | Skip. Trust the BEAM VM. |
| **Discretionary (Mubah)** | Cleanup | "Remove unused intermediate lemmas" | Delete dead code. |

#### Convergence Criteria: System Verification Complete

The system reaches convergence (verification complete) when agents achieve equilibrium based on the classification matrix:

```elixir
defmodule ConvergenceCheck do
  @moduledoc """
  Determines if the multi-agent system has converged to a stable,
  verified state based on the Five-Fold Classification.
  """

  def check_status(agent_reports) do
    # Aggregate counts across all agents
    counts = aggregate_classifications(agent_reports)

    cond do
      # 1. PROHIBITED DETECTED: Immediate Failure
      counts.prohibited > 0 ->
        {:error, :unsafe,
         "System contains #{counts.prohibited} PROHIBITED violations"}

      # 2. CRITICAL PENDING: Verification Incomplete
      counts.critical_required > 0 ->
        {:pending,
         "Blocking on #{counts.critical_required} CRITICAL tasks"}

      # 3. RECOMMENDED PENDING: Acceptable but not Ideal
      counts.strongly_recommended > 0 ->
        {:ok, :acceptable,
         "System valid. #{counts.strongly_recommended} improvements suggested"}

      # 4. IDEAL STATE: All Required and Recommended Done
      true ->
        {:ok, :perfect,
         "System converged. All critical and recommended actions complete"}
    end
  end

  defp aggregate_classifications(agent_reports) do
    Enum.reduce(agent_reports,
      %{prohibited: 0, critical_required: 0, strongly_recommended: 0,
        anti_pattern: 0, discretionary: 0},
      fn report, acc ->
        Map.update!(acc, report.classification, &(&1 + 1))
      end
    )
  end
end
```

#### Benefits of OODA Integration

**1. Prevents Over-Engineering**
- Agents stop wasting cycles on anti-patterns (Makruh)
- LLM prevented from spiraling into unnecessary abstractions
- Focus maintained on critical and recommended tasks

**2. Absolute Safety**
- Prohibited (Haram) actions trigger immediate HALT
- No hallucinated "quick fixes" that bypass safety
- System cannot proceed with unresolved safety violations

**3. Automatic Prioritization**
- Critical (Fard) fixes always execute before discretionary (Mubah) tweaks
- Resource allocation follows ethical priorities
- Type errors and race conditions addressed before code cleanup

**4. Graceful Convergence**
- Clear exit criteria based on classification counts
- System knows when verification is "good enough" vs. "perfect"
- Acceptable states defined (e.g., critical done, recommended pending)

**5. Auditable Decision Trail**
- Every OODA cycle produces classification rationale
- Complete trace: Observe → Orient (classify) → Decide (strategy) → Act (execute)
- Explainable AI through ethical categorization

#### Example: Complete OODA Cycle

```
OBSERVATION: Agent detects "Using String.to_atom/1 on user input"

ORIENT (Classify):
  - Matches: indicators.prohibited (arbitrary atom creation)
  - Category: :prohibited
  - Rationale: "Atom table exhaustion attack vector"
  - Action: :halt

DECIDE:
  - Strategy: execution_strategy[:prohibited]
  - Execution: :halt
  - Retry: false

ACT:
  - Result: {:error, :halted, "PROHIBITED: Atom table exhaustion attack"}
  - Next: Escalate to human review
  - System: Blocks all downstream agents until fixed

→ Agent cannot proceed. Human intervention required.
```

```
OBSERVATION: Agent detects "Dialyzer reports no_return warning"

ORIENT (Classify):
  - Matches: indicators.critical_required (type system violation)
  - Category: :critical_required
  - Rationale: "Type correctness blocker"
  - Action: :fix_immediately

DECIDE:
  - Strategy: execution_strategy[:critical_required]
  - Execution: :blocking
  - Retry: 3 attempts

ACT:
  - Attempt 1: Fix type specification
  - Attempt 2: Dialyzer re-run → Success
  - Result: {:ok, state_with_fixed_types}
  - Next: Continue to next OODA cycle

→ Critical issue resolved. Agent proceeds to next observation.
```

---

## Core Principles

### Domain 1: Security & Reliability Engineering

**Objective**: System Integrity (Hifz al-Din) & Resource Efficiency (Hifz al-Mal)

This domain protects the fundamental "truth" of the system.

#### I. Encryption as Foundation (Fard 🔴)
**Data at rest and in transit must be encrypted.**

Unencrypted data violates user trust (Amanah). Every communication channel, every storage system must protect confidentiality and integrity.

**Implementation**:
- TLS 1.3 for all network traffic
- AES-256 for data at rest
- Key management via HSM or cloud KMS
- Certificate rotation automated
- Perfect forward secrecy enabled

**Tools**: Let's Encrypt, AWS KMS, HashiCorp Vault, TLS 1.3

**Trade-off**: Minimal performance impact vs. catastrophic breach risk. Always encrypt.

**Anti-pattern** (Haram 🔴): Transmitting credentials or PII over HTTP, storing passwords in plaintext, committing encryption keys to version control.

---

#### II. Access Control as Default (Fard 🔴)
**Implement role-based access control (RBAC) to prevent unauthorized state mutation.**

Default deny. Explicit allow. Principle of least privilege. Every action requires authentication and authorization.

**Implementation**:
- RBAC or ABAC enforced at application layer
- JWT or OAuth2 for stateless authentication
- Permission checks before every state-changing operation
- Audit logs for all access attempts
- Regular access reviews (quarterly minimum)

**Example**:
```python
# Anti-pattern: No authorization check
def delete_user(user_id):
    User.delete(user_id)

# Ethical: Explicit permission check
def delete_user(user_id, actor):
    if not actor.has_permission('user:delete'):
        raise PermissionDenied
    audit_log.record(actor, 'delete_user', user_id)
    User.delete(user_id)
```

**Trade-off**: Development complexity vs. security. Non-negotiable for multi-user systems.

---

#### III. Input Validation as Defense (Fard 🔴)
**Sanitize all inputs to prevent injection attacks.**

Never trust user input. Validate type, format, range. Encode outputs. Parameterize queries. Prevent corruption of truth.

**Implementation**:
- Whitelist validation (allow known-good, not block known-bad)
- Parameterized SQL queries or ORM
- Content Security Policy (CSP) headers
- Input length limits
- Type validation at API boundaries

**Tools**: OWASP ESAPI, DOMPurify, SQL prepared statements

**Anti-pattern** (Haram 🔴): String concatenation in SQL, `eval()` on user input, innerHTML without sanitization, disabled CSP.

---

#### IV. Vulnerability Remediation (Fard 🔴)
**Critical CVEs must be patched within SLA.**

Knowingly shipping vulnerable code is negligent. Monitor dependencies. Automate scanning. Remediate promptly.

**Implementation**:
- Dependency scanning in CI/CD (Dependabot, Snyk)
- CVE monitoring with severity classification
- SLA: Critical (24h), High (7d), Medium (30d)
- Automated security updates where safe
- Incident response plan for zero-days

**Trade-off**: Update churn vs. exploitation risk. Security wins.

**Anti-pattern** (Haram 🔴): Ignoring CVE notifications, deferring critical patches indefinitely, disabling security scanners.

---

### Domain 2: DevOps & Infrastructure

**Objective**: System Longevity (Hifz al-Nasl)

This domain ensures code survives and evolves across generations.

#### V. Immutable Infrastructure (Mandub 🟡)
**Replace servers rather than patching them.**

Mutable servers drift. Immutable infrastructure ensures consistency—a form of integrity. Infrastructure as code. Cattle, not pets.

**Implementation**:
- Containerization (Docker, Kubernetes)
- Infrastructure as Code (Terraform, Pulumi)
- Golden images built in CI/CD
- No SSH access to production servers
- Blue-green or canary deployments

**Trade-off**: Initial complexity vs. long-term reproducibility. Highly recommended for cloud-native systems.

**Anti-pattern** (Makruh 🟠): Manual server configuration, "snowflake" servers, in-place patching without version control.

---

#### VI. Comprehensive CI/CD (Mandub 🟡)
**Automate the deployment ritual to remove human error.**

Manual deployments create variance. Automation creates consistency. Every commit flows through the same pipeline.

**Implementation**:
- Automated testing at every stage (unit, integration, E2E)
- Automated security scanning (SAST, DAST, SCA)
- Automated deployment to staging
- Gated production deployment (approval + smoke tests)
- Rollback automation

**Tools**: GitHub Actions, GitLab CI, Jenkins, CircleCI, ArgoCD

**Trade-off**: Setup time vs. deployment reliability. Essential for teams >3 engineers.

**Anti-pattern** (Makruh 🟠): Manual deployments, "works on my machine" syndrome, skipping tests to ship faster.

---

#### VII. Disaster Recovery Readiness (Mandub 🟡)
**Practice for failure to ensure system survival.**

Backups without testing are hope, not strategy. Run fire drills. Document runbooks. Ensure the system can recover.

**Implementation**:
- Automated backups (3-2-1 rule: 3 copies, 2 media, 1 offsite)
- Quarterly disaster recovery drills
- RTO/RPO defined and tested
- Incident response playbooks
- Chaos engineering (Chaos Monkey)

**Trade-off**: Time investment vs. business continuity. Critical for production systems.

---

### Domain 3: Product Management & UX

**Objective**: Human Sustainability (Hifz al-Nafs)

This domain protects the wellbeing of users and developers.

#### VIII. Accessibility as Requirement (Fard 🔴)
**Systems must be usable by people with disabilities.**

Excluding disabled users causes harm. WCAG AA compliance is not optional—it's a moral and legal obligation.

**Implementation**:
- Semantic HTML with ARIA labels
- Keyboard navigation for all interactive elements
- Screen reader compatibility testing
- Sufficient color contrast (4.5:1 minimum)
- Captions for video, transcripts for audio
- Automated testing (axe, Pa11y, Lighthouse)

**Tools**: axe DevTools, WAVE, NVDA, JAWS, VoiceOver

**Trade-off**: None. Accessibility benefits all users and is legally required.

**Anti-pattern** (Haram 🔴): Skipping accessibility, keyboard traps, removing focus outlines, inaccessible forms.

---

#### IX. Privacy Compliance (Fard 🔴)
**Protect the user's "digital self."**

Privacy is a human right. GDPR, CCPA, and similar laws codify this. Collect minimum data. Honor user choices. Be transparent.

**Implementation**:
- Data minimization (collect only what's necessary)
- Explicit consent for data collection
- Right to access, rectify, delete (GDPR Articles 15-17)
- Privacy policy in plain language
- Data retention policies with automated deletion
- Privacy-by-design in architecture

**Tools**: OneTrust, TrustArc, Osano

**Trade-off**: None. Privacy violations carry massive fines and reputational damage.

**Anti-pattern** (Haram 🔴): Selling user data without consent, dark patterns in consent flows, retaining data indefinitely, unclear privacy policies.

---

#### X. Ethical Design (Fard 🔴)
**Reject addictive mechanics and dark patterns.**

Algorithms designed to manipulate users violate human sustainability. Respect user agency. Don't exploit psychological vulnerabilities.

**Examples of Haram**:
- Infinite scroll designed to maximize engagement time
- Notifications engineered to trigger FOMO
- Hidden unsubscribe buttons
- Manipulative countdown timers
- Fake scarcity indicators

**Ethical alternatives**:
- Finite content boundaries
- User-controlled notification preferences
- Clear, prominent unsubscribe
- Honest availability information

**Trade-off**: Short-term engagement vs. long-term trust. Ethics wins.

---

#### XI. Developer Sustainability (Fard 🔴)
**Protect team wellbeing. Reject crunch culture.**

Burnout harms people. Harming your team violates Hifz al-Nafs. Sustainable pace produces better work than hero culture.

**Implementation**:
- No mandatory overtime without compensation
- Realistic sprint planning with slack time
- On-call rotation with fair compensation
- Vacation policies enforced (not just offered)
- Mental health support resources
- Blameless postmortems

**Trade-off**: None. Burned-out engineers produce low-quality code and quit.

**Anti-pattern** (Haram 🔴): Death marches, glorifying overwork, penalizing work-life balance, toxic on-call without support.

---

### Domain 4: Software Architecture

**Objective**: Knowledge Capital (Hifz al-Aql) & Resource Efficiency

Architecture protects the "intellect" of the system.

#### XII. Domain-Driven Design (Mandub 🟡)
**Align code with real-world business language.**

When code mirrors domain concepts, meaning is preserved. Ubiquitous language bridges business and engineering.

**Implementation**:
- Bounded contexts for complex domains
- Entities, Value Objects, Aggregates from DDD
- Code reviews with domain experts
- Glossary of domain terms
- Event storming for complex workflows

**Trade-off**: Upfront modeling time vs. long-term clarity. Excellent for complex business logic.

**Anti-pattern** (Makruh 🟠): Generic CRUD operations obscuring business rules, technical jargon instead of domain language.

---

#### XIII. Documentation as Code (Mandub 🟡)
**Record architectural decisions. Preserve institutional knowledge.**

Without documentation, the "intellect" of the team dies when senior engineers leave. ADRs capture the "why."

**Implementation**:
- Architecture Decision Records (ADRs) in version control
- README for every module
- API documentation (OpenAPI, GraphQL schema)
- Onboarding guides
- Runbooks for operational tasks

**Tools**: arc42, Docusaurus, Mermaid diagrams, PlantUML

**Trade-off**: Writing time vs. knowledge transfer. Essential for teams >5 or long-lived systems.

**Anti-pattern** (Makruh 🟠): Tribal knowledge only, outdated documentation, "the code is the documentation."

---

#### XIV. Appropriate Abstraction (Mandub 🟡)
**Avoid premature optimization and over-engineering.**

Premature microservices add cognitive load without benefit. God objects make code impossible to reason about. Right-size abstractions.

**Guidelines**:
- Monolith first, microservices when proven necessary
- Rule of Three: abstract after third duplication
- YAGNI: You Aren't Gonna Need It
- Measure before optimizing

**Anti-pattern** (Makruh 🟠):
- Premature microservices for small systems
- God objects with 50+ methods
- Over-engineered frameworks for simple problems
- Optimizing unproven bottlenecks

---

### Domain 5: Data Science & AI

**Objective**: System Integrity (Truth) & Human Sustainability

#### XV. Bias Audits (Fard 🔴)
**Ensure models don't discriminate.**

Biased models violate justice (Adl). Test for disparate impact. Use representative datasets. Monitor for drift.

**Implementation**:
- Diverse, representative training data
- Fairness metrics (demographic parity, equalized odds)
- Regular bias audits across protected classes
- Human review for high-stakes decisions
- Model cards documenting limitations

**Tools**: Fairlearn, AI Fairness 360, What-If Tool

**Trade-off**: None. Discriminatory AI is unethical and often illegal.

**Anti-pattern** (Haram 🔴): Training on biased datasets without mitigation, ignoring disparate impact, deploying without bias testing.

---

#### XVI. Explainability (Fard 🔴)
**Users must know why a decision was made.**

Black-box decisions violate Hifz al-Aql. Provide explanations. Enable appeals. Maintain human oversight for consequential decisions.

**Implementation**:
- Model interpretability techniques (SHAP, LIME)
- Model cards with use cases and limitations
- Human-in-the-loop for high-stakes decisions
- Right to explanation (GDPR Article 22)
- Audit trails for model decisions

**Trade-off**: Model complexity vs. transparency. Regulated domains require explainability by law.

**Anti-pattern** (Haram 🔴): Black-box sentencing (hiring, loans, bail) without human oversight, unexplainable deep learning for critical decisions.

---

#### XVII. Human Oversight (Fard 🔴)
**AI must not make life-altering decisions alone.**

Automated hiring, loan approval, or bail decisions without human review are unethical. AI assists; humans decide.

**Implementation**:
- Human-in-the-loop for consequential decisions
- Override mechanisms for incorrect predictions
- Regular human audits of automated decisions
- Escalation paths for edge cases
- Clear accountability for AI-assisted decisions

**Trade-off**: None. Removing human judgment from high-stakes decisions is negligent.

---

### Domain 6: Testing & Quality Assurance

**Objective**: System Longevity (Hifz al-Nasl) & System Integrity (Hifz al-Din)

#### XVIII. Comprehensive Testing (Mandub 🟡)
**Test at multiple levels to protect against regressions.**

Tests are a form of documentation and insurance. They preserve correctness over time as the system evolves.

**Implementation**:
- Unit tests for business logic (>80% coverage)
- Integration tests for component interactions
- End-to-end tests for critical user flows
- Property-based testing for edge cases
- Mutation testing to validate test quality

**Trade-off**: Test writing time vs. confidence in changes. Essential for production systems.

---

#### XIX. Continuous Monitoring (Mandub 🟡)
**Observe system behavior in production.**

Tests prove code works in isolation. Monitoring proves it works in reality. Instrument everything. Alert on anomalies.

**Implementation**:
- Metrics: RED (Rate, Errors, Duration) or USE (Utilization, Saturation, Errors)
- Logs: structured logging with correlation IDs
- Traces: distributed tracing for microservices
- Alerts: actionable, low false-positive rate
- Dashboards: business and technical metrics

**Tools**: Prometheus, Grafana, ELK Stack, Datadog, Honeycomb, OpenTelemetry

---

### Domain 7: Code Quality & Maintainability

**Objective**: Knowledge Capital (Hifz al-Aql)

#### XX. Readability as Priority (Mandub 🟡)
**Code is read 10× more than written.**

Optimize for human comprehension. Clear names. Obvious structure. Boring over clever. Future maintainers will thank you.

**Implementation**:
- Meaningful variable and function names
- Max function length: ~25 lines
- Max nesting depth: 3 levels
- Code reviews focused on clarity
- Automated formatting (Black, Prettier, rustfmt)

**Trade-off**: None. Readable code is maintainable code.

**Anti-pattern** (Makruh 🟠): Clever one-liners, cryptic abbreviations, deeply nested conditionals, god functions.

---

## Implementation Checklists

### Security & Reliability (Domain 1)

**Fard (Critical Required)**:
- [ ] TLS 1.3 for all network traffic
- [ ] AES-256 encryption for data at rest
- [ ] RBAC or ABAC enforced at application layer
- [ ] Input validation on all user inputs
- [ ] Parameterized SQL queries or ORM
- [ ] CVE scanning in CI/CD pipeline
- [ ] Critical CVEs patched within 24 hours

**Mandub (Strongly Recommended)**:
- [ ] Security headers (CSP, HSTS, X-Frame-Options)
- [ ] Dependency scanning (Dependabot, Snyk)
- [ ] Secret management (Vault, AWS Secrets Manager)
- [ ] Security audit logs
- [ ] Penetration testing (annual)

**Haram (Prohibited)**:
- [ ] Verify no hardcoded secrets in repository
- [ ] Verify no plaintext passwords
- [ ] Verify no HTTP for sensitive data

---

### DevOps & Infrastructure (Domain 2)

**Mandub (Strongly Recommended)**:
- [ ] Infrastructure as Code (Terraform, Pulumi)
- [ ] Containerization (Docker)
- [ ] CI/CD pipeline with automated tests
- [ ] Automated deployments to staging
- [ ] Backup automation with 3-2-1 rule
- [ ] Disaster recovery plan documented
- [ ] DR drill conducted (quarterly)

**Makruh (Anti-Pattern to Avoid)**:
- [ ] Eliminate manual server configuration
- [ ] Eliminate SSH access to production
- [ ] Eliminate in-place patching

---

### Product & UX (Domain 3)

**Fard (Critical Required)**:
- [ ] WCAG 2.1 AA compliance
- [ ] Keyboard navigation for all interactions
- [ ] Screen reader testing
- [ ] GDPR compliance (if EU users)
- [ ] Privacy policy in plain language
- [ ] Data deletion workflow implemented
- [ ] No dark patterns in UI
- [ ] No addictive mechanics

**Makruh (Discretionary)**:
- [ ] Feature flags for gradual rollout
- [ ] A/B testing framework

---

### Architecture (Domain 4)

**Mandub (Strongly Recommended)**:
- [ ] Architecture Decision Records (ADRs)
- [ ] README for each module
- [ ] API documentation (OpenAPI)
- [ ] Domain-driven design for complex logic
- [ ] Onboarding documentation

**Makruh (Anti-Pattern to Avoid)**:
- [ ] Avoid premature microservices
- [ ] Refactor god objects (>500 LOC or >20 methods)
- [ ] Avoid premature optimization

---

### AI/ML (Domain 5)

**Fard (Critical Required - if deploying AI)**:
- [ ] Bias audit across protected classes
- [ ] Model card documenting limitations
- [ ] Explainability for consequential decisions
- [ ] Human oversight for high-stakes decisions
- [ ] Right to appeal automated decisions

**Haram (Prohibited)**:
- [ ] No automated hiring without human review
- [ ] No loan decisions without human oversight
- [ ] No bail/sentencing without explainability

---

## Ethical Engineering Maturity Model

### Level 0: Unaware
- No ethical framework
- Security as afterthought
- No accessibility considerations
- Documentation absent

### Level 1: Reactive
- Fixes security issues when discovered
- Basic input validation
- Some documentation
- Accessibility not prioritized

### Level 2: Proactive (Foundation)
- **Security**: Encryption, RBAC, input validation standard
- **Infrastructure**: CI/CD pipeline, automated deployments
- **UX**: Basic accessibility (keyboard nav, semantic HTML)
- **Privacy**: GDPR compliance for EU users
- **Code Quality**: Code reviews, basic testing

### Level 3: Managed (Professional)
- **Security**: CVE monitoring, dependency scanning, security audits
- **Infrastructure**: Immutable infrastructure, disaster recovery tested
- **UX**: WCAG AA compliance, screen reader testing
- **Privacy**: Privacy-by-design, data minimization
- **Architecture**: ADRs, DDD for complex domains
- **Team**: Sustainable pace, no crunch culture

### Level 4: Measured (Excellence)
- **Security**: Zero trust architecture, supply chain security
- **Infrastructure**: Chaos engineering, multi-region DR
- **UX**: Inclusive design, user testing with disabled users
- **AI**: Bias audits, explainability, human oversight
- **Code**: High test coverage, continuous monitoring
- **Team**: Psychological safety, blameless postmortems

### Level 5: Optimized (Industry Leading)
- Security: Formal verification for critical paths
- UX: WCAG AAA compliance
- AI: Fairness as core product metric
- Team: Open source contributions to ethical tooling
- Organization: Published ethical guidelines, industry advocacy

---

## Domain Applications

### Web Application Checklist

**Critical (Fard)**:
- Encryption (HTTPS/TLS)
- Authentication & authorization (RBAC)
- Input validation & output encoding
- WCAG AA accessibility
- GDPR privacy compliance
- CVE remediation

**Recommended (Mandub)**:
- CI/CD pipeline
- Comprehensive testing (unit, integration, E2E)
- Monitoring & alerting
- Documentation (API, onboarding)

---

### Mobile Application Checklist

**Critical (Fard)**:
- Secure data storage (encrypted)
- Certificate pinning for API calls
- Accessibility (screen reader, dynamic type)
- Privacy: minimal permissions, clear consent
- No dark patterns

**Recommended (Mandub)**:
- Crash reporting & analytics
- Automated testing
- Release automation

---

### API/Backend Service Checklist

**Critical (Fard)**:
- Authentication (JWT, OAuth2)
- Rate limiting
- Input validation
- Encryption in transit
- Audit logging

**Recommended (Mandub)**:
- OpenAPI documentation
- Comprehensive tests
- Circuit breakers for resilience
- Observability (metrics, logs, traces)

---

### Data Pipeline Checklist

**Critical (Fard)**:
- PII encryption
- Access controls for data stores
- Data retention policies

**Recommended (Mandub)**:
- Idempotent pipelines
- Data quality tests
- Lineage tracking
- Observability

---

## Summary Table

| Domain | If the action is... | It is mapped to... | Because it preserves... |
|---|---|---|---|
| Security | Encrypting data | Critical (Fard) | System Integrity + Trust |
| Security | Fixing a CVE | Critical (Fard) | System Integrity |
| Security | Hardcoding secrets | Prohibited (Haram) | System Integrity |
| DevOps | Immutable infrastructure | Recommended (Mandub) | System Longevity |
| DevOps | Manual deployments | Anti-Pattern (Makruh) | System Longevity |
| Testing | Writing unit tests | Recommended (Mandub) | System Longevity |
| Frontend | Accessibility fix | Critical (Fard) | Human Sustainability |
| Frontend | Dark patterns | Prohibited (Haram) | Human Sustainability |
| Frontend | Pixel pushing | Discretionary (Mubah) | Resource Efficiency |
| UX | Privacy compliance | Critical (Fard) | Human Sustainability |
| UX | Addictive mechanics | Prohibited (Haram) | Human Sustainability |
| Backend | Refactoring | Recommended (Mandub) | Knowledge Capital |
| Architecture | Documentation (ADRs) | Recommended (Mandub) | Knowledge Capital |
| Architecture | God objects | Anti-Pattern (Makruh) | Knowledge Capital |
| Data/AI | Bias audits | Critical (Fard) | Justice + Human Sustainability |
| Data/AI | Explainability | Critical (Fard) | Knowledge Capital + Trust |
| Data/AI | Black-box sentencing | Prohibited (Haram) | Human Sustainability |
| Data | Selling user data | Prohibited (Haram) | Human Sustainability |
| Process | Sustainable pace | Critical (Fard) | Human Sustainability |
| Process | Crunch / Burnout culture | Prohibited (Haram) | Human Sustainability |

---

## Tools & Ecosystem

### Security
- **Encryption**: Let's Encrypt, AWS KMS, HashiCorp Vault
- **Scanning**: Snyk, Dependabot, GitHub Advanced Security, SonarQube
- **Monitoring**: Datadog Security, Wiz, Lacework

### Infrastructure
- **IaC**: Terraform, Pulumi, AWS CDK
- **CI/CD**: GitHub Actions, GitLab CI, CircleCI, ArgoCD
- **Containers**: Docker, Kubernetes, ECS

### Accessibility
- **Testing**: axe DevTools, WAVE, Pa11y, Lighthouse
- **Screen Readers**: NVDA, JAWS, VoiceOver, TalkBack

### Privacy
- **Compliance**: OneTrust, TrustArc, Osano
- **Data Management**: BigID, Collibra

### AI Ethics
- **Bias Detection**: Fairlearn, AI Fairness 360, What-If Tool
- **Explainability**: SHAP, LIME, InterpretML

### Documentation
- **ADRs**: adr-tools, log4brains
- **API Docs**: Swagger/OpenAPI, Redoc, Postman
- **Diagrams**: Mermaid, PlantUML, draw.io

---

## Metrics & Measurement

### Security Metrics
- CVE remediation time (target: Critical <24h, High <7d)
- % dependencies with known vulnerabilities
- Security audit findings (trend down)
- Incident response time (MTTD, MTTR)

### Accessibility Metrics
- Automated test pass rate (target: 100%)
- WCAG audit score
- Screen reader task completion rate
- Accessibility bug backlog (trend down)

### DevOps Metrics
- Deployment frequency (higher is better)
- Lead time for changes (lower is better)
- Change failure rate (lower is better)
- Time to restore service (lower is better)

### Code Quality Metrics
- Test coverage (target: >80% for critical paths)
- Code review approval time
- Documentation coverage
- Technical debt ratio (trend down)

### Team Health Metrics
- Developer satisfaction (survey quarterly)
- On-call burden (hours per person per month)
- Turnover rate (trend down)
- Psychological safety score

---

## Trade-Offs & Anti-Patterns

### When Ethical Principles Conflict

**Scenario**: Performance optimization vs. explainability in AI
- **Resolution**: For non-consequential decisions (recommendations), optimize. For high-stakes decisions (loans, hiring), explainability wins.

**Scenario**: Accessibility vs. fast iteration
- **Resolution**: Core WCAG A/AA is Fard (non-negotiable). AAA features can follow in increments.

**Scenario**: Security vs. usability
- **Resolution**: Find the balance. MFA is Fard. 60-character minimum passwords are Makruh (anti-pattern).

**Scenario**: Developer velocity vs. testing
- **Resolution**: Unit tests for critical business logic are Mandub. 100% coverage including trivial code is Makruh.

---

## Learning Paths

### 30-Day Ethical Engineering Primer

**Week 1: Security Foundations**
- Read OWASP Top 10
- Implement: TLS, input validation, RBAC
- Scan dependencies for CVEs

**Week 2: Accessibility Basics**
- Read WCAG Quick Reference
- Implement: semantic HTML, keyboard nav
- Run axe DevTools on your application

**Week 3: Privacy & Ethics**
- Read GDPR Article 5 (data principles)
- Audit: what data do you collect? Is it necessary?
- Add privacy policy and consent flows

**Week 4: Infrastructure & Longevity**
- Document: create ADRs for major decisions
- Automate: move one manual process to CI/CD
- Test: run a disaster recovery drill

---

### 3-Month Deep Dive

**Month 1: Security Hardening**
- Implement defense in depth
- Set up SIEM (Security Information and Event Management)
- Conduct threat modeling workshop
- Penetration testing (external)

**Month 2: User-Centric Design**
- WCAG AA compliance audit
- User testing with disabled users
- Privacy-by-design architecture review
- Remove dark patterns

**Month 3: Sustainable Systems**
- Migrate to immutable infrastructure
- Comprehensive test suite (unit, integration, E2E)
- Monitoring & alerting framework
- Team sustainability audit (burnout prevention)

---

## Adoption Strategy

### Individual Engineer
1. **This week**: Run security scanner on your current project
2. **This month**: Audit accessibility of one feature you built
3. **This quarter**: Implement one Fard principle that's missing

### Team
1. **Sprint 1**: Establish security baseline (encryption, RBAC, input validation)
2. **Sprint 2-3**: Add accessibility to definition of done
3. **Month 2-3**: Migrate to CI/CD pipeline
4. **Month 4-6**: Comprehensive testing and documentation

### Organization
1. **Q1**: Executive buy-in, ethical engineering champion identified
2. **Q2**: Pilot team implements maturity level 2-3
3. **Q3**: Org-wide rollout with training
4. **Q4**: Measure, refine, publish case study

---

## Relationship to Other Manifestos

This manifesto integrates and extends:

- **🔬 Formal Verification**: Fard for safety-critical paths (Domain 1)
- **✨ Vibe Coding**: Mandub for knowledge capital (Domain 4, Principle XX)
- **🔒 Security Hardening**: Fard for encryption, access control, input validation (Domain 1)
- **🎨 User Experience**: Fard for accessibility, ethical design (Domain 3)
- **♿ Accessibility**: Fard - detailed implementation of Principle VIII (Domain 3)
- **📊 Data & Analytics**: Mandub for data quality, lineage (Domain 5)
- **📝 Content & Communication**: Mandub for documentation (Domain 4)

Ethical Engineering provides the **moral framework**. Other manifestos provide the **technical implementation**.

---

## Conclusion

Software engineering is not ethically neutral. Every line of code, every architectural decision, every deployment carries moral weight.

This manifesto provides a framework for navigating those choices:

- **Fard** (Critical): Encryption, accessibility, privacy, vulnerability remediation, human oversight for AI
- **Mandub** (Recommended): Testing, CI/CD, documentation, monitoring, immutable infrastructure
- **Mubah** (Discretionary): Technology choices, aesthetic decisions, A/B testing
- **Makruh** (Anti-Pattern): Manual deployments, god objects, premature optimization
- **Haram** (Prohibited): Hardcoded secrets, dark patterns, ignoring CVEs, selling user data, burnout culture

Build systems that are:
- **Secure** (Hifz al-Din): protecting truth and integrity
- **Efficient** (Hifz al-Mal): respecting resources
- **Sustainable** (Hifz al-Nasl): surviving across generations
- **Humane** (Hifz al-Nafs): protecting people
- **Understandable** (Hifz al-Aql): preserving knowledge

Code with integrity. Ship with conscience. Build for the long term.

---

**Navigation**: [Ethical Framework Mapping](./ETHICAL_FRAMEWORK_MAPPING.md) | [Changelog](./CHANGELOG.md) | [Main README](../README.md)
