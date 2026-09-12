# Temporal Model

KORDAXIS is bitemporal because event time alone cannot answer what the system knew at a historical moment.

## Valid time
Represents when a state or relationship was believed to be true in the modeled cyber environment.

Core fields:
- valid_from
- valid_to

## Knowledge time
Represents when KORDAXIS learned, recorded, or superseded that belief.

Core fields:
- recorded_at
- superseded_at

## Observation time
`observed_at` records when a producer claims the observation occurred.

## Receipt time
`received_at` records when KORDAXIS received the material.

Observation, receipt, valid, and knowledge time are not interchangeable.

## Required queries
The temporal layer must support at least:

1. What do we currently believe was true at time T?
2. What did KORDAXIS believe at knowledge time K about world time T?
3. When was an observation reportedly produced?
4. When did KORDAXIS receive it?
5. Which later evidence superseded an earlier belief?

## Replay constraint
Historical replay uses explicit ordering rules and versioned schemas, policies, inference logic, solver configuration, and scenario seeds. A replay result is reproducible only within those declared versions.

## Correction rule
Late or corrected evidence may change current reconstruction of historical valid time, but must never erase the previous knowledge state.
