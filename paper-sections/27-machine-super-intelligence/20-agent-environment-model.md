---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.8. Agent-environment model
section_role: other
section_index: 20
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Up to this point we have only considered the inductive inference problem, either in terms of inferring hypotheses, or predicting the continuation of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.8. Agent-environment model

> Section 20 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Up to this point we have only considered the inductive inference problem,
either in terms of inferring hypotheses, or predicting the continuation of a
sequence. In both cases the agents were passive in the sense that they were
unable to take actions that affect the future. Obviously this greatly limits
them. More powerful is the class of active agents which not only observe their
environment, they are also able to take actions that may affect the environment. Such agents are able to explore and achieve goals in their environment.

observation
reward
agent environment
action

Figure 2.1.: The agent and the environment interact by sending action, observation and reward signals to each other.

We will need to consider active agents in order to satisfy our definition of intelligence, that is, the ability to achieve goals in a wide range of environments.
Solomonoff induction, although extremely powerful for sequence prediction,
operates in too limited a setting.

2.8.1 Example. Consider an agent that plays chess. It is not sufficient for
the agent to merely observe the other player. The agent actually has to decide
which moves to make, so as to win the game. Of course an important part of
this will be to carefully observe the other player, infer the strategy they are
using, and then predict which moves they are likely to make in the future.
Clearly then, inductive inference still plays an important role in the active
case. Now, however, the agent has to somehow take this inferred knowledge
and use it to develop a strategy of moves that will likely lead to winning the
game. This second part may not be easy. Indeed, even if the agent knew the
other player’s strategy in detail, it might take considerable effort to find a way
to overcome the other player’s strategy and win the game.

The framework in which we describe active agents is what we call the agentenvironment model. The model consists of two entities called the agent and
the environment. The agent receives input information from the environment,
which we will refer to as perceptions, and sends output information back to
the environment, which we call actions. The environment on the other hand
receives actions from the agent as input and generates perceptions as output.
Each perception consists of an observation component and a reward component. Observations are just regular information, however rewards have a
special significance because the goal of the agent is to try to gain as much
reward as possible from the environment. The basic structure of this agentenvironment interaction model is illustrated in Figure 2.1.

The only way that the agent can influence the environment, and thus the
rewards it receives, is through its action signals. Thus a good agent is one
that carefully selects its actions so as to cause the environment to generate as
much reward as possible. Presumably such an agent will make good use of any useful information contained in past rewards, actions and observations. For
example, the agent might find that certain actions tend to produce rewards
while others do not. In more complex environments the relationship between
the agent’s actions, what it observes and the rewards it receives might be very
difficult to discover.

The agent-environment model is the framework used in the area of artificial
intelligence known as reinforcement learning. It is equivalent to the controllerplant framework used in control theory, where the controller takes the place of
the agent, and the plant is the environment that must be controlled. With a
little imagination, a huge variety of problems can be expressed in this framework: everything from playing a game of chess, to landing an aeroplane, to
writing an award winning novel. Furthermore, the model says nothing about
how the agent or the environment work, it only describes their role within the
framework and thus many different environments and agents are possible.

2.8.2 Example. (Two coins game) To illustrate the agent-model consider
the following game. In each cycle two 50 coins are tossed. Before the coins
settle the player must guess at the number of heads that will result: either 0,
1, or 2. If the guess is correct the player gets to keep both coins and then two
new coins are produced and the game repeats. If the guess is incorrect the
player does not receive any coins, and the game is repeated.

In terms of the agent-environment model, the player is the agent and the
system that produces all the coins, tosses them and distributes the reward
when appropriate, is the environment. The agent’s actions are its guesses at
the number of heads in each iteration of the game: 0, 1 or 2. The observation
is the state of the coins when they settle, and the reward is either 0 or 1.

