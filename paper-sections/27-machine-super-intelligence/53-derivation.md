---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6.2. Derivation
section_role: other
section_index: 53
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "The empirical future discounted reward of a state sk is the sum of actual rewards following from state sk in time steps k,k + 1,..., where the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.2. Derivation

> Section 53 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

The empirical future discounted reward of a state sk is the sum of actual
rewards following from state sk in time steps k,k + 1,..., where the rewards
are discounted as they go into the future. Formally, the empirical value of
state sk at time k for k = 1,...,t is,

$$
s_{k}
$$

$$
s_{k}
$$

$$
k,k+1,\ldots
$$

$$
s_{k}
$$

$$
v_{k}:=\sum_{u=k}^{\infty}\gamma^{u-k}r_{u},
$$

(6.3)

where the future rewards ru are geometrically discounted by γ < 1. In practice
the exact value of vk is always unknown to us as it depends not only on rewards
that have been already observed, but also on unknown future rewards. Note
that if sm = sn for m = n, that is, we have visited the same state twice at
different times m and n, this does not imply that vn = vm as the observed
rewards following the state visit may be different each time.

$$
r_{u}
$$

$$
\gamma<1
$$

$$
v_{k}
$$

$$
s_{m}=s_{n}
$$

$$
m\neq n
$$

$$
n,
$$

$$
v_{n}=v_{m}
$$

Our goal is that for each state s the estimate Vst should be as close as possible
to the true expected future discounted reward V s. Thus, for each state s we
would like Vs to be close to vk for all k such that s = sk. Furthermore, in
non-stationary environments we would like to discount old evidence by some
parameter λ ∈ (0, 1]. Formally, we want to minimise the loss function,

$$
V_{s}^{t}
$$

$$
\tilde{\overline{V}}_{s}
$$

$$
V_{s}
$$

$$
v_{k}
$$

$$
s=s_{k}
$$

$$
\lambda\in(0,1]
$$

$$
L:=\frac{1}{2}\sum_{k=1}^{t}\lambda^{t-k}\big(v_{k}-V_{s_{k}}^{t}\big)^{2}.
$$

(6.4)

For stationary environments we may simply set λ = 1 a priori.

$$
\lambda=1
$$

As we wish to minimise this loss, we take the partial derivative with respect
to the value estimate of each state and set to zero,

$$
\frac{\partial L}{\partial V_{s}^{t}}=-\sum_{k=1}^{t}\lambda^{t-k}\big(v_{k}-V_{s_{k}}^{t}\big)\delta_{s_{k}s}=V_{s}^{t}\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}-\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}v_{k}=0,
$$

where we could change Vstk into Vst due to the presence of the Kronecker δsks,
defined δxy:= 1 if x = y, and 0 otherwise. By defining a discounted state visit
∑t
counter Nst:=k=1λt−kδskswe get

$$
V_{s_{k}}^{t}
$$

$$
V_{s}^{t}
$$

$$
\delta_{xy}:=1
$$

$$
\delta_{s_{k}s},
$$

$$
x=y
$$

$$
\widetilde{N_{s}^{t}}:=\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}
$$

$$
V_{s}^{t}N_{s}^{t}=\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}v_{k}.
$$

(6.5)

Since vk depends on future rewards rk, Equation (6.5) can not be used in
its current form. Next we note that vk has a self-consistency property with
respect to the rewards. Specifically, the tail of the future discounted reward
sum for each state depends on the empirical value at time t in the following
way,
∑t−1

$$
v_{k}
$$

$$
r_{k}
$$

$$
v_{k}
$$

$$
v_{k}=\sum_{u=k}^{t-1}\gamma^{u-k}r_{u}+\gamma^{t-k}v_{t}.
$$

Substituting this into Equation (6.5) and exchanging the order of the double
sum,

$$
\begin{array}{r c l}{V_{s}^{t}N_{s}^{t}}&{=}&{\sum_{u=1}^{t-1}\sum_{k=1}^{u}\lambda^{t-k}\delta_{s_{k}s}\gamma^{u-k}r_{u}+\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}\gamma^{t-k}v_{t}}\\ {}&{=}&{\sum_{u=1}^{t-1}\lambda^{t-u}\sum_{k=1}^{u}(\lambda\gamma)^{u-k}\delta_{s_{k}s}r_{u}+\sum_{k=1}^{t}(\lambda\gamma)^{t-k}\delta_{s_{k}s}v_{t}}\\ {}&{=}&{R_{s}^{t}+E_{s}^{t}v_{t},}\\ \end{array}
$$

∑t
where Est:=k=1(λγ)t−kδsksis the eligibility trace of state s, and Rst:=
∑t−1
u=1λt−uEsuru is the discounted reward with eligibility.

