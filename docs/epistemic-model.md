# Epistemic Model

KORDAXIS models why a proposition is supported rather than storing conclusions as unexplained facts.

## Claim evaluation dimensions

Generation 0 records at least:
- support strength
- contradiction strength
- source diversity
- source independence
- telemetry coverage
- freshness
- temporal consistency
- mechanistic consistency
- missing expected evidence
- model uncertainty

## Claim states

CONFIRMED

PROBABLE

POSSIBLE

CONTESTED

AMBIGUOUS

UNKNOWN

INSUFFICIENT_EVIDENCE

These states are derived classifications under versioned policy, not immutable truths.

## Numerical confidence rule

Generation 0 does not display an uncalibrated number such as `0.81` as a probability.

A numeric internal score, if used, must be labeled as a score until calibration against held-out scenarios demonstrates probabilistic meaning.

## Source independence

Two observations are not independent merely because they arrived from two APIs. The system must be able to represent common upstream origin or shared failure domains.

## Missing evidence

Absence becomes informative only when an expected-evidence model exists. Expected evidence records the producer/channel, expectation window, applicability conditions, and whether the expectation itself is reliable.

## Competing hypotheses

Multiple explanations remain active when evidence does not distinguish them. New evidence updates support and contradiction without deleting plausible alternatives.

A core investigation query is:

`Which obtainable evidence would most strongly distinguish the leading competing hypotheses?`

Generation 0 may implement this initially through deterministic discriminating-evidence rules before more advanced information-gain methods are justified.
