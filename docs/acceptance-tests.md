# Generation-0 Acceptance Tests

Generation 0 passes only when its material claims have automated evidence.

## AT-001 Immutable ingestion
The same exact raw payload bytes produce the same raw payload hash. Parsing or normalization cannot change the preserved raw digest.

## AT-002 Schema rejection
Malformed input cannot enter canonical projection without an explicit failure state.

## AT-003 Bitemporal reconstruction
Fixtures reproduce both world-at-T and knowledge-at-K expectations using declared interval semantics.

## AT-004 Evidence lineage
Every material claim resolves to preserved evidence and versioned inference records.

## AT-005 Missing telemetry
Loss of an expected heartbeat or coverage interval produces degraded observability rather than a safe conclusion.

## AT-006 Authority graph
Effective-authority paths match the scenario oracle.

## AT-007 Authority drift
A newly possible indirect capability is detected even when no direct privilege was added to the final resource.

## AT-008 Reachability
Known reachable, unreachable, possible, and unknown transitions match the scenario oracle.

## AT-009 Hypothesis competition
Contradictory evidence changes hypothesis state without silently deleting plausible alternatives.

## AT-010 Supply-chain lineage
Expected artifact/provenance inconsistencies are detected.

## AT-011 Mission propagation
Mission consequence matches declared dependency semantics.

## AT-012 Intervention baseline
For bounded small graphs where exhaustive evaluation is practical, the solver output matches the known optimum under the declared cost model.

## AT-013 Counterfactual validity
Changing a modeled precondition only suppresses downstream transitions that depend on that precondition or its consequences.

## AT-014 Safety gate
Low-evidence, high-mission-impact action candidates cannot cross the automated-response boundary.

## AT-015 Decision receipt
Every material decision receipt includes required evidence references, versions, simulation result, authorization state, and outcome fields.

## AT-016 Deterministic replay
Identical preserved evidence, ingest ordering, schema versions, code version, policy versions, solver configuration, and seeds produce the same canonical semantic output digest.

Execution-specific metadata such as benchmark run identifier or wall-clock duration is excluded from the semantic digest and is validated separately.

## AT-017 Degraded mode
Loss or staleness of a required capability changes explicit capability-health state.

## AT-018 Duplicate preservation
Repeated delivery of the same source material does not destroy receipt history and does not double-count the semantic observation after deduplication rules are applied.

## AT-019 Ordering collision
Records with equal source or receipt timestamps replay deterministically according to preserved ordering keys and versioned tie-break policy.
