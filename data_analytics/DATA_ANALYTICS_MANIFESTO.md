---
id: "data-analytics"
title: "Data & Analytics Manifesto"
version: "2.1"
status: "current"
focus: "Data reliability & scalability"
primary_users: ["data-engineers", "data-analysts", "ml-engineers"]
learning_curve: "medium-high"
roi_timeline: "medium-term"
adoption_scope: "data-intensive"
principles_count: 5 # Was 18, revised to 5 core principles
tier_structure:
  core: 5
  standard: 0
  excellence: 0
applicability:
  project_types: ["data-warehouses", "data-pipelines", "bi-systems", "ml-platforms", "data-mesh"]
  languages: ["sql", "python", "scala", "java"]
  contexts: ["batch-processing", "streaming", "analytics", "reporting"]
related_manifestos:
  complements: ["security-hardening", "vibe-coding"]
  prerequisites: []
  enables: ["ml-ops", "data-governance"]
tools:
  categories: ["orchestration", "quality", "observability", "governance"]
  count: 40+
measurement:
  data_quality:
    completeness:
      target: "≥99%"
      acceptable: "≥95%"
      measurement: "great-expectations-dbt-tests"
    accuracy:
      target: "≥99.9%"
      acceptable: "≥99%"
      measurement: "validation-rules"
    timeliness:
      target: "≤sla"
      measurement: "pipeline-orchestrator"
  slos:
    pipeline_success_rate:
      target: "≥99.9%"
      acceptable: "≥99%"
      measurement: "airflow-dagster-metrics"
    data_freshness:
      target: "≤15 minutes for real-time"
      acceptable: "≤1 hour for near-real-time"
      measurement: "dbt-freshness-checks"
  testing:
    data_test_coverage:
      target: "≥90% of critical tables"
      measurement: "dbt-test-count"
  incident_response:
    mttr_data_incidents:
      target: "≤4 hours"
      acceptable: "≤8 hours"
      measurement: "incident-tracking-system"
---
# The Data & Analytics Manifesto

**Version**: 2.1
**Last Updated**: 2025-11-23

> Data is not a byproduct; it is a foundational asset that requires disciplined engineering. This manifesto outlines the principles for building reliable, scalable, and trustworthy data platforms that empower an organization to make better decisions, faster.

---

## The Five Core Principles

These five principles are the philosophical core of modern data engineering. They provide the "why" behind the technical decisions that follow.

### 1. Treat Data as a Product.
Data assets are not side effects of operational systems; they are first-class products. Each dataset must have a clear owner, documented SLAs, versioned schemas, and a defined set of consumers. The producers of data are accountable for its quality and reliability, and their success is measured by the success of their consumers.

### 2. Build on a Foundation of Immutability.
Facts are appended, never overwritten. Historical data is a permanent, auditable log of what happened. The current state is always a derivation of this history. This approach simplifies pipelines, enables time-travel queries, and ensures that corrections are made by appending new information, not by destroying the old.

### 3. Enforce a Single Source of Truth (SSOT).
Every core business concept (e.g., "customer," "revenue," "active user") must have exactly one, authoritative source. Downstream systems can consume and transform this data, but they must never redefine it. This prevents metric divergence and ensures the entire organization is operating from a shared, consistent understanding of reality.

### 4. Guarantee Quality by Design.
Data quality is not an afterthought; it is a feature that must be built and tested at every step. Invalid data should be rejected at the point of ingestion, not discovered by an analyst in a dashboard weeks later. Pipelines must have automated quality gates, and data assets must be monitored for freshness, volume, and correctness.

### 5. Define Logic Declaratively.
Data transformations should define *what* the desired state is, not *how* to achieve it. Use declarative tools like SQL to create version-controlled, peer-reviewed, and easily testable transformation logic. This approach makes data pipelines more transparent, maintainable, and self-documenting.

---

## The Pillars of Implementation

These pillars provide the practical "how" for implementing the core principles. They contain more specific guidance and best practices.

### Pillar 1: Foundational Architecture
*(Implements: Immutability, Single Source of Truth)*

