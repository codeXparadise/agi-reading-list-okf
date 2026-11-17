---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.5. Solomonoff-Levin prior
section_role: other
section_index: 17
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Besides the prior described in the previous section, Solomonoff also suggested to define a universal prior by taking a mixture of distributions…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.5. Solomonoff-Levin prior

> Section 17 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Besides the prior described in the previous section, Solomonoff also suggested
to define a universal prior by taking a mixture of distributions (Solomonoff,
1964). In the 1970’s this alternate approach was generalised and further developed (Zvonkin and Levin, 1970; Levin, 1974). As Leonid Levin (1948–)
played an important role in this, here we will refer to this as the Solomonoff-
Levin prior. It is closely related to the universal prior in the previous section:
they lie within a multiplicative constant of each other and share key technical
properties.

Although taking mixtures is perhaps less intuitive, it has the advantage
of making important theoretical properties of the prior more transparent. It
also gives an explicit prior over both the hypothesis space and the space of
sequences. The topic is quite technical, however it is worth spending some
time on as it lies at the heart of universal artificial intelligence.

The hypotheses we have been working with up to now have all been probability measures. These can be generalised as follows:

2.5.1 Definition. A semi-measure is a function ν : B∗ → [0, 1] such that,

$$
\nu:\mathbb{B}^{*}\to[0,1]
$$

$$
\nu(\underline{{\epsilon}})\leq1,
$$

$$
\forall x\in\mathbb{B}^*\quad\nu(\underline{x})\geq\nu(\underline{x}\underline{0})+\nu(\underline{x}\underline{1}).
$$

Intuitively one may think of a semi-measure that is not a probability measure
as being a kind of defective probability measure whose probabilities do not
quite add up as they should. This defect can be fixed in the sense that a
semi-measure can be built up to be a probability measure by appropriately
normalising things.

Intuitively, a function is enumerable if it can be progressively approximated
from below. More formally, f : X → R is enumerable if there exists a computable function g : X × N → Q such that ∀x ∈ X, ∀i ∈ N : gi+1(x) ≥ gi(x)
and ∀x ∈ X : limi→∞gi(x) = f (x). Enumerability is weaker than computability because for any x ∈ X we only ever have the lower bound gi(x) on the
value of f (x). Thus we can never know for sure how far our bound is from the
true value of f (x), that is, we do not know how large f (x) − gi(x) might be.

$$
f:X\to\mathbb{R}
$$

$$
g:X\times\mathbb{N}\to\mathbb{Q}
$$

$$
\forall x\in X,\forall i\in\mathbb{N}:g_{i+1}(x)\geq g_i(x)
$$

$$
\forall x\in X:\lim_{i\to\infty}g_i(x)=f(x)
$$

$$
x\in X
$$

$$
g_{i}(x)
$$

$$
f(x)
$$

$$
f(x)-g_i(x)
$$

If a similar condition holds, but with the approximation function converging
to f from above rather than below, we say that f is coenumerable. One
example of such a function is the Kolmogorov complexity function K in the
previous section. If a function is both enumerable and coenumerable, then
we have both upper and lower bounds and thus can compute the value of f
to any required accuracy. In this case we simply say that f is a real valued
computable function. Clearly then, the enumerable functions are a superset of
the computable functions.

Our task is to construct a prior distribution over the enumerable semimeasures. To do this we need to formalise Occam’s razor, and for that we
need to define a way to measure the complexity of enumerable semi-measures.
Solomonoff measured the complexity of sequences according to the length of
their programs, here we can do something similar.

By definition, all enumerable functions can be approximated from below
by a computable function. Thus, it is not too hard to prove that the set of
enumerable functions can be indexed by a Turing machine, and that this can be
further restricted to just the set of enumerable semi-measures. More precisely,
there exists a Turing machine T that for any enumerable semi-measure µ there
exists an index i ∈ N such that ∀x ∈ B∗: µ(x) = νi(x) := limk→∞T (i,k,x)
with T increasing in k. In effect, the index i is a description of µ in that once
we know i we can approximate the value of µ from below for any x by using
the Turing machine T. As k increases, these approximations increase towards
the true value of µ(x). For details on how all this is done see Section 4.5
of (Li and Vit´anyi, 1997) or (Legg, 1997). The main thing we will need is the
computable enumeration of enumerable semi-measures itself, which we will
denote by Me:= ν1,ν2,ν3,.... As all probability measures are semi-measures
by definition, and all computable functions are enumerable, it follows that
the set of enumerable semi-measures is a superset of the set of computable
probability measures. We write Mc to denote an enumeration of just the
computable measures.

