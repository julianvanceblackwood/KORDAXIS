# Generation-0 Threat Model

## Protected properties

Generation 0 protects the integrity and reproducibility of raw evidence, evidence lineage, temporal state, identity and authority relationships, derived claims, competing hypotheses, attack reachability, mission consequences, defensive simulations, decision receipts, and replay results.

## Adversary capabilities

The synthetic adversary may compromise one human identity, reuse or steal session authority, discover repository and CI relationships, exploit legitimate delegation, influence a software delivery path, obtain temporary cloud authority, manipulate artifact lineage, reach production resources, delay telemetry, remove a subset of telemetry, introduce clock skew, inject duplicate observations, introduce misleading observations, and impair a security sensor.

## Explicit trust assumptions

Generation 0 does not assume simultaneous compromise of every independent telemetry producer, the append-only evidence boundary, the benchmark ground-truth generator, and the decision-receipt trust root.

If every independent evidence and integrity boundary is assumed compromised simultaneously, meaningful inference is impossible.

## AI boundary

LLM output is non-authoritative. An AI component may retrieve, summarize, compare, explain, and propose investigation questions. It may not independently create canonical truth or execute critical actions.

## Ground-truth separation

Synthetic scenario ground truth is accessible to benchmark infrastructure. It is not accessible to KORDAXIS inference components during evaluation.