$$
E_{s}^{t}:=\sum_{k=1}^{t}(\lambda\gamma)^{t-k}\delta_{s_{k}s}
$$

$$
s,
$$

$$
R_{s}^{t}:=
\sum_{u=1}^{t-1}\lambda^{t-u}E_{s}^{u}r_{u}
$$

Est and Rst depend only on quantities known at time t. The only unknown
quantity is vt, which we have to replace with our current estimate of this value
at time t, which is Vstt. In other words, we bootstrap our estimates. This gives
us,
V N = Rt + E V.

$$
E_{s}^{t}
$$

$$
R_{s}^{t}
$$

$$
v_{t}
$$

$$
V_{s_{t}}^{t}
$$

$$
t,
$$

$$
V_{s}^{t}N_{s}^{t}=R_{s}^{t}+E_{s}^{t}V_{s_{t}}^{t}.
$$

(6.6)

For state s = st, this simplifies to

$$
s=s_{t}
$$

$$
V_{s_{t}}^{t}=\frac{R_{s_{t}}^{t}}{N_{s_{t}}^{t}-E_{s_{t}}^{t}}.
$$

Substituting this back into Equation (6.6) we obtain,

$$
V_{s}^{t}N_{s}^{t}=R_{s}^{t}+E_{s}^{t}\frac{R_{s_{t}}^{t}}{N_{s_{t}}^{t}-E_{s_{t}}^{t}}.
$$

(6.7)

This gives us an explicit expression for our V estimates. However, from an
algorithmic perspective an incremental update rule is more convenient. To
derive this we make use of the relations,

$$
\begin{array}{r l}{N_{s}^{t+1}=}&{\lambda N_{s}^{t}+\delta_{s_{t+1}s},\qquad\quad N_{s}^{0}=0,}\\ {E_{s}^{t+1}=}&{\lambda\gamma E_{s}^{t}+\delta_{s_{t+1}s},\qquad\quad E_{s}^{0}=0,}\\ {R_{s}^{t+1}=}&{\lambda R_{s}^{t}+\lambda E_{s}^{t}r_{t},\qquad\quad R_{s}^{0}=0,}\end{array}
$$

Inserting these into Equation (6.7) with t replaced by t + 1,

$$
\begin{align*}V_{s}^{t+1}N_{s}^{t+1}\quad&=\quad R_{s}^{t+1}+E_{s}^{t+1}\frac{R_{s_{t+1}}^{t+1}}{N_{s_{t+1}}^{t+1}-E_{s_{t+1}}^{t+1}}\\&=\quad\lambda R_{s}^{t}+\lambda E_{s}^{t}r_{t}+E_{s}^{t+1}\frac{R_{s_{t+1}}^{t}+E_{s_{t+1}}^{t}r_{t}}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}.\end{align*}
$$

By solving Equation (6.6) for Rst and substituting back in,

$$
R_{s}^{t}
$$

$$
\begin{aligned}{V_{s}^{t+1}N_{s}^{t+1}}&{{}=\lambda\big(V_{s}^{t}N_{s}^{t}-E_{s}^{t}V_{s_{t}}^{t}\big)+\lambda E_{s}^{t}r_{t}+E_{s}^{t+1}\frac{N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-E_{s_{t+1}}^{t}V_{s_{t}}^{t}+E_{s_{t+1}}^{t}r_{t}}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}}\\ {}&{{}=\;\big(\lambda N_{s}^{t}+\delta_{s_{t+1}s}\big)V_{s}^{t}-\delta_{s_{t+1}s}V_{s}^{t}-\lambda E_{s}^{t}V_{s_{t}}^{t}+\lambda E_{s}^{t}r_{t}}\\ {}&{{}\quad+E_{s}^{t+1}\frac{N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-E_{s_{t+1}}^{t}V_{s_{t}}^{t}+E_{s_{t+1}}^{t}r_{t}}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}.}\\ \end{aligned}
$$

Dividing through by Nst+1(= λNst+ δst+1s),

$$
N_{s}^{t+1}(=\lambda N_{s}^{t}+\delta_{s_{t+1}s}).
$$

$$
\begin{aligned}V_{s}^{t+1}=V_{s}^{t}&+\frac{-\delta_{s_{t+1}s}V_{s}^{t}-\lambda E_{s}^{t}V_{s_{t}}^{t}+\lambda E_{s}^{t}r_{t}}{\lambda N_{s}^{t}+\delta_{s_{t+1}s}}\\&+\frac{(\lambda\gamma E_{s}^{t}+\delta_{s_{t+1}s})(N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-E_{s_{t+1}}^{t}V_{s_{t}}^{t}+E_{s_{t+1}}^{t}r_{t})}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}+\delta_{s_{t+1}s})}.\end{aligned}
$$

