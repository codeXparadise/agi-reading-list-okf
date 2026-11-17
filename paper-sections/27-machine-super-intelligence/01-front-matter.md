---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: Front matter
section_role: front-matter
section_index: 1
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "The text below was extracted from the published source (PhD thesis (PDF)) on 2026-11-17. The full doctoral dissertation PDF, text extracted in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Front matter

> Section 1 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `front-matter` · pages n/a

The text below was extracted from the published source (PhD thesis (PDF)) on 2026-11-17. The full doctoral dissertation PDF, text extracted in reading order.

### Machine Super Intelligence

Doctoral Dissertation submitted to the
Faculty of Informatics of the University of Lugano
in partial fulfillment of the requirements for the degree of
Doctor of Philosophy

presented by
Shane Legg

under the supervision of
Prof. Dr. Marcus Hutter

June 2008

Copyright Shane Legg 2008

This document is licensed under a Creative Commons
Attribution-Share Alike 2.5 Switzerland License.

CC BY SA

Dissertation Committee

Prof. Dr. Marcus Hutter

Australian National University, Australia

Prof. Dr. J¨urgen Schmidhuber

IDSIA, Switzerland

Prof. Dr. Fernando Pedone

Technical University of Munich, Germany

University of Lugano, Switzerland

Prof. Dr. Matthias Hauswirth

University of Lugano, Switzerland

Prof. Dr. Marco Wiering

Utrecht University, The Netherlands

Supervisor

Prof. Dr. Marcus Hutter

PhD program director
Prof. Dr. Fabio Crestani

## Contents

Preface i
Thesis outline ........... .................... iii
Prerequisite knowledge ...... .................... vi
Acknowledgements........ .................... vi
1.Nature and Measurement of Intelligence 1
1.1.Theories of intelligence ... .................... 3
1.2.Definitions of human intelligence................. 4
1.3.Definitions of machine intelligence................ 9
1.4.Intelligence testing..... .................... 11
1.5.Human intelligence tests .. .................... 13
1.6.Animal intelligence tests .. .................... 15
1.7.Machine intelligence tests. .................... 16
1.8.Conclusion......... .................... 22
2.Universal Artificial Intelligence 23
2.1.Inductive inference..... .................... 23
2.2.Bayes’ rule......... .................... 25
2.3.Binary sequence prediction.................... 27
2.4.Solomonoff’s prior and Kolmogorov complexity......... 30
2.5.Solomonoff-Levin prior ... .................... 32
2.6.Universal inference..... .................... 36
2.7.Solomonoff induction .... .................... 38
2.8.Agent-environment model. .................... 39
2.9.Optimal informed agents .. .................... 43
2.10. Universal AIXI agent .... .................... 47
3.Taxonomy of Environments 53
3.1.Passive environments .... .................... 53
3.2.Active environments.... .................... 57
3.3.Some common problem classes.................. 60
3.4.Ergodic MDPs....... .................... 62
3.5.Environments that admit self-optimising agents ......... 65
3.6.Conclusion......... .................... 68
4.Universal Intelligence Measure 71
4.1.A formal definition of machine intelligence ............ 72

4.2.Universal intelligence of various agents...
4.3.Properties of universal intelligence.....
4.4.Response to common criticisms. ......
4.5.Conclusion............ ......
5.Limits of Computational Agents
5.1.Preliminaries........... ......
5.2.Prediction of computable sequences .....
5.3.Prediction of simple computable sequences .
5.4.Complexity of prediction ..... ......
5.5.Hard to predict sequences.... ......
5.6.The limits of mathematical analysis....
5.7.Conclusion............ ......
6.Temporal Difference Updating without a Learning Rate
6.1.Temporal difference learning ... ......
6.2.Derivation ............. ......
6.3.Estimating a small Markov process.....
6.4.A larger Markov process..... ......
6.5.Random Markov process ..... ......
6.6.Non-stationary Markov process. ......
6.7.Windy Gridworld ......... ......
6.8.Conclusion............ ......
7.Discussion
7.1.Are super intelligent machines possible?..
7.2.How could intelligent machines be developed?
7.3.Is building intelligent machines a good idea? .
A. Notation and Conventions
B. Ergodic MDPs admit self-optimising agents
B.1.Basic definitions......... ......
B.2.Analysis of stationary Markov chains ....
B.3.An optimal stationary policy.. ......
B.4.Convergence of expected average value...
C. Definitions of Intelligence
C.1.Collective definitions....... ......
C.2.Psychologist definitions..... ......
C.3.AI researcher definitions..... ......
Bibliography
Index

