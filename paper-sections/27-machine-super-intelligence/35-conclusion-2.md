---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.6. Conclusion
section_role: conclusion
section_index: 35
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In this chapter we have defined a range of classes of environments and shown that many of these are either special cases of other more general…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.6. Conclusion

> Section 35 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `conclusion` · pages n/a

In this chapter we have defined a range of classes of environments and shown
that many of these are either special cases of other more general classes, or
are at least reducible to more elementary classes through a change of action
and perception spaces. This hierarchy of classes defines a kind of taxonomy
of environments. To the best of our knowledge this analysis has not been
done before. Figure 3.1 summarises these relationships. The most general
and powerful classes of environments are at the top and the most limited and
specific classes at the bottom. As we can see, all of the more concrete classes at
the bottom of the hierarchy admit self-optimising agents. By Theorem 2.10.5
it then follows that a universal agent defined over one of these classes is also
self-optimising. This supports our earlier claim that universal agents are able
to perform well in a wide range of environments, as required by our informal
definition of intelligence.

Chronological Environment

POMDP

Passive Environment

Sequence Prediction

nth order MDP

MDP

Function Maximisation

Totally Passive Environment

Markov Chain

Computable Sequence Prediction

Ergodic nth order MDP

Ergodic MDP

Ergodic Markov Chain

Repeated Strategic Game

Bandit

Classification

Bernoulli Scheme

Environments that admit self-optimising agents

Figure 3.1.: Taxonomy of environments. Downward arrows indicate that the
class below is a special case of the class above. Dotted horizontal
lines indicate that two classes of environments are reducible to
each other. The greyed area contains the classes of environments
that admit self-optimising agents, that is, the environments in
which a universal agent will learn to behave optimally.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
