---
type: PhD Thesis
title: Machine Super Intelligence
description: "Defines universal intelligence formally as expected performance across all computable environments, weighted by simplicity, and follows the consequences for agents, compression and safety."
resource: https://www.vetta.org/documents/Machine_Super_Intelligence.pdf
tags: [agi-reading-list, kolmogorov-complexity, thesis]
sequence: 27
section: /sections/04-theory-complexity-and-optimization.md
authors: [Shane Legg]
year: 2008
venue: "PhD thesis, University of Lugano"
topics: ["/topics/kolmogorov-complexity.md"]
builds_on: ["/papers/24-tutorial-minimum-description-length.md", "/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md"]
enables: []
sources:
  - id: reading-list
    resource: /references/the-30-papers-to-ai-mastery.md
    title: The 30 Papers to AI Mastery (curated by @rachit.speaks)
  - id: original
    resource: https://www.vetta.org/documents/Machine_Super_Intelligence.pdf
    title: "Machine Super Intelligence (PhD thesis, University of Lugano)"
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
extraction:
  full_text: web-extracted
  source_kind: PhD thesis (PDF)
  coverage: complete
  tool: Firecrawl PDF parser
  characters: 381204
figures:
  local: 0
  remote: 0
  note: no figures: the source PDF is larger than the transfer limit, read them in the original
---

# Machine Super Intelligence

**Authors:** Shane Legg  
**Year:** 2008 · **Venue:** PhD thesis, University of Lugano · **Position in the list:** 27 of 30  
**Read the original:** <https://www.vetta.org/documents/Machine_Super_Intelligence.pdf>

## Overview

Defines universal intelligence formally as expected performance across all computable environments, weighted by simplicity, and follows the consequences for agents, compression and safety. Supervised by Marcus Hutter; Legg went on to co-found DeepMind.[^reading-list]

## Where it sits

This paper is part of [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md), the theory, complexity & optimization section of the list.

It assumes you have read: [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md), [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md).

## Full text

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

### Acknowledgements

First and foremost I would like to thank my supervisor Marcus Hutter. Getting a PhD is a somewhat long process and I have appreciated his guidance
throughout this endeavour. I am especially grateful for the way in which he
has always gone through my work carefully and provided detailed feedback on
where there was room for improvement. Not every graduate student receives
such careful appraisal and guidance during this long voyage.

Essentially all of the research contained in this thesis was carried out at the
Dalle Molle Institute for Artificial Intelligence (IDSIA) near Lugano, Switzerland. It has been a pleasure to work with such a talented group of people
over the last 4 years. In particular I would like to thank Alexey Chernov for
encouraging me to develop a few short proofs on the limits of computational
prediction systems into a full length paper. For me, that was a turning point
in my thesis.

A special thanks goes to my reading group: Jeff Rose, Cyrus Hall, Giovanni
Luca Ciampaglia, Katerina Barone-Adesi, Tom Schaul and Daan Wierstra.
They went through most of my thesis finding typos and places where things
were not well explained. The thesis is no doubt far more intelligible due
to their efforts. Special thanks also to my mother Gail Legg and Christoph
Kolodziejski for further proof reading efforts.

My research has benefited from interaction with many other colleagues,
both at IDSIA and other research centres, in particular J¨urgen Schmidhuber, Jan Poland, Daniil Ryabko, Faustino Gomez, Matteo Gagliolo, Frederick

Ducatelle, Alex Graves, Bram Bakker, Viktor Zhumatiy and Laurent Orseau.
I would also like to thank the institute secretary, Cinzia Daldini, for her amazing ability to find solutions to all manner of issues. It made coming to work
at IDSIA and living in Switzerland a breeze. Finally, thanks to etomchek for
designing the beautiful electric sheep on the front cover, and releasing it under
the creative commons licence. I always wanted a sheep on the cover of my PhD
thesis.

This research was funded by the Swiss National Science Foundation under
grants 2100-67712.0 and 200020-107616. Many funding agencies are not willing
to support such blue-sky research. Their backing has been greatly appreciated.

Lugano, Switzerland, June 2008

Shane Legg

PREFACE

## 1. Nature and Measurement of Intelligence

“Innumerable tests are available for measuring intelligence, yet no
one is quite certain of what intelligence is, or even just what it is
that the available tests are measuring.” Gregory (1998)

What is intelligence? It is a concept that we use in our daily lives that
seems to have a fairly concrete, though perhaps naive, meaning. We say that
our friend who got an A in his calculus test is very intelligent, or perhaps our
cat who has learnt to go into hiding at the first mention of the word “vet”.
Although this intuitive notion of intelligence presents us with no difficulties, if
we attempt to dig deeper and define it in precise terms we find the concept to
be very difficult to nail down. Perhaps the ability to learn quickly is central to
intelligence? Or perhaps the total sum of one’s knowledge is more important?
Perhaps communication and the ability to use language play a central role?
What about “thinking” or the ability to perform abstract reasoning? How
about the ability to be creative and solve problems? Intelligence involves a
perplexing mixture of concepts, many of which are equally difficult to define.

Psychologists have been grappling with these issues ever since humans first
became fascinated with the nature of the mind. Debates have raged back and
forth concerning the correct definition of intelligence and how best to measure
the intelligence of individuals. These debates have in many instances been very
heated as what is at stake is not merely a scientific definition, but a fundamental issue of how we measure and value humans: Is one employee smarter than
another? Are men on average more intelligent than women? Are white people
smarter than black people? As a result intelligence tests, and their creators,
have on occasion been the subject of intense public scrutiny. Simply determining whether a test, perhaps quite unintentionally, is partly a reflection of
the race, gender, culture or social class of its creator is a subtle, complex and
often politically charged issue (Gould, 1981; Herrnstein and Murray, 1996).
Not surprisingly, many have concluded that it is wise to stay well clear of this
topic.

In reality the situation is not as bad as it is sometimes made out to be.
Although the details of the definition are debated, in broad terms a fair degree of consensus has been achieved about the scientific definition of human
intelligence and how to measure it (Gottfredson, 1997a; Sternberg and Berg,
1986). Indeed it is widely recognised that when standard intelligence tests are
correctly applied and interpreted, they all measure approximately the same

1. Nature and Measurement of Intelligence

thing (Gottfredson, 1997a). Furthermore, what they measure is both stable
over time in individuals and has significant predictive power, in particular for
future academic performance and other mentally demanding pursuits. The issues that continue to draw debate are questions such as whether the tests test
only a part or a particular type of intelligence, or whether they are somehow
biased towards a particular group or set of mental skills. Great effort has gone
into dealing with these issues, but they are difficult problems with no easy
solutions.

Somewhat disconnected from this exists a parallel debate over the nature
of intelligence in the context of machines. While the debate is less politically
charged, in some ways the central issues are even more difficult. Machines can
have physical forms, sensors, actuators, means of communication, information
processing abilities and exist in environments that are totally unlike those that
we experience. This makes the concept of “machine intelligence” particularly
difficult to get a handle on. In some cases, a machine may have properties that
are similar to human intelligence, and so it might be reasonable to describe
the machine as also being intelligent. In other situations this view is far too
limited and anthropocentric. Ideally we would like to be able to measure the
intelligence of a wide range of systems: humans, dogs, flies, robots or even
disembodied systems such as chat-bots, expert systems, classification systems
and prediction algorithms (Johnson, 1992; Albus, 1991).

One response to this problem might be to develop specific kinds of tests
for specific kinds of entities, just as intelligence tests for children differ to
intelligence tests for adults. While this works well when testing humans of
different ages, it comes undone when we need to measure the intelligence of
entities which are profoundly different to each other in terms of their cognitive
capacities, speed, senses, environments in which they operate, and so on. To
measure the intelligence of such diverse systems in a meaningful way we must
step back from the specifics of particular systems and establish fundamentally
what it is that we are really trying to measure.

The difficulty of forming a highly general notion of intelligence is readily
apparent. Consider, for example, that memory and numerical computation
tasks were once regarded as defining hallmarks of human intelligence. We now
know that these tasks are absolutely trivial for a machine and do not test its
intelligence in any meaningful sense. Indeed, even the mentally demanding
task of playing chess can now be largely reduced to brute force search (Hsu
et al., 1995). What else may in time be possible with relatively simple algorithms running on powerful machines is hard to say. What we can be sure
of is that, as technology advances, our concept of intelligence will continue to
evolve with it.

How then are we to develop a concept of intelligence that is applicable to
all kinds of systems? Any proposed definition must encompass the essence
of human intelligence, as well as other possibilities, in a consistent way. It
should not be limited to any particular set of senses, environments or goals,
nor should it be limited to any specific kind of hardware, such as silicon or biological neurons. It should be based on principles which are fundamental
and thus unlikely to alter over time. Furthermore, the definition of intelligence
should ideally be formally expressed, objective, and practically realisable as
an effective test. Before attempting to construct such a formal definition in
Chapter 4, in this chapter we will first survey existing definitions, tests and
theories of intelligence. We are particularly interested in common themes and
general perspectives on intelligence that could be applicable to many kinds of
systems, including machines.

### 1.1. Theories of intelligence

A central question in the study of intelligence concerns whether intelligence
should be viewed as one ability, or many. On one side of the debate are
the theories that view intelligence as consisting of many different components
and that identifying these components is important to understanding intelligence. Different theories propose different ways to do this. One of the first was
Thurstone’s “multiple-factors” theory which considers seven “primary mental
abilities”: verbal comprehension, word fluency, number facility, spatial visualisation, associative memory, perceptual speed and reasoning (Thurstone, 1938).
Another approach is Sternberg’s “Triarchic Mind” which breaks intelligence
down into analytical intelligence, creative intelligence, and practical intelligence (Sternberg, 1985), however this model is now considered outdated, even
by Sternberg himself.

Taking the number of components to an extreme is Guilford’s “Structure of
Intellect” theory. Under this theory there are three fundamental dimensions:
contents, operations, and products. Together these give rise to 120 different
categories (Guilford, 1967). In later work this increased to 150 categories. This
theory has been criticised due to the fact that measuring such precise combinations of cognitive capacities in individuals seems to be infeasible and thus it
is difficult to experimentally study such a fine-grained model of intelligence.

A recently popular approach is Gardner’s “multiple intelligences” where he
argues that the components of human intelligence are sufficiently separate
that they are actually different “intelligences”(Gardner, 1993). Based on the
structure of the human brain he identifies these intelligences to be linguistic,
musical, logical-mathematical, spatial, bodily kinaesthetic, intra-personal and
inter-personal intelligence. Although Gardner’s theory of multiple intelligences
has certainly captured the imagination of the public, it remains to be seen to
what degree it will have a lasting impact in professional circles.

At the other end of the spectrum is the work of Spearman and those that
have followed in his approach. Here intelligence is seen as a very general
mental ability that underlies and contributes to all other mental abilities. As
evidence they point to the fact that an individual’s performance levels in reasoning, association, linguistic, spatial thinking, pattern identification etc. are
positively correlated. Spearman called this positive statistical correlation be- tween different mental abilities the “g-factor”, where g stands for “general
intelligence”(Spearman, 1927). Because standard IQ tests measure a range of
key cognitive abilities, from a collection of scores on different cognitive tasks
we can estimate an individual’s g-factor. Some who consider the generality
of intelligence to be primary take the g-factor to be the very definition of
intelligence (Gottfredson, 2002).

A well known refinement to the g-factor theory due to Cattell is to distinguish between “fluid intelligence”, which is a very general and flexible innate
ability to deal with problems and complexity, and “crystallized intelligence”,
which measures the knowledge and abilities that an individual has acquired
over time (Cattell, 1987). For example, while an adolescent may have a similar
level of fluid intelligence to that of an adult, their level of crystallized intelligence is typically lower due to less life experience (Horn, 1970). Although it is
difficult to determine to what extent these two influence each other, the distinction is an important one because it captures two distinct notions of what
the word “intelligence” means.

As the g-factor is simply the statistical correlation between different kinds
of mental abilities, it is not fundamentally inconsistent with the view that
intelligence can have multiple aspects or dimensions. Thus a synthesis of the
two perspectives is possible by viewing intelligence as a hierarchy with the gfactor at its apex and increasing levels of specialisation for the different aspects
of intelligence forming branches (Carroll, 1993). For example, an individual
might have a high g-factor, which contributes to all of their cognitive abilities,
but also have an especially well developed musical sense. This hierarchical
view of intelligence is now quite popular (Neisser et al., 1996).

### 1.2. Definitions of human intelligence

“Viewed narrowly, there seem to be almost as many definitions of
intelligence as there were experts asked to define it.” R. J. Sternberg quoted in (Gregory, 1998)

In this section and the next we will overview a range of definitions of intelligence that have been given by psychologists. For an even more extensive
collection of definitions of intelligence, indeed the largest collection that we
are aware of, see Appendix C or visit our online collection (Legg and Hutter,
2007a). Although definitions differ, there are many reoccurring features; in
some cases these are explicitly stated, while in others they are more implicit.
We start by considering ten definitions that take a similar perspective:

“It seems to us that in intelligence there is a fundamental faculty, the
alteration or the lack of which, is of the utmost importance for practical life. This faculty is judgement, otherwise called good sense, practical sense, initiative, the faculty of adapting oneself to circumstances.”
Binet and Simon (1905)

“The capacity to learn or to profit by experience.” Dearborn quoted
in (Sternberg, 2000)

“Ability to adapt oneself adequately to relatively new situations in life.”
Pinter quoted in (Sternberg, 2000)

“A person possesses intelligence insofar as he has learned, or can learn, to
adjust himself to his environment.” Colvin quoted in (Sternberg, 2000)

“We shall use the term ‘intelligence’ to mean the ability of an organism
to solve new problems . . . ” Bingham (1937)

“A global concept that involves an individual’s ability to act purposefully,
think rationally, and deal effectively with the environment.” Wechsler
(1958)

“Individuals differ from one another in their ability to understand complex ideas, to adapt effectively to the environment, to learn from experience, to engage in various forms of reasoning, to overcome obstacles
by taking thought.” American Psychological Association (Neisser et al.,
1996)

“. . . I prefer to refer to it as ‘successful intelligence.’ And the reason is
that the emphasis is on the use of your intelligence to achieve success in
your life. So I define it as your skill in achieving whatever it is you want
to attain in your life within your sociocultural context — meaning that
people have different goals for themselves, and for some it’s to get very
good grades in school and to do well on tests, and for others it might be to
become a very good basketball player or actress or musician.” Sternberg
(2003)

“Intelligence is part of the internal environment that shows through at
the interface between person and external environment as a function of
cognitive task demands.” R. E. Snow quoted in (Slatter, 2001)

“. . . certain set of cognitive capacities that enable an individual to adapt
and thrive in any given environment they find themselves in, and those
cognitive capacities include things like memory and retrieval, and problem solving and so forth. There’s a cluster of cognitive abilities that lead
to successful adaptation to a wide range of environments.” Simonton
(2003)

Perhaps the most elementary common feature of these definitions is that
intelligence is seen as a property of an individual who is interacting with an
external environment, problem or situation. Indeed, at least this much is
common to practically all proposed definitions of intelligence.

Another common feature is that an individual’s intelligence is related to
their ability to succeed or profit. This implies the existence of some kind of objective or goal. What the goal is, is not specified, indeed individuals’ goals
may be varied. The important thing is that the individual is able to carefully
choose their actions in a way that leads to them accomplishing their goals.
The greater this capacity to succeed with respect to various goals, the greater
the individual’s intelligence.

The strong emphasis on learning, adaption and experience in these definitions implies that the environment is not fully known to the individual and
may contain new situations that could not have been anticipated in advance.
Thus intelligence is not the ability to deal with a fully known environment,
but rather the ability to deal with some range of possibilities which cannot be
wholly anticipated. What is important then is that the individual is able to
quickly learn and adapt so as to perform as well as possible over a wide range
of environments, situations, tasks and problems. Collectively we will refer to
these as “environments”, similar to some of the definitions above.

Bringing these key features together gives us what we believe to be the
essence of intelligence in its most general form:

Intelligence measures an agent’s ability to achieve goals in a wide
range of environments.

We take this to be our informal working definition of intelligence for this thesis.
The remainder of this section considers a range of other definitions that are
not as strongly connected to our adopted definition. Usually it is not that they
are entirely incompatible with our definition, but rather they stress different
aspects of intelligence. The following definition is an especially interesting
definition as it was given as part of a group statement signed by 52 experts in
the field. As such it obviously represents a fairly mainstream perspective:

“Intelligence is a very general mental capability that, among other things,
involves the ability to reason, plan, solve problems, think abstractly,
comprehend complex ideas, learn quickly and learn from experience.”
Gottfredson (1997a)

Reasoning, planning, solving problems, abstract thinking, learning from experience and so on, these are all mental abilities that allow us to successfully
achieve goals. If we were missing any one of these capacities, we would clearly
be less able to successfully deal with such a wide range of environments. Thus,
these capacities are implicit in our definition also. The difference is that our
definition does not attempt to specify what capabilities might be needed, something which is clearly very difficult and would depend on the particular tasks
that the agent must deal with. Our approach is to consider intelligence to be
the effect of capacities such as those listed above. It is not the result of having
any specific set of capacities. Indeed, intelligence could also be the effect of
many other capacities, some of which humans may not have. In summary,
our definition is not in conflict with the above definition, rather it is that our
definition is more abstract and general.

“. . . in its lowest terms intelligence is present where the individual animal, or human being, is aware, however dimly, of the relevance of his
behaviour to an objective. Many definitions of what is indefinable have
been attempted by psychologists, of which the least unsatisfactory are 1.
the capacity to meet novel situations, or to learn to do so, by new adaptive responses and 2. the ability to perform tests or tasks, involving the
grasping of relationships, the degree of intelligence being proportional to
the complexity, or the abstractness, or both, of the relationship.” Drever
(1952)

This definition has many similarities to ours. Firstly, it emphasises the
agent’s ability to choose its actions so as to achieve an objective, or in our
terminology, a goal. It then goes on to stress the agent’s ability to deal with
situations which have not been encountered before. In our terminology, this is
the ability to deal with a wide range of environments. Finally, this definition
highlights the agent’s ability to perform tests or tasks, something which is
entirely consistent with our performance orientated perspective of intelligence.

“Intelligence is not a single, unitary ability, but rather a composite of several functions. The term denotes that combination of abilities required
for survival and advancement within a particular culture.” Anastasi
(1992)

This definition does not specify exactly which capacities are important, only
that they should enable the individual to survive and advance with the culture.
As such this is a more abstract “success” orientated definition of intelligence,
like ours. Naturally, culture is a part of the agent’s environment, though only
complex environments with other agents would have true culture.

“The ability to carry on abstract thinking.” L. M. Terman quoted
in (Sternberg, 2000)

This is not really much of a definition as it simply shifts the problem of
defining intelligence to the problem of defining abstract thinking. The same
is true of many other definitions that refer to things such as imagination,
creativity or consciousness. The following definition has a similar problem:

“The capacity for knowledge, and knowledge possessed.” Henmon (1921)

What exactly constitutes “knowledge”, as opposed to perhaps data or information? For example, does a library contain a lot of knowledge, and if so, is it
intelligent? Or perhaps the internet? Modern concepts of the word knowledge
stress the fact that the information has to be in some sense properly contextualised so that it has meaning. Defining this more precisely appears to be difficult however. Because this definition of intelligence dates from 1921, perhaps it reflects pre-information age thinking when computers with vast storage
capacities did not exist.

Nonetheless, our definition of intelligence is not entirely inconsistent with
the above definition in that an individual may be required to know many
things, or have a significant capacity for knowledge, in order to perform well
in some environments. However, our definition is narrower in that knowledge,
or the capacity for knowledge, is not by itself sufficient. We require that the
knowledge can be used effectively. Indeed, unless information can be effectively
utilised for various purposes, it seems reasonable to consider it to be merely
“data”, rather than “knowledge”.

“The capacity to acquire capacity.” H. Woodrow quoted in (Sternberg,
2000)

The definition of Woodrow is typical of those that emphasise not the current
ability of the individual, but rather the individual’s ability to expand and
develop new abilities. This is a fundamental point of divergence for many
views on intelligence. Consider the following question: Is a young child as
intelligent as an adult? From one perspective, children are very intelligent
because they can learn and adapt to new situations quickly. On the other
hand, a child is unable to do many things due to a lack of knowledge and
experience and thus will make mistakes an adult would know to avoid. These
need not just be physical acts, they could also be more subtle things like
errors in reasoning as their mind, while very malleable, has not yet matured.
In which case, perhaps their intelligence is currently low, but will increase with
time and experience?

Fundamentally, this difference in perspective is a question of time scale:
Must an agent be able to tackle some task immediately, or perhaps after a
short period of time during which learning can take place, or perhaps it only
matters that they can eventually learn to deal with the problem? Being able
to deal with a difficult problem immediately is a matter of experience, rather
than intelligence. While being able to deal with it in the very long run might
not require much intelligence at all, for example, simply trying a vast number
of possible solutions might eventually produce the desired results. Intelligence
then seems to be the ability to adapt and learn as quickly as possible given
the constraints imposed by the problem at hand.

“Intelligence is a general factor that runs through all types of performance.” A. Jensen

At first this might not look like a definition of intelligence, but it makes an
important point: Intelligence is not really the ability to do anything in particular, rather it is a very general ability that affects many kinds of performance.
Conversely, by measuring many different kinds of performance we can estimate
an individual’s intelligence. This is consistent with our definition’s emphasis
on the agent’s ability to perform well in many environments.

“Intelligence is what is measured by intelligence tests.” Boring (1923)

Boring’s famous definition of intelligence takes this idea a step further. If intelligence is not the ability to do anything in particular, but rather an abstract
ability that indirectly affects performance in many tasks, then perhaps it is
most concretely described as the ability to do the kind of abstract problems
that appear in intelligence tests? In which case, Boring’s definition is not as
facetious as it first appears. This definition also highlights the fact that the
concept of intelligence, and how it is measured, are intimately related. In the
context of this paper we refer to these as definitions of intelligence, and tests of
intelligence, respectively, although in some cases the distinction is not sharp.

### 1.3. Definitions of machine intelligence

The following sample of informal definitions of machine intelligence capture a
range of perspectives. There also exist several formal definitions and tests of
machine intelligence, however we will deal with those in Chapter 4. We begin
with five definitions that have clear connections to our informal definition:

“. . . the mental ability to sustain successful life.” K. Warwick quoted
in (Asohan, 2003)

“. . . doing well at a broad range of tasks is an empirical definition of
‘intelligence’ ” Masum et al. (2002)

“Intelligence is the computational part of the ability to achieve goals in
the world. Varying kinds and degrees of intelligence occur in people,
many animals and some machines.” McCarthy (2004)

“Any system . . . that generates adaptive behaviour to meet goals in a
range of environments can be said to be intelligent.” Fogel (1995)

“. . . the ability of a system to act appropriately in an uncertain environment, where appropriate action is that which increases the probability
of success, and success is the achievement of behavioral subgoals that
support the system’s ultimate goal.” Albus (1991)

The position taken by Albus is especially similar to ours. Although the
quote above does not explicitly mention the need to be able to perform well in
a wide range of environments, at a later point in the same paper he mentions
the need to be able to succeed in a “large variety of circumstances”.

“Intelligent systems are expected to work, and work well, in many different environments. Their property of intelligence allows them to maximize the probability of success even if full knowledge of the situation
is not available. Functioning of intelligent systems cannot be considered
separately from the environment and the concrete situation including
the goal.” Gudwin (2000)

1. Nature and Measurement of Intelligence

While this definition is consistent with the position we have taken, when
trying to actually test the intelligence of an agent Gudwin does not believe
that a “black box” behaviour based approach is sufficient, rather his approach
is to look at the “. . . architectural details of structures, organizations, processes
and algorithms used in the construction of the intelligent systems,” (Gudwin,
2000). Our perspective is simply to not care whether an agent looks intelligent
on the inside. If it is able to perform well in a wide range of environments,
that is all that matters.

“We define two perspectives on artificial system intelligence: (1) native intelligence, expressed in the specified complexity inherent in the
information content of the system, and (2) performance intelligence, expressed in the successful (i.e., goal-achieving) performance of the system
in a complicated environment.” Horst (2002)

Here we see two distinct notions of intelligence, a performance based one
and an information content one. This is similar to the distinction between
fluid intelligence and crystallized intelligence made by the psychologist Cattell
(see Section 1.1). The performance based notion of intelligence is similar to
our definition with the exception that performance is measured in a complex
environment rather than across a wide range of environments. This perspective
appears in some other definitions also,

“. . . the ability to solve hard problems.” Minsky (1985)

“Achieving complex goals in complex environments” Goertzel (2006)

The emphasis on complex goals and environments is not really so different
to our “wide range of environments” in that any agent which could not achieve
simple goals in simple environments presumably would not be considered intelligent. One might argue that the ability to achieve truly complex goals in
complex environments requires the ability to achieve simple ones, in which
case the two perspectives are equivalent.

Some definitions emphasise not just the ability to perform well, but also the
need for efficiency:

“[An intelligent agent does what] is appropriate for its circumstances
and its goal, it is flexible to changing environments and changing goals,
it learns from experience, and it makes appropriate choices given perceptual limitations and finite computation.” Poole et al. (1998)

“. . . in any real situation behavior appropriate to the ends of the system
and adaptive to the demands of the environment can occur, within some
limits of speed and complexity.” Newell and Simon (1976)

“Intelligence is the ability to use optimally limited resources – including
time – to achieve goals.” Kurzweil (2000)

“Intelligence is the ability for an information processing agent to adapt
to its environment with insufficient knowledge and resources.” Wang
(1995)

We consider the addition of resource limitations to the definition of intelligence to be either superfluous, or wrong. In the first case, if limited computational resources are a fundamental and unavoidable part of reality, which
certainly seems to be the case, then their addition to the definition of intelligence is unnecessary. Perhaps the first three definitions above fall into this
category.

On the other hand, if limited resources are not a fundamental restriction,
for example a new model of computation was discovered that was vastly more
powerful than the current model, then it would be odd to claim that the
unbelievably powerful machines that would then result were not intelligent.
Normally we do not judge the intelligence of something relative to the resources
it uses. For example, if a rat had human level learning and problem solving
abilities, we would not think of the rat as being more intelligent than a human
due to the fact that its brain was much smaller.

While we do not consider efficiency to be a part of the definition of intelligence, this is not to say that considering the efficiency of agents is unimportant.
Indeed, a key goal of artificial intelligence is to find algorithms which have the
greatest efficiency of intelligence, that is, which achieve the most intelligence
per unit of computational resources consumed.

### 1.4. Intelligence testing

Having explored what intelligence is, we now turn to how it is measured.
Contrary to popular public opinion, most psychologists believe that standard
psychometric tests of intelligence, such as IQ tests, reliably measure something important in humans (Neisser et al., 1996; Gottfredson, 1997b). In fact,
standard intelligence tests are among the most statistically stable and reliable psychological tests. Furthermore, it is well known that these scores are a
good predictor of various things, such as academic performance. The question
then is not whether these tests are useful or measure something meaningful,
but rather whether what they measure is indeed “intelligence”. Some experts
believe that they do, while others think that they only succeed in measuring
certain aspects of, or types of, intelligence.

There are many properties that a good test of intelligence should have. One
important property is that the test should be repeatable, in the sense that it
consistently returns about the same score for a given individual. For example,
the test subject should not be able to significantly improve their performance
if tested again a short time later. Statistical variability can also be a problem
in short tests. Longer tests help in this regard, however they are naturally
more costly to administer.

1. Nature and Measurement of Intelligence

Another important reliability factor is the bias that might be introduced by
the individual administering the test. Purely written tests avoid this problem
as there is minimal interaction between the tested individual and the tester.
However, this lack of interaction also has disadvantages as it may mean that
other sources of bias, such as cultural differences, language problems or even
something as simple as poor eyesight, might not be properly identified. Thus,
even with a written test the individual being tested should first be examined
by an expert in order to ensure that the test is appropriate.

Cultural bias in particular is a difficult problem, and tests should be designed to minimise this problem where possible, or at least detect potential
bias problems when they occur. One way to do this is to test each ability in
multiple ways, for example both verbally and visually. While language is an
obvious potential source of cultural bias, more subtle forms of bias are difficult to detect and remedy. For example, different cultures emphasise different
cognitive abilities and thus it is difficult, perhaps impossible, to compare intelligence scores in a way that is truly objective. Indeed, this choice of emphasis
is a key issue for any intelligence test, it depends on the perspective taken on
what intelligence is.

An intelligence test should be valid in the sense that it appears to be testing
what it claims it is testing for. One way to check this is to show that the test
produces results consistent with other manifestations of intelligence. A test
should also have predictive power, for example the ability to predict future
academic performance, or performance in other cognitively demanding tasks.
This ensures that what is being measured is somehow meaningful, beyond just
the ability to answer the questions in the test. Standard intelligence tests are
thoroughly tested for years on the above criteria, and many others, before they
are ready for wide spread use.

Finally, when testing large numbers of individuals, for example when testing
army recruits, the cost of administering the test becomes important. In these
cases less accurate but more economical test procedures may be used, such
as purely written tests without any direct interaction between the individuals
being tested and a psychologist.

Standard intelligence tests, such as those described in the next section, are
all examples of “static tests”. By this we mean that they test an individual’s
knowledge and ability to solve one-off problems. They do not directly measure
the ability to learn and adapt over time. If an individual was good at learning
and adapting then we might expect this to be reflected in their total knowledge
and thus be picked up in a static test. However, it could be that an individual
has a great capacity to learn, but that this is not reflected in their knowledge
due to limited education. In which case, if we consider the capacity to learn
and adapt to be a defining characteristic of intelligence, rather than the sum
of knowledge, then to class an individual as unintelligent due to limited access
to education would be a mistake.

What is needed is a more direct test of an individual’s ability to learn and
adapt: a so called “dynamic test”(Sternberg and Grigorenko, 2002) (for re- lated work see also Johnson-Laird and Wason, 1977). In a dynamic test the
individual interacts over a period of time with the tester, who now becomes a
kind of teacher. The tester’s task is to present the test subject with a series
of problems. After each attempt at solving a problem, the tester provides
feedback to the individual who then has to adapt their behaviour accordingly
in order to solve the next problem.

Although dynamic tests could in theory be very powerful, they are not yet
well established due to a number of difficulties. One of the drawbacks is that
they require a much greater degree of interaction between the test subject and
the tester. This makes dynamic testing more costly to perform and increases
the danger of tester bias.

### 1.5. Human intelligence tests

The first modern style intelligence test was developed by the French psychologist Alfred Binet in 1905. Binet believed that intelligence was best studied
by looking at relatively complex mental tasks, unlike earlier tests developed
by Francis Galton which focused on reaction times, auditory discrimination
ability, physical coordination and so on. Binet’s test consisted of 30 short
tasks related to everyday problems such as: naming parts of the body, comparing lengths and weights, counting coins, remembering digits and definitions
of words. For each task category there were a number of problems of increasing difficulty. The child’s results were obtained by normalising their raw score
against peers of the same age. Initially his test was designed to measure
the mental performance of children with learning problems (Binet and Simon,
1905). Later versions were also developed for normal children (Binet, 1911). It
was found that Binet’s test results were a good predictor of children’s academic
performance.

Lewis Terman of Stanford University developed a version of Binet’s test in
English. As the age norms for French children did not correspond well with
American children, he revised Binet’s test in various ways, in particular he
increased the upper age limit. This resulted in the now famous Stanford-Binet
test (Terman and Merrill, 1950). This test formed the basis of a number of
other intelligence tests, such as the Army Alpha and Army Beta tests which
were used to classify recruits. Since its development, the Stanford-Binet has
been periodically revised, with updated versions being widely used today.

David Wechsler believed that the original Binet tests were too focused on
verbal skills and thus disadvantaged certain otherwise intelligent individuals,
for example the deaf or people who did not speak the test language as a
first language. To address this problem, he proposed that tests should contain a combination of both verbal and nonverbal problems. He also believed
that in addition to an overall IQ score, a profile should be produced showing the performance of the individual in the various areas tested. Borrowing
significantly from the Stanford-Binet, the US army Alpha test, and others, he developed a range of tests targeting specific age groups from preschoolers up to adults (Wechsler, 1958). Due in part to problems with revisions of
the Stanford-Binet test in the 1960’s and 1970’s, Wechsler’s tests became the
standard. They continue to be well respected and widely used.

Modern versions of the Wechsler and the Stanford-Binet have a similar basic
structure (Kaufman, 2000). Both test the individual in a number of verbal
and non-verbal ways. In the case of a Stanford-Binet the test is broken up
into five key areas: fluid reasoning, knowledge, quantitative reasoning, visualspatial processing, and working memory. In the case of the Wechsler Adult
Intelligence Scale (WAIS-III), the verbal tests include areas such as knowledge,
basic arithmetic, comprehension, vocabulary, and short term memory. Nonverbal tests include picture completion, spatial perception, problem solving,
symbol search and object assembly.

As part of an effort to make intelligence tests more culture neutral John
Raven developed the progressive matrices test (Raven, 2000). In this test each
problem consists of a short sequence of basic shapes. For example, a circle
in a box, then a circle with a cross in the middle followed by a circle with
a triangle inside. The test subject then has to select from a second list the
image that best continues the pattern. Simple problems have simple patterns,
while difficult problems have more subtle and complex patterns. In each case,
the simplest pattern that can explain the observed sequence is the one that
correctly predicts its continuation. Thus, not only is the ability to recognise
patterns tested, but also the ability to evaluate the complexity of different
explanations and then correctly apply the philosophical principle of Occam’s
razor (see Section 2.1). This will play a key role for us in later chapters.

Today several different versions of the Raven test exist designed for different age groups and ability levels. As the tests depend strongly on the ability
to identify abstract patterns, rather than knowledge, they are considered to
be some of the most “g-loaded” intelligence tests available (see Section 1.1).
The Raven tests remain in common use today, particularly when it is thought
that culture or language bias could be an issue. The universality of abstract
sequence prediction tests makes them potentially useful in the context of machine intelligence, indeed we will see that some tests of machine intelligence
take this approach.

The intelligence quotient, or IQ, was originally introduced by Stern (1912).
It was computed by taking the age of a child as estimated by their performance
in an intelligence test, and then dividing this by their true biological age and
multiplying by 100. Thus a 10 year old child whose mental performance was
equal to that of a normal 12 year old, had an IQ of 120. As the concept of
mental age has now been discredited, and was never applicable to adults anyway, modern IQ scores are simply normalised to a Gaussian distribution with
a mean of 100. The standard deviation used varies: in the United States 15 is
commonly used, while in Europe 25 is common. For children the normalising
Gaussian is based on peers of the same age.

Whatever normalising distribution is used, by definition an individual’s IQ
is always an indication of their cognitive performance relative to some larger
group. Clearly this would be problematic in the context of machines where
the performance of some machines could be many orders of magnitude greater
than others. Furthermore, the distribution of machine performance would be
continually changing due to advancing technology. Thus, for machine intelligence, an absolute measure is more meaningful than a traditional IQ type of
measure.

For an overview of the history of intelligence testing and the structure of
modern tests, see (Kaufman, 2000).

### 1.6. Animal intelligence tests

Testing the intelligence of animals is of particular interest to us as it moves
beyond strictly human focused concepts of intelligence and testing methods.
Difficult problems in human intelligence testing, such as bias due to language
differences or physical handicap, become even more difficult if we try to compare animals with different perceptual and cognitive capacities. Even within
a single species measurement is difficult as it is not always obvious how to
conduct the tests, or even what should be tested for. Furthermore, as humans
devise the tests, there is a persistent danger that the tests may be biased in
terms of our sensory, motor, and motivational systems (Macphail, 1985). For
example, it is known that rats can learn some types of relationships much more
easily through smell rather than other senses (Slotnick and Katz, 1974). Furthermore, while an IQ test for children might in some sense be validated by its
ability to predict future academic or other success, it is not always clear how
to validate an intelligence test for animals: if survival or the total number of
offspring was a measure of success, then bacteria would be the most intelligent
life on earth!

As is often the case when we try to generalise concepts, abstraction is necessary. When attempting to measure the intelligence of lower animals it is necessary to focus on simple things like short and long term memory, the forming
of associations, the ability to generalise simple patterns and make predictions,
simple counting and basic communication. It is only with relatively intelligent
social animals, such as birds and apes, that more sophisticated properties such
as deception, imitation and the ability to recognise oneself are relevant. For
simpler animals, the focus is more on the animal’s essential information processing capacity. For example, the work on measuring the capacity of ants to
remember patterns (Reznikova and Ryabko, 1986).

One interesting difficulty when testing animal intelligence is that we are
unable to directly explain to the animal what its goal is. Instead, we have to
guide the animal towards a problem by carefully rewarding selected behaviours
with something like food. In general, when testing machine intelligence we
face a similar problem in that we cannot assume that a machine will have a sufficient level of language comprehension to be able to understand commands.
A simple solution is to use basic “rewards” to guide behaviour, as we do with
animals. Although this approach is extremely general, one difficulty is that
solving the task, and simply learning what the task is, become confounded
and thus the results need to be interpreted carefully (Zentall, 1997).

For good overviews of animal intelligence research see (Zentall, 2000), (Herman and Pack, 1994) or (Reznikova, 2007).

