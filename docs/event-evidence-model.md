# Event and Evidence Model

KORDAXIS separates raw transport material, receipt identity, normalized observations, evidence, claims, and inference records.

The raw evidence boundary is authoritative for what KORDAXIS received. It is not authoritative for whether an external assertion is true.

## RawPayload

RawPayload represents exact immutable payload bytes and their content identity.

Current domain fields:

- content: exact bytes received at the evidence boundary
- sha256: SHA-256 digest of those exact bytes

size_bytes is derived from content.

The digest is content identity and an integrity check. It is not a trust score and does not prove semantic correctness.

Parsing, JSON key ordering, whitespace normalization, transcoding, or schema normalization must never change the bytes used to calculate the raw payload digest.

## RawEventDraft

RawEventDraft represents one receipt episode before persistence assigns authoritative ingest order.

Current fields:

- envelope_id
- source_id
- source_event_id, optional
- source_timestamp, optional
- received_at
- media_type
- payload
- ingest_contract_version

envelope_id is KORDAXIS receipt identity.

source_event_id is an external source assertion when supplied. It is not KORDAXIS receipt identity and is not assumed to be globally unique or truthful.

source_timestamp is source-reported time. It is not KORDAXIS receipt time and is not an ordering authority when clocks disagree.

received_at is the time KORDAXIS received the material and must be timezone-aware.

media_type describes the received representation. It is receipt metadata and is not part of payload content identity.

## RawEventEnvelope

RawEventEnvelope is the persisted immutable receipt episode.

It contains the RawEventDraft fields and adds:

- ingest_sequence

ingest_sequence is assigned by authoritative persistence and must be positive.

Generation 0 uses the deterministic receipt ordering key:

~~~text
(ingest_sequence, envelope_id)
~~~

This ordering supports replay. It does not claim to reconstruct real-world event order.

## Persistence contract

Generation 0 stores raw evidence in two append-only PostgreSQL tables.

### raw_payloads

Stores payload content once per SHA-256 identity.

Material fields include:

- sha256
- content
- generated size_bytes
- first_persisted_at

### raw_event_envelopes

Stores receipt metadata and references payload content by payload_sha256.

Material fields include:

- envelope_id
- source_id
- source_event_id
- source_timestamp
- received_at
- media_type
- ingest_sequence
- payload_sha256
- ingest_contract_version
- persisted_at

Payload persistence and receipt persistence occur in one transaction.

Database constraints verify the raw SHA-256 digest against stored content and reject UPDATE, DELETE, and TRUNCATE operations on raw evidence tables through the normal application path.

These controls establish append-only behavior for Generation 0. They are not a claim of immutability against a sufficiently privileged database owner or superuser.

## Duplicate delivery

Receipt identity, payload identity, source event identity, and future semantic observation identity are separate domains.

Repeated delivery of the same payload does not erase receipt history.

Two receipt episodes may reference the same payload SHA-256 while retaining independent receipt metadata and ingest order.

Conceptually:

~~~text
same payload
≠
same receipt

same source_event_id
≠
same receipt

two receipts
≠
two semantic observations
~~~

Semantic deduplication is downstream from raw evidence preservation.

## Observation

An Observation is a normalized representation of what a source asserted or what a defined observation process produced.

An Observation is not KORDAXIS truth.

Every material Observation must remain attributable to preserved raw evidence and the versioned transformation that produced it.

The Canonical Observation contract is the current Generation-0 engineering gate and is not finalized by this document.

## Evidence

Evidence binds preserved observations or artifacts with integrity, provenance, temporal, collection, and impairment context.

Relevant dimensions may include:

- origin
- collection method
- content identity
- temporal quality
- source capability
- source health
- correlation or shared failure domain
- retention reference
- known impairment

Evidence quality and semantic truth remain separate questions.

## Claim

A Claim is a testable semantic proposition.

Claims may reference:

- supporting evidence
- contradicting evidence
- assumptions
- derivation
- expected-but-missing evidence
- coverage gaps
- versioned classification state

A claim classification is derived under versioned policy. It is not immutable truth.

## InferenceRecord

InferenceRecord describes how derived state was produced.

At minimum, a material inference record identifies:

- inference type
- implementation or logic version
- ordered input identifiers where ordering matters
- parameters or configuration that affect semantics
- output identifiers

The purpose is reproducibility and attribution.

## Hypothesis

A Hypothesis is a machine-evaluable set of compatible claims and assumptions.

Narrative text may explain a hypothesis. Prose is never the authoritative machine representation.

Competing hypotheses remain available while evidence is insufficient to eliminate them.

## Non-destructive derivation

Normalization, correction, and later reasoning never overwrite raw evidence.

Corrections create new derived representations or explicit supersession relationships.

The required lineage direction is:

~~~text
Derived State
    ↓
Observation
    ↓
RawEventEnvelope
    ↓
RawPayload
~~~

A material derived object that cannot resolve to its preserved inputs violates the evidence-lineage invariant.
