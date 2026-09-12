# ADR-0001 — Generation-Zero Architecture

## Status

Accepted

## Context

KORDAXIS Generation 0 must demonstrate immutable evidence ingestion, temporal state reconstruction, epistemic reasoning, identity and authority graphs, attack reachability, mission propagation, defensive intervention analysis, counterfactual simulation, and deterministic replay.

At this stage there is no measured requirement for independently scalable services, distributed event streaming, dedicated graph persistence, or distributed orchestration.

Adding those components before a demonstrated need would increase failure modes without proving a corresponding capability.

## Decision

Generation 0 will use a modular architecture with one repository, one primary application boundary, PostgreSQL as authoritative persistence, append-only evidence records, versioned schemas, rebuildable derived projections, and deterministic in-process graph algorithms where practical.

Generation 0 will not initially require Kafka, Neo4j, Redis, Kubernetes, microservices, or a dedicated search cluster.

## Rationale

The primary Generation-0 risks are semantic and correctness risks: incorrect evidence lineage, invalid temporal reconstruction, unjustified certainty, incorrect authority propagation, false attack paths, incorrect counterfactuals, and non-deterministic replay.

Distributed-system complexity does not solve these problems.

## Exit criteria

A dedicated graph store may be proposed when representative benchmark workloads demonstrate that the existing model cannot meet required graph-query objectives after reasonable indexing and algorithmic optimization.

A message broker may be proposed when measured ingestion, durability, backpressure, or producer-decoupling requirements cannot be satisfied by the existing design.

A service may be extracted when an independent operational boundary is demonstrated.

Complexity requires evidence.
