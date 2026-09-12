# KORDAXIS

## Evidence-Native Cyber Mission Reasoning & Decision System

KORDAXIS is an engineering research system for reasoning about cyber environments when telemetry is incomplete, delayed, contradictory, degraded, or potentially manipulated.

It is not a SIEM, SOC dashboard, attack-graph visualization product, or LLM wrapper.

KORDAXIS exists to answer a harder question:

> What can a defender justifiably conclude, what remains uncertain, what can an adversary still reach, what mission consequences follow, and which intervention reduces the greatest risk with the least operational disruption?

## Thesis

KORDAXIS maintains an uncertainty-aware temporal model of a cyber environment, reconstructs adversary operations from imperfect evidence, computes reachable attack transitions and mission consequences, and evaluates defensive interventions before execution.

## Doctrine

**OBSERVE.**  
**PRESERVE.**  
**CORROBORATE.**  
**CHALLENGE.**  
**RECONSTRUCT.**  
**COMPUTE.**  
**SIMULATE.**  
**CONSTRAIN.**  
**DECIDE.**  
**PROVE.**

## Generation 0

Generation 0 intentionally focuses on one deep synthetic incident spanning human identity, Git, CI/CD, cloud authority, artifact lineage, workload identity, production resources, mission dependencies, and degraded telemetry.

The system must prove immutable evidence ingestion, provenance-preserving normalization, bitemporal reconstruction, telemetry degradation detection, competing hypotheses, authority reasoning, attack reachability, mission consequence propagation, defensive intervention analysis, counterfactual simulation, safety-gated decisions, decision receipts, and deterministic replay.

A convincing UI is not evidence.

## Core invariants

1. No material conclusion without evidence lineage.
2. Historical knowledge is never silently rewritten.
3. UNKNOWN is never silently converted to SAFE.
4. Missing telemetry never automatically lowers risk.
5. AI output is never ground truth by itself.
6. Critical actions require explicit authorization and safety conditions.
7. Derived state must be reproducible from preserved evidence and versioned logic.
8. Mission consequence is distinct from technical reachability.
9. Cryptographic provenance proves origin/integrity, not semantic truth.
10. Complexity requires evidence.

## Repository discipline

`main` is the authoritative integration branch. After bootstrap, material changes enter `main` through pull requests.

Issues are reserved for meaningful engineering work: measurable defects, architectural changes, research questions that affect implementation, benchmark gaps, and significant security properties.

Security vulnerabilities must not be disclosed through public issues. See [SECURITY.md](SECURITY.md).

## Status

**Generation 0 — Foundation**
