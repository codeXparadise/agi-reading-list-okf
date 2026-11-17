---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6.6. Non-stationary Markov process
section_role: other
section_index: 57
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "The λ parameter in HL(λ), introduced in Equation (6.4), reduces the importance of old observations when computing the state value estimates. When the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.6. Non-stationary Markov process

> Section 57 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

The λ parameter in HL(λ), introduced in Equation (6.4), reduces the importance of old observations when computing the state value estimates. When the
environment is stationary this is not useful and so we can set λ = 1.0, however
in a non-stationary environment we need to reduce this value so that the state
values adapt properly to changes in the environment. The more rapidly the
environment is changing, the lower we need to make λ in order to more rapidly
forget old observations.

$$
\lambda=1.0
$$

To test HL(λ) in such a setting we reverted back to the 21 state Markov
chain from Section 6.3 in order to speed up convergence. We used this Markov
chain for the first 5,000 time steps. At that point, we changed the reward
when transitioning from the last state to the middle state from -1.0 to be 0.5.
At time 10,000 we then switched back to the original Markov chain, and so on
alternating between the models of the environment every 5,000 steps. At each
switch, we also changed the target state values that the algorithm was trying
to estimate to match the current configuration of the environment. For this
experiment we set γ = 0.9.

$$
\gamma=0.9.
$$

As expected, the optimal value of λ for HL(λ) fell from 1 down to about
0.9995. This is about what we would expect given that each phase is 5,000
steps long. For TD(λ) the optimal value of λ was around 0.8 and the optimum
learning rate was around 0.05. As we would expect, for both algorithms when
we pushed λ above its optimal value this caused poor performance in the
periods following each switch in the environment (these bad parameter settings
are not shown in the results). On the other hand, setting λ too low produced
initially fast adaption to each environment switch, but poor performance after
that until the next environment change. To get accurate statistics we averaged
over 200 runs. The results of these tests appear in Figure 6.6.

$$
\lambda
$$

Algorithm 2 HLS(λ)
Initialise Q(s,a) = 0, N (s,a) = 1 and E(s,a) = 0 for all s, a
Initialise s and a
repeat
Take action a, observed r, s′
Choose a′ by using ǫ-greedy selection on Q(s′, ·)
∆ ← r + γQ(s′,a′) − Q(s,a)
E(s,a) ← E(s,a) + 1
N (s,a) ← N (s,a) + 1
for all s,a do
1 N (s′,a′)
β((s,a), (s′,a′)) ←
N (s′,a′)−γE(s′,a′) N (s,a)
end for
for all s,a do
()
Q(s,a) ← Q(s,a) + β (s,a), (s′,a′) E(s,a)∆
E(s,a) ← γλE(s,a)
N (s,a) ← λN (s,a)
end for
s ← s′; a ← a′
until end of run

$$
E(s,a)=0
$$

$$
Q(s,a)=0,\;N(s,a)=1
$$

$$
a,
$$

$$
a^{\prime}
$$

$$
r,\;s^{\prime}
$$

$$
\Delta\leftarrow r+\gamma Q(s',a')-Q(s,a)
$$

$$
Q\big(s^{\prime},\cdot\big)
$$

$$
E(s,a)\leftarrow E(s,a)+1
$$

$$
N(s,a)\leftarrow N(s,a)+1
$$

$$
\beta((s,a),(s^{\prime},a^{\prime}))\leftarrow\frac{1}{\scriptstyle N(s^{\prime},a^{\prime})-\gamma E(s^{\prime},a^{\prime})}\quad\frac{\scriptstyle N(s^{\prime},a^{\prime})}{\scriptstyle N(s,a)}
$$

$$
s,a
$$

$$
Q(s,a)\leftarrow Q(s,a)+\beta\big((s,a),(s^{\prime},a^{\prime})\big)E(s,a)\Delta
$$

$$
E(s,a)\leftarrow\gamma\lambda E(s,a)
$$

$$
N(s,a)\leftarrow\lambda N(s,a)
$$

$$
s\leftarrow s';a\leftarrow a'
$$

For some reason HL(0.9995) learns faster than TD(0.8) in the first half
of the first cycle, but only equally fast at the start of each following cycle.
Furthermore, its performance in the second half of the first cycle is poor. We
are not sure why this is happening. We could improve the initial speed at
which HL(λ) learnt in the last three cycles by reducing λ, however that comes
at a performance cost in terms of the lowest mean squared error attained at
the end of each cycle. In any case, in this non-stationary situation HL(λ) again
performed well in general.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
