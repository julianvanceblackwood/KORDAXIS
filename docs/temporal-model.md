# Temporal Model

KORDAXIS is bitemporal because event time alone cannot answer what the system knew at a historical moment.

## Valid time
Represents when a state or relationship was believed to be true in the modeled cyber environment.

Core fields:
- valid_from
- valid_to

Unless a domain contract explicitly states otherwise, intervals use half-open semantics: `[valid_from, valid_to)`.

## Knowledge time
Represents when KORDAXIS learned, recorded, or superseded that belief.

Core fields:
- recorded_at
- superseded_at

Knowledge intervals likewise use explicit interval semantics and may not be inferred from wall-clock ordering alone.

## Observation time
`observed_at` records the semantically normalized time at which a producer claims the observation occurred. The original source timestamp remains preserved in the raw envelope.

## Receipt time
`received_at` records when KORDAXIS received the material.

Observation, receipt, valid, and knowledge time are not interchangeable.

## Canonical time representation
Generation 0 stores canonical timestamps as timezone-aware UTC instants. Original source timestamp representation is preserved with raw evidence when needed for forensic interpretation.

## Deterministic ordering
Timestamps alone are not a total ordering mechanism. Two records may share a timestamp or arrive with unreliable clocks.

Replay therefore uses a declared stable ordering key. Generation 0 preserves `ingest_sequence` on raw receipt envelopes and records any later deterministic tie-break rules as versioned replay policy.

Source time never silently overrides receipt order when clocks disagree.

## Required queries
The temporal layer must support at least:

1. What do we currently believe was true at time T?
2. What did KORDAXIS believe at knowledge time K about world time T?
3. When was an observation reportedly produced?
4. When did KORDAXIS receive it?
5. Which later evidence superseded an earlier belief?

## Replay constraint
Historical replay uses preserved ordering keys plus versioned schemas, policies, inference logic, solver configuration, and scenario seeds. A replay result is reproducible only within those declared versions.

## Correction rule
Late or corrected evidence may change current reconstruction of historical valid time, but must never erase the previous knowledge state.
