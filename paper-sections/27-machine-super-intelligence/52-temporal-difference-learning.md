---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6.1. Temporal difference learning
section_role: other
section_index: 52
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In the field of reinforcement learning, perhaps the most popular way to estimate the future discounted reward of states is the method of temporal…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.1. Temporal difference learning

> Section 52 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In the field of reinforcement learning, perhaps the most popular way to estimate the future discounted reward of states is the method of temporal difference learning. It is unclear who exactly introduced this first, however the first
explicit version of temporal difference as a learning rule appears to be Witten
(1977). The idea is as follows: The expected future discounted reward of a state
s is,
{}
V := E r + γr + γ2r + ···|s = s,

$$
\overline{{V}}_{s}:=\mathbf{E}\left\{r_{k}+\gamma r_{k+1}+\gamma^{2}r_{k+2}+\cdots|s_{k}=s\right\},
$$

where the rewards rk,rk+1
γ < 1. From this definition it follows that,

,... are geometrically discounted into the future by
{}

$$
r_{k},r_{k+1},\ldots
$$

$$
\gamma<1
$$

$$
\overline{{V}}_{s}=\mathbf{E}\left\{r_{k}+\gamma\overline{{V}}_{s_{k+1}}|s_{k}=s\right\}.
$$

(6.1)

Our task, at time t, is to compute an estimate Vst of V s for each state s.
The only information we have to base this estimate on is the current history
of state transitions, s1,s2,...,st, and the current history of observed rewards,
r1,r2,...,rt. Equation (6.1) suggests that at time t + 1 the value of rt + γVst+1
provides us with information on what Vst should be: if it is higher than Vstt
then perhaps this estimate should be increased, and vice versa. This intuition
gives us the following estimation heuristic for state st,
()

$$
V_{s}^{t}
$$

$$
\overline{V}_{s}
$$

$$
s
$$

$$
s_{1},s_{2},\ldots,s_{t}
$$

$$
r_{1},r_{2},\ldots,r_{t}
$$

$$
r_{t}+\gamma V_{s_{t+1}}
$$

$$
V_{s}^{t}
$$

$$
V_{s_{t}}^{t}
$$

$$
s_{t}
$$

$$
V_{s_{t}}^{t+1}:=V_{s_{t}}^{t}+\alpha\left(r_{t}+\gamma V_{s_{t+1}}^{t}-V_{s_{t}}^{t}\right),
$$

where α is a parameter that controls the rate of learning. This type of temporal
difference learning is known as TD(0).

$$
\mathrm{TD}(0)
$$

One shortcoming of this method is that at each time step the value of only
the last state st is updated. States before the last state are also affected by

$$
s_{t}
$$

Algorithm 1 TD(λ)
Initialise V (s) arbitrarily and E(s) = 0 for all s
Initialise s
repeat
Make state transition and observe r, s′
∆ ← r + γV (s′) − V (s)
E(s) ← E(s) + 1
for all s do
V (s) ← V (s) + αE(s)∆
E(s) ← γλE(s)
end for
s ← s′
until end of run

$$
E(s)=0
$$

$$
V(s)
$$

$$
r,s^{\prime}
$$

$$
\Delta\leftarrow r+\gamma\overline{V}\left(s^{\prime}\right)-\overline{V}\left(s\right)
$$

$$
E(s)\leftarrow E(s)+1
$$

$$
V(s)\leftarrow V(s)+\alpha E(s)\Delta
$$

$$
E(s)\leftarrow\gamma\lambda E(s)
$$

$$
s\leftarrow s'
$$

changes in the last state’s value and thus these could be updated too. This is
what happens with so called temporal difference learning with eligibility traces,
where a history, or trace, is kept of which states have been recently visited.
Under this method, when we update the value of a state we also go back
through the trace updating the earlier states as well. Formally, for any state
s its eligibility trace is computed by,
{

$$
E_{s}^{t}:=\left\{\begin{array}{ll}\gamma\lambda E_{s}^{t-1}&\text{if}s\neq s_{t},\\\gamma\lambda E_{s}^{t-1}+1&\text{if}s=s_{t},\end{array}\right.
$$

where λ is used to control the rate at which the eligibility trace is discounted.
The temporal difference update is then, for all states s,
()

$$
V_{s}^{t+1}:=V_{s}^{t}+\alpha E_{s}^{t}\left(r+\gamma V_{s_{t+1}}^{t}-V_{s_{t}}^{t}\right).
$$

(6.2)

This more powerful version of temporal different learning is known as TD(λ)
(Sutton, 1988). The complete algorithm appears in Algorithm 1.

Although it has been successfully applied to many simple problems, plain
TD(λ) has a number of drawbacks. One of these is that the learning rate
parameter α has to be experimentally tuned by hand. Indeed, even this is
not always enough, for optimal performance some monotonically decreasing
function has to be experimentally found that decreases the learning rate over
time at the right rate. If the learning rate decreases too quickly, the system
may become stuck at a level of sub-optimal performance, if it decreases too
slowly then convergence will be unnecessarily late. The main contribution of
this chapter is to solve this problem by deriving a temporal difference rule
from statistical principles that automatically sets its learning rate.

Perhaps the closest work to ours is the LSTD(λ) algorithm (Bradtke and
Barto, 1996; Boyan, 1999; Lagoudakis and Parr, 2003). LSTD(λ) is concerned
with finding a least-squares linear function approximation to the true value function. The unknown expected rewards and transition probabilities are replaced by empirical averages up to current time t. In contrast, we consider
finite state spaces and no function approximation. We derive a least-squares
estimate of the empirical values including future rewards by bootstrapping.
The computation time for our update is linear in the number of states, like
TD(λ), while LSTD is quadratic (even in the case of state-indicator features
and no function approximation). Indeed our algorithm exactly coincides with
TD/Q/Sarsa(λ) but with a novel learning rate derived from statistical principles. LSTD has not yet been developed for general λ and γ. Our algorithm and
LSTD both get rid of the learning rate and the necessity to initialise V. Since
LSTD has primarily been developed for linear function approximation and has
a much more expensive update rule, we focused our experimental comparison
to the algorithms for which we determined the learning rate (finite state space,
linear time TD/Q/Sarsa algorithms). It remains to be seen how our approach
generalises to (linear) function approximation.

$$
\lambda
$$

$$
\gamma
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
