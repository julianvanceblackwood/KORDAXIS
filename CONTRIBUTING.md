# Contributing to KORDAXIS

KORDAXIS treats repository history as engineering evidence. Changes should be reviewable, testable, attributable, and narrow enough to reason about.

## Branch strategy

Use short-lived branches with prefixes such as `feat/`, `fix/`, `research/`, `test/`, `docs/`, and `chore/`.

## Issue policy

Create an issue only for meaningful engineering work: incorrect system behavior, violated invariants, architectural changes, measurable benchmark gaps, new research requirements, or security-relevant design changes.

Do not create issues for typos, small README edits, mechanical formatting, obvious housekeeping, or one-line maintenance.

Not every pull request requires an issue.

## Pull request policy

After bootstrap, material changes to `main` must use a pull request. Every substantial PR should explain the problem, why the change is necessary, affected security/system property, new failure modes, validation, replay impact, threat-model impact, and rollback strategy.

## Review model

KORDAXIS currently has one maintainer. The repository will not pretend that independent human review exists when it does not. Pull requests are still mandatory because they provide isolated change sets, CI execution, diff review, discussion history, and architectural traceability.

A mandatory second-party approval will be introduced when an independent maintainer exists.

## Merge strategy

Use squash merge. The resulting commit should describe the engineering result rather than preserve temporary implementation commits.

## Definition of done

A change is not complete until its relevant tests, documentation, threat-model implications, benchmark implications, and failure behavior have been addressed.
