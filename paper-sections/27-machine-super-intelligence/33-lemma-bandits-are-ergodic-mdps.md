---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.5.4 Lemma. Bandits are ergodic MDPs.
section_role: other
section_index: 33
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Proof. Consider a bandit (A, X,µ). By definition it is trivially an MDP. As the environment is accessible ∀ok, ∃ax<kak: µ(ax<kaok) 0. Applying the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.5.4 Lemma. Bandits are ergodic MDPs.

> Section 33 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Proof. Consider a bandit (A, X,µ). By definition it is trivially an MDP.
As the environment is accessible ∀ok, ∃ax<kak: µ(ax<kaok) > 0. Applying the
definition of a Bandit this reduces to,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall\boldsymbol{o}_{k},\exists\boldsymbol{a}\boldsymbol{x}_{<k}\boldsymbol{a}_{k}:\mu(\boldsymbol{a}\boldsymbol{x}_{<k}\boldsymbol{a}_{k})>0
$$

$$
\forall o_{k},\exists a_{k}:\mu(\underline{o}_{k})>0.
$$

(3.1)

Next we need to show that there exists an agent under which the agent
interacting with the environment defines an ergodic Markov chain. If we define
1
an agent ∀ak: π(ak) := it follows that ∀ax<kaok,
|A|

$$
\forall a_{k}:\pi(\underline{a}_{k}):=\frac{1}{|\mathcal{A}|}
$$

$$
\forall ax_{<k}oo_{k}
$$

$$
\pi(a x_{<k}a\underline{{o}}_{k}):=\sum_{a_{k}\in\mathcal{A}}\pi(\underline{{a}}_{k})\mu(a\underline{{o}}_{k})=\frac{1}{|\mathcal{A}|}\sum_{a_{k}\in\mathcal{A}}\mu(a\underline{{o}}_{k})=:\pi(\underline{{o}}_{k}).
$$

From Equation 3.1 it then follows that for each ok at least one of the terms
π
in the above sum is non-zero. Thus, ∀ok: πµ(ok) > 0 and soµis an ergodic
Markov chain and therefore µ is an ergodic MDP.

$$
o_{k}
$$

$$
\forall o_{k}:\bar{\bar{\mu}}(\underline{o}_{k})>0
$$

$$
\begin{array}{c}\pi\\ \mu\end{array}
$$

$$
\mu
$$

Unfortunately, repeated strategic games are not ergodic MDPs. The problem
is that there may be observations which can only occur at certain points in each
episode, for example at the start or the end. Clearly then one cannot define
an agent such that these observations have period 1, making it impossible to
construct an ergodic Markov chain. Nevertheless, through a change of action
and perception spaces a repeated strategic game can be converted into an
equivalent system which is a bandit. Bandits, as we saw above, are ergodic
MDPs. For our purposes such a conversion is sufficient as it allows these
environments to admit self-optimising agents.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