It is easy to see that for unbiased coins the most likely outcome is 1 head
and thus the optimal strategy for the agent is to always guess 1. However,
if the coins are significantly biased it might be optimal to guess either 0 or 2
heads depending on the bias.

Having introduced the framework, we now formalise it. The agent sends
information to the environment by sending symbols from some finite alphabet
of symbols, for example, {left, right, up, down}. We call this set the action
space and denote it by A. Similarly, the environment sends signals to the agent
with symbols from an alphabet called the perception space, which we denote
X. The reward space, denoted by R, is always a subset of the rational unit
interval [0, 1] ∩ Q. Restricting to ration numbers is a technical detail to ensure
that the information contained in each perception is finite. Every perception
consists of two separate parts: an observation and a reward. For example,
we might have X := {(cold, 0.0), (warm, 1.0), (hot, 0.3)} where the first part
describes what the agent observes (cold, warm or hot) and the second part
describes the reward (0.0, 1.0 or 0.3).

To denote symbols being sent we use the lower case variable names a, o and
r for actions, observations and rewards respectively. We index these in the

2. Universal Artificial Intelligence

order in which they occur, thus a1 is the agent’s first action, a2 is the second action and so on. The agent and the environment take turns at sending
symbols, starting with the agent. This produces a history of actions, observations and rewards which can be written, a1o1r1a2o2r2a3o3r3.... As we refer
to interaction histories a lot, we need to be able to represent these compactly.
Firstly, we introduce the symbol x ∈X to stand for a perception that consists of an observation and a reward. That is, ∀k : xk:= okrk. Our second
trick is to squeeze symbols together and then index them as blocks of symbols. For the complete interaction history up to and including cycle t, we
can write ax1:t:= a1x1a2x2a3...atxt. For the history before cycle t we use
ax<t:= ax1:t−1.

$$
a_{1}
$$

$$
a_{2}
$$

$$
a_{1}0_{1}r_{1}a_{2}0_{2}r_{2}a_{3}0_{3}r_{3}\ldots\ As
$$

$$
x\in\mathcal{X}
$$

$$
\forall k:x_{k}:=o_{k}r_{k}
$$

$$
a x_{1:t}:=a_{1}x_{1}a_{2}x_{2}a_{3}\cdots a_{t}x_{t}
$$

$$
ax_{<t}:=ax_{1:t-1}
$$

Before this section all our strings and sequences have been binary, now we
have strings and sequences from potentially larger alphabets, such as A and
X. Either we can encode symbols from these alphabets as uniquely identifiable
binary strings, or we can extend our previous definitions of strings, measures
etc. to larger alphabets in the obvious way. In some results technical problems
can arise, for example, it takes some work to extend Theorem 2.7.1 to arbitrary
alphabets (Hutter, 2001). Here we can safely ignore these technical issues and
simply extend our previous definitions to general alphabets.

$$
\mathcal{X}
$$

Formally, the agent is a function, denoted by π, which takes the current
history as input and chooses the next action as output. We do not want to
restrict the agent in any way, in particular we do not require that it is deterministic. A convenient way of representing the agent then is as a probability
measure over actions conditioned on the complete interaction history. Thus,
π(ax1a2) is the probability of action a2 in the second cycle, given that the
current history is ax1. A deterministic agent is simply one that always assigns
a probability of 1 to a single action for any given history. As the history that
the agent can use to select its action expands indefinitely, the agent need not
be Markovian. Indeed, how the agent produces its distribution over actions
for any given history is left open. In practical artificial intelligence the agent
will of course be a machine and so π will be a computable function. In general
however, the system generating the probabilities for different actions could be
just about anything:√ An algorithm that generates probabilities according to
successive digits of e, an incomputable function, or even a human pushing
buttons on a keyboard.

$$
\pi
$$

$$
\pi(ax_{1}\underline{a}_{2})
$$

$$
a_{2}
$$

$$
ax_{1}
$$

$$
\pi
$$

$$
\sqrt{e}
$$

