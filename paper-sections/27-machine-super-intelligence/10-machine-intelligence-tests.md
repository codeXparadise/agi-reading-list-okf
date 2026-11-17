---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 1.7. Machine intelligence tests
section_role: other
section_index: 10
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "This section surveys proposed tests of machine intelligence. Given that the measurement of machine intelligence is fundamental to the field of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.7. Machine intelligence tests

> Section 10 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

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

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
