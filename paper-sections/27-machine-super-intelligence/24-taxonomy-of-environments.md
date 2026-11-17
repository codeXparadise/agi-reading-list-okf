---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3. Taxonomy of Environments
section_role: other
section_index: 24
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In the previous chapter we introduced the AIXI agent πξ, and its generalisation to arbitrary spaces of environments, πζ. Of particular importance was…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3. Taxonomy of Environments

> Section 24 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In the previous chapter we introduced the AIXI agent πξ, and its generalisation
to arbitrary spaces of environments, πζ. Of particular importance was Theorem 2.10.5 which roughly said: For any class of environments for which there
exists a self-optimising agent, the agent πζ defined over this class is also selfoptimising. Thus, in order to understand the performance of πζ across a wide
range of environments, we need to understand which classes of environments
admit self-optimising agents, and which do not. In this chapter we present a
partial answer to this question by showing that many well known classes of
environments admit self-optimising agents under reasonable conditions.

$$
\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

We begin by formalising some common classes of environments. To do this
we examine the environments’ measures and in particular the way in which
they condition on the interaction history. In this way we characterise and
relate many well known classes of environments, such as Bernoulli schemes,
Markov chains, and Markov decision processes (MDPs). Some interesting new
classes of environments naturally arise from the analysis. We then take some
important classes of problems studied in artificial intelligence, such as sequence
prediction and classification, and express these too in terms of the structure of
their measures. This formalisation in terms of chronological measures reveals
that many classes of environments are special cases of other classes, that is, a
hierarchy of classes of environments exists. Studying this more closely we see
that many of these classes are in fact reducible to the class of ergodic MDPs.
Putting all these relationships together produces a taxonomy of classes of
environments.

It is known that certain machine learning algorithms, such as Q-learning,
are self-optimising in the class of ergodic MDPs. As many of the classes in
our taxonomy are reducible to ergodic MDPs, it follows that these classes
also admit self-optimising agents. Thus, from Theorem 2.10.5, we see that πζ
converges to optimal behaviour in these classes of environments. In this way,
we clarify our earlier claim that universal agents can learn to behave optimally
in a wide range of environments, as required by our definition of intelligence.

$$
\pi^{\zeta}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