We define the environment, denoted by µ, in a similar way. Specifically, for
all k ∈ N the probability of xk, given the current interaction history ax<kak,
is given by the conditional probability measure µ(ax<kaxk).

$$
\mu,
$$

$$
k\in\mathbb{N}
$$

$$
x_{k}
$$

$$
ax_{<k}a_{k}
$$

$$
\mu(a x_{<k}a\underline{{x}}_{k})
$$

Technically, neither µ nor π completely define a measure over the space of
interaction sequences. They only define the conditional probability of certain
symbols given an interaction history: π defines the conditional probability over
the actions, and µ of the perceptions. However, taken together they do define
a measure over the interaction sequences that we will denote πµ. Specifically,
we can chain together the conditional probabilities defined by π and µ to work

$$
\mu
$$

$$
\pi
$$

$$
\pi
$$

$$
\mu
$$

$$
\begin{array}{c}\pi\\\mu\end{array}
$$

$$
\pi
$$

$$
\mu
$$ out the probability of any interaction. For example,

$$
\mu(\underline{{a x}}_{1:2}):=\pi(\underline{{a}}_{1})\mu(a\underline{{x}}_{1})\pi(a x_{1}\underline{{a}}_{2})\mu(a x_{1}a\underline{{x}}_{2}).
$$

When we need to take an expectation over interaction sequences this is the
measure we will use. However in most other cases we will only need the
conditional probabilities defined by π or µ.

2.8.3 Example. To illustrate this formalism, consider again the Two Coins
Game introduced in Example 2.8.2. Let X := {0, 1, 2}×{0, 1} be the perception space representing the number of heads after tossing the two coins and
the value of the received reward. Likewise let A := {0, 1, 2} be the action
space representing the agent’s guess at the number of heads that will occur.
Assuming two fair coins, and recalling that xk:= okrk, we can represent this
environment by defining ∀k ∈ N:


$$
\mathcal{X}:=\{0,1,2\}\times\{0,1\}
$$

$$
\mathcal{A}:=\{0,1,2\}
$$

$$
x_{k}:=o_{k}r_{k}
$$

$$
\forall k\in\mathbb{N}
$$

$$
\mu(\mathit{ax}_{<k}\mathit{a}\underline{{x}}_{k}):=\left\{\begin{array}{l l}{\frac{1}{4}}&{\quad\mathit{\operatorname{if}}~a_{k}=0\land o_{k}=0\land r_{k}=1,}\\ {\frac{3}{4}}&{\quad\mathit{\operatorname{if}}~a_{k}=0\land o_{k}\neq0\land r_{k}=0,}\\ {\frac{1}{2}}&{\quad\mathit{\operatorname{if}}~a_{k}=1\land o_{k}=1\land r_{k}=1,}\\ {\frac{1}{2}}&{\quad\mathit{\operatorname{if}}~a_{k}=1\land o_{k}\neq1\land r_{k}=0,}\\ {\frac{1}{4}}&{\quad\mathit{\operatorname{if}}~a_{k}=2\land o_{k}=2\land r_{k}=1,}\\ {\frac{3}{4}}&{\quad\mathit{\operatorname{if}}~a_{k}=2\land o_{k}\neq2\land r_{k}=0,}\\ {0}&{\quad\mathit{\operatorname{otherwise}}.}\\ \end{array}\right.
$$

An agent that performs well in this environment would be,
{

$$
\pi(a x_{<k}\underline{{a}}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{for}a_{k}=1,}\\ {0}&{\mathrm{otherwise}.}\end{array}\right.
$$

That is, always guess that one head will be the result of the two coins being
tossed. A more complex agent might keep count of how many heads occur in
each cycle and then adapt its strategy if it seems that the coins are sufficiently
biased. For example, a Bayesian agent might use techniques similar to those
used to predict coin flips in Examples 2.3.2 and 2.3.3.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
