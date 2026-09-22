# KORDAXIS Development Method

## Evidence-Native Systems Engineering

## Purpose

KORDAXIS is developed through an **evidence-native, foundations-first systems engineering method**.

The objective is not to maximize implementation speed, feature count, repository activity, architectural complexity, or visual sophistication.

The objective is to construct a system whose important conclusions, state transitions, decisions, and engineering claims can be explained, challenged, reproduced, and traced to evidence.

KORDAXIS therefore treats:

* learning;
* research;
* formalization;
* implementation;
* experimentation;
* testing;
* measurement;
* security review;
* replay;
* documentation;
* and public engineering history

as parts of one continuous engineering process.

> **Preserve evidence before interpretation.
> Model uncertainty before confidence.
> Measure before claiming.
> Reproduce before trusting.**

---

## Normative Boundary

This document defines how KORDAXIS engineering work is conducted.

It does not replace the domain specifications that define the semantics of the system.

Normative domain semantics remain defined by dedicated artifacts including:

- `docs/system-invariants.md`
- `docs/event-evidence-model.md`
- `docs/temporal-model.md`
- `docs/epistemic-model.md`
- `docs/trust-boundaries.md`
- `docs/acceptance-tests.md`
- `docs/benchmark-methodology.md`
- relevant ADRs and versioned contracts

Where this development method summarizes a domain concept and a dedicated specification differs, the dedicated specification governs.

Changes to domain semantics must update the normative source first. This document may then be updated to reflect the resulting engineering process.


# 1. Engineering Thesis

KORDAXIS exists because operational cyber environments are not perfectly observable.

Telemetry can be:

* incomplete;
* duplicated;
* delayed;
* reordered;
* stale;
* malformed;
* contradictory;
* corrupted;
* produced by degraded sensors;
* produced by untrusted sources;
* semantically ambiguous;
* or unavailable.

The system must therefore never confuse:

```text
observation
```

with:

```text
truth
```

or:

```text
missing evidence
```

with:

```text
evidence of absence
```

or:

```text
technical reachability
```

with:

```text
mission consequence
```

or:

```text
recommended intervention
```

with:

```text
authorized action
```

The engineering method exists to preserve these distinctions throughout the system.

---

# 2. The Development Pipeline

KORDAXIS work should normally progress through the following sequence:

```text
Real Problem
    ↓
Prerequisite Knowledge
    ↓
Mental Model
    ↓
Failure Model
    ↓
Formal Semantics
    ↓
Invariant
    ↓
Minimal Experiment
    ↓
Contract
    ↓
Implementation
    ↓
Negative / Adversarial Testing
    ↓
Benchmark
    ↓
Replay Verification
    ↓
Cross-Examination
    ↓
Engineering Evidence
    ↓
Pull Request
    ↓
Merge
    ↓
Operator Surface
```

The sequence is not bureaucracy.

It exists to prevent implementation from outrunning understanding.

---

# 3. Three Parallel Tracks

Every major KORDAXIS development slice should be understood through three parallel tracks.

## 3.1 Knowledge Track

Build the foundations required to reason correctly about the problem.

Relevant foundations may include:

* logic;
* set theory;
* relations;
* functions;
* probability;
* statistics;
* graph theory;
* algorithms;
* data structures;
* distributed systems;
* operating systems;
* databases;
* networking;
* computer architecture;
* concurrency;
* cryptography;
* information theory;
* control concepts;
* security engineering;
* digital forensics;
* experimental design;
* measurement;
* performance engineering;
* reliability engineering.

Knowledge is introduced because a project problem requires it.

It is not introduced merely to make the project appear sophisticated.

---

## 3.2 Engineering Track

Translate validated understanding into executable capability.

Artifacts may include:

* schemas;
* data models;
* parsers;
* normalizers;
* storage layers;
* state machines;
* algorithms;
* graph models;
* simulation engines;
* replay systems;
* tests;
* benchmarks;
* migrations;
* command-line tools;
* APIs;
* operator surfaces;
* architecture decisions.

Implementation is downstream from semantics.

---

## 3.3 Evidence Track

Produce inspectable evidence showing what was actually established.

Examples include:

* preserved raw inputs;
* test fixtures;
* ground-truth datasets;
* experiment protocols;
* benchmark results;
* failure reports;
* deterministic replay outputs;
* architecture decisions;
* threat models;
* signed commits where configured;
* reviewed pull requests;
* documented limitations;
* reproducible measurements.

A capability claim without evidence remains a hypothesis.

---

# 4. Stage 0 Define the Real Problem

Development begins with a problem, not a technology.

Before implementation, answer:

```text
What is wrong, unknown, missing, unsafe, or unverified?

Why does it matter?

What operational consequence can result?

Which evidence demonstrates that the problem exists?

What assumptions are being made?

What is inside the current scope?

What is explicitly outside the scope?

What result would prove the current idea wrong?

How will success be measured?
```

A problem that cannot be bounded cannot yet be engineered reliably.

---

# 5. Stage 1 Identify the System Boundary

Before defining components, define the boundary.

Questions include:

```text
What enters KORDAXIS?

What leaves KORDAXIS?

Which inputs are assertions?

Which inputs are preserved evidence?

Which components are trusted?

Which components are merely tolerated?

What can an external source control?

What can only KORDAXIS control?

Where does authority change?
```

System boundaries must be explicit because evidence semantics depend on them.

---

# 6. Stage 2 Preserve Before Interpreting

Raw material must be preserved before semantic transformation.

The foundational sequence is:

```text
External Material
       ↓
Exact Raw Bytes
       ↓
Receipt
       ↓
Persistence
       ↓
Parsing
       ↓
Normalization
       ↓
Observation
       ↓
Evidence
       ↓
Claim
       ↓
Reasoning
```

Normalization must never replace raw evidence.

Parsing failure must never destroy raw evidence.

Schema failure must never erase the original input.

Semantic corrections produce new derived state rather than rewriting history.

---

# 7. Stage 3 Distinguish Identity Domains

KORDAXIS must not collapse different identities into one identifier.

Important identity domains may include:

```text
receipt identity
content identity
source event identity
canonical observation identity
entity identity
claim identity
inference identity
decision identity
replay identity
```

For example:

```text
two receipts
≠
two semantic events
```

and:

```text
same exact payload
≠
same receipt
```

and:

```text
same source event identifier
≠
proven same real-world event
```

Identity semantics must be declared before deduplication logic is introduced.

---

# 8. Stage 4 Define Every Field Semantically

A data model is not correct merely because its types compile.

Every important field must answer four questions.

## Semantics

```text
What fact, assertion, state, or relationship does this field represent?
```

## Authority

```text
Who originates it?

Who assigns it?

Who is authoritative for its meaning?
```

## Presence

```text
Can it be unknown?

Can it be absent?

Can it be not applicable?

Can it be invalid?

Are NULL, UNKNOWN, omitted, and empty values distinct?
```

## Replay Determinism

```text
Given identical preserved inputs,
identical versions,
and identical configuration,
must replay produce the same value?
```

A field that cannot answer these questions requires further design.

---

# 9. Stage 5 Model UNKNOWN Explicitly

KORDAXIS must be allowed to conclude:

```text
UNKNOWN
```

UNKNOWN is not:

```text
FALSE
```

UNKNOWN is not:

```text
SAFE
```

UNKNOWN is not automatically:

```text
NULL
```

Possible absence semantics may include:

```text
UNKNOWN
NOT_PROVIDED
NOT_OBSERVED
NOT_COLLECTED
NOT_APPLICABLE
INVALID
UNAVAILABLE
```

These states should only be introduced when the distinction materially affects reasoning.

Complexity must remain proportional to evidence.

---

# 10. Stage 6 Separate Observation From Truth

A canonical observation represents what a source asserted or what a defined observation process produced.

It does not automatically represent ground truth.

Conceptually:

```text
Source Assertion
       ↓
Canonical Observation
       ↓
Evidence Evaluation
       ↓
Claim
```

A canonical observation must remain attributable to:

* the source;
* the raw receipt;
* the transformation;
* the schema;
* the implementation version.

KORDAXIS must be able to answer:

> Where did this observation come from?

---

# 11. Stage 7 Provenance Must Survive Every Transformation

