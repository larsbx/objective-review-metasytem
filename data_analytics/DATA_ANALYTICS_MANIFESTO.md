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
principles_count: 5
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

> Data is a foundational asset. We treat it as a product, build on immutability, and guarantee quality by design.

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
