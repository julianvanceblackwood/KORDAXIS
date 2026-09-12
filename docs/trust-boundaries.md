# Trust Boundaries

KORDAXIS models trust changes explicitly. Authentic transport does not imply semantic truth.

## TB-0 External sources
Identity, Git, CI, cloud, workload, sensor, and intelligence systems are external assertion producers.

## TB-1 Ingestion
Preserve original payloads, source identity, source timestamp, receipt timestamp, schema outcome, and content hash. Parser failures remain visible.

## TB-2 Evidence
Raw evidence is append-only. Normalized representations never replace original material. Every material derivation must resolve to evidence or a versioned inference.

## TB-3 Reasoning
World-state projections, claims, hypotheses, authority relations, reachability results, and mission consequences are derived state and must be rebuildable.

## TB-4 AI
AI output is non-authoritative. It may retrieve, summarize, compare, explain, surface contradictions, and propose investigation questions. It does not become canonical state without validated structured processing.

## TB-5 Decision
Candidate defensive actions and simulations are produced without external side effects.

## TB-6 Controlled response
Authorization, evidence sufficiency, mission constraints, rollback availability, policy, and approval are checked before any controlled response.

## TB-7 Evaluation ground truth
Synthetic-range ground truth is separated from KORDAXIS inference components during evaluation and is available only to benchmark infrastructure.