Derived state must remain connected to its inputs.

A target provenance path is:

```text
Decision
    ↓
Simulation
    ↓
Intervention Evaluation
    ↓
Mission Consequence
    ↓
Reachability
    ↓
Claim
    ↓
Evidence
    ↓
Canonical Observation
    ↓
Raw Event Envelope
    ↓
Raw Payload
```

A conclusion that cannot resolve toward preserved inputs has crossed an evidence boundary without attribution.

That is an engineering defect.

---

# 12. Stage 8 Time Is Part of the Evidence Model

KORDAXIS does not assume that one timestamp represents truth.

Relevant concepts may include:

```text
source time
receipt time
persistence time
valid time
knowledge time
derivation time
replay time
```

These values answer different questions.

For example:

```text
When did the source claim the event occurred?
```

is not the same question as:

```text
When did KORDAXIS learn about the event?
```

Temporal uncertainty must not be replaced by false precision.

---

# 13. Stage 9 Preserve Partial Ordering

Equal or unreliable timestamps must not force a fictional total timeline.

Possible relations may eventually include:

```text
BEFORE
AFTER
OVERLAPS
POSSIBLY_CONCURRENT
ORDER_UNKNOWN
```

Deterministic replay ordering may still require a stable processing order.

Processing order and real-world temporal order must remain distinct concepts.

---

# 14. Stage 10 Model Trust as Multidimensional

Trust must not collapse into one number without evidence.

A source may be:

```text
authenticated
```

while also:

```text
incomplete
```

or:

```text
integrity-preserved
```

while:

```text
semantically unreliable
```

or:

```text
healthy
```

while:

```text
incapable of observing the required phenomenon
```

Relevant dimensions may include:

* identity;
* integrity;
* capability;
* freshness;
* health;
* coverage;
* independence;
* transformation history.

Trust models must explain what each dimension means.

---

# 15. Stage 11 Silence Requires an Observation Model

No event observed does not automatically mean no event occurred.

Before silence becomes negative evidence, KORDAXIS must ask:

```text
Was the sensor active?

Was the sensor healthy?

Could the sensor observe this event class?

Was collection complete?

Was the relevant interval covered?

Could events have been dropped?

Was ingestion delayed?

Was the source stale?
```

If these questions cannot be answered, silence may remain UNKNOWN.

---

# 16. Stage 12 Competing Hypotheses Remain First-Class

Reasoning must preserve alternative explanations when evidence does not justify collapsing them.

Conceptually:

```text
H1
supported by E1, E2

H2
supported by E3

H3
consistent with current blind spot
```

New evidence may:

* strengthen a hypothesis;
* weaken it;
* contradict it;
* eliminate it;
* or leave the ranking unchanged.

The system must not silently delete inconvenient alternatives.

---

# 17. Stage 13 Reachability Is Not Mission Consequence

A path may be technically reachable without creating material mission impact.

KORDAXIS therefore separates:

```text
technical capability
```

from:

```text
mission consequence
```

The intended reasoning sequence is closer to:

```text
Identity
   ↓
Authority
   ↓
Reachability
   ↓
Resource
   ↓
Dependency
   ↓
Mission Capability
   ↓
Consequence
```

This boundary must remain explicit.

---

# 18. Stage 14 Intervention Requires Counterfactual Reasoning

A defensive intervention is not automatically good because it removes a path.

An intervention may also:

* break legitimate workflows;
* remove observability;
* destroy evidence;
* create operational downtime;
* move risk elsewhere;
* introduce new trust dependencies.

Evaluation must therefore consider both:

```text
security effect
```

and:

```text
mission effect
```

where the model supports such conclusions.

---

# 19. Stage 15 Decision Is Separate From Recommendation

KORDAXIS must distinguish:

```text
candidate action
```

from:

```text
evaluated intervention
```

from:

```text
recommended action
```

from:

```text
authorized action
```

from:

```text
executed action
```

A reasoning engine does not gain execution authority merely because it produced a high-scoring option.

---

# 20. Stage 16 Replay Is a Core Capability

Replay is not a debugging convenience.

It is part of the evidence model.