### 1.7. Machine intelligence tests

This section surveys proposed tests of machine intelligence. Given that the
measurement of machine intelligence is fundamental to the field of artificial
intelligence, it is remarkable that few researchers are aware of research in this
area beyond the Turing test and some of its variants. Indeed, to the best of
our knowledge the survey presented in this section (derived from Legg and
Hutter, 2007b) is the only general survey of tests of machine intelligence that
has been published!

Turing test and derivatives. The classic approach to determining whether
a machine is intelligent is the so called Turing test (Turing, 1950) which has
been extensively debated over the last 50 years (Saygin et al., 2000). Turing
realised how difficult it would be to directly define intelligence and thus attempted to side step the issue by setting up his now famous imitation game:
if human judges cannot effectively discriminate between a computer and a human through teletyped conversation then we must conclude that the computer
is intelligent.

Though simple and clever, the test has attracted much criticism. Block
and Searle argue that passing the test is not sufficient to establish intelligence
(Block, 1981; Searle, 1980; Eisner, 1991). Essentially they both argue that a
machine could appear to be intelligent without having any “real intelligence”,
perhaps by using a very large table of answers to questions. While such a
machine would be impossible in practice, due to the vast size of the table
required, it is not logically impossible. Thus, an unintelligent machine could,
at least in theory, consistently pass the Turing test. Some consider this to
bring the validity of the test into question.

In response to these challenges, even more demanding versions of the Turing
test have been proposed such as the total Turing test in which the machine
must respond to all forms of input that a human could, rather than just
teletyped text (Harnad, 1989). For example, the machine should have sensorimotor capabilities. Going further, the truly total Turing test demands the
performance of not just one machine, but of the whole “race” of machines
over an extended period of time (Schweizer, 1998). Another extension is the
inverted Turing test in which the machine takes the place of a judge and must
be able to distinguish between humans and machines (Watt, 1996). Dowe argues that the Turing test should be extended by ensuring that the agent
has a compressed representation of the domain area, thus ruling out look-up
table counter arguments (Dowe and Hajek, 1998). Of course these attacks on
the Turing test can be applied to any test of intelligence that considers only a
system’s external behaviour, that is, most intelligence tests.

A more common criticism is that passing the Turing test is not necessary
to establish intelligence. Usually this argument is based on the fact that the
test requires the machine to have a highly detailed model of human knowledge
and patterns of thought, making it a test of humanness rather than intelligence (French, 1990; Ford and Hayes, 1998). Indeed, even small things like
pretending to be unable to perform complex arithmetic quickly and faking
human typing errors become important, something which clearly goes against
the purpose of the test.

The Turing test has other problems as well. Current AI systems are a long
way from being able to pass an unrestricted Turing test. From a practical
point of view this means that the full Turing test is unable to offer much guidance to our work. Indeed, even though the Turing test is the most famous test
of machine intelligence, almost no current research in artificial intelligence is
specifically directed towards passing it. Simply restricting the domain of conversation in the Turing test to make the test easier, as is done in the Loebner
competition (Loebner, 1990), is not sufficient. With restricted conversation
possibilities the most successful Loebner entrants are even more focused on faking human fallibility, rather than anything resembling intelligence (Hutchens,
1996). Finally, the Turing test returns different results depending on who the
human judges are. Its unreliability has in some cases lead to clearly unintelligent machines being classified as human, and at least one instance of a human
actually failing a Turing test. When queried about the latter, one of the judges
explained that “no human being would have that amount of knowledge about
Shakespeare”(Shieber, 1994).

Compression tests. Mahoney has proposed a particularly simple solution to
the binary pass or fail problem with the Turing test: replace the Turing test
with a text compression test (Mahoney, 1999). In essence this is somewhat
similar to a “Cloze test” where an individual’s comprehension and knowledge
in a domain is estimated by having them guess missing words from a passage
of text.

While simple text compression can be performed with symbol frequencies,
the resulting compression is relatively poor. By using more complex models
that capture higher level features such as aspects of grammar, the best compressors are able to compress text to about 1.5 bits per character for English.
However humans, which can also make use of general world knowledge, the
logical structure of the argument etc., are able to reduce this down to about
1 bit per character. Thus the compression statistic provides an easily com-

1. Nature and Measurement of Intelligence

puted measure of how complete a machine’s models of language, reasoning and
domain knowledge are, relative to a human.

To see the connection to the Turing test, consider a compression test based
on a very large corpus of dialogue. If a compressor could perform extremely
well on such a test, this is mathematically equivalent to being able to determine
which sentences are probable at a give point in a dialogue, and which are
not (for the equivalence of compression and prediction see Bell et al., 1990).
Thus, as failing a Turing test occurs when a machine (or person!) generates a
sentence which would be improbable for a human, extremely good performance
on dialogue compression implies the ability to pass a Turing test.

A recent development in this area is the Hutter Prize (Hutter, 2006). In
this test the corpus is a 100 MB extract from Wikipedia. The idea is that
this should represent a reasonable sample of world knowledge and thus any
compressor that can perform very well on this test must have a good model of
not just English, but also world knowledge in general.

One criticism of compression tests is that it is not clear whether a powerful
compressor would easily translate into a general purpose artificial intelligence.
Also, while a young child has a significant amount of elementary knowledge
about how to interact with the world, this knowledge would be of little use
when trying to compress an encyclopedia full of abstract “adult knowledge”
about the world.

Linguistic complexity. A more linguistic approach is taken by the HAL
project at the company Artificial Intelligence NV (Treister-Goren and
Hutchens, 2001). They propose to measure a system’s level of conversational
ability by using techniques developed to measure the linguistic ability of children. These methods examine things such as vocabulary size, length of utterances, response types, syntactic complexity and so on. This would allow
systems to be “. . . assigned an age or a maturity level beside their binary Turing test assessment of ‘intelligent’ or ‘not intelligent’ ”(Treister-Goren et al.,
2000). As they consider communication to be the basis of intelligence, and the
Turing test to be a valid test of machine intelligence, in their view the best
way to develop intelligence is to retrace the way in which human linguistic
development occurs. Although they do not explicitly refer to their linguistic
measure as a test of intelligence, because it measures progress towards what
they consider to be a valid intelligence test, it acts as one.

Multiple cognitive abilities. A broader developmental approach is being
taken by IBM’s Joshua Blue project (Alvarado et al., 2002). In this project
they measure the performance of their system by considering a broad range
of linguistic, social, association and learning tests. Their goal is to first pass
what they call a toddler Turing test, that is, to develop an AI system that can
pass as a young child in a similar set up to the Turing test.

Another company pursuing a similar developmental approach based on measuring system performance through a broad range of cognitive tests is the a2i2
project at Adaptive AI (Voss, 2005). Rather than toddler level intelligence,
their current goal is to work toward a level of cognitive performance similar to that of a small mammal. The idea being that even a small mammal
has many of the key cognitive abilities required for human level intelligence
working together in an integrated way.

Competitive games. The Turing Ratio method of Masum et al. has more
emphasis on tasks and games rather than cognitive tests. Similar to our own
definition, they propose that “. . . doing well at a broad range of tasks is an empirical definition of ‘intelligence’.”(Masum et al., 2002) To quantify this they
seek to identify tasks that measure important abilities, admit a series of strategies that are qualitatively different, and are reproducible and relevant over an
extended period of time. They suggest a system of measuring performance
through pairwise comparisons between AI systems that is similar to that used
to rate players in the international chess rating system. The key difficulty
however, which the authors acknowledge is an open challenge, is to work out
what these tasks should be, and to quantify just how broad, important and
relevant each is. In our view these are some of the most central problems that
must be solved when attempting to construct an intelligence test. Thus we
consider this approach to be incomplete in its current state.

Collection of psychometric tests. An approach called Psychometric AI tries
to address the problem of what to test for in a pragmatic way. In the view
of Bringsjord and Schimanski, “Some agent is intelligent if and only if it excels at all established, validated tests of [human] intelligence.”(Bringsjord and
Schimanski, 2003) They later broaden this to also include “tests of artistic and
literary creativity, mechanical ability, and so on.” With this as their goal, their
research is focused on building robots that can perform well on standard psychometric tests designed for humans, such as the Wechsler Adult Intelligence
Scale and Raven Progressive Matrices (see Section 1.5).

As effective as these tests are for humans, we believe that they are unlikely
to be adequate for measuring machine intelligence. For a start they are highly
anthropocentric. Another problem is that they embody basic assumptions
about the test subject that are likely to be violated by computers. For example,
consider the fundamental assumption that the test subject is not simply a
collection of specialised algorithms designed only for answering common IQ
test questions. While this is obviously true of a human, or even an ape,
it may not be true of a computer. The computer could be nothing more
than a collection of specific algorithms designed to identify patterns in shapes,
predict number sequences, write poems on a given subject or solve verbal
analogy problems — all things that AI researchers have worked on. Such a
machine might be able to obtain a respectable IQ score (Sanghi and Dowe,

1. Nature and Measurement of Intelligence

2003), even though outside of these specific test problems it would be next
to useless. If we try to correct for these limitations by expanding beyond
standard tests, as Bringsjord and Schimanski seem to suggest, this once again
opens up the difficulty of exactly what, and what not, to test for. Thus
we consider Psychometric AI, at least as it is currently formulated, to only
partially address this central question.

C-Test. One perspective among psychologists is that intelligence is “the ability to deal with complexity”(Gottfredson, 1997b). Thus, in a test of intelligence, the most difficult questions are the ones that are the most complex
because these will, by definition, require the most intelligence to solve. It follows then that if we could formally define and measure the complexity of test
problems using complexity theory we could construct a formal test of intelligence. The possibility of doing this was perhaps first suggested by Chaitin
(1982). While this path requires numerous difficulties to be dealt with, we
believe that it is the most natural and offers many advantages: it is formally
motivated and precisely defined, and potentially could be used to measure
the performance of both computers and biological systems on the same scale
without the problem of bias towards any particular species or culture.

The C-Test consists of a number of sequence prediction and abduction problems similar to those that appear in many standard IQ tests (Herńandez-
Orallo, 2000b). This test has been successfully applied to humans with interesting results showing a positive correlation between individual’s IQ test scores
and C-Test scores (Herńandez-Orallo and Minaya-Collado, 1998; Herńandez-
Orallo, 2000a). Similar to standard IQ tests, the C-Test always ensures that
each question has an unambiguous answer in the sense that there is always one
hypothesis that is consistent with the observed pattern that has significantly
lower complexity than the alternatives. Other than making the test easier to
score, it has the added advantage of reducing the test’s sensitivity to changes
in the reference machine used to define the complexity measure.

The key difference to sequence problems that appear in standard intelligence tests is that the questions are based on a formally expressed measure of
complexity. As Kolmogorov complexity is not computable (see Section 2.5),
the C-Test instead uses Levin’s related Kt complexity (Levin, 1973). In order
to retain the invariance property of Kolmogorov complexity, Levin complexity
requires the additional assumption that the universal Turing machines are able
to simulate each other in linear time, for example, pointer machines. As far
as we know, this is the only formal definition of intelligence that has so far
produced a usable test of intelligence.

To illustrate the C-Test, below are some example problems taken
from (Herńandez-Orallo and Minaya-Collado, 1998). Beside each question is
its complexity, naturally more complex patterns are also more difficult:

| Complexity | Sequence Prediction Test |  |
| --- | --- | --- |
|  | Sequence | Answer |
| 9 | a, d, g, j, - , ... | m |
| 12 | a, a, z, c, y, e, x, - , ... | g |
| 14 | c, a, b, d, b, c, c, e, c, d, - , ... | d |

| Complexity | Sequence Abduction Test |  |
| --- | --- | --- |
|  | Sequence | Answer |
| 8 | a, - , a, z, a, y, a, ... | a |
| 10 | a, x, - , v, w, t, u, ... | y |
| 13 | a, y, w, - , w, u, w, u, s, ... | y |

$$
a,d,g,j,\_,\ldots
$$

$$
\begin{aligned}{\mathtt{a},\mathtt{a},\mathtt{Z},\mathtt{c},\mathtt{y},\mathtt{e},\mathtt{X},\_,\dots}\\ \end{aligned}
$$

$$
\mathtt{c},\mathtt{a},\mathtt{b},\mathtt{d},\mathtt{b},\mathtt{c},\mathtt{c},\mathtt{e},\mathtt{c},\mathtt{d},\_,\dots
$$

$$
\begin{aligned}{\mathtt{a},\_,\:\mathtt{a},\:\mathtt{Z},\:\mathtt{a},\:\mathtt{y},\:\mathtt{a},\:\dots}\\ \end{aligned}
$$

$$
a,\mathtt{X},\_,\mathtt{V},\mathtt{w},\mathtt{t},\mathtt{u},\dots
$$

$$
\tt{a,y,w,\_,w,u,w,u,S,\ldots}
$$

Our main criticism of the C-Test is that it does not require the agent to be
able to deal with problems that require interacting with an environment. For
example, an agent could have a very high C-Test score due to being a very
good sequence predictor, and yet be unable to deal with more general kinds
of problems. This falls short of what is required by our informal definition of
intelligence, that is, the ability to achieve goals in a wide range of environments.

Smith’s Test. Another complexity based formal definition of intelligence that
appeared recently in an unpublished report is due to Smith (2006). His approach has a number of connections to our work, indeed Smith states that his
work is largely a “. . . rediscovery of recent work by Marcus Hutter”. Perhaps
this is over stating the similarities because while there are some connections,
there are also many important differences.

The basic structure of Smith’s definition is that an agent faces a series of
problems that are generated by an algorithm. In each iteration the agent must
try to produce the correct response to the problem that it has been given. The
problem generator then responds with a score of how good the agent’s answer
was. If the agent so desires it can submit another answer to the same problem.
At some point the agent requests the problem generator to move onto the next
problem and the score that the agent received for its last answer to the current
problem is then added to its cumulative score. Each interaction cycle counts
as one time step and the agent’s intelligence is then its total cumulative score
considered as a function of time. In order to keep things feasible, the problems
must all be in the complexity class P, that is, decision problems which can
be solved by a deterministic Turing machine using a polynomial amount of
computation time.

We have three main criticisms of Smith’s definition. Firstly, while for practical reasons it might make sense to restrict problems to be in P, we do not see
why this practical restriction should be a part of the very definition of intelligence. If some breakthrough meant that agents could solve difficult problems
in not just P but sometimes also in the larger complexity class NP, then surely
these new agents would be more intelligent? We had similar objections to in- formal definitions of machine intelligence that included efficiency requirements
in Section 1.3.

Our second criticism is similar to that of the C-Test. Although there is some
interaction between the agent and the environment, this interaction is rather
limited. The problem-answer format of the test is too limited to fully test an
agent’s capabilities.

The final criticism is that while the definition is somewhat formally defined,
it still leaves open the important question of what exactly the individual tests
should be. Smith suggests that researchers should dream up tests and then
contribute them to some common pool of tests. As such, this intelligence test
is not fully specified.

### 1.8. Conclusion

Although this chapter provides only a short treatment of the complex topic
of intelligence, for a work on artificial intelligence to devote more than a few
paragraphs to the topic is rare. We believe that this is a mistake: if artificial
intelligence research is ever to produce systems with real intelligence, questions
of what intelligence actually means and how to measure it in machines need
to be taken seriously. At present practically nobody is doing this. The reason,
it appears, is that the definition and measurement of intelligence are viewed
as being too difficult. We accept that the topic is difficult, however we do not
accept that the topic is so difficult as to be hopeless and best avoided. As we
have seen in our survey of definitions, there are many commonalities across
the various proposals. This leads to our informal definition of intelligence that
we argue captures the essence of these. Furthermore, although intelligence
tests for humans are widely treated with suspicion by the public, by various
metrics these tests have proven to be very effective and reliable when correctly
applied. This gives us hope that useful tests of machine intelligence may
also be possible. At present only a handful of researchers are working on
these problems, mostly in obscurity. No doubt these fundamental issues will
someday return to the fore when the field is more advanced.

## 2. Universal Artificial Intelligence

Having reviewed what intelligence is and how it is measured, we now turn
our attention to artificial systems that appear to be intelligent, at least in
theory. The problem is that although machines and algorithms are becoming
progressively more powerful, as yet no existing system can be said to have
true intelligence — they simply lack the power, and in particular the breadth,
to really be called intelligent. However, among theoretical models which are
free of practical concerns such as computational resource limitations, intelligent machines can be defined and analysed. In this chapter we introduce a
very powerful theoretical model: Hutter’s universal artificial intelligence agent,
known as AIXI.

A full treatment of this topic requires a significant amount of technical mathematics. The goal here is to explain the foundations of the topic and some of
the key results in the area in a relatively easy to understand fashion. For the
full details, including precise mathematical definitions, proofs and connections
to other fields, see (Hutter, 2005), or for a more condensed presentation (Hutter, 2007b). At this point the reader may wish to browse Appendix A that
describes the mathematical notation and conventions used in this thesis.

### 2.1. Inductive inference

Inductive inference is the process by which one observes the world and then
infers the causes behind what has been observed. This is a key process by which
we try to understand the universe and so naturally examples of it abound.
Indeed much of science can be viewed as a process of inductively inferring
natural causes. For example, at a microscopic level, one may fire sub-atomic
particles into a gas chamber, observe the patterns they trace out, and then
try to infer what the underlying principles are that govern these events. At
a larger scale one may observe that global temperatures are changing along
with other atmospheric conditions, and from this information attempt to infer
what processes may be driving climate change.

Science is not the only domain where inductive inference is important. A
businessman may observe stock prices over time and then attempt to infer a
model of this process in order to predict the market. A parent may return
home from work to discover a chair propped against the refrigerator with the
cookie jar on top a little emptier. Whether we are a detective trying to catch
a thief, a scientist trying to discover a new physical law, or a businessman attempting to understand a recent change in demand, we are all in the process
of collecting information and trying to infer the underlying causes.

Formally we can abstract the inductive inference problem as follows: An
agent has observed some data D := x1,x2,...xt and has a set of hypotheses
H := h1,h2,..., some of which may be good models of the unknown process
µ that is generating D. The task is to decide which hypothesis, or hypotheses
in H are the most likely to accurately reflect µ. For example, x1,x2,... might
be the market value of a stock over time and H might consist of a set of
mathematical models of the stock price. Once we have identified which model
or models are likely to accurately describe the price behaviour, we may want
to use this information to predict future stock prices. Typically this is the
case: Often our goal is not just to understand our observations, but also to
be able to predict future observations. It is in prediction that good models
become truly useful.

$$
\mathcal{D}:=x_{1},x_{2},\ldots x_{t}
$$

$$
\mathcal{H}:=h_{1},h_{2},\ldots,
$$

$$
\mu.
$$

$$
x_{1},x_{2},..
$$

Inductive inference has a long history in philosophy. An early thinker on
the subject was the Greek philosopher Epicurus (342? B.C. – 270 B.C.) who
noted that there typically exist many hypotheses which are consistent with all
of the available data. Logically then, we cannot use the data to rule out any
of these hypotheses; they must all be kept as potential explanations. This is
known as Epicurus’ principle of multiple explanations and is often stated as,

Keep all hypotheses that are consistent with the data.

To illustrate this, consider the cookie jar example again and place yourself
in the position of the parent returning home from work. Having observed the
chair by the refrigerator and missing cookies, one seemingly likely hypothesis
is that your daughter has pushed the chair over to the refrigerator, climbed on
top of it, and then removed some cookies. Another hypothesis is that a hungry
but unusually short thief picked the lock on the back door, saw the cookie jar
and decided to move the chair over to the refrigerator in order to get some
cookies. Although this seems much less likely, you cannot completely rule out
this possibility, or even more elaborate explanations, based solely on the scene
in the kitchen. Philosophically this leaves you in the uncomfortable situation
of having to consider all sorts of strange explanations as being theoretically
possible given the information available. The need to keep these hypotheses
would become clear if you were then to walk into the living room and notice that your new television and other expensive items were also missing —
suddenly the unlikely seems more plausible.

Although we may accept that all hypotheses which are consistent with the
observed facts should be considered at least possible, it is intuitively clear
that some hypotheses are much more likely than others. For example, if you
had previously observed similar techniques being employed by your daughter
to access the cookie jar, but had never been burgled, it would be natural to
consider that the small thief in question was of your own flesh and blood,
rather than a career criminal. However, you are basing this judgement on
your experience prior to returning home. What if you really had very little prior knowledge? How then should you judge the relative likelihood of different
hypotheses?

2.1.1 Example. Consider the following sequence:

**1, 3, 5, 7**

What process do you think is generating these numbers? What do you predict
will come next?

An obvious hypothesis is that these are the positive odd numbers. If this
is true then the next number is going to be 9. A more complex hypotheses
is that the sequence is being generated by the equation 2n − 1 + (n − 1)(n −
2)(n − 3)(n − 4) for n ∈ N. In this case the next number would be 33. Even
when people are aware that this equation generates a sequence consistent with
the digits above, most would not consider it to be very likely at all.

$$
2)(n-3)(n-4)
$$

