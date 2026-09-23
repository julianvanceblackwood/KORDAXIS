# KORDAXIS Development Method

## Purpose

KORDAXIS is developed through an evidence-native, foundations-first systems engineering method.

The objective is not to maximize feature count, commit volume, architectural complexity, or visual polish. The objective is to produce behavior that can be explained, tested, challenged, reproduced, and traced to evidence.

> Understanding precedes implementation. Evidence precedes confidence.

## Normative authority

This document defines the development process. It does not redefine KORDAXIS domain semantics.

Normative system behavior is defined by the dedicated specifications and ADRs, including:

- docs/system-invariants.md
- docs/event-evidence-model.md
- docs/temporal-model.md
- docs/epistemic-model.md
- docs/trust-boundaries.md
- docs/acceptance-tests.md
- docs/benchmark-methodology.md
- docs/adr/

If this document and a normative specification differ, the normative specification governs. Semantic changes update the authoritative specification first.

## Development loop

Material work should normally follow this sequence:

~~~text
Real problem
    ↓
Required foundations
    ↓
Mental model
    ↓
Failure model
    ↓
Invariant
    ↓
Minimal experiment
    ↓
Contract
    ↓
Implementation
    ↓
Verification
    ↓
Measurement or replay
    ↓
Cross-examination
    ↓
Pull request
    ↓
Merge
~~~

The sequence exists to prevent implementation from outrunning understanding.

A development gate may end in one of five states:

- ADVANCE: evidence supports the next layer
- REVISE: the model remains useful but needs correction
- REPEAT: the experiment is inconclusive
- REJECT: the hypothesis did not survive testing
- UNKNOWN: available evidence does not justify a stronger conclusion

A failed experiment is useful when it changes the model.

## Problem framing

Implementation starts with a bounded problem, not a preferred technology.

Before substantive work, establish:

- what is unknown, incorrect, unsafe, missing, or unverified
- why the problem matters
- what evidence suggests the problem exists
- the system and trust boundaries involved
- assumptions
- in-scope and out-of-scope behavior
- success criteria
- falsification criteria
- the smallest experiment capable of changing the decision

A problem that cannot be bounded is not ready for implementation.

## Foundations rule

Study prerequisites because correctness depends on them, not because they make the project look advanced.

Possible foundations include logic, sets, relations, probability, graph theory, algorithms, databases, operating systems, networking, distributed systems, concurrency, cryptography, measurement, security engineering, and experimental design.

For each topic:

1. identify the primitive concept
2. explain the system consequence
3. connect it to the KORDAXIS problem
4. test transfer with a different example
5. implement only after the mental model is stable enough to review

Do not skip a prerequisite that materially affects correctness. Do not add one for appearance.

## Semantic contract review

A data model is not correct merely because its types compile.

Every material field must answer:

### Meaning

What fact, assertion, state, or relationship does the field represent?

### Origin

Who first asserts or generates the value?

### Assignment

Which KORDAXIS component records or derives it?

### Authority

Which source or contract is authoritative for its meaning?

### Presence

Can the value be unknown, absent, not applicable, invalid, or omitted? Are those states semantically distinct?

### Determinism

Given the same preserved inputs, versions, policy, and configuration, must replay produce the same value?

### Version dependence

Which schema, parser, normalizer, policy, model, or solver version determines the field semantics?

Ambiguous answers require design work before implementation.

## Identity discipline

Different identity domains must not collapse into one identifier.

Examples include:

- receipt identity
- payload content identity
- source event identity
- canonical observation identity
- entity identity
- claim identity
- inference identity
- decision identity
- replay identity

Equality in one domain does not imply equality in another.

Examples:

~~~text
same payload bytes
≠
same receipt

same source event identifier
≠
proven same real-world event

two receipts
≠
two semantic observations
~~~

Deduplication rules follow declared identity semantics, not convenience.

## Evidence boundary

Raw material is preserved before interpretation.

~~~text
External material
    ↓
