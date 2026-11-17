---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 4.4. Response to common criticisms
section_role: other
section_index: 40
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Attempting to mathematically define intelligence is very ambitious and so, not surprisingly, the reactions we get can be interesting. Having…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.4. Response to common criticisms

> Section 40 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

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

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
