---
name: data-analytics-review
description: Design, review, and remediate data platforms, pipelines, metrics, analytics, and ML data systems for reliability, quality, lineage, governance, observability, and scalable operation.
---
# Data and Analytics Review

Establish the decision, data grain, ownership, freshness requirement, and authoritative definitions before assessing a system. Trace inputs through transformations to outputs, test quality claims against observable evidence, and report unresolved lineage or measurement gaps. Do not infer data correctness from pipeline success alone.

**Version**: 2.1
**Last Updated**: 2025-11-23

> Data is not a byproduct; it is a foundational asset that requires disciplined engineering. Build reliable, scalable, and trustworthy data platforms that support better decisions.

---

## The 5 Rulings

### OBLIGATORY (Core Principles)
**Mandatory for reliable data engineering.**

-   **Treat Data as a Product**: Defined ownership, SLAs, and versioned schemas.
-   **Enforce Single Source of Truth**: One definition for "revenue", "customer", etc. No metric divergence.
-   **Guarantee Quality by Design**: Automated quality gates at ingestion. No bad data in Gold tables.
-   **Immutability**: Facts are appended, never overwritten. Preserve history.
-   **Declarative Logic**: Define *what* (SQL), not *how*. Version control everything.

### ENCOURAGED (Pillars of Implementation)
**Recommended best practices for scale.**

-   **Separation of Concerns**: Separate Storage, Compute, and Consumption.
-   **Schema as Contract**: Enforce schemas (Avro/Protobuf) to prevent breaking changes.
-   **Lineage & Provenance**: Traceability from source to report.
-   **Idempotency**: Pipelines must be re-runnable without side effects.
-   **Metrics as Code**: Define metrics in a semantic layer (e.g., dbt), not in BI tools.
-   **Data Observability**: Monitor freshness, volume, and quality automatically.

### OPTIONAL (Advanced Architecture)
**Context-dependent choices.**

-   **Data Mesh**: Decentralized domain ownership (for large orgs).
-   **Streaming Architecture**: Real-time event processing (only when latency requirements demand it).
-   **Feature Stores**: Managed ML features for training/serving consistency.

## Modern Data Architectures in Practice

-   **Data Mesh**: For large organizations, decentralize data ownership. Have each business domain own and serve its data as a product. A central platform team provides the self-serve infrastructure, and a federated governance body sets the standards.
-   **Streaming Architecture**: For real-time use cases (e.g., fraud detection), use an event-driven architecture with tools like Kafka and Flink. Understand that this adds significant complexity and cost and should be used deliberately, not as a default.
-   **ML/AI Pipelines**: Use a Feature Store to manage curated signals for machine learning. This helps prevent training/serving skew and provides a versioned, auditable source for model inputs.

## Common Anti-Patterns to Avoid

-   **Dashboard-Driven Development**: Building a pipeline just to match a broken dashboard. Fix the upstream data source instead.
-   **Copy-Paste Transformations**: Duplicating business logic (e.g., the definition of "revenue") in multiple places. Centralize it in a semantic layer.
-   **Schema-less Hell**: Dumping unstructured JSON into a data lake with no schema enforcement, leading to unreliable queries.
-   **Manual Data Quality**: Relying on an analyst to spot-check a dashboard every morning. Automate quality checks and alerts.
-   **The Centralized Bottleneck**: Forcing all data requests through a single, overworked data team. Enable self-service with good tooling and governance.

### DISCOURAGED (Anti-Patterns)
**Practices that lead to "data swamps".**

-   **Dashboard-Driven Development**: Building hacks to fix a chart.
-   **Copy-Paste Logic**: Duplicating SQL snippets across tools.
-   **Schema-less Hell**: Dumping raw JSON without structure or types.
-   **Manual Quality Checks**: "Eyeballing" the dashboard.
-   **Non-Deterministic Logic**: Using `NOW()` without a frozen timestamp in backfills.

### PROHIBITED (Forbidden)
**Practices that destroy trust.**

-   **Destructive Updates**: Overwriting historical facts without an audit trail.
-   **Undocumented Tables**: "Mystery data" in production.
-   **Silencing Alerts**: Ignoring pipeline failures.
-   **Direct Prod Access**: Ad-hoc write access to production warehouses.

---

## Measurement Framework

-   **Completeness**: ≥99%.
-   **Accuracy**: ≥99.9%.
-   **Pipeline Success**: ≥99.9%.
-   **Test Coverage**: ≥90% of critical tables.