......
......
......
......
......
......
......
......
......
......
......
......
......
......
......
......
......
......
......
......
.....
.....
......
......
......
......
......
......
......

..... 78
..... 83
..... 86
..... 93
95
..... 96
..... 98
..... 100
..... 102
..... 103
..... 104
..... 106
109
..... 110
..... 112
..... 115
..... 117
..... 118
..... 119
..... 120
..... 123
125
..... 126
..... 128
..... 135
139
143
..... 143
..... 146
..... 152
..... 155
159
..... 159
..... 161
..... 164
167
179

Mystics exult in mystery and want it to stay mysterious.
Scientists exult in mystery for a different reason:
it gives them something to do.

Richard Dawkins in The God Delusion

## Preface

This thesis concerns the optimal behaviour of agents in unknown computable
environments, also known as universal artificial intelligence. These theoretical
agents are able to learn to perform optimally in many types of environments.
Although they are able to optimally use prior information about the environment if it is available, in many cases they also learn to perform optimally in the
absence of such information. Moreover, these agents can be proven to upper
bound the performance of general purpose computable agents. Clearly such
agents are extremely powerful and general, hence the name universal artificial
intelligence.

That such agents can be mathematically defined at all might come as a surprise to some. Surely then artificial intelligence has been solved? Not quite.
The problem is that the theory behind these universal agents assumes infinite
computational resources. Although this greatly simplifies the mathematical
definitions and analysis, it also means that these models cannot be directly
implemented as artificial intelligence algorithms. Efforts have been made to
scale these ideas down, however as yet none of these methods have produced
practical algorithms that have been adopted by the mainstream. The main
use of universal artificial intelligence theory thus far has been as a theoretical tool with which to mathematically study the properties of machine super
intelligence.

The foundations of universal intelligence date back to the origins of philosophy and inductive inference. Universal artificial intelligence proper started
with the work of Ray J. Solomonoff in the 1960’s. Solomonoff was considering
the problem of predicting binary sequences. What he discovered was a formulation for an inductive inference system that can be proven to very rapidly
learn to optimally predict any sequence that has a computable probability
distribution. Not only is this theory astonishingly powerful, it also brings together and elegantly formalises key philosophical principles behind inductive
inference. Furthermore, by considering special cases of Solomonoff’s model,
one can recover well known statistical principles such as maximum likelihood,
minimum description length and maximum entropy. This makes Solomonoff’s
model a kind of grand unified theory of inductive inference. Indeed, if it
were not for its incomputability, the problem of induction might be considered
solved. Whatever practical concerns one may have about Solomonoff’s model,
most would agree that it is nonetheless a beautiful blend of mathematics and
philosophy.

The main theoretical limitation of Solomonoff induction is that it only
addresses the problem of passive inductive learning, in particular sequence
prediction. Whether the agent’s predictions are correct or not has no effect on
the future observed sequence. Thus the agent is passive in the sense that it
is unable to influence the future. An example of this might be predicting the
movement of the planets across the sky, or maybe the stock market, assuming
that one is not wealthy enough to influence the market.

In the more general active case the agent is able to take actions which
may affect the observed future. For example, an agent playing chess not only
observes the other player, it is also able to make moves itself in order to
increase its chances of winning the game. This is a very general setting in
which seemingly any kind of goal directed problem can be framed. It is not
necessary to assume, as is typically done in game theory, that the environment,
in this case other player, plays optimally. We also do not assume that the
behaviour of the environment is Markovian, as is typically done in control
theory and reinforcement learning.

In the late 1990’s Marcus Hutter extended Solomonoff’s passive induction
model to the active case by combining it with sequential decision theory. This
produced a theory of universal agents, and in particular a universal agent for
a very general class of interactive environments, known as the AIXI agent.
Hutter was able to prove that the behaviour of universal agents converges to
optimal in any setting where this is at all possible for a general agent, and
that these agents are Pareto optimal in the sense that no agent can perform
as well in all environments and strictly better in at least one. These are the
strongest known results for a completely general purpose agent. Given that
AIXI has such generality and extreme performance characteristics, it can be
considered to be a theoretical model of a super intelligent agent.

