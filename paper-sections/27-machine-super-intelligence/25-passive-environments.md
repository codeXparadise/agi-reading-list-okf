---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.1. Passive environments
section_role: other
section_index: 25
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "The first class of environments we will consider is the class of passive environments. Loosely speaking, such environments are not affected by the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.1. Passive environments

> Section 25 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

The first class of environments we will consider is the class of passive environments. Loosely speaking, such environments are not affected by the agent’s
actions. We will be more interested in the active environments to be described
in later sections.

3.1.1 Definition. A Bernoulli scheme is an environment (A, X,µ) such
that ∀ax1:k,
µ(ax ax) = µ(x).

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(\underline{x}_{k}).
$$

As the random variables x1,x2,... are independent and identically distributed
(i.i.d.), one may think of a Bernoulli scheme as being an i.i.d. process.

$$
x_{1},x_{2},..
$$

$$
\left(i.i.d.\right)
$$

The above definition involves some slight abuse of notation. Essentially,
what we are showing is that an equivalent measure with the same name (on the
right hand side) can be defined over a reduced parameter space by dropping the
parameters that have no effect on the value of the original measure (on the left
hand side). In other words, the equation above indicates that the distribution
µ over xk can be defined in a way that it is completely independent of the
history ax<kak.

$$
\mu
$$

$$
x_{k}
$$

$$
ax_{<k}a_{k}
$$

Note also that we have written (A, X,µ) in order to specify the action and
perception spaces associated with the measure. This will be necessary in this
chapter as we will often need to consider relationships between environments
that differ in their action and perception spaces.

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

3.1.2 Example. Many simple stochastic processes can be described as
Bernoulli schemes. Imagine a game where a 6 sided die is thrown repetitively.
The agent receives a reward of 1 whenever a 6 is thrown, and 0 otherwise.
There are no actions that the agent can take. Formally, A := {ǫ}, O :=
{1, 2, 3, 4, 5, 6} and R := B. The measure is defined ∀ax1:k,
{

$$
\mathcal{A}\;:=\;\{\epsilon\},\;\mathcal{O}\;:=
\mathcal{R}:=\mathbb{B}
$$

$$
\forall\mathit{ax}_{1:k}
$$

$$
\mu(\underline{{x}}_{k}):=\left\{\begin{array}{l l}{\frac{1}{6}}&{\mathrm{for}x_{k}=o_{k}r_{k}\in\{(1,0),(2,0),(3,0),(4,0),(5,0),(6,1)\},}\\ {0}&{\mathrm{otherwise}.}\\ \end{array}\right.
$$

Other than perhaps a constant environment, Bernoulli schemes are about
the simplest environments possible. Despite their simplicity, they are important in statistics where sets of i.i.d. random variables play an important role.
For example, sampling from a population should ideally produce individuals
that are both independent of each other, and come from the same underlying
distribution.

A natural generalisation of Bernoulli schemes is to allow the next perception to depend on the previous observation. This gives us a richer class of
environments where the distribution over perceptions can change with time:

3.1.3 Definition. A Markov chain is an environment (A, X,µ) that is a
Bernoulli scheme ∀ax1, and ∀ax1:k with k > 1,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1}
$$

$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{k-1}\underline{x}_{k}).
$$

For a Markov chain the last observation completely defines the system’s
state and so these outputs are usually referred to as states. In more general classes of environments this is not the case, so for consistency we will use our
usual terminology of observations and perceptions. Note that we treat the
first cycle as a special case as there is no previous perception to condition on.
By requiring the system to be a Bernoulli scheme in the first cycle we ensure
that the first action has no effect.

3.1.4 Example. Imagine a game where we have a ring shaped playing board
that has been divided into 20 different cells. There is a pebble that starts in
cell 1 and moves around the board as follows: On each turn a standard six
sided die is thrown to decide how many positions the pebble will be moved
clockwise around the board. In cells 5 and 15 the agent receives a reward of
1. Otherwise the reward is 0.