-   **Separation of Concerns**: Architecturally separate storage, computation, and consumption layers. Use a columnar warehouse (e.g., Snowflake, BigQuery) for analytics (OLAP) and a row-based database (e.g., PostgreSQL) for transactions (OLTP).
-   **Late Binding & Flexibility**: Use a layered approach (e.g., Bronze/Silver/Gold). Keep raw data in a flexible, schema-on-read format in the "Bronze" layer for exploration. Enforce strict schemas and governance in the "Gold" layer for production reporting.
-   **Partitioning**: Partition large datasets by time or another relevant key. This is the single most effective strategy for cost and performance optimization, as it allows queries to scan only the data they need.

### Pillar 2: Quality & Governance
*(Implements: Quality by Design, Data as a Product)*

-   **Schema as Contract**: Data structures must be explicitly defined, versioned, and enforced using a schema registry (e.g., Avro, Protobuf). Breaking changes must be managed through versioning.
-   **Lineage & Provenance**: All data transformations must be traceable from the source to the final report. This is critical for debugging, impact analysis, and building trust.
-   **Privacy by Design**: Data governance must be embedded in the architecture. Classify data automatically, enforce access controls, and manage retention policies to comply with regulations like GDPR.
-   **Comprehensive Testing**: Test your data pipelines as rigorously as you test your application code. This includes unit tests for transformations, integration tests for pipeline segments, and contract tests between producers and consumers.

### Pillar 3: Efficient & Maintainable Pipelines
*(Implements: Declarative Logic, Immutability)*

-   **Idempotency & Determinism**: Every pipeline run must produce the identical result if run multiple times on the same input. This makes reprocessing safe and debugging predictable. Avoid non-deterministic functions like `NOW()` in your core logic.
-   **Incremental Processing**: Design pipelines to process only new or changed data since the last run. Full table scans are inefficient and costly.
-   **Cost-Aware Engineering**: Understand the cost implications of your design choices (e.g., materialization strategies, compute sizing). Monitor costs and set budget alerts.

### Pillar 4: Value & Consumption
*(Implements: Data as a Product, Single Source of Truth)*

-   **Metrics as Code**: Define key business metrics (e.g., revenue, churn) in a centralized, version-controlled semantic layer (e.g., dbt metrics, LookML). This ensures consistency across all reports and dashboards.
-   **Data Observability**: Instrument your pipelines to automatically monitor and alert on issues with freshness, volume, schema, and data quality. Don't wait for users to report broken dashboards.
-   **Documentation as Practice**: Every dataset must be documented with a clear description, owner, and column definitions. Good documentation turns a table into a usable product.

---

## Modern Data Architectures in Practice

-   **Data Mesh**: For large organizations, decentralize data ownership. Have each business domain own and serve its data as a product. A central platform team provides the self-serve infrastructure, and a federated governance body sets the standards.
-   **Streaming Architecture**: For real-time use cases (e.g., fraud detection), use an event-driven architecture with tools like Kafka and Flink. Understand that this adds significant complexity and cost and should be used deliberately, not as a default.
-   **ML/AI Pipelines**: Use a Feature Store to manage curated signals for machine learning. This helps prevent training/serving skew and provides a versioned, auditable source for model inputs.

---

## Common Anti-Patterns to Avoid

-   **Dashboard-Driven Development**: Building a pipeline just to match a broken dashboard. Fix the upstream data source instead.
-   **Copy-Paste Transformations**: Duplicating business logic (e.g., the definition of "revenue") in multiple places. Centralize it in a semantic layer.
-   **Schema-less Hell**: Dumping unstructured JSON into a data lake with no schema enforcement, leading to unreliable queries.
-   **Manual Data Quality**: Relying on an analyst to spot-check a dashboard every morning. Automate quality checks and alerts.
-   **The Centralized Bottleneck**: Forcing all data requests through a single, overworked data team. Enable self-service with good tooling and governance.

---

## Appendices for Practitioners

*(This section would link to the detailed content from the original manifesto, reformatted as appendices.)*

-   **Appendix A: Detailed Implementation Guides for all 18 Original Principles**
-   **Appendix B: Data Tooling Ecosystem Map**
-   **Appendix C: Data Pipeline Maturity Model**
-   **Appendix D: Dimensional Modeling Best Practices**
-   **Appendix E: Implementation Checklists**
