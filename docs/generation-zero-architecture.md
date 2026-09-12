# Generation-0 Architecture

Generation 0 is a modular monolith optimized for semantic correctness, deterministic replay, and scientific evaluation.

## Authoritative persistence
PostgreSQL is the initial authoritative persistence layer.

Raw evidence and derived state remain logically separated even if they share one database instance.

## Initial modules

- ingest — source adapters and raw envelope creation
- normalize — canonical observation mapping
- provenance — hashes, lineage, and evidence references
- temporal — bitemporal state projection
- trust — telemetry health and source-quality dimensions
- epistemic — claims, contradictions, expected evidence, and hypotheses
- authority — principals, delegation, and effective authority
- reachability — transition feasibility and reachable-state computation
- reconstruction — operation hypothesis assembly
- mission — mission dependencies and consequence propagation
- intervention — candidate controls and path-reduction analysis
- simulation — counterfactual state projection
- safety — evidence, policy, authorization, and mission gates
- receipt — attributable decision records
- replay — deterministic reconstruction
- range — synthetic scenarios and ground-truth generation

## Explicit exclusions
Generation 0 does not require Kafka, Neo4j, Redis, Kubernetes, Elasticsearch, or microservices.

## Graph strategy
Canonical relations are persisted in PostgreSQL. Computation may use deterministic in-memory graph snapshots initially.

A dedicated graph database requires benchmark evidence that indexing, query redesign, and in-process algorithms cannot satisfy representative requirements.

## Messaging strategy
No message broker is introduced before measured throughput, durability, backpressure, or decoupling requirements demand it.

## Failure principle
Every component must expose failure or degradation explicitly. A subsystem failure must not leave the overall system appearing fully healthy.
