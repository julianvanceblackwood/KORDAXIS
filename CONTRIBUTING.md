# Contributing to KORDAXIS

KORDAXIS treats repository history as engineering evidence. Changes should be narrow enough to review, explicit about the property they affect, and supported by validation appropriate to the claim.

Read the [Development method](docs/engineering/DEVELOPMENT_METHOD.md) before substantive work.

## Branch strategy

Use short-lived branches with descriptive prefixes such as:

- feat/
- fix/
- research/
- test/
- docs/
- chore/

A branch should represent one coherent engineering objective.

## Issue policy

Create an issue when durable tracking is justified for:

- incorrect system behavior
- violated invariants
- architectural changes
- security-relevant design changes
- measurable benchmark gaps
- substantial research questions

Do not create issues for typos, routine formatting, small README edits, obvious housekeeping, or work already covered by an active engineering objective.

Not every pull request requires a new issue.

## Semantic changes

When a change alters domain meaning, update the normative contract before or with the implementation.

Examples include changes to:

- field semantics
- identity rules
- temporal semantics
- trust boundaries
- claim states
- replay behavior
- authorization conditions
- acceptance criteria

Implementation and documentation must not describe different contracts.

## Pull request policy

Material changes to main use pull requests.

A substantial PR should explain, where relevant:

- the problem
- the intended engineering result
- affected invariant or system property
- scope and explicit non-goals
- new or changed failure modes
- validation performed
- replay or determinism impact
- security or trust-boundary impact
- benchmark impact
- migration or rollback considerations

Do not add sections that have no material relationship to the change.

## Validation

Validation should match the property being claimed.

Examples include:

- unit tests for local invariants
- integration tests for component boundaries
- database constraint tests for persistence guarantees
- negative tests for rejection behavior
- replay checks for deterministic semantics
- controlled experiments for reasoning claims
- benchmarks for performance claims

A passing demonstration does not establish behavior outside the tested conditions.

## Review model

KORDAXIS currently has one maintainer.

The repository does not claim independent human review when none occurred. Pull requests remain required because they preserve isolated diffs, CI evidence, review history, and architectural traceability.

A mandatory second-party approval can be introduced when an independent maintainer exists.

## Merge strategy

Use squash merge for normal KORDAXIS work.

The resulting commit should describe the engineering result rather than preserve temporary implementation history.

## Definition of done

A change is complete when:

- its semantics are explicit
- relevant tests or experiments pass
- documentation matches implementation
- material failure behavior is understood
- security and replay implications are addressed where applicable
- claims remain no stronger than the available evidence
