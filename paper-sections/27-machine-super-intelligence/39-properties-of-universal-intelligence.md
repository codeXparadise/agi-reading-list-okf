---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 4.3. Properties of universal intelligence
section_role: other
section_index: 39
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "What we have presented is a definition of machine intelligence. It is not a practical test of machine intelligence, indeed the value of Υ is not…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.3. Properties of universal intelligence

> Section 39 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

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

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
