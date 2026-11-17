---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.4. Ergodic MDPs
section_role: other
section_index: 28
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Intuitively, a Markov chain is ergodic if the current observation cannot impose any long term constraints on future observations. Given that the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.4. Ergodic MDPs

> Section 28 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Intuitively, a Markov chain is ergodic if the current observation cannot impose
any long term constraints on future observations. Given that the reward in a
Markov chain only depends on the last observation, being ergodic also implies
that the current observation does not place any long term constraints on future rewards either. Although the ergodic property is typically studied in the
context of Markov chains, in this section we will extend the notion to MDPs.
To illustrate the idea, we begin by considering some Markov chains that are
not ergodic.

3.4.1 Example. Imagine a Markov chain with O := {A,B,C}. The
chain starts with observation A and then transitions to either B or C. In all
subsequent cycles the observation remains the same. Thus, once observation
B has been generated, observation C will never occur. This is a long term
constraint on future observations, and thus the Markov chain is not ergodic.

$$
\mathcal{O}:=\{A,B,C\}
$$

It is as if the agent has gone through a one-way door into a part of the
environment that it can never return from. This is similar to the Heaven
and Hell environment in Example 2.10.1, except that in the above example
the agent was unable to choose where to go as the environment was passive.
Consider now a slightly more subtle example of non-ergodic behaviour.

3.4.2 Example. Imagine a Markov chain with O := {A,B}. The environment starts with observation A and then in the first cycle transitions to B.
In the following cycle it transitions back to state A, and then in the next it
returns to B. In this way the system alternates between the two observations.

$$
\mathcal{O}:=\{A,B\}
$$

This environment might seem ergodic as both possible observations continue
to occur forever and so the agent clearly has not become confined to just one
part of the environment. However, if the current observation is A, it must
be the case that two time steps into the future the observation will again be
A. In fact, for any even number of time steps into the future the observation
will always be A. As this is a long term constraint on future observations the
environment is not ergodic.

The above example can be modified so that it is ergodic: after outputting
observation A make it so that there is a 0.1 probability of generating this
again, and a 0.9 probability of outputting B. Thus, no matter what the
current observation is, after three time steps the environment could output
either observation.

We now formalise the proceeding concepts. We say that two observations
communicate if it is possible to go from one observation to the other and
return after some finite number of steps. A communicating class is a set of
observations that all communicate with each other, and do not communicate
with any observations outside this set. If all observations of the Markov chain
belong to the same communicating class, we say that the Markov chain is
irreducible. An observation has period k if any return to the observation must
occur in some multiple of k time steps and k is the largest number with this
property. For example, if it is only possible to return to an observation in an
even number of steps, then this observation has period 2. If an observation
has period 1 then it is aperiodic, and if all observations are aperiodic we say
that the Markov chain is aperiodic. We can now formally define what it means
for a Markov chain to be ergodic:

3.4.3 Definition. A Markov chain environment (A, X,µ) is ergodic if and
only if it is irreducible and aperiodic.

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

Consider again the two examples above. The technical reason the Markov
chain in Example 3.4.1 was not ergodic was because the observations A and
B were not communicating and thus the Markov chain was not irreducible. In
Example 3.4.2 the problem was that both observations had period 2 and thus
the Markov chain was not aperiodic.

To extend the concept of being ergodic to cover MDPs consider again the
relationship between Markov chains and MDPs. Let µ be an MDP environment,
and π an agent that is conditioned on only the last observation. That is,
∀ax<kak with k > 1 we have,

$$
\mu
$$

$$
\pi
$$

$$
\forall\mathit{ax}_{<k}\mathit{a}_{k}
$$

$$
k>1
$$

$$
\pi(a x_{<k}\underline{a}_{k})=\pi(o_{k-1}\underline{a}_{k}).
$$

3. Taxonomy of Environments

π
Now consider the measureµthat describes how the above environment and
agent interact. In each cycle we have,

$$
\begin{array}{c}\pi\\\mu\end{array}
$$

$$
\begin{array}{r c l}{{}_{\mu}^{\pi}(\mathit{ax}_{<k}\mathit{a}\underline{{x}}_{k})}&{:=}&{\sum_{a_{k}\in\mathcal{A}}\pi(o_{k-1}\underline{{a}}_{k})\:\mu(o_{k-1}\mathit{a}\underline{{x}}_{k})}\\ {}&{=}&{{}_{\mu}^{\pi}(o_{k-1}\underline{{x}}_{k}).}\\ \end{array}
$$

Thus, if π has the form above and is fixed, the distribution over the next
π
perception depends on only the last observation. That is,µdefines a Markov
chain. In other words, an MDP can be thought of as a Markov chain with the
addition of actions that allow an agent to influence future observations. We
can remove this by taking an appropriate agent and building it into the MDP.
The resulting system no long has free actions to be chosen, and reverts back
to being a Markov chain.

$$
\begin{array}{c}\pi\\ \mu\end{array}
$$

Using this relationship, we can now define ergodic MDPs in the natural way:

3.4.4 Definition. An MDP environment (A, X,µ) is ergodic if and only if
π
there exists an agent (A, X,π) such thatµdefines an ergodic Markov chain.

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\left(\mathcal{A},\mathcal{X},\pi\right)
$$

$$
\begin{array}{c}\pi\\ \mu\end{array}
$$

As higher order MDPs are reducible to MDPs, we will say that a higher order
MDP is ergodic if it is reducible to an ergodic MDP.

Consider again the Heaven and Hell environment defined in Example 2.10.1.
After the first interaction cycle the agent is always in either heaven or hell.
Furthermore, no matter what the agent does, it cannot switch between being
in heaven or being in hell, it is stuck in its current location for all eternity.
Thus, no matter what agent we select we cannot create a Markov chain such
that the observations of being in heaven communicate with the observations
of being in hell, and so this MDP environment is not ergodic.

The importance of ergodic MDPs for us will be their relationship to learning. In an MDP environment only the current observation and action have
any impact on future perceptions. When the MDP is ergodic, the current observation also has no long term impact on future perceptions that cannot be
overcome by taking the right actions. This means that in an ergodic MDP
environment no matter what mistakes an agent might make, there is always a
way to recover from these. Obviously this is a significant property for learning
agents, and indeed the following important result can be proven:

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