Exact raw bytes
    ↓
Receipt
    ↓
Persistence
    ↓
Parsing
    ↓
Normalization
    ↓
Canonical observation
    ↓
Evidence
    ↓
Claim
    ↓
Reasoning
~~~

The boundary has four non-negotiable properties:

- parsing never replaces raw evidence
- normalization never rewrites raw evidence
- malformed input produces explicit failure state
- derived state remains attributable to preserved inputs

Corrections create new derived representations or supersession relationships. They do not rewrite history.

## Implementation discipline

Project source is authored and edited in VS Code.

The terminal is used for:

- Git operations
- tests
- dependency and environment management
- database commands
- static analysis
- debugging
- profiling
- benchmark execution
- generated-output inspection

Important implementation lines should be explainable in terms of syntax, type behavior, control flow, failure behavior, security implications, and relevant performance or memory consequences.

KORDAXIS owns its domain semantics, invariants, reasoning models, data contracts, experiments, and replay rules.

It does not reimplement mature infrastructure or cryptographic primitives merely to appear self-contained. Proven primitives are reused when doing so reduces correctness and security risk.

## Complexity rule

Architecture is an engineering response to measured requirements.

Generation 0 remains a modular monolith unless evidence demonstrates a need for additional infrastructure.

A new service, broker, cache, database, orchestration layer, or distributed boundary requires a concrete problem such as:

- measured throughput limitation
- measured query limitation
- memory pressure
- isolation requirement
- durability requirement
- backpressure requirement
- coordination requirement

Technology choice is not portfolio evidence by itself.

## Verification discipline

Tests target invariants and failure modes, not demonstrations.

Relevant questions include:

- can raw evidence be modified
- can malformed input enter canonical state
- can duplicate delivery destroy receipt history
- can semantic deduplication double-count evidence
- can missing telemetry collapse to SAFE
- can stale or degraded sources appear healthy
- can equal timestamps break deterministic replay
- can provenance become unresolved
- can a trust boundary be bypassed
- can replay produce external side effects
- can a decision lose its evidence or authorization lineage

Choose the test technique that exposes the failure mode.

Possible techniques include:

- unit tests
- integration tests
- database constraint tests
- negative tests
- property-based tests
- fuzzing
- fault injection
- corruption tests
- concurrency tests
- differential tests
- deterministic replay tests
- controlled ground-truth experiments

A passing happy path is necessary but insufficient.

## Debugging discipline

Debugging is hypothesis testing.

~~~text
Observed failure
    ↓
Bound the problem
    ↓
Form hypothesis
    ↓
Design discriminating test
    ↓
Collect evidence
    ↓
Reject or retain hypothesis
    ↓
Identify cause
    ↓
Fix
    ↓
Regression test
~~~

Changing code until the symptom disappears is not a sufficient explanation.

## Measurement discipline

Words such as fast, scalable, low-latency, efficient, and real-time require a declared measurement.

Possible dimensions include:

- ingest throughput
- persistence latency
- normalization latency
- reconstruction latency
- reachability latency
- intervention-solver latency
- replay runtime
- CPU use
- memory use
- storage amplification

Measurements must state workload, environment, versions, methodology, and relevant uncertainty.

Optimization starts after a bottleneck is demonstrated.

## Reproducibility and replay

Replay is part of the evidence model, not only a debugging tool.

A semantic output is treated conceptually as a function of declared inputs:

~~~text
output =
F(
    preserved evidence,
    ordering,
    schemas,
    parser versions,
    normalizer versions,
    policies,
    model versions,
    solver versions,
    configuration,
    seeds
)
~~~

Derived state must not silently depend on undeclared sources such as current wall-clock time, randomness, mutable external APIs, ambient filesystem state, or machine-local configuration.

If nondeterminism is necessary, the source and replay consequences must be explicit.

## Cross-examination

Before merge, review the change as if the author were wrong.

Ask:

