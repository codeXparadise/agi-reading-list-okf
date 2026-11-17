---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.10. Universal AIXI agent
section_role: other
section_index: 22
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Although the agent πµ performs optimally in environment µ, this does not meet the requirements for intelligence according to our definition adopted…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.10. Universal AIXI agent

> Section 22 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Although the agent πµ performs optimally in environment µ, this does not
meet the requirements for intelligence according to our definition adopted in
Chapter 1. What we require is a general agent that works well in many different
environments. Such an agent must learn about its environment by interacting
with it, and then modify its behaviour accordingly in order to optimise performance. Only then will the agent have the kind of adaptability to different
environments that we require of an intelligent agent.

$$
\pi^{\mu}
$$

$$
\mu,
$$

$$
\mathrm{it}.
$$

This problem with the optimal agent πµ is similar to the one we encountered
in Section 2.7. There the optimal sequence predictor was based on the distribution µ that was actually generating the sequence. Of course, for inductive
inference µ is unknown and must be inferred by observing the sequence. Thus,
basing a predictor on µ might be “optimal” in terms of prediction performance,
but it is in some sense cheating. Moreover, it is certainly not general as the
predictor is designed for just one environment.

$$
\pi^{\mu}
$$

$$
\mu
$$

$$
\mu
$$

$$
\mu
$$

Solomonoff’s solution was to replace the unknown µ in the optimal predictor with a universal prior distribution, such as ξ. This produced an extremely powerful universal predictor that rapidly converged to optimal predictions whenever the distribution µ was computable (Theorem 2.7.1). In this
way Solomonoff solved, at least in theory, the problem of predicting sequences
from unknown distributions. Hutter’s innovation was to do essentially the
same trick for active agents: he took the optimal active agent πµ, described in
the previous section, and replaced the unknown µ with a generalised universal
prior distribution ξ. This produced πξ, also known as AIXI, which will be
described in this section.

$$
\mu
$$

$$
\xi.
$$

$$
\mu
$$

$$
\pi^{\mu}
$$

$$
\mu
$$

$$
\xi
$$

$$
\pi^{\xi}
$$

In order to construct πξ, the first thing to do is to generalise ξ in Definition 2.5.4 from sequences to active environments. As we saw earlier, an active
environment µ is an enumerable semi-measure conditioned, in chronological
order, on a sequence of actions from an agent. The presence of these actions
causes no problems, indeed the development of a universal distribution over active environments is virtually identical to what we did for sequence prediction
in Section 2.5.

$$
\pi^{\xi}
$$

$$
\xi
$$

$$
\mu
$$

It can be shown that the space of all enumerable chronological semi-measures
can be effectively enumerated. Let E := {µ1,µ2,...} be such an enumeration.
Define the Kolmogorov complexity of one of these environments to be the
length of the shortest program that computes the environment’s index: just
as we did for distributions over sequences in Definition 2.5.2. This gives us the
universal prior probability of a chronological environment ν ∈ E,

$$
E:=\left\{\mu_{1},\mu_{2},\ldots\right\}
$$

$$
\nu\in E
$$

$$
P_{E}(\nu):=2^{-K(\nu)}.
$$

From this prior over environments we can construct a prior over the agent’s
observations in a given interaction history by taking a mixture over the envi-

2. Universal Artificial Intelligence

$$
\xi(a\underline{{x}}_{1:n}):=\sum_{\nu\in E}2^{-K(\nu)}\nu(a\underline{{x}}_{1:n}).
$$

ronments,

It is easy to see that ξ is enumerable because 2−K(ν) is enumerable, as is
each ν in the sum. Furthermore, this sum of chronological semi-measures is
itself a chronological semi-measure. Thus, we see that ξ ∈ E. As was the
case for sequences, the dominance property for ξ can easily be seen by taking
one element from the sum corresponding to the semi-measure to be dominated.
Note that we are reusing the symbol ξ. Whether we are talking about ξ defined
over sequences, or over chronological environments, will always be clear from
the context.

$$
2^{-K(\nu)}
$$

$$
\xi
$$

$$
\xi
$$

$$
\xi\in E
$$

$$
\xi_{1}
$$

$$
\xi
$$

To construct the AIXI agent πξ
∑ ∑

, simply take π
∑ [

µ and replace µ with ξ,

$$
\pi^{\xi}
$$

$$
\pi^{\mu}
$$

$$
a_{t}^{\pi^{\xi}}:=\arg\operatorname*{m a x}_{a_{t}}\operatorname*{l i m}_{m\to\infty}\sum_{x_{t}}\operatorname*{m a x}_{a_{t+1}}\sum_{x_{t+1}}\cdots\operatorname*{m a x}_{a_{m}}\sum_{x_{m}}\left[\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}\right]\xi(a x_{<t}a\underline{{x}}_{t:m}).
$$

$$
\mu
$$

$$
\xi
$$

This gives us an agent that does not depend on the unknown µ. Replacing
the true distribution µ in the optimal agent πµ with the universal prior distribution ξ is essentially the same as what we did in Section 2.7 when defining
Solomonoff’s universal predictor. Of course now we are working in the more
general setting of chronological environments rather than just sequences.

$$
\mu.
$$

$$
\mu
$$

$$
\pi^{\mu}
$$

$$
\xi
$$

Given that Solomonoff prediction works so well for sequence prediction, we
might expect the agent πξ defined above to be similarly powerful in chronological environments. To some extent this is the case, however analysing the
performance of universal agents in chronological environments turns out to be
significantly more complex.

