# Benchmark Methodology

KORDAXIS capability claims are evaluated against controlled synthetic ground truth rather than visual plausibility.

## Scenario partitions

### Development set
Visible ground truth used while implementing core behavior.

### Calibration set
Separate scenarios used to tune thresholds and, only later, probabilistic calibration.

### Blind evaluation set
Ground truth is unavailable to inference components during execution and is compared only by benchmark infrastructure.

## Primary correctness metrics

- reconstruction precision and recall
- attack-path precision and recall
- false reachable-path rate
- authority-path correctness
- telemetry-gap detection precision and recall
- mission-impact correctness
- counterfactual correctness
- intervention path reduction
- mission disruption under intervention
- evidence-lineage coverage
- decision reproducibility
- replay determinism

## Calibration metrics
Probabilistic outputs are not introduced until held-out evaluation exists. When they are introduced, calibration should include Brier score, reliability analysis, and an explicitly chosen calibration-error metric.

## Performance metrics

- ingest throughput
- canonical projection latency
- reachability latency
- intervention-solver latency
- replay runtime
- storage amplification

Performance targets must be attached to representative scenario sizes rather than published as context-free numbers.

## Resilience matrix
Scenarios should vary event loss, delivery delay, clock skew, duplicate delivery, misleading observations, and sensor outage in controlled combinations.

## Repetition and uncertainty
Non-deterministic experiments require multiple runs and reported dispersion or confidence intervals. Deterministic replay tests require exact declared equivalence under fixed versions and seeds.

## Anti-overfitting rule
GEN0-001 is not sufficient evidence for universal capability. Passing the development scenario cannot substitute for held-out scenario evaluation.