Unfortunately, even stronger results showing that AIXI converges to optimal
behaviour rapidly, similar to Solomonoff’s convergence result, have been shown
to be impossible in some settings, and remain open questions in others. Indeed,
many questions about universal artificial intelligence remain open. In part
this is because the area is quite new with few people working in it, and partly
because proving results about universal intelligent agents seems to be difficult.

The goal of this thesis is to explore some of the open issues surrounding
universal artificial intelligence. In particular: In which settings the behaviour
of universal agents converges to optimal, the way in which AIXI theory relates
to the concept and definition of intelligence, the limitations that computable
agents face when trying to approximate theoretical super intelligent agents
such as AIXI, and finally some of the big picture implications of super intelligent machines and whether this is a topic that deserves greater study.

### Thesis outline

Much of the work presented in this thesis comes from prior publications. In
some cases whole chapters are heavily based on prior publications, in other
cases prior work is only mentioned in passing. Furthermore, while I wrote
the text of the thesis, naturally not all of the ideas and work presented are
my own. Besides the presented background material, many of the results and
ideas in this thesis have been developed through collaboration with various
colleagues, in particular my supervisor Marcus Hutter. This section outlines
the contents of the thesis and also provides some guidance on the nature of
my contribution to each chapter.

1) Nature and Measurement of Intelligence. Chapter 1 begins the thesis
with the most fundamental question of all: What is intelligence? Amazingly,
books and papers on artificial intelligence rarely delve into what intelligence
actually is, or what artificial intelligence is trying to achieve. When they
do address the topic they usually just mention the Turing test and that the
concept of intelligence is poorly defined, before moving on to algorithms that
presumably have this mysterious quality. As this thesis concerns theoretical
models of systems that we claim to be extremely intelligent, we must first explore the different tests and definitions of intelligence that have been proposed
for humans, animals and machines. We draw from these an informal definition
of intelligence that we will use throughout the rest of the thesis.

This overview of the theory, definition and testing of intelligence is my own
work. This chapter is based on (Legg and Hutter, 2007c), in particular the
parts which built upon (Legg and Hutter 2007b; 2007a).

2) Universal Artificial Intelligence. At present AIXI is not widely known in
academic circles, though it has captured the imagination of a community interested in new approaches to general purpose artificial intelligence, so called
artificial general intelligence (AGI). However even within this community, it
is clear that there is some confusion about AIXI and universal artificial intelligence. This may be attributable in part to the fact that current expositions of
AIXI are difficult for non-mathematicians to digest. As such, a less technical
introduction to the subject would be helpful. Not only should this help clear
up some misconceptions, it may also serve as an appetiser for the more technical treatments that have been published by Hutter. Chapter 2 provides such
an introduction. It starts with the basics of inductive inference and slowly
builds up to the AIXI agent and its key theoretical properties.

This introduction to universal artificial intelligence has not been published
before, though small parts of it were derived from (Hutter et al., 2007)
and (Legg, 1997). Section 2.6 is largely based on the material in (Hutter,
2007a), and the sections that follow this on (Hutter, 2005).

PREFACE

3) Optimality of AIXI. Hutter has proven that universal agents converge
to optimal behaviour in any environment where this is possible for a general
agent. He further showed that the result holds for certain types of Markov
decision processes, and claimed that this should generalise to related classes
of environments. Formally defining these environments and identifying the
additional conditions for the convergence result to hold was left as an open
problem. Indeed, it seems that nobody has ever documented the many abstract
environment classes that are studied and formally shown how they are related
to each other. In Chapter 3 we create such a taxonomy and identify the
environment classes in which universal agents are able to learn to behave
optimally. The diversity of these classes of environments adds weight to our
claim that AIXI is super intelligent.

Most of the classes of environments are well known, though their exact formalisations as presented are my own. The proofs of the relationships between
them and the resulting taxonomy of environment classes is my work. This
chapter is largely based on (Legg and Hutter, 2004).

