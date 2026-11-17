---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.9. Optimal informed agents
section_role: other
section_index: 21
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In the agent-environment model, the agent’s goal is to receive as much reward as possible. Unfortunately, this is not sufficiently precise as there…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.9. Optimal informed agents

> Section 21 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In the agent-environment model, the agent’s goal is to receive as much reward
as possible. Unfortunately, this is not sufficiently precise as there may be many
possible reward sequences in a given environment and it is not clear which is
preferred.

2.9.1 Example. Consider the following two agents: Agent π1 immediately
finds a way to get a reward of 0.5 and does so in every cycle. Thus, after

$$
\pi^{1}
$$

2. Universal Artificial Intelligence

100 cycles it has received a total reward of 50. Agent π2, however, spends the
first 90 cycles trying to find the best possible way to receive reward in each
cycle. During this time it gets an average reward of 0.1 in each cycle. At
cycle 90 it works out the optimal behaviour and then receives a reward of 1
in every cycle thereafter. Thus, after 100 cycles it has received a total reward
of 90 × 0.1 + 10 = 19. In terms of the total reward received after 100 cycles,
π1 is superior to π2. However, after 1,000 cycles this has reversed as π1 has a
total reward of 500, while π2 has a total reward of 919.

$$
\pi^{2}
$$

$$
90\times0.1+10=19
$$

$$
\pi^{2}
$$

$$
\pi^{1}
$$

$$
\pi^{1}
$$

$$
\pi^{2}
$$

$$
\diamondsuit
$$

Which of these two agents is the better one? The answer depends on how
we value reward at different points in the future. In some situations we may
want our agent to perform well quickly, and thus place more value on short
term rewards. In others, we might only care that it eventually reaches a level
of performance that is as high as possible, and thus place relatively high value
on rewards far into the future. Before we can define an optimal agent, we first
need to formally express our temporal preferences.

A general approach is to weight, or discount, each reward in a way that
depends on which cycle it occurs in. Let γ1,γ2,... be the discounts we apply
∑∞
to the reward in each successive cycle, where ∀i : γi ≥ 0, andi=1γi <
∞ in order to avoid infinite weighted sums. Now define the expected future
discounted reward for agent π interacting with environment µ given interaction
history ax<tto be,

$$
\gamma_{1},\gamma_{2},\ldots
$$

$$
\forall i\::\:\gamma_{i}\:\geq\:0
$$

$$
\sum_ {i = 1} ^ {\infty} \gamma_ {i} <
$$

$$
\infty
$$

$$
\pi
$$

$$
\mu
$$

$$
ax_{<t}
$$

$$
\begin{array}{r c l}{V_{\gamma}^{\pi\mu}(\mathit{ax}_{<t})}&{:=}&{\mathbf{E}\Bigg(\sum_{i=t}^{\infty}\gamma_{i}r_{i}\:\Big|\:\mathit{ax}_{<t}\Bigg)}\\ {}&{=}&{\operatorname*{l i m}_{m\to\infty}\sum_{\mathit{ax}_{t:m}}\left(\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}\right)\:_{\mu}^{\pi}(\mathit{ax}_{<t}\mathit{ax}_{t:m}).}\\ \end{array}
$$

As the sum is monotonically increasing in m, and finitely upper bounded, the
limit always exists. For t = 1 we drop the interaction history from the notation
and simply write Vγπµ.

$$
m,
$$

$$
t=1
$$

$$
V_{\gamma}^{\pi\mu}
$$

One of the most common ways to set the discount parameters is to decrease
them geometrically into the future. That is, set ∀i : γi:= αi for some discount
rate α ∈ (0, 1). By increasing α towards 1 we weight long term rewards more
heavily, conversely by reducing it we weight them less so. Thus, the parameter
α controls how short term greedy, or long term farsighted, the agent should
be.

$$
\forall i:\gamma_{i}:=\alpha^{i}
$$

$$
\alpha\in(0,1)
$$

$$
\alpha
$$

