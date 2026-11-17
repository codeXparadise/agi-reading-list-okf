---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6.3. Estimating a small Markov process
section_role: other
section_index: 54
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "$$ V{s} $$ For our first test we consider a small Markov process with 21 states. In each step the state number is either incremented or decremented…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.3. Estimating a small Markov process

> Section 54 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

$$
V_{s}
$$

For our first test we consider a small Markov process with 21 states. In each
step the state number is either incremented or decremented by one with equal

**TD UPDATING WITHOUT A LEARNING RATE**

| Time (x1e4) | HL(1.0) (RMSE) | TD(0.7) a = 0.07 (RMSE) | TD(0.7) a = 0.13 (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.26 | 0.26 | 0.26 |
| 0.2 | 0.055 | 0.06 | 0.05 |
| 0.4 | 0.04 | 0.04 | 0.065 |
| 0.6 | 0.037 | 0.055 | 0.075 |
| 0.8 | 0.037 | 0.06 | 0.085 |
| 1.0 | 0.033 | 0.058 | 0.09 |

**TD UPDATING WITHOUT A LEARNING RATE**

| Time (x1e4) | HL(1.0) (RMSE) | TD(0.7) a = 0.07 (RMSE) | TD(0.7) a = 0.13 (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.26 | 0.26 | 0.26 |
| 0.2 | 0.055 | 0.07 | 0.06 |
| 0.4 | 0.045 | 0.04 | 0.075 |
| 0.6 | 0.04 | 0.05 | 0.078 |
| 0.8 | 0.038 | 0.055 | 0.08 |
| 1.0 | 0.037 | 0.06 | 0.078 |

Figure 6.1.: 21 state Markov process,
average performance over
10 runs.

Figure 6.2.: 21 state Markov process,
average performance over
100 runs.

probability, unless the system is in state 0 or 20 in which case it always transitions to state 10 in the following step. When the state transitions from 0 to
10 a reward of 1.0 is generated, and for a transition from 20 to 10 a reward of
-1.0 is generated. All other transitions have a reward of 0. We set the discount
value γ = 0.9 and then computed the true discounted value of each state by
running a brute force Monte Carlo simulation.

$$
\gamma=0.9
$$

For our first test we ran our algorithm 10 times on the above Markov chain
and computed the root mean squared error in the value estimate across the
states at each time step averaged across each run. The optimal value of λ for
our algorithm, which we will call HL(λ), was 1.0. This was to be expected
given that the environment is stationary and thus discounting old experience
is not helpful. Setting this parameter correctly was important, for example if
we reduced the value of λ to 0.98 performance became poor.

For TD(λ) the optimal value of λ was about 0.7. This algorithm was much
less sensitive to the setting of λ. The other important parameter for TD(λ)
was the learning rate α. We tested a variety of values, the effect of which is
illustrated by the two values α = 0.07 and α = 0.13 on Figure 6.1.

$$
\alpha=0.07
$$

$$
\alpha=0.13
$$

When α was high, TD(λ) learnt more quickly, as we would expect, but then
became unstable as the learning rate was too high for fine tuning the value
estimates. With the lower learning rate of 0.07, TD(λ) learnt more slowly, but
eventually achieved a more accurate value estimate before becoming stuck. In
fact rather than just becoming stuck, what we see is that the error reaches
a minimum at around t = 4,000 and then actually becomes worse for the
remainder of the run. This is a well known undesirable characteristic of TD(λ)
(see for example Section 6.2 of Sutton and Barto, 1998). With a fixed learning
rate we also see that the variability in the error estimate does not improve
towards the end of the run.

In comparison, HL(λ) had very fast learning initially, combined with a more
accurate final estimate of the discounted state values, and the mean squared
error in the second half of the experiment was very stable. This is significant
given that TD(λ) required two parameters to be tuned for good performance,
while HL(λ) had just λ which could be set a priori to 1.0.

Figure 6.2 shows the same experiment averaged over 100 runs. This obscures
the better stability of HL(λ), but more clearly illustrates its faster learning and
better convergence.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
