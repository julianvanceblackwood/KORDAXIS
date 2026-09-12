# Event and Evidence Model

KORDAXIS separates transport facts, normalized observations, preserved evidence, semantic claims, and inference records.

## RawEventEnvelope
Represents one receipt episode for material delivered by a producer.

Required semantics:
- event_id — KORDAXIS identifier for this receipt episode
- ingest_sequence — stable replay-order key assigned at ingestion
- source_id
- source_event_id when supplied
- source_timestamp when supplied
- received_at
- raw_payload_hash
- raw_payload_reference
- raw_media_type when known
- schema_hint
- ingest_version

The raw envelope is immutable.

`raw_payload_hash` is calculated from the exact preserved payload bytes received at the evidence boundary. Parsing, JSON key ordering, whitespace normalization, character transcoding, or schema normalization must not alter the bytes used for this hash.

If a normalized representation requires a separate digest, that digest is stored separately and must never replace `raw_payload_hash`.

## Duplicate delivery
Repeated delivery does not silently delete evidence. Multiple receipt episodes may reference the same payload hash and source event identifier while preserving their own receipt metadata. Deduplication is a projection/query concern, not destruction of evidence history.

## Observation
A normalized representation of what a source asserted.

An Observation is not KORDAXIS truth. It records a source assertion together with normalization metadata and a reference to the source envelope.

## Evidence
Evidence binds one or more preserved observations or artifacts with integrity and provenance metadata.

Relevant dimensions include origin, collection method, content hash, temporal quality, independence/correlation domains, retention reference, and known impairment.

## Claim
A testable semantic proposition.

Claims link supporting evidence, contradicting evidence, assumptions, derivation, expected-but-missing evidence, coverage gaps, and classification state.

## InferenceRecord
Records how a derived object was produced.

At minimum it identifies inference type, implementation/version, ordered input object identifiers where ordering is material, parameters, and output identifiers.

## Hypothesis
A hypothesis is a machine-evaluable set of compatible claims and assumptions. Narrative text may explain it, but prose is never the authoritative representation.

## Non-destructive normalization
Normalization never overwrites raw evidence. Corrections create new derived representations and explicit supersession relationships.