$$
2n-1+(n-1)(n-
$$

$$
n\in\mathbb{N}
$$

The philosophical principle behind this intuition was first clearly stated by
the English logician and Franciscan friar, William of Ockham (1285 – 1349,
also spelt Occam). He argued that when inferring a cause one should not
include in the explanation anything that is not strictly required to explain the
observations. Or as originally stated, “entia non sunt multiplicanda praeter
necessitatem”, which translates as “entities should not be multiplied beyond
necessity”. A more modern and perhaps clearer expression is,

Among all hypotheses consistent with the observations, the simplest
is the most likely.

This philosophical principle is known as Occam’s razor as it allows one to
cut away unnecessary baggage from explanations. If we consider the number
prediction problem again, it is clear that the principle of Occam’s razor agrees
with our intuition: the simple hypothesis seemed to be more likely, a priori,
than the complex hypothesis. As we saw in the previous chapter, the ability
to apply Occam’s razor is a standard feature of intelligence tests.

### 2.2. Bayes’ rule

Although fundamental, the principles of Epicurus and Occam by themselves
are insufficient to provide us with a mechanism for performing inductive inference. A major step forward in this direction came from the English mathematician and Presbyterian minister, Thomas Bayes (1702 – 1761).

In inductive inference we seek to find the most likely hypothesis, or hypotheses, given the data. Expressed in terms of probability, we seek to find h ∈H
such that the probability of h given D, written P (h|D), is high. From the
definition of conditional probability, P (h|D) := P (h ∩D)/P (D). Rearranging
this we get P (h|D)P (D) = P (h ∩D) = P (D|h)P (h), from which it follows
that,
P (D|h)P (h) P (D|h)P (h)

$$
h\in\mathcal{H}
$$

$$
P(h|\mathcal{D})
$$

$$
P(h|\mathcal{D}):=P(h\cap\mathcal{D})/P(\mathcal{D})
$$

$$
P(h|\mathcal{D})P(\mathcal{D})=P(h\cap\mathcal{D})=P(\mathcal{D}|h)P(h)
$$

$$
P(h|\mathcal{D})=\frac{P(\mathcal{D}|h)P(h)}{P(\mathcal{D})}=\frac{P(\mathcal{D}|h)P(h)}{\sum_{h'\in\mathcal{H}}P(\mathcal{D}|h')P(h')}.
$$

2. Universal Artificial Intelligence

This equation is known as Bayes’ rule. It allows one to compute the probability of different hypotheses h ∈H given the observed data D, and a distribution
P (h) over H. The probability of the observed data, P (D), is known as the
evidence. P (h) is known as the prior distribution as it is the distribution over
the space of hypotheses before taking into account the observed data. The
distribution P (h|D) is known as the posterior distribution as it is the distribution after taking the data into account. Thus in essence, Bayes’ rule takes
some beliefs that we may have about the world and updates these according
to some observed data. In the above formulation we have assumed that the
set of hypotheses H is countable. For uncountable sets the sum is replaced by
an integral.

$$
h\in\mathcal{H}
$$

$$
P(h)
$$

$$
P(\mathcal{D})
$$

$$
P(h)
$$

$$
P(h|D)
$$

Despite its elegance and simplicity, Bayesian inference is controversial. To
this day professional statisticians can be roughly divided into Bayesians who
accept the rule, and classical statisticians who do not. The debate is a subtle
and complex one and there are many different positions within each of the two
camps. At the core of the debate is the very notion of what probability means,
and in particular what the prior probability P (h) means.

How can one talk about the probability of a hypothesis before seeing any
data? Even if this prior probability is meaningful, how can one know what
its value is? We need to take this question seriously because in Bayes’ rule
the choice of prior affects the relative values of P (h|D) for each h, and thus
influences the inference results. Indeed, if Bayesians are free to choose the
prior over H, how can they claim to have objective results?

$$
P(h|\mathcal{D})
$$

Bayesians respond to this in a number of ways. Firstly, they point out that
the problem is generally small, in the sense that with a reasonable prior and
quantity of data, the posterior distribution P (h|D) depends almost entirely
on D rather than the chosen prior P (h). In fact on any sizable data set, not
only does the choice of prior not especially matter, but Bayesian and classical
statistical methods typically produce similar results, as one would expect. It
is only with relatively small data sets or complex models that the choice of
prior becomes an issue.

$$
P(h|\mathcal{D})
$$

If classical statistical methods could avoid the problem of prior bias when
dealing with small data sets then this would be a significant argument in their
favour. However Bayesians argue that all systems of inductive inference that
obey some basic consistency principles define, either explicitly or implicitly,
a prior distribution over hypotheses. Thus, methods from classical statistics
make assumptions that are in effect equivalent to defining a prior. The difference is that in Bayesian statistics these assumptions take the form of an
explicit prior distribution. In other words, it is not that prior bias in Bayesian
statistics is necessarily any better or worse than in classical statistics, it is
simply more transparent.

In practical terms, if priors cannot be avoided, one strategy to reduce the
potential for prior selection abuse is to use well known priors whenever possible. To this end many standard prior distributions have been developed. The
key desirable property is that a prior should not strongly influence the poste- rior distribution and thus unduly affect the inference results. This means that
the prior should express a high degree of impartiality by treating the various
hypotheses somewhat equally. For example, when the set H is finite, an obvious choice is to assign equal prior probability to each hypothesis, formally,
1
P (h) := for all h ∈H. Things become more problematic in infinite hy-
|H|
pothesis spaces as it is then mathematically impossible to assign an equal finite
probability to each of the hypotheses in H, and still have P (H) = 1. Some
Bayesians abandon this condition and use so called improper priors which are
not true probability distributions. For the classical statistician, such a radical
departure from the definition of probability does not really solve the problem of the unknown prior, rather it suggests that something is fundamentally
amiss.

$$
\mathcal{H}
$$

$$
P(h):=\frac{1}{|\mathcal{H}|}
$$

$$
h\in\mathcal{H}
$$

$$
\mathcal{H}.
$$

$$
P(\mathcal{H})=1
$$

Instead of mathematical tricks or other workarounds, what Bayesians would
ideally like is to solve the unknown prior problem once and for all by having
a universal prior distribution. Only then would the Bayesian approach be
truly complete. The principles of Epicurus and Occam provide some hints on
how this might be done. From Epicurus, whenever a hypothesis is consistent
with the data, that is P (D|h) > 0, we should keep this hypothesis by having
P (h|D) > 0. From Bayes’ rule this requires that ∀h ∈H : P (h) > 0. From
Occam we see that P (h) should decrease with the complexity of h, and thus
we need a way to measure the complexity of hypotheses. However before
continuing with this, we first consider the inference problem from another
perspective.

$$
P(\mathcal{D}|h)>0
$$

$$
\forall h\in\mathcal{H}:P(h)>0
$$

$$
P(h|\mathcal{D})>0
$$

$$
P(h)
$$

$$
h,
$$

### 2.3. Binary sequence prediction

An alternate characterisation of inductive inference can be made in terms of
binary sequence prediction. One reason this is useful is that binary sequences
and strings provide a more natural setting in which to deal with issues of computability. The problem can be formulated as follows: There is an unknown
probability distribution µ over the space of binary sequences B∞. From this
distribution a sequence ω is drawn one bit at a time. At time t ∈ N we have
observed the initial string ω1:t:= ω1ω2...ωt, and our task is to predict what
the next bit in the sequence will be, that is, ωt+1. To do this we select a
model, or models, from a set of potential models that explain the observed
sequence so far and that, we hope, will be good at predicting future bits in
the sequence.

$$
\mu
$$

$$
\mathbb{B}^{\infty}
$$

$$
\omega
$$

$$
t\in\mathbb{N}
$$

$$
\omega_{1:t}:=\omega_{1}\omega_{2}\cdots\omega_{t}
$$

$$
\omega_{t+1}
$$

In terms of inductive inference the observed initial binary string ω1:t is the
observed data D, and our set of potential models of the data is the set of
hypotheses H. We would like to find a model ν ∈H, or models, that are as
close as possible to the unknown true model of the data µ, in the sense that ν
will allow us to predict future bits in the sequence as accurately as possible.

$$
\omega_{1:t}
$$

$$
\mathcal{D}.
$$

$$
\nu\in\mathcal{H}
$$

$$
\mathcal{H}.
$$

$$
\mu,
$$

We begin by clarifying what we mean by a probability distribution. In mathematical statistics a probability distribution is known as a probability measure

2. Universal Artificial Intelligence

as it belongs to the class of functions known as measures. Over the space of
binary strings these can be defined as follows:

2.3.1 Definition. A probability measure is a function ν : B∗ → [0, 1] such
that,
ν(ǫ) = 1,

$$
\nu:\mathbb{B}^{*}\to[0,1]
$$

$$
\nu(\underline{\epsilon})=1,
$$

$$
\forall x\in\mathbb{B}^*\quad\nu(\underline{x})=\nu(\underline{x}\underline{0})+\nu(\underline{x}\underline{1}).
$$

In this thesis we will interpret ν(x) to mean the probability that a binary
sequence sampled according to the distribution ν begins with the string x ∈ B∗.
As all strings and sequences begin with the null string ǫ, by definition, the first
condition above simply says that the ν probability that a sequence belongs to
the set of all sequences is 1. The second condition says that the ν probability
that a sequence begins with string x0, plus the ν probability that it begins with
x1, is equal to the ν probability that it begins with x. This makes sense given
that all sequences that begin with x must have either a 0 or a 1 as their next
bit and so we would expect the probabilities of these sets of sequences to add
up. This style of notation for measures will be convenient for our purposes,
however it is somewhat unusual. To see how it relates to conventional measure
theory see Appendix A.

$$
\nu(\underline{{x}})
$$

$$
x\in\mathbb{B}^*
$$

Sequence prediction forms a large part of this thesis and thus we will often
be interested in what comes next in a sequence given an initial string. More
precisely, if a sequence ω has been sampled from the distribution µ, and ω
begins with the string y ∈ B∗, what is the probability that the next bits from
ω will be the string x ∈ B∗? For this will we adopt the following notation for
the conditional probability, µ(yx) := µ(yx)/µ(y). The benefit of this notation
will become apparent later when we need to deal with complex interaction
sequences. Not only does it preserve the order in which the sequence occurs,
it also allows for more compact expressions when we need to condition on only
certain parts of a sequence.

$$
\omega
$$

$$
\mu,
$$

$$
\omega
$$

$$
y\in\mathbb{B}^*
$$

$$
x\in\mathbb{B}^*?
$$

$$
\mu(y\underline{x}):=\mu(\underline{y x})/\mu(\underline{y})
$$

As noted earlier in this section, sequence prediction can be viewed as an
inductive inference problem. Thus, we can use Bayes’ rule to estimate how
likely some model ν ∈H is given the observed sequence ω1:t:

$$
\nu\in\mathcal{H}
$$

$$
\omega_{1:t}:
$$

$$
P\left(\nu\middle|\omega_{1:t}\right)=\frac{P\left(\underline{\omega}_{1:t}\middle|\nu\right)P\left(\nu\right)}{P\left(\underline{\omega}_{1:t}\right)}=\frac{\nu\left(\underline{\omega}_{1:t}\right)P\left(\nu\right)}{\sum_{\varrho\in\mathcal{H}}\varrho\left(\underline{\omega}_{1:t}\right)P\left(\varrho\right)}.
$$

2.3.2 Example. Consider the problem of inferring whether a coin is a normal fair coin based on a sample of coin flips. To simplify things, assume
that the coin is either heads on both sides, tails on both sides, or a normal fair coin. Further assume that t = 4 and we have the observed data
D = head, head, head, head. In terms of binary sequence prediction, the outcome of t coin tosses can be expressed as a string ω1:t ∈ Bt, with each tail being
represented as a 0 bit, and each head as a 1 bit. Thus we have ω1:4 = 1111.

$$
\omega_{1:t}\in\mathbb{B}^t
$$

$$
\omega_{1:4}=1111
$$

Let H be the set of models consisting of the distributions νp(ω1:t) := pr(1 −
{} ∑t
p)t−r, where p ∈ 0, 1/2, 1 and r :=i=1ωi is the number of observed heads.

$$
\nu_{p}(\underline{\omega}_{1:t}):=p^{r}(1-
$$

$$
p)^{t-r}
$$

$$
p\in\left\{0,\frac{1}{2},1\right\}
$$

$$
r:=\sum_{i=1}^{t}\omega_{i}
$$

As there are just three models in H, assume a uniform prior, that is, ∀p ∈
{}
0, 21, 1 let P (νp) := 1/3. Now from Bayes’ rule,

$$
\mathcal{H},
$$

$$
\forall p\in
$$

$$
\left\{0,\frac{1}{2},1\right\}
$$

$$
P(\nu_{p}):=\frac{1}{3}
$$

$$
P(\nu_{\frac{1}{2}}|\omega_{1:4}=1111)\;=\;\frac{\frac{1}{3}\left(\frac{1}{2}\right)^{4}\left(1-\frac{1}{2}\right)^{0}}{\frac{1}{3}\left[0^{4}(1-0)^{0}+\left(\frac{1}{2}\right)^{4}\left(1-\frac{1}{2}\right)^{0}+1^{4}(1-1)^{0}\right]}\;=\;\frac{1}{17}.
$$

Similarly, P (ν0|ω1:4 = 1111) = 0 and P (ν1|ω1:4 = 1111) = 16/17. Thus the results
clearly point towards the coin being double headed, as we would expect having
just observed four heads in a row.

$$
P(\nu_{0}|\omega_{1:4}=1111)=0
$$

$$
P(\nu_{1}|\omega_{1:4}=1111)=\frac{16}{17}
$$

More complex examples could involve data collected from medical measurements, music or weather satellite images. Good models would then have to
describe biological processes, music styles, or the dynamics of weather systems
respectively. In each case the binary string representing D could be simply the
string of bits as they would appear in a computer file. However, finding a good
prior over such spaces is not trivial. Furthermore, actually computing Bayes’
rule and finding the most likely models, as we did in the example above, can
become very computationally difficult and may need to be approximated. In
any case, Bayes’ rule at least tells us how to solve the induction problem in
theory, so long as we have a prior distribution.

Rather than just estimating which model or models are the most likely, we
may be interested in actually predicting the sequence. One possibility is to
calculate the probability that the next bit is a 1 based on the most likely model.
The full Bayesian approach, however, is to consider each possible model ν ∈H
and weight the prediction made by each according to how confident we are
about each model, i.e. P (ν|ω1:t). This gives us the mixture model predictor,

$$
\nu\in\mathcal{H}
$$

$$
P(\nu|\omega_{1:t})
$$

$$
\begin{align*}P(\omega_{1:t}\underline{1})\quad=&\quad\sum_{\nu\in\mathcal{H}}P(\nu|\omega_{1:t})\nu(\omega_{1:t}\underline{1})\\=&\quad\sum_{\nu\in\mathcal{H}}\frac{\nu(\underline{\omega}_{1:t})P(\nu)}{P(\underline{\omega}_{1:t})}\frac{\nu(\underline{\omega}_{1:t}\underline{1})}{\nu(\underline{\omega}_{1:t})}=\frac{P(\underline{\omega}_{1:t}\underline{1})}{P(\underline{\omega}_{1:t})}.\end{align*}
$$

As we can see, the Bayes mixture predictor reduces to the definition of conditional probability. This has removed the prior over H, and in its place we now
have the related prior over D, in this setting the space of binary sequences.
The fact that we can use one prior to define the other means that the two
unknown priors are in fact two perspectives on the same fundamental problem
of specifying our prior knowledge.

$$
\mathcal{H},
$$

2.3.3 Example. Continuing Example 2.3.2, we can compute the prior distribution over sequences from the prior distribution over H,
∑

$$
\mathcal{H}
$$

$$
\begin{array}{r c l}{P(\underline{{\omega}}_{1:t})}&{=}&{\sum_{\nu\in\mathcal{H}}\nu(\underline{{\omega}}_{1:t})P(\nu)}\\ {}&{=}&{\frac{1}{3}\left[0^{t}(1-0)^{t-r}+\left(\frac{1}{2}\right)^{t}\left(1-\frac{1}{2}\right)^{t-r}+1^{t}(1-1)^{t-r}\right]}\\ {}&{=}&{\frac{1}{3}\left[\left(\frac{1}{2}\right)^{2t-r}+\delta_{t r}\right].}\\ \end{array}
$$

∑t
where r :=i=1ωi is the number of observed heads, and the Kronecker delta
symbol δab is defined to be 1 if a = b, and 0 otherwise. Thus, given that
ω1:4 = 1111, according to the mixture model the probability that the next bit
is a 1 is,
[(1)2(5)−5]
1()5

$$
r:=\sum_{i=1}^{t}\omega_{i}
$$

$$
\delta_{ab}
$$

$$
a=b
$$

$$
\omega_{1:4}=1111
$$

$$
P(1111\underline{1})=\frac{\frac{1}{3}\left[\left(\frac{1}{2}\right)^{2(5)-5}+\delta_{5,5}\right]}{\frac{1}{3}\left[\left(\frac{1}{2}\right)^{2(4)-4}+\delta_{4,4}\right]}=\frac{\left(\frac{1}{2}\right)^{5}+1}{\left(\frac{1}{2}\right)^{4}+1}=\frac{33}{34}.
$$

### 2.4. Solomonoff’s prior and Kolmogorov complexity

In the 1960’s Ray J. Solomonoff (1926–) investigated the problem of inductive
inference from the perspective of binary sequence prediction (Solomonoff 1964;
1978). He was interested in a very general form of the problem, specifically,
learning to predict a binary sequence that has been sampled from an arbitrary
unknown computable distribution. Solomonoff defined his prior distribution
over sequences as follows: The prior probability that a sequence begins with
a string x ∈ B∗ is the probability that a universal Turing machine running
a randomly generated program computes a sequence that begins with x. By
randomly generated, we mean that the bits of the program have a uniform
distribution, for example, they could come from flipping a fair coin. Formally,

$$
x\in\mathbb{B}^*
$$

2.4.1 Definition.
with the string x ∈ B

The Solomonoff prior probability that a sequence begins
∗ is,
∑

$$
x\in\mathbb{B}^*
$$

$$
M(\underline{{x}}):=\sum_{p:\mathcal{U}(p)=x*}2^{-\ell(p)},
$$

where U (p) = x∗ means that the universal Turing machine U computes an
output sequence that begins with x ∈ B∗ when it runs the program p, and ℓ(p)
is the length of p in bits.

$$
\mathcal{U}(p)=x*
$$

$$
x\in\mathbb{B}^*
$$

$$
p,
$$

$$
\ell(p)
$$

Note that the 2−ℓ(p) term in this definition comes from the fact that the
probability of p under a uniform distribution halves for each additional bit.

$$
2^{-\ell(p)}
$$

We will assume that U is a prefix universal Turing machine. This means
that no valid program for U is a prefix of any other. More precisely, if p,q ∈ B∗
are valid programs on U, then there does not exist a string x ∈ B∗ such that
p = qx. Prefix universal Turing machines have technical properties that we
will need and so throughout this thesis we will assume that U is of this type.
Technically, U is actually a type of prefix universal Turing machine known as
a monotone universal Turing machine (see Section 5.1). For the moment we
can safely gloss over these details.

$$
p,q\in\mathbb{B}^{*}
$$

$$
\mathcal{U}.
$$

$$
x\in\mathbb{B}^*
$$

$$
p=qx
$$

2.4.2 Example. Rather than a classic universal Turing machine running a
program specified by a binary string on an input tape, it is often more intuitive
to think in terms of a program written in a high level programing language
that is being executed on a real computer. Indeed, if a computer had infinite
memory and never broke down it would be technically equivalent to a universal
Turing machine. Consider a short program in C that prints a binary sequence
of all 1’s:

$$
\mathrm{main}()\{\mathrm{while}(1)\mathrm{print}(1);\}
$$

As far as C programs go, this is nearly as simple as they get. This is not
surprising given that the output is also very simple. If we want a program that
generates a more complex sequence, such as an infinite sequence of successive
digits of the mathematical constant π = 3.141592..., such a program would
be at least ten times as long. It follows then that the probability of randomly
generating a program that outputs all 1’s is far higher than the probability of
randomly generating a program that computes π. Thus, Solomonoff’s prior
assigns much higher probability to the sequences of all 1’s than to the sequence
for π. More complex sequences would require still larger programs and thus
have even lower prior probability.

$$
\pi=3.141592\ldots
$$

$$
\pi
$$

$$
\pi
$$

$$
\diamondsuit
$$

Although Solomonoff’s definition requires nothing more than random bits
being fed into a universal Turing machine, we can see that the resulting distribution over sequences neatly formalises Occam’s razor. Specifically, sets
of sequences that have short programs, and are thus in some sense simple,
are given higher prior probability than sets of sequences that have only long
programs.

The idea that the complexity of a sequence is related to the length of the
shortest program that generates the sequence motivates the following definition:

2.4.3 Definition. The Kolmogorov complexity of a sequence ω ∈ B∞ is,

$$
\omega\in\mathbb{B}^{\infty}
$$

$$
K(\omega):=\min_{p\in\mathbb{B}^{*}}\left\{\ell(p):\mathcal{U}(p)=\omega\right\},
$$ where U is a prefix universal Turing machine. If no such p exists, we define
K(ω) = ∞. For a string x ∈ B∗, we define K(x) to be the length of the
shortest program that outputs x and then halts.

$$
K(\omega)=\infty
$$

$$
x\in\mathbb{B}^*
$$

$$
K(x)
$$

Kolmogorov complexity has many powerful theoretical properties and is a
central ingredient in the theory of universal artificial intelligence. Its most
important property is that the complexity it assigns to strings and sequences
does not depend too much on the choice of the universal Turing machine U.
This comes from the fact that universal Turing machines are universal in the
sense that they are able to simulate each other with a constant number of
additional input bits. Thus, if we change U above to some other universal
Turing machine U′, the minimal value of ℓ(p) and thus K(x), can only change
by a bounded number of bits. This bound depends on U and U′, but not on
x.

$$
\ell(p)
$$

$$
\mathcal{U}'
$$

$$
K(x)
$$

$$
\mathcal{U}'
$$

$$
x.
$$

The biggest problem with Kolmogorov complexity is that the value of K
is not in general computable. It can only be approximated from above. The
reason for this is that in general we cannot find the shortest program to compute a string x on U due to the halting problem. Intuitively, there might exist
a very short program p∗ such that U (p∗) = x, however we do not know this
because p∗ takes such a long time to run. Nevertheless, in theoretical applications the simplicity and theoretical power of Kolmogorov complexity often
outweighs this computability problem. In practical applications Kolmogorov
complexity is approximated, for example by using a compression algorithm to
estimate the length of the shortest program (Cilibrasi and Vit´anyi, 2005).

$$
\mathcal{U}
$$

$$
p^{*}
$$

$$
\mathcal{U}(p^*)=x
$$

$$
p^{*}
$$

### 2.5. Solomonoff-Levin prior

Besides the prior described in the previous section, Solomonoff also suggested
to define a universal prior by taking a mixture of distributions (Solomonoff,
1964). In the 1970’s this alternate approach was generalised and further developed (Zvonkin and Levin, 1970; Levin, 1974). As Leonid Levin (1948–)
played an important role in this, here we will refer to this as the Solomonoff-
Levin prior. It is closely related to the universal prior in the previous section:
they lie within a multiplicative constant of each other and share key technical
properties.

Although taking mixtures is perhaps less intuitive, it has the advantage
of making important theoretical properties of the prior more transparent. It
also gives an explicit prior over both the hypothesis space and the space of
sequences. The topic is quite technical, however it is worth spending some
time on as it lies at the heart of universal artificial intelligence.

The hypotheses we have been working with up to now have all been probability measures. These can be generalised as follows:

2.5.1 Definition. A semi-measure is a function ν : B∗ → [0, 1] such that,

$$
\nu:\mathbb{B}^{*}\to[0,1]
$$

$$
\nu(\underline{{\epsilon}})\leq1,
$$

$$
\forall x\in\mathbb{B}^*\quad\nu(\underline{x})\geq\nu(\underline{x}\underline{0})+\nu(\underline{x}\underline{1}).
$$

Intuitively one may think of a semi-measure that is not a probability measure
as being a kind of defective probability measure whose probabilities do not
quite add up as they should. This defect can be fixed in the sense that a
semi-measure can be built up to be a probability measure by appropriately
normalising things.

Intuitively, a function is enumerable if it can be progressively approximated
from below. More formally, f : X → R is enumerable if there exists a computable function g : X × N → Q such that ∀x ∈ X, ∀i ∈ N : gi+1(x) ≥ gi(x)
and ∀x ∈ X : limi→∞gi(x) = f (x). Enumerability is weaker than computability because for any x ∈ X we only ever have the lower bound gi(x) on the
value of f (x). Thus we can never know for sure how far our bound is from the
true value of f (x), that is, we do not know how large f (x) − gi(x) might be.

$$
f:X\to\mathbb{R}
$$

$$
g:X\times\mathbb{N}\to\mathbb{Q}
$$

$$
\forall x\in X,\forall i\in\mathbb{N}:g_{i+1}(x)\geq g_i(x)
$$

$$
\forall x\in X:\lim_{i\to\infty}g_i(x)=f(x)
$$

$$
x\in X
$$

$$
g_{i}(x)
$$

$$
f(x)
$$

$$
f(x)-g_i(x)
$$

If a similar condition holds, but with the approximation function converging
to f from above rather than below, we say that f is coenumerable. One
example of such a function is the Kolmogorov complexity function K in the
previous section. If a function is both enumerable and coenumerable, then
we have both upper and lower bounds and thus can compute the value of f
to any required accuracy. In this case we simply say that f is a real valued
computable function. Clearly then, the enumerable functions are a superset of
the computable functions.

Our task is to construct a prior distribution over the enumerable semimeasures. To do this we need to formalise Occam’s razor, and for that we
need to define a way to measure the complexity of enumerable semi-measures.
Solomonoff measured the complexity of sequences according to the length of
their programs, here we can do something similar.

By definition, all enumerable functions can be approximated from below
by a computable function. Thus, it is not too hard to prove that the set of
enumerable functions can be indexed by a Turing machine, and that this can be
further restricted to just the set of enumerable semi-measures. More precisely,
there exists a Turing machine T that for any enumerable semi-measure µ there
exists an index i ∈ N such that ∀x ∈ B∗: µ(x) = νi(x) := limk→∞T (i,k,x)
with T increasing in k. In effect, the index i is a description of µ in that once
we know i we can approximate the value of µ from below for any x by using
the Turing machine T. As k increases, these approximations increase towards
the true value of µ(x). For details on how all this is done see Section 4.5
of (Li and Vit´anyi, 1997) or (Legg, 1997). The main thing we will need is the
computable enumeration of enumerable semi-measures itself, which we will
denote by Me:= ν1,ν2,ν3,.... As all probability measures are semi-measures
by definition, and all computable functions are enumerable, it follows that
the set of enumerable semi-measures is a superset of the set of computable
probability measures. We write Mc to denote an enumeration of just the
computable measures.

$$
\mu
$$

$$
i\in\mathbb{N}
$$

$$
\forall x\in\mathbb{B}^{*}:\mu(\underline{{x}})=\nu_{i}(\underline{{x}}):=\lim_{k\to\infty}T(i,k,x)
$$

$$
\mu
$$

$$
\mu
$$

$$
T
$$

$$
\mu(x)
$$

$$
\mathcal{M}_{e}:=\nu_{1},\nu_{2},\nu_{3},\cdots\mathrm{As}
$$

$$
\mathcal{M}_{c}
$$

2. Universal Artificial Intelligence

Note the two uses of the word “enumerable” above. When we say that a set
can be enumerated, what we mean is that there exists a way to step though all
the elements in this set. When we say that an individual function is enumerable, such as a semi-measure, what we mean is that it can be approximated
from below by a series of computable functions. Some authors avoid this
dual usage by referring to enumerable functions as lower semi-computable. In
this terminology, what Me provides is a computable enumeration of the lower
semi-computable semi-measures. In any case, it is still a mouthful!

$$
\mathcal{M}_{e}
$$

We can now return to the question of how to measure the complexity of
an enumerable semi-measure. As noted above, for νi ∈Me the index i is in
effect a description of νi. At this point, it might seem that the natural thing
to do is to take the value of an enumerable semi-measure’s index to be its
complexity. The problem, however, is that some extremely large index values,
such as 21000, contain a lot less information than far smaller index values which
are not as easily described: for example, an index whose binary representation
is a string of 100 random bits. The solution is that we must measure not
the value, but the information content of the index in order to measure the
complexity of the enumerable semi-measure it describes. We do this by taking
the Kolmogorov complexity of the index. That is, we define the complexity
of an enumerable semi-measure to be the length of the shortest program that
computes its index. Formally,

$$
\nu_{i}\in\mathcal{M}_{e}
$$

$$
\nu_{i}
$$

$$
2^{\overset{\cdot}{1000}}
$$

2.5.2 Definition.

The Kolmogorov complexity of µ ∈Me is,

$$
\mu\in\mathcal{M}_e
$$

$$
K(\mu):=\min_{p\in\mathbb{B}^{*}}\left\{\ell(p):\mathcal{U}(p)=i\right\},
$$

where µ is the ith element in the recursive enumeration of all enumerable
semi-measures Me, and U is a prefix universal Turing machine.

$$
\mu
$$

$$
i^{th}
$$

$$
\mathcal{M}_{e}
$$

$$
\mathcal{U}
$$

In essence this is just an extension of the Kolmogorov complexity function for
strings and sequences (Definition 2.4.3), to enumerable semi-measures. Indeed,
all the key theoretical properties of the complexity function remain the same.
We can again see echos of Solomonoff’s prior for sequences in that enumerable
semi-measures that can be described by short programs are considered to be
simple, while ones that require long programs are complex.

Having defined a suitable complexity measure for enumerable semimeasures, we can now construct a prior distribution over Me in a way that
is similar to what Solomonoff did. As each enumerable semi-measure µ has
some shortest program p ∈ B∗ that specifies its index, we can set the prior
probability of µ to be the probability of randomly generating p by flipping a
coin to get each bit. Formally:

$$
\mathcal{M}_{e}
$$

$$
p\in\mathbb{B}^*
$$

$$
\mu
$$

$$
\mu
$$

2.5.3 Definition. The algorithmic prior probability of µ ∈Me is,

$$
\mu\in\mathcal{M}_e
$$

$$
P_{\mathcal{M}_{e}}(\mu):=2^{-K(\mu)}.
$$

As K is coenumerable, from the definition above we can see that PMe is
enumerable. Thus, this distribution can only be approximated from below.

$$
P_{\mathcal{M}_{e}}
$$

With K as the definition of hypothesis complexity, PMe clearly respects
Occam’s razor as each hypothesis µ ∈Me is assigned a prior probability that
is a decreasing function of its complexity. Furthermore, every enumerable
semi-measure has some shortest program that specifies its index and so ∀µ ∈
Me: K(µ) > 0 and thus ∀µ ∈Me: PMe(µ) > 0. It follows then that for an
induction system based on Bayes’ rule and the prior PMe, the value of P (ν|D)
will be non-zero whenever D is consistent with ν, that is, P (D|ν) > 0. Such
systems will not discard hypotheses that are consistent with the data and thus
respect Epicurus’ principle of multiple explanations.

$$
P_{\mathcal{M}_{e}}
$$

$$
\mu\in\mathcal{M}_e
$$

$$
\forall\mu\in\mathcal{M}_e:P_{\mathcal{M}_e}(\mu)>0
$$

$$
\forall\mu\in
$$

$$
\mathcal{M}_{e}:K(\mu)>0
$$

$$
P_{\mathcal{M}_e}
$$

$$
P(\nu|\mathcal{D})
$$

$$
\nu.
$$

$$
P(\mathcal{D}|\nu)>0
$$

With a prior over our hypothesis space Me, we can now take a mixture to
define a prior over the space of sequences, just as we did in Example 2.3.3:

$$
\mathcal{M}_{e}
$$

2.5.4 Definition. The Solomonoff-Levin prior probability of a binary sequence beginning with the string x ∈ B∗ is,
∑

$$
x\in\mathbb{B}^*
$$

$$
\xi(\underline{x}):=\sum_{\nu\in\mathcal{M}_{e}}P_{\mathcal{M}_{e}}(\nu)\nu(\underline{x}).
$$

Clearly this distribution respects Occam’s razor as sets of sequences which
have high probability under some simple distribution ν, will also have high
probability under ξ, and vice versa.

$$
\nu,
$$

$$
\xi,
$$

It is easy to see that the presence of just one semi-measure in the above
mixture is sufficient to cause ξ to also be a semi-measure, rather than a probability measure. Furthermore, it can be proven that ξ is enumerable but not
computable. Thus, we have that ξ ∈Me. The fact that ξ is not a probability measure is not too much of a problem because, as mentioned earlier, it is
possible to normalise a semi-measure to convert it into a probability measure.
In situations where we need a universal probability measure the normalised
version of ξ is useful. Its main drawback is that it is no longer enumerable,
and thus no longer a member of Me. In most theoretical applications it is
usual to work with the plain ξ as defined above.

$$
\xi
$$

$$
\xi
$$

$$
\xi\in\mathcal{M}_e
$$

$$
\xi
$$

$$
\xi
$$

$$
\mathcal{M}_{e}
$$

$$
\xi
$$

A fundamental result is that the two priors are strongly related:

2.5.5 Theorem. The Solomonoff prior M and Solomonoff-Levin prior ξ lie
within a multiplicative constant of each other. That is, M = ξ.×

$$
\xi
$$

$$
M\stackrel{\times}{=}\xi.
$$

Due to this relation, in many theoretical applications the differences between
the two priors are unimportant. Indeed, it is their shared property of dominance that is the key to their theoretical power:

2.5.6 Definition. For some set of semi-measures M, we say that ν ∈M is
dominant if ∀̺ ∈M there exists a constant c̺> 0 such that ∀x : c̺ν(x) ≥
̺(x). Or more compactly, ∀̺ ∈M : ν ≥ ̺.×

$$
\mathcal{M}
$$

$$
\nu\in\mathcal{M}
$$

$$
\forall\varrho\in\mathcal{M}
$$

$$
c_{\varrho}>0
$$

$$
c_{\varrho}\nu(\underline{x})\geq
$$

$$
\varrho(\underline{x})
$$

$$
\forall\varrho\in\mathcal{M}:\nu\stackrel{\times}{\geq}\varrho.
$$

2. Universal Artificial Intelligence

It is easy to see that ξ is dominant over the set of enumerable semi-measures
from its construction: for x ∈ B∗ we have ξ(x) ≥ PMe(µ) µ(x) = 2−K(µ)µ(x).
×
It follows then that ∀µ ∈Me, ∀x ∈ B∗: 2K(µ)ξ(x) ≥ µ(x). As M = ξ, we see
that M is also dominant. We call distributions that are dominant over large
spaces, such as Me, universal priors. This is due to their extreme generality
and performance as prior distributions, something that we will explore in the
next two sections: firstly in the context of Bayesian theory in general, and
then in the context of sequence prediction.

$$
\xi
$$

$$
x\in\mathbb{B}^*
$$

$$
\xi(\underline{x})\geq P_{\mathcal{M}_{e}}(\mu)\mu(\underline{x})=2^{-K(\mu)}\mu(\underline{x})
$$

$$
\forall\mu\in\mathcal{M}_{e},\forall x\in\mathbb{B}^{*}:2^{K(\mu)}\xi(\underline{{x}})\geq\mu(\underline{{x}})
$$

$$
M\stackrel{\times}{=}\xi,
$$

$$
\mathcal{M}_{e}
$$

### 2.6. Universal inference

As we saw in Section 2.2, Bayes’ rule partially solves the induction problem
by providing an equation for updating beliefs. This is only a partial solution
because it leaves open two important issues: how do we choose the class of
hypotheses H, and what prior distribution PH should we use over this class?
Various principles and methods have been proposed to solve these problems,
however they tend to run into trouble, especially for large H. In this section
we will look at how taking the universal prior PMe over the hypothesis space
Me theoretically solves these problems.

$$
\mathcal{H}
$$

$$
P_{\mathcal{H}}
$$

$$
P_{\mathcal{M}_{e}}
$$

$$
\mathcal{M}_{e}
$$

When approaching an inductive inference problem from a Bayesian perspective, the first step is to define H. The most obvious consideration is that H
should be large enough to contain the correct hypothesis, or at least a sufficiently close one. Being forced to expand our initial H due to new evidence
is problematic as both the redistribution of the prior probabilities, and the
way in which H is extended, can bias the induction process. In order to avoid
these problems, we should make sure that H is large enough to contain a good
hypothesis to start with. One solution is to simply choose H to be very large,
as we did in the previous section where we set H = Me. As this contains all
computable stochastic hypotheses, a larger hypothesis space should never be
required.

$$
\mathcal{H}.
$$

$$
\mathcal{H}=\mathcal{M}_e
$$

Having selected H, the next problem is to define a good prior distribution
over this space. Essentially, a prior distribution PH over a space of hypotheses
H is an expression of how likely we think different hypotheses are before taking
the data into account. If this prior knowledge is easily quantifiable we can use
it to construct a prior. In the case of PMe this simply means taking the
conditional form of the Kolmogorov complexity function and conditioning on
this prior information.

$$
\mathcal{H}.
$$

$$
P_{\mathcal{H}}
$$

$$
\mathcal{H}
$$

$$
P_{\mathcal{M}_{e}}
$$

More often, however, we either have insufficient prior information to construct a prior, or we simply wish the data to ‘speak for itself’. The latter
case is important when we want to present our findings to others who may
not share our prior beliefs. The standard solution is to select a prior that
is in some sense neutral about the relative likelihood of different hypotheses.
This is known as the indifference principle. It is what we applied in the coin estimation problem in Example 2.3.2 when we set P (νp) := |H|−1 = 31. That
is, we simply assumed that a priori all hypotheses were equally likely.

$$
P(\nu_{p}):=|\mathcal{H}|^{-1}=\frac{1}{3}
$$

The indifference principle works well for small discrete H, however if we
extend the concept to even small continuous parametrised classes by defining
a probability density function in terms of the volume of H, problems start to
arise. Consider again the coin problem, however this time allow the bias of
the coin to be θ ∈ [0, 1]. By the indifference principle the prior is the uniform
probability density P (νθ) = 1. Now consider what happens if we look at this
coin estimation problem in a different way, where the parameter of interest
√
is actually θ′:= θ. Obviously, if we take a uniform prior over θ′ this is
not equivalent to taking a uniform prior over θ. In other words, the way in
which we view a problem, and thus the way in which we parametrise it, affects
the prior probabilities assigned by a ‘uniform prior’. Obviously this is not as
neutral and objective as we would like.

$$
\mathcal{H}
$$

$$
\theta\in[0,1]
$$

$$
P(\nu_{\theta})=1
$$

$$
\theta^{\prime}\;:=\;\sqrt{\theta}.
$$

$$
\theta.
$$

$$
\theta^{\prime}
$$

Consider how the algorithmic prior probability PMe behaves under a simple
reparametrisation. Let H := {νθ ∈ Mc: θ ∈ Θ} be a set of probability
measures indexed by a parameter θ ∈ Θ, and define θ′:= f (θ) where f is
a computable bijection. It is an elementary fact of Kolmogorov complexity
+ +
theory that K(f (θ)) < K(θ) + K(f), and similarly K(f−1(θ′)) < K(θ′) +
+
K(f), from which it follows that K(θ) = K(θ′). With a straight forward
extension, the same argument can be applied to the Kolmogorov complexity
+
of the indexed measures, resulting in K(νθ) = K(νθ′). From Definition 2.5.3
we then see that,

$$
P_{\mathcal{M}_e}
$$

$$
\mathcal{H}:=\left\{\nu_{\theta}\in\mathcal{M}_{c}:\theta\in\Theta\right\}
$$

$$
\theta\in\Theta
$$

$$
\theta^{\prime}\;:=\;f(\theta)
$$

$$
K(f(\theta))\stackrel{+}{<}K(\theta)+K(f)
$$

$$
K(f^{-1}(\theta'))\stackrel{+}{<}K(\theta')+
K(f)
$$

$$
K(\theta)\stackrel{+}{=}K(\theta')
$$

$$
K(\nu_{\theta})\triangleq K(\nu_{\theta^{\prime}})
$$

$$
P_{\mathcal{M}_{e}}(\nu_{\theta})\;:=\;2^{-K(\nu_{\theta})}\;\triangleq\;2^{-K(\nu_{\theta^{\prime}})}\;=:\;P_{\mathcal{M}_{e}}(\nu_{\theta^{\prime}}).
$$

That is, for any bijective reparametrisation f the algorithmic prior probability
assigned to parametrised hypotheses is invariant up to a multiplicative constant. If f is simple this constant is small and thus quickly washes out in the
posterior distribution, leaving the inference results essentially unaffected by
the change.

A more difficult version of the above problem occurs when the transformation is non-bijective. For example, define the new parameter θ′:= (θ − 21)2.
1 3
Now θ = and θ = both correspond to the same value of θ′. Unlike
4 4
in the bijective case, non-bijective transformations also cause problems for
finite discrete hypothesis spaces. For example, we might have three hypotheses, H3 := {heads biased, tails biased, fair}. Alternatively, we could
regroup to have just two hypotheses, H2 := {biased, fair}. Both H3 and
H2 cover the full range of possibilities for the coin. However, a uniform prior
1
over H3 assigns a prior probability of to the coin being fair, while a uniform
3
1
prior over H2 assigns a prior probability of just to the same thing.
2

$$
\theta':=(\theta-\frac{1}{2})^2
$$

$$
\theta\;=\;\frac{1}{4}
$$

$$
\theta\;=\;\frac{3}{4}
$$

$$
\theta^{\prime}
$$

$$
\mathcal{H}_{3}:=
\mathcal{H}_{3}
$$

$$
\mathcal{H}_{2}:=\{\mathrm{biased},\mathrm{fair}\}
$$

$$
\mathcal{H}_{2}
$$

$$
\mathcal{H}_{3}
$$

$$
\frac{1}{3}
$$

$$
\mathcal{H}_{2}
$$

$$
\frac{1}{2}
$$

The standard Bayesian approach is to try to find a symmetry group for the
problem and a prior that is invariant under group transformations. However,
in some cases there may be no obvious symmetry, and even if there is the
resulting prior may be improper, meaning that the area under the distribution

2. Universal Artificial Intelligence

is no longer 1. Invariance under group transformations is a highly desirable but
difficult property to attain. Remarkably, under simple group transformations
PMe can be proven to be invariant, again up to a small multiplicative constant.
For a proof of this, as well as further powerful properties of the universial prior
distribution, see the paper that this section is based on (Hutter, 2007a).

$$
P_{\mathcal{M}_e}
$$

### 2.7. Solomonoff induction

Given a prior distribution ξ over B∞, it is straightforward to predict the continuation of a binary sequence using the same approach as we used in Section 2.3.
∞
Given prior distribution ξ and the observed string ω1:t ∈ B from a sequence
ω ∈ B∞ that has been sampled from an unknown computable distribution
µ ∈Mc, our estimate of the probability that the next bit will be 0 is,

$$
\xi over\mathbb{B}^{\infty}
$$

$$
\xi
$$

$$
\omega_{1:t}\in\mathbb{B}^{\infty}
$$

$$
\omega\in\mathbb{B}^{\infty}
$$

$$
\mu\in\mathcal{M}_{c},
$$

$$
\xi(\omega_{1:t}\underline{0})=\frac{\xi(\underline{\omega}_{1:t}\underline{0})}{\xi(\underline{\omega}_{1:t})}.
$$

Is this predictor based on ξ any good? By definition, the best possible
predictor would be based on the unknown true distribution µ that ω has been
sampled from. That is, the true probability that the next bit is a 0 given an
observed initial string ω1:t is,

$$
\xi
$$

$$
\mu
$$

$$
\omega
$$

$$
\omega_{1:t}
$$

$$
\mu(\omega_{1:t}\underline{0})=\frac{\mu(\underline{\omega}_{1:t}\underline{0})}{\mu(\underline{\omega}_{1:t})}.
$$

As this predictor is optimal by construction, it can be used to quantify the
relative performance of the predictor based on ξ. For example, consider the
expected squared error in the estimated probability that the tth bit will be a
0: ∑
()2
S = µ(x) ξ(x0) − µ(x0).

$$
\xi
$$

$$
t^{th}
$$

$$
0;
$$

$$
S_{t}=\sum_{\underline{x}\in\mathbb{B}^{t-1}}\mu(\underline{x})\big(\xi(x\underline{0})-\mu(x\underline{0})\big)^{2}.
$$

If ξ is a good predictor, then its predictions should be close to those made by
the optimal predictor µ, and thus St will be small.

$$
\mathrm {I f} \xi
$$

$$
\mu,
$$

$$
S_{t}
$$

Solomonoff (1978) was able to prove the following remarkable convergence
theorem:

2.7.1 Theorem. For any computable probability measure µ ∈Mc,

$$
\mu\in\mathcal{M}_{c}
$$

$$
\sum_{t=1}^{\infty}S_{t}\;\leq\;\frac{\ln2}{2}\thinspace K(\mu).
$$

That is, the total of all the prediction errors over the length of the infinite sequence ω is bounded by a constant. This implies rapid convergence for
any unknown hypothesis that can be described by a computable distribution
(for a precise analysis see Hutter, 2007a). This set includes all computable

$$
\omega
$$ hypotheses over binary strings, which is essentially the set of all well defined
hypotheses. If it were not for the fact that the universal prior ξ is not computable, Solomonoff induction would be the ultimate all purpose universal
predictor.

$$
\xi
$$

Although we will not present Solomonoff’s proof, the following highlights
the key step required to obtaining the convergence result. For any probability
measure µ the following relation can be proven,

$$
\mu
$$

$$
\sum_{t=1}^{n}S_{t}\;\leq\;\frac{1}{2}\sum_{\underline{{x}}\in\mathbb{B}^{n}}\mu(\underline{{x}})\ln\frac{\mu(\underline{{x}})}{\xi(\underline{{x}})}.
$$

This in fact holds for any semi-measure ξ, thus no special properties of the
universal distribution have been used up to this point in the proof. Now, by the
universal dominance property of ξ, we know that ∀x ∈ B∗: ξ(x)≥2−K(µ)µ(x).
Substituting this into the above equation,

$$
\xi,
$$

$$
\xi
$$

$$
\forall x\in\mathbb{B}^*:\xi(\underline{x})\geq2^{-K(\mu)}\mu(\underline{x})
$$

$$
\sum_{t=1}^{n}S_{t}\;\leq\;\frac{1}{2}\sum_{\underline{{x}}\in\mathbb{B}^{n}}\mu(\underline{{x}})\ln\frac{\mu(\underline{{x}})}{2^{-K(\mu)}\mu(\underline{{x}})}\;=\;\frac{\ln2}{2}K(\mu)\sum_{\underline{{x}}\in\mathbb{B}^{n}}\mu(\underline{{x}})\;=\;\frac{\ln2}{2}K(\mu).
$$

As this holds for all n ∈ N, the result follows. It is this application of
dominance to obtain powerful convergence results that lies at the heart of
Solomonoff induction, and indeed universal artificial intelligence in general.

$$
n\in\mathbb{N}
$$

Although Solomonoff induction is not computable and is thus impractical,
it nevertheless has many connections to practical principles and methods that
are used for inductive inference. Clearly, if we define a computable prior rather
than ξ, we recover normal Bayesian inference. If we define our prior to be uniform, for example by assuming that all models have the same complexity, then
the result is maximum a posteriori (MAP) estimation, which in turn is related
to maximum likelihood (ML) estimation. Relations can also be established to
Minimum Message Length (MML), Minimum Description Length (MDL), and
Maximum entropy (ME) based prediction (see Chapter 5 of Li and Vit´anyi,
1997). Thus, although Solomonoff induction does not yield a prediction algorithm itself, it does provide a theoretical framework that can be used to
understand various practical inductive inference methods. It is a kind of ideal,
but unattainable, model of optimal inductive inference.

$$
\xi,
$$

### 2.8. Agent-environment model

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

### 2.9. Optimal informed agents

In the agent-environment model, the agent’s goal is to receive as much reward
as possible. Unfortunately, this is not sufficiently precise as there may be many
possible reward sequences in a given environment and it is not clear which is
preferred.

2.9.1 Example. Consider the following two agents: Agent π1 immediately
finds a way to get a reward of 0.5 and does so in every cycle. Thus, after

$$
\pi^{1}
$$

2. Universal Artificial Intelligence

100 cycles it has received a total reward of 50. Agent π2, however, spends the
first 90 cycles trying to find the best possible way to receive reward in each
cycle. During this time it gets an average reward of 0.1 in each cycle. At
cycle 90 it works out the optimal behaviour and then receives a reward of 1
in every cycle thereafter. Thus, after 100 cycles it has received a total reward
of 90 × 0.1 + 10 = 19. In terms of the total reward received after 100 cycles,
π1 is superior to π2. However, after 1,000 cycles this has reversed as π1 has a
total reward of 500, while π2 has a total reward of 919.

$$
\pi^{2}
$$

$$
90\times0.1+10=19
$$

$$
\pi^{2}
$$

$$
\pi^{1}
$$

$$
\pi^{1}
$$

$$
\pi^{2}
$$

$$
\diamondsuit
$$

Which of these two agents is the better one? The answer depends on how
we value reward at different points in the future. In some situations we may
want our agent to perform well quickly, and thus place more value on short
term rewards. In others, we might only care that it eventually reaches a level
of performance that is as high as possible, and thus place relatively high value
on rewards far into the future. Before we can define an optimal agent, we first
need to formally express our temporal preferences.

A general approach is to weight, or discount, each reward in a way that
depends on which cycle it occurs in. Let γ1,γ2,... be the discounts we apply
∑∞
to the reward in each successive cycle, where ∀i : γi ≥ 0, andi=1γi <
∞ in order to avoid infinite weighted sums. Now define the expected future
discounted reward for agent π interacting with environment µ given interaction
history ax<tto be,

$$
\gamma_{1},\gamma_{2},\ldots
$$

$$
\forall i\::\:\gamma_{i}\:\geq\:0
$$

$$
\sum_ {i = 1} ^ {\infty} \gamma_ {i} <
$$

$$
\infty
$$

$$
\pi
$$

$$
\mu
$$

$$
ax_{<t}
$$

$$
\begin{array}{r c l}{V_{\gamma}^{\pi\mu}(\mathit{ax}_{<t})}&{:=}&{\mathbf{E}\Bigg(\sum_{i=t}^{\infty}\gamma_{i}r_{i}\:\Big|\:\mathit{ax}_{<t}\Bigg)}\\ {}&{=}&{\operatorname*{l i m}_{m\to\infty}\sum_{\mathit{ax}_{t:m}}\left(\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}\right)\:_{\mu}^{\pi}(\mathit{ax}_{<t}\mathit{ax}_{t:m}).}\\ \end{array}
$$

As the sum is monotonically increasing in m, and finitely upper bounded, the
limit always exists. For t = 1 we drop the interaction history from the notation
and simply write Vγπµ.

$$
m,
$$

$$
t=1
$$

$$
V_{\gamma}^{\pi\mu}
$$

One of the most common ways to set the discount parameters is to decrease
them geometrically into the future. That is, set ∀i : γi:= αi for some discount
rate α ∈ (0, 1). By increasing α towards 1 we weight long term rewards more
heavily, conversely by reducing it we weight them less so. Thus, the parameter
α controls how short term greedy, or long term farsighted, the agent should
be.

$$
\forall i:\gamma_{i}:=\alpha^{i}
$$

$$
\alpha\in(0,1)
$$

$$
\alpha
$$

2.9.2 Example. Consider again the two agents from Example 2.9.1. As the
rewards are deterministic for π1 we can drop the expectation,

$$
\pi^{1}
$$

$$
V_{\gamma}^{\pi^{1}\mu}=\sum_{i=1}^{\infty}\alpha^{i}0.5=0.5A,
$$

α
where A := is from the standard formulae for geometric series. On the
1−α
other hand for agent π2,

$$
A:=\frac{\alpha}{1-\alpha}
$$

$$
V_{\gamma}^{\pi^{2}\mu}=\sum_{i=1}^{90}\alpha^{i}0.1+\sum_{i=91}^{\infty}\alpha^{i}=0.1A(1-\alpha^{90})+A\alpha^{90}.
$$

Equating the two and then solving, we find that
discounted reward than π1 when α >

π2 has higher expected future
√
90
4/9 ≈ 0.991.

$$
\pi^{2}
$$

$$
\pi^{1}
$$

$$
\alpha>\sqrt[90]{4/9}\approx0.991
$$

$$
\diamond
$$

A major advantage of geometric discounting is that it is mathematically
convenient to work with. Indeed, it is what we will use in Chapter 6 for our
reinforcement learning algorithm. In the present context, however, we want
to keep the development fairly general and thus we will leave the structure
of γ unspecified. An even more general approach is to consider the space of
all bounded enumerable discount sequences. We will take this approach when
formally defining intelligence in Chapter 4 as it will allow us to completely
remove γ from the model. Here we will follow the more conventional approach
to AIXI and simply take γ to be a free parameter.

$$
\gamma
$$

$$
\gamma
$$

$$
\gamma
$$

Having formalised the agent’s temporal preference in terms of γ, we can now
define the optimal agent:

$$
\gamma
$$

2.9.3 Definition. The optimal agent for an environment µ and discounting γ is the agent πµ that has maximal expected future discounted reward.
Formally,
πµ:= arg max V.

$$
\mu
$$

$$
\gamma
$$

$$
\pi^{\mu}
$$

$$
\pi^{\mu}:=\arg\max_{\pi}V_{\gamma}^{\pi\mu}.
$$

The superscript µ emphasises the fact that the agent is optimal with respect
to the specific environment µ. This optimality is possible because the agent
was constructed using µ. In a sense the agent knows what its environment
is before it has even interacted with it. This is similar to Section 2.7 where
the optimal sequence predictor was defined using the distribution that was
generating the sequence to be predicted.

$$
\mu
$$

$$
\mu
$$

$$
\mu.
$$

To understand how the optimal agent πµ behaves in each cycle, we first
express the value function in a recursive form for an arbitrary agent π. From
the definition of V,
∑

$$
\pi^{\mu}
$$

$$
\pi
$$

$$
V
$$

$$
\begin{align*}V_{\gamma}^{\pi\mu}(ax_{<t})\;&=\;\lim_{m\to\infty}\sum_{ax_{t:m}}(\gamma_t r_t+\cdots+\gamma_m r_m)\;_{\mu}^{\pi}(ax_{<t}\underline{ax}_{t:m})\\&=\;\sum_{ax_t}\left[\lim_{m\to\infty}\sum_{ax_{t+1:m}}(\gamma_t r_t+\cdots+\gamma_m r_m)\;_{\mu}^{\pi}(ax_{1:t}\underline{ax}_{t+1:m})\right]_{\mu}^{\pi}(ax_{<t}\underline{ax}_t)\\&=\;\sum_{ax_t}\left[\gamma_t r_t+V_{\gamma}^{\pi\mu}(ax_{1:t})\right]_{\mu}^{\pi}(ax_{<t}\underline{ax}_t).\end{align*}
$$

(2.1)

In the first step we broke cycle t off both the sum and πµ. As these do not
involve m, we pushed them outside the square brackets and moved the limit

$$
\pi\cdot
m,
$$

2. Universal Artificial Intelligence

inside. In the second step we broke off the first discounted reward and dropped
the sum for this term as it was redundant. The remaining discounted rewards
are just V with t advanced by one, thus producing the desired recursion in V.

This is essentially a discrete time form of the Bellman equation commonly
used in control theory, finance, reinforcement learning and other fields concerned with optimising dynamic systems (Bellman, 1957; Sutton and Barto,
1998). Usually it is assumed that the environment is Markovian and thus only
a limited history needs to be taken into account. Here, however, we include
the entire interaction history and thus are able to avoid these restrictions on
the environment. Again, this is to keep the model as general as possible.

Consider now how at is chosen by the optimal agent πµ. By definition, the
optimal action is the one that maximises V. Therefore πµ(ax<tat)=1 for
the expected future discounted reward maximising action, and zero otherwise
(ties can be broken arbitrarily).∑Thus, after expanding Equation (2.1) with π
replaced by πµ, we can replaceat and πµ(ax<tat) with simply a maximum
over the possible actions,

$$
a_{t}
$$

$$
\pi^{\mu}
$$

$$
\pi^{\mu}(ax_{<t}\underline{a}_{t})=1
$$

$$
\pi
$$

$$
\pi^{\mu}
$$

$$
\sum_{a_{t}}
$$

$$
\pi^{\mu}(a x_{<t}\underline{{a}}_{t})
$$

$$
\begin{align*}V_{\gamma}^{\pi^{\mu}\mu}(ax_{<t})&=\sum_{a_{t}}\sum_{x_{t}}\Big[\gamma_{t}r_{t}+V_{\gamma}^{\pi^{\mu}\mu}(ax_{1:t})\Big]\pi^{\mu}(ax_{<t}\underline{a_{t}})\mu(ax_{<t}\underline{a_{t}})\\&=\max_{a_{t}}\sum_{x_{t}}\Big[\gamma_{t}r_{t}+V_{\gamma}^{\pi^{\mu}\mu}(ax_{1:t})\Big]\mu(ax_{<t}\underline{a_{t}})\\&=\max_{a_{t}}\sum_{x_{t}}\cdots\max_{a_{m}}\sum_{x_{m}}\Big[\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}+V_{\gamma}^{\pi^{\mu}\mu}(ax_{1:m})\Big]\mu(ax_{<t}\underline{a_{t}}).\end{align*}
$$

In the last step we have simply unfolded the recursion in V for the first m
cycles. As m → ∞ the term Vγπµµ(ax1:m) → 0. Thus, if we take the limit
m →∞ above we can drop V without affecting the result. It follows then that
the action taken by the optimal policy πµ in the tth cycle is,

$$
m\to\infty
$$

$$
V_{\gamma}^{\pi^{\mu}\mu}(a x_{1:m})\rightarrow0
$$

$$
m\to\infty
$$

$$
\pi^{\mu}
$$

$$
t^{th}
$$

$$
a_{t}^{\pi^{\mu}}:=\arg\operatorname*{m a x}_{a_{t}}\operatorname*{l i m}_{m\to\infty}\sum_{x_{t}}\operatorname*{m a x}_{a_{t+1}}\sum_{x_{t+1}}\cdots\operatorname*{m a x}_{a_{m}}\sum_{x_{m}}\left[\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}\right]\mu(a x_{<t}a\underline{{x}}_{t:m}).
$$

If there is more than one maximising action in cycle t, we simply select one of
these in an arbitrary way.

Intuitively, in the above equation we can see that the optimal agent takes
the distribution µ, and in effect does a brute force search through all possible
futures looking for the action in the current cycle that maximises the expected
future discounted reward. The agent knows that the environment will always
respond according to the distribution µ, thus in each cycle it takes the expectation by summing over all the possible observations x and weighting these by
their probability according to µ. Furthermore, as the agent always follows an
optimal strategy, its own future actions are just a series of value maximising
actions.

$$
\mu,
$$

$$
\mu,
$$

$$
\mu.
$$

### 2.10. Universal AIXI agent

Although the agent πµ performs optimally in environment µ, this does not
meet the requirements for intelligence according to our definition adopted in
Chapter 1. What we require is a general agent that works well in many different
environments. Such an agent must learn about its environment by interacting
with it, and then modify its behaviour accordingly in order to optimise performance. Only then will the agent have the kind of adaptability to different
environments that we require of an intelligent agent.

$$
\pi^{\mu}
$$

$$
\mu,
$$

$$
\mathrm{it}.
$$

This problem with the optimal agent πµ is similar to the one we encountered
in Section 2.7. There the optimal sequence predictor was based on the distribution µ that was actually generating the sequence. Of course, for inductive
inference µ is unknown and must be inferred by observing the sequence. Thus,
basing a predictor on µ might be “optimal” in terms of prediction performance,
but it is in some sense cheating. Moreover, it is certainly not general as the
predictor is designed for just one environment.

$$
\pi^{\mu}
$$

$$
\mu
$$

$$
\mu
$$

$$
\mu
$$

Solomonoff’s solution was to replace the unknown µ in the optimal predictor with a universal prior distribution, such as ξ. This produced an extremely powerful universal predictor that rapidly converged to optimal predictions whenever the distribution µ was computable (Theorem 2.7.1). In this
way Solomonoff solved, at least in theory, the problem of predicting sequences
from unknown distributions. Hutter’s innovation was to do essentially the
same trick for active agents: he took the optimal active agent πµ, described in
the previous section, and replaced the unknown µ with a generalised universal
prior distribution ξ. This produced πξ, also known as AIXI, which will be
described in this section.

$$
\mu
$$

$$
\xi.
$$

$$
\mu
$$

$$
\pi^{\mu}
$$

$$
\mu
$$

$$
\xi
$$

$$
\pi^{\xi}
$$

In order to construct πξ, the first thing to do is to generalise ξ in Definition 2.5.4 from sequences to active environments. As we saw earlier, an active
environment µ is an enumerable semi-measure conditioned, in chronological
order, on a sequence of actions from an agent. The presence of these actions
causes no problems, indeed the development of a universal distribution over active environments is virtually identical to what we did for sequence prediction
in Section 2.5.

$$
\pi^{\xi}
$$

$$
\xi
$$

$$
\mu
$$

It can be shown that the space of all enumerable chronological semi-measures
can be effectively enumerated. Let E := {µ1,µ2,...} be such an enumeration.
Define the Kolmogorov complexity of one of these environments to be the
length of the shortest program that computes the environment’s index: just
as we did for distributions over sequences in Definition 2.5.2. This gives us the
universal prior probability of a chronological environment ν ∈ E,

$$
E:=\left\{\mu_{1},\mu_{2},\ldots\right\}
$$

$$
\nu\in E
$$

$$
P_{E}(\nu):=2^{-K(\nu)}.
$$

From this prior over environments we can construct a prior over the agent’s
observations in a given interaction history by taking a mixture over the envi-

2. Universal Artificial Intelligence

$$
\xi(a\underline{{x}}_{1:n}):=\sum_{\nu\in E}2^{-K(\nu)}\nu(a\underline{{x}}_{1:n}).
$$

ronments,

It is easy to see that ξ is enumerable because 2−K(ν) is enumerable, as is
each ν in the sum. Furthermore, this sum of chronological semi-measures is
itself a chronological semi-measure. Thus, we see that ξ ∈ E. As was the
case for sequences, the dominance property for ξ can easily be seen by taking
one element from the sum corresponding to the semi-measure to be dominated.
Note that we are reusing the symbol ξ. Whether we are talking about ξ defined
over sequences, or over chronological environments, will always be clear from
the context.

$$
2^{-K(\nu)}
$$

$$
\xi
$$

$$
\xi
$$

$$
\xi\in E
$$

$$
\xi_{1}
$$

$$
\xi
$$

To construct the AIXI agent πξ
∑ ∑

, simply take π
∑ [

µ and replace µ with ξ,

$$
\pi^{\xi}
$$

$$
\pi^{\mu}
$$

$$
a_{t}^{\pi^{\xi}}:=\arg\operatorname*{m a x}_{a_{t}}\operatorname*{l i m}_{m\to\infty}\sum_{x_{t}}\operatorname*{m a x}_{a_{t+1}}\sum_{x_{t+1}}\cdots\operatorname*{m a x}_{a_{m}}\sum_{x_{m}}\left[\gamma_{t}r_{t}+\cdots+\gamma_{m}r_{m}\right]\xi(a x_{<t}a\underline{{x}}_{t:m}).
$$

$$
\mu
$$

$$
\xi
$$

This gives us an agent that does not depend on the unknown µ. Replacing
the true distribution µ in the optimal agent πµ with the universal prior distribution ξ is essentially the same as what we did in Section 2.7 when defining
Solomonoff’s universal predictor. Of course now we are working in the more
general setting of chronological environments rather than just sequences.

$$
\mu.
$$

$$
\mu
$$

$$
\pi^{\mu}
$$

$$
\xi
$$

Given that Solomonoff prediction works so well for sequence prediction, we
might expect the agent πξ defined above to be similarly powerful in chronological environments. To some extent this is the case, however analysing the
performance of universal agents in chronological environments turns out to be
significantly more complex.

$$
\pi^{\xi}
$$

Perhaps the most elementary question concerns whether our generalised ξ
converges to the true environment µ. It turns out that convergence results
can be proven, including a result similar to Solomonoff’s convergence result
generalised to interaction histories. More precisely, it can be proven that the
total µ-expected squared difference between µ and ξ is finite for interaction
histories sampled from πµ interacting with a computable environment µ. Unfortunately, when the interaction history comes from µ interacting with πξ,
rather than πµ, we run into trouble. This problem is well illustrated by the
Heaven and Hell environment from Section 5.3.2 of (Hutter, 2005):

$$
\mu.
$$

$$
\xi
$$

$$
\mu-
$$

$$
\mu
$$

$$
\xi
$$

$$
\pi^{\mu}
$$

$$
\mu.
$$

$$
\pi^{\mu}
$$

$$
\pi^{\xi}
$$

$$
\mu
$$

2.10.1 Example. (Heaven and Hell) Imagine an environment where in
the first cycle the agent is faced with two unmarked doors, one of which must
be opened. One of these doors leads to “heaven” where the agent receives
plentiful rewards, and the other leads to “hell” where the agent never gets any
reward. Once a door is chosen there is no way to go back, the agent is stuck
in either heaven or hell forever.

This is no problem for πµ as it knows µ and so it knows which door to take
to get to heaven. Thus it always achieves maximal future discounted reward.
The agent πξ, on the other hand, must learn through experience. Of course

$$
\pi^{\mu}
$$

$$
\mu
$$

$$
\pi^{\xi}
$$ once it has the necessary experience to make the right choice, it may already
be too late. All πξ can do is to guess which door to take and hope for the best.
Obviously the expected performance of πξ will be far below that of πµ.

$$
\mathrm{All}\pi^{\xi}
$$

$$
\pi^{\xi}
$$

$$
\pi^{\mu}.\qquad\diamondsuit
$$

This example does not expose a design flaw in πξ, in the sense that no
general agent is able to consistently behave optimally in such environments.
For example, consider an environment µ′ with the two doors switched. Agent
πµ would always go to hell in this environment. We could define an agent
πµ′ which would be optimal in µ′, however it would always go to hell in µ.
Clearly, no agent could behave optimally in both environments without being
told what the true environment was in advance. Matching the performance of
optimal agents in each of their respective environments is thus an impossible
task for any one agent. As such, we need to think carefully about what it is
that we want to prove if we are to show that πξ is indeed a very powerful and
general agent.

$$
\pi^{\xi}
$$

$$
\mu^{\prime}
$$

$$
\pi^{\mu}
$$

$$
\mu.
$$

$$
\pi^{\mu^{\prime}}
$$

$$
\mu^{\prime}
$$

$$
\pi^{\xi}
$$

We have already seen in Section 2.7 that the above problem does not occur
in the sequence prediction setting. This is because in sequence prediction an
agent’s predictions do not affect the future observed sequence and thus mistakes have no consequences beyond the current cycle. This allows Solomonoff’s
prediction system to be able to learn to perform optimally across the entire
space of computable sequence prediction problems. Such optimising behaviour
is possible in certain other classes of environments. What this suggests then is
that we should focus on classes of environments, such as sequence prediction,
in which it is at least possible for a general agent to learn to behave optimally.

We begin by generalising the AIXI model to different classes of environments. Let E be a non-strict subset of the enumeration E of all enumerable
chronological semi-measures. Define the mixture distribution over E,
∑

$$
\mathcal{E}
$$

$$
E
$$

$$
\mathcal{E}
$$

$$
\zeta\left(a\underline{x}_{1:n}\right):=\sum_{\nu\in\mathcal{E}}2^{-K(\nu)}\nu\left(a\underline{x}_{1:n}\right).
$$

Now define the agent πζ based on ζ, just as we defined πξ based on ξ. Note that
while πξ is a single agent, the agent πζ depends on which class of environments
E we are considering. If E = E then ζ = ξ and so πζ = πξ. In this sense πζ
generalises πξ.

$$
\pi^{\zeta}
$$

$$
\zeta,
$$

$$
\pi^{\xi}
$$

$$
\xi.
$$

$$
\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
\mathcal{E}
$$

$$
\mathcal{E}=E
$$

$$
\zeta=\xi
$$

$$
\pi^{\zeta}=\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\xi}
$$

Perhaps the most elementary property that an optimal general agent must
have is that there should not exist any other agent that is strictly superior.
More precisely:

2.10.2 Definition. An agent π is Pareto optimal if there is no other agent
ρ such that ∀µ ∈E,

$$
\pi
$$

$$
\forall\mu\in\mathcal{E}
$$

$$
\rho
$$

$$
V_{\gamma}^{\rho\mu}(a x_{<t})\geq V_{\gamma}^{\pi\mu}(a x_{<t})\quad\forall a x_{<t},
$$

with strict inequality for at least one µ.

$$
\mu
$$

2. Universal Artificial Intelligence

$$
\mathcal{E}
$$

Note that Pareto optimality does not rule out the possibility that some other
agent exists which performs better in some environment in E. It simply means
that no other agent exists which is at least as good in all environments in E,
and strictly better in at least one. For the agent πζ the following optimality
result can be proven (Section 5.5 of Hutter, 2005):

$$
\mathcal{E}
$$

$$
\pi^{\zeta}
$$

### 2.10.3 Theorem. For any E⊆ E, the agent πζ is Pareto optimal.

$$
\mathcal{E}\subseteq E
$$

$$
\pi^{\zeta}
$$

As this holds for any E, it also holds for E = E. Thus, the AIXI agent πξ is
a Pareto optimal agent over the space of environments E. Note that for any
space of environments E many Pareto optimal agents may exist.

$$
\mathcal{E}
$$

$$
\mathcal{E}=E
$$

$$
\pi^{\xi}
$$

$$
\mathcal{E}
$$

A stronger result can be proven showing that πζ is also balanced Pareto optimal (Hutter, 2005). Essentially, this means that any increase in performance
in some environment due to switching to another agent, is compensated for by
an equal or greater decrease in performance in some other environment.

$$
\pi^{\zeta}
$$

While these Pareto optimality results are very general, they only succeed
in showing that πζ is superior, or at least equal, to other general agents over
the same class of environments. The result does not rule out the possibility
that all general agents, including πζ, typically perform poorly. What we need
is to show that πζ does indeed learn to perform well in many environments.
The complication, as we saw in Example 2.10.1 above, is that in some types
of environments it is impossible for general agents to perform well. Thus we
somehow need to characterise those types of environments in which it is at
least possible for a general agent to perform well. Furthermore, even when
optimal performance is possible for a general agent, we cannot expect such an
agent to perform optimally immediately. We need a performance measure that
gives the agent time to learn about the structure of µ through interaction. One
way to formalise the concept of optimal performance after a period of learning
is the following:

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

$$
\mu
$$

2.10.4 Definition. An agent π is said to be self-optimising in an environment µ if,
1 1
µ

$$
\pi
$$

$$
\mu
$$

$$
\frac{1}{\Gamma_{t}}\:V_{\gamma}^{\pi\mu}(a x_{<t})\;\to\;\frac{1}{\Gamma_{t}}\:V_{\gamma}^{\pi^{\mu}\mu}(\dot{a}\dot{x}_{<t})
$$

with µ probability 1 as t →∞. Here ax<tis an interaction history sampled
from π interacting with µ, and ȧẋ<tis an interaction history ∑sampled from
∞
πµ interacting with µ. The normalisation factor, defined Γt:=i=tγi, is the
total discount remaining at time t.

$$
\mu
$$

$$
t\to\infty
$$

$$
ax_{<t}
$$

$$
\pi
$$

$$
\mu,
$$

$$
\dot{a}\dot{x}_{<t}
$$

$$
\pi^{\mu}
$$

$$
\Gamma_{t}:=\sum_{i=t}^{\infty}\gamma_{i}
$$

$$
\mu
$$

Essentially this says that with high probability the performance of the agent
π converges to the performance of the optimal agent. The normalisation is
necessary because the un-normalised expected future discounted reward always
converges to zero. Thus without it convergence would trivially hold for any
agent.

$$
\pi
$$

We say that π is self-optimising for the set of environments E if it is selfoptimising for every environment in E. Furthermore, we say that a set of

$$
\pi
$$

$$
\mathcal{E}
$$

$$
\mathcal{E}
$$ environments E admits self-optimising agents if there exists an agent π that
is self-optimising for E. We also extend the result to non-stationary agents by
saying that a series of agents π1,π2,... is self-optimising if the above result
holds with π replaced by πt. That is, in the tth cycle agent πt is applied.

$$
\mathcal{E}
$$

$$
\pi
$$

$$
\mathcal{E}
$$

$$
\pi_{1},\pi_{2},\ldots
$$

$$
\pi
$$

$$
\pi_{t}
$$

$$
t^{th}
$$

$$
\pi_{t}
$$

The following powerful self-optimising result can be proven (Hutter, 2005):

2.10.5 Theorem. If there exists a sequence of self-optimising agents πm for
a class of environments E, then the agent πζ is also self-optimising for E.

$$
\pi_{m}
$$

$$
\pi^{\zeta}
$$

$$
\mathcal{E}
$$

$$
\mathcal{E}
$$

Intuitively, this result says that the performance of πζ will converge to optimal performance in any class of environments where this is possible for a
single agent, even if the agent is non-stationary. This is the minimal requirement possible, in the sense that if no self-optimising agent existed for some
class of environments, then trivially πζ cannot be self-optimising in the class
either.

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

Although this is a strong optimality result, it does have two limitations.
Firstly, while the result shows that πξ converges to optimal performance whenever this is possible in a class of environments, it does not tell us how fast the
convergence is. In Solomonoff’s convergence theorem we saw that the convergence of the universal predictor was extremely rapid. Ideally we would
like a similar result for active environments. Unfortunately, such a result is
impossible in general:

$$
\pi^{\xi}
$$

2.10.6 Example. (Needle in a haystack) Imagine an environment with
N buttons, one of which generates a reward of 1 in every cycle when pressed,
and all the rest produce no reward. The location of the correct button would
take roughly log2 N bits to encode, thus for most values of N we have K(µ) =
O(log2 N). As πξ is not informed prior to the start of the game as to which
button generates reward, the best it can do is to press the buttons one at
a time. Thus the expected number of incorrect choices that πζ will make is
()
O(N) = O 2K(µ).

$$
K(\mu)=
\log_{2}
$$

$$
O(\log_{2}N)
$$

$$
\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
O(N)=O\left(2^{K(\mu)}\right)
$$

$$
\diamond
$$

Compare this to Theorem 2.7.1 for sequence prediction which bounds the
total squared difference in prediction error by O(K(µ)). Here in the active
case the best possible bound for any general agent is exponentially worse at
()
O 2K(µ). This is not a design flaw in πξ as the above limit applies to any general agent. Clearly then, bounds showing rapid convergence are not possible
in general. We can only hope to prove convergence speed bounds for specific
classes of environments. Unfortunately, results in this direction currently exist
only in very simple settings.

$$
O(K(\mu))
$$

$$
O\big(2^{K(\mu)}\big)
$$

$$
\pi^{\xi}
$$

This is a significant weakness in the theory of universal agents. Until further
results are proven it is hard to say just how fast, or slow, convergence to optimal
behaviour is in different classes of environments. As it appears that results in
this direction will be difficult, a more elementary result is to establish which
classes of environments at least admit self-optimising agents, and under what
conditions. Once we have established this, by Theorem 2.10.5 it would then

2. Universal Artificial Intelligence

follow that πζ is also self-optimising in these environments. If we can show
this for many classes of environments, it then follows that πζ is able to perform
well in a wide range of environments, at least in the limit.

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

Although the required analysis is not particularly difficult for many of the
basic classes of environments, sorting out all the definitions, the relationships between them and the conditions under which they admit self-optimising
agents is lengthy and requires some care. This is the subject of the next chapter.

## 3. Taxonomy of Environments

In the previous chapter we introduced the AIXI agent πξ, and its generalisation
to arbitrary spaces of environments, πζ. Of particular importance was Theorem 2.10.5 which roughly said: For any class of environments for which there
exists a self-optimising agent, the agent πζ defined over this class is also selfoptimising. Thus, in order to understand the performance of πζ across a wide
range of environments, we need to understand which classes of environments
admit self-optimising agents, and which do not. In this chapter we present a
partial answer to this question by showing that many well known classes of
environments admit self-optimising agents under reasonable conditions.

$$
\pi^{\xi}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

$$
\pi^{\zeta}
$$

We begin by formalising some common classes of environments. To do this
we examine the environments’ measures and in particular the way in which
they condition on the interaction history. In this way we characterise and
relate many well known classes of environments, such as Bernoulli schemes,
Markov chains, and Markov decision processes (MDPs). Some interesting new
classes of environments naturally arise from the analysis. We then take some
important classes of problems studied in artificial intelligence, such as sequence
prediction and classification, and express these too in terms of the structure of
their measures. This formalisation in terms of chronological measures reveals
that many classes of environments are special cases of other classes, that is, a
hierarchy of classes of environments exists. Studying this more closely we see
that many of these classes are in fact reducible to the class of ergodic MDPs.
Putting all these relationships together produces a taxonomy of classes of
environments.

It is known that certain machine learning algorithms, such as Q-learning,
are self-optimising in the class of ergodic MDPs. As many of the classes in
our taxonomy are reducible to ergodic MDPs, it follows that these classes
also admit self-optimising agents. Thus, from Theorem 2.10.5, we see that πζ
converges to optimal behaviour in these classes of environments. In this way,
we clarify our earlier claim that universal agents can learn to behave optimally
in a wide range of environments, as required by our definition of intelligence.

$$
\pi^{\zeta}
$$

### 3.1. Passive environments

The first class of environments we will consider is the class of passive environments. Loosely speaking, such environments are not affected by the agent’s
actions. We will be more interested in the active environments to be described
in later sections.

3.1.1 Definition. A Bernoulli scheme is an environment (A, X,µ) such
that ∀ax1:k,
µ(ax ax) = µ(x).

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(\underline{x}_{k}).
$$

As the random variables x1,x2,... are independent and identically distributed
(i.i.d.), one may think of a Bernoulli scheme as being an i.i.d. process.

$$
x_{1},x_{2},..
$$

$$
\left(i.i.d.\right)
$$

The above definition involves some slight abuse of notation. Essentially,
what we are showing is that an equivalent measure with the same name (on the
right hand side) can be defined over a reduced parameter space by dropping the
parameters that have no effect on the value of the original measure (on the left
hand side). In other words, the equation above indicates that the distribution
µ over xk can be defined in a way that it is completely independent of the
history ax<kak.

$$
\mu
$$

$$
x_{k}
$$

$$
ax_{<k}a_{k}
$$

Note also that we have written (A, X,µ) in order to specify the action and
perception spaces associated with the measure. This will be necessary in this
chapter as we will often need to consider relationships between environments
that differ in their action and perception spaces.

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

3.1.2 Example. Many simple stochastic processes can be described as
Bernoulli schemes. Imagine a game where a 6 sided die is thrown repetitively.
The agent receives a reward of 1 whenever a 6 is thrown, and 0 otherwise.
There are no actions that the agent can take. Formally, A := {ǫ}, O :=
{1, 2, 3, 4, 5, 6} and R := B. The measure is defined ∀ax1:k,
{

$$
\mathcal{A}\;:=\;\{\epsilon\},\;\mathcal{O}\;:=
\mathcal{R}:=\mathbb{B}
$$

$$
\forall\mathit{ax}_{1:k}
$$

$$
\mu(\underline{{x}}_{k}):=\left\{\begin{array}{l l}{\frac{1}{6}}&{\mathrm{for}x_{k}=o_{k}r_{k}\in\{(1,0),(2,0),(3,0),(4,0),(5,0),(6,1)\},}\\ {0}&{\mathrm{otherwise}.}\\ \end{array}\right.
$$

Other than perhaps a constant environment, Bernoulli schemes are about
the simplest environments possible. Despite their simplicity, they are important in statistics where sets of i.i.d. random variables play an important role.
For example, sampling from a population should ideally produce individuals
that are both independent of each other, and come from the same underlying
distribution.

A natural generalisation of Bernoulli schemes is to allow the next perception to depend on the previous observation. This gives us a richer class of
environments where the distribution over perceptions can change with time:

3.1.3 Definition. A Markov chain is an environment (A, X,µ) that is a
Bernoulli scheme ∀ax1, and ∀ax1:k with k > 1,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1}
$$

$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{k-1}\underline{x}_{k}).
$$

For a Markov chain the last observation completely defines the system’s
state and so these outputs are usually referred to as states. In more general classes of environments this is not the case, so for consistency we will use our
usual terminology of observations and perceptions. Note that we treat the
first cycle as a special case as there is no previous perception to condition on.
By requiring the system to be a Bernoulli scheme in the first cycle we ensure
that the first action has no effect.

3.1.4 Example. Imagine a game where we have a ring shaped playing board
that has been divided into 20 different cells. There is a pebble that starts in
cell 1 and moves around the board as follows: On each turn a standard six
sided die is thrown to decide how many positions the pebble will be moved
clockwise around the board. In cells 5 and 15 the agent receives a reward of
1. Otherwise the reward is 0.

We can model this system as a Markov chain. Let A := {ǫ}, O :=
{0, 1, 2,..., 19}, R := B. For k = 1 the pebble is in cell 1 and thus ∀ax1,
{

$$
\mathcal{A}\;:=\;\{\epsilon\},\;\mathcal{O}\;:=
\{0,1,2,\ldots,19\},\mathcal{R}:=\mathbb{B}
$$

$$
\forall ax_{1}
$$

$$
\mu(\underline{{x}}_{1}):=\left\{\begin{array}{l l}{1}&{\mathrm{f o r~}o_{1}=1\wedge r_{1}=0,}\\ {0}&{\mathrm{o t h e r w i s e.}}\end{array}\right.
$$

Now define ∀ax1:k with k > 1,
 {

$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(o_{k-1}\underline{{x}}_{k}):=\left\{\begin{array}{l l}{\frac{1}{6}}&{\operatorname{for}o_{k}\in\big\{(o_{k-1}+1)\bmod20,\ldots,(o_{k-1}+6)\bmod20\big\}}\\ {}&{\wedge r_{k}=\delta_{5,o_{k}}+\delta_{15,o_{k}},}\\ {0}&{\operatorname{otherwise}.}\\ \end{array}\right.
$$

1
In this game there is a chance of obtaining reward if the pebble is currently
6
in one of the six cells before either cell 5 or cell 15.

$$
\frac{1}{6}
$$

From the definitions of Bernoulli schemes and Markov chains it is clear that
in both of these classes an agent is “passive”, in the sense that its actions have
no effect on the environment’s behaviour. The difference between the two
classes is the size of the history that is relevant to determining the next perception. Increasing the length of this history to the full history of observations
gives us the most general class of completely passive environments:

3.1.5 Definition. A Totally Passive Environment is an environment
(A, X,µ) such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall a x_{1:k}
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{<k}\underline{x}_{k}).
$$

By construction, this class of environments is a superset of the classes of
environments defined thus far. We could define a more limited version of this
class where the next perception only depends on the last n observations, rather
than the full history. However, such an environment is mathematically equivalent to a standard Markov chain where for each history of length n we create
a unique observation in an enlarged observation space. In this new space the
environment can then be represented by a first order Markov chain. This reduction technique will be used in a more general setting to prove Lemma 3.2.6.

3. Taxonomy of Environments

While totally passive environments are useful in modelling some systems,
in terms of artificial intelligence they are relatively uninteresting because the
agent cannot do anything. We can relax this constraint just a little by only
requiring that the agent cannot affect future observations:

3.1.6 Definition. A Passive Environment is an environment (A, X,µ)
such that ∀ax<kaok,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall\underline{ax}_{<k}\underline{\omega}_{k}
$$

$$
\mu(a x_{<k}a\underline{o}_{k})=\mu(o_{<k}\underline{o}_{k}).
$$

Note that there are no restrictions on the rewards; the environment is free
to reward or punish the agent in any way. Totally passive environments are
clearly a special case of passive environments. For more on AIXI in passive
environments see Section 5.3.2 of (Hutter, 2005).

Another important special case is the class of problems where the agent is
rewarded for correctly predicting a sequence that it cannot influence:

3.1.7 Definition. A Sequence Prediction Problem is a passive environment (A, X,µ) such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a o\underline{{r}}_{k})=\mu(a o\underline{{r}}_{k}).
$$

That is, the reward in each cycle depends entirely on the action and the
observation that immediately follows it. As sequence prediction environments
are passive the observations do not depend on the agent’s actions, however
there is no limit on how long the relevant observation history can be. The
above definition makes precise what we meant in previous chapters where
sequence prediction problems were referred to as being “passive”. For more on
how AIXI deals with sequence prediction problems see Section 6.2 of (Hutter,
2005).

3.1.8 Example. Let A = O := {0, 1,..., 9}. Define ∀ax1:k,

$$
\mathcal{A}=\mathcal{O}:=\{0,1,\ldots,9\}
$$

$$
\mu(o_{<k}\underline{{o}}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{i f~}o_{k}\mathrm{~t h e~}k^{t h}\mathrm{~d i g i t~i n~}3.141592\ldots,}\\ {0}&{\mathrm{otherwise},}\\ \end{array}\right.
\mu(\mathit{aor}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{if}r_{k}=1-\frac{1}{9}|o_{k}-a_{k}|,}\\ {0}&{\mathrm{otherwise}.}\end{array}\right.
$$

and

Thus, in order to maximise reward, the agent must generate successive digits
of the mathematical constant π. A correct digit gets a reward of 1, while an
incorrect digit gets a lesser reward proportional to the difference between the
correct digit and the guess.

$$
\pi.\ A
$$

### 3.2. Active environments

The simplest active environment is one where the next perception xk depends
on only the last action ak:

$$
x_{k}
$$

$$
a_{k}
$$

3.2.1 Definition. A Bandit is an environment (A, X,µ) such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(a\underline{x}_{k}).
$$

This class of environments is named after the bandit machines found in casinos around the world, although the relation to real bandit machines is tenuous.
Bandit environments are weaker than Markov chains as future perceptions do
not depend on past observations. However, they do have the ability to react to the last action, and so in this respect they are more powerful. Even
though bandit problems are conceptually simple, solving them optimally is
surprisingly involved (Berry and Fristedt, 1985; Gittins, 1989).

3.2.2 Example. Imagine a machine that has n different levers, or arms, that
the agent can pull. Each arm has a different but fixed probability of generating
a reward. For this example, let the reward be either 0 or 1. The agent’s task
is to figure out which arm to pull so that it maximises its expected reward.
One approach might be to spend time pulling different arms and collecting
statistics in order to estimate which produces the most reward.

We can formally define this bandit as follows: Let O := {ǫ}, R := B and
let A := {1, 2, 3,...,n} represent the n different arms that the agent can pull.
Let β1,β2,...,βn be the respective probabilities of obtaining a reward of 1
after pulling the corresponding arm. Now define ∀ax1:k,
{

$$
\mathcal{O}:=\{\epsilon\},\mathcal{R}:=\mathbb{B}
$$

$$
\mathcal{A}:=\{1,2,3,\ldots,n\}
$$

$$
\beta_{1},\beta_{2},\ldots,\beta_{n}
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a\underline{x}_{k}):=\left\{\begin{array}{l l}{\beta_{a_{k}}}&{\mathrm{for}r_{k}=1,}\\ {1-\beta_{a_{k}}}&{\mathrm{for}r_{k}=0.}\end{array}\right.
$$

A natural extension to the class of bandits is to allow the next perception
to depend on both the last observation and the last action. This produces a
much more powerful class of environments that has been intensively studied
and has many theoretical and practical applications:

3.2.3 Definition. A (stationary) Markov Decision Process (MDP)
is an environment (A, X,µ) that is a Bernoulli scheme ∀ax1, and ∀ax1:k with
k > 1,
µ(ax ax) = µ(o ax).

$$
\forall ax_{1}
$$

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{k-1}a\underline{x}_{k}).
$$

Usually MDPs are defined in such a way that the agent does not act before
the first perception. However, in our definition the first cycle is a Bernoulli
scheme and so the first action has no effect anyway. Aside from this detail,
our definition is equivalent to the standard definition (Bellman, 1957). It is

3. Taxonomy of Environments

immediately clear that this class generalises Bernoulli schemes, bandits and
Markov chains.

What we have defined above is a stationary MDP. This is because the probability of a perception given the current action and the last perception does
not change, that is, it is independent of k. In some definitions the measure µ
is allowed to vary over time. These non-stationary MDPs can be modelled as
POMDPs, which will be defined shortly.

3.2.4 Example. Consider again the simple Markov chain in Example 3.1.4.
This can be extended to an MDP by allowing the agent to decide whether to
move clockwise or anticlockwise around the board. Let O := {0, 1,..., 19}
and R := B as before, but now A := {,} as the agent can select which
direction to move in. For k = 1 the pebble is in cell 1 and thus ∀ax1,
{

$$
\mathcal{O}:=\{0,1,\ldots,19\}
$$

$$
\mathcal{R}:=\mathbb{B}
$$

$$
\mathcal{A}:=\{\circ,\circ\}
$$

$$
k=1
$$

$$
\mu(a\underline{{x}}_{1}):=\left\{\begin{array}{l l}{1}&{\mathrm{f o r~}o_{1}=1\wedge r_{1}=0,}\\ {0}&{\mathrm{o t h e r w i s e.}}\end{array}\right.
\forall ax_{1}
$$

Now define ∀ax1:k with k > 1,


$$
\forall ax_{1:k}
$$

$$
k>1
$$

$$
\mu(o_{k-1}\mathit{a}\underline{{x}}_{k}):=\{\begin{array}{c l}{\frac{1}{6}}&{\operatorname{for}o_{k}\in\{(o_{k-1}+1)\bmod20,\ldots,(o_{k-1}+6)\bmod20\}}\\ {}&{\wedge r_{k}=\delta_{5,o_{k}}+\delta_{15,o_{k}}\wedge a_{k}=\circlearrowleft,}\\ {\frac{1}{6}}&{\operatorname{for}o_{k}\in\{(o_{k-1}-1)\bmod20,\ldots,(o_{k-1}-6)\bmod20\}}\\ {}&{\wedge r_{k}=\delta_{5,o_{k}}+\delta_{15,o_{k}}\wedge a_{k}=\circlearrowleft,}\\ {0}&{\operatorname{o t h e r w i s e.}}\\ \end{array}..
$$

A natural way to generalise the class of MDPs is to allow the next perception
to depend on the last n observations and actions:

3.2.5 Definition. A (stationary) nth order Markov Decision Process
is an environment (A, X,µ) that is a Bernoulli scheme ∀ax1, and ∀ax1:k with
k > 1,
µ(ax ax) = µ(o ao ax),

$$
n^{\mathrm{th}}
$$

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\forall ax_{1}
$$

$$
\forall a x_{1:k}
$$

$$
k>1
$$

$$
\mu(a x_{<k}a\underline{x}_{k})=\mu(o_{k-m}a o_{k-m+1:k-1}a\underline{x}_{k}),
$$

where m := min{n,k}.

$$
m:=\min\{n,k\}
$$

Immediately from the definition we can see that a standard MDP is an nth
order MDP where n = 1. The added complication of the variable m is to allow
for the situation where the current history length k is less than n.

$$
n^{th}
$$

$$
n=1
$$

It might appear that nth order MDPs are more general than standard MDPs,
however it turns out that any nth order MDP can be converted into an equivalent MDP. This is done by extending the observation space and appropriately
modifying the measure. The proof follows the same pattern as the reduction
of nth order Markov chains to standard Markov chains, except that now we
have to deal with the complication of having actions in the history.

$$
n^{th}
$$

$$
n^{th}
$$

$$
n^{th}
$$

3.2.6 Lemma. nth order MDPs can be reduced to MDPs.

$$
n^{th}
$$

$$
\textit{MDPs}
$$

Proof. Let (A, X = O×R,µ) be an nth order MDP. To prove the result
we will define an equivalent first order MDP (A, Z = Q×R, µ˜). We begin by
defining the new observation space,
⋃n

$$
\left(\mathcal{A},\mathcal{X}=\mathcal{O}\times\mathcal{R},\mu\right)
$$

$$
n^{th}
$$

$$
\left(\mathcal{A},\mathcal{Z}=\mathcal{Q}\times\mathcal{R},\tilde{\mu}\right)
$$

$$
\mathcal{Q}:=\bigcup_{i=1}^{n}\mathcal{O}\times(\mathcal{A}\times\mathcal{O})^{i-1}.
$$

Every interaction history that the nth order MDP conditions on is thus uniquely
represented in Q. Although it complicates things, we need to include histories
of length less than n to accommodate the first n − 1 cycles of the system.

$$
n^{th}
$$

$$
\mathcal{Q}
$$

$$
n-1
$$

Next we define a measure µ˜ over the perception space Z, that is equivalent
to the measure µ over the perception space X. We begin by dealing with the
first interaction cycle: ∀az1 ∈A×Z define,
{

$$
\tilde{\mu}
$$

$$
\mathcal{Z},
$$

$$
\mu
$$

$$
\mathcal{X}
$$

$$
\forall a z_{1}\in\mathcal{A}\times\mathcal{Z}
$$

$$
\tilde{\mu}(a\underline{{z}}_{1}):=\left\{\begin{array}{l l}{\mu(a\underline{{z}}_{1})}&{\mathrm{for}z_{1}\in\mathcal{X},}\\ {0}&{\mathrm{otherwise}.}\end{array}\right.
$$

This makes the processes equivalent in the first cycle.

Next, for interaction cycles k > 1, define ∀q


k−1azk ∈Q×A×Z,

$$
\forall q_{k-1}a z_{k}\in\mathcal{Q}\times\mathcal{A}\times\mathcal{Z}
$$

$$
k>1
$$

$$
\tilde{\mu}(q_{k-1}\underline{{\alpha}}_{k}):=\left\{\begin{array}{l l}{\mu(o_{k-m}\mathit{ao}_{k-m+1:k-1}\mathit{a}\underline{{r}}_{k})}&{\mathrm{i f~}q_{k-1}=o_{k-m}\mathit{ao}_{k-m+1:k-1}}\\ {}&{\quad\wedge z_{k}=q_{k}r_{k}}\\ {}&{\quad\wedge q_{k}=o_{k-m+1}\mathit{ao}_{k-m+2:k-1}\mathit{ao}_{k},}\\ {0}&{\mathrm{o t h e r w i s e.}}\\ \end{array}\right.
$$

That is, if the transition qk−1azk is possible when represented in the original
environment, then this transition is given the same probability by µ˜ in the
new environment. Any transition qk−1azk which is impossible in the original
environment, for example because the two histories represented by qk−1 and
qk are inconsistent, is given a transition probability of zero by µ˜. Thus, the
two environments have equivalent structure and dynamics.

$$
q_{k-1}az_{k}
$$

$$
\tilde{\mu}
$$

$$
q_{k-1}az_{k}
$$

$$
q_{k-1}
$$

$$
q_{k}
$$

$$
\tilde{\mu}.
$$

As the proof illustrates, writing down the equation for a higher order MDP
and working with it is cumbersome. Thus, the above result is useful as it means
that we only have to deal with first order MDPs in our analysis. Nevertheless,
conceptually it is often more natural to think of certain problems as being nth
order MDPs.

$$
n^{th}
$$

Rather than increasing the history that the measure conditions on, another
extension is to assume that the agent cannot properly observe the MDP’s
outputs:

3.2.7 Definition. A Partially Observable Markov Decision Process (POMDP) is an environment (A, X = O×R,µ) defined as follows: Let
(A, X˜ = Õ×R, µ˜) be an MDP called the core MDP. Let φ : X×X → ˜ [0, 1] be a
conditional probability measure of the form φ(˜xx) which expresses the probability of perceiving x when the core MDP outputs ˜x. Define ∀ax1:k ∈ (A×X)k,
∑

$$
\left(\mathcal{A},\mathcal{X}=\mathcal{O}\times\mathcal{R},\mu\right)
$$

$$
\left(\mathcal{A},\tilde{\mathcal{X}}=\tilde{\mathcal{O}}\times\mathcal{R},\tilde{\mu}\right)
$$

$$
\phi:\tilde{\mathcal{X}}\times\mathcal{X}\to[0,1]
$$

$$
\phi(\tilde{x}\underline{x})
$$

$$
\forall a x_{1:k}\in(\mathcal{A}\times\mathcal{X})^{k}
$$

$$
\tilde{x}
$$

$$
\mu(a\underline{{x}}_{1:k})\::=\sum_{\tilde{x}_{1:k}\in\tilde{\mathcal{X}}^{k}}\tilde{\mu}(a\underline{{\tilde{x}}}_{1})\:\phi(\tilde{x}_{1}\underline{{x}}_{1})\:\tilde{\mu}(\tilde{o}_{1}a\underline{{\tilde{x}}}_{2})\:\phi(\tilde{x}_{2}\underline{{x}}_{2})\:\cdots\:\tilde{\mu}(\tilde{o}_{k-1}a\underline{{\tilde{x}}}_{k})\:\phi(\tilde{x}_{k}\underline{{x}}_{k}).
$$

3. Taxonomy of Environments

The nature of POMDPs is perhaps best illustrated by example.

3.2.8 Example. Let the core MDP (A, X˜, µ˜) be the MDP defined in Example 3.2.4. Now imagine that the agent cannot reliably observe which cell
the pebble is in. To do this, let X := X˜ and define the observation function
∀x,x ˜ ∈X,
{
61
if x˜ = x,

$$
(\mathcal{A},\tilde{\mathcal{X}},\tilde{\mu})
$$

$$
\mathcal{X}:=\tilde{\mathcal{X}}
$$

$$
\forall\tilde{x},x\in\mathcal{X}
$$

$$
\phi(\tilde{x}\underline{{x}}):=\left\{\begin{array}{l l}{\frac{61}{100}\qquad}&{\mathrm{if}\tilde{x}=x,}\\ {\frac{1}{100}\qquad}&{\mathrm{otherwise}.}\end{array}\right.
$$

Thus, with probability 0.61 the agent observes the true output of the core
MDP. The rest of the time it observes some other randomly chosen output.
The probabilities add up as |X| = |O|×|R| = 20 × 2 = 40. Thus, x can take
39 values other than ˜x.

$$
|\mathcal{X}|=|\mathcal{O}|\times|\mathcal{R}|=20\times2=40
$$

$$
\tilde{x}.
$$

The fact that POMDPs generalise MDPs can be seen by letting X = X˜ and
φ(˜xx) := δx,x˜, in which case it follows that µ = ˜µ. That is, the POMDP reduces
to being its core MDP. Furthermore, as nth order MDPs can be reduced to first
order MDPs, it follows that POMDPs also generalise higher order MDPs.

$$
\mathcal{X}=\tilde{\mathcal{X}}
$$

$$
\phi(\tilde{x}\underline{x}):=\delta_{\tilde{x},x},
$$

$$
\mu=\tilde{\mu}
$$

$$
n^{th}
$$

To see that POMDPs can define non-stationary MDPs, consider a POMDP
where X is a strict subset of X˜. Now use this extra internal information in
the core MDP to keep a parameter that varies over time and that affects the
core MDP’s behaviour. To the external agent who cannot observe this extra
information, it appears that the environment is non-stationary.

$$
\tilde{\mathcal{X}}
$$

Both theoretically and practically this class of environments is difficult to
work with. However, it does encompass a huge variety of possibilities, including all of the environments considered in this chapter, and many real world
problems.

### 3.3. Some common problem classes

Many of the problems considered in artificial intelligence can be expressed as
classes of environments using our measure notation. In this section we will
formalise some of them.

3.3.1 Definition. A Function Maximisation Problem is an environment
(A, X,µ) such that O = R and for some objective function f : A→R we have
∀ax1:k,
{

$$
\left(\mathcal{A},\bar{\mathcal{X}},\mu\right)
$$

$$
\mathcal{O}=\mathcal{R}
$$

$$
f:\mathcal{A}\to\mathcal{R}
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a\underline{{x}}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{i f~}o_{k}=f\big(a_{k}\big)\wedge r_{k}=\operatorname*{m a x}\{o_{1},\ldots,o_{k}\},}\\ {0}&{\mathrm{o t h e r w i s e.}}\end{array}\right.
$$

Essentially, the agent’s actions are interpreted as input to some function,
and in each cycle the result of the function is returned as an observation. We
do not simply return the current value of the function as the reward as this discourages the agent from exploring once a good value has been found. Rather we return the reward associated with the best value found so far. Obviously,
maximisation problems with different ranges, or minimisation problems, can
be expressed by applying a simple transformation to the original objective
function. For more on how AIXI deals with various types of function optimisation problems see Section 6.4 of (Hutter, 2005).

3.3.2 Example. Let f (a) := 1 − (a − 41)2. To maximise reward the agent
must generate the action that maximises f, that is, a = 41.

$$
f(a):=1-(a-\frac{1}{4})^2
$$

$$
a=\frac{1}{4}
$$

Artificial intelligence often considers environments that consist of some kind
of a game that is repetitively played by the agent. Games such as chess, various
card games, tic-tac-toe and others belong to this class, so long as at the end
of each match a new match is started. This can be formalised as follows:

3.3.3 Definition. A Repeated Strategic Game is an environment
(A, X,µ) where ∃l ∈ N such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\exists l\in\mathbb{N}
$$

$$
\forall a x_{1:k}
$$

$$
\mu(ax_{<k}o\underline{x}_{k})=\mu(oo_{lm:k-1}o\underline{x}_{k})
$$

where m := ⌊k/l⌋ is the number of the episode when in cycle k, and l is the
episode length.

$$
m:=\left\lfloor k/l\right\rfloor
$$

Clearly, Bernoulli schemes and bandits are repeated strategic games. If we
want to allow games to finish before the episode finishes we can pad the remaining cycles, and perhaps also reward the system for padded cycles following
a victory in order to encourage rapid wins. For more on how AIXI deals with
strategic games see Section 6.3 of (Hutter, 2005).

Another common type of problem considered in artificial intelligence is classification. A classification problem consists of a domain space W and a set of
classes Z and some function f : W →Z. The agent must try to learn this
mapping based on examples. When given cases where the class is missing it
has to correctly guess the class in order to obtain reward. More formally:

$$
f:\mathcal{W}\to\mathcal{Z}
$$

3.3.4 Definition. A Classification Problem is an environment (A, X,µ)
set up as follows. Let W and Z be two sets called the attribute space
and the class space respectively. Z includes a special symbol “?” used to
indicate whether the agent needs to guess the class. Let O⊂W×Z and let
f : W→Z\{“?”} where ∀ax1:k such that xk−1 = wzrk−1 and xk = wzrk,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\mathcal{Z}
$$

$$
\mathcal{O}\subset\mathcal{W}\times\mathcal{Z}
$$

$$
f:\mathcal{W}\to\mathcal{Z}\setminus\{``?\}
$$

$$
x_{k-1}=w z r_{k-1}
$$

$$
\forall a x_{1:k}
$$

$$
x_{k}=w z r_{k}
$$

$$
\mu(a x_{\leq k}a\underline{w}_{k})=\mu(\underline{w}_{k}),
$$

and for α ∈ (0, 1),

$$
\alpha\in(0,1)
$$

$$
\mu(w_{\underline{z}_{k}})=\left\{\begin{array}{ll}\alpha&if z_{k}=f(w_{k}),\\1-\alpha&if z_{k}=``?,\\0&otherwise,\end{array}\right.
$$

3. Taxonomy of Environments

and

$$
\mu(z_{k-1}a_{k}\underline{r}_{k})=\left\{\begin{array}{ll}1&z_{k-1}="?"\land a_{k}=f(w_{k-1})\land r_{k}=1,\\ 1&z_{k-1}\neq"?"\land r_{k}=0,\\ 0&otherwise.\end{array}\right.
$$

The first condition says that the distribution of the points in the attribute
space is independent of the system’s history. In other words, this part of xk is
a Bernoulli scheme. The second condition says that in each cycle the system
must either provide a training instance or ask for the agent to classify based on
the attribute vector. The parameter α controls how often the agent is asked
to guess the class. The third condition says that reward is given when the
system asks for a classification and the agent guesses it correctly. It is easy to
see that classification problems are passive MDPs.

$$
x_{k}
$$

3.3.5 Example. Let each element of W be a vector of medical measurements
for a patient, and Z some list of diseases. When provided with a list of
patients’ statistics and their diseases, the agent’s job is to learn a function
that determines which disease is present given a patient’s medical data.

For more on how AIXI deals with supervised learning problems see Section 6.5 of (Hutter, 2005).

### 3.4. Ergodic MDPs

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

### 3.4.5 Theorem. Ergodic MDPs admit self-optimising agents.

For references and other details see Appendix B. As ergodic MDPs admit
self-optimising agents it follows by Theorem 2.10.5 that the universal agent πζ
defined over the class of ergodic MDPs is also self-optimising. What remains
to be shown is that many important classes of environments are in fact special
cases of ergodic MDPs. This is the topic of the next section.

$$
\pi^{\zeta}
$$

### 3.5. Environments that admit self-optimising agents

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

### 3.5.2 Lemma. Bernoulli schemes are ergodic MDPs.

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

### 3.5.3 Lemma. Classification problems are ergodic MDPs.

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

### 3.5.4 Lemma. Bandits are ergodic MDPs.

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

### 3.5.5 Lemma. Repeated strategic games are reducible to ergodic MDPs.

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

### 3.6. Conclusion

In this chapter we have defined a range of classes of environments and shown
that many of these are either special cases of other more general classes, or
are at least reducible to more elementary classes through a change of action
and perception spaces. This hierarchy of classes defines a kind of taxonomy
of environments. To the best of our knowledge this analysis has not been
done before. Figure 3.1 summarises these relationships. The most general
and powerful classes of environments are at the top and the most limited and
specific classes at the bottom. As we can see, all of the more concrete classes at
the bottom of the hierarchy admit self-optimising agents. By Theorem 2.10.5
it then follows that a universal agent defined over one of these classes is also
self-optimising. This supports our earlier claim that universal agents are able
to perform well in a wide range of environments, as required by our informal
definition of intelligence.

Chronological Environment

POMDP

Passive Environment

Sequence Prediction

nth order MDP

MDP

Function Maximisation

Totally Passive Environment

Markov Chain

Computable Sequence Prediction

Ergodic nth order MDP

Ergodic MDP

Ergodic Markov Chain

Repeated Strategic Game

Bandit

Classification

Bernoulli Scheme

Environments that admit self-optimising agents

Figure 3.1.: Taxonomy of environments. Downward arrows indicate that the
class below is a special case of the class above. Dotted horizontal
lines indicate that two classes of environments are reducible to
each other. The greyed area contains the classes of environments
that admit self-optimising agents, that is, the environments in
which a universal agent will learn to behave optimally.

## 4. Universal Intelligence Measure

“. . . we need a definition of intelligence that is applicable to machines as well as humans or even dogs. Further, it would be helpful
to have a relative measure of intelligence, that would enable us to
judge one program more or less intelligent than another, rather
than identify some absolute criterion. Then it will be possible to
assess whether progress is being made . . . ” Johnson (1992)

In Chapter 1 we explored the concept of intelligence and proposed an informal definition of intelligence. In Chapter 2 we introduced universal agents,
and in Chapter 3 we detailed some of the classes of environments in which
their behaviour converges to optimal. This shows that universal agents are
highly intelligent with respect to the definition of intelligence that we have
adopted. One could argue that the universal agent defined over the space of
all enumerable chronological environments, that is AIXI, is in some sense an
optimal machine intelligence.

In this chapter we turn this idea on its head: Instead of using the theory of
universal artificial intelligence to define powerful agents, we use it instead to
formally define intelligence itself. One approach is to take AIXI and to mathematically define a performance measure under which AIXI is the maximal
agent by construction. This is the approach taken by the Intelligence Order
Relation (see Section 5.1.4 in Hutter, 2005). Although this produces a very
general relation for comparing the relative performance of agents, in order to
justify calling this a formal definition of “intelligence” one must carefully examine the way in which intelligence is defined, and then show how this relates
to the equation.

In this chapter we bridge this gap by proceeding in the opposite direction.
We begin with our informal definition of intelligence from Chapter 1 that was
based on a range of standard definitions given by psychologists and artificial
intelligence researchers. We then formalise this definition, borrowing ideas
from reinforcement learning, Kolmogorov complexity, Solomonoff induction
and universal artificial intelligence theory as necessary. The result is an equation for intelligence that is strongly related to existing definitions, and with
respect to which highly intelligent agents can be proven to have powerful optimality properties. We then look at some of this definition’s properties and
compare it to other tests and definitions of machine intelligence.

### 4.1. A formal definition of machine intelligence

Consider again our informal definition of intelligence:

Intelligence measures an agent’s ability to achieve goals in a wide
range of environments.

This definition contains three essential components: An agent, environments
and goals. Clearly, the agent and the environment must be able to interact
with each other, specifically, the agent needs to be able to send signals to
the environment and also receive signals being sent from the environment.
Similarly, the environment must be able to send and receive signals. In our
terminology we will adopt the agent’s perspective on these communications
and refer to the signals sent from the agent to the environment as actions, and
the signals sent from the environment to the agent as perceptions.

Our definition of an agent’s intelligence also requires there to be some kind
of goal for the agent to try to achieve. Perhaps an agent could be intelligent,
in an abstract sense, without having any objective to apply its intelligence
to. Or perhaps the agent has no desire to exercise its intelligence in a way
that affects its environment. In either case, the agent’s intelligence would be
unobservable and, more importantly, of no practical consequence. Intelligence
then, at least the concrete kind that interests us, comes into effect when the
agent has an objective or goal that it actively pursues by interacting with its
environment.

The existence of a goal raises the problem of how the agent knows what the
goal is. One possibility would be for the goal to be known in advance and
for this knowledge to be built into the agent. The problem with this is that
it limits each agent to just one goal. We need to allow agents that are more
flexible, specifically, we need to be able to inform the agent of what the goal
is. For humans this is easily done using language. In general however, the
possession of a sufficiently high level of language is too strong an assumption
to make about the agent. Indeed, even for something as intelligent as a dog
or a cat, direct explanation is not very effective.

Fortunately there is another possibility which is, in some sense, a blend of
the above two. We define an additional communication channel with the simplest possible semantics: a signal that indicates how good the agent’s current
situation is. We will call this signal the reward. The agent simply has to
maximise the amount of reward it receives, which is a function of the goal. In
a complex setting the agent might be rewarded for winning a game or solving
a puzzle. If the agent is to succeed in its environment, that is, receive a lot of
reward, it must learn about the structure of the environment and in particular
what it needs to do in order to get reward.

This system of an agent interacting with an environment and trying to
achieve some goal is the reinforcement learning agent-environment framework
from Section 2.8. That this framework fits well with our informal definition
of intelligence is not surprising given how simple and general it is. Indeed, it is not only used in artificial intelligence, in control theory it is known as
the plant-controller framework. For example, the plant could be a nuclear
power plant, and the controller a system designed to keep the reactor within
safe operating guidelines. Even the way in which you might train your dog
to perform tricks by rewarding certain behaviours fits into this very general
framework.

As in Section 2.8, we will include the reward signal as a part of the perception
generated by the environment. The perceptions also contain a non-reward
part, which we will refer to as observations. The goal is implicitly defined by
the environment as this is what controls when rewards are generated. Thus,
in the framework as we have defined it, to test an agent in any given way it is
sufficient to fully define the environment.

Unfortunately, maximising reward is not sufficient to define how the agent
should behave over time. We have to define some kind of a temporal preference
that describes how much the agent should value near term rewards verses
rewards further into the future. As we saw in Section 2.9, a general approach
is to weight, or discount, each reward in a way that depends on which cycle
it occurs in. Let γ1,γ2,... be the discounts we apply to the reward in each
∑∞
successive cycle, where ∀i : γi ≥ 0, andi=1γi < ∞ in order to avoid infinite
weighted sums. Now define the expected future discounted reward for agent π
interacting with environment µ to be,
()

$$
\gamma_{1},\gamma_{2},\ldots
$$

$$
\forall i:\gamma_{i}\geq0
$$

$$
\sum_{i=1}^{\infty}\gamma_{i}<\infty
$$

$$
\pi
$$

$$
\mu
$$

$$
V_{\gamma}^{\pi\mu}:=\mathbf{E}\Bigg(\sum_{i=t}^{\infty}\gamma_{i}r_{i}\Bigg).
$$

It is this value function that incorporates our temporal preferences that the
agent must optimise. Although this is very general, the discounting parameters γ1,γ2,... are nevertheless free parameters. In order to make our formal
measure unique we want to remove these parameters, and of course we must
do so in a way that is still completely general.

$$
\gamma_{1},\gamma_{2},\ldots
$$

If we look at the value function above, we see that discounting plays two
roles. Firstly, it normalises rewards received so that their sum is always finite.
Secondly, it weights the rewards at different points in the future which in effect
defines a temporal preference. A direct way to solve both of these problems,
without needing an external parameter, is to simply require the total reward
returned by the environment to be bounded. Without loss of generality, we
set the bound to be 1. We denote this set of reward-summable environments
by E. For any µ ∈ E, it follows that the expected value of the sum of rewards
is also finite and thus discounting is no longer required,
()

$$
\mu\in\mathbb{E}
$$

$$
V_{\mu}^{\pi}:=\;\mathbf{E}\left(\sum_{i=1}^{\infty}r_{i}\right)\leq1.
$$

One way of viewing this is that the rewards returned by the environment
now have the temporal preference already factored in. Indeed, because every

4. Universal Intelligence Measure

reward summable environment is included, in effect every possible temporal
preference is represented in the space of environments. The cost is that this is
an additional condition that we place on the space of environments. Previously
we required that each reward signal was in a subset of [0, 1] ∩ Q, now we have
the additional constraint that the reward sum is always bounded.

Next we need to quantify what we mean by “goals in a wide range of environments.” As we have argued previously, intelligence is not simply the ability
to perform well at a narrowly defined task; it is much broader. An intelligent agent is able to adapt and learn to deal with many different situations,
kinds of problems and types of environments. In our informal definition this
was described as the agent’s general ability to perform well in a “wide range
of environments.” This flexibility is a defining characteristic and one of the
most important differences between humans and many current AI systems:
while Gary Kasparov would still be a formidable player if we were to change
the rules of chess, IBM’s Deep Blue chess super computer would be rendered
useless without significant human intervention.

As we want our definition to be as broad and encompassing as possible, the
space of environments used should be as large as possible. As the environment
is a probability measure with a certain structure, an obvious possibility would
be to consider the space of all probability measures of this form. Unfortunately, this extremely broad class of environments causes serious problems.
As the space of all probability measures is uncountably infinite, some environments cannot be described in a finite way and so are incomputable. This would
make it impossible, by definition, to test an agent in such an environment using a computer. Further, most environments would be infinitely complex and
have little structure for the agent to learn from.

The solution is to require the environmental probability measures to be
computable. Not only is this condition necessary if we are to have an effective
measure of intelligence, it is also not as restrictive as it might first appear.
There are still an infinite number of environments with no upper bound on
their maximal complexity. Also, although the measures that describe the environments are computable, this does not mean that the environments are deterministic. For example, although a typical sequence of 1’s and 0’s generated
by flipping a coin is not computable, the probability measure that describes
this distribution is computable and thus it is included in our space of possible environments. Indeed, there is currently no evidence that the physical
universe cannot be simulated by a Turing machine in the above sense (for further discussion of this point see Section 4.4). This appears to be the largest
reasonable space of environments.

We have now formalised all the elements of our informal definition. The next
problem is how to bring these together in order to define an overall measure
of performance; we need to find a way to combine an agent’s performance
in many different environments into a single overall measure. As there are an
infinite number of environments, we cannot simply take a uniform distribution over them. Mathematically, we must weight some environments higher than
others. But how?

Consider the agent’s perspective on this situation: there exists a probability measure that describes the true environment, however this measure is not
known to the agent. The only information the agent has are some past observations of the environment. From these, the agent can construct a list of
probability measures that are consistent with the observations. We call these
potential explanations of the true environment hypotheses. As the number of
observations increases, the set of hypotheses shrinks and hopefully the remaining hypotheses become increasingly accurate at modelling the environment.

The problem is that in any given situation there will likely be a large number of hypotheses that are consistent with the current set of observations.
The agent must keep these in accordance with Epicurus’ principle of multiple
explanations, as we saw in Section 2.1. Because they are all consistent with
the current observations, if the agent is going to estimate which hypotheses
are the most likely to be correct it must resort to something other than this
observational information. This is a frequently occurring problem in inductive
inference for which the most common approach is to invoke the principle of
Occam’s razor, which we also met in Section 2.1:

Given multiple hypotheses that are consistent with the data, the simplest should be preferred.

This is generally considered the rational and intelligent thing to do (Wallace,
2005). Indeed, as noted in Section 1.5, standard IQ tests implicitly test an
individual’s ability to use Occam’s razor. In some cases we may even consider
the correct use of Occam’s razor to be a more important demonstration of
intelligence than achieving a successful outcome. Consider, for example, the
following game:

4.1.1 Example. (Dumb luck game) A questioner lays twenty 10 notes
out on a table before you and then points to the first one and asks “Yes or
No?”. If you answer “Yes” he hands you the money. If you answer “No”
he takes it from the table and puts it in his pocket. He then points to the
next 10 note on the table and asks the same question. Although you, as
an intelligent agent, might experiment with answering both “Yes” and “No”
a few times, by the 13th round you would have decided that the best choice
seems to be “Yes” each time. However what you do not know is that if you
answer “Yes” in the 13th round then the questioner will pull out a gun and
shoot you! Thus, although answering “Yes” in the 13th round is the most
intelligent choice, given what you know, it is not the most successful one. An
exceptionally dim individual may have failed to notice the obvious relationship
between answers and getting the money, and thus might answer “No” in the
13th round, thereby saving his life due to what could truly be called “dumb
luck”.

$$
13^{th}
$$

$$
13^{th}
$$

$$
13^{th}
$$

$$
13^{th}
$$

4. Universal Intelligence Measure

What is important then, is not that an intelligent agent succeeds in any given
situation, but rather that it takes actions that we would expect to be the most
likely ones to lead to success. Given adequate experience this might be clear,
however experience is often not sufficient and one must fall back on good prior
assumptions about the world, such as Occam’s razor. It is important then that
we test the agents in such a way that they are, at least on average, rewarded
for correctly applying Occam’s razor, even if in some cases this leads to failure.

Note that this does not necessarily mean always following the simplest hypothesis that is consistent with the observations. It is just that simpler hypotheses are considered to be more likely to be correct. Thus, if there is a
simple hypothesis suggesting one thing, and a large number of slightly more
complex hypotheses suggesting something else, the latter may be considered
the most likely.

There is another subtlety that needs to be pointed out. Often intelligence is
thought of as the ability to deal with complexity. Or in the words of one psychologist, “. . . [intelligence] is the ability to deal with cognitive complexity —
in particular, with complex information processing.”(Gottfredson, 1997b) It is
tempting then to equate the difficultly of an environment with its complexity. Unfortunately, things are not so straightforward. Consider the following
environment:

4.1.2 Example. Imagine a very complex environment with a rich set of
relationships between the agent’s actions and observations. The measure that
describes this will have a high complexity. However, also imagine that the reward signal is always maximal no matter what the agent does. Thus, although
this is a very complex environment in which the agent is unlikely to be able to
predict what it will observe next, it is also an easy environment in the sense
that all agents are optimal, even very simple ones that do nothing at all. The
environment contains a lot of structure that is irrelevant to the goal that the
agent is trying to achieve.

From this perspective, a problem is thought of as being difficult if the simplest good solution to the problem is complex. Easy problems on the other
hand are those that have simple solutions. This is a very natural way to think
about the difficulty of problems, or in our terminology, environments.

Fortunately, this distinction does not affect our use of Occam’s razor. This
is because Occam’s razor assigns to each hypothesis a prior probability of it
being the correct model according to its complexity. It says nothing about how
relevant or useful that hypothesis might be to the agent’s goals. For example,
according to Occam’s razor a simple environment that always gives the agent
maximal reward would be more likely than a complex environment that also
always gives the agent maximal reward, even though the two environments are
equally easy to succeed in. Of course from an agent’s perspective, an incorrect
hypothesis that fails to model much of the environment may be a good one if
the parts of the environment that the hypothesis fails to model are not relevant
to receiving reward. Nevertheless, if we want to reward agents on average for correctly using Occam’s razor, we must weight the environments according to
their complexity, not their difficulty.

Although we have chosen to follow a fairly strict interpretation of Occam’s
razor, the idea of weighting according to the complexity of the simplest good
solution may have some merit. For example, if we weight the different “experts” in a prediction with expert advice algorithm according to their complexity, we are in effect applying this alternate principle. In practice, this can work
well.

Our remaining problem now is to measure the complexity of environments.
This is a problem that we have already solved for sequences in Section 2.5, and
then generalised to active environments in Section 2.10: for any environment
µ ∈ E we define its complexity to be K(µ), that is, its Kolmogorov complexity
which is essentially just the length of the shortest program that describes µ.

$$
\mu\in\mathbb{E}
$$

$$
K(\mu)
$$

$$
\mu
$$

Bringing all these pieces together, we can now define our formal measure of
intelligence:

4.1.3 Definition. The universal intelligence of an agent π is its expected
performance with respect to the universal distribution 2−K(µ) over the space
of all computable reward-summable environments E, that is,
∑

$$
2^{-K(\mu)}
$$

$$
\Upsilon(\pi):=\sum_{\mu\in\mathbb{E}}2^{-K(\mu)}V_{\mu}^{\pi}=V_{\xi}^{\pi}.
$$

The final equality above follows from the linearity of V and the definition of ξ
as a weighted mixture of environments. It shows that the universal intelligence
of an agent is simply its expected performance with respect to the universal
distribution.

$$
\xi
$$

Consider how this equation corresponds to our informal definition. We need
to measure an agent’s ability to achieve goals in a wide range of environments.
Clearly present in the equation is the agent π, the environment µ and, implicit
in the environment, a goal. The agent’s “ability to achieve” is represented by
the value function Vµπ. By a “wide range of environments” we have taken the
space of all computable reward-summable environments, where these environments have been characterised as computable chronological measures in the
set E. Occam’s razor is given by the term 2−K(µ) which weights the agent’s
performance in each environment in a way that decreases according to its complexity. The definition is very general in terms of which sensors or actuators
the agent might have, as all information exchanged between the agent and the
environment takes place over very general communication channels. Finally,
the formal definition places no limits on the internal workings of the agent.
Thus, we can apply the definition to any system that is able to receive and
generate information with a view to achieving goals.

$$
\pi
$$

$$
\mu
$$

$$
V_{\mu}^{\pi}
$$

$$
2^{-K(\mu)}
$$

The main drawback is that the Kolmogorov complexity function K is not
computable and can only be approximated. This is acceptable as our aim has
simply been to define the concept of intelligence in the most general, powerful
and elegant way. In future research we will explore ways to approximate this

4. Universal Intelligence Measure

ideal with a practical test. Naturally, the process of estimation will introduce
weaknesses and flaws that the current definition does not have. For example,
while the definition considers the general performance of an agent over all
computable environments with bounded reward sum, in practice a test could
only ever estimate this by testing the agent on a finite sample of environments.

This situation is similar to the definition of randomness for sequences: Informally, an infinite sequence is said to be Martin-L¨of random when it has no
significant regularity (Martin-L¨of, 1966). This lack of regularity is equivalent
to saying that the sequence cannot be compressed in any significant way, and
thus we can characterise randomness using Kolmogorov complexity. Naturally,
we cannot test a sequence for every possible regularity, which is equivalent to
saying that we cannot compute its Kolmogorov complexity. We can however
test sequences for randomness by checking them for a large number of statistical regularities; indeed, this is what is done in practice. Of course, just
because a sequence passes all our tests does not mean that it must be random.
There could always be some deeper structure to the sequence that our tests
were not able to detect. All we can say is that the sequence seems random
with respect to our ability to detect patterns.

Some might argue that the definition of something should not just capture
the concept, it should also be practical. For example, the definition of intelligence should be such that intelligence can be easily measured. The above
example, however, illustrates why this approach is sometimes flawed: if we
were to define randomness with respect to a particular set of tests, then one
could specifically construct a sequence that followed a regular pattern in such
a way that it passed all of our randomness tests. This would completely undermine our definition of randomness. A better approach is to define the concept
in the strongest and cleanest way possible, and then to accept that our ability
to test for this ideal has limitations. In other words, our task is to find better
and more effective tests, not to redefine what it is that we are testing for.
This is the attitude we have taken here, though in this thesis our focus is on
the first part, that is, establishing a strong theoretical definition of machine
intelligence.

### 4.2. Universal intelligence of various agents

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

### 4.3. Properties of universal intelligence

What we have presented is a definition of machine intelligence. It is not a
practical test of machine intelligence, indeed the value of Υ is not computable
due to the use of Kolmogorov complexity. Although some of the criteria by
which we judge practical tests of intelligence are not relevant to a pure definition of intelligence, many of the desirable properties are similar. Thus, to
understand the strengths and weaknesses of our definition, consider again the
desirable properties for a test of intelligence from Section 1.4.

Valid. The most important property of any proposed formal definition of
intelligence is that it does indeed describe something that can reasonably be
called intelligence. Essentially, this is the core argument of this chapter so far:
we have taken a mainstream informal definition and step by step formalised it.
Thus, so long as our informal definition is acceptable, and our formalisation
argument holds, the result can reasonably be described as a formal definition
of intelligence.

As we saw in the previous section, universal intelligence orders the power
and adaptability of simple agents in a natural way. Furthermore, a high value
of Υ implies that the agent performs well on most simple and moderately
complex environments. Such an agent would be an impressively powerful and
flexible piece of technology, with many potential uses. Clearly then, universal intelligence is inherently meaningful, independent of whether or not one
considers it to be a measure of intelligence.

Informative. Υ(π) assigns to agent π a real value that is independent of the
performance of other possible agents. Thus we can make direct comparisons
between many different agents on a single scale. This property is useful if we
want to use this measure to study new algorithms or modifications to existing
algorithms. In comparison, some other tests return only comparative results,
i.e. that one algorithm is better than another, or even just a binary pass or
fail.

4. Universal Intelligence Measure

Wide range. As we saw in the previous section, universal intelligence is able
basic
to order the intelligence of even the most basic agents such as πrand, π,
2forward
π2back and π. At the other extreme we have the theoretical super intelligent agent AIXI which has maximal Υ value. Thus, universal intelligence
spans trivial learning algorithms right up to incomputable super intelligent
agents. This seems to be the widest range possible for a measure of machine
intelligence.

$$
\pi^{\tt r a n d},\pi^{\tt b a s i c}
$$

$$
\pi^{\tt2b a c k}
$$

$$
\pi^{\tt2f o r w a r d}
$$

General. As the agent’s performance on all well defined environments is factored into its Υ value, a broader performance metric is difficult to imagine.
Indeed, a well defined measure of intelligence that is broader than universal
intelligence would seem to contradict the Church-Turing thesis as it would
imply that we could effectively measure an agent’s performance for some well
defined problem that was outside of the space of computable measures.

Dynamic. Universal intelligence includes environments in which the agent
has to learn and adapt its behaviour over time in order to maximise reward.
As such, it is a so called “dynamic intelligence test” that allows rich interaction
between the agent being tested and its environment (see Section 1.4). In
comparison, most other intelligence tests are “static”, in the sense that they
only require the agent to solve isolated one-off problems. Such tests cannot
directly measure an agent’s ability to learn and adapt over time.

Unbiased. In a standard intelligence test, an individual’s performance is
judged on specific kinds of problems, and then these scores are combined to
produce an overall result. Thus the outcome of the test depends on which
types of problems it uses, and how each score is weighted to produce the end
result. Unfortunately, how we do this is a product of many things, including our culture, values and the theoretical perspective on intelligence that
we have taken. For example, while one intelligence test might contain many
logical puzzle problems, another might be more linguistic in emphasis, while
another stresses visual reasoning. Modern intelligence tests like the Stanford-
Binet try to minimise this problem by covering the most important areas of
human reasoning both verbally and non-verbally. This helps but it is still
very anthropocentric as we are only testing those abilities that we think are
important for human intelligence.

For an intelligence measure for machines we have to base the test on something more general and principled: universal Turing computation. As all proposed models of computation have thus far been equivalent in their expressive
power, the concept of computation appears to be a fundamental theoretical
property rather than the product of any specific culture. Thus, by weighting
different environments depending on their Kolmogorov complexity, and considering the space of all computable environments, we have avoided having to
define intelligence with respect to any particular culture, species etc.

Unfortunately, we have not entirely removed the problem. The environmental distribution 2−K(µ) that we have used is invariant, up to a multiplicative
constant, to changes in the reference machine U. Although this affords us some
protection, the relative intelligence of agents can change if we change our reference machine. One approach to this problem is to limit the complexity of
the reference machine, for example by limiting its state-symbol complexity.
We expect that for highly intelligent machines that can deal with a wide range
of environments of varying complexity, the effect of changing from one simple
reference machine to another will be minor. For simple agents, such as those
considered in Section 4.2, the ordering of their machine intelligence was also
not particularly sensitive to natural choices of reference machine. Recently attempts have been made to make algorithmic probability completely unique by
identifying which universal Turing machines are, in some sense, the most simple (M¨uller, 2006). Unfortunately however, an elegant solution to this problem
has not yet been found.

An alternate solution, suggested by Peter Dayan (personal communication),
would be to allow the agent to maintain state between different test environments. This would mitigate any bias introduced as intelligent agents would
then be able to adapt to the test’s reference machine over multiple test trials.

Fundamental. Universal intelligence is based on Turing computation, information and complexity. These are fundamental universal concepts that are
unlikely to change in the future with changes in technology. It also means
that universal intelligence is in no way anthropocentric.

Formal and objective. As universal intelligence is expressed as a mathematical equation, there is little space for ambiguity in the definition. In particular,
it in no way depends on any subjective criteria, unlike some other intelligence
tests and definitions.

Fully defined. For a fixed reference machine, the universal intelligence measure is fully defined. In comparison, some tests of machine intelligence have
aspects which are currently unspecified and in need of further research.

Impractical. In its current form the definition cannot be directly turned into
a test of intelligence as the Kolmogorov complexity function is not computable.
Thus, in its pure form, we can only use it to analyse the nature of intelligence
and to theoretically examine the intelligence of mathematically defined learning algorithms.

In order to use universal intelligence more generally we will need to construct a workable test that approximates an agent’s Υ value. The equation
for Υ suggests how we might approach this problem. Essentially, an agent’s
universal intelligence is a weighted sum of its performance over the space of all

4. Universal Intelligence Measure

environments. Thus, we could randomly generate programs that describe environmental probability measures and then test the agent’s performance against
each of these environments. After sampling sufficiently many environments,
the agent’s approximate universal intelligence could be estimated by weighting
its score in each environment according to the complexity of the environment
as given by the length of its program. Another possibility might be to try to
approximate the sum by enumerating environmental programs from short to
long, as the short ones will make by far the greatest contribution to the sum.
However, in this case we will need to be able to reset the state of the agent so
that it cannot cheat by learning our environmental enumeration method. In
any case, various practical challenges will need to be addressed before universal intelligence can be used to construct an effective intelligence test. As this
would be a significant project in its own right, here we focus on the theoretical
issues surrounding universal intelligence.

Definition rather than a test. As it is not practical in its current form, universal intelligence is more of a formal definition of intelligence than a test of
intelligence. Some proposals we have reviewed aim to be just tests of intelligence, others aim to be definitions, and in some cases they are intended to
be both. Often the exact classification of a proposal as a test or definition, or
both, is somewhat subjective.

Having covered the key properties of the universal intelligence measure, we
now compare these properties with the properties of the other proposed tests
and definitions of machine intelligence surveyed in Section 1.7. Although we
have attempted to be as fair as possible, some of our judgements will of course
be debatable. Nevertheless, we hope that it provides a rough overview of the
relative strengths and weaknesses of the proposals. The summary comparison
appears in Table 4.1.

### 4.4. Response to common criticisms

Attempting to mathematically define intelligence is very ambitious and so,
not surprisingly, the reactions we get can be interesting. Having presented the
essence of this work as posters at several conferences, and also as a 30 minute
talk, we now have some idea of what the typical responses are. Most people
start out sceptical but end up generally enthusiastic, even if they still have a
few reservations. This positive feedback has helped motivate us to continue
this direction of research. In this section, however, we will attempt to cover
some of the more common criticisms.

It’s obviously false, there’s nothing in your definition, just a few equations.
Perhaps the most common criticism is also the most vacuous one: It’s obviously

| 4.4. Response to common criticisms |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Intelligence Test | Valid | Informative | Wide Range General | Dynamic | Unbiased | Fundamental | Formal &amp; Obj. | Fully Defined Practical | Test vs. Def. |  |  |
| Turing Test | ● | · | · | · | ● | · | · | ● | ● | T |  |
| Total Turing Test | ● | · | · | · | ● | · | · | ● | · | T |  |
| Inverted Turing Test | ● | ● | · | · | ● | · | · | ● | ● | T |  |
| Toddler Turing Test | ● | · | · | · | ● | · | · | · | · | T |  |
| Linguistic Complexity | ● | ● | · | · | · | · | · | · | · | T |  |
| Text Compression Test | ● | ● | ● | ● | · | ● | ● | ● | ● | T |  |
| Turing Ratio | ● | ● | ● | ● | ? | ? | ? | ? | ? | T/D |  |
| Psychometric AI | ● | ● | · | ● | ? | ● | · | ● | ● | T/D |  |
| Smith's Test | ● | ● | ● | ● | · | ? | ● | ● | · | T/D |  |
| C-Test | ● | ● | ● | ● | · | ● | ● | ● | ● | T/D |  |
| Universal Intelligence | ● | ● | ● | ● | ● | ● | ● | ● | ● | D |  |

Table 4.1.: In the tablemeans “yes”, • means “debatable”, · means “no”,
and ? means unknown. When something is rated as unknown it is
because the test in question is not sufficiently specified.

wrong! These people seem to believe that defining intelligence with an equation
is clearly impossible, and thus there must be very large and obvious flaws in
our work.Not surprisingly, these people are also the least likely to want to
spend 10 minutes having the material explained to them. Unfortunately, none
of these people have been able to communicate why the work is so obviously
flawed in any concrete way — despite in one instance chasing the poor fellow
out of the conference centre and down the street begging for an explanation.
If anyone would like to properly explain their position to us in the future, we
promise not to chase you down the street!

It’s obviously correct, indeed everybody already knows this.Curiously, the
second most common criticism is the exact opposite: The work is obviously
right, and indeed it is already well known.Digging deeper, the heart of this
criticism comes from the perception that we have not done much more than just
describe reinforcement learning. If you already accept that the reinforcement
learning framework is the most general and flexible way to describe artificial
intelligence, and not everybody does, then by mixing in Occam’s razor and a
dash of complexity theory the equation for universal intelligence follows in a
fairly straightforward way.While this is true, the way in which these things
have been brought together is new.Furthermore, simply coming up with an
equation is not enough, one must argue that what the equation describes is in
fact intelligence in a sense that is reasonable for machines.

We have addressed this question in three main ways: Firstly,in Chapter 1 we explored many expert definitions of intelligence.Based on these,
we adopted our own informal definition of intelligence in Section 1.2.In the

4. Universal Intelligence Measure

present chapter this informal definition was piece by piece formalised leading
to the equation for Υ. This chain of argument ties our equation for intelligence to existing informal definitions and ideas on the nature of intelligence.
Secondly, in Sections 4.2 and 4.3 we showed that the equation has properties
that are consistent with a definition of intelligence. Finally, in Section 4.2 it
was shown that universal intelligence is strongly connected to the theory of
universally optimal learning agents, in particular AIXI. From this it follows
that machines with very high universal intelligence have a wide range of powerful optimality properties. Clearly then, what we have done goes far beyond
merely restating reinforcement learning theory.

Assuming that the environment is computable is too strong. It is certainly
possible that the physical universe is not computable, in the sense that the
probability distribution over future events cannot, even in theory, be simulated
to an arbitrary precision by a computable process. Some people take this position on various philosophical grounds, such as the need for freewill. However,
in standard physics there is no law of the universe that is not computable in the
above sense. Nor is there any evidence showing that such a physical law must
exist. This includes quantum theory and chaotic systems, both of which can
be extremely difficult to compute for some physical systems, but are not fundamentally incomputable theories. In the case of quantum computers, they can
compute with lower time complexity than classical Turing machines, however
they are unable to compute anything that a classical Turing machine cannot,
when given enough time. Thus, as there is no hard evidence of incomputable
processes in the universe, our assumption that the agent’s environment has a
computable distribution is certainly not unreasonable.

If a physical process was ever discovered that was not Turing computable,
then this would likely result in a new extended model of computation. Just as
we have based universal intelligence on the Turing model of computation, it
might be possible to construct a new definition of universal intelligence based
on this new model in a natural way.

Finally, even if the universe is not computable, and we do not update our
formal definition of intelligence to take this into account, the fact that everything in physics so far is computable means that a computable approximation
to our universe would still be extremely accurate over a huge range of situations. In which case, an agent that could deal with a wide range of computable
environments would most likely still function well within such a universe.

Assuming that environments return bounded sum rewards is unrealistic. If
an environment µ is an artificial game, like chess, then it seems fairly natural
for µ to meet any requirements in its definition, such as having a bounded
reward sum. However, if we think of the environment µ as being the universe
in which the agent lives, then it seems unreasonable to expect that it should
be required to respect such a bound.

$$
\mu
$$

$$
\mu
$$

$$
\mu
$$

Strictly speaking, reward is an interpretation of the state of the environment. In this case the environment is the universe, and clearly the universe
does not have any notion of reward for particular agents. In humans this interpretation is internal, for example, the pain that is experienced when you
touch something hot. In this case, should it be a part of the agent rather than
the environment? If we gave the agent complete control over rewards then our
framework would become meaningless: the perfect agent could simply give
itself constant maximum reward. Perhaps the analogous situation for humans
would be taking the “perfect” drug.

A more accurate framework would consist of an agent, an environment and
a separate goal system that interpreted the state of the environment and rewarded the agent appropriately. In such a set up the bounded rewards restriction would be a part of the goal system and thus the above problem would not
occur. However, for our current purposes, it is sufficient just to fold this goal
mechanism into the environment and add an easily implemented constraint to
how the environment may generate rewards. One simple way to bound an environment’s total rewards would be to use geometric discounting as discussed
in Section 2.9.

How do you respond to Block’s “Blockhead” argument? The approach
we have taken is unabashedly functional. Theoretically, we desired to have a
formal, simple and very general definition. This is easier to do if we abstract
over the internal workings of the agent and define intelligence only in terms
of external communications. Practically, what matters is how well something
works. By definition, if an agent has a high value of Υ, then it must work well
over a wide range of environments.

Block attacks this perspective by describing a machine that appears to be
intelligent as it is able to pass the Turing test, but is in fact no more than
just a big look-up table of questions and answers (Block, 1981, for a related
argument see Gunderson, 1971). Although such a look-up table would be
unfeasibly large, the fact that a finite machine could in theory consistently pass
the Turing test, seemingly without any real intelligence, intuitively seems odd.
Our formal measure of machine intelligence could be challenged in the same
way, as could any test of intelligence that relies only on an agent’s external
behaviour.

Our response to this is very simple: if an agent has a very high value of
Υ then it is, by definition, able to successfully operate in a wide range of
environments. We simply do not care whether the agent is efficient, due to
some very clever algorithm, or absurdly inefficient, for example by using an
unfeasibly gigantic look-up table of precomputed answers. The important
point for us is that the machine has an amazing ability to solve a huge range
of problems in a wide variety of environments.

4. Universal Intelligence Measure

How do you respond to Searle’s “Chinese room” argument? Searle’s Chinese room argument attacks our functional position in a similar way by arguing that a system may appear to be intelligent without really understanding
anything (Searle, 1980). From our perspective, whether or not an agent understands what it is doing is only important to the extent that it affects the
measurable performance of the agent. If the performance is identical, as Searle
seems to suggest, then whether or not the room with Searle inside understands
the meaning of what is going on is of no practical concern; indeed, it is not
even clear to us how to define understanding if its presence has no measurable
effects. So long as the system as a whole has the powerful properties required
for universal machine intelligence, then we have the kind of extremely general
and powerful machine that we desire. On the other hand, if understanding
does have a measurable impact on an agent’s performance in some situations,
then it is of interest to us. In which case, because Υ measures performance in
all well defined situations, it follows that Υ is in part a measure of how much
understanding an agent has.

But you don’t deal with consciousness (or creativity, imagination, freewill,
emotion, love, soul, etc.) We apply the same argument to consciousness,
emotions, freewill, creativity, the soul and other such things. Our goal is to
build powerful and flexible machines and thus these somewhat vague properties
are only relevant to our goal to the extent to which they have some measurable
effect on performance in some well defined environment. If no such measurable
effect exists, then they are not relevant to our objective. Of course this is not
the same as saying that these things do not exist. The question is whether
they are relevant or not. We would consider understanding, imagination and
creativity, appropriately defined, to have a significant impact on an agent’s
ability to adapt to challenging environments. Perhaps the same is also true
of emotions, freewill and other qualities. If one accepts that these properties
affect an agent’s performance, then universal intelligence is in part a test for
these properties.

Intelligence is fundamentally an anthropocentric concept. As artificial intelligence researchers our goal is not to create an “artificial human”. We are
interested in making machines that are able to process information in powerful ways in order to achieve many kinds of goals and solve many kinds of
problems. As such, a limited anthropocentric concept of intelligence is not
interesting to us. Or at least, if such a definition were to be adopted, it would
simply mean that we are interested in something more general and powerful
than this human focused concept of “intelligence”.

Perhaps this is similar to the development of heavier than air flight. One
of the most outspoken sceptics of this was the American astronomer Simon
Newcomb. Interestingly, even after planes were regularly “flying” he refused
to accept defeat. He accepted that planes existed and moved around at great speed up in the air, however he did not accept that what they were doing was
“flying”. To his mind, what birds did was quite different. Of course, the rest
of the population simply generalised and adapted their concept of flying to
reflect the new technology.

We believe that with more progress in artificial intelligence the same thing
will eventually happen to the everyday concept of intelligence. At present,
most people think of intelligence in human terms simply because this is the
only kind of powerful intelligence they have ever encountered. Indeed, from the
perspective of evolutionary psychology, it appears that we may have evolved
to expect other intelligent agents to think and act like ourselves.

Universal intelligence does not agree with some everyday intuitions about
the nature of intelligence. Everyday intuitions are not a good guide. People
informally use the word “intelligence” to mean a variety of different things, and
even a single person will use the word in multiple ways that are not consistent
with each other. Thus, although our definition should clearly be related to the
everyday concept, it is not necessarily desirable, or even possible, for a precise
and self-consistent definition to always agree with everyday usage.

Consider a word that has both an everyday meaning and a precise technical
meaning. When someone says “It’s a beautiful spring day, I am full of energy
and could run up a mountain”, what they mean by the word ‘energy’ is related
to the concept of energy in physics, i.e. they need energy in the technical
sense to get up the mountain. However, the definition of energy from physics
does not entirely capture what they mean. This does not imply that there is
something wrong with the concept of energy in physics. We expect the same
in artificial intelligence: people will continue to use the word “intelligence” in
an informal way, however in order to do research we will need to adopt a more
precise definition that may be slightly different.

An agent may be intelligent even if it doesn’t achieve anything in any
environments. Consider, for example, that you are quietly sitting in a dark
room thinking about a problem you are trying to solve. Even though you are
not achieving anything in your environment, some would argue that you are
still intelligent due to your internal process of thought. Or imagine perhaps the
famous physicist Stephen Hawking disconnected from his motorised wheelchair
and talking computer. Although his ability to achieve goals in the environment
would be limited, he is still no doubt highly intelligent. A related problem is
that an agent may simply lack the motivation to exhibit intelligent behaviour,
such as a child who wants to get an IQ test out of the way as soon as possibly
in order to go outside and play. In both of these cases the agent’s intelligence
seems to be divorced from the intelligence observable in its behaviour.

The above highlights the fact that when informally considering the measurement of intelligence we need to be careful about exactly how the measurement
is done. Obviously, it only makes sense to measure an individual’s intelligence

4. Universal Intelligence Measure

if certain essential requirements are met: a purely written test for a blind
person is senseless, as are the results of a test where the test subject has no
interest in performing well. Informally, we just assume that the test has been
conducted in an appropriate way. When we say that an agent is intelligent,
what we actually mean is that there exists some reasonable setup such that
the agent exhibits a high level of intelligence: a blind person may require an
oral test, and a disinterested child some kind of a bribe. Clearly then, if we
want to be precise about the measured intelligence of an agent we must specify
these details about exactly how the test was conducted.

When we say that an agent has low intelligence, what we mean is that there
does not exist any reasonable test setup such that the agent exhibits intelligent
behaviour. Some take the position that an entity could be intelligent even if it
has no measurable intelligence under any test setup. However, such an agent’s
“intelligence” would be rather meaningless as it would be a property that has
no measurable effects or consequences. Even the philosophical “brain in a vat”
could in theory be interfaced to in order to measure its universal intelligence.

Such an agent is not intelligent because it cannot choose its goals. In the
setup we have defined the agent cannot decide what its primary goal is. It
simply tries to maximise the reward signal defined by the environment. In the
context of machines this is probably a good idea: we want to be the ones defining what the machine’s primary objective is. However, this does not address
the question as to whether such a machine should really be called intelligent,
or whether it is just a very powerful and general optimiser. Intelligent humans,
after all, can choose their own goals in life. But is this really true?

Obviously we can decide that we want to become a successful scientist, a
teacher, or maybe a rock star. So we certainly have some choice in our goals.
But are these things our primary motivations? If we want to be a successful
scientist or a rock star, perhaps this is due to a deeper biological drive to attain
high status because this increases our chances of reproductive success. Perhaps
the desire to become a teacher stems from a biological drive to care for children,
again because having this drive tends to increase our probability of passing on
our genes and memes to future generations. Our interest in mating with an
attractive member of the opposite sex, avoiding intense physical pain or the
pleasure of eating energy rich foods, all of these things have clear biological
motivations. Even a suicide bomber who kills himself and thus destroys his
future reproductive potential may be driven by an out-of-control biological
motivation that tries to increase his societal status in an effort to improve his
chances of reproductive success.

These ideas appear in areas such as evolutionary psychology and, it must
be said, attract a fair amount of controversy. Here we will not attempt to
defend them. We simply note that they offer one explanation as to how we
are able to choose our goals in life, while at the same time having relatively
fixed fundamental motivations.

Universal intelligence is impossible due to the No-Free-Lunch theorem.
Some, such as Edmonds (2006), argue that universal definitions of intelligence
are impossible due to Wolpert’s so called “No Free Lunch” theorem (Wolpert
and Macready, 1997). However this theorem, or any of the standard variants
on it, cannot be applied to universal intelligence for the simple reason that we
have not taken a uniform distribution over the space of environments. Instead
we have used a highly non-uniform distribution based on Occam’s razor.

It is conceivable that there might exist some more general kind of “No Free
Lunch” theorem for agents that limits their maximal intelligence according to
our definition. Clearly any such result would have to apply only to computable
agents given that the incomputable AIXI agent faces no such limit. If such a
result were true, it would suggest that our definition of intelligence is perhaps
too broad in its scope. Currently we know of no such result (c.f. Chapter 5).

### 4.5. Conclusion

Given the obvious significance of formal definitions of intelligence for research,
and calls for more direct measures of machine intelligence to replace the problematic Turing test and other imitation based tests (Johnson, 1992), little work
has been done in this area. In this chapter we have attempted to tackle this
problem by taking an informal definition of intelligence modelled on expert
definitions of human intelligence, and then formalising it. We believe that the
resulting mathematical definition captures the concept of machine intelligence
in a very powerful and elegant way. Furthermore, we have seen that agents
which are extremely intelligent with respect to this definition, such as AIXI,
can be proven to have powerful optimality properties.

The central challenge for future work on universal intelligence is to convert
this theoretical definition of machine intelligence into a workable test. The
basic structure of such a test is already apparent from the equation for Υ: the
test would work by evaluating the performance of an agent on a large sample
of simulated environments, and then combine the agent’s performance in each
environment into an overall intelligence value. This would be done by weighting the agent’s performance in each environment according the environment’s
complexity.

A theoretical challenge that will need to be dealt with is to find a suitable
replacement for the incomputable Kolmogorov complexity function. One solution could be to use Kt complexity (Levin, 1973), another might be to use
the Speed prior (Schmidhuber, 2002). Both of these consider the complexity
of an algorithm to be determined by both its minimal description length and
running time, thus forcing the complexity measures to be computable. Taking
computation time into account also makes reasonable intuitive sense because
we would not usually consider a very short algorithm that takes an enormous
amount of time to run to be a particularly simple one. The fact that such an
approach can be made to work is evidenced by the C-Test (see Section 1.7).

## 5. Limits of Computational Agents

One of the reasons for studying mathematical models such as AIXI is to gain
insights that may be useful for designing practical artificial intelligence agents.
The question then arises as to how useful all this incomputable theory really is.
In this chapter we will explore this question by looking at the theoretical limitations faced by computable sequence predictors that attempt to approximate
the power and generality of Solomonoff induction. As sequence prediction lies
at the heart of reinforcement learning, any limitations found here will carry
over to general computable agents.

As we saw in Chapter 2, sequence prediction and compression are intimately
related. Indeed, they are two different ways of looking at the same problem.
Intuitively, if you can accurately predict what is coming next you do not need
to use much information to encode what the data actually is, and vice versa.
For sequence predictors based on the Minimum Description Length (MDL)
principle (Rissanen, 1996) or the Minimum Message Length (MML) principle
(Wallace and Boulton, 1968), this connection is especially evident as they
predict by attempting to find the shortest possible description, or model, of the
data. Not surprisingly then, they can be viewed as computable approximations
of Solomonoff induction (Section 5.5 of Li and Vit´anyi, 1997). Furthermore,
in order to produce a working sequence predictor these methods can easily
be combined with general purpose data compressors, such as the Lempel-Ziv
algorithm (Feder et al., 1992) or Context Tree Weighting (Willems et al., 1995).
Unfortunately, while useful in practice, these real world compressors have their
limitations: they are able to find some kinds of computable regularities in
sequences, but not others. As such, predictors based on them fall short of the
power and generality of Solomonoff induction. Furthermore, even with ideal
compression MDL and MML based predictors can take exponentially longer
than Solomonoff induction to learn as they use only the shortest description of
the data, rather than the set of all possible descriptions (Poland and Hutter,
2004).

Can we do better than this? Do universal and computable predictors for
computable sequences exist? Unfortunately, it is easy to see that they do not:
simply consider a sequence where the next bit is always the opposite of what
the predictor predicts. This is essentially the same as what Dawid noted when
he found that for any statistical forecasting system there exist sequences for
which the predictor is not calibrated, and thus cannot be learnt (Dawid, 1985).
However, he does not deal with the complexity of the sequences themselves, nor
does he make a precise statement in terms of a specific measure of complexity.
The impossibility of forecasting has since been developed in considerably more depth by V’yugin (1998), in particular he proves that there is an efficient
randomised procedure producing sequences that cannot be predicted, with
high probability, by computable forecasting systems.

In this chapter we study the prediction of computable sequences from the
perspective of Kolmogorov complexity. The central question we look at is the
prediction of sequences which have bounded Kolmogorov complexity. This
leads us to a new notion of complexity: Rather than the length of the shortest program able to generate a given sequence, in other words standard Kolmogorov complexity, we take the length of the shortest program able to learn
to predict the sequence. This new complexity measure has the same fundamental invariance property as Kolmogorov complexity, and certain strong
relationships between the two measures are proven. Nevertheless, in some
cases the two can diverge significantly. For example, although a long random
string that indefinitely repeats has a very high Kolmogorov complexity, this
sequence also has a relatively simple structure that even a simple predictor
can learn to predict.

We then prove that some sequences can only be predicted by very complex
predictors. This implies that very general prediction algorithms, in particular
those that can learn to predict all sequences up to a given Kolmogorov complexity, must themselves be complex. This puts an end to our hope of there
being an extremely general and yet relatively simple prediction algorithm. We
then use this fact to prove that although very powerful prediction algorithms
exist, they cannot be mathematically discovered due to G¨odel incompleteness.
This significantly constrains our ability to design and analyse powerful prediction algorithms, and indeed powerful artificial intelligence algorithms in
general.

### 5.1. Preliminaries

For the basic notation for strings and sequences see Appendix A. In this
chapter we will sometimes need to encode a natural number as a string. Using
simple encoding techniques it can be shown that there exists a computable
injective function f : N → B∗ where no string in the range of f is a prefix of
any other, and ∀n ∈ N : ℓ(f (n)) ≤ log2 n + 2 log2 log2 n + 1 = O(log n).

$$
f:\mathbb{N}\to\mathbb{B}^*
$$

$$
\forall n\in\mathbb{N}:\ell(f(n))\leq\log_{2}n+2\log_{2}\log_{2}n+1=O(\log n)
$$

Of particular interest to us will be the class of sequences which can be
generated by an algorithm executed on the following type of machine:

5.1.1 Definition. A monotone universal Turing machine U is defined
as a universal Turing machine with one unidirectional input tape, one unidirectional output tape, and some bidirectional work tapes. Input tapes are read
only, output tapes are write only, unidirectional tapes are those where the head
can only move from left to right. All tapes are binary (no blank symbol) and
the work tapes are initially filled with zeros. We say that U outputs/computes
a sequence ω on input p, and write U (p) = ω, if U reads all of p but no more
as it continues to write ω to the output tape.

$$
p,
$$

$$
\mathcal{U}(p)=\omega
$$

We fix U and define U (p,x) by simply using a standard coding technique
to encode a program p along with a string x ∈ B∗ as a single input string for
U. For simplicity of notation we will often write p(x) to mean the function
computed by the program p when executed on U along with the input string
x, that is, p(x) is short hand for U (p,x).

$$
\mathcal{U}(p,x)
$$

$$
x\in\mathbb{B}^*
$$

$$
\mathcal{U}
$$

$$
p(x)
$$

$$
p
$$

$$
p(x)
$$

$$
\mathcal{U}(p,x)
$$

5.1.2 Definition. A sequence ω ∈ B∞ is a computable binary sequence
if there exists a program q ∈ B∗ that writes ω to a one-way output tape when
run on a monotone universal Turing machine U, that is, ∃q ∈ B∗: U (q) = ω.
We denote the set of all computable sequences by C.

$$
\omega\in\mathbb{B}^{\infty}
$$

$$
q\in\mathbb{B}^*
$$

$$
\omega
$$

$$
\mathcal{U},
$$

$$
\exists q\in\mathbb{B}^*:\mathcal{U}(q)=\omega
$$

A similar definition for strings is not necessary as all strings have finite
length and are therefore trivially computable: all an algorithm has to do is to
copy the desired string to the output tape and then halt.

5.1.3 Definition. A computable binary predictor is a program p ∈ B∗
that on a universal Turing machine U computes a total function B∗ → B.

$$
p\in\mathbb{B}^*
$$

$$
\mathbb{B}^{*}\to\mathbb{B}
$$

Having x1:n as input, the objective of a predictor is for its output, called
its prediction, to match the next symbol in the sequence. Formally we express
this by writing p(x1:n) = xn+1.

$$
x_{1:n}
$$

$$
p(x_{1:n})=x_{n+1}
$$

Note that this is different to earlier chapters where a predictor generated
a distribution over the possible symbols that might occur next, rather than
outputting the predicted symbol. What we consider here is a special case of
probabilistic prediction as it is equivalent to a probabilistic predictor that in
each cycle always assigns probability 1 to some symbol.

As the algorithmic prediction of incomputable sequences, such as the halting sequence, is impossible by definition, we only consider the problem of
predicting computable sequences. To simplify things we will assume that the
predictor has an unlimited supply of computation time and storage. We will
also make the assumption that the predictor has unlimited data to learn from,
that is, we are only concerned with whether or not a predictor can learn to
predict in the following sense:

5.1.4
sequence ω
p(x1:n) = x

Definition. We say that a predictor p can learn to predict a
:= x1x2... ∈ B∞ if there exists m ∈ N such that ∀n ≥ m :
n+1.

$$
p
$$

$$
\omega:=x_{1}x_{2}\cdots\in\mathbb{B}^{\infty}
$$

$$
m\in\mathbb{N}
$$

$$
\forall n\geq m
$$

$$
p(x_{1:n})=x_{n+1}
$$

The existence of m in the above definition need not be constructive, that is,
we might not know when the predictor will stop making prediction errors for
a given sequence, just that this will occur eventually. This is essentially “next
value” prediction as characterised by Barzdin (1972), which follows the notion
of identifiability in the limit for languages from Gold (1967).

$$
m
$$

5.1.5 Definition. Let P (ω) be the set of all predictors able ⋂to learn to
∞
predict ω. Similarly for sets of sequences S ⊂ B, define P (S) :=ω∈SP (ω).

$$
\mathcal{P}(\omega)
$$

$$
\omega
$$

$$
S\subset\mathbb{B}^{\infty}
$$

$$
\mathcal{P}(S):=\bigcap_{\omega\in S}\mathcal{P}(\omega)
$$

5. Limits of Computational Agents

A standard measure of complexity for sequences is the length of the shortest
program which generates the sequence:

5.1.6 Definition. For any sequence ω ∈ B∞ the Kolmogorov complexity
of the sequence is,

$$
\omega\in\mathbb{B}^{\infty}
$$

$$
K(\omega):=\min_{q\in\mathbb{B}^{*}}\left\{\ell(q):\mathcal{U}(q)=\omega\right\},
$$

where U is a monotone universal Turing machine. If no such q exists, we define
K(ω) := ∞.

$$
\mathcal{U}
$$

$$
q
$$

$$
K(\omega):=\infty
$$

In essentially the same way we can define the Kolmogorov complexity of a
string x ∈ Bn, written K(x), by requiring that U (q) halts after generating x
on the output tape.

$$
x\in\mathbb{B}^n
$$

$$
K(x)
$$

$$
\mathcal{U}(q)
$$

It can be shown that Kolmogorov complexity depends on our choice of universal Turing machine U, but only up to an additive constant that is independent of ω. This is due to the fact that a universal Turing machine can
simulate any other universal Turing machine with a fixed length program. For
more explanation see Section 2.4, or for an extensive treatment of Kolmogorov
complexity and some of its applications see (Li and Vit´anyi, 1997) or (Calude,
2002).

$$
\omega.
$$

### 5.2. Prediction of computable sequences

The most elementary result is that every computable sequence can be predicted
by at least one predictor, and that this predictor need not be significantly more
complex than the sequence to be predicted.

5.2.1 Lemma. ∀ω ∈C, ∃p ∈P (ω) : K(p) < K(ω).+

$$
\forall\omega\in\mathcal{C},\exists p\in\mathcal{P}(\omega):K(p)\leq K(\omega)
$$

Proof. As the sequence ω is computable, there must exist at least one
algorithm that generates ω. Let q be the shortest such algorithm and construct
an algorithm p that “predicts” ω as follows: Firstly the algorithm p reads x1:n
to find the value of n, then it runs q to generate x1:n+1 and returns xn+1 as its
prediction. Clearly p perfectly predicts ω and ℓ(p) < ℓ(q) + c, for some small
constant c that is independent of ω and q.

$$
\omega
$$

$$
q
$$

$$
x_{1:n}
$$

$$
n,
$$

$$
x_{1:n+1}
$$

$$
q
$$

$$
x_{n+1}
$$

$$
\omega
$$

$$
p
$$

$$
\ell(p)<\ell(q)+c,
$$

$$
\omega
$$

$$
q
$$

Not only can any computable sequence be predicted, there also exist very
simple predictors able to predict arbitrarily complex sequences:

5.2.2 Lemma. There exists a predictor p such that ∀n ∈ N, ∃ ω ∈ C : p ∈
P (ω) and K(ω) > n.

$$
\mathcal{P}(\omega)
$$

$$
\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}:p\in
$$

$$
K(\omega)>n
$$

Proof. Take a string x such that K(x) = ℓ(x) ≥ 2n, and from this define a
sequence ω := x0000.... Clearly K(ω) > n and yet a simple predictor p that
always predicts 0 can learn to predict ω.

$$
K(x)=\ell(x)\geq2n
$$

$$
\omega:=x0000\ldots
$$

$$
K(\omega)>n
$$

$$
\omega
$$

The predictor used in the above proof is very simple and can only “learn”
sequences that end with all 0’s, albeit where the initial string can have arbitrarily high Kolmogorov complexity. It may seem that this is due to sequences that are initially complex but where the “tail complexity”, defined
lim infi→∞K(ωi:∞), is zero. This is not the case:

$$
0^{\prime}\mathrm{s}
$$

$$
\operatorname{nf}_{i\to\infty}K(\omega_{i:\infty})
$$

### 5.2.3 Lemma. P (ω) and lim inf

There exists a predictor p such that ∀n ∈ N, ∃ ω ∈ C : p ∈ i→∞K(ωi:∞) > n.

$$
\mathcal{P}(\omega)
$$

$$
\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}:p\in
$$

$$
\mathrm{f}_{i\to\infty}K(\omega_{i:\infty})>n
$$

Proof. A predictor p for eventually periodic sequences can be defined
as follows: On input ω1:k the predictor goes through the ordered pairs
(1, 1), (1, 2), (2, 1), (1, 3), (2, 2), (3, 1), (1, 4),... checking for each pair (a,b)
whether the string ω1:k consists of an initial string of length a followed by
a repeating string of length b. On the first match that is found p predicts that
the repeating string continues, and then p halts. If a + b > k before a match
is found, then p outputs a fixed symbol and halts. Clearly K(p) is a small
constant and p will learn to predict any sequence that is eventually periodic.

$$
p
$$

$$
\omega_{1:k}
$$

$$
(1,1),(1,2),(2,1),(1,3),(2,2),(3,1),(1,4),\ldots
$$

$$
\omega_{1:k}
$$

$$
a+b>k
$$

For any (m,n) ∈ N2, let ω := x(y∗) where x ∈ Bm, and y ∈ Bn is a random
string, that is, K(y) = n. As ω is eventually periodic p ∈P (ω) and also we see
that lim infi→∞K(ωi:∞) = min{K(ωm+1:∞),K(ωm+2:∞),...,K(ωm+n:∞)}.

$$
(m,n)\in\mathbb{N}^2
$$

$$
\omega:=x(y^*)
$$

$$
x\in\mathbb{B}^m
$$

$$
y\in\mathbb{B}^n
$$

$$
K(y)=n
$$

$$
p\in\mathcal{P}(\omega)
$$

$$
\inf_{i\to\infty}K(\omega_{i:\infty})=\operatorname*{m i n}\{K(\omega_{m+1:\infty}),K(\omega_{m+2:\infty}),\ldots,K(\omega_{m+n:\infty})\}
$$

For any k ∈ {1,...,n}
ate ωm+k:∞. We can define
this program consists of q
K(ωk:∞)+O(log n). As n = K(y) ≤ ℓ(q
As n and k are arbitrary the result follows.

let qk∗ be
a halting
k∗, n and k.

the shortest
program
Thus, ℓ(q
k′), we see that K(ω

program that can generqk′ that outputs y where
k′) = ℓ(qk∗) + O(log n) =
k:∞) > n−O(log n).

$$
k\;\in\;\{1,\ldots,n\}
$$

$$
q_{k}^{*}
$$

$$
q_{k}^{\prime}
$$

$$
\omega_{m+k:\infty}
$$

$$
q_{k}^{*}
$$

$$
\ell(q_{k}^{\prime})=\ell(q_{k}^{*})+O(\log n)
$$

$$
K(\omega_{k:\infty})+O(\log n)
$$

$$
n=K(y)\leq\ell(q_k')
$$

$$
K(\omega_{k:\infty})>n-O(\log n)
$$

Using a more sophisticated version of this proof it can be shown that there
exist predictors that can learn to predict arbitrary regular or primitive recursive sequences. Thus we might wonder whether there exists a computable
predictor able to learn to predict all computable sequences. Unfortunately, no
universal predictor exists, indeed for every predictor there exists a sequence
which it cannot predict at all:

5.2.4 Lemma. For any predictor p there constructively exists a sequence
+
ω := x1x2... ∈C such that ∀n ∈ N : p(x1:n) = xn+1 and K(ω) < K(p).

$$
\omega:=x_{1}x_{2}\ldots\in\mathcal{C}
$$

$$
\forall n\in\mathbb{N}:p(x_{1:n})\neq x_{n+1}
$$

$$
K(\omega)\stackrel{\mp}{<}K(p)
$$

Proof. For any computable predictor p there constructively exists a computable sequence ω = x1x2x3... computed by an algorithm q defined as follows: Set x1 = 1 − p(λ), then x2 = 1 − p(x1), then x3 = 1 − p(x1:2) and so on.
Clearly ω ∈C and ∀n ∈ N : p(x1:n) = 1 − xn+1.

$$
x_{1}=1-p(\lambda)
$$

$$
\omega=x_{1}x_{2}x_{3}\ldots
$$

$$
x_{2}=1-p(x_{1})
$$

$$
x_{3}=1-p(x_{1:2})
$$

$$
\omega\in\mathcal{C}
$$

$$
\forall n\in\mathbb{N}:p(x_{1:n})=1-x_{n+1}
$$

Let p∗ be the shortest program that computes the same function as p and
define a sequence generation algorithm q∗ based on p∗ using the procedure
above. By construction, ℓ(q∗) = ℓ(p∗) + c for some constant c that is independent of p∗. Because q∗ generates ω, it follows that K(ω) ≤ ℓ(q∗). By definition
+
K(p) = ℓ(p∗) and so K(ω) < K(p).

$$
p^{*}
$$

$$
q^{*}
$$

$$
p^{*}
$$

$$
\ell(q^*)=\ell(p^*)+c
$$

$$
p^{*}
$$

$$
q^{*}
$$

$$
\omega
$$

$$
K(\omega)\leq\ell(q^{*})
$$

$$
K(p)=\ell(p^*)
$$

$$
K(\omega)\stackrel{+}{<}K(p)
$$

5. Limits of Computational Agents

Allowing the predictor to be probabilistic, as we did in previous chapters,
does not fundamentally avoid the problem of Lemma 5.2.4. In each step, rather
than generating the opposite to what will be predicted by p, instead q attempts
to generate the symbol that p is least likely to predict given x1:n. To do this
q must simulate p in order to estimate the probability that p(x1:n) = 1. With
sufficient simulation effort, q can estimate this probability to any desired accuracy for any x1:n. This produces a computable sequence ω such that ∀n ∈ N
the probability that p(x1:n) = xn+1 is not significantly greater than 1/2, that
is, the performance of p is no better than a predictor that makes completely
random predictions. As probabilistic prediction complicates things without
avoiding this problem, in this chapter we will consider only deterministic predictors. This will also allow us to see the root of this problem as clearly as
possible.

$$
p,
$$

$$
p
$$

$$
x_{1:n}
$$

$$
p
$$

$$
p(x_{1:n})=1
$$

$$
x_{1:n}
$$

$$
\omega
$$

$$
\forall n\in\mathbb{N}
$$

$$
p(x_{1:n})=x_{n+1}
$$

$$
\frac{1}{2}
$$

With the preliminaries covered, we now move on to the central problem:
predicting sequences of limited Kolmogorov complexity.

### 5.3. Prediction of simple computable sequences

As the computable prediction of any computable sequence is impossible, a
weaker goal is to be able to predict all “simple” computable sequences.

5.3.1 Definition. For n ∈ N, let Cn:= {ω ∈C : K(ω) ≤ n}. Further, let
Pn:= P (Cn) be the set of predictors able to learn to predict all sequences in
Cn.

$$
\mathcal{C}_{n}:=\{\omega\in\mathcal{C}:K(\omega)\leq n\}
$$

$$
n\in\mathbb{N}
$$

$$
\mathcal{P}_{n}:=\mathcal{P}(\mathcal{C}_{n})
$$

$$
\mathcal{C}_{n}
$$

Firstly, we establish that prediction algorithms exist that can learn to predict
all sequences up to a given complexity, and that these predictors need not be
significantly more complex than the sequences they can predict:

+ 5.3.2 Lemma. ∀n ∈ N, ∃p ∈Pn: K(p) < n + O(log n).

$$
\forall n\in\mathbb{N},\exists p\in\mathcal{P}_{n}:K(p)\stackrel{\pm}{<}n+O(\log n)
$$

Proof. Let h ∈ N be the number of programs of length n or less which
generate infinite sequences. Build the value of h into a prediction algorithm p
constructed as follows:

$$
h\in\mathbb{N}
$$

In the kth prediction cycle run in parallel all programs of length n or less until
h of these programs have each produced k + 1 symbols of output. Next predict
according to the k + 1th symbol of the generated string whose first k symbols
is consistent with the observed string. If more than one generated string is
consistent with the observed sequence, pick the one which was generated by
the program that occurs first in a lexicographical ordering of the programs. If
no generated output is consistent, give up and output a fixed symbol.

$$
k^{th}
$$

$$
k+1^{th}
$$

For sufficiently large k, only the h programs which produce infinite sequences
will produce output strings of length k + 1. As this set of sequences is finite,
they can be uniquely identified by finite initial strings. Thus, for sufficiently large k, the predictor p will correctly predict any computable sequence ω for
which K(ω) ≤ n, that is, p ∈Pn.

$$
\omega
$$

$$
K(\omega)\leq n
$$

$$
p\in\mathcal{P}_n
$$

As there are 2n+1 − 1 possible strings of length n or less, h < 2n+1 and thus
we can encode h with log2 h + 2 log2 log2 h = n + 1 + 2 log2(n + 1) bits. Thus,
K(p) < n + 1 + 2 log2(n + 1) + c for some constant c that is independent of
n.

$$
2^{n+1}-1
$$

$$
h<2^{n+1}
$$

$$
\log_{2}h+2\log_{2}\log_{2}h=n+1+2\log_{2}(n+1)
$$

$$
K(p)<n+1+2\log_2(n+1)+c
$$

Can we do better than this? Lemmas 5.2.2 and 5.2.3 show us that there
exist predictors able to predict at least some sequences vastly more complex
than themselves. This suggests that there might exist simple predictors able
to predict arbitrary sequences up to a high complexity. Formally, could there
exist p ∈ Pn where n ≫ K(p)? Unfortunately, these simple but powerful
predictors are not possible:

$$
p\in\mathcal{P}_n
$$

$$
n\gg K(p)?
$$

+ 5.3.3 Theorem. ∀n ∈ N : p ∈Pn ⇒ K(p) > n.

$$
\forall n\in\mathbb{N}:p\in\mathcal{P}_n\Rightarrow K(p)\stackrel{+}{>}n.
$$

Proof. For any n ∈ N let p ∈ Pn, that is, ∀ω ∈ Cn: p ∈ P (ω). By
Lemma 5.2.4 we know that ∃ ω′ ∈C : p /∈P (ω′) . As p /∈P (ω′) it must be the
case that ω′ ∈C / n, that is, K(ω′) ≥ n. From Lemma 5.2.4 we also know that
+
K(p) > K(ω′) and so the result follows.

$$
n\in\mathbb{N}
$$

$$
p\in\mathcal{P}_n
$$

$$
\forall\omega\in\mathcal{C}_n:p\in\mathcal{P}(\omega)
$$

$$
\exists\omega^{\prime}\in\mathcal{C}:p\notin\mathcal{P}(\omega^{\prime})
$$

$$
p\notin\mathcal{P}(\omega')
$$

$$
\omega^{\prime}\notin\mathcal{C}_{n}
$$

$$
K(\omega')\geq n
$$

$$
K(p)\stackrel{+}{>}K(\omega')
$$

Intuitively the reason for this is as follows: Lemma 5.2.4 guarantees that
every simple predictor fails for at least one simple sequence. Thus, if we want
a predictor that can learn to predict all sequences up to a moderate level of
complexity, then clearly the predictor cannot be simple. Likewise, if we want a
predictor that can predict all sequences up to a high level of complexity, then
the predictor itself must be very complex. Even though we have made the
generous assumption of unlimited computational resources and data to learn
from, only very complex algorithms can be truly powerful predictors.

These results easily generalise to notions of complexity that take computation time into consideration. As sequences are infinite, the appropriate measure of time is the time needed to generate or predict the next symbol in the
sequence. Under any reasonable measure of time complexity, the operation of
inverting a single output from a binary valued function can be performed with
little cost. If C is any complexity measure with this property, it is trivial to
see that the proof of Lemma 5.2.4 still holds for C. From this, an analogue of
Theorem 5.3.3 for C easily follows.

With similar arguments these results also generalise, in a straightforward
way, to complexity measures that take space or other computational resources
into account. Thus, the fact that extremely powerful predictors must be very
complex, holds under any measure of complexity for which inverting a single
bit is inexpensive.

### 5.4. Complexity of prediction

Another way of viewing these results is in terms of an alternate notion of
sequence complexity defined as the size of the smallest predictor able to learn
to predict the sequence. This allows us to express the results of the previous
sections more concisely. Formally, for any sequence ω define the complexity
measure,
K˙ (ω) := min { ℓ(p) : p ∈P (ω)},

$$
\omega
$$

$$
\dot{K}(\omega):=\min_{p\in\mathbb{B}^{*}}\left\{\ell(p):p\in\mathcal{P}(\omega)\right\},
$$

and K˙ (ω) := ∞ if P (ω) = ∅. Thus, if K˙ (ω) is high then the sequence ω is
complex in the sense that only complex prediction algorithms are able to learn
to predict it. It can easily be seen that this notion of complexity has the same
invariance to the choice of reference universal Turing machine as the standard
Kolmogorov complexity measure.

$$
\dot{K}(\omega):=\infty if\mathcal{P}(\omega)=\varnothing
$$

$$
\dot{K}(\omega)
$$

$$
\omega
$$

It may be tempting to conjecture that this definition simply describes what
might be called the “tail complexity” of a sequence, that is, K˙ (ω) is equal to
lim infi→∞K(ωi:∞). This is not the case. In the proof of Lemma 5.2.3 we saw
that there exists a single predictor capable of learning to predict any sequence
that consists of a repeating string, and thus for these sequences K˙ is bounded.
It was further shown that there exist sequences of this form with arbitrarily
high tail complexity. Clearly then tail complexity and K˙ cannot be equal in
general.

$$
\dot{K}(\omega)
$$

$$
\operatorname{f}_{i\to\infty}K(\omega_{i:\infty})
$$

$$
\dot{K}
$$

Using K˙ we can now rewrite a number of our previous results much more
succinctly. From Lemma 5.2.1 it immediately follows that,

$$
\dot{K}
$$

$$
\forall\omega:0\leq\dot{K}(\omega)\stackrel{+}{<}K(\omega).
$$

From Lemma 5.2.2 we know that ∃c ∈ N, ∀n ∈ N, ∃ ω ∈C such that K˙ (ω) < c
and K(ω) > n, that is, K˙ can attain the lower bound above within a small
constant, no matter how large the value of K is. The sequences for which the
upper bound on K˙ is tight are interesting as they are the ones which demand
complex predictors. We prove the existence of these sequences and look at
some of their properties in the next section.

$$
\exists c\in\mathbb{N},\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}
$$

$$
K(\omega)>n
$$

$$
\dot{K}(\omega)<c
$$

$$
\dot{K}
$$

$$
\dot{K}
$$

The complexity measure K˙ can also be generalised to sets of sequences, for
∞
S⊂B define K˙ (S) := minp { ℓ(p) : p ∈P (S)}. This allows us to rewrite
Lemma 5.3.2 and Theorem 5.3.3 as simply,

$$
\dot{K}
$$

$$
S\subset\mathbb{B}^{\infty}
$$

$$
\dot{K}(S):=\min_{p}\left\{\ell(p):p\in\mathcal{P}(S)\right\}
$$

$$
\forall n\in\mathbb{N}\::\:n\:\stackrel{+}{<}\dot{K}(\mathcal{C}_{n})\:\stackrel{+}{<}\:n+O(\log n).
$$

This is just a restatement of the fact that the simplest predictor capable of
predicting all sequences up to a Kolmogorov complexity of n, has itself a
Kolmogorov complexity of roughly n.

$$
n,
$$

Perhaps the most surprising thing about K˙ complexity is that this very natural definition of the complexity of a sequence, as viewed from the perspective
of prediction, does not appear to have been studied before.

$$
\dot{K}
$$

### 5.5. Hard to predict sequences

We have already seen that some individual sequences, such as the repeating
string used in the proof of Lemma 5.2.3, can have arbitrarily high Kolmogorov
complexity but nevertheless can be predicted by trivial algorithms. Thus,
although these sequences contain a lot of information in the Kolmogorov sense,
in a deeper sense their structure is very simple and easily learnt.

What interests us in this section is the other extreme: individual sequences
that can only be predicted by complex predictors. As we are concerned with
prediction in the limit, this extra complexity in the predictor must be some
kind of special information which cannot be learnt through observing the sequence. Our first task is to show that these hard to predict sequences exist.

$$
\mathbf{5.5.1}\quad\mathbf{T h e o r e m.}\quad\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}\quad:\quad n\quad\stackrel{+}{<}\quad\dot{K}(\omega)\quad\stackrel{+}{<}\quad K(\omega)\quad\stackrel{+}{<}\quad n+O(\log n).
$$

<n
Proof. For any n ∈ N, let Qn ⊂ B be the set of programs shorter than n
that are predictors, and let x1:k ∈ Bk be the observed initial string from the
sequence ω that is to be predicted. Now construct a meta-predictor pˆ:

$$
n\in\mathbb{N}
$$

$$
Q_{n}\subset\mathbb{B}^{<n}
$$

$$
x_{1:k}\in\mathbb{B}^k
$$

$$
\hat{p}\hat{:}
$$

By dovetailing the computations, run in parallel every program of length
less than n on every string in B≤k. Each time a program is found to halt on
all of these input strings, add the program to a set of “candidate prediction
algorithms”, called Q˜kn. As each element of Qn is a valid predictor, and thus
halts for all input strings in B∗ by definition, for every n and k it eventually
will be the case that |Q˜kn| = |Qn|. At this point the simulation to approximate
Qn terminates. It is clear that for sufficiently large values of k all of the valid
predictors, and only the valid predictors, will halt with a single symbol of
output on all tested input strings. That is, ∃r ∈ N, ∀k > r : Q˜kn = Qn.

$$
\mathbb{B}^{\leq k}
$$

$$
\tilde{Q}_{n}^{k}
$$

$$
Q_{n}
$$

$$
\mathbb{B}^*
$$

$$
\left|\widetilde{Q_{n}^{k}}\right|=\left|Q_{n}\right|
$$

$$
Q_{n}
$$

$$
\exists r\in\mathbb{N},\forall k>r:\tilde{Q}_n^k=Q_n
$$

The second part of the pˆ algorithm uses these candidate prediction algo-
∑k−1
rithms to make a prediction. For p ∈ Q˜kn define dk(p) := |p(x1:i) − xi+1|.
i=1
Informally, dk(p) is the number of prediction errors made by p so far. Compute this for all p ∈ Q˜kn and then let p∗k ∈ Q˜kn be the program with minimal
dk(p). If there is more than one such program, break the tie by letting p∗k be
the lexicographically first of these. Finally, pˆ computes the value of p∗k(x1:k)
and then returns this as its prediction and halts.

$$
\hat{p}
$$

$$
p\in\tilde{Q}_n^k
$$

$$
d^{k}(p):=\sum_{i=1}^{k-1}\left|p(x_{1:i})-x_{i+1}\right|
$$

$$
d^{k}(p)
$$

$$
p\in\tilde{Q}_n^k
$$

$$
p_{k}^{*}\in\tilde{Q}_{n}^{k}
$$

$$
d^{k}(p)
$$

$$
p_{k}^{*}
$$

$$
\hat{p}
$$

$$
p_{k}^{*}(x_{1:k})
$$

By Lemma 5.2.4, there exists ω′ ∈C such that pˆ makes a prediction error
for every k when trying to predict ω′. Thus, in each cycle at least one of
the finitely many predictors with minimal dk makes a prediction error and
so ∀p ∈ Qn: dk(p) → ∞ as k → ∞. Therefore, ∄p ∈ Qn: p ∈ P (ω′),
that is, no program of length less than n can learn to predict ω′ and so n ≤
+
K˙ (ω′). Further, from Lemma 5.2.1 we know that K˙ (ω′) < K(ω′), and from
+
Lemma 5.2.4 again, K(ω′)<K(ˆp).

$$
\omega^{\prime}\in\mathcal{C}
$$

$$
\hat{p}
$$

$$
\omega^{\prime}
$$

$$
d^{k}
$$

$$
\forall p\in Q_n:d^k(p)\to\infty
$$

$$
\exists p\in Q_n:p\in\mathcal{P}(\omega')
$$

$$
k\to\infty
$$

$$
\dot{K}(\omega')
$$

$$
n\leq
$$

$$
\omega^{\prime}
$$

$$
\dot{K}(\omega')\stackrel{+}{<}K(\omega')
$$

$$
K(\omega^{\prime})\overset{+}{<}K(\hat{p})
$$

Examining the algorithm for pˆ, we see that it contains some fixed length
program code and an encoding of |Qn|, where |Qn|<2n − 1. Thus, using a
standard encoding method for integers, K(ˆp) < n + O(log n). Chaining these,+
+ + + +
n < K˙ (ω′) < K(ω′)<K(ˆp) < n + O(log n), which proves the theorem.

$$
\hat{p},
$$

$$
\left|Q_{n}\right|
$$

$$
\left|Q_{n}\right|<2^{n}-1
$$

$$
K(\hat{p})\stackrel{+}{<}n+O(\log n)
$$

$$
n\stackrel{\pm}{<}\dot{K}(\omega')\stackrel{\pm}{<}K(\omega')\stackrel{\pm}{<}K(\hat{p})\stackrel{\pm}{<}n+O(\log n)
$$

5. Limits of Computational Agents

This establishes the existence of sequences with arbitrarily high K˙ complexity which also have a similar level of Kolmogorov complexity. Next we
establish a fundamental property of high K˙ complexity sequences: they are
extremely difficult to compute.

$$
\dot{K}
$$

$$
\dot{K}
$$

For an algorithm q that generates ω ∈C, define tq(n) to be the number of
computation steps performed by q before the nth symbol of ω is written to the
output tape. For example, if q is a simple algorithm that outputs the sequence
010101..., then clearly tq(n) = O(n) and so ω can be computed quickly. The
following theorem proves that if a sequence can be computed in a reasonable
amount of time, then the sequence must have a low K˙ complexity:

$$
q
$$

$$
\omega\in\mathcal{C}
$$

$$
t_{q}(n)
$$

$$
q
$$

$$
n^{th}
$$

$$
\omega
$$

$$
q
$$

$$
010101\ldots
$$

$$
t_{q}(n)=O(n)
$$

$$
\omega
$$

$$
\dot{K}
$$

5.5.2 Lemma. ∀ω ∈C, if ∃q : U (q) = ω and ∃r ∈ N, ∀n > r : tq(n) < 2n,
then K˙ (ω) = 0.+

$$
\forall\omega\in\mathcal{C},\quad\exists q:\mathcal{U}(q)=\omega\quad and\quad\exists r\in\mathbb{N},\forall n>r:t_q(n)<2^n.
$$

$$
\dot{K}(\omega)\stackrel{+}{=}0
$$

Proof. Construct a prediction algorithm p˜ as follows:

$$
\tilde{p}
$$

On input x1:n, run all programs of length n or less, each for 2n+1 steps. In
a set Wn collect together all generated strings which are at least n + 1 symbols
long and where the first n symbols match the observed string x1:n. Now order
the strings in Wn according to a lexicographical ordering of their generating
programs. If Wn = ∅, then just return a prediction of 1 and halt. If |Wn|>1
then return the n + 1th symbol from the first sequence in the above ordering.

$$
x_{1:n}
$$

$$
2^{n+1}
$$

$$
n
$$

$$
W_{n}
$$

$$
n+1
$$

$$
x_{1:n}
$$

$$
W_{n}
$$

$$
\left|W_{n}\right|>1
$$

$$
W_{n}=\varnothing
$$

$$
n+1^{th}
$$

Assume that ∃q : U (q) = ω such that ∃r ∈ N, ∀n > r : tq(n) < 2n. If q is
not unique, take q to be the lexicographically first of these. Clearly ∀n > r
the initial string from ω generated by q will be in the set Wn. As there
is no lexicographically lower program which can generate ω within the time
constraint tq(n) < 2n for all n > r, for sufficiently large n the predictor ˜p must
converge on using q for each prediction and thus p˜ ∈P (ω). As ℓ(˜p) is clearly
a fixed constant that is independent of ω, it follows then that K˙ (ω) < ℓ(˜p) =+
0.

$$
q
$$

$$
\exists q:\mathcal{U}(q)=\omega
$$

$$
\exists r\in\mathbb{N},\forall n>r:t_q(n)<2^n
$$

$$
\forall n>r
$$

$$
q
$$

$$
W_{n}
$$

$$
\omega
$$

$$
\omega
$$

$$
t_{q}(n)<2^{n}
$$

$$
n>r
$$

$$
\tilde{p}
$$

$$
q
$$

$$
\tilde{p}\in\mathcal{P}(\omega)
$$

$$
\ell(\tilde{p})
$$

$$
\omega
$$

$$
\dot{K}(\omega)<\ell(\tilde{p})\stackrel{+}{=}
$$

$$
0
$$

We could replace the 2n bound in the above result with any monotonically
growing computable function, for example, 22n. In any case, this does not
change the fundamental result that sequences which have a high K˙ complexity
are practically impossible to compute. However, from our theoretical perspective, these sequences present no problem as they can be predicted, albeit with
immense difficulty.

$$
2^{n}
$$

$$
2^{2^{n}}
$$

$$
\dot{K}
$$

### 5.6. The limits of mathematical analysis

One way to interpret the results of the previous sections is in terms of constructive theories of prediction. Essentially, a constructive theory of prediction
expressed in some sufficiently rich formal system F, is in effect a description
of a prediction algorithm with respect to a universal Turing machine which
implements the required parts of F. Thus, from Theorems 5.3.3 and 5.5.1,
it follows that if we want to have a predictor that can learn to predict all

$$
\mathfrak{F}
$$

$$
\mathfrak{F}.
$$ sequences up to a high level of Kolmogorov complexity, or even just predict
individual sequences which have high K˙ complexity, the constructive theory of
prediction that we base our predictor on must be very complex. Elegant and
highly general constructive theories of prediction simply do not exist, even if
we assume unlimited computational resources. This is in marked contrast to
Solomonoff’s highly elegant but non-constructive theory of prediction.

$$
\dot{K}
$$

Naturally, highly complex theories of prediction will be very difficult to
mathematically analyse, if not practically impossible. Thus, at some point
the development of very general prediction algorithms must become mainly
an experimental endeavour due to the difficulty of working with the required
theory. Interestingly, an even stronger result can be proven showing that
beyond some point the mathematical analysis is in fact impossible, even in
theory:

5.6.1 Theorem. In any consistent formal axiomatic system F that is sufficiently rich to express statements of the form “p ∈Pn”, there exists m ∈ N
such that for all n > m and for all predictors p ∈ Pn the true statement
“p ∈Pn” cannot be proven in F.

$$
\mathfrak{F}
$$

$$
suf\bar{f}\bar{h}
$$

$$
“ p \in \mathcal {P} _ {n} ”
$$

$$
m\in\mathbb{N}
$$

$$
n>m
$$

$$
p\in\mathcal{P}_n
$$

$$
``\mathit{p}\in\mathcal{P}_{\mathit{n}}''
$$

$$
\mathfrak{F}
$$

In other words, even though we have proven that very powerful sequence
prediction algorithms exist, beyond a certain complexity it is impossible to
find any of these algorithms using mathematics. The proof has a similar
structure to Chaitin’s information theoretic proof (Chaitin, 1982) of G¨odel’s
incompleteness theorem for formal axiomatic systems (G¨odel, 1931).

Proof. For each n ∈ N let Tn be the set of statements expressed in the
formal system F of the form “p ∈Pn”, where p is filled in with the complete
description of some algorithm in each case. As the set of programs is denumerable, Tn is also denumerable and each element of Tn has finite length. From
Lemma 5.3.2 and Theorem 5.3.3 it follows that each Tn contains infinitely
many statements of the form “p ∈Pn” which are true.

$$
T_{n}
$$

$$
n\in\mathbb{N}
$$

$$
\mathfrak{F}
$$

$$
``p\in\mathcal{P}_n''
$$

$$
T_{n}
$$

$$
T_{n}
$$

$$
T_{n}
$$

$$
``p\in\mathcal{P}_n''
$$

Fix n and create a search algorithm s that enumerates all proofs in the
formal system F searching for a proof of a statement in the set Tn. As the set
Tn is recursive, s can always recognise a proof of a statement in Tn. If s finds
any such proof, it outputs the corresponding program p and then halts.

$$
\mathfrak{F}
$$

$$
T_{n}
$$

$$
T_{n}
$$

$$
T_{n}
$$

By way of contradiction, assume that s halts, that is, a proof of a theorem
in Tn is found and p such that p ∈ Pn is generated as output. The size of
the algorithm s is a constant (a description of the formal system F and some
proof enumeration code) as well as an O(log n) term needed to describe n. It
follows then that K(p) < O(log n).+ However, from Theorem 5.3.3 we know
that K(p) > n.+ Thus, for sufficiently large n, we have a contradiction and
so our assumption of the existence of a proof must be false. That is, for
sufficiently large n and for all p ∈Pn, the true statement “p ∈Pn” cannot be
proven within the formal system F.

$$
p\in\mathcal{P}_n
$$

$$
T_{n}
$$

$$
\mathfrak{F}
$$

$$
K(p)\stackrel{+}{<}O(\log n)
$$

$$
K(p)\stackrel{+}{>}n
$$

$$
p\in\mathcal{P}_n
$$

$$
``p\in\mathcal{P}_n''
$$

$$
\mathfrak{F}
$$

5. Limits of Computational Agents

The exact value of m depends on our choice of formal system F and which
reference machine U we measure complexity with respect to. However, for
reasonable choices of F and U the value of m would be in the order of 1000.
That is, the bound m is certainly not so large as to be vacuous.

$$
\mathfrak{F}
$$

$$
\mathfrak{F}
$$

### 5.7. Conclusion

We have shown that there does not exist an elegant constructive theory of
prediction for computable sequences, even if we assume unbounded computational resources, unbounded data and learning time, and place moderate
bounds on the Kolmogorov complexity of the sequences to be predicted. Very
powerful computable predictors are therefore necessarily complex. We have
further shown that the source of this problem is the existence of computable
sequences which are extremely expensive to compute. While we have proven
that very powerful prediction algorithms which can learn to predict these sequences exist, we have also proven that, unfortunately, mathematical analysis
cannot be used to discover these algorithms due to G¨odel incompleteness.

These results can be extended to more general settings, specifically to those
problems which are equivalent to, or depend on, sequence prediction. Consider,
for example, a reinforcement learning agent interacting with an environment,
as described in Chapters 2 and 3. In each interaction cycle the agent must
choose its actions so as to maximise the future rewards that it receives from
the environment. Of course the agent cannot know for certain if some action
will lead to rewards in the future. Whether explicitly or implicitly, it must
somehow predict these. Thus, at the heart of reinforcement learning lies a
prediction problem, and so the results for computable predictors presented in
this paper also apply to computable reinforcement learners. More specifically,
from Theorem 5.3.3 it follows that very powerful computable reinforcement
learners are necessarily complex, and from Theorem 5.6.1 it follows that it is
impossible to discover any of these extremely powerful reinforcement learning
algorithms mathematically. These relationships are illustrated in Figure 5.1.

It is reasonable to ask whether the assumptions we have made in our model
need to be changed. If we increase the power of the predictors further, for
example by providing them with some kind of an oracle, this would make the
predictors even more unrealistic than they currently are. This goes against
our goal of finding an elegant, powerful and general prediction theory that is
more realistic in its assumptions than Solomonoff’s incomputable model. On
the other hand, if we weaken our assumptions about the predictors’ resources
to make them more realistic, we are in effect taking a subset of our current
class of predictors. As such, all the same limitations and problems will still
apply, as well as some new ones.

It seems then that the way forward is to further restrict the problem space.
One possibility would be to bound the amount of computation time needed to
generate the next symbol in the sequence. However, if we do this without re- stricting the predictors’ resources then the simple predictor from Lemma 5.5.2
easily learns to predict any such sequence and thus the problem of prediction
in the limit has become trivial. Another possibility might be to bound the
memory of the machine used to generate the sequence, however this makes the
generator a finite state machine and thus bounds its computation time, again
making the problem trivial.

Perhaps the only reasonable solution would be to add additional restrictions
to both the algorithms which generate the sequences to be predicted, and to
the predictors. We may also want to consider not just learnability in the limit,
but also how quickly the predictor is able to learn. Of course we are then
facing a much more difficult analysis problem.

Powerful AI

Impossible Algorithms

Powerful but unprovable algorithms

Upper bound on performance of provable algorithms

Gödel Incompleteness

Weak provable algorithms

Weak AI

Simple Algorithms

Complex Algorithms

Figure 5.1.: Theorem 5.3.3 rules out simple but powerful artificial intelligence
algorithms, as indicated by the greyed out region in the upper
left. Theorem 5.6.1 upper bounds how powerful an algorithm can
be before it can no longer be proven to be a powerful algorithm.
This is indicated by the horizontal line separating the region of
provable algorithms from the region of G¨odel incompleteness.

## 6. Temporal Difference Updating without a Learning Rate

In Chapters 2 and 3 we saw how universal agents are able to learn to behave
optimally across a wide range of environments. Unfortunately, these agents
are incomputable as they are based on incomputable universal prior distributions. Thus, in order to use the theory of universal artificial intelligence to
design and build practical algorithms, we must first find a way to scale the
theory down. In Chapter 5 we investigated some of the constraints faced when
attempting this. What we uncovered was a number of fundamental negative
results. In short, computable predictors capable of predicting all sequences up
to a moderate Kolmogorov complexity are both highly complex and mathematically impossible to find due to G¨odel incompleteness. The only way out
of this bind, it seems, is to move to a more sophisticated measure of complexity that takes not only information content into account, but also time and
space. Unfortunately, the theory of resource bounded complexity is notoriously difficult to work with and has many unsolved fundamental questions.
Furthermore, even if the universal prior distribution could be replaced by a
suitable computable prior, perhaps something like the Speed prior (Schmidhuber, 2002), there still remains the fact that AIXI’s search through possible
futures requires computation time that is exponential in the depth of the look
ahead (see the equation for AIXI in Section 2.10).

Despite these difficulties, several attempts at scaling AIXI down have been
made. The most theoretically founded of these is AIXItl (Chapter 7 of Hutter,
2005). In this model, proof search is used to limit the size and computation
time of the algorithm. Unfortunately, although technically computable, the
resulting agent still requires impossibly vast computational resources. Another
more drastic scaling down of AIXI did produce a usable algorithm (Poland and
Hutter, 2006). Here the problem domain was limited to games that could be
described by 2 × 2 matrices, and the look ahead was bounded to 8 interaction
cycles. The resulting algorithm was able to learn simple game theoretic interaction strategies. While this proves that some kind of scaling down of AIXI is
possible, the problem space of 2 × 2 matrix games falls well short of what is
needed for a useful artificial intelligence algorithm.

In this chapter we present what started out as another attempt to scale
AIXI down. As we have seen in previous chapters, at the core of the reinforcement learning problem lies the problem of estimating the expected future
discounted reward. We begin by expressing this estimation problem as a loss
function, more specifically, as the squared difference between the empirical future discounted reward and our estimate. We then derive an equation for
this estimator by minimising the loss function. Although the resulting learning
equations no longer bear much resemblance to AIXI, they do strongly resemble
the standard equation for temporal difference learning with eligibility traces,
also known as the TD(λ) algorithm. Interestingly, while the standard algorithm has a free learning rate parameter, in our new equation there is none. In
its place there is an equation that automatically sets the learning rate in a way
that is specific to each state transition. We have experimentally tested this new
learning rule against TD(λ) and found that it offers superior performance in
various settings. We have also extended the algorithm to reinforcement learning and again found encouraging results. This chapter covers the derivation
of this algorithm and our experimental results.

Note that while the notation used in this chapter is fairly standard for the
temporal difference learning literature, it is a little different to what we used
to define AIXI. For example, we now talk of states rather than observations,
and index the value function in a new way.

### 6.1. Temporal difference learning

In the field of reinforcement learning, perhaps the most popular way to estimate the future discounted reward of states is the method of temporal difference learning. It is unclear who exactly introduced this first, however the first
explicit version of temporal difference as a learning rule appears to be Witten
(1977). The idea is as follows: The expected future discounted reward of a state
s is,
{}
V := E r + γr + γ2r + ···|s = s,

$$
\overline{{V}}_{s}:=\mathbf{E}\left\{r_{k}+\gamma r_{k+1}+\gamma^{2}r_{k+2}+\cdots|s_{k}=s\right\},
$$

where the rewards rk,rk+1
γ < 1. From this definition it follows that,

,... are geometrically discounted into the future by
{}

$$
r_{k},r_{k+1},\ldots
$$

$$
\gamma<1
$$

$$
\overline{{V}}_{s}=\mathbf{E}\left\{r_{k}+\gamma\overline{{V}}_{s_{k+1}}|s_{k}=s\right\}.
$$

(6.1)

Our task, at time t, is to compute an estimate Vst of V s for each state s.
The only information we have to base this estimate on is the current history
of state transitions, s1,s2,...,st, and the current history of observed rewards,
r1,r2,...,rt. Equation (6.1) suggests that at time t + 1 the value of rt + γVst+1
provides us with information on what Vst should be: if it is higher than Vstt
then perhaps this estimate should be increased, and vice versa. This intuition
gives us the following estimation heuristic for state st,
()

$$
V_{s}^{t}
$$

$$
\overline{V}_{s}
$$

$$
s
$$

$$
s_{1},s_{2},\ldots,s_{t}
$$

$$
r_{1},r_{2},\ldots,r_{t}
$$

$$
r_{t}+\gamma V_{s_{t+1}}
$$

$$
V_{s}^{t}
$$

$$
V_{s_{t}}^{t}
$$

$$
s_{t}
$$

$$
V_{s_{t}}^{t+1}:=V_{s_{t}}^{t}+\alpha\left(r_{t}+\gamma V_{s_{t+1}}^{t}-V_{s_{t}}^{t}\right),
$$

where α is a parameter that controls the rate of learning. This type of temporal
difference learning is known as TD(0).

$$
\mathrm{TD}(0)
$$

One shortcoming of this method is that at each time step the value of only
the last state st is updated. States before the last state are also affected by

$$
s_{t}
$$

Algorithm 1 TD(λ)
Initialise V (s) arbitrarily and E(s) = 0 for all s
Initialise s
repeat
Make state transition and observe r, s′
∆ ← r + γV (s′) − V (s)
E(s) ← E(s) + 1
for all s do
V (s) ← V (s) + αE(s)∆
E(s) ← γλE(s)
end for
s ← s′
until end of run

$$
E(s)=0
$$

$$
V(s)
$$

$$
r,s^{\prime}
$$

$$
\Delta\leftarrow r+\gamma\overline{V}\left(s^{\prime}\right)-\overline{V}\left(s\right)
$$

$$
E(s)\leftarrow E(s)+1
$$

$$
V(s)\leftarrow V(s)+\alpha E(s)\Delta
$$

$$
E(s)\leftarrow\gamma\lambda E(s)
$$

$$
s\leftarrow s'
$$

changes in the last state’s value and thus these could be updated too. This is
what happens with so called temporal difference learning with eligibility traces,
where a history, or trace, is kept of which states have been recently visited.
Under this method, when we update the value of a state we also go back
through the trace updating the earlier states as well. Formally, for any state
s its eligibility trace is computed by,
{

$$
E_{s}^{t}:=\left\{\begin{array}{ll}\gamma\lambda E_{s}^{t-1}&\text{if}s\neq s_{t},\\\gamma\lambda E_{s}^{t-1}+1&\text{if}s=s_{t},\end{array}\right.
$$

where λ is used to control the rate at which the eligibility trace is discounted.
The temporal difference update is then, for all states s,
()

$$
V_{s}^{t+1}:=V_{s}^{t}+\alpha E_{s}^{t}\left(r+\gamma V_{s_{t+1}}^{t}-V_{s_{t}}^{t}\right).
$$

(6.2)

This more powerful version of temporal different learning is known as TD(λ)
(Sutton, 1988). The complete algorithm appears in Algorithm 1.

Although it has been successfully applied to many simple problems, plain
TD(λ) has a number of drawbacks. One of these is that the learning rate
parameter α has to be experimentally tuned by hand. Indeed, even this is
not always enough, for optimal performance some monotonically decreasing
function has to be experimentally found that decreases the learning rate over
time at the right rate. If the learning rate decreases too quickly, the system
may become stuck at a level of sub-optimal performance, if it decreases too
slowly then convergence will be unnecessarily late. The main contribution of
this chapter is to solve this problem by deriving a temporal difference rule
from statistical principles that automatically sets its learning rate.

Perhaps the closest work to ours is the LSTD(λ) algorithm (Bradtke and
Barto, 1996; Boyan, 1999; Lagoudakis and Parr, 2003). LSTD(λ) is concerned
with finding a least-squares linear function approximation to the true value function. The unknown expected rewards and transition probabilities are replaced by empirical averages up to current time t. In contrast, we consider
finite state spaces and no function approximation. We derive a least-squares
estimate of the empirical values including future rewards by bootstrapping.
The computation time for our update is linear in the number of states, like
TD(λ), while LSTD is quadratic (even in the case of state-indicator features
and no function approximation). Indeed our algorithm exactly coincides with
TD/Q/Sarsa(λ) but with a novel learning rate derived from statistical principles. LSTD has not yet been developed for general λ and γ. Our algorithm and
LSTD both get rid of the learning rate and the necessity to initialise V. Since
LSTD has primarily been developed for linear function approximation and has
a much more expensive update rule, we focused our experimental comparison
to the algorithms for which we determined the learning rate (finite state space,
linear time TD/Q/Sarsa algorithms). It remains to be seen how our approach
generalises to (linear) function approximation.

$$
\lambda
$$

$$
\gamma
$$

### 6.2. Derivation

The empirical future discounted reward of a state sk is the sum of actual
rewards following from state sk in time steps k,k + 1,..., where the rewards
are discounted as they go into the future. Formally, the empirical value of
state sk at time k for k = 1,...,t is,

$$
s_{k}
$$

$$
s_{k}
$$

$$
k,k+1,\ldots
$$

$$
s_{k}
$$

$$
v_{k}:=\sum_{u=k}^{\infty}\gamma^{u-k}r_{u},
$$

(6.3)

where the future rewards ru are geometrically discounted by γ < 1. In practice
the exact value of vk is always unknown to us as it depends not only on rewards
that have been already observed, but also on unknown future rewards. Note
that if sm = sn for m = n, that is, we have visited the same state twice at
different times m and n, this does not imply that vn = vm as the observed
rewards following the state visit may be different each time.

$$
r_{u}
$$

$$
\gamma<1
$$

$$
v_{k}
$$

$$
s_{m}=s_{n}
$$

$$
m\neq n
$$

$$
n,
$$

$$
v_{n}=v_{m}
$$

Our goal is that for each state s the estimate Vst should be as close as possible
to the true expected future discounted reward V s. Thus, for each state s we
would like Vs to be close to vk for all k such that s = sk. Furthermore, in
non-stationary environments we would like to discount old evidence by some
parameter λ ∈ (0, 1]. Formally, we want to minimise the loss function,

$$
V_{s}^{t}
$$

$$
\tilde{\overline{V}}_{s}
$$

$$
V_{s}
$$

$$
v_{k}
$$

$$
s=s_{k}
$$

$$
\lambda\in(0,1]
$$

$$
L:=\frac{1}{2}\sum_{k=1}^{t}\lambda^{t-k}\big(v_{k}-V_{s_{k}}^{t}\big)^{2}.
$$

(6.4)

For stationary environments we may simply set λ = 1 a priori.

$$
\lambda=1
$$

As we wish to minimise this loss, we take the partial derivative with respect
to the value estimate of each state and set to zero,

$$
\frac{\partial L}{\partial V_{s}^{t}}=-\sum_{k=1}^{t}\lambda^{t-k}\big(v_{k}-V_{s_{k}}^{t}\big)\delta_{s_{k}s}=V_{s}^{t}\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}-\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}v_{k}=0,
$$

where we could change Vstk into Vst due to the presence of the Kronecker δsks,
defined δxy:= 1 if x = y, and 0 otherwise. By defining a discounted state visit
∑t
counter Nst:=k=1λt−kδskswe get

$$
V_{s_{k}}^{t}
$$

$$
V_{s}^{t}
$$

$$
\delta_{xy}:=1
$$

$$
\delta_{s_{k}s},
$$

$$
x=y
$$

$$
\widetilde{N_{s}^{t}}:=\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}
$$

$$
V_{s}^{t}N_{s}^{t}=\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}v_{k}.
$$

(6.5)

Since vk depends on future rewards rk, Equation (6.5) can not be used in
its current form. Next we note that vk has a self-consistency property with
respect to the rewards. Specifically, the tail of the future discounted reward
sum for each state depends on the empirical value at time t in the following
way,
∑t−1

$$
v_{k}
$$

$$
r_{k}
$$

$$
v_{k}
$$

$$
v_{k}=\sum_{u=k}^{t-1}\gamma^{u-k}r_{u}+\gamma^{t-k}v_{t}.
$$

Substituting this into Equation (6.5) and exchanging the order of the double
sum,

$$
\begin{array}{r c l}{V_{s}^{t}N_{s}^{t}}&{=}&{\sum_{u=1}^{t-1}\sum_{k=1}^{u}\lambda^{t-k}\delta_{s_{k}s}\gamma^{u-k}r_{u}+\sum_{k=1}^{t}\lambda^{t-k}\delta_{s_{k}s}\gamma^{t-k}v_{t}}\\ {}&{=}&{\sum_{u=1}^{t-1}\lambda^{t-u}\sum_{k=1}^{u}(\lambda\gamma)^{u-k}\delta_{s_{k}s}r_{u}+\sum_{k=1}^{t}(\lambda\gamma)^{t-k}\delta_{s_{k}s}v_{t}}\\ {}&{=}&{R_{s}^{t}+E_{s}^{t}v_{t},}\\ \end{array}
$$

∑t
where Est:=k=1(λγ)t−kδsksis the eligibility trace of state s, and Rst:=
∑t−1
u=1λt−uEsuru is the discounted reward with eligibility.

$$
E_{s}^{t}:=\sum_{k=1}^{t}(\lambda\gamma)^{t-k}\delta_{s_{k}s}
$$

$$
s,
$$

$$
R_{s}^{t}:=
\sum_{u=1}^{t-1}\lambda^{t-u}E_{s}^{u}r_{u}
$$

Est and Rst depend only on quantities known at time t. The only unknown
quantity is vt, which we have to replace with our current estimate of this value
at time t, which is Vstt. In other words, we bootstrap our estimates. This gives
us,
V N = Rt + E V.

$$
E_{s}^{t}
$$

$$
R_{s}^{t}
$$

$$
v_{t}
$$

$$
V_{s_{t}}^{t}
$$

$$
t,
$$

$$
V_{s}^{t}N_{s}^{t}=R_{s}^{t}+E_{s}^{t}V_{s_{t}}^{t}.
$$

(6.6)

For state s = st, this simplifies to

$$
s=s_{t}
$$

$$
V_{s_{t}}^{t}=\frac{R_{s_{t}}^{t}}{N_{s_{t}}^{t}-E_{s_{t}}^{t}}.
$$

Substituting this back into Equation (6.6) we obtain,

$$
V_{s}^{t}N_{s}^{t}=R_{s}^{t}+E_{s}^{t}\frac{R_{s_{t}}^{t}}{N_{s_{t}}^{t}-E_{s_{t}}^{t}}.
$$

(6.7)

This gives us an explicit expression for our V estimates. However, from an
algorithmic perspective an incremental update rule is more convenient. To
derive this we make use of the relations,

$$
\begin{array}{r l}{N_{s}^{t+1}=}&{\lambda N_{s}^{t}+\delta_{s_{t+1}s},\qquad\quad N_{s}^{0}=0,}\\ {E_{s}^{t+1}=}&{\lambda\gamma E_{s}^{t}+\delta_{s_{t+1}s},\qquad\quad E_{s}^{0}=0,}\\ {R_{s}^{t+1}=}&{\lambda R_{s}^{t}+\lambda E_{s}^{t}r_{t},\qquad\quad R_{s}^{0}=0,}\end{array}
$$

Inserting these into Equation (6.7) with t replaced by t + 1,

$$
\begin{align*}V_{s}^{t+1}N_{s}^{t+1}\quad&=\quad R_{s}^{t+1}+E_{s}^{t+1}\frac{R_{s_{t+1}}^{t+1}}{N_{s_{t+1}}^{t+1}-E_{s_{t+1}}^{t+1}}\\&=\quad\lambda R_{s}^{t}+\lambda E_{s}^{t}r_{t}+E_{s}^{t+1}\frac{R_{s_{t+1}}^{t}+E_{s_{t+1}}^{t}r_{t}}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}.\end{align*}
$$

By solving Equation (6.6) for Rst and substituting back in,

$$
R_{s}^{t}
$$

$$
\begin{aligned}{V_{s}^{t+1}N_{s}^{t+1}}&{{}=\lambda\big(V_{s}^{t}N_{s}^{t}-E_{s}^{t}V_{s_{t}}^{t}\big)+\lambda E_{s}^{t}r_{t}+E_{s}^{t+1}\frac{N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-E_{s_{t+1}}^{t}V_{s_{t}}^{t}+E_{s_{t+1}}^{t}r_{t}}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}}\\ {}&{{}=\;\big(\lambda N_{s}^{t}+\delta_{s_{t+1}s}\big)V_{s}^{t}-\delta_{s_{t+1}s}V_{s}^{t}-\lambda E_{s}^{t}V_{s_{t}}^{t}+\lambda E_{s}^{t}r_{t}}\\ {}&{{}\quad+E_{s}^{t+1}\frac{N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-E_{s_{t+1}}^{t}V_{s_{t}}^{t}+E_{s_{t+1}}^{t}r_{t}}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}.}\\ \end{aligned}
$$

Dividing through by Nst+1(= λNst+ δst+1s),

$$
N_{s}^{t+1}(=\lambda N_{s}^{t}+\delta_{s_{t+1}s}).
$$

$$
\begin{aligned}V_{s}^{t+1}=V_{s}^{t}&+\frac{-\delta_{s_{t+1}s}V_{s}^{t}-\lambda E_{s}^{t}V_{s_{t}}^{t}+\lambda E_{s}^{t}r_{t}}{\lambda N_{s}^{t}+\delta_{s_{t+1}s}}\\&+\frac{(\lambda\gamma E_{s}^{t}+\delta_{s_{t+1}s})(N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-E_{s_{t+1}}^{t}V_{s_{t}}^{t}+E_{s_{t+1}}^{t}r_{t})}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}+\delta_{s_{t+1}s})}.\end{aligned}
$$

Making the first denominator the same as the second, then expanding the
numerator,

$$
\begin{aligned}&V_{s}^{t+1}=V_{s}^{t}{+}\frac{\lambda E_{s}^{t}r_{t}N_{s_{t+1}}^{t}-\lambda E_{s}^{t}V_{s_{t}}^{t}N_{s_{t+1}}^{t}-\delta_{s_{t+1}s}V_{s}^{t}N_{s_{t+1}}^{t}-\lambda\gamma E_{s_{t+1}}^{t}E_{s}^{t}r_{t}}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}{+}\delta_{s_{t+1}s})}\\ &\\ &\quad{+}\frac{\lambda\gamma E_{s_{t+1}}^{t}E_{s}^{t}V_{s_{t}}^{t}+\gamma E_{s_{t+1}}^{t}V_{s}^{t}\delta_{s_{t+1}s}+\lambda\gamma E_{s}^{t}N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-\lambda\gamma E_{s}^{t}E_{s_{t+1}}^{t}V_{s_{t}}^{t}}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}{+}\delta_{s_{t+1}s})}\\ \end{aligned}
$$

$$
+\frac{\lambda\gamma E_{s}^{t}E_{s_{t+1}}^{t}r_{t}+\delta_{s_{t+1}s}N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-\delta_{s_{t+1}s}E_{s_{t+1}}^{t}V_{s_{t}}^{t}+\delta_{s_{t+1}s}E_{s_{t+1}}^{t}r_{t}}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}+\delta_{s_{t+1}s})}.
$$

