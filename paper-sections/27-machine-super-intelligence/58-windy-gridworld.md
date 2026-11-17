---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6.7. Windy Gridworld
section_role: other
section_index: 58
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Reinforcement learning algorithms such as Watkins’ version of Q(λ) (Watkins, 1989) and Sarsa(λ) (Rummery and Niranjan, 1994; Rummery, 1995) are based…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.7. Windy Gridworld

> Section 58 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Reinforcement learning algorithms such as Watkins’ version of Q(λ) (Watkins,
1989) and Sarsa(λ) (Rummery and Niranjan, 1994; Rummery, 1995) are based
on temporal difference updates. This suggests that new reinforcement learning
algorithms based on HL(λ) should be possible.

For our first experiment we took the standard Sarsa(λ) algorithm and modified it in the obvious way to use an HL temporal difference update. In the
presentation of this algorithm we have changed notation slightly to make things
more consistent with that typical in reinforcement learning. Specifically, we
have dropped the t super script as this is implicit in the algorithm specification, and have defined Q(s,a) := V(s,a), E(s,a) := E(s,a) and N (s,a) := N(s,a).
Our new reinforcement learning algorithm, which we call HLS(λ) is given in
Algorithm 2. Essentially the only changes to the standard Sarsa(λ) algorithm

$$
Q(s,a):=V_{(s,a)},E(s,a):=E_{(s,a)}
$$

$$
N(s,a):=N_{(s,a)}
$$

| Category | wind strength 0 | wind strength 1 | wind strength 2 |
| --- | --- | --- | --- |
| unlabelled 1 |  | ↑ | ↑ |
| unlabelled 2 |  | ↑ | ↑ |
| unlabelled 3 |  | ↑ | ↑ |
| S |  | ↑ | G |
| unlabelled 4 |  | ↑ | ↑ |
| unlabelled 5 |  | ↑ | ↑ |
| unlabelled 6 |  | ↑ | ↑ |

Figure 6.7.: [Windy Gridworld] S marks the start state and G the goal state,
at which the agent jumps back to S with a reward of 1. Small
arrows indicate an upward wind of one row per time step. The
large arrows indicate a wind of two rows per time step.

have been to add code to compute the visit counter N (s,a), add a loop to
compute the β values, and replace α with β in the temporal difference update.

$$
N(s,a)
$$

$$
\beta
$$

$$
\beta
$$

To test HLS(λ) against standard Sarsa(λ) we used the Windy Gridworld
environment described on page 146 of (Sutton and Barto, 1998). This world is
a grid of 7 by 10 squares that the agent can move through by going either up,
down, left or right. If the agent attempts to move off the grid it simply stays
where it is. The agent starts in the 4th row of the 1st column and receives
a reward of 1 when it finds its way to the 4th row of the 8th column. To
make things more difficult, there is a “wind” blowing the agent up 1 row in
columns 4, 5, 6, and 9, and a strong wind of 2 rows in columns 7 and 8. This
is illustrated in Figure 6.7. Unlike in the original version, we have set up this
problem to be a continuing discounted task with an automatic transition from
the goal state back to the start state. This is because we have not yet derived
an episodic version of our learning rule.

$$
4^{th}
$$

$$
1^{st}
$$

$$
4^{th}
$$

$$
8^{th}
$$

We set γ = 0.99 and in each run computed the empirical future discounted
reward at each point in time. As this value oscillated we also ran a moving
average through these values with a window length of 50. Each run lasted for
50,000 time steps as this allowed us to see at what level each learning algorithm
topped out. These results appear on the left of Figure 6.8 and were averaged
over 500 runs to get accurate statistics.

$$
\gamma=0.99
$$

Despite putting considerable effort into tuning the parameters of Sarsa(λ),
we were unable to achieve a final future discounted reward above 5.0. The

| Time | HLS(0.995) e = 0.003 (Future Discounted Reward) | Sarsa(0.5) a = 0.4 e = 0.005 (Future Discounted Reward) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10000 | 4.0 | 3.8 |
| 20000 | 4.9 | 4.7 |
| 30000 | 5.15 | 4.85 |
| 40000 | 5.2 | 4.9 |
| 50000 | 5.25 | 4.95 |

