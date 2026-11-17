---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 4.2. Universal intelligence of various agents
section_role: other
section_index: 38
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In order to gain some intuition for our definition of intelligence, in this section we will consider a range of different agents and their relative…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.2. Universal intelligence of various agents

> Section 38 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In order to gain some intuition for our definition of intelligence, in this section we will consider a range of different agents and their relative degrees of
universal intelligence.

A random agent. The agent with the lowest intelligence, at least among
those that are not actively trying to perform badly, would be one that makes
uniformly random actions. We will call this πrandrand. Although this is clearly a
weak agent, we cannot simply conclude that the value of Vµπ will always be
low as some environments will generate high reward no matter what the agent

$$
\pi^{\mathtt{r a n d}}
$$

$$
V_{\mu}^{\circ}{}^{\mathtt{r a n d}}
$$ does. Nevertheless, in general such an agent will not be very successful as it
will fail to exploit any regularities in the environment, even trivial ones. It
rand
follows then that the values of Vµπ will typically be low compared to other
agents, and thus Υ(πrand) will be low. Conversely, if Υ(πrand) is very low, then
the equation for Υ implies that for simple environments, and many complex
rand
environments, the value of Vµπ must also be relatively low. This kind of poor
performance in general is what we would expect of an unintelligent agent.

$$
V_{\mu}^{\pi^{\mathtt{r a n d}}}
$$

$$
\Upsilon(\pi^{\tt r a n d})
$$

$$
\Upsilon(\pi^{\tt r a n d})
$$

$$
V_{\mu}^{\pi^{\mathtt{r a n d}}}
$$