After cancelling equal terms (keeping in mind that in every term with a Kronecker δxy factor we may assume that x = y as the term is always zero otherwise), and factoring out Est the right hand side becomes,
()

$$
\delta_{xy}
$$

$$
E_{s}^{t}
$$

$$
x=y
$$

$$
V_{s}^{t}+\frac{E_{s}^{t}\left(\lambda r_{t}N_{s_{t+1}}^{t}-\lambda V_{s_{t}}^{t}N_{s_{t+1}}^{t}+\gamma V_{s}^{t}\delta_{s_{t+1}s}+\lambda\gamma N_{s_{t+1}}^{t}V_{s_{t+1}}^{t}-\delta_{s_{t+1}s}V_{s_{t}}^{t}+\delta_{s_{t+1}s}r_{t}\right)}{(N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t})(\lambda N_{s}^{t}+\delta_{s_{t+1}s})}
$$

Finally, by factoring out λNstt+1 + δst+1

swe obtain our update rule,
()

$$
\lambda N_{s_{t+1}}^{t}+\delta_{s_{t+1}s}
$$

(6.8)

$$
V_{s}^{t+1}=V_{s}^{t}+E_{s}^{t}\beta_{t}(s,s_{t+1})\left(r_{t}+\gamma V_{s_{t+1}}^{t}-V_{s_{t}}^{t}\right),
$$