- is the semantic model precise
- is any claim stronger than the evidence
- what happens with malformed input
- what happens with duplicate, delayed, stale, or contradictory input
- what happens when a source degrades
- can provenance break
- can UNKNOWN disappear
- can history be rewritten
- can replay diverge
- can a security or authorization boundary be bypassed
- is there a simpler design with equal evidence
- does the change introduce an undeclared dependency

Review friction is expected when evidence is weak.

## Git and GitHub lifecycle

Substantive work should normally follow:

~~~text
Problem
    ↓
Issue when durable tracking is justified
    ↓
Research or design
    ↓
Short-lived branch
    ↓
Implementation
    ↓
Tests or experiments
    ↓
Local diff review
    ↓
Commit
    ↓
Push
    ↓
Pull request
    ↓
CI
    ↓
Cross-examination
    ↓
Merge
~~~

Issues are intentionally sparse.

Use an issue for a meaningful engineering objective, architecture change, security problem, benchmark gap, research question, or reproducible defect.

Do not create issues for typos, routine formatting, trivial README edits, or housekeeping already covered by an active objective.

Commit volume is not a performance metric.

## Repository evidence

Public repository history is treated as engineering evidence.

Strong artifacts include:

- falsifiable problem statements
- versioned specifications
- controlled experiments
- benchmarks
- threat models
- architecture decisions
- invariant-driven tests
- failure analysis
- explicit limitations
- reproducible outputs
- review history

The repository should show what was established and how it was challenged.

## Operator surface

A future operator interface is a projection of authoritative and derived state. It is not a source of truth.

UI work follows proven contracts for evidence, provenance, time, observability, claims, authority, reachability, mission consequence, intervention, decisions, and replay.

A convincing interface cannot substitute for an unproven reasoning layer.

## Cross-repository integration

External systems connect through explicit, versioned contracts.

~~~text
External system
    ↓
Versioned contract
    ↓
KORDAXIS trust boundary
    ↓
Raw preservation
    ↓
Adapter
    ↓
Canonical representation
    ↓
Reasoning
~~~

A participating system should state:

- I PRODUCE
- I CONSUME
- I GUARANTEE
- I DO NOT GUARANTEE

KORDAXIS does not silently promote another repository's output to ground truth.

ELENCHION may become an external evidence-producing system, but producer identity, version, provenance, uncertainty, and trust dependencies must remain explicit.

## Security and action authority

KORDAXIS is developed as defensive and controlled research infrastructure.

Research and testing must not silently expand into real-world offensive exploitation, credential theft, malware deployment, destructive action, unauthorized scanning, persistence, command-and-control capability, or autonomous real-target remediation.

Automation may reconstruct, compare, simulate, identify uncertainty, and propose interventions.

It does not automatically gain authority to execute high-impact external actions.

## Current gate: Canonical Observation

The current engineering question is:

> How can source-specific assertions be converted into a deterministic canonical representation without destroying raw evidence, manufacturing certainty, or breaking provenance?

The implementation must eventually demonstrate:

- raw evidence remains unchanged
- malformed input fails explicitly
- normalization is deterministic within declared versions
- observation lineage resolves to preserved raw evidence
- a source assertion is not promoted to truth
- duplicate receipts do not automatically double-count semantic state
- schema and normalizer changes remain attributable

Before a Canonical Observation field is accepted, review:

- what does it mean
- who originates it
- who assigns it
- who is authoritative
- can it be unknown or omitted
- can it be invalid or not applicable
- is absence meaningful
- must replay reproduce it
- which input determines it
- which version determines its semantics

Implementation begins only after these contracts are precise enough to test.

## Definition of progress

A development session produces durable progress when it strengthens at least one of:

- understanding
- specification
- evidence
- implementation
- testing
- measurement
- reproducibility
- security
- architecture clarity
- failure understanding

A commit is justified when the repository gains durable engineering value.

KORDAXIS follows one final rule:

> Never manufacture certainty that the evidence does not support.
