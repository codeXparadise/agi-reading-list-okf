---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.2. Active environments
section_role: other
section_index: 26
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "The simplest active environment is one where the next perception xk depends on only the last action ak: $$ x{k} $$ $$ a{k} $$ 3.2.1 Definition. A…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.2. Active environments

> Section 26 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

The simplest active environment is one where the next perception xk depends
on only the last action ak:

$$
x_{k}
$$

$$
a_{k}
$$

3.2.1 Definition. A Bandit is an environment (A, X,µ) such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(a\underline{x}_{k}).
$$

This class of environments is named after the bandit machines found in casinos around the world, although the relation to real bandit machines is tenuous.
Bandit environments are weaker than Markov chains as future perceptions do
not depend on past observations. However, they do have the ability to react to the last action, and so in this respect they are more powerful. Even
though bandit problems are conceptually simple, solving them optimally is
surprisingly involved (Berry and Fristedt, 1985; Gittins, 1989).

3.2.2 Example. Imagine a machine that has n different levers, or arms, that
the agent can pull. Each arm has a different but fixed probability of generating
a reward. For this example, let the reward be either 0 or 1. The agent’s task
is to figure out which arm to pull so that it maximises its expected reward.
One approach might be to spend time pulling different arms and collecting
statistics in order to estimate which produces the most reward.

We can formally define this bandit as follows: Let O := {ǫ}, R := B and
let A := {1, 2, 3,...,n} represent the n different arms that the agent can pull.
Let β1,β2,...,βn be the respective probabilities of obtaining a reward of 1
after pulling the corresponding arm. Now define ∀ax1:k,
{

$$
\mathcal{O}:=\{\epsilon\},\mathcal{R}:=\mathbb{B}
$$

$$
\mathcal{A}:=\{1,2,3,\ldots,n\}
$$

$$
\beta_{1},\beta_{2},\ldots,\beta_{n}
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a\underline{x}_{k}):=\left\{\begin{array}{l l}{\beta_{a_{k}}}&{\mathrm{for}r_{k}=1,}\\ {1-\beta_{a_{k}}}&{\mathrm{for}r_{k}=0.}\end{array}\right.
$$

A natural extension to the class of bandits is to allow the next perception
to depend on both the last observation and the last action. This produces a
much more powerful class of environments that has been intensively studied
and has many theoretical and practical applications:

3.2.3 Definition. A (stationary) Markov Decision Process (MDP)
is an environment (A, X,µ) that is a Bernoulli scheme ∀ax1, and ∀ax1:k with
k > 1,
µ(ax ax) = µ(o ax).

$$
\forall ax_{1}
$$

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{k-1}a\underline{x}_{k}).
$$

Usually MDPs are defined in such a way that the agent does not act before
the first perception. However, in our definition the first cycle is a Bernoulli
scheme and so the first action has no effect anyway. Aside from this detail,
our definition is equivalent to the standard definition (Bellman, 1957). It is

3. Taxonomy of Environments

immediately clear that this class generalises Bernoulli schemes, bandits and
Markov chains.

What we have defined above is a stationary MDP. This is because the probability of a perception given the current action and the last perception does
not change, that is, it is independent of k. In some definitions the measure µ
is allowed to vary over time. These non-stationary MDPs can be modelled as
POMDPs, which will be defined shortly.

