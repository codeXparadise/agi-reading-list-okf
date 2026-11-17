---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6.4. A larger Markov process
section_role: other
section_index: 55
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In order to understand how well HL(λ) scales as the number of states increases, we ran the previous experiment again but with 51 states. As the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.4. A larger Markov process

> Section 55 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In order to understand how well HL(λ) scales as the number of states increases,
we ran the previous experiment again but with 51 states. As the movement
through the states is almost entirely a random walk with reward on just two
transitions, estimating the value function on this Markov chain is significantly
more difficult than before, even though the total number of states has not
grown all that much. In the new experiment the return state was still in
the middle of the chain, i.e. state 25. As most of the state space was a long
way from the rewards, we increased the γ value to 0.99 so that states in the
middle of the chain would not have values too close to 0. The true discounted
value of each state was again computed by running a brute force Monte Carlo
simulation.

$$
\gamma
$$

We ran our algorithm 10 times on the above Markov chain and computed
the root mean squared error in the value estimate across the states at each
time step averaged across each run. The optimal value of λ for HL(λ) was 1.0,
which was to be expected given that the environment is stationary and thus
discounting old experience is not helpful.

For TD(λ) we tried various different learning rates and values of λ. We
could find no settings where TD(λ) was competitive with HL(λ). If the learning rate α was set too high the system would learn as fast as HL(λ) briefly
before becoming stuck. With a lower learning rate the final performance was
improved, however the initial performance was now much worse than HL(λ).
The results of these tests appear in Figure 6.3.

$$
\lambda.
$$

Similar tests were performed with larger and smaller Markov chains, and
with different values of γ. HL(λ) was consistently superior to TD(λ) across
these tests. One wonders whether this may be due to the fact that the implicit learning rate that HL(λ) uses is not fixed. To test this we explored the
performance of a number of different learning rate functions on the 51 state
κ
Markov chain described above. We found that functions of the form always
t
performed poorly, however good performance was possible by setting κ cor-
√κ √κ
rectly for functions of the form and3. As the results were much closer,
t t
we averaged over 300 runs. These results appear in Figure 6.4.

$$
\gamma
$$

$$
\frac{\kappa}{t}
$$

$$
\frac{\kappa}{\sqrt{t}}
$$

$$
\frac{\kappa}{\sqrt[3]{t}}
$$

With a variable learning rate TD(λ) is performing much better, however we
were still unable to find an equation that reduced the learning rate in such

| Time (x1e+4) | HL(1.0) (RMSE) | TD(0.9) a = 0.1 (RMSE) | TD(0.9) a = 0.2 (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.36 | 0.36 | 0.36 |
| 0.5 | 0.11 | 0.19 | 0.11 |
| 1.0 | 0.08 | 0.10 | 0.15 |
| 1.5 | 0.06 | 0.07 | 0.13 |
| 2.0 | 0.06 | 0.06 | 0.14 |

| Time (x1e+4) | HL(1.0) (RMSE) | TD(0.9) a = 8.0/sqrt(t) (RMSE) | TD(0.9) a = 2.0/cbrt(t) (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.35 | 0.35 | 0.35 |
| 0.5 | 0.11 | 0.13 | 0.12 |
| 1.0 | 0.08 | 0.085 | 0.085 |
| 1.5 | 0.065 | 0.07 | 0.07 |
| 2.0 | 0.06 | 0.065 | 0.065 |

Figure 6.3.: 51 state Markov process
averaged over 10 runs.
The parameter a is the
learning rate α.

$$
\alpha.
$$

Figure 6.4.: 51 state Markov process
averaged over 300 runs.

a way that TD(λ) would outperform HL(λ). This is evidence that HL(λ) is
adapting the learning rate optimally without the need for manual equation
tuning.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