A reproducible result should be a function of declared inputs such as:

```text
preserved evidence
schema versions
parser versions
normalizer versions
policy versions
model versions
solver versions
configuration
seeds
stable ordering rules
```

Conceptually:

```text
output =
F(
    evidence,
    versions,
    configuration
)
```

Identical semantic inputs under identical declared versions should produce identical semantic output.

---

# 21. Stage 17 Nondeterminism Must Be Declared

Derived state must not silently depend on:

```text
now()
random()
current network state
unversioned external APIs
ambient filesystem state
implicit environment variables
machine-local configuration
```

If nondeterminism is necessary, its source must be explicit and recorded where reproducibility requires it.

---

# 22. Stage 18 Microexperiment Before Architecture Expansion

When a semantic question can be tested with a small controlled experiment, prefer the experiment over new infrastructure.

For example:

```text
complete telemetry
vs
delayed telemetry
vs
lost telemetry
vs
duplicate telemetry
```

may teach more than introducing another service.

A microexperiment should ideally be:

* bounded;
* deterministic;
* reproducible;
* measurable;
* falsifiable;
* safe;
* understandable end-to-end.

---

# 23. Stage 19 Complexity Requires Evidence

KORDAXIS does not adopt infrastructure because it is fashionable.

The initial architecture deliberately avoids unnecessary:

```text
microservices
message brokers
graph databases
caches
orchestration systems
distributed coordination
```

A dedicated component should enter the architecture only when a measured requirement justifies it.

Examples include:

```text
measured throughput limitation
measured query limitation
measured memory pressure
measured coordination requirement
measured fault-isolation need
```

Architecture is an engineering response, not portfolio decoration.

---

# 24. Stage 20 Test the Invariant

Tests should prove properties, not screenshots.

Questions may include:

```text
Can raw evidence be modified?

Can parser failure destroy evidence?

Can duplicate delivery erase receipt history?

Can duplicate material double-count semantic state?

Can UNKNOWN become SAFE?

Can source silence become false negative evidence?

Can an untrusted source preserve an unjustified strong claim?

Can equal timestamps break replay determinism?

Can stale state appear current?

Can an intervention bypass the safety boundary?

Can replay change semantic output without a declared version change?
```

Happy-path tests are necessary but insufficient.

---

# 25. Stage 21 Match the Test Technique to the Failure Mode

Available techniques may include:

* unit testing;
* integration testing;
* database constraint testing;
* negative testing;
* property-based testing;
* fuzzing;
* differential testing;
* concurrency testing;
* fault injection;
* corruption testing;
* deterministic replay testing;
* benchmark comparison;
* controlled ground-truth experiments.

The test method should be selected because it exposes the relevant failure mode.

---

# 26. Stage 22 Debugging Is Hypothesis Testing

Debugging follows:

```text
Observed Failure
      ↓
Bound the Failure
      ↓
Form Hypothesis
      ↓
Create Discriminating Test
      ↓
Collect Evidence
      ↓
Reject / Retain Hypothesis
      ↓
Identify Cause
      ↓
Fix
      ↓
Regression Test
```

Changing code until the error disappears is not sufficient.

The explanation matters.

---

# 27. Stage 23 Measure Before Performance Claims

Words such as:

```text
fast
low-latency
real-time
efficient
scalable
high-throughput
```

require measurement.

Measurements may include:

* ingest throughput;
* persistence latency;
* normalization latency;
* replay duration;
* graph reconstruction latency;
* solver latency;
* query latency;
* CPU usage;
* memory usage;
* storage amplification;
* event-loss tolerance;
* recovery duration.

No optimization is justified merely because code “looks slow.”

---

# 28. Stage 24 Benchmark Against an Oracle Where Possible

Generation-0 uses synthetic ground truth deliberately.

The system under test must not receive that ground truth during inference.

After inference, results may be compared with the oracle.

Possible metrics include:

* evidence-lineage coverage;
* observation correctness;
* temporal reconstruction quality;
* authority-path correctness;
* reachability correctness;
* mission-impact correctness;
* intervention effectiveness;
* replay determinism;
* decision reproducibility.

Internal scores must not be described as probabilities without calibration evidence.

