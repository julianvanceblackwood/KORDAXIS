# External Evaluation Brief

**Status:** Generation Zero research. The raw-evidence boundary is implemented; canonical observations and later reasoning layers remain research or planned work.

## The decision problem

Security teams can be asked to justify intervention using fragmented, late or conflicting telemetry. KORDAXIS researches how to preserve the original evidence, distinguish observation from inference and keep uncertainty visible through reconstruction and decision support.

## What can be evaluated today

The implemented slice preserves exact payload bytes, records distinct receipts, computes SHA-256 content identities, persists raw evidence in PostgreSQL, orders ingestion and checks integrity on reconstruction. Unit tests and PostgreSQL integration tests cover that boundary.

The implemented system does **not** yet establish the full evidence-to-decision pipeline described by the thesis. Begin with [the implementation status](../README.md#what-exists-today), [generation-zero architecture](generation-zero-architecture.md), [system invariants](system-invariants.md), and [acceptance tests](acceptance-tests.md).

## Review questions

1. Can two receipts share identical content without losing their distinct collection histories?
2. Does reconstruction retain original bytes and independently detect corrupted persisted payloads?
3. Which append-only guarantees survive normal application access, and which do not survive privileged database access?
4. Can the proposed canonical observation model preserve source attribution, parser failure, versioning and UNKNOWN without silently strengthening a claim?
5. How will withheld synthetic ground truth and [benchmark methodology](benchmark-methodology.md) distinguish useful inference from confident but unsupported output?

## What would count as progress

- A documented, executable canonical-observation contract with explicit failure and unknown states.
- Replay tests tying normalized assertions to preserved source receipts.
- Controlled cases covering source disagreement, missing telemetry and incorrect event ordering.
- Independent reproduction of a stated capability under recorded test conditions.

These are future acceptance criteria, not completed capabilities.

## Boundaries and engagement

KORDAXIS is defensive research, not a production SOC, autonomous response engine or an offensive testing service. Do not submit customer logs, credentials or sensitive incident evidence to public issues. Follow [SECURITY.md](../SECURITY.md) for vulnerability reporting.

Independent test cases, semantic counterexamples, evidence-lineage reviews and evaluation-methodology feedback are useful. Provide a minimal reproducer, environment, revision and expected versus observed behavior where possible. For non-public collaboration, use the contact route on the [research profile](https://github.com/julianvanceblackwood). No existing customer, sponsor, deployment or institutional endorsement is implied. Public visibility alone does not establish reuse or commercial licensing rights.