| Time | HLQ(0.99) e = 0.01 (Future Discounted Reward) | Q(0.75) a = 0.99 e = 0.01 (Future Discounted Reward) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10000 | 4.3 | 4.0 |
| 20000 | 5.15 | 4.9 |
| 30000 | 5.4 | 5.3 |
| 40000 | 5.45 | 5.4 |
| 50000 | 5.45 | 5.45 |

Figure 6.8.: Windy Gridworld performance tests. The left graph shows
HLS(λ) vs. Sarsa(λ), while the right graph shows HLQ(λ) vs.
Q(λ). In both tests the algorithm based on HL learning performed
best. e represents the exploration parameter ǫ, and a represents
the learning rate α. For both tests the performance was averaged
over 500 runs.

settings shown on the graph represent the best final value we could achieve.
In comparison HLS(λ) easily beat this result at the end of the run, while being
slightly slower than Sarsa(λ) at the start. By setting λ = 0.99 we were able
to achieve the same performance as Sarsa(λ) at the start of the run, however
the performance at the end of the run was then only slightly better than
Sarsa(λ). This combination of superior performance and fewer parameters
to tune suggest that the benefits of HL(λ) carry over into the reinforcement
learning setting. In terms of computational cost, HL(λ) was about 1.7 times
slower than Sarsa(λ) per time step due to the cost of computing the β values.

$$
\lambda=0.99
$$

$$
\beta
$$

Another popular reinforcement learning algorithm is Watkins’ Q(λ). Similar
to Sarsa(λ) above, we simply inserted the HL(λ) temporal difference update
into the usual Q(λ) algorithm in the obvious way. We call this new algorithm
HLQ(λ) and it is given in Algorithm 3. The test environment was exactly the
same as we used with Sarsa(λ) above.

$$
Q(\lambda)
$$

The results this time were more competitive and appear on the right hand
side of Figure 6.8. Nevertheless, despite spending a considerable amount of
time fine tuning the parameters of Q(λ), we were unable to beat HLQ(λ). As
the performance advantage was relatively modest, the main benefit of HLQ(λ)
was that it achieved this level of performance without having to manually tune
a learning rate.

Algorithm 3 HLQ(λ)
Initialise Q(s,a) = 0, N (s,a) = 1 and E(s,a) = 0 for all s, a
Initialise s and a
repeat
Take action a, observed r, s′
Choose a′ by using ǫ-greedy selection on Q(s′, ·)
a∗ ← arg maxb Q(s′,b)
∆ ← r + γQ(s′,a∗) − Q(s,a)
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
N (s,a) ← λN (s,a)
if a′ = a∗ then
E(s,a) ← γλE(s,a)
else
E(s,a) ← 0
end if
end for
s ← s′; a ← a′
until end of run

$$
r,s^{\prime}
$$

$$
a^{\prime}
$$

$$
Q\big(s^{\prime},\cdot\big)
$$

$$
\Delta\leftarrow r+\gamma Q(s',a^*)-Q(s,a
$$

$$
E(s,a)\leftarrow E(s,a)+1
$$

$$
N(s,a)\leftarrow N(s,a)+1
$$

$$
\beta((s,a),(s^{\prime},a^{\prime}))\leftarrow\frac{1}{N(s^{\prime},a^{\prime})-\gamma E(s^{\prime},a^{\prime})}\quad\frac{N(s^{\prime},a^{\prime})}{N(s,a)}
$$

$$
s,a
$$

$$
Q(s,a)\leftarrow Q(s,a)+\beta\big((s,a),(s^{\prime},a^{\prime})\big)E(s,a)\Delta
$$

$$
N(s,a)\leftarrow\lambda N(s,a)
$$

$$
a^{\prime}=a^{*}
$$

$$
E(s,a)\leftarrow\gamma\lambda E(s,a)
$$

$$
E(s,a)\leftarrow0
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