2.9.2 Example. Consider again the two agents from Example 2.9.1. As the
rewards are deterministic for π1 we can drop the expectation,

$$
\pi^{1}
$$

$$
V_{\gamma}^{\pi^{1}\mu}=\sum_{i=1}^{\infty}\alpha^{i}0.5=0.5A,
$$

α
where A := is from the standard formulae for geometric series. On the
1−α
other hand for agent π2,

$$
A:=\frac{\alpha}{1-\alpha}
$$

$$
V_{\gamma}^{\pi^{2}\mu}=\sum_{i=1}^{90}\alpha^{i}0.1+\sum_{i=91}^{\infty}\alpha^{i}=0.1A(1-\alpha^{90})+A\alpha^{90}.
$$

Equating the two and then solving, we find that
discounted reward than π1 when α >

π2 has higher expected future
√
90
4/9 ≈ 0.991.

$$
\pi^{2}
$$

$$
\pi^{1}
$$

$$
\alpha>\sqrt[90]{4/9}\approx0.991
$$

$$
\diamond
$$

A major advantage of geometric discounting is that it is mathematically
convenient to work with. Indeed, it is what we will use in Chapter 6 for our
reinforcement learning algorithm. In the present context, however, we want
to keep the development fairly general and thus we will leave the structure
of γ unspecified. An even more general approach is to consider the space of
all bounded enumerable discount sequences. We will take this approach when
formally defining intelligence in Chapter 4 as it will allow us to completely
remove γ from the model. Here we will follow the more conventional approach
to AIXI and simply take γ to be a free parameter.

$$
\gamma
$$

$$
\gamma
$$

$$
\gamma
$$

Having formalised the agent’s temporal preference in terms of γ, we can now
define the optimal agent:

$$
\gamma
$$

2.9.3 Definition. The optimal agent for an environment µ and discounting γ is the agent πµ that has maximal expected future discounted reward.
Formally,
πµ:= arg max V.

$$
\mu
$$

$$
\gamma
$$

$$
\pi^{\mu}
$$

$$
\pi^{\mu}:=\arg\max_{\pi}V_{\gamma}^{\pi\mu}.
$$

The superscript µ emphasises the fact that the agent is optimal with respect
to the specific environment µ. This optimality is possible because the agent
was constructed using µ. In a sense the agent knows what its environment
is before it has even interacted with it. This is similar to Section 2.7 where
the optimal sequence predictor was defined using the distribution that was
generating the sequence to be predicted.

$$
\mu
$$

$$
\mu
$$

$$
\mu.
$$

To understand how the optimal agent πµ behaves in each cycle, we first
express the value function in a recursive form for an arbitrary agent π. From
the definition of V,
∑

$$
\pi^{\mu}
$$

$$
\pi
$$

$$
V
$$

$$
\begin{align*}V_{\gamma}^{\pi\mu}(ax_{<t})\;&=\;\lim_{m\to\infty}\sum_{ax_{t:m}}(\gamma_t r_t+\cdots+\gamma_m r_m)\;_{\mu}^{\pi}(ax_{<t}\underline{ax}_{t:m})\\&=\;\sum_{ax_t}\left[\lim_{m\to\infty}\sum_{ax_{t+1:m}}(\gamma_t r_t+\cdots+\gamma_m r_m)\;_{\mu}^{\pi}(ax_{1:t}\underline{ax}_{t+1:m})\right]_{\mu}^{\pi}(ax_{<t}\underline{ax}_t)\\&=\;\sum_{ax_t}\left[\gamma_t r_t+V_{\gamma}^{\pi\mu}(ax_{1:t})\right]_{\mu}^{\pi}(ax_{<t}\underline{ax}_t).\end{align*}
$$

(2.1)

In the first step we broke cycle t off both the sum and πµ. As these do not
involve m, we pushed them outside the square brackets and moved the limit

$$
\pi\cdot
m,
$$

2. Universal Artificial Intelligence