Making the first denominator the same as the second, then expanding the
numerator,

$$
\begin{aligned}&V_{s}^{t+1}=V_{s}^{t}{+}\frac{\lambda E_{s}^{t}r_{t}N_{s_{t+1}}^{t}-\lambda E_{s}^{t}V_{s_{t}}^{t}N_{s_{t+1}}^{t}-\delta_{s_{t+1}s}V_{s}^{t}N_{s_{t+1}}^{t}-\lambda\gamma E_{s_{t+1}}^{t}E_{s}^{t}r_{t}}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}{+}\delta_{s_{t+1}s})}\\ &\\ &\quad{+}\frac{\lambda\gamma E_{s_{t+1}}^{t}E_{s}^{t}V_{s_{t}}^{t}+\gamma E_{s_{t+1}}^{t}V_{s}^{t}\delta_{s_{t+1}s}+\lambda\gamma E_{s}^{t}N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-\lambda\gamma E_{s}^{t}E_{s_{t+1}}^{t}V_{s_{t}}^{t}}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}{+}\delta_{s_{t+1}s})}\\ \end{aligned}
$$

$$
+\frac{\lambda\gamma E_{s}^{t}E_{s_{t+1}}^{t}r_{t}+\delta_{s_{t+1}s}N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-\delta_{s_{t+1}s}E_{s_{t+1}}^{t}V_{s_{t}}^{t}+\delta_{s_{t+1}s}E_{s_{t+1}}^{t}r_{t}}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}+\delta_{s_{t+1}s})}.
$$

After cancelling equal terms (keeping in mind that in every term with a Kronecker δxy factor we may assume that x = y as the term is always zero otherwise), and factoring out Est the right hand side becomes,
()

$$
\delta_{xy}
$$

$$
E_{s}^{t}
$$

$$
x=y
$$

$$
V_{s}^{t}+\frac{E_{s}^{t}\left(\lambda r_{t}N_{s_{t+1}}^{t}-\lambda V_{s_{t}}^{t}N_{s_{t+1}}^{t}+\gamma V_{s}^{t}\delta_{s_{t+1}s}+\lambda\gamma N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-\delta_{s_{t+1}s}V_{s_{t}}^{t}+\delta_{s_{t+1}s}r_{t}\right)}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}+\delta_{s_{t+1}s})}
$$

Finally, by factoring out λNstt+1 + δst+1

swe obtain our update rule,
()

$$
\lambda N_{s_{t+1}}^{t}+\delta_{s_{t+1}s}
$$

(6.8)

$$
V_{s}^{t+1}=V_{s}^{t}+E_{s}^{t}\beta_{t}(s,s_{t+1})\left(r_{t}+\gamma V_{s_{t+1}}^{t}-V_{s_{t}}^{t}\right),
$$

where the learning rate is given by,

$$
\beta_{t}(s,s_{t+1})\quad:=\quad\frac{1}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}\quad\frac{N_{s_{t+1}}^{t}}{N_{s}^{t}}.
$$

(6.9)

Examining Equation (6.8), we find the usual update equation for temporal
difference learning with eligibility traces (see Equation (6.2)), however the
learning rate α has now been replaced by βt(s,st+1). This learning rate was
derived by minimising the squared loss between the estimated and true state
value. In the derivation we have exploited the fact that the latter must be
self-consistent and then bootstrapped to get Equation (6.6). This gives us an
equation for the learning rate for each state transition at time t, as opposed to
the standard temporal difference learning where the learning rate α is either
a fixed free parameter for all transitions, or is decreased over time by some
monotonically decreasing function. In either case, the learning rate is not
automatic and must be experimentally tuned for good performance. The above
derivation appears to theoretically solve this problem.

$$
\beta_{t}(s,s_{t+1})
$$

The first term in βt seems to provide some type of normalisation to the
learning rate, though the intuition behind this is not clear to us. The meaning
of second term however can be understood as follows: Nst measures how often
we have visited state s in the recent past. Therefore, if Nst ≪ Nstt+1 then
state s has a value estimate based on relatively few samples, while state st+1
has a value estimate based on relatively many samples. In such a situation,
the second term in βt boosts the learning rate so that Vst+1 moves more aggressively towards the presumably more accurate rt + γVstt+1. In the opposite
situation when st+1 is a less visited state, we see that the reverse occurs and
the learning rate is reduced in order to maintain the existing value of Vs.

$$
\beta_{t}
$$

$$
N_{s}^{t}
$$

$$
N_{s}^{t}\ll N_{s_{t+1}}^{t}
$$

$$
s_{t+1}
$$

$$
V_{s}^{t+1}
$$

$$
\beta_{t}
$$

$$
r_{t}+\gamma V_{s_{t+1}}^{t}
$$

$$
s_{t+1}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