where the learning rate is given by,

$$
\beta_{t}(s,s_{t+1})\quad:=\quad\frac{1}{N_{s_{t+1}}^{t}-\gamma E_{s_{t+1}}^{t}}\quad\frac{N_{s_{t+1}}^{t}}{N_{s}^{t}}.
$$

(6.9)

Examining Equation (6.8), we find the usual update equation for temporal
difference learning with eligibility traces (see Equation (6.2)), however the
learning rate α has now been replaced by βt(s,st+1). This learning rate was
derived by minimising the squared loss between the estimated and true state
value. In the derivation we have exploited the fact that the latter must be
self-consistent and then bootstrapped to get Equation (6.6). This gives us an
equation for the learning rate for each state transition at time t, as opposed to
the standard temporal difference learning where the learning rate α is either
a fixed free parameter for all transitions, or is decreased over time by some
monotonically decreasing function. In either case, the learning rate is not
automatic and must be experimentally tuned for good performance. The above
derivation appears to theoretically solve this problem.

$$
\beta_{t}(s,s_{t+1})
$$

The first term in βt seems to provide some type of normalisation to the
learning rate, though the intuition behind this is not clear to us. The meaning
of second term however can be understood as follows: Nst measures how often
we have visited state s in the recent past. Therefore, if Nst ≪ Nstt+1 then
state s has a value estimate based on relatively few samples, while state st+1
has a value estimate based on relatively many samples. In such a situation,
the second term in βt boosts the learning rate so that Vst+1 moves more aggressively towards the presumably more accurate rt + γVstt+1. In the opposite
situation when st+1 is a less visited state, we see that the reverse occurs and
the learning rate is reduced in order to maintain the existing value of Vs.

