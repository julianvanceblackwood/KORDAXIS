# KORDAXIS

## Evidence-Native Cyber Mission Reasoning & Decision System

KORDAXIS is an engineering research system for reasoning about cyber environments when telemetry is incomplete, delayed, contradictory, degraded, or potentially manipulated.

It is not a SIEM.

It is not a SOC dashboard.

It is not a vulnerability scanner, generic threat-intelligence aggregator, attack-graph visualization product, or LLM wrapper.

KORDAXIS is designed around a harder problem:

> **Given imperfect evidence, what can a defender actually justify, what remains unknown, what can an adversary still reach, what mission consequences follow, and which defensive intervention changes the outcome with the least operational disruption?**

---

## System thesis

KORDAXIS maintains an uncertainty-aware, bitemporal model of a cyber environment; preserves evidence provenance; reconstructs adversary operations from imperfect observations; computes identity and authority transitions; evaluates attack reachability and mission consequence; and simulates defensive interventions before execution.

The project is built around one principle:

> **A trustworthy security system must remain explicit about what it knows, why it knows it, and what it still cannot prove.**

---

## Why KORDAXIS exists

Modern incidents rarely remain inside one technical layer.

A single operation may cross:

```text
Human Identity
    ↓
Session / Token
    ↓
OAuth / Federation / Delegation
    ↓
Repository
    ↓
CI/CD Workflow
    ↓
Runner / Build Environment
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
```

Traditional tooling often observes fragments of this chain independently.

KORDAXIS attempts to reason across those fragments without pretending that incomplete telemetry is complete truth.

---

## Core reasoning model

KORDAXIS keeps four concepts deliberately separate.

### Observation

What an external producer reported.

An observation may be correct, incomplete, stale, duplicated, delayed, or misleading.

### Evidence

Preserved material with explicit origin, integrity, provenance, temporal properties, and collection context.

Evidence is not silently rewritten when normalization or interpretation changes.

### Claim

A falsifiable semantic proposition supported or contradicted by evidence.

Example:

```text
Claim:
Session S was controlled by an unauthorized actor during interval T.

Support:
- authentication anomaly
- repository activity
- authority transition

Contradictions:
- expected administrative window

Missing expected evidence:
- endpoint heartbeat interval
```

### Decision

A defensive action evaluated against evidence sufficiency, mission constraints, uncertainty, reversibility, authorization, and expected consequence.

AI output alone is never sufficient evidence for a critical decision.

---

## Temporal cyber world model

KORDAXIS is not designed around a mutable "current state" table.

The system must answer both:

> What do we currently believe was true at time T?

and:

> What did KORDAXIS believe at knowledge time K about world time T?

For this reason, Generation 0 uses bitemporal semantics.

Material records distinguish:

```text
observed_at   → when the producer says something occurred
received_at   → when KORDAXIS received the material
valid_from/to → when the modeled state applies in the cyber world
recorded_at   → when KORDAXIS recorded the belief
superseded_at → when that belief was replaced by later knowledge
```

Late evidence may change today's reconstruction of yesterday.

It must never erase what the system believed yesterday.

---

## Evidence-native architecture

The Generation-0 reasoning flow is intentionally explicit:

```text
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
Telemetry / Source Trust
      ↓
Bitemporal World State
      ↓
Claims + Competing Hypotheses
      ↓
Identity / Authority Graph
      ↓
Attack Reachability
      ↓
Adversary Reconstruction
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
```

Derived state is treated as rebuildable.

Preserved evidence is the durable foundation.

---

## Identity and authority are first-class

KORDAXIS does not reduce identity to human user accounts.

Generation 0 models principals and authority relationships across:

- human identities
- service principals
- workload identities
- sessions and tokens
- OAuth grants
- OIDC assertions
- cloud roles
- federation bindings
- delegated authority
- temporary authority
- repositories
- CI/CD identities
- deployment authority

The important question is not only:

> Who is this identity?

It is:

> **What effective capability can this principal obtain through direct, inherited, delegated, federated, temporary, or transitive authority?**

This becomes the basis for authority-drift detection and attack reachability.

---

## Attack reachability, not static graph decoration

An edge in KORDAXIS is not merely a line between two nodes.

A transition may depend on:

- current authority
- credential possession
- trust relationships
- network feasibility
- software state
- federation state
- temporal validity
- adversary capability assumptions
- supporting evidence

A transition can therefore be classified as:

```text
ENABLED
POSSIBLY_ENABLED
DISABLED
UNKNOWN
```

`UNKNOWN` is not silently converted into reachable or unreachable.

---

## Competing hypotheses

KORDAXIS does not force one incident narrative too early.

The same evidence may support multiple explanations.

For example:

```text
H1 — compromised employee session
H2 — legitimate administrative activity
H3 — CI / supply-chain compromise
H4 — apparent incident amplified by degraded telemetry
```

Hypotheses accumulate support, contradiction, missing expected evidence, source diversity, and model uncertainty independently.

One hypothesis becoming stronger does not automatically delete the others.

A core investigation question is:

> **What obtainable evidence would most strongly distinguish the leading hypotheses?**

---

## Observability is itself security state

Zero telemetry does not mean zero threat.

If a source normally emits a heartbeat and becomes silent, KORDAXIS should reason about degraded observability rather than interpret silence as safety.

The system models factors such as:

- source identity
- freshness
- expected heartbeat
- delivery latency
- duplication
- missing intervals
- schema validity
- clock quality
- sequence consistency
- known impairment
- shared failure domains

Core invariant:

> **Absence of evidence is not evidence of absence unless an explicit observation model makes that absence meaningful.**

---

## Mission consequence

Technical reachability and mission consequence are intentionally different concepts.

A reachable database is not automatically a mission failure.

Generation 0 separates technical infrastructure from mission dependencies.

A mission capability may depend on components using semantics such as:

```text
REQUIRES_ALL
REQUIRES_ANY
K_OF_N
```

This allows KORDAXIS to reason about operational degradation rather than simply label every downstream node "critical."

---

## Defensive intervention and counterfactual reasoning

Finding an attack path is only part of the problem.

KORDAXIS ultimately asks:

> Which intervention removes the most meaningful adversary capability while causing the least mission disruption?

Candidate controls may include actions such as:

- revoke temporary authority
- invalidate a session
- remove a delegation
- isolate a CI runner
- block a deployment transition

Generation 0 begins with graph-cut style baselines, but the long-term problem includes:

- intervention cost
- partial effectiveness
- mission disruption
- reversibility
- execution time
- authorization constraints
- uncertain control effectiveness

Counterfactual simulation then asks questions such as:

```text
If authority A had been removed at T1,
which later transitions would become impossible?

If CI runner R had been isolated,
could production still be reached?
```

Counterfactuals operate over modeled transition rules rather than free-form LLM prediction.

---

## Decision safety

A technically possible defensive action is not automatically a safe action.

Before a critical action can cross the response boundary, the decision layer must evaluate:

- evidence sufficiency
- contradictory evidence
- current observability
- mission constraints
- authorization
- reversibility
- rollback availability
- execution uncertainty

Some states must explicitly produce:

```text
UNSAFE_TO_AUTOMATE
```

Generation 0 does not implement autonomous production remediation.

---

## Deterministic replay

Incident analysis must be reproducible.

Replay therefore binds results to explicit versions of:

- evidence inputs
- schemas
- policies
- inference logic
- solver configuration
- model versions
- scenario seeds

Equal source timestamps are not sufficient for deterministic ordering; ingestion assigns a stable ordering key.

Replay correctness is evaluated using canonical semantic outputs rather than incidental runtime metadata.

---

# Generation 0

Generation 0 intentionally proves one narrow but deep vertical slice before expanding the platform.