inside. In the second step we broke off the first discounted reward and dropped
the sum for this term as it was redundant. The remaining discounted rewards
are just V with t advanced by one, thus producing the desired recursion in V.

This is essentially a discrete time form of the Bellman equation commonly
used in control theory, finance, reinforcement learning and other fields concerned with optimising dynamic systems (Bellman, 1957; Sutton and Barto,
1998). Usually it is assumed that the environment is Markovian and thus only
a limited history needs to be taken into account. Here, however, we include
the entire interaction history and thus are able to avoid these restrictions on
the environment. Again, this is to keep the model as general as possible.

Consider now how at is chosen by the optimal agent πµ. By definition, the
optimal action is the one that maximises V. Therefore πµ(ax<tat)=1 for
the expected future discounted reward maximising action, and zero otherwise
(ties can be broken arbitrarily).∑Thus, after expanding Equation (2.1) with π
replaced by πµ, we can replaceat and πµ(ax<tat) with simply a maximum
over the possible actions,

$$
a_{t}
$$

$$
\pi^{\mu}
$$

$$
\pi^{\mu}(ax_{<t}\underline{a}_{t})=1
$$

$$
\pi
$$

$$
\pi^{\mu}
$$

$$
\sum_{a_{t}}
$$

$$
\pi^{\mu}(a x_{<t}\underline{{a}}_{t})
$$

$$
\begin{align*}V_{\gamma}^{\pi^{\mu}\mu}(ax_{<t})&=\sum_{a_{t}}\sum_{x_{t}}\Big[\gamma_{t}r_{t}+V_{\gamma}^{\pi^{\mu}\mu}(ax_{1:t})\Big]\pi^{\mu}(ax_{<t}\underline{a_{t}})\mu(ax_{<t}\underline{a_{t}})\\&=\max_{a_{t}}\sum_{x_{t}}\Big[\gamma_{t}r_{t}+V_{\gamma}^{\pi^{\mu}\mu}(ax_{1:t})\Big]\mu(ax_{<t}\underline{a_{t}})\\&=\max_{a_{t}}\sum_{x_{t}}\cdots\max_{a_{m}}\sum_{x_{m}}\Big[\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}+V_{\gamma}^{\pi^{\mu}\mu}(ax_{1:m})\Big]\mu(ax_{<t}\underline{a_{t}}).\end{align*}
$$

In the last step we have simply unfolded the recursion in V for the first m
cycles. As m → ∞ the term Vγπµµ(ax1:m) → 0. Thus, if we take the limit
m →∞ above we can drop V without affecting the result. It follows then that
the action taken by the optimal policy πµ in the tth cycle is,

$$
m\to\infty
$$

$$
V_{\gamma}^{\pi^{\mu}\mu}(a x_{1:m})\rightarrow0
$$

$$
m\to\infty
$$

$$
\pi^{\mu}
$$

$$
t^{th}
$$

$$
a_{t}^{\pi^{\mu}}:=\arg\operatorname*{m a x}_{a_{t}}\operatorname*{l i m}_{m\to\infty}\sum_{x_{t}}\operatorname*{m a x}_{a_{t+1}}\sum_{x_{t+1}}\cdots\operatorname*{m a x}_{a_{m}}\sum_{x_{m}}\left[\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}\right]\mu(a x_{<t}a\underline{{x}}_{t:m}).
$$

If there is more than one maximising action in cycle t, we simply select one of
these in an arbitrary way.

Intuitively, in the above equation we can see that the optimal agent takes
the distribution µ, and in effect does a brute force search through all possible
futures looking for the action in the current cycle that maximises the expected
future discounted reward. The agent knows that the environment will always
respond according to the distribution µ, thus in each cycle it takes the expectation by summing over all the possible observations x and weighting these by
their probability according to µ. Furthermore, as the agent always follows an
optimal strategy, its own future actions are just a series of value maximising
actions.

$$
\mu,
$$

$$
\mu,
$$

$$
\mu.
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