$$
\beta_{t}
$$

$$
N_{s}^{t}
$$

$$
N_{s}^{t}\ll N_{s_{t+1}}^{t}
$$

$$
s_{t+1}
$$

$$
V_{s}^{t+1}
$$

$$
\beta_{t}
$$

$$
r_{t}+\gamma V_{s_{t+1}}^{t}
$$

$$
s_{t+1}
$$

### 6.3. Estimating a small Markov process

$$
V_{s}
$$

For our first test we consider a small Markov process with 21 states. In each
step the state number is either incremented or decremented by one with equal

**TD UPDATING WITHOUT A LEARNING RATE**

| Time (x1e4) | HL(1.0) (RMSE) | TD(0.7) a = 0.07 (RMSE) | TD(0.7) a = 0.13 (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.26 | 0.26 | 0.26 |
| 0.2 | 0.055 | 0.06 | 0.05 |
| 0.4 | 0.04 | 0.04 | 0.065 |
| 0.6 | 0.037 | 0.055 | 0.075 |
| 0.8 | 0.037 | 0.06 | 0.085 |
| 1.0 | 0.033 | 0.058 | 0.09 |

**TD UPDATING WITHOUT A LEARNING RATE**

| Time (x1e4) | HL(1.0) (RMSE) | TD(0.7) a = 0.07 (RMSE) | TD(0.7) a = 0.13 (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.26 | 0.26 | 0.26 |
| 0.2 | 0.055 | 0.07 | 0.06 |
| 0.4 | 0.045 | 0.04 | 0.075 |
| 0.6 | 0.04 | 0.05 | 0.078 |
| 0.8 | 0.038 | 0.055 | 0.08 |
| 1.0 | 0.037 | 0.06 | 0.078 |

Figure 6.1.: 21 state Markov process,
average performance over
10 runs.

Figure 6.2.: 21 state Markov process,
average performance over
100 runs.

probability, unless the system is in state 0 or 20 in which case it always transitions to state 10 in the following step. When the state transitions from 0 to
10 a reward of 1.0 is generated, and for a transition from 20 to 10 a reward of
-1.0 is generated. All other transitions have a reward of 0. We set the discount
value γ = 0.9 and then computed the true discounted value of each state by
running a brute force Monte Carlo simulation.

$$
\gamma=0.9
$$

For our first test we ran our algorithm 10 times on the above Markov chain
and computed the root mean squared error in the value estimate across the
states at each time step averaged across each run. The optimal value of λ for
our algorithm, which we will call HL(λ), was 1.0. This was to be expected
given that the environment is stationary and thus discounting old experience
is not helpful. Setting this parameter correctly was important, for example if
we reduced the value of λ to 0.98 performance became poor.

For TD(λ) the optimal value of λ was about 0.7. This algorithm was much
less sensitive to the setting of λ. The other important parameter for TD(λ)
was the learning rate α. We tested a variety of values, the effect of which is
illustrated by the two values α = 0.07 and α = 0.13 on Figure 6.1.

$$
\alpha=0.07
$$

$$
\alpha=0.13
$$

When α was high, TD(λ) learnt more quickly, as we would expect, but then
became unstable as the learning rate was too high for fine tuning the value
estimates. With the lower learning rate of 0.07, TD(λ) learnt more slowly, but
eventually achieved a more accurate value estimate before becoming stuck. In
fact rather than just becoming stuck, what we see is that the error reaches
a minimum at around t = 4,000 and then actually becomes worse for the
remainder of the run. This is a well known undesirable characteristic of TD(λ)
(see for example Section 6.2 of Sutton and Barto, 1998). With a fixed learning
rate we also see that the variability in the error estimate does not improve
towards the end of the run.

In comparison, HL(λ) had very fast learning initially, combined with a more
accurate final estimate of the discounted state values, and the mean squared
error in the second half of the experiment was very stable. This is significant
given that TD(λ) required two parameters to be tuned for good performance,
while HL(λ) had just λ which could be set a priori to 1.0.

Figure 6.2 shows the same experiment averaged over 100 runs. This obscures
the better stability of HL(λ), but more clearly illustrates its faster learning and
better convergence.

### 6.4. A larger Markov process

In order to understand how well HL(λ) scales as the number of states increases,
we ran the previous experiment again but with 51 states. As the movement
through the states is almost entirely a random walk with reward on just two
transitions, estimating the value function on this Markov chain is significantly
more difficult than before, even though the total number of states has not
grown all that much. In the new experiment the return state was still in
the middle of the chain, i.e. state 25. As most of the state space was a long
way from the rewards, we increased the γ value to 0.99 so that states in the
middle of the chain would not have values too close to 0. The true discounted
value of each state was again computed by running a brute force Monte Carlo
simulation.

$$
\gamma
$$

We ran our algorithm 10 times on the above Markov chain and computed
the root mean squared error in the value estimate across the states at each
time step averaged across each run. The optimal value of λ for HL(λ) was 1.0,
which was to be expected given that the environment is stationary and thus
discounting old experience is not helpful.

For TD(λ) we tried various different learning rates and values of λ. We
could find no settings where TD(λ) was competitive with HL(λ). If the learning rate α was set too high the system would learn as fast as HL(λ) briefly
before becoming stuck. With a lower learning rate the final performance was
improved, however the initial performance was now much worse than HL(λ).
The results of these tests appear in Figure 6.3.

$$
\lambda.
$$

Similar tests were performed with larger and smaller Markov chains, and
with different values of γ. HL(λ) was consistently superior to TD(λ) across
these tests. One wonders whether this may be due to the fact that the implicit learning rate that HL(λ) uses is not fixed. To test this we explored the
performance of a number of different learning rate functions on the 51 state
κ
Markov chain described above. We found that functions of the form always
t
performed poorly, however good performance was possible by setting κ cor-
√κ √κ
rectly for functions of the form and3. As the results were much closer,
t t
we averaged over 300 runs. These results appear in Figure 6.4.

$$
\gamma
$$

$$
\frac{\kappa}{t}
$$

$$
\frac{\kappa}{\sqrt{t}}
$$

$$
\frac{\kappa}{\sqrt[3]{t}}
$$

With a variable learning rate TD(λ) is performing much better, however we
were still unable to find an equation that reduced the learning rate in such

| Time (x1e+4) | HL(1.0) (RMSE) | TD(0.9) a = 0.1 (RMSE) | TD(0.9) a = 0.2 (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.36 | 0.36 | 0.36 |
| 0.5 | 0.11 | 0.19 | 0.11 |
| 1.0 | 0.08 | 0.10 | 0.15 |
| 1.5 | 0.06 | 0.07 | 0.13 |
| 2.0 | 0.06 | 0.06 | 0.14 |

| Time (x1e+4) | HL(1.0) (RMSE) | TD(0.9) a = 8.0/sqrt(t) (RMSE) | TD(0.9) a = 2.0/cbrt(t) (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.35 | 0.35 | 0.35 |
| 0.5 | 0.11 | 0.13 | 0.12 |
| 1.0 | 0.08 | 0.085 | 0.085 |
| 1.5 | 0.065 | 0.07 | 0.07 |
| 2.0 | 0.06 | 0.065 | 0.065 |

Figure 6.3.: 51 state Markov process
averaged over 10 runs.
The parameter a is the
learning rate α.

$$
\alpha.
$$

Figure 6.4.: 51 state Markov process
averaged over 300 runs.

a way that TD(λ) would outperform HL(λ). This is evidence that HL(λ) is
adapting the learning rate optimally without the need for manual equation
tuning.

### 6.5. Random Markov process

To test on a Markov process with a more complex transition structure, we
created a random 50 state Markov process. We did this by creating a 50 by 50
transition matrix where each element was set to 0 with probability 0.9, and a
uniformly random number in the interval [0, 1] otherwise. We then scaled each
row to sum to 1. Then to transition between states we interpret the ith row
as a probability distribution over which state follows state i. To compute the
reward associated with each transition we created a random matrix as above,
but without normalising. We set γ = 0.9 and then ran a brute force Monte
Carlo simulation to compute the true discounted value of each state.

$$
i^{th}
$$

$$
\gamma=0.9
$$

The λ parameter for HL(λ) was simply set to 1.0 as the environment is
stationary. For TD we experimented with a range of parameter settings and
learning rate decrease functions. We found that a fixed learning rate of α = 0.2,
1√.5
and a decreasing rate of3performed reasonable well, but never as well as
t
HL(λ). The results were generated by averaging over 10 runs, and are shown
in Figure 6.5.

$$
\lambda
$$

$$
\alpha=0.2
$$

$$
\frac{1.5}{\sqrt[3]{t}}
$$

Although the structure of this Markov process is quite different to that used
in the previous experiment, the results are again similar: HL(λ) preforms as
well or better than TD(λ) from the beginning to the end of the run. Furthermore, stability in the error towards the end of the run is better with HL(λ)
and no manual learning tuning was required for these performance gains.

| Time | HL(1.0) (RMSE) | TD(0.9) a = 0.2 (RMSE) | TD(0.9) a = 1.5/cbrt(t) (RMSE) |
| --- | --- | --- | --- |
| 1000 | 0.14 | 0.17 | 0.16 |
| 2000 | 0.10 | 0.14 | 0.12 |
| 3000 | 0.09 | 0.13 | 0.12 |
| 4000 | 0.085 | 0.13 | 0.10 |
| 5000 | 0.075 | 0.13 | 0.10 |

Figure 6.5.: Random 50 state Markov
process. The parameter a
is the learning rate α.

| Time (x1e+4) | HL(0.9995) (RMSE) | TD(0.8) a = 0.05 (RMSE) | TD(0.9) a = 0.05 (RMSE) |
| --- | --- | --- | --- |
| 0.0 | 0.25 | 0.25 | 0.25 |
| 0.5 | 0.05 | 0.04 | 0.05 |
| 1.0 | 0.04 | 0.05 | 0.05 |
| 1.5 | 0.045 | 0.055 | 0.055 |
| 2.0 | 0.035 | 0.05 | 0.05 |

Figure 6.6.: 21 state non-stationary
Markov process.

### 6.6. Non-stationary Markov process

The λ parameter in HL(λ), introduced in Equation (6.4), reduces the importance of old observations when computing the state value estimates. When the
environment is stationary this is not useful and so we can set λ = 1.0, however
in a non-stationary environment we need to reduce this value so that the state
values adapt properly to changes in the environment. The more rapidly the
environment is changing, the lower we need to make λ in order to more rapidly
forget old observations.

$$
\lambda=1.0
$$

To test HL(λ) in such a setting we reverted back to the 21 state Markov
chain from Section 6.3 in order to speed up convergence. We used this Markov
chain for the first 5,000 time steps. At that point, we changed the reward
when transitioning from the last state to the middle state from -1.0 to be 0.5.
At time 10,000 we then switched back to the original Markov chain, and so on
alternating between the models of the environment every 5,000 steps. At each
switch, we also changed the target state values that the algorithm was trying
to estimate to match the current configuration of the environment. For this
experiment we set γ = 0.9.

$$
\gamma=0.9.
$$

As expected, the optimal value of λ for HL(λ) fell from 1 down to about
0.9995. This is about what we would expect given that each phase is 5,000
steps long. For TD(λ) the optimal value of λ was around 0.8 and the optimum
learning rate was around 0.05. As we would expect, for both algorithms when
we pushed λ above its optimal value this caused poor performance in the
periods following each switch in the environment (these bad parameter settings
are not shown in the results). On the other hand, setting λ too low produced
initially fast adaption to each environment switch, but poor performance after
that until the next environment change. To get accurate statistics we averaged
over 200 runs. The results of these tests appear in Figure 6.6.

$$
\lambda
$$

Algorithm 2 HLS(λ)
Initialise Q(s,a) = 0, N (s,a) = 1 and E(s,a) = 0 for all s, a
Initialise s and a
repeat
Take action a, observed r, s′
Choose a′ by using ǫ-greedy selection on Q(s′, ·)
∆ ← r + γQ(s′,a′) − Q(s,a)
E(s,a) ← E(s,a) + 1
N (s,a) ← N (s,a) + 1
for all s,a do
1 N (s′,a′)
β((s,a), (s′,a′)) ←
N (s′,a′)−γE(s′,a′) N (s,a)
end for
for all s,a do
()
Q(s,a) ← Q(s,a) + β (s,a), (s′,a′) E(s,a)∆
E(s,a) ← γλE(s,a)
N (s,a) ← λN (s,a)
end for
s ← s′; a ← a′
until end of run

$$
E(s,a)=0
$$

$$
Q(s,a)=0,\;N(s,a)=1
$$

$$
a,
$$

$$
a^{\prime}
$$

$$
r,\;s^{\prime}
$$

$$
\Delta\leftarrow r+\gamma Q(s',a')-Q(s,a)
$$

$$
Q\big(s^{\prime},\cdot\big)
$$

$$
E(s,a)\leftarrow E(s,a)+1
$$

$$
N(s,a)\leftarrow N(s,a)+1
$$

$$
\beta((s,a),(s^{\prime},a^{\prime}))\leftarrow\frac{1}{\scriptstyle N(s^{\prime},a^{\prime})-\gamma E(s^{\prime},a^{\prime})}\quad\frac{\scriptstyle N(s^{\prime},a^{\prime})}{\scriptstyle N(s,a)}
$$

$$
s,a
$$

$$
Q(s,a)\leftarrow Q(s,a)+\beta\big((s,a),(s^{\prime},a^{\prime})\big)E(s,a)\Delta
$$

$$
E(s,a)\leftarrow\gamma\lambda E(s,a)
$$

$$
N(s,a)\leftarrow\lambda N(s,a)
$$

$$
s\leftarrow s';a\leftarrow a'
$$

For some reason HL(0.9995) learns faster than TD(0.8) in the first half
of the first cycle, but only equally fast at the start of each following cycle.
Furthermore, its performance in the second half of the first cycle is poor. We
are not sure why this is happening. We could improve the initial speed at
which HL(λ) learnt in the last three cycles by reducing λ, however that comes
at a performance cost in terms of the lowest mean squared error attained at
the end of each cycle. In any case, in this non-stationary situation HL(λ) again
performed well in general.

### 6.7. Windy Gridworld

Reinforcement learning algorithms such as Watkins’ version of Q(λ) (Watkins,
1989) and Sarsa(λ) (Rummery and Niranjan, 1994; Rummery, 1995) are based
on temporal difference updates. This suggests that new reinforcement learning
algorithms based on HL(λ) should be possible.

For our first experiment we took the standard Sarsa(λ) algorithm and modified it in the obvious way to use an HL temporal difference update. In the
presentation of this algorithm we have changed notation slightly to make things
more consistent with that typical in reinforcement learning. Specifically, we
have dropped the t super script as this is implicit in the algorithm specification, and have defined Q(s,a) := V(s,a), E(s,a) := E(s,a) and N (s,a) := N(s,a).
Our new reinforcement learning algorithm, which we call HLS(λ) is given in
Algorithm 2. Essentially the only changes to the standard Sarsa(λ) algorithm

$$
Q(s,a):=V_{(s,a)},E(s,a):=E_{(s,a)}
$$

$$
N(s,a):=N_{(s,a)}
$$

| Category | wind strength 0 | wind strength 1 | wind strength 2 |
| --- | --- | --- | --- |
| unlabelled 1 |  | ↑ | ↑ |
| unlabelled 2 |  | ↑ | ↑ |
| unlabelled 3 |  | ↑ | ↑ |
| S |  | ↑ | G |
| unlabelled 4 |  | ↑ | ↑ |
| unlabelled 5 |  | ↑ | ↑ |
| unlabelled 6 |  | ↑ | ↑ |

Figure 6.7.: [Windy Gridworld] S marks the start state and G the goal state,
at which the agent jumps back to S with a reward of 1. Small
arrows indicate an upward wind of one row per time step. The
large arrows indicate a wind of two rows per time step.

have been to add code to compute the visit counter N (s,a), add a loop to
compute the β values, and replace α with β in the temporal difference update.

$$
N(s,a)
$$

$$
\beta
$$

$$
\beta
$$

To test HLS(λ) against standard Sarsa(λ) we used the Windy Gridworld
environment described on page 146 of (Sutton and Barto, 1998). This world is
a grid of 7 by 10 squares that the agent can move through by going either up,
down, left or right. If the agent attempts to move off the grid it simply stays
where it is. The agent starts in the 4th row of the 1st column and receives
a reward of 1 when it finds its way to the 4th row of the 8th column. To
make things more difficult, there is a “wind” blowing the agent up 1 row in
columns 4, 5, 6, and 9, and a strong wind of 2 rows in columns 7 and 8. This
is illustrated in Figure 6.7. Unlike in the original version, we have set up this
problem to be a continuing discounted task with an automatic transition from
the goal state back to the start state. This is because we have not yet derived
an episodic version of our learning rule.

$$
4^{th}
$$

$$
1^{st}
$$

$$
4^{th}
$$

$$
8^{th}
$$

We set γ = 0.99 and in each run computed the empirical future discounted
reward at each point in time. As this value oscillated we also ran a moving
average through these values with a window length of 50. Each run lasted for
50,000 time steps as this allowed us to see at what level each learning algorithm
topped out. These results appear on the left of Figure 6.8 and were averaged
over 500 runs to get accurate statistics.

$$
\gamma=0.99
$$

Despite putting considerable effort into tuning the parameters of Sarsa(λ),
we were unable to achieve a final future discounted reward above 5.0. The

| Time | HLS(0.995) e = 0.003 (Future Discounted Reward) | Sarsa(0.5) a = 0.4 e = 0.005 (Future Discounted Reward) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10000 | 4.0 | 3.8 |
| 20000 | 4.9 | 4.7 |
| 30000 | 5.15 | 4.85 |
| 40000 | 5.2 | 4.9 |
| 50000 | 5.25 | 4.95 |

| Time | HLQ(0.99) e = 0.01 (Future Discounted Reward) | Q(0.75) a = 0.99 e = 0.01 (Future Discounted Reward) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10000 | 4.3 | 4.0 |
| 20000 | 5.15 | 4.9 |
| 30000 | 5.4 | 5.3 |
| 40000 | 5.45 | 5.4 |
| 50000 | 5.45 | 5.45 |

Figure 6.8.: Windy Gridworld performance tests. The left graph shows
HLS(λ) vs. Sarsa(λ), while the right graph shows HLQ(λ) vs.
Q(λ). In both tests the algorithm based on HL learning performed
best. e represents the exploration parameter ǫ, and a represents
the learning rate α. For both tests the performance was averaged
over 500 runs.

settings shown on the graph represent the best final value we could achieve.
In comparison HLS(λ) easily beat this result at the end of the run, while being
slightly slower than Sarsa(λ) at the start. By setting λ = 0.99 we were able
to achieve the same performance as Sarsa(λ) at the start of the run, however
the performance at the end of the run was then only slightly better than
Sarsa(λ). This combination of superior performance and fewer parameters
to tune suggest that the benefits of HL(λ) carry over into the reinforcement
learning setting. In terms of computational cost, HL(λ) was about 1.7 times
slower than Sarsa(λ) per time step due to the cost of computing the β values.

$$
\lambda=0.99
$$

$$
\beta
$$

Another popular reinforcement learning algorithm is Watkins’ Q(λ). Similar
to Sarsa(λ) above, we simply inserted the HL(λ) temporal difference update
into the usual Q(λ) algorithm in the obvious way. We call this new algorithm
HLQ(λ) and it is given in Algorithm 3. The test environment was exactly the
same as we used with Sarsa(λ) above.

$$
Q(\lambda)
$$

The results this time were more competitive and appear on the right hand
side of Figure 6.8. Nevertheless, despite spending a considerable amount of
time fine tuning the parameters of Q(λ), we were unable to beat HLQ(λ). As
the performance advantage was relatively modest, the main benefit of HLQ(λ)
was that it achieved this level of performance without having to manually tune
a learning rate.

Algorithm 3 HLQ(λ)
Initialise Q(s,a) = 0, N (s,a) = 1 and E(s,a) = 0 for all s, a
Initialise s and a
repeat
Take action a, observed r, s′
Choose a′ by using ǫ-greedy selection on Q(s′, ·)
a∗ ← arg maxb Q(s′,b)
∆ ← r + γQ(s′,a∗) − Q(s,a)
E(s,a) ← E(s,a) + 1
N (s,a) ← N (s,a) + 1
for all s,a do
1 N (s′,a′)
β((s,a), (s′,a′)) ←
N (s′,a′)−γE(s′,a′) N (s,a)
end for
for all s,a do
()
Q(s,a) ← Q(s,a) + β (s,a), (s′,a′) E(s,a)∆
N (s,a) ← λN (s,a)
if a′ = a∗ then
E(s,a) ← γλE(s,a)
else
E(s,a) ← 0
end if
end for
s ← s′; a ← a′
until end of run

$$
r,s^{\prime}
$$

$$
a^{\prime}
$$

$$
Q\big(s^{\prime},\cdot\big)
$$

$$
\Delta\leftarrow r+\gamma Q(s',a^*)-Q(s,a
$$

$$
E(s,a)\leftarrow E(s,a)+1
$$

$$
N(s,a)\leftarrow N(s,a)+1
$$

$$
\beta((s,a),(s^{\prime},a^{\prime}))\leftarrow\frac{1}{N(s^{\prime},a^{\prime})-\gamma E(s^{\prime},a^{\prime})}\quad\frac{N(s^{\prime},a^{\prime})}{N(s,a)}
$$

$$
s,a
$$

$$
Q(s,a)\leftarrow Q(s,a)+\beta\big((s,a),(s^{\prime},a^{\prime})\big)E(s,a)\Delta
$$

$$
N(s,a)\leftarrow\lambda N(s,a)
$$

$$
a^{\prime}=a^{*}
$$

$$
E(s,a)\leftarrow\gamma\lambda E(s,a)
$$

$$
E(s,a)\leftarrow0
$$

### 6.8. Conclusion

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

## Relationships

- **Section:** [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md)
- **Previous in the list:** [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)
- **Next in the list:** [28 - Generative Adversarial Nets](/papers/28-generative-adversarial-nets.md)
- **Builds on:** [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md), [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)
- **Alongside:** [19](/papers/19-gpipe-pipeline-parallelism.md), [20](/papers/20-adam-stochastic-optimization.md), [21](/papers/21-dropout-regularization.md), [22](/papers/22-first-law-of-complexodynamics.md), [23](/papers/23-keeping-neural-networks-simple.md), [24](/papers/24-tutorial-minimum-description-length.md) …
- **Topics:** [Kolmogorov Complexity](/topics/kolmogorov-complexity.md)
- **People:** [Shane Legg](/people/shane-legg.md)
- **Reading paths:** [Theory and Compression](/reading-paths/theory-and-compression.md)

## Source and provenance

- Listed at position 27 of the 30-paper reading list compiled by @rachit.speaks, the list Ilya Sutskever is reported to have given John Carmack.[^reading-list]
- Original: <https://www.vetta.org/documents/Machine_Super_Intelligence.pdf>
- Full text not included in this bundle; follow the link above.

[^reading-list]: The 30 Papers to AI Mastery, curated by @rachit.speaks
[^original]: Machine Super Intelligence - PhD thesis, University of Lugano