3.2.4 Example. Consider again the simple Markov chain in Example 3.1.4.
This can be extended to an MDP by allowing the agent to decide whether to
move clockwise or anticlockwise around the board. Let O := {0, 1,..., 19}
and R := B as before, but now A := {,} as the agent can select which
direction to move in. For k = 1 the pebble is in cell 1 and thus ∀ax1,
{

$$
\mathcal{O}:=\{0,1,\ldots,19\}
$$

$$
\mathcal{R}:=\mathbb{B}
$$

$$
\mathcal{A}:=\{\circ,\circ\}
$$

$$
k=1
$$

$$
\mu(a\underline{{x}}_{1}):=\left\{\begin{array}{l l}{1}&{\mathrm{f o r~}o_{1}=1\wedge r_{1}=0,}\\ {0}&{\mathrm{o t h e r w i s e.}}\end{array}\right.
\forall ax_{1}
$$

Now define ∀ax1:k with k > 1,


$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(o_{k-1}\mathit{a}\underline{{x}}_{k}):=\{\begin{array}{c l}{\frac{1}{6}}&{\operatorname{for}o_{k}\in\{(o_{k-1}+1)\bmod20,\ldots,(o_{k-1}+6)\bmod20\}}\\ {}&{\wedge r_{k}=\delta_{5,o_{k}}+\delta_{15,o_{k}}\wedge a_{k}=\circlearrowleft,}\\ {\frac{1}{6}}&{\operatorname{for}o_{k}\in\{(o_{k-1}-1)\bmod20,\ldots,(o_{k-1}-6)\bmod20\}}\\ {}&{\wedge r_{k}=\delta_{5,o_{k}}+\delta_{15,o_{k}}\wedge a_{k}=\circlearrowleft,}\\ {0}&{\operatorname{o t h e r w i s e.}}\\ \end{array}..
$$

A natural way to generalise the class of MDPs is to allow the next perception
to depend on the last n observations and actions:

3.2.5 Definition. A (stationary) nth order Markov Decision Process
is an environment (A, X,µ) that is a Bernoulli scheme ∀ax1, and ∀ax1:k with
k > 1,
µ(ax ax) = µ(o ao ax),

$$
n^{\mathrm{th}}
$$

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1}
$$

$$
\forall a x_{1:k}
$$

$$
k>1
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{k-m}a o_{k-m+1:k-1}a\underline{x}_{k}),
$$

where m := min{n,k}.

$$
m:=\min\{n,k\}
$$

Immediately from the definition we can see that a standard MDP is an nth
order MDP where n = 1. The added complication of the variable m is to allow
for the situation where the current history length k is less than n.

$$
n^{th}
$$

$$
n=1
$$

It might appear that nth order MDPs are more general than standard MDPs,
however it turns out that any nth order MDP can be converted into an equivalent MDP. This is done by extending the observation space and appropriately
modifying the measure. The proof follows the same pattern as the reduction
of nth order Markov chains to standard Markov chains, except that now we
have to deal with the complication of having actions in the history.

$$
n^{th}
$$

$$
n^{th}
$$

$$
n^{th}
$$

3.2.6 Lemma. nth order MDPs can be reduced to MDPs.

$$
n^{th}
$$

$$
\textit{MDPs}
$$

Proof. Let (A, X = O×R,µ) be an nth order MDP. To prove the result
we will define an equivalent first order MDP (A, Z = Q×R, µ˜). We begin by
defining the new observation space,
⋃n

$$
\left(\mathcal{A},\mathcal{X}=\mathcal{O}\times\mathcal{R},\mu\right)
$$

$$
n^{th}
$$

$$
\left(\mathcal{A},\mathcal{Z}=\mathcal{Q}\times\mathcal{R},\tilde{\mu}\right)
$$

$$
\mathcal{Q}:=\bigcup_{i=1}^{n}\mathcal{O}\times(\mathcal{A}\times\mathcal{O})^{i-1}.
$$

Every interaction history that the nth order MDP conditions on is thus uniquely
represented in Q. Although it complicates things, we need to include histories
of length less than n to accommodate the first n − 1 cycles of the system.

$$
n^{th}
$$

$$
\mathcal{Q}
$$

$$
n-1
$$

Next we define a measure µ˜ over the perception space Z, that is equivalent
to the measure µ over the perception space X. We begin by dealing with the
first interaction cycle: ∀az1 ∈A×Z define,
{

$$
\tilde{\mu}
$$

$$
\mathcal{Z},
$$

$$
\mu
$$

$$
\mathcal{X}
$$

$$
\forall a z_{1}\in\mathcal{A}\times\mathcal{Z}
$$

$$
\tilde{\mu}(a\underline{{z}}_{1}):=\left\{\begin{array}{l l}{\mu(a\underline{{z}}_{1})}&{\mathrm{for}z_{1}\in\mathcal{X},}\\ {0}&{\mathrm{otherwise}.}\end{array}\right.
$$

This makes the processes equivalent in the first cycle.

Next, for interaction cycles k > 1, define ∀q


k−1azk ∈Q×A×Z,

$$
\forall q_{k-1}a z_{k}\in\mathcal{Q}\times\mathcal{A}\times\mathcal{Z}
$$

$$
k>1
$$

$$
\tilde{\mu}(q_{k-1}\underline{{\alpha}}_{k}):=\left\{\begin{array}{l l}{\mu(o_{k-m}\mathit{ao}_{k-m+1:k-1}\mathit{a}\underline{{r}}_{k})}&{\mathrm{i f~}q_{k-1}=o_{k-m}\mathit{ao}_{k-m+1:k-1}}\\ {}&{\quad\wedge z_{k}=q_{k}r_{k}}\\ {}&{\quad\wedge q_{k}=o_{k-m+1}\mathit{ao}_{k-m+2:k-1}\mathit{ao}_{k},}\\ {0}&{\mathrm{o t h e r w i s e.}}\\ \end{array}\right.
$$

That is, if the transition qk−1azk is possible when represented in the original
environment, then this transition is given the same probability by µ˜ in the
new environment. Any transition qk−1azk which is impossible in the original
environment, for example because the two histories represented by qk−1 and
qk are inconsistent, is given a transition probability of zero by µ˜. Thus, the
two environments have equivalent structure and dynamics.

$$
q_{k-1}az_{k}
$$

$$
\tilde{\mu}
$$

$$
q_{k-1}az_{k}
$$

$$
q_{k-1}
$$

$$
q_{k}
$$

$$
\tilde{\mu}.
$$

As the proof illustrates, writing down the equation for a higher order MDP
and working with it is cumbersome. Thus, the above result is useful as it means
that we only have to deal with first order MDPs in our analysis. Nevertheless,
conceptually it is often more natural to think of certain problems as being nth
order MDPs.

$$
n^{th}
$$

Rather than increasing the history that the measure conditions on, another
extension is to assume that the agent cannot properly observe the MDP’s
outputs:

3.2.7 Definition. A Partially Observable Markov Decision Process (POMDP) is an environment (A, X = O×R,µ) defined as follows: Let
(A, X˜ = Õ×R, µ˜) be an MDP called the core MDP. Let φ : X×X → ˜ [0, 1] be a
conditional probability measure of the form φ(˜xx) which expresses the probability of perceiving x when the core MDP outputs ˜x. Define ∀ax1:k ∈ (A×X)k,
∑

$$
\left(\mathcal{A},\mathcal{X}=\mathcal{O}\times\mathcal{R},\mu\right)
$$

$$
\left(\mathcal{A},\tilde{\mathcal{X}}=\tilde{\mathcal{O}}\times\mathcal{R},\tilde{\mu}\right)
$$

$$
\phi:\tilde{\mathcal{X}}\times\mathcal{X}\to[0,1]
$$

$$
\phi(\tilde{x}\underline{x})
$$

$$
\forall a x_{1:k}\in(\mathcal{A}\times\mathcal{X})^{k}
$$

$$
\tilde{x}
$$

$$
\mu(a\underline{{x}}_{1:k})\::=\sum_{\tilde{x}_{1:k}\in\tilde{\mathcal{X}}^{k}}\tilde{\mu}(a\underline{{\tilde{x}}}_{1})\:\phi(\tilde{x}_{1}\underline{{x}}_{1})\:\tilde{\mu}(\tilde{o}_{1}a\underline{{\tilde{x}}}_{2})\:\phi(\tilde{x}_{2}\underline{{x}}_{2})\:\cdots\:\tilde{\mu}(\tilde{o}_{k-1}a\underline{{\tilde{x}}}_{k})\:\phi(\tilde{x}_{k}\underline{{x}}_{k}).
$$

3. Taxonomy of Environments

The nature of POMDPs is perhaps best illustrated by example.

3.2.8 Example. Let the core MDP (A, X˜, µ˜) be the MDP defined in Example 3.2.4. Now imagine that the agent cannot reliably observe which cell
the pebble is in. To do this, let X := X˜ and define the observation function
∀x,x ˜ ∈X,
{
61
if x˜ = x,

$$
(\mathcal{A},\tilde{\mathcal{X}},\tilde{\mu})
$$

$$
\mathcal{X}:=\tilde{\mathcal{X}}
$$

$$
\forall\tilde{x},x\in\mathcal{X}
$$

$$
\phi(\tilde{x}\underline{{x}}):=\left\{\begin{array}{l l}{\frac{61}{100}\qquad}&{\mathrm{if}\tilde{x}=x,}\\ {\frac{1}{100}\qquad}&{\mathrm{otherwise}.}\end{array}\right.
$$

Thus, with probability 0.61 the agent observes the true output of the core
MDP. The rest of the time it observes some other randomly chosen output.
The probabilities add up as |X| = |O|×|R| = 20 × 2 = 40. Thus, x can take
39 values other than ˜x.

$$
|\mathcal{X}|=|\mathcal{O}|\times|\mathcal{R}|=20\times2=40
$$

$$
\tilde{x}.
$$

The fact that POMDPs generalise MDPs can be seen by letting X = X˜ and
φ(˜xx) := δx,x˜, in which case it follows that µ = ˜µ. That is, the POMDP reduces
to being its core MDP. Furthermore, as nth order MDPs can be reduced to first
order MDPs, it follows that POMDPs also generalise higher order MDPs.

$$
\mathcal{X}=\tilde{\mathcal{X}}
$$

$$
\phi(\tilde{x}\underline{x}):=\delta_{\tilde{x},x},
$$

$$
\mu=\tilde{\mu}
$$

$$
n^{th}
$$

To see that POMDPs can define non-stationary MDPs, consider a POMDP
where X is a strict subset of X˜. Now use this extra internal information in
the core MDP to keep a parameter that varies over time and that affects the
core MDP’s behaviour. To the external agent who cannot observe this extra
information, it appears that the environment is non-stationary.

$$
\tilde{\mathcal{X}}
$$

Both theoretically and practically this class of environments is difficult to
work with. However, it does encompass a huge variety of possibilities, including all of the environments considered in this chapter, and many real world
problems.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
