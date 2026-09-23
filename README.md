# KORDAXIS

## Evidence-Native Cyber Mission Reasoning & Decision System

KORDAXIS is an engineering research system for reasoning about cyber environments when telemetry is incomplete, delayed, contradictory, degraded, or potentially manipulated.

It is not a SIEM, SOC dashboard, vulnerability scanner, generic threat-intelligence aggregator, attack-graph visualization product, or LLM wrapper.

KORDAXIS is built around a harder question:

> **Given imperfect evidence, what can a defender justify, what remains unknown, what can an adversary still reach, what mission consequences follow, and which defensive intervention changes the outcome with the least operational disruption?**

## System thesis

KORDAXIS maintains an uncertainty-aware, bitemporal model of a cyber environment. It preserves evidence provenance, reconstructs operations from imperfect observations, models identity and effective authority, computes reachability and mission consequence, evaluates defensive interventions, and preserves the information required for deterministic replay.

The governing principle is simple:

> **A trustworthy security system must remain explicit about what it knows, why it knows it, and what it still cannot prove.**

## Core model

KORDAXIS keeps four concepts separate.

### Observation

A normalized representation of what a source asserted or what a defined observation process produced.

An observation is not automatically ground truth.

### Evidence

Preserved material with explicit origin, integrity, provenance, temporal properties, and collection context.

Normalization and interpretation never replace the original raw evidence.

### Claim

A falsifiable semantic proposition supported or contradicted by evidence.

Claims retain supporting evidence, contradicting evidence, assumptions, expected-but-missing evidence, coverage gaps, and versioned classification state.

### Decision

A defensive action evaluated against evidence sufficiency, uncertainty, mission constraints, reversibility, authorization, simulation results, and expected consequence.

AI output alone is never authoritative evidence for a critical decision.

## Reasoning flow

Generation 0 uses an explicit evidence-to-decision pipeline:

~~~text
External Sources
      ↓
Raw Event Ingestion
      ↓
Immutable Raw Evidence
      ↓
Canonical Observations
      ↓
Provenance + Integrity
      ↓
Temporal + Observability State
      ↓
Claims + Competing Hypotheses
      ↓
Identity + Effective Authority
      ↓
Reachability
      ↓
Operation Reconstruction
      ↓
Mission Consequence
      ↓
Candidate Interventions
      ↓
Counterfactual Simulation
      ↓
Decision Safety Gate
      ↓
Decision Receipt
      ↓
Deterministic Replay
~~~

Derived state is rebuildable. Preserved evidence is the durable foundation.

## Why the model is evidence-native

Modern incidents cross technical layers:

~~~text
Human Identity
    ↓
Session / Token
    ↓
OAuth / Federation / Delegation
    ↓
Repository
    ↓
CI/CD
    ↓
Artifact
    ↓
Deployment Authority
    ↓
Workload Identity
    ↓
Database / Data
    ↓
Mission Capability
~~~

Traditional tools often observe fragments of this chain independently.

KORDAXIS is designed to reason across those fragments without treating incomplete telemetry as complete truth.

That requires several architecture-level distinctions:

- source assertions are not truth
- content identity is not receipt identity
- valid time is not knowledge time
- missing telemetry is not a safe state
- trust is multidimensional
- technical reachability is not mission consequence
- a recommendation is not authorization
- provenance is not semantic correctness
- replay ordering is not real-world event ordering

The normative definitions live in the project specifications, not in the README.

## Generation 0

Generation 0 proves one narrow vertical slice before the platform expands.

The synthetic environment spans:

~~~text
Employee Identity
      ↓
Git Provider
      ↓
Repository
      ↓
CI/CD Trust
      ↓
Cloud Federation
      ↓
Artifact Registry
      ↓
Production Workload
      ↓
Database
      ↓
Mission Capability
~~~

The range owns ground truth. KORDAXIS inference components do not.

Controlled variants introduce event loss, delivery delay, clock skew, duplicate delivery, misleading observations, source outage, stale context, and conflicting assertions.

Primary tracking issue:

[#1 Prove the evidence-to-decision vertical slice](https://github.com/julianvanceblackwood/KORDAXIS/issues/1)

## Current implementation status

The raw evidence boundary is implemented.

Generation 0 currently has:

- exact-byte payload preservation
- SHA-256 content identity over the preserved bytes
- immutable raw receipt domain objects
- PostgreSQL authoritative raw-evidence persistence
- database-assigned ingest ordering
- duplicate receipt preservation with payload content deduplication
- append-only database enforcement for raw evidence tables
- integrity validation when evidence is reconstructed from persistence
- unit and real PostgreSQL integration coverage in CI

This establishes the boundary below normalization.

## Current gate: Canonical Observation

The next engineering gate is:

~~~text
Persisted Raw Evidence
        ↓
Parsing
        ↓
Canonical Observation
        ↓
Provenance Link
        ↓
Replayable Knowledge Input
~~~

The central question is:

> **How can source-specific assertions be converted into a deterministic canonical representation without destroying raw evidence, manufacturing certainty, or breaking provenance?**

The next slice must establish explicit contracts for observation identity, source attribution, parsing failure, normalization versions, schema evolution, temporal semantics, absence and UNKNOWN semantics, provenance, and deterministic replay.

Implementation follows semantic review. Every material field must answer:

- what does it mean
- who originates it
- who assigns it
- who is authoritative
- can it be unknown, absent, invalid, or not applicable
- must replay reproduce it
- which version defines its semantics

## Architecture

Generation 0 is a modular monolith with PostgreSQL as authoritative persistence.

Logical modules are:

~~~text
ingest
normalize
provenance
temporal
trust
epistemic
authority
reachability
reconstruction
mission
intervention
simulation
safety
receipt
replay
range
~~~

The architecture does not begin with Kafka, Neo4j, Redis, Kubernetes, Elasticsearch, or a microservice fleet.

A new infrastructure component must solve a measured problem before entering the design.

See [Generation-0 architecture](docs/generation-zero-architecture.md) and [ADR-0001](docs/adr/0001-generation-zero-architecture.md).

## Scientific evaluation

Generation 0 separates development, calibration, and blind-evaluation scenarios.

Capability claims require automated tests, controlled experiments, benchmark evidence, or comparison with withheld synthetic ground truth as appropriate.

An internal score is not presented as a probability until calibration evidence exists.

See:

- [Acceptance tests](docs/acceptance-tests.md)
- [Benchmark methodology](docs/benchmark-methodology.md)
- [Synthetic range](docs/range-design.md)

## Core invariants

Features may not violate the architecture-level invariants.

Among them:

- no material conclusion without machine-resolvable evidence lineage
- historical knowledge is never silently rewritten
- UNKNOWN never collapses to SAFE
- silence becomes meaningful only under an observation model
- source trust remains multidimensional
- derived state is rebuildable
- AI output is non-authoritative
- replay is side-effect free
- mission consequence differs from technical reachability
- provenance does not prove semantic truth
- material decisions remain attributable

Full definitions: [System invariants](docs/system-invariants.md).

## Documentation map

| Document | Purpose |
| --- | --- |
| [Development method](docs/engineering/DEVELOPMENT_METHOD.md) | Defines the evidence-native engineering, verification, replay, review, and Git/GitHub process |
| [Manifesto](docs/manifesto.md) | Defines the reasoning doctrine |
| [Formal problem definition](docs/problem-definition.md) | Formalizes knowledge state, reachability, and intervention problems |
| [Threat model](docs/threat-model.md) | Defines Generation-0 adversary capabilities and trust assumptions |
| [Trust boundaries](docs/trust-boundaries.md) | Defines external assertion, reasoning, AI, decision, response, and evaluation boundaries |
| [System invariants](docs/system-invariants.md) | Defines architecture-level rules |
| [Canonical ontology](docs/ontology.md) | Defines Generation-0 entity and relationship vocabulary |
| [Event and evidence model](docs/event-evidence-model.md) | Defines raw payloads, receipt envelopes, observations, evidence, claims, and inference records |
| [Temporal model](docs/temporal-model.md) | Defines observation, receipt, valid, and knowledge time |
| [Epistemic model](docs/epistemic-model.md) | Defines claims, contradictions, expected evidence, and competing hypotheses |
| [Generation-0 architecture](docs/generation-zero-architecture.md) | Defines initial module boundaries and technology constraints |
| [Synthetic range](docs/range-design.md) | Defines GEN0-001 and ground-truth isolation |
| [Acceptance tests](docs/acceptance-tests.md) | Defines what Generation 0 must prove |
| [Benchmark methodology](docs/benchmark-methodology.md) | Defines scientific evaluation and anti-overfitting discipline |
| [ADR-0001](docs/adr/0001-generation-zero-architecture.md) | Records the initial modular-monolith architecture decision |

## Engineering discipline

Material changes enter through short-lived branches and pull requests.

Issues are intentionally sparse and reserved for meaningful engineering objectives, architecture changes, security-relevant problems, benchmark gaps, research questions, and reproducible defects.

Repository activity is not a performance metric.

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Development method](docs/engineering/DEVELOPMENT_METHOD.md).

## Security

KORDAXIS is defensive and controlled research infrastructure.

Generation 0 deliberately excludes:

- autonomous production remediation
- real-target offensive exploitation
- unauthorized or internet-scale scanning
- credential theft or malware deployment
- nation-state attribution
- generic chatbot development
- arbitrary machine learning
- premature distributed architecture
- custom cryptography

Do not disclose suspected vulnerabilities through public issues.

See [SECURITY.md](SECURITY.md).

## Standard

KORDAXIS is not considered correct because its output looks convincing.

It must remain defensible when evidence is incomplete, sources disagree, observability degrades, authority propagates indirectly, provenance becomes uncertain, and defensive actions have mission consequences.

**Observe. Preserve. Corroborate. Challenge. Reconstruct. Compute. Simulate. Constrain. Decide. Prove.**