---

# 29. Stage 25 Negative Results Are Engineering Results

A failed hypothesis may still create valuable knowledge.

Valid gate outcomes include:

```text
ADVANCE
REVISE
REPEAT
REJECT
UNKNOWN
```

A failed experiment is not repaired by hiding it behind more complexity.

The result should change the model.

---

# 30. Stage 26 Cross-Examine Every Material Change

Before merge, challenge the implementation as if its author were wrong.

Ask:

```text
Is the semantic model correct?

Is the claim stronger than the evidence?

What happens under malformed input?

What happens under duplicated input?

What happens under delayed input?

What happens under stale input?

What happens under contradictory evidence?

What happens when a sensor is degraded?

Can provenance break?

Can history be rewritten?

Can UNKNOWN disappear?

Can replay diverge?

Can a trust boundary be bypassed?

Can the design be simpler?
```

Review should create friction when the evidence is weak.

---

# 31. Stage 27 Git and GitHub Lifecycle

Substantive KORDAXIS work should normally follow:

```text
Problem
   ↓
Issue when durable tracking is justified
   ↓
Research / Design
   ↓
Dedicated Branch
   ↓
Implementation
   ↓
Tests / Experiments
   ↓
Local Diff Review
   ↓
Commit
   ↓
Push
   ↓
Pull Request
   ↓
CI
   ↓
Cross-Examination
   ↓
Merge
```

Issues are intentionally sparse.

Create them for:

* meaningful engineering objectives;
* architectural changes;
* important defects;
* security concerns;
* benchmark gaps;
* substantial research questions.

Do not create issues merely for:

* typo fixes;
* formatting;
* routine README edits;
* tiny housekeeping tasks.

Commit volume is not an engineering metric.

---

# 32. Stage 28 VS Code and Terminal Responsibilities

Project source files are authored and edited in **VS Code**.

The terminal is used for:

* Git operations;
* test execution;
* dependency installation;
* environment management;
* database commands;
* static analysis;
* debugging;
* profiling;
* inspecting generated outputs.

Code must not be pasted without understanding.

Each important line should eventually be explainable in terms of:

* syntax;
* type behavior;
* runtime behavior;
* control flow;
* failure behavior;
* memory behavior where relevant;
* security implications;
* performance implications where relevant;
* relationship to system invariants.

---

# 33. Stage 29 Learning Must Transfer

Understanding is periodically tested through three modes.

## Recall

Explain the concept without copying the implementation.

## Transfer

Apply the concept to a different system or failure mode.

## Reconstruction

Rebuild a small version from first principles.

Implementation familiarity is not sufficient if the concept cannot survive transfer.

---

# 34. Stage 30 Operator Surface Is a Projection

The future KORDAXIS platform/dashboard is not the source of truth.

It is a projection of authoritative evidence and derived state.

Candidate surfaces may eventually include:

* evidence provenance;
* observability health;
* temporal reconstruction;
* competing hypotheses;
* authority graphs;
* reachability;
* mission impact;
* intervention simulation;
* decision receipts;
* deterministic replay.

A visually convincing interface cannot substitute for an unproven reasoning layer.

---

# 35. Stage 31 Cross-Repository Integration

KORDAXIS may consume outputs from other systems.

Integration must occur through explicit contracts.

The preferred model is:

```text
External Repository
        ↓
Versioned Contract
        ↓
KORDAXIS Trust Boundary
        ↓
Raw Preservation
        ↓
Adapter
        ↓
Canonical Representation
        ↓
Reasoning
```

Repositories must not become tightly coupled through hidden shared internal state.

---

# 36. ELENCHION Integration Principle

ELENCHION is a candidate external evidence-producing system.

Conceptually:

```text
ELENCHION
execution-level evidence-bounded knowledge
        ↓
versioned interchange contract
        ↓
KORDAXIS
environment / authority / mission reasoning
```

KORDAXIS must not silently promote ELENCHION output to ground truth.

Producer identity, version, provenance, uncertainty, and trust boundaries must remain explicit.

---

# 37. Stage 32 Repository Interface Discipline

A system participating in the future ecosystem should be able to state:

```text
I PRODUCE
What information or capability do I emit?

I CONSUME
Which external contracts can I accept?

I GUARANTEE
Which properties can downstream systems rely on?

I DO NOT GUARANTEE
Which interpretations remain outside my authority?
```

This is preferred over implicit dependency.

---

# 38. Stage 33 Security Boundary

KORDAXIS is developed as defensive and controlled research infrastructure.

Development must not silently expand into:

* real-world offensive exploitation;
* credential theft;
* malware deployment;
* destructive actions;
* autonomous real-target remediation;
* unauthorized scanning;
* offensive persistence;
* command-and-control capability.

Synthetic or controlled environments are preferred for adversarial scenarios.

---

# 39. Stage 34 Human Authority Remains First-Class

Automation may:

* reconstruct;
* compare;
* score;
* simulate;
* identify uncertainty;
* propose interventions.

Automation does not automatically gain authority to perform high-impact external actions.

Action authority must remain an explicit system boundary.

---

# 40. Stage 35 Engineering Evidence Before Portfolio Claims

The repository is treated as public engineering evidence.

Portfolio strength should emerge from:

```text
problem importance
×
technical depth
×
semantic correctness
×
experimental evidence
×
reproducibility
×
security discipline
×
measurement
×
review quality
×
communication
```

Not from:

```text
commit count
repository count
feature count
framework count
dashboard complexity
```

---

# 41. Stage 36 Current Generation-0 Application

The current development sequence is:

```text
Exact Raw Bytes
      ↓
Raw Evidence Persistence
      ↓
Canonical Observation
      ↓
Provenance
      ↓
Temporal Knowledge
      ↓
Trust / Observability
      ↓
Claims / Hypotheses
      ↓
Authority
      ↓
Reachability
      ↓
Mission Consequence
      ↓
Intervention
      ↓
Safety
      ↓
Decision Receipt
      ↓
Deterministic Replay
      ↓
Operator Platform
```

Each layer must establish the contracts required by the layer above it.

---

# 42. Current Gate Canonical Observation

The current engineering question is:

> How can source-specific assertions be converted into a deterministic canonical representation without destroying raw evidence, manufacturing certainty, or breaking provenance?

Prerequisites include:

```text
bytes
serialization
parsing
schemas
data modeling
identity
semantic normalization
time
provenance
UNKNOWN semantics
determinism
versioning
```

The implementation must eventually demonstrate:

```text
raw evidence remains unchanged

malformed input fails explicitly

normalization remains deterministic

observation lineage resolves to raw evidence

source assertion is not promoted to truth

duplicate receipts do not automatically double-count semantics

schema/version changes remain attributable
```

---

# 43. Canonical Observation Review Questions

Before the model is finalized, every important field should answer:

```text
What does this field mean?

Who originates it?

Who assigns it?

Who is authoritative?

Can it be UNKNOWN?

Can it be omitted?

Can it be invalid?

Is absence meaningful?

Must replay reproduce it?

Which input determines it?

Which version determines its semantics?
```

If those answers remain ambiguous, implementation is premature.

---

# 44. Definition of Engineering Progress

A development session has produced meaningful progress when at least one of the following becomes stronger:

* understanding;
* specification;
* evidence;
* implementation;
* testing;
* measurement;
* reproducibility;
* security;
* architecture clarity;
* failure understanding.

A commit is not required for every learning session.

A commit is justified when the repository has gained durable engineering value.

---

# 45. Final Rule

KORDAXIS development follows one overriding discipline:

> **Never manufacture certainty that the evidence does not support.**

The system must preserve the distinction between different state dimensions rather than inventing one universal status vocabulary.

Claim classification remains governed by the versioned epistemic model.

Observability, source health, trust, reachability, mission state, and authorization remain separate domains with their own semantics.

For example, degraded observability does not automatically mean that a claim is contradicted, and a strong claim classification does not imply healthy observation coverage.

`UNKNOWN` remains a first-class result wherever available evidence does not justify a stronger conclusion.

The same discipline applies to the engineering process itself.

We do not claim capability because code exists.

We claim capability only when the relevant behavior is understood, tested, measured where necessary, reproducible within declared versions, and supported by evidence.
