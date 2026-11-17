---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6. Temporal Difference Updating without a Learning Rate
section_role: other
section_index: 51
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In Chapters 2 and 3 we saw how universal agents are able to learn to behave optimally across a wide range of environments. Unfortunately, these…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6. Temporal Difference Updating without a Learning Rate

> Section 51 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In Chapters 2 and 3 we saw how universal agents are able to learn to behave
optimally across a wide range of environments. Unfortunately, these agents
are incomputable as they are based on incomputable universal prior distributions. Thus, in order to use the theory of universal artificial intelligence to
design and build practical algorithms, we must first find a way to scale the
theory down. In Chapter 5 we investigated some of the constraints faced when
attempting this. What we uncovered was a number of fundamental negative
results. In short, computable predictors capable of predicting all sequences up
to a moderate Kolmogorov complexity are both highly complex and mathematically impossible to find due to G¨odel incompleteness. The only way out
of this bind, it seems, is to move to a more sophisticated measure of complexity that takes not only information content into account, but also time and
space. Unfortunately, the theory of resource bounded complexity is notoriously difficult to work with and has many unsolved fundamental questions.
Furthermore, even if the universal prior distribution could be replaced by a
suitable computable prior, perhaps something like the Speed prior (Schmidhuber, 2002), there still remains the fact that AIXI’s search through possible
futures requires computation time that is exponential in the depth of the look
ahead (see the equation for AIXI in Section 2.10).

Despite these difficulties, several attempts at scaling AIXI down have been
made. The most theoretically founded of these is AIXItl (Chapter 7 of Hutter,
2005). In this model, proof search is used to limit the size and computation
time of the algorithm. Unfortunately, although technically computable, the
resulting agent still requires impossibly vast computational resources. Another
more drastic scaling down of AIXI did produce a usable algorithm (Poland and
Hutter, 2006). Here the problem domain was limited to games that could be
described by 2 × 2 matrices, and the look ahead was bounded to 8 interaction
cycles. The resulting algorithm was able to learn simple game theoretic interaction strategies. While this proves that some kind of scaling down of AIXI is
possible, the problem space of 2 × 2 matrix games falls well short of what is
needed for a useful artificial intelligence algorithm.

In this chapter we present what started out as another attempt to scale
AIXI down. As we have seen in previous chapters, at the core of the reinforcement learning problem lies the problem of estimating the expected future
discounted reward. We begin by expressing this estimation problem as a loss
function, more specifically, as the squared difference between the empirical future discounted reward and our estimate. We then derive an equation for
this estimator by minimising the loss function. Although the resulting learning
equations no longer bear much resemblance to AIXI, they do strongly resemble
the standard equation for temporal difference learning with eligibility traces,
also known as the TD(λ) algorithm. Interestingly, while the standard algorithm has a free learning rate parameter, in our new equation there is none. In
its place there is an equation that automatically sets the learning rate in a way
that is specific to each state transition. We have experimentally tested this new
learning rule against TD(λ) and found that it offers superior performance in
various settings. We have also extended the algorithm to reinforcement learning and again found encouraging results. This chapter covers the derivation
of this algorithm and our experimental results.

Note that while the notation used in this chapter is fairly standard for the
temporal difference learning literature, it is a little different to what we used
to define AIXI. For example, we now talk of states rather than observations,
and index the value function in a new way.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