$$
\mu
$$

$$
i\in\mathbb{N}
$$

$$
\forall x\in\mathbb{B}^{*}:\mu(\underline{{x}})=\nu_{i}(\underline{{x}}):=\lim_{k\to\infty}T(i,k,x)
$$

$$
\mu
$$

$$
\mu
$$

$$
T
$$

$$
\mu(x)
$$

$$
\mathcal{M}_{e}:=\nu_{1},\nu_{2},\nu_{3},\cdots\mathrm{As}
$$

$$
\mathcal{M}_{c}
$$

2. Universal Artificial Intelligence

Note the two uses of the word “enumerable” above. When we say that a set
can be enumerated, what we mean is that there exists a way to step though all
the elements in this set. When we say that an individual function is enumerable, such as a semi-measure, what we mean is that it can be approximated
from below by a series of computable functions. Some authors avoid this
dual usage by referring to enumerable functions as lower semi-computable. In
this terminology, what Me provides is a computable enumeration of the lower
semi-computable semi-measures. In any case, it is still a mouthful!

$$
\mathcal{M}_{e}
$$

We can now return to the question of how to measure the complexity of
an enumerable semi-measure. As noted above, for νi ∈Me the index i is in
effect a description of νi. At this point, it might seem that the natural thing
to do is to take the value of an enumerable semi-measure’s index to be its
complexity. The problem, however, is that some extremely large index values,
such as 21000, contain a lot less information than far smaller index values which
are not as easily described: for example, an index whose binary representation
is a string of 100 random bits. The solution is that we must measure not
the value, but the information content of the index in order to measure the
complexity of the enumerable semi-measure it describes. We do this by taking
the Kolmogorov complexity of the index. That is, we define the complexity
of an enumerable semi-measure to be the length of the shortest program that
computes its index. Formally,

$$
\nu_{i}\in\mathcal{M}_{e}
$$

$$
\nu_{i}
$$

$$
2^{\overset{\cdot}{1000}}
$$

2.5.2 Definition.

The Kolmogorov complexity of µ ∈Me is,

$$
\mu\in\mathcal{M}_e
$$

$$
K(\mu):=\min_{p\in\mathbb{B}^{*}}\left\{\ell(p):\mathcal{U}(p)=i\right\},
$$

where µ is the ith element in the recursive enumeration of all enumerable
semi-measures Me, and U is a prefix universal Turing machine.

$$
\mu
$$

$$
i^{th}
$$

$$
\mathcal{M}_{e}
$$

$$
\mathcal{U}
$$

In essence this is just an extension of the Kolmogorov complexity function for
strings and sequences (Definition 2.4.3), to enumerable semi-measures. Indeed,
all the key theoretical properties of the complexity function remain the same.
We can again see echos of Solomonoff’s prior for sequences in that enumerable
semi-measures that can be described by short programs are considered to be
simple, while ones that require long programs are complex.

Having defined a suitable complexity measure for enumerable semimeasures, we can now construct a prior distribution over Me in a way that
is similar to what Solomonoff did. As each enumerable semi-measure µ has
some shortest program p ∈ B∗ that specifies its index, we can set the prior
probability of µ to be the probability of randomly generating p by flipping a
coin to get each bit. Formally:

$$
\mathcal{M}_{e}
$$

$$
p\in\mathbb{B}^*
$$

$$
\mu
$$

$$
\mu
$$

2.5.3 Definition. The algorithmic prior probability of µ ∈Me is,

$$
\mu\in\mathcal{M}_e
$$

$$
P_{\mathcal{M}_{e}}(\mu):=2^{-K(\mu)}.
$$

As K is coenumerable, from the definition above we can see that PMe is
enumerable. Thus, this distribution can only be approximated from below.

$$
P_{\mathcal{M}_{e}}
$$

With K as the definition of hypothesis complexity, PMe clearly respects
Occam’s razor as each hypothesis µ ∈Me is assigned a prior probability that
is a decreasing function of its complexity. Furthermore, every enumerable
semi-measure has some shortest program that specifies its index and so ∀µ ∈
Me: K(µ) > 0 and thus ∀µ ∈Me: PMe(µ) > 0. It follows then that for an
induction system based on Bayes’ rule and the prior PMe, the value of P (ν|D)
will be non-zero whenever D is consistent with ν, that is, P (D|ν) > 0. Such
systems will not discard hypotheses that are consistent with the data and thus
respect Epicurus’ principle of multiple explanations.

