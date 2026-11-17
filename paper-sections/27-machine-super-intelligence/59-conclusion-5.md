---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 6.8. Conclusion
section_role: conclusion
section_index: 59
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "We have derived a new equation for setting the learning rate in temporal difference learning with eligibility traces. The equation replaces the free…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.8. Conclusion

> Section 59 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `conclusion` · pages n/a

We have derived a new equation for setting the learning rate in temporal difference learning with eligibility traces. The equation replaces the free learning
rate parameter α, which is normally experimentally tuned by hand. In every
setting tested, be it stationary Markov chains, non-stationary Markov chains
or reinforcement learning, our new method produced superior results.

To further our theoretical understanding, the next step would be to try
to prove that the method converges to correct estimates. This can be done
for TD(λ) under certain assumptions on how the learning rate decreases over
time (Dayan, 1992; Peng, 1993). Hopefully, something similar can be proven
for our new method. In terms of experimental results, it would be interesting
to try different types of reinforcement learning problems and to more clearly
identify where the ability to set the learning rate differently for different state
transition pairs helps performance.

Many extensions to the algorithm should also be possible. One would be
to generalise the learning rule to episodic tasks, another would be to merge
our update rule with Peng’s version of Q(λ) (Peng and Williams, 1996), as we

TD UPDATING WITHOUT A LEARNING RATE

have done with Sarsa(λ) and Watkins’ version of Q(λ). Finally, it would be
useful to extend the algorithm to work with function approximation methods
so that it could deal with larger state spaces.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
