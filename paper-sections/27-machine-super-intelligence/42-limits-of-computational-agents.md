---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 5. Limits of Computational Agents
section_role: other
section_index: 42
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "One of the reasons for studying mathematical models such as AIXI is to gain insights that may be useful for designing practical artificial…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5. Limits of Computational Agents

> Section 42 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

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

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
