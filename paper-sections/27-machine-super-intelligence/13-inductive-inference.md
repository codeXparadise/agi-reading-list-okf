---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.1. Inductive inference
section_role: other
section_index: 13
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Inductive inference is the process by which one observes the world and then infers the causes behind what has been observed. This is a key process by…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.1. Inductive inference

> Section 13 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Inductive inference is the process by which one observes the world and then
infers the causes behind what has been observed. This is a key process by which
we try to understand the universe and so naturally examples of it abound.
Indeed much of science can be viewed as a process of inductively inferring
natural causes. For example, at a microscopic level, one may fire sub-atomic
particles into a gas chamber, observe the patterns they trace out, and then
try to infer what the underlying principles are that govern these events. At
a larger scale one may observe that global temperatures are changing along
with other atmospheric conditions, and from this information attempt to infer
what processes may be driving climate change.

Science is not the only domain where inductive inference is important. A
businessman may observe stock prices over time and then attempt to infer a
model of this process in order to predict the market. A parent may return
home from work to discover a chair propped against the refrigerator with the
cookie jar on top a little emptier. Whether we are a detective trying to catch
a thief, a scientist trying to discover a new physical law, or a businessman attempting to understand a recent change in demand, we are all in the process
of collecting information and trying to infer the underlying causes.

Formally we can abstract the inductive inference problem as follows: An
agent has observed some data D := x1,x2,...xt and has a set of hypotheses
H := h1,h2,..., some of which may be good models of the unknown process
µ that is generating D. The task is to decide which hypothesis, or hypotheses
in H are the most likely to accurately reflect µ. For example, x1,x2,... might
be the market value of a stock over time and H might consist of a set of
mathematical models of the stock price. Once we have identified which model
or models are likely to accurately describe the price behaviour, we may want
to use this information to predict future stock prices. Typically this is the
case: Often our goal is not just to understand our observations, but also to
be able to predict future observations. It is in prediction that good models
become truly useful.

$$
\mathcal{D}:=x_{1},x_{2},\ldots x_{t}
$$

$$
\mathcal{H}:=h_{1},h_{2},\ldots,
$$

$$
\mu.
$$

$$
x_{1},x_{2},..
$$

Inductive inference has a long history in philosophy. An early thinker on
the subject was the Greek philosopher Epicurus (342? B.C. – 270 B.C.) who
noted that there typically exist many hypotheses which are consistent with all
of the available data. Logically then, we cannot use the data to rule out any
of these hypotheses; they must all be kept as potential explanations. This is
known as Epicurus’ principle of multiple explanations and is often stated as,

Keep all hypotheses that are consistent with the data.

To illustrate this, consider the cookie jar example again and place yourself
in the position of the parent returning home from work. Having observed the
chair by the refrigerator and missing cookies, one seemingly likely hypothesis
is that your daughter has pushed the chair over to the refrigerator, climbed on
top of it, and then removed some cookies. Another hypothesis is that a hungry
but unusually short thief picked the lock on the back door, saw the cookie jar
and decided to move the chair over to the refrigerator in order to get some
cookies. Although this seems much less likely, you cannot completely rule out
this possibility, or even more elaborate explanations, based solely on the scene
in the kitchen. Philosophically this leaves you in the uncomfortable situation
of having to consider all sorts of strange explanations as being theoretically
possible given the information available. The need to keep these hypotheses
would become clear if you were then to walk into the living room and notice that your new television and other expensive items were also missing —
suddenly the unlikely seems more plausible.

Although we may accept that all hypotheses which are consistent with the
observed facts should be considered at least possible, it is intuitively clear
that some hypotheses are much more likely than others. For example, if you
had previously observed similar techniques being employed by your daughter
to access the cookie jar, but had never been burgled, it would be natural to
consider that the small thief in question was of your own flesh and blood,
rather than a career criminal. However, you are basing this judgement on
your experience prior to returning home. What if you really had very little prior knowledge? How then should you judge the relative likelihood of different
hypotheses?

2.1.1 Example. Consider the following sequence:

**1, 3, 5, 7**

What process do you think is generating these numbers? What do you predict
will come next?

An obvious hypothesis is that these are the positive odd numbers. If this
is true then the next number is going to be 9. A more complex hypotheses
is that the sequence is being generated by the equation 2n − 1 + (n − 1)(n −
2)(n − 3)(n − 4) for n ∈ N. In this case the next number would be 33. Even
when people are aware that this equation generates a sequence consistent with
the digits above, most would not consider it to be very likely at all.

$$
2)(n-3)(n-4)
$$

$$
2n-1+(n-1)(n-
$$

$$
n\in\mathbb{N}
$$

The philosophical principle behind this intuition was first clearly stated by
the English logician and Franciscan friar, William of Ockham (1285 – 1349,
also spelt Occam). He argued that when inferring a cause one should not
include in the explanation anything that is not strictly required to explain the
observations. Or as originally stated, “entia non sunt multiplicanda praeter
necessitatem”, which translates as “entities should not be multiplied beyond
necessity”. A more modern and perhaps clearer expression is,

Among all hypotheses consistent with the observations, the simplest
is the most likely.

This philosophical principle is known as Occam’s razor as it allows one to
cut away unnecessary baggage from explanations. If we consider the number
prediction problem again, it is clear that the principle of Occam’s razor agrees
with our intuition: the simple hypothesis seemed to be more likely, a priori,
than the complex hypothesis. As we saw in the previous chapter, the ability
to apply Occam’s razor is a standard feature of intelligence tests.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
