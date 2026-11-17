---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.5.3 Lemma. Classification problems are ergodic MDPs.
section_role: other
section_index: 32
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Proof. From Definition 3.3.4 we see that the distribution over the attribute space W is not dependent on the interaction history, and the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.5.3 Lemma. Classification problems are ergodic MDPs.

> Section 32 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Proof. From Definition 3.3.4 we see that the distribution over the attribute
space W is not dependent on the interaction history, and the distribution over
the class space Z depends only on the attribute in the current cycle and so
it too is independent of anything in prior cycles. More formally, ∀ax<kakok:
µ(ax<kakok) = µ(wk) µ(wkzk) where ok:= wkzk. Thus the distribution over
observations is completely independent of prior cycles.

$$
\mathcal{Z}
$$

$$
\forall a x_{<k}a_{k}o_{k}
$$

$$
\mu\left(a x_{<k}a_{k}\underline{{o}}_{k}\right)=\mu\left(\underline{{w}}_{k}\right)\mu\left(w_{k}\underline{{z}}_{k}\right)
$$

$$
o_{k}:=w_{k}z_{k}
$$

Again from the definition of classification problems we see that the distribution over rewards depends on only the observation in the previous interaction
cycle and the action in the current cycle. It follows then that in each cycle the

3. Taxonomy of Environments

perception (consisting of an attribute, class and reward) depends on only the
action in the current cycle and the observation in the previous cycle. Thus,
classification problems are MDPs.

As the environment is accessible, ∀ok, ∃ax<kak: µ(ax<kakok) > 0. Because
the distribution over observations is independent of previous interaction cycles this immediately reduces to ∀ok: µ(ok)>0 and so the environment is
ergodic.

$$
\forall\boldsymbol{o}_{k},\exists\boldsymbol{a}\boldsymbol{x}_{<k}\boldsymbol{a}_{k}:\mu(\boldsymbol{a}\boldsymbol{x}_{<k}\boldsymbol{a}_{k}\underline{\boldsymbol{o}}_{k})>0
$$

$$
\forall o_{k}:\mu(\underline{o}_{k})>0
$$

As classification problems are passive, in the above proof it was again possible to construct an ergodic Markov chain without specifying the agent. In
active environments, such as bandits, we must define an appropriate agent:

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