$$
\pi^{\xi}
$$

Perhaps the most elementary question concerns whether our generalised ξ
converges to the true environment µ. It turns out that convergence results
can be proven, including a result similar to Solomonoff’s convergence result
generalised to interaction histories. More precisely, it can be proven that the
total µ-expected squared difference between µ and ξ is finite for interaction
histories sampled from πµ interacting with a computable environment µ. Unfortunately, when the interaction history comes from µ interacting with πξ,
rather than πµ, we run into trouble. This problem is well illustrated by the
Heaven and Hell environment from Section 5.3.2 of (Hutter, 2005):

$$
\mu.
$$

$$
\xi
$$

$$
\mu-
$$

$$
\mu
$$

$$
\xi
$$

$$
\pi^{\mu}
$$

$$
\mu.
$$

$$
\pi^{\mu}
$$

$$
\pi^{\xi}
$$

$$
\mu
$$

2.10.1 Example. (Heaven and Hell) Imagine an environment where in
the first cycle the agent is faced with two unmarked doors, one of which must
be opened. One of these doors leads to “heaven” where the agent receives
plentiful rewards, and the other leads to “hell” where the agent never gets any
reward. Once a door is chosen there is no way to go back, the agent is stuck
in either heaven or hell forever.

This is no problem for πµ as it knows µ and so it knows which door to take
to get to heaven. Thus it always achieves maximal future discounted reward.
The agent πξ, on the other hand, must learn through experience. Of course

$$
\pi^{\mu}
$$

$$
\mu
$$

$$
\pi^{\xi}
$$ once it has the necessary experience to make the right choice, it may already
be too late. All πξ can do is to guess which door to take and hope for the best.
Obviously the expected performance of πξ will be far below that of πµ.

$$
\mathrm{All}\pi^{\xi}
$$

$$
\pi^{\xi}
$$

$$
\pi^{\mu}.\qquad\diamondsuit
$$

This example does not expose a design flaw in πξ, in the sense that no
general agent is able to consistently behave optimally in such environments.
For example, consider an environment µ′ with the two doors switched. Agent
πµ would always go to hell in this environment. We could define an agent
πµ′ which would be optimal in µ′, however it would always go to hell in µ.
Clearly, no agent could behave optimally in both environments without being
told what the true environment was in advance. Matching the performance of
optimal agents in each of their respective environments is thus an impossible
task for any one agent. As such, we need to think carefully about what it is
that we want to prove if we are to show that πξ is indeed a very powerful and
general agent.

$$
\pi^{\xi}
$$

$$
\mu^{\prime}
$$

$$
\pi^{\mu}
$$

$$
\mu.
$$

$$
\pi^{\mu^{\prime}}
$$

$$
\mu^{\prime}
$$

$$
\pi^{\xi}
$$

We have already seen in Section 2.7 that the above problem does not occur
in the sequence prediction setting. This is because in sequence prediction an
agent’s predictions do not affect the future observed sequence and thus mistakes have no consequences beyond the current cycle. This allows Solomonoff’s
prediction system to be able to learn to perform optimally across the entire
space of computable sequence prediction problems. Such optimising behaviour
is possible in certain other classes of environments. What this suggests then is
that we should focus on classes of environments, such as sequence prediction,
in which it is at least possible for a general agent to learn to behave optimally.

We begin by generalising the AIXI model to different classes of environments. Let E be a non-strict subset of the enumeration E of all enumerable
chronological semi-measures. Define the mixture distribution over E,
∑

$$
\mathcal{E}
$$

$$
E
$$

$$
\mathcal{E}
$$

$$
\zeta\left(a\underline{x}_{1:n}\right):=\sum_{\nu\in\mathcal{E}}2^{-K(\nu)}\nu\left(a\underline{x}_{1:n}\right).
$$

Now define the agent πζ based on ζ, just as we defined πξ based on ξ. Note that
while πξ is a single agent, the agent πζ depends on which class of environments
E we are considering. If E = E then ζ = ξ and so πζ = πξ. In this sense πζ
generalises πξ.

$$
\pi^{\zeta}
$$

$$
\zeta,
$$

$$
\pi^{\xi}
$$

$$
\xi.
$$

$$
\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
\mathcal{E}
$$

$$
\mathcal{E}=E
$$

$$
\zeta=\xi
$$

$$
\pi^{\zeta}=\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\xi}
$$

Perhaps the most elementary property that an optimal general agent must
have is that there should not exist any other agent that is strictly superior.
More precisely:

2.10.2 Definition. An agent π is Pareto optimal if there is no other agent
ρ such that ∀µ ∈E,

$$
\pi
$$

$$
\forall\mu\in\mathcal{E}
$$

$$
\rho
$$

$$
V_{\gamma}^{\rho\mu}(a x_{<t})\geq V_{\gamma}^{\pi\mu}(a x_{<t})\quad\forall a x_{<t},
$$

with strict inequality for at least one µ.

$$
\mu
$$

2. Universal Artificial Intelligence

$$
\mathcal{E}
$$

Note that Pareto optimality does not rule out the possibility that some other
agent exists which performs better in some environment in E. It simply means
that no other agent exists which is at least as good in all environments in E,
and strictly better in at least one. For the agent πζ the following optimality
result can be proven (Section 5.5 of Hutter, 2005):

$$
\mathcal{E}
$$

$$
\pi^{\zeta}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
