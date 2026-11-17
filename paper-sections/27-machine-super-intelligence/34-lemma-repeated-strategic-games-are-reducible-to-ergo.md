---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.5.5 Lemma. Repeated strategic games are reducible to ergodic MDPs.
section_role: other
section_index: 34
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Proof. Let (A, X,µ) be a repeated strategic game with episode length l. Now define a new action space Ã := Al. In this new action space every…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.5.5 Lemma. Repeated strategic games are reducible to ergodic MDPs.

> Section 34 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Proof. Let (A, X,µ) be a repeated strategic game with episode length
l. Now define a new action space Ã := Al. In this new action space every
combination of actions that an agent can take in a single episode of the game
is represented by a single action. Similarly, define a new perception space that

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\tilde{\mathcal{A}}:=\mathcal{A}^l
$$ represents each episode, X˜ := X l, and now define a chronological measure µ˜
over the new spaces such that ∀ãx˜1:k,

$$
\tilde{\mathcal{X}}:=\mathcal{X}^l
$$

$$
\tilde{\mu}
$$

$$
\forall\tilde{a}\tilde{x}_{1:k}
$$

$$
\tilde{\mu}(\tilde{a}\tilde{x}_{<k}\tilde{a}\tilde{\underline{{x}}}_{k})\;=\;\tilde{\mu}(\tilde{a}\tilde{\underline{{x}}}_{k})\;:=\;\mu(a\underline{{x}}_{(k-1)l+1:(k-1)l+l}).
$$

By construction the environment (Ã, X,˜ µ˜) is a bandit and thus by
Lemma 3.5.4 it is an ergodic MDP.

$$
(\tilde{A},\tilde{X},\tilde{\mu})
$$

The above results show that Bernoulli schemes, classification problems, bandits and repeated strategic games are either ergodic MDPs or can be reduced to
one. As such, they all admit self-optimising policies and thus an appropriately
defined universal agent πζ is self-optimising in these classes of environments.
As the rewards received in totally passive environments are independent of
the agent’s behaviour, these trivially admit self-optimising agents, indeed all
agents are equally “optimal”. What about function optimisation and sequence
prediction problems?

$$
\pi^{\zeta}
$$

Unfortunately, the above approach does not work for function optimisation
problems as we have defined them. The problem is that they are not MDPs as
the reward signal depends on more than just the current action and the last
observation. They can be modelled as a POMDP by including the last reward
in the core MDP and making this unobservable. In any case, this is not a
problem because any agent that enumerates the action space will eventually
hit upon the optimal action and thus is self-optimising. What this highlights
is that being self-optimising only tells us something about performance in the
limit, it says nothing about how quickly an agent will learn to perform well.

Sequence prediction problems are more problematic. In general, no agent
can be self-optimising over the class of all sequence prediction problems. To
see this, simply consider that for any prediction agent there exists a sequence
where the next observation is always the observation which the agent predicted
would be the least likely (for a formal statement of this see Lemma 5.2.4). This
is true even for incomputable agents. If we restrict the sequences to have computable distributions, but still allow the agent to be incomputable, then we
have seen that Solomonoff’s predictor has a bounded total expected prediction error. As the prediction error converges to zero, the reward converges to
optimal and so Solomonoff’s predictor is self-optimising. Given that the universal agent was built upon the same foundations as Solomonoff’s predictor,
we might then expect the same result to hold. At present nobody has been able
to prove this, though it is conjectured to be true. Currently the best bound
is exponentially worse and holds only for deterministic computable sequence
prediction (Section 6.2.2 of Hutter, 2005). For our purposes an exponentially
worse bound is still finite and thus it follows that a universal agent defined
over the space of computable sequences is self-optimising.

3. Taxonomy of Environments

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
