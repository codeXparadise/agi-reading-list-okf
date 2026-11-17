---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.6. Universal inference
section_role: other
section_index: 18
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "As we saw in Section 2.2, Bayes’ rule partially solves the induction problem by providing an equation for updating beliefs. This is only a partial…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.6. Universal inference

> Section 18 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

As we saw in Section 2.2, Bayes’ rule partially solves the induction problem
by providing an equation for updating beliefs. This is only a partial solution
because it leaves open two important issues: how do we choose the class of
hypotheses H, and what prior distribution PH should we use over this class?
Various principles and methods have been proposed to solve these problems,
however they tend to run into trouble, especially for large H. In this section
we will look at how taking the universal prior PMe over the hypothesis space
Me theoretically solves these problems.

$$
\mathcal{H}
$$

$$
P_{\mathcal{H}}
$$

$$
P_{\mathcal{M}_{e}}
$$

$$
\mathcal{M}_{e}
$$

When approaching an inductive inference problem from a Bayesian perspective, the first step is to define H. The most obvious consideration is that H
should be large enough to contain the correct hypothesis, or at least a sufficiently close one. Being forced to expand our initial H due to new evidence
is problematic as both the redistribution of the prior probabilities, and the
way in which H is extended, can bias the induction process. In order to avoid
these problems, we should make sure that H is large enough to contain a good
hypothesis to start with. One solution is to simply choose H to be very large,
as we did in the previous section where we set H = Me. As this contains all
computable stochastic hypotheses, a larger hypothesis space should never be
required.

$$
\mathcal{H}.
$$

$$
\mathcal{H}=\mathcal{M}_e
$$

Having selected H, the next problem is to define a good prior distribution
over this space. Essentially, a prior distribution PH over a space of hypotheses
H is an expression of how likely we think different hypotheses are before taking
the data into account. If this prior knowledge is easily quantifiable we can use
it to construct a prior. In the case of PMe this simply means taking the
conditional form of the Kolmogorov complexity function and conditioning on
this prior information.

$$
\mathcal{H}.
$$

$$
P_{\mathcal{H}}
$$

$$
\mathcal{H}
$$

$$
P_{\mathcal{M}_{e}}
$$

More often, however, we either have insufficient prior information to construct a prior, or we simply wish the data to ‘speak for itself’. The latter
case is important when we want to present our findings to others who may
not share our prior beliefs. The standard solution is to select a prior that
is in some sense neutral about the relative likelihood of different hypotheses.
This is known as the indifference principle. It is what we applied in the coin estimation problem in Example 2.3.2 when we set P (νp) := |H|−1 = 31. That
is, we simply assumed that a priori all hypotheses were equally likely.

$$
P(\nu_{p}):=|\mathcal{H}|^{-1}=\frac{1}{3}
$$

The indifference principle works well for small discrete H, however if we
extend the concept to even small continuous parametrised classes by defining
a probability density function in terms of the volume of H, problems start to
arise. Consider again the coin problem, however this time allow the bias of
the coin to be θ ∈ [0, 1]. By the indifference principle the prior is the uniform
probability density P (νθ) = 1. Now consider what happens if we look at this
coin estimation problem in a different way, where the parameter of interest
√
is actually θ′:= θ. Obviously, if we take a uniform prior over θ′ this is
not equivalent to taking a uniform prior over θ. In other words, the way in
which we view a problem, and thus the way in which we parametrise it, affects
the prior probabilities assigned by a ‘uniform prior’. Obviously this is not as
neutral and objective as we would like.

$$
\mathcal{H}
$$

$$
\theta\in[0,1]
$$

$$
P(\nu_{\theta})=1
$$

$$
\theta^{\prime}\;:=\;\sqrt{\theta}.
$$

$$
\theta.
$$

$$
\theta^{\prime}
$$

Consider how the algorithmic prior probability PMe behaves under a simple
reparametrisation. Let H := {νθ ∈ Mc: θ ∈ Θ} be a set of probability
measures indexed by a parameter θ ∈ Θ, and define θ′:= f (θ) where f is
a computable bijection. It is an elementary fact of Kolmogorov complexity
+ +
theory that K(f (θ)) < K(θ) + K(f), and similarly K(f−1(θ′)) < K(θ′) +
+
K(f), from which it follows that K(θ) = K(θ′). With a straight forward
extension, the same argument can be applied to the Kolmogorov complexity
+
of the indexed measures, resulting in K(νθ) = K(νθ′). From Definition 2.5.3
we then see that,

$$
P_{\mathcal{M}_e}
$$

$$
\mathcal{H}:=\left\{\nu_{\theta}\in\mathcal{M}_{c}:\theta\in\Theta\right\}
$$

$$
\theta\in\Theta
$$

$$
\theta^{\prime}\;:=\;f(\theta)
$$

$$
K(f(\theta))\stackrel{+}{<}K(\theta)+K(f)
$$

$$
K(f^{-1}(\theta'))\stackrel{+}{<}K(\theta')+
K(f)
$$

$$
K(\theta)\stackrel{+}{=}K(\theta')
$$

$$
K(\nu_{\theta})\triangleq K(\nu_{\theta^{\prime}})
$$

$$
P_{\mathcal{M}_{e}}(\nu_{\theta})\;:=\;2^{-K(\nu_{\theta})}\;\triangleq\;2^{-K(\nu_{\theta^{\prime}})}\;=:\;P_{\mathcal{M}_{e}}(\nu_{\theta^{\prime}}).
$$

That is, for any bijective reparametrisation f the algorithmic prior probability
assigned to parametrised hypotheses is invariant up to a multiplicative constant. If f is simple this constant is small and thus quickly washes out in the
posterior distribution, leaving the inference results essentially unaffected by
the change.

A more difficult version of the above problem occurs when the transformation is non-bijective. For example, define the new parameter θ′:= (θ − 21)2.
1 3
Now θ = and θ = both correspond to the same value of θ′. Unlike
4 4
in the bijective case, non-bijective transformations also cause problems for
finite discrete hypothesis spaces. For example, we might have three hypotheses, H3 := {heads biased, tails biased, fair}. Alternatively, we could
regroup to have just two hypotheses, H2 := {biased, fair}. Both H3 and
H2 cover the full range of possibilities for the coin. However, a uniform prior
1
over H3 assigns a prior probability of to the coin being fair, while a uniform
3
1
prior over H2 assigns a prior probability of just to the same thing.
2

$$
\theta':=(\theta-\frac{1}{2})^2
$$

$$
\theta\;=\;\frac{1}{4}
$$

$$
\theta\;=\;\frac{3}{4}
$$

$$
\theta^{\prime}
$$

$$
\mathcal{H}_{3}:=
\mathcal{H}_{3}
$$

$$
\mathcal{H}_{2}:=\{\mathrm{biased},\mathrm{fair}\}
$$

$$
\mathcal{H}_{2}
$$

$$
\mathcal{H}_{3}
$$

$$
\frac{1}{3}
$$

$$
\mathcal{H}_{2}
$$

$$
\frac{1}{2}
$$

The standard Bayesian approach is to try to find a symmetry group for the
problem and a prior that is invariant under group transformations. However,
in some cases there may be no obvious symmetry, and even if there is the
resulting prior may be improper, meaning that the area under the distribution

2. Universal Artificial Intelligence

is no longer 1. Invariance under group transformations is a highly desirable but
difficult property to attain. Remarkably, under simple group transformations
PMe can be proven to be invariant, again up to a small multiplicative constant.
For a proof of this, as well as further powerful properties of the universial prior
distribution, see the paper that this section is based on (Hutter, 2007a).

$$
P_{\mathcal{M}_e}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
