# Canonical Ontology — Generation 0

Generation 0 keeps the ontology intentionally narrow. New entity classes require a demonstrated scenario or reasoning need.

## Principal
HumanPrincipal, ServicePrincipal, WorkloadPrincipal, AgentPrincipal, ExternalPrincipal.

## Authentication and credentials
Credential, Session, AccessToken, RefreshToken, OIDCAssertion, OAuthGrant, KeyMaterialReference.

## Authority
Permission, Role, Grant, Delegation, TrustRelationship, FederationBinding, Policy, EffectiveAuthority.

## Software supply chain
Repository, Revision, WorkflowDefinition, WorkflowRun, Runner, Build, Artifact, Attestation, Dependency, RegistryObject, Deployment.

## Compute and runtime
Host, Workload, Container, RuntimeService, CloudResource.

## Data
Secret, Database, Dataset.

## Observability
Sensor, TelemetrySource, ObservationChannel, CoverageWindow, HeartbeatExpectation.

## Security reasoning
Vulnerability, Observation, Evidence, Claim, Hypothesis, Assumption, Contradiction, ExpectedEvidence.

## Mission
MissionCapability, MissionDependency, MissionConstraint, RecoveryPriority, AcceptableDegradation.

## Decision support
CandidateAction, Simulation, Authorization, Decision, ExecutionResult, DecisionReceipt.

## Relationship rule
Relationships are typed first-class records rather than anonymous graph edges. Material relationships carry temporal validity, provenance, and derivation metadata where applicable.

## Generation-0 constraint
Ontology growth is rejected unless the new concept is required to represent evidence, reproduce state, evaluate a hypothesis, compute authority/reachability, model mission consequence, or evaluate a defensive decision.
