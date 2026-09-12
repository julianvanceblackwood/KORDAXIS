# Event and Evidence Model

KORDAXIS separates transport facts, normalized observations, preserved evidence, semantic claims, and inference records.

## RawEventEnvelope
Represents material received from a producer.

Required semantics:
- event_id
- source_id
- source_event_id when available
- source_timestamp when supplied
- received_at
- raw_payload_hash
- raw_payload_reference
- schema_hint
- ingest_version

The raw envelope is immutable.

## Observation
A normalized representation of what a source asserted.

An Observation is not KORDAXIS truth. It records a source assertion with normalization metadata.

## Evidence
Evidence binds one or more preserved observations or artifacts with integrity and provenance metadata.

Relevant dimensions include origin, collection method, content hash, temporal quality, independence group, retention reference, and known impairment.

## Claim
A testable semantic proposition.

Claims link supporting evidence, contradicting evidence, assumptions, derivation, expected-but-missing evidence, coverage gaps, and classification state.

## InferenceRecord
Records how a derived object was produced.

At minimum it identifies inference type, implementation/version, input object identifiers, parameters, and output identifiers.

## Hypothesis
A hypothesis is a machine-evaluable set of compatible claims and assumptions. Narrative text may explain it, but prose is never the authoritative representation.

## Non-destructive normalization
Normalization never overwrites raw evidence. Corrections create new derived representations and explicit supersession relationships.
