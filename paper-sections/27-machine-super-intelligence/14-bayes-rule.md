---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: "2.2. Bayes’ rule"
section_role: other
section_index: 14
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Although fundamental, the principles of Epicurus and Occam by themselves are insufficient to provide us with a mechanism for performing inductive…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.2. Bayes’ rule

> Section 14 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Although fundamental, the principles of Epicurus and Occam by themselves
are insufficient to provide us with a mechanism for performing inductive inference. A major step forward in this direction came from the English mathematician and Presbyterian minister, Thomas Bayes (1702 – 1761).

In inductive inference we seek to find the most likely hypothesis, or hypotheses, given the data. Expressed in terms of probability, we seek to find h ∈H
such that the probability of h given D, written P (h|D), is high. From the
definition of conditional probability, P (h|D) := P (h ∩D)/P (D). Rearranging
this we get P (h|D)P (D) = P (h ∩D) = P (D|h)P (h), from which it follows
that,
P (D|h)P (h) P (D|h)P (h)

$$
h\in\mathcal{H}
$$

$$
P(h|\mathcal{D})
$$

$$
P(h|\mathcal{D}):=P(h\cap\mathcal{D})/P(\mathcal{D})
$$

$$
P(h|\mathcal{D})P(\mathcal{D})=P(h\cap\mathcal{D})=P(\mathcal{D}|h)P(h)
$$

$$
P(h|\mathcal{D})=\frac{P(\mathcal{D}|h)P(h)}{P(\mathcal{D})}=\frac{P(\mathcal{D}|h)P(h)}{\sum_{h'\in\mathcal{H}}P(\mathcal{D}|h')P(h')}.
$$

2. Universal Artificial Intelligence

This equation is known as Bayes’ rule. It allows one to compute the probability of different hypotheses h ∈H given the observed data D, and a distribution
P (h) over H. The probability of the observed data, P (D), is known as the
evidence. P (h) is known as the prior distribution as it is the distribution over
the space of hypotheses before taking into account the observed data. The
distribution P (h|D) is known as the posterior distribution as it is the distribution after taking the data into account. Thus in essence, Bayes’ rule takes
some beliefs that we may have about the world and updates these according
to some observed data. In the above formulation we have assumed that the
set of hypotheses H is countable. For uncountable sets the sum is replaced by
an integral.

$$
h\in\mathcal{H}
$$

$$
P(h)
$$

$$
P(\mathcal{D})
$$

$$
P(h)
$$

$$
P(h|D)
$$

Despite its elegance and simplicity, Bayesian inference is controversial. To
this day professional statisticians can be roughly divided into Bayesians who
accept the rule, and classical statisticians who do not. The debate is a subtle
and complex one and there are many different positions within each of the two
camps. At the core of the debate is the very notion of what probability means,
and in particular what the prior probability P (h) means.

How can one talk about the probability of a hypothesis before seeing any
data? Even if this prior probability is meaningful, how can one know what
its value is? We need to take this question seriously because in Bayes’ rule
the choice of prior affects the relative values of P (h|D) for each h, and thus
influences the inference results. Indeed, if Bayesians are free to choose the
prior over H, how can they claim to have objective results?

$$
P(h|\mathcal{D})
$$

Bayesians respond to this in a number of ways. Firstly, they point out that
the problem is generally small, in the sense that with a reasonable prior and
quantity of data, the posterior distribution P (h|D) depends almost entirely
on D rather than the chosen prior P (h). In fact on any sizable data set, not
only does the choice of prior not especially matter, but Bayesian and classical
statistical methods typically produce similar results, as one would expect. It
is only with relatively small data sets or complex models that the choice of
prior becomes an issue.

$$
P(h|\mathcal{D})
$$

If classical statistical methods could avoid the problem of prior bias when
dealing with small data sets then this would be a significant argument in their
favour. However Bayesians argue that all systems of inductive inference that
obey some basic consistency principles define, either explicitly or implicitly,
a prior distribution over hypotheses. Thus, methods from classical statistics
make assumptions that are in effect equivalent to defining a prior. The difference is that in Bayesian statistics these assumptions take the form of an
explicit prior distribution. In other words, it is not that prior bias in Bayesian
statistics is necessarily any better or worse than in classical statistics, it is
simply more transparent.

In practical terms, if priors cannot be avoided, one strategy to reduce the
potential for prior selection abuse is to use well known priors whenever possible. To this end many standard prior distributions have been developed. The
key desirable property is that a prior should not strongly influence the poste- rior distribution and thus unduly affect the inference results. This means that
the prior should express a high degree of impartiality by treating the various
hypotheses somewhat equally. For example, when the set H is finite, an obvious choice is to assign equal prior probability to each hypothesis, formally,
1
P (h) := for all h ∈H. Things become more problematic in infinite hy-
|H|
pothesis spaces as it is then mathematically impossible to assign an equal finite
probability to each of the hypotheses in H, and still have P (H) = 1. Some
Bayesians abandon this condition and use so called improper priors which are
not true probability distributions. For the classical statistician, such a radical
departure from the definition of probability does not really solve the problem of the unknown prior, rather it suggests that something is fundamentally
amiss.

$$
\mathcal{H}
$$

$$
P(h):=\frac{1}{|\mathcal{H}|}
$$

$$
h\in\mathcal{H}
$$

$$
\mathcal{H}.
$$

$$
P(\mathcal{H})=1
$$

Instead of mathematical tricks or other workarounds, what Bayesians would
ideally like is to solve the unknown prior problem once and for all by having
a universal prior distribution. Only then would the Bayesian approach be
truly complete. The principles of Epicurus and Occam provide some hints on
how this might be done. From Epicurus, whenever a hypothesis is consistent
with the data, that is P (D|h) > 0, we should keep this hypothesis by having
P (h|D) > 0. From Bayes’ rule this requires that ∀h ∈H : P (h) > 0. From
Occam we see that P (h) should decrease with the complexity of h, and thus
we need a way to measure the complexity of hypotheses. However before
continuing with this, we first consider the inference problem from another
perspective.

$$
P(\mathcal{D}|h)>0
$$

$$
\forall h\in\mathcal{H}:P(h)>0
$$

$$
P(h|\mathcal{D})>0
$$

$$
P(h)
$$

$$
h,
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
