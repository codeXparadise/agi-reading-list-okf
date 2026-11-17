---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.5.2 Lemma. Bernoulli schemes are ergodic MDPs.
section_role: other
section_index: 31
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Proof. Consider a Bernoulli scheme (A, X,µ). From the definition of a Bernoulli scheme we immediately see that they are a special case of the MDP…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.5.2 Lemma. Bernoulli schemes are ergodic MDPs.

> Section 31 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Proof. Consider a Bernoulli scheme (A, X,µ). From the definition of a
Bernoulli scheme we immediately see that they are a special case of the MDP
definition. As the environment is accessible, ∀ok, ∃ax<kak: µ(ax<kakok) > 0.
Applying the definition of a Bernoulli scheme, this reduces to ∀ok: µ(ok) > 0.
Thus, as the next observation does not depend on observations prior to ok−1,
nor does it depend on the actions or rewards, the agent and environment
together define a Markov chain. As all observations are possible at every point
in time it follows that all observations belong to the same communicating class
and are aperiodic. That is, the Markov chain is ergodic.

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall o_{k},\exists ax_{<k}a_{k}:\mu(ax_{<k}a_{k}\underline{o}_{k})>0.
$$

$$
\forall o_{k}:\mu(\underline{o}_{k})>0.
$$

$$
o_{k-1}
$$

Note that the above result holds independent of the agent as the environment
is passive. The same is true for classification problems:

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