$$
P_{\mathcal{M}_{e}}
$$

$$
\mu\in\mathcal{M}_e
$$

$$
\forall\mu\in\mathcal{M}_e:P_{\mathcal{M}_e}(\mu)>0
$$

$$
\forall\mu\in
$$

$$
\mathcal{M}_{e}:K(\mu)>0
$$

$$
P_{\mathcal{M}_e}
$$

$$
P(\nu|\mathcal{D})
$$

$$
\nu.
$$

$$
P(\mathcal{D}|\nu)>0
$$

With a prior over our hypothesis space Me, we can now take a mixture to
define a prior over the space of sequences, just as we did in Example 2.3.3:

$$
\mathcal{M}_{e}
$$

2.5.4 Definition. The Solomonoff-Levin prior probability of a binary sequence beginning with the string x ∈ B∗ is,
∑

$$
x\in\mathbb{B}^*
$$

$$
\xi(\underline{x}):=\sum_{\nu\in\mathcal{M}_{e}}P_{\mathcal{M}_{e}}(\nu)\nu(\underline{x}).
$$

Clearly this distribution respects Occam’s razor as sets of sequences which
have high probability under some simple distribution ν, will also have high
probability under ξ, and vice versa.

$$
\nu,
$$

$$
\xi,
$$

It is easy to see that the presence of just one semi-measure in the above
mixture is sufficient to cause ξ to also be a semi-measure, rather than a probability measure. Furthermore, it can be proven that ξ is enumerable but not
computable. Thus, we have that ξ ∈Me. The fact that ξ is not a probability measure is not too much of a problem because, as mentioned earlier, it is
possible to normalise a semi-measure to convert it into a probability measure.
In situations where we need a universal probability measure the normalised
version of ξ is useful. Its main drawback is that it is no longer enumerable,
and thus no longer a member of Me. In most theoretical applications it is
usual to work with the plain ξ as defined above.

$$
\xi
$$

$$
\xi
$$

$$
\xi\in\mathcal{M}_e
$$

$$
\xi
$$

$$
\xi
$$

$$
\mathcal{M}_{e}
$$

$$
\xi
$$

A fundamental result is that the two priors are strongly related:

2.5.5 Theorem. The Solomonoff prior M and Solomonoff-Levin prior ξ lie
within a multiplicative constant of each other. That is, M = ξ.×

$$
\xi
$$

$$
M\stackrel{\times}{=}\xi.
$$

Due to this relation, in many theoretical applications the differences between
the two priors are unimportant. Indeed, it is their shared property of dominance that is the key to their theoretical power:

2.5.6 Definition. For some set of semi-measures M, we say that ν ∈M is
dominant if ∀̺ ∈M there exists a constant c̺> 0 such that ∀x : c̺ν(x) ≥
̺(x). Or more compactly, ∀̺ ∈M : ν ≥ ̺.×

$$
\mathcal{M}
$$

$$
\nu\in\mathcal{M}
$$

$$
\forall\varrho\in\mathcal{M}
$$

$$
c_{\varrho}>0
$$

$$
c_{\varrho}\nu(\underline{x})\geq
$$

$$
\varrho(\underline{x})
$$

$$
\forall\varrho\in\mathcal{M}:\nu\stackrel{\times}{\geq}\varrho.
$$

2. Universal Artificial Intelligence

It is easy to see that ξ is dominant over the set of enumerable semi-measures
from its construction: for x ∈ B∗ we have ξ(x) ≥ PMe(µ) µ(x) = 2−K(µ)µ(x).
×
It follows then that ∀µ ∈Me, ∀x ∈ B∗: 2K(µ)ξ(x) ≥ µ(x). As M = ξ, we see
that M is also dominant. We call distributions that are dominant over large
spaces, such as Me, universal priors. This is due to their extreme generality
and performance as prior distributions, something that we will explore in the
next two sections: firstly in the context of Bayesian theory in general, and
then in the context of sequence prediction.

$$
\xi
$$

$$
x\in\mathbb{B}^*
$$

$$
\xi(\underline{x})\geq P_{\mathcal{M}_{e}}(\mu)\mu(\underline{x})=2^{-K(\mu)}\mu(\underline{x})
$$

$$
\forall\mu\in\mathcal{M}_{e},\forall x\in\mathbb{B}^{*}:2^{K(\mu)}\xi(\underline{{x}})\geq\mu(\underline{{x}})
$$

$$
M\stackrel{\times}{=}\xi,
$$

$$
\mathcal{M}_{e}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
