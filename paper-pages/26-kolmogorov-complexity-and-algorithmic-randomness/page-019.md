---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 19
pages: [19]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "20 WHAT IS THIS BOOK ABOUT? of 𝑁 , therefore 𝐶(𝐵(𝑁 )) 6 𝐶(bin(𝑁 )) + 𝑂(1) 6 𝑙(bin(𝑁 )) + 𝑂(1) 6 log2 𝑁 + 𝑂(1) (the first inequality is provided by…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 19 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 19 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

20 WHAT IS THIS BOOK ABOUT?
of 𝑁 , therefore
𝐶(𝐵(𝑁 )) 6 𝐶(bin(𝑁 )) + 𝑂(1) 6 𝑙(bin(𝑁 )) + 𝑂(1) 6 log2 𝑁 + 𝑂(1)
(the first inequality is provided by Theorem 3, the second one is provided by The-
orem 2; term 𝑂(1) stands for a bounded function). So we obtain
𝑁 < 𝐶(𝐵(𝑁 )) 6 log2 𝑁 + 𝑂(1),
which cannot happen if 𝑁 is large enough. 
Some applications of Kolmogorov complexity
Let us start with a disclaimer: the applications we will talk about are not real
“practical” applications; we just establish relations between Kolmogorov complexity
and other important notions.
Occam’s razor. We start with a philosophical question. What do we mean
when we say that a theory provides a good explanation for some experimental data?
Assume that we are given some experimental data and there are several theories to
explain the data. For example, the data might be the observed positions of planets
in the sky. We can explain them as Ptolemy did, with epicycles and deferents,
introducing extra corrections when needed. On the other hand, we can use the
laws of the modern mechanics. Why do we think that the modern theory is better?
A possible answer: the modern theory can compute the positions of planets with
the same (or even better) accuracy given less parameters. In other words, Kepler’s
achievement is a shorter description of the experimental data.
Roughly speaking, experimenters obtain binary strings and theorists find short
descriptions for them (thus proving upper bounds for complexities of those strings);
the shorter the description is, the better is the theorist.
This approach is sometimes called “Occam’s razor” and is attributed to the
philosopher William of Ockham who said that entities should not be multiplied be-
yond necessity. It is hard to judge whether he would agree with such interpretation
of his words.
We can use the same idea in more practical contexts. Assume that we design
a machine that reads handwritten zip codes on envelopes. We are looking for a
rule that separates, say, images of zeros from images of ones. An image is given as
a Boolean matrix (or a binary string). We have several thousands of images and
for each image we know whether it means 0 or 1. We want to find a reasonable
separating rule (with the hope that it can be applied to the forthcoming images).
What means “reasonable” in this context? If we just list all the images in our list
together with their classification, we get a valid separation rule—at least it works
until we receive a new image—however, the rule is way too long. It is natural to
assume that a reasonable rule must have a short description, that is, it must have
low Kolmogorov complexity.
Foundations of probability theory. The probability theory itself, being
currently a part of measure theory, is mathematically sound and does not need any
extra “foundations”. The difficult questions arise, however, if we try to understand
why this theory could be applied to the real world phenomena and how it should
be applied.
Assume that we toss a coin thousand times (or test some other hardware ran-
dom number generator) and get a bit string of length 1000. If this string contains

---

[previous page](page-018.md) · [next page](page-020.md) · [all pages](index.md)
