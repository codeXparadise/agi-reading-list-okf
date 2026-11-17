---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.5. Environments that admit self-optimising agents
section_role: other
section_index: 30
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In this section we will prove that some of the environments we have defined are in fact ergodic MDPs. Thus, by the results in the last section, πζ is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.5. Environments that admit self-optimising agents

> Section 30 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In this section we will prove that some of the environments we have defined
are in fact ergodic MDPs. Thus, by the results in the last section, πζ is
self-optimising in these environments. Before we begin we first need to introduce one extra property: we need to assume that environments are accessible,
meaning that there are no observations that have zero probability of ever being
observed.

$$
\pi^{\zeta}
$$

3.5.1 Definition. A chronological environment (A, X,µ) is accessible if
∀ok, ∃ax<kak such that µ(ax<kakok) > 0.

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall o_{k},\exists a x_{<k}a_{k}
$$

$$
\mu(a x_{<k}a_{k}\underline{{o}}_{k})>0
$$

It is reasonable to assume this because if it is impossible to find any finite
interaction history that gives some observation a non-zero probability then we
can simply remove it from the observation space. This produces an equivalent
environment that is accessible. In particular, this does not interfere with the
property that ergodic MDPs admit self-optimising agents. These unused extra
observations play no role.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