4) Universal Intelligence Measure. If AIXI really is an optimally intelligent
machine, this suggests that we may be able to turn the problem around and
use universal artificial intelligence theory to formally define a universal measure of machine intelligence. In Chapter 4 we take the informal definition of
intelligence from Chapter 1 and abstract and formalise it using ideas from
the theory of universal artificial intelligence in Chapter 2. The result is an
alternate characterisation of Hutter’s intelligence order relation. This gives us
a formal definition of machine intelligence that we then compare with other
formal definitions and tests of machine intelligence that have been proposed.

The specific formulation of the universal intelligence measure is of my own
creation. The chapter is largely based on (Legg and Hutter, 2007c), in particular the parts of this paper which build upon (Legg and Hutter 2005b; 2006).

5) Limits of Computational Agents. One of the key reasons for studying incomputable but elegant theoretical models, such as Solomonoff induction and
AIXI, is that it is hoped that these will someday guide us towards powerful
computable models of artificial intelligence. Although there have been a number of attempts at converting these universal theories into practical methods,
the resulting methods have all been a mere shadow of their original founding
theory. Is this because we have not yet seen how to properly convert these
theories into practical algorithms, or are there more fundamental limitations
at work?

Chapter 5 explores this question mathematically. Specifically, it looks at
the existence and nature of computable agents which are powerful and extremely general. The results reveal a number of fundamental constraints on
any endeavour to construct very general artificial intelligence algorithms.

The elementary results at the start of the chapter are already well known,
nevertheless the proofs given are my own. The more significant results towards
the end are entirely original and are my own work. The chapter is based
primarily on (Legg, 2006b) which built upon the results in (Legg, 2006a). The
core results also appear with other related work in the book chapter (Legg
et al., 2008).

6) Fundamental Temporal Difference Learning. Although deriving practical
theories based on universal artificial intelligence is problematic, there still exist
many opportunities for theory to contribute to the development of new learning
techniques, albeit on a somewhat less grand scale. In Chapter 6 we derive an
equation for temporal difference learning from statistical principles. We start
with the variational principle and then bootstrap to produce an update-rule
for discounted state value estimates. The resulting equation is similar to the
standard equation for temporal difference learning with eligibility traces, so
called TD(λ), however it lacks the parameter that specifies the learning rate.
In the place of this free parameter there is now an equation for the learning
rate that is specific to each state transition. We experimentally test this new
learning rule against TD(λ). Finally, we make some preliminary investigations
into how to extend our new temporal difference algorithm to reinforcement
learning.

The derivation of the temporal difference learning rate comes from a collection of unpublished derivations by Hutter. I went through this collect of
handwritten notes, checked the proofs and took out what seemed to be the
most promising candidate for a new learning rule. The presented proof has
some reworking for improved presentation. The implementation and testing of
this update-rule is my own work, as is the extension to reinforcement learning
by merging it with Sarsa(λ) and Q(λ). These results were published in (Hutter
and Legg, 2007).

7) Discussion The concluding discussion on the future development of machine intelligence is my own. This has not been published before.

Appendix A A description of the mathematical notation used.

Appendix B A convergence proof for ergodic MDPs needed for key results in
Chapter 2

Appendix C This collection of definitions of intelligence, seemly the largest
in existence, is my own work. This section of the appendix was based on (Legg
and Hutter, 2007a).

Some of my other publications which are only mentioned in passing in this
thesis include (Smith et al., 1994; Legg, 1996; Cleary et al., 1996; Calude et al., 2000; Legg et al., 2004; Legg and Hutter, 2005a; Hutter and Legg, 2006).
Coverage of the research in this thesis in the popular scientific press includes
New Scientist magazine (Graham-Rowe, 2005), Le Monde de l’intelligence
(Fíevet, 2005), as well as numerous blog and online newspaper articles.

### Prerequisite knowledge

The thesis aims to be fairly self contained, however some knowledge of mathematics, statistics and theoretical computer science is assumed. From mathematics the reader should be familiar with linear algebra, calculus, basic set
theory and logic. From statistics, basic probability theory and elementary
distributions such as the uniform and binomial distributions. A knowledge of
measure theory would be beneficial, but is not essential. From theoretical computer science a knowledge of the basics such as Turing computation, universal
Turing machines, incomputability and the halting problem are needed. The
mathematical notation and conventions adopted are described in Appendix A.
The reader may want to consult this before beginning Chapter 2 as this is
where the mathematical material begins.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
