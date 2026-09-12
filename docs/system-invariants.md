# System Invariants

These are architecture-level rules, not optional features.

## INV-01 Evidence lineage
No material conclusion exists without machine-resolvable evidence lineage.

## INV-02 Immutable knowledge history
New knowledge may supersede previous knowledge. It may never silently rewrite what the system previously believed.

## INV-03 Bitemporal truth
World-valid time and system-knowledge time are distinct.

## INV-04 Unknown is first-class
UNKNOWN must never collapse to SAFE.

## INV-05 Silence requires an observation model
Missing data becomes meaningful only when an expected observation, heartbeat, or coverage model exists.

## INV-06 Source trust is multidimensional
No telemetry producer is reduced to one universal trust score.

## INV-07 Derived state is rebuildable
Projections, claims, hypotheses, graph state, and decision-support outputs must be reproducible from preserved inputs and versioned logic.

## INV-08 AI is non-authoritative
AI-generated text cannot independently become canonical fact.

## INV-09 Controlled action is constrained
Material defensive actions require explicit policy, evidence, and authorization conditions.

## INV-10 Replay is side-effect free
Historical replay uses simulation boundaries and cannot perform external changes.

## INV-11 Reproducibility is version-bound
Replay records schema, code, policy, model, solver, scenario seed, and deterministic configuration versions.

## INV-12 Mission consequence differs from technical reachability
Reachable does not mean mission-critical; compromised does not automatically mean mission failure.

## INV-13 Provenance is not semantic truth
Integrity and origin evidence do not prove that an assertion is correct.

## INV-14 Decisions are attributable
Every material decision must resolve to its world-state version, evidence, policy, simulation, approval state, and result.