We can model this system as a Markov chain. Let A := {ǫ}, O :=
{0, 1, 2,..., 19}, R := B. For k = 1 the pebble is in cell 1 and thus ∀ax1,
{

$$
\mathcal{A}\;:=\;\{\epsilon\},\;\mathcal{O}\;:=
\{0,1,2,\ldots,19\},\mathcal{R}:=\mathbb{B}
$$

$$
\forall ax_{1}
$$

$$
\mu(\underline{{x}}_{1}):=\left\{\begin{array}{l l}{1}&{\mathrm{f o r~}o_{1}=1\wedge r_{1}=0,}\\ {0}&{\mathrm{o t h e r w i s e.}}\end{array}\right.
$$

Now define ∀ax1:k with k > 1,
 {

$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(o_{k-1}\underline{{x}}_{k}):=\left\{\begin{array}{l l}{\frac{1}{6}}&{\operatorname{for}o_{k}\in\big\{(o_{k-1}+1)\bmod20,\ldots,(o_{k-1}+6)\bmod20\big\}}\\ {}&{\wedge r_{k}=\delta_{5,o_{k}}+\delta_{15,o_{k}},}\\ {0}&{\operatorname{otherwise}.}\\ \end{array}\right.
$$

1
In this game there is a chance of obtaining reward if the pebble is currently
6
in one of the six cells before either cell 5 or cell 15.

$$
\frac{1}{6}
$$

From the definitions of Bernoulli schemes and Markov chains it is clear that
in both of these classes an agent is “passive”, in the sense that its actions have
no effect on the environment’s behaviour. The difference between the two
classes is the size of the history that is relevant to determining the next perception. Increasing the length of this history to the full history of observations
gives us the most general class of completely passive environments:

3.1.5 Definition. A Totally Passive Environment is an environment
(A, X,µ) such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall a x_{1:k}
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{<k}\underline{x}_{k}).
$$

By construction, this class of environments is a superset of the classes of
environments defined thus far. We could define a more limited version of this
class where the next perception only depends on the last n observations, rather
than the full history. However, such an environment is mathematically equivalent to a standard Markov chain where for each history of length n we create
a unique observation in an enlarged observation space. In this new space the
environment can then be represented by a first order Markov chain. This reduction technique will be used in a more general setting to prove Lemma 3.2.6.

3. Taxonomy of Environments

While totally passive environments are useful in modelling some systems,
in terms of artificial intelligence they are relatively uninteresting because the
agent cannot do anything. We can relax this constraint just a little by only
requiring that the agent cannot affect future observations:

3.1.6 Definition. A Passive Environment is an environment (A, X,µ)
such that ∀ax<kaok,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall\underline{ax}_{<k}\underline{\omega}_{k}
$$

$$
\mu(a x_{<k}a\underline{o}_{k})=\mu(o_{<k}\underline{o}_{k}).
$$

Note that there are no restrictions on the rewards; the environment is free
to reward or punish the agent in any way. Totally passive environments are
clearly a special case of passive environments. For more on AIXI in passive
environments see Section 5.3.2 of (Hutter, 2005).

Another important special case is the class of problems where the agent is
rewarded for correctly predicting a sequence that it cannot influence:

3.1.7 Definition. A Sequence Prediction Problem is a passive environment (A, X,µ) such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a o\underline{{r}}_{k})=\mu(a o\underline{{r}}_{k}).
$$

That is, the reward in each cycle depends entirely on the action and the
observation that immediately follows it. As sequence prediction environments
are passive the observations do not depend on the agent’s actions, however
there is no limit on how long the relevant observation history can be. The
above definition makes precise what we meant in previous chapters where
sequence prediction problems were referred to as being “passive”. For more on
how AIXI deals with sequence prediction problems see Section 6.2 of (Hutter,
2005).

3.1.8 Example. Let A = O := {0, 1,..., 9}. Define ∀ax1:k,

$$
\mathcal{A}=\mathcal{O}:=\{0,1,\ldots,9\}
$$

$$
\mu(o_{<k}\underline{{o}}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{i f~}o_{k}\mathrm{~t h e~}k^{t h}\mathrm{~d i g i t~i n~}3.141592\ldots,}\\ {0}&{\mathrm{otherwise},}\\ \end{array}\right.
\mu(\mathit{aor}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{if}r_{k}=1-\frac{1}{9}|o_{k}-a_{k}|,}\\ {0}&{\mathrm{otherwise}.}\end{array}\right.
$$

and

Thus, in order to maximise reward, the agent must generate successive digits
of the mathematical constant π. A correct digit gets a reward of 1, while an
incorrect digit gets a lesser reward proportional to the difference between the
correct digit and the guess.

$$
\pi.\ A
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
