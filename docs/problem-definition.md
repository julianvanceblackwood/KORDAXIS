# Formal Problem Definition

Let the real cyber environment at time `t` be `X_t`.

KORDAXIS cannot directly observe `X_t`. It receives imperfect observations `O_[0:t]` and preserved evidence `E_[0:t]`.

KORDAXIS constructs a knowledge state:

`K_t = F(E_[0:t], P_t, M_t)`

where `P_t` represents versioned policies, inference rules, schemas, and model versions, and `M_t` represents the mission dependency model.

`K_t` is not declared to be reality. It represents what the system can defensibly assert given the evidence available at that knowledge time.

## Reachability problem

Given an adversary capability model `C_A`:

`R_t = Reachable(K_t, C_A)`

KORDAXIS computes feasible, infeasible, possible, and unknown adversary transitions. Unknown edges must not silently become reachable or unreachable.

## Defensive intervention problem

For candidate interventions `A = {a_1, a_2, ..., a_n}`, KORDAXIS seeks an intervention set minimizing residual mission risk, operational disruption, decision uncertainty, and irreversibility cost, subject to authorization constraints, safety constraints, evidence sufficiency, mission constraints, and technical feasibility.

Generation 0 does not present uncalibrated numeric belief scores as probabilities. Probability claims require calibration evidence.
