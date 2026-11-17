---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: "2.10.3 Theorem. For any E⊆ E, the agent πζ is Pareto optimal."
section_role: other
section_index: 23
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "$$ mathcal{E}subseteq E $$ $$ pi^{zeta} $$ As this holds for any E, it also holds for E = E. Thus, the AIXI agent πξ is a Pareto optimal agent over…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.10.3 Theorem. For any E⊆ E, the agent πζ is Pareto optimal.

> Section 23 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

$$
\mathcal{E}\subseteq E
$$

$$
\pi^{\zeta}
$$

As this holds for any E, it also holds for E = E. Thus, the AIXI agent πξ is
a Pareto optimal agent over the space of environments E. Note that for any
space of environments E many Pareto optimal agents may exist.

$$
\mathcal{E}
$$

$$
\mathcal{E}=E
$$

$$
\pi^{\xi}
$$

$$
\mathcal{E}
$$

A stronger result can be proven showing that πζ is also balanced Pareto optimal (Hutter, 2005). Essentially, this means that any increase in performance
in some environment due to switching to another agent, is compensated for by
an equal or greater decrease in performance in some other environment.

$$
\pi^{\zeta}
$$

While these Pareto optimality results are very general, they only succeed
in showing that πζ is superior, or at least equal, to other general agents over
the same class of environments. The result does not rule out the possibility
that all general agents, including πζ, typically perform poorly. What we need
is to show that πζ does indeed learn to perform well in many environments.
The complication, as we saw in Example 2.10.1 above, is that in some types
of environments it is impossible for general agents to perform well. Thus we
somehow need to characterise those types of environments in which it is at
least possible for a general agent to perform well. Furthermore, even when
optimal performance is possible for a general agent, we cannot expect such an
agent to perform optimally immediately. We need a performance measure that
gives the agent time to learn about the structure of µ through interaction. One
way to formalise the concept of optimal performance after a period of learning
is the following:

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

$$
\mu
$$

2.10.4 Definition. An agent π is said to be self-optimising in an environment µ if,
1 1
µ

$$
\pi
$$

$$
\mu
$$

$$
\frac{1}{\Gamma_{t}}\:V_{\gamma}^{\pi\mu}(a x_{<t})\;\to\;\frac{1}{\Gamma_{t}}\:V_{\gamma}^{\pi^{\mu}\mu}(\dot{a}\dot{x}_{<t})
$$

with µ probability 1 as t →∞. Here ax<tis an interaction history sampled
from π interacting with µ, and ȧẋ<tis an interaction history ∑sampled from
∞
πµ interacting with µ. The normalisation factor, defined Γt:=i=tγi, is the
total discount remaining at time t.

$$
\mu
$$

$$
t\to\infty
$$

$$
ax_{<t}
$$

$$
\pi
$$

$$
\mu,
$$

$$
\dot{a}\dot{x}_{<t}
$$

$$
\pi^{\mu}
$$

$$
\Gamma_{t}:=\sum_{i=t}^{\infty}\gamma_{i}
$$

$$
\mu
$$

Essentially this says that with high probability the performance of the agent
π converges to the performance of the optimal agent. The normalisation is
necessary because the un-normalised expected future discounted reward always
converges to zero. Thus without it convergence would trivially hold for any
agent.

$$
\pi
$$

We say that π is self-optimising for the set of environments E if it is selfoptimising for every environment in E. Furthermore, we say that a set of

$$
\pi
$$

$$
\mathcal{E}
$$

$$
\mathcal{E}
$$ environments E admits self-optimising agents if there exists an agent π that
is self-optimising for E. We also extend the result to non-stationary agents by
saying that a series of agents π1,π2,... is self-optimising if the above result
holds with π replaced by πt. That is, in the tth cycle agent πt is applied.

$$
\mathcal{E}
$$

$$
\pi
$$

$$
\mathcal{E}
$$

$$
\pi_{1},\pi_{2},\ldots
$$

$$
\pi
$$

$$
\pi_{t}
$$

$$
t^{th}
$$

$$
\pi_{t}
$$

The following powerful self-optimising result can be proven (Hutter, 2005):

2.10.5 Theorem. If there exists a sequence of self-optimising agents πm for
a class of environments E, then the agent πζ is also self-optimising for E.

$$
\pi_{m}
$$

$$
\pi^{\zeta}
$$

$$
\mathcal{E}
$$

$$
\mathcal{E}
$$

Intuitively, this result says that the performance of πζ will converge to optimal performance in any class of environments where this is possible for a
single agent, even if the agent is non-stationary. This is the minimal requirement possible, in the sense that if no self-optimising agent existed for some
class of environments, then trivially πζ cannot be self-optimising in the class
either.

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

Although this is a strong optimality result, it does have two limitations.
Firstly, while the result shows that πξ converges to optimal performance whenever this is possible in a class of environments, it does not tell us how fast the
convergence is. In Solomonoff’s convergence theorem we saw that the convergence of the universal predictor was extremely rapid. Ideally we would
like a similar result for active environments. Unfortunately, such a result is
impossible in general:

$$
\pi^{\xi}
$$

2.10.6 Example. (Needle in a haystack) Imagine an environment with
N buttons, one of which generates a reward of 1 in every cycle when pressed,
and all the rest produce no reward. The location of the correct button would
take roughly log2 N bits to encode, thus for most values of N we have K(µ) =
O(log2 N). As πξ is not informed prior to the start of the game as to which
button generates reward, the best it can do is to press the buttons one at
a time. Thus the expected number of incorrect choices that πζ will make is
()
O(N) = O 2K(µ).

$$
K(\mu)=
\log_{2}
$$

$$
O(\log_{2}N)
$$

$$
\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
O(N)=O\left(2^{K(\mu)}\right)
$$

$$
\diamond
$$

Compare this to Theorem 2.7.1 for sequence prediction which bounds the
total squared difference in prediction error by O(K(µ)). Here in the active
case the best possible bound for any general agent is exponentially worse at
()
O 2K(µ). This is not a design flaw in πξ as the above limit applies to any general agent. Clearly then, bounds showing rapid convergence are not possible
in general. We can only hope to prove convergence speed bounds for specific
classes of environments. Unfortunately, results in this direction currently exist
only in very simple settings.

$$
O(K(\mu))
$$

$$
O\big(2^{K(\mu)}\big)
$$

$$
\pi^{\xi}
$$

This is a significant weakness in the theory of universal agents. Until further
results are proven it is hard to say just how fast, or slow, convergence to optimal
behaviour is in different classes of environments. As it appears that results in
this direction will be difficult, a more elementary result is to establish which
classes of environments at least admit self-optimising agents, and under what
conditions. Once we have established this, by Theorem 2.10.5 it would then

2. Universal Artificial Intelligence

follow that πζ is also self-optimising in these environments. If we can show
this for many classes of environments, it then follows that πζ is able to perform
well in a wide range of environments, at least in the limit.

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

Although the required analysis is not particularly difficult for many of the
basic classes of environments, sorting out all the definitions, the relationships between them and the conditions under which they admit self-optimising
agents is lengthy and requires some care. This is the subject of the next chapter.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