A very specialised agent. From the equation for Υ, we see that an agent
could have very low universal intelligence but still perform extremely well at
a few very specific and complex tasks. Consider, for example, IBM’s Deep
Blue chess supercomputer, which we will represent by πdblue. When µchess
dblue chess
)
describes the game of chess, Vµπchessis very high. However 2−K(µ is small,
and for µ = µchess the value function will be low as πdblue only plays chess.
Therefore, the value of Υ(πdblue) will be very low. Intuitively, this is because
Deep Blue is too inflexible and narrow to have general intelligence. Current
artificial intelligence systems fall into this category: powerful in some domain,
but not general and adaptable enough to be truly intelligent.

$$
\pi^{\tt d b l u e}
$$

$$
\mu^{\tt c h e s s}
$$

$$
V_{\mu^{\tt c h e s s}}^{\pi^{\tt d b l u e}}
$$

$$
2^{-K}(\mu^{\mathrm{chess}})
$$

$$
\mu\neq\mu^{\tt c h e s s}
$$

$$
\pi^{\tt d b l u e}
$$

$$
\Upsilon(\pi^{\tt d b l u e})
$$

Interestingly, universal intelligence becomes somewhat counter intuitive
when we use it to compare very specialised agents. Consider an agent πsimple
which is only able to learn to predict sequences of the form 0000... and
1111.... Obviously this agent will fail in most environments and thus will
have a low universal intelligence, as we would expect. However, environments
of this form will have short programs and thus are much more likely than
environments which describe, for example, chess. As πdblue can only play
chess, it cannot learn to predict these simple sequences, it follows then that
Υ(πdblue) < Υ(πsimple). Intuitively we would expect the reverse to be true.

$$
\pi^{\tt s i m p l e}
$$

$$
1111\ldots
$$

$$
0000..
$$

$$
\mathrm {A s} \pi^ {\mathrm {d b l u e}}
$$

$$
\Upsilon(\pi^{\tt d b l u e})<\Upsilon(\pi^{\tt s i m p l e})
$$

What this shows is that the universal intelligence measure strongly emphasises the ability to solve simple problems. If any system cannot do this, even if
it can do something relatively complex like play chess, then it is considered to
have very little intelligence. Of course extreme cases such the one above only
occur with artificial constructions such as chess playing machines. Any human
able to play chess would easily be able to learn to predict trivial patterns such
as 0000....

With the above in mind, it is interesting to consider the progress of artificial
intelligence as a field from the perspective of universal intelligence. In the early
days of artificial intelligence there was a lot of emphasis on developing machines
that were able to do simple reasoning and pattern matching etc. Extending
the power of these general systems was difficult and over time the field become
increasingly concerned with very narrow systems that were able to solve quite
specific problems. This has lead some people to complain that while we now
have impressive systems for some specific things, we have not progressed much
towards true intelligence, meaning artificial general intelligence. Indeed, from

4. Universal Intelligence Measure

the perspective of universal intelligence, by focusing on increasingly specialised
systems we have in fact have gone backwards.

A general but simple agent. Imagine an agent that performs very basic
learning by building up a table of observation and action pairs and keeping
statistics on the rewards that follow. Each time an observation that it has
seen before occurs, the agent takes the action with highest estimated expected
reward in the next cycle with 0.9 probability, or a random action with 0.1
probability. We will call this agent πbasic. It is clear that many environments,
both complex and very simple, will have at least some structure that such an
basic
agent would take advantage of. Thus, for almost all µ we will have Vµπ >
rand
basic
Vµπ and so Υ(π) > Υ(πrand). Intuitively, this is what we would expect
basic
as π, while very simplistic, is surely more intelligent than πrand.

$$
\pi^{\tt b a s i c}
$$

$$
\mu
$$

$$
V_{\mu}^{\pi^{\tt b a s i c}}>
$$

$$
V_{\mu}^{\pi^{\mathtt{r a n d}}}
$$

$$
\Upsilon\left(\pi^{\mathrm{basic}}\right)>\Upsilon\left(\pi^{\mathrm{rand}}\right)
$$

$$
\pi^{\mathtt{r a n d}}
$$

$$
\pi^{\tt b a s i c}
$$

Similarly, as πdblue will fail to take advantage of even trivial regularities in
some of the most basic environments, Υ(πbasic) > Υ(πdblue). This is reasonable as our aim is to measure a machine’s level of general intelligence. Thus
an agent that can take advantage of basic regularities in a wide range of environments should rate more highly than a specialised machine that fails outside
of a very limited domain.

$$
\pi^{\tt d b l u e}
$$

$$
\Upsilon(\pi^{\tt b a s i c})>\Upsilon(\pi^{\tt d b l u e})
$$

A simple agent with more history. The first order structure of πbasic, while
very general, will miss many simple exploitable regularities. Consider the
following environment µalt. Let A = {up, down} and O = {ε}. In cycle k
the environment generates a reward of 2−k each time the agent’s action is
different to its previous action. Otherwise the reward is 0. We can define this
environment formally,


$$
\pi^{\tt b a s i c}
$$

$$
\mu^{\tt a l t}
$$

$$
\mathcal{A}=\{\mathrm{up},\mathrm{down}\}
$$

$$
\mathcal{O}=\{\varepsilon\}
$$

$$
\left[\bar{2^{-k}}\right.
\mu^{\tt a l t}(a x_{<k}a\underline{{x}}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{if}a_{k}\neq a_{k-1}\land r_{k}=2^{-k},}\\ {1}&{\mathrm{if}a_{k}=a_{k-1}\land r_{k}=0,}\\ {0}&{\mathrm{otherwise}.}\\ \end{array}\right.
$$

Clearly the optimal strategy for an agent is simply to alternate between the
actions up and down. Even though this is very simple, this strategy requires
the agent to correlate its current action with its previous action, something
basic
that π cannot do. Note that we set the reward in cycle k to be 2k in order
to satisfy our bounded reward sum condition.

$$
\pi^{\tt b a s i c}
$$

$$
2^{k}
$$

A natural extension of πbasic is to use a longer history of actions, observations and rewards in its internal table. Let π2back be the agent that
builds a table of statistics for the expected reward conditioned on the last
two actions, rewards and observations. It is immediately clear that π2back
will exploit the structure of the µalt environment. Furthermore, by definition
basic
π2back is a generalisation of π and thus it will adapt to any regularity that
2back basic
basic
π can adapt to. It follows then that in general Vµπ > Vµπ and so
basic
Υ(π2back) > Υ(π), as we would expect. In the same way we can extend the
history that the agent utilises back further and produce even more powerful

$$
\pi^{\tt b a s i c}
$$

$$
\pi^{\mathtt{2b a c k}}
$$

$$
\pi^{\vdots}
$$

$$
\mu^{\tt a l t}
$$

$$
\pi^{\tt2b a c k}
$$

$$
\pi^{\tt b a s i c}
$$

$$
\pi^{\tt b a s i c}
$$

$$
V_{\mu}^{\pi^{2\mathrm{back}}}>V_{\mu}^{\pi^{\mathrm{back}}}
$$

$$
\Upsilon\left(\pi^{2\mathrm{back}}\right)>\Upsilon\left(\pi^{\mathrm{basic}}\right)
$$ top
a = rest or climb
r = 2-k
a = climb
a = rest
bottom r = 0.0
r = 2-k-4

Figure 4.1.: A simple game in which the agent climbs a playground slide and
slides back down again. A shortsighted agent will always just rest
at the bottom of the slide.

agents that are able to adapt to more lengthy temporal structures and which
will have still higher universal intelligence.

A simple forward looking agent. In some environments simply trying to
maximise the next reward is not sufficient, the agent must also take into account the rewards that are likely to follow further into the future, that is,
the agent must plan ahead. Consider the following environment µslide. Let
A={rest, climb} and O = {ε}. Imagine there is a slide such as you would
see in a playground. The agent can rest at the bottom of the slide, for which
it receives a reward of 2−k−4. The alternative is to climb the slide, which gives
a reward of 0. Once at the top of the slide the agent always slides back down
no matter what action is taken; this gives a reward of 2−k. This deterministic
environment is illustrated in Figure 4.1.

$$
\mu^{\tt s l i d e}
$$

$$
\mathcal{A}=\{\mathrm{rest},\mathrm{climb}\}
$$

$$
\mathcal{O}=\{\varepsilon\}
$$

$$
2^{-k-4}
$$

$$
2^{-k}
$$

Because climbing receives a reward of 0, while resting receives a reward of
2−k−4, a very shortsighted agent that only tries to maximise the reward in
the next cycle will choose to stay at the bottom of the slide. Both πbasic and
π2back have this problem, even though they also take random actions with 0.1
probability and so will occasionally climb the slide by chance. Clearly this is
not optimal in terms of total reward over time.

$$
2^{-k-4}
$$

$$
\pi^{\tt b a s i c}
$$

$$
\pi^{\tt2b a c k}
$$

2forward
We can extend the π2back agent again by defining a new agent π that
with 0.9 probability chooses its next action to maximise not just the next
reward, but ˆrk + ˆrk+1, where ˆrk and ˆrk+1 are the agent’s estimates of the next
two rewards. As the estimate of ˆrk+1 will potentially depend not only on ak,
but also on ak+1, the agent assumes that ak+1 is chosen to simply maximise
the estimated reward ˆrk+1.

$$
\pi^{\mathtt{2b a c k}}
$$

$$
\pi^{\tt2f o r w a r d}
$$

$$
\hat{r}_{k}+\hat{r}_{k+1}
$$

$$
\hat{r}_{k}
$$

$$
\hat{r}_{k+1}
$$

$$
a_{k+1}
$$

$$
\hat{r}_{k+1}
$$

$$
a_{k}
$$

$$
a_{k+1}
$$

$$
\hat{r}_{k+1}
$$

The π2forward agent can see that by missing out on the resting reward of
2−k−4 for one cycle and climbing, a greater reward of 2−k will be had when
sliding back down the slide in the following cycle. Note that the value of the

$$
\pi^{\tt2f o r w a r d}
$$

$$
2^{-k-4}
$$

$$
2^{-k}
$$

4. Universal Intelligence Measure

time index k will have increased by the time the agent gets to slide down,
however this is not enough to change the optimal course of action.

2forward
By definition π2forward generalises π2back2back in a way that more closely reflects
the value function V and thus in general Vµπ > Vµπ. It then follows
2forward
that Υ(π) > Υ(π2back) as we would intuitively expect for this more
powerful agent.

$$
\pi^{\tt2f o r w a r d}
$$

$$
\pi^{\tt2b a c k}
$$

$$
V_{\mu}^{\pi^{2\mathrm{forward}^{\prime}}}>V_{\mu}^{\pi^{2\mathrm{back}}}
$$

$$
\Upsilon\left(\pi^{2\mathrm{forward}}\right)>\Upsilon\left(\pi^{2\mathrm{back}}\right)
$$

In a similar way agents of increasing complexity and adaptability can be
defined which will have still greater intelligence. However, with more complex
agents it is usually difficult to see whether one agent has more universal intelligence than another. Nevertheless, the simple examples above illustrate how
the more flexible and powerful an agent is, the higher V typically is and thus
the higher its universal intelligence.

A very intelligent agent. A very intelligent agent would perform well in
simple environments, and reasonably well compared to most other agents in
more complex environments. From the equation for universal intelligence this
would clearly produce a high value for Υ. Conversely, if Υ was high then
the equation for Υ implies that the agent must perform well in most simple
environments and reasonably well in many complex ones also. Thus, the agent
is able to achieve goals in a wide range of environments, as required by our
informal definition of intelligence.

A super intelligent agent. Consider what would be required to maximise
the value of Υ. By definition, a “perfect” agent would always pick the action
which had greatest expected future reward. To do this, for every environment
µ ∈ E the agent must take into account how likely it is that it is facing µ,
given the interaction history so far and the prior probability of µ, that is,
2−K(µ). It would then consider all possible future interactions that might
occur, how likely they are, and from this select the action in the current cycle
that maximises the expected future reward.

$$
\mu\in\mathbb{E}
$$

$$
\mu,
$$

$$
\mu,
$$

$$
2^{-K(\mu)}
$$

Essentially, this is the AIXI agent described in Section 2.10. The only difference is that AIXI was defined using discount parameters, while universal
intelligence avoided these by requiring the total reward from environments to
be bounded. If we remove discounting for AIXI and define it to work over
reward bounded environments, then the universal intelligence measure is in
some sense the dual of the universal agent AIXI. It follows that agents with
very high universal intelligence have powerful performance characteristics.

With our modified AIXI being the most intelligent agent by construction,
we can define the upper bound on universal intelligence to be,
()

$$
\bar{\Upsilon}:=\max_{\pi}\Upsilon(\pi)=\Upsilon(\pi^{\xi}).
$$

This upper bounds the intelligence of all future machines, no matter how
powerful their hardware and algorithms might be.

A human.

For simple environments, a human should be able to identify their
structure and exploit this to maximise reward. However, for more complex
environments it is hard to know how well a human would perform. Much of the
human brain is set up to process certain kinds of structured information from
the human sense organs, and thus is quite specialised, at least compared to the
extremely general setting considered here. Perhaps the amount of universal
machine intelligence that a human has is not that high compared to some
machine learning algorithms? It is difficult to know without experimental
results.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