## GEN0-001 synthetic environment

```text
Employee Identity
       ↓
Git Provider
       ↓
Repository
       ↓
CI/CD Workflow
       ↓
Runner Identity
       ↓
Cloud Federation
       ↓
Deployment Authority
       ↓
Artifact Registry
       ↓
Production Workload
       ↓
Database
       ↓
Mission Capability Alpha
```

During the scenario, part of the telemetry is intentionally impaired.

The range owns ground truth.

KORDAXIS inference components do not.

## Ground-truth sequence

```text
T0  normal environment
T1  employee session becomes unauthorized
T2  repository reconnaissance
T3  CI trust relationship discovered
T4  software/build path changes
T5  CI workflow executes
T6  short-lived cloud authority obtained
T7  artifact lineage diverges
T8  artifact enters deployment path
T9  production authority becomes reachable
T10 database becomes reachable
T11 mission capability enters at-risk state
```

Controlled variants later introduce:

- event loss
- delayed telemetry
- clock skew
- duplicate delivery
- misleading observations
- sensor outage
- conflicting assertions

---

## Generation-0 proof obligations

Generation 0 does not pass because its output looks convincing.

It must demonstrate measurable behavior for:

- immutable raw evidence ingestion
- exact-byte hashing
- provenance-preserving normalization
- explicit parser failure
- bitemporal reconstruction
- telemetry-gap detection
- competing hypotheses
- effective-authority computation
- authority drift
- attack reachability
- software-supply-chain lineage
- mission consequence propagation
- intervention analysis
- counterfactual correctness
- safety-gated decisions
- decision receipts
- deterministic replay

See [Generation-0 acceptance tests](docs/acceptance-tests.md).

---

## Scientific evaluation

KORDAXIS separates:

### Development scenarios

Visible ground truth used while implementing behavior.

### Calibration scenarios

Held-out scenarios used for threshold and later confidence calibration.

### Blind evaluation scenarios

Ground truth unavailable to inference components during execution.

Representative metrics include:

- reconstruction precision / recall
- attack-path precision / recall
- false reachable-path rate
- authority-path correctness
- telemetry-gap detection
- evidence-lineage coverage
- mission-impact correctness
- intervention effectiveness
- counterfactual correctness
- replay determinism
- decision reproducibility

An internal score is not presented as a probability until calibration evidence exists.

See [Benchmark methodology](docs/benchmark-methodology.md).

---

## Generation-0 architecture

Generation 0 begins as a **modular monolith**.

Initial authoritative persistence is **PostgreSQL**.

The architecture intentionally does **not** begin with:

- Kafka
- Neo4j
- Redis
- Kubernetes
- Elasticsearch
- dozens of microservices

A dedicated infrastructure component must solve a measured problem before entering the architecture.

Current logical modules are:

```text
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
```

See [Generation-0 architecture](docs/generation-zero-architecture.md) and [ADR-0001](docs/adr/0001-generation-zero-architecture.md).

---

## Current engineering focus

**Generation 0 — Evidence foundation**

The active implementation milestone is:

```text
Exact Raw Bytes
      ↓
RawEventEnvelope
      ↓
Preserved Evidence
      ↓
Canonical Observation
```

The first implementation must prove that:

1. the exact received bytes are preserved;
2. the raw digest is computed over those exact bytes;
3. duplicate deliveries do not destroy receipt history;
4. parser failure never destroys evidence;
5. equal timestamps still receive deterministic ingest ordering;
6. normalization remains downstream from the immutable evidence boundary.

Active branch:

`feat/raw-evidence-envelope`

Primary Generation-0 tracking issue:

[#1 — Prove the evidence-to-decision vertical slice](https://github.com/julianvanceblackwood/KORDAXIS/issues/1)

No additional issue is created for routine work inside this already-defined engineering objective.

---

## Core invariants

1. No material conclusion without evidence lineage.
2. Historical knowledge is never silently rewritten.
3. `UNKNOWN` is never silently converted to `SAFE`.
4. Missing telemetry never automatically lowers risk.
5. Source trust is multidimensional.
6. Derived state must be rebuildable.
7. AI output is never authoritative by itself.
8. Replay cannot produce external side effects.
9. Mission consequence is distinct from technical reachability.
10. Cryptographic provenance is not semantic truth.
11. Every critical decision is attributable.
12. Complexity requires evidence.

Full definitions: [System invariants](docs/system-invariants.md).

---

## Documentation map

| Document | Purpose |
| --- | --- |
| [Manifesto](docs/manifesto.md) | The reasoning doctrine and epistemic philosophy |
| [Formal problem definition](docs/problem-definition.md) | Formalizes knowledge state, reachability, and intervention problems |
| [Threat model](docs/threat-model.md) | Defines Generation-0 adversary capabilities and trust assumptions |
| [Trust boundaries](docs/trust-boundaries.md) | Separates external assertions, evidence, reasoning, AI, and response boundaries |
| [System invariants](docs/system-invariants.md) | Architecture-level rules that features may not violate |
| [Canonical ontology](docs/ontology.md) | Defines Generation-0 entity and relationship vocabulary |
| [Event and evidence model](docs/event-evidence-model.md) | Defines raw envelopes, observations, evidence, claims, and inference records |
| [Temporal model](docs/temporal-model.md) | Defines observation, receipt, valid, and knowledge time |
| [Epistemic model](docs/epistemic-model.md) | Defines claims, contradictions, expected evidence, and competing hypotheses |
| [Generation-0 architecture](docs/generation-zero-architecture.md) | Defines initial module boundaries and technology constraints |
| [Synthetic range](docs/range-design.md) | Defines GEN0-001 and ground-truth isolation |
| [Acceptance tests](docs/acceptance-tests.md) | Defines what Generation 0 must prove |
| [Benchmark methodology](docs/benchmark-methodology.md) | Defines scientific evaluation and anti-overfitting discipline |
| [ADR-0001](docs/adr/0001-generation-zero-architecture.md) | Records the initial modular-monolith architecture decision |

---

## Repository engineering discipline

`main` is the authoritative integration branch.

Material changes enter through short-lived branches and pull requests.

Issues are intentionally sparse.

An issue is justified for:

- a reproducible defect or invariant violation
- a significant architectural change
- a research problem that changes implementation
- a measurable benchmark gap
- a security-relevant capability requiring coordinated work

An issue is **not** required for:

- routine README edits
- small documentation corrections
- mechanical formatting
- straightforward work already covered by an active engineering issue

Not every PR requires a new issue.

Pull requests remain important because they preserve:

- isolated diffs
- CI evidence
- review history
- failure-mode analysis
- rollback context
- architectural traceability

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Security

Do not disclose suspected vulnerabilities through public issues.

Use the repository's private vulnerability reporting path.

See [SECURITY.md](SECURITY.md).

---

## What KORDAXIS will not do in Generation 0

Generation 0 deliberately excludes:

- autonomous production remediation
- real-target offensive exploitation
- internet-scale scanning
- nation-state attribution
- predictive "next attack" claims
- generic chatbot development
- arbitrary machine learning
- premature distributed architecture
- blockchain
- custom cryptography

These do not make the system more rigorous.

---

## Final standard

The objective is not to produce a repository that merely looks sophisticated.

The objective is to produce engineering evidence that the system can remain trustworthy when:

- observations are incomplete,
- telemetry is degraded,
- sources disagree,
- authority propagates indirectly,
- software provenance becomes uncertain,
- and defensive actions have mission consequences.

> **The hardest security system is not the one with the most components. It is the one that remains defensible when its information is incomplete and its environment is hostile.**

---

**Observe. Preserve. Corroborate. Challenge. Reconstruct. Compute. Simulate. Constrain. Decide. Prove.**
