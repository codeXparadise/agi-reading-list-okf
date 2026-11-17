---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 15
pages: [15]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "3. We Have Only the Data Many (but not all6) other methods of inductive inference are based on the idea that there exists some ‘true state of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 15 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 15 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

3. We Have Only the Data Many (but not all6) other methods of inductive inference are based on the idea that there exists some ‘true state of nature’, typically a distribution assumed to lie in some model H. The methods are then designed as a means to identify or approximate this state of nature based on as little data as possible. According to Rissanen7, such methods are fundamentally flawed. The main reason is that the methods are designed under the assumption that the true state of nature is in the assumed model H, which is often not the case. Therefore, such methods only admit a clear interpretation under assumptions that are typically violated in practice. Many cherished statistical methods are designed in this way - we mention hypothesis testing, minimum-variance unbiased estimation, several non-parametric methods, and even some forms of Bayesian inference – see Example 2.22. In contrast, MDL has a clear interpretation which depends only on the data, and not on the assumption of any underlying ‘state of nature’.

Example 1.5 \[Models that are Wrong, yet Useful\] Even though the models under consideration are often wrong, they can nevertheless be very useful. Examples are the successful ‘Naive Bayes’ model for spam filtering, Hidden Markov Models for speech recognition (is speech a stationary ergodic process? probably not), and the use of linear models in econometrics and psychology. Since these models are evidently wrong, it seems strange to base inferences on them using methods that are designed under the assumption that they contain the true distribution. To be fair, we should add that domains such as spam filtering and speech recognition are not what the fathers of modern statistics had in mind when they designed their procedures – they were usually thinking about much simpler domains, where the assumption that some distribution P ∗∈H is ‘true’ may not be so unreasonable.

4. MDL and Consistency Let H be a probabilistic model, such that each P ∈H is a probability distribution. Roughly, a statistical procedure is called consistent relative to H if, for all P ∗∈H, the following holds: suppose data are distributed according to P ∗. Then given enough data, the learning method will learn a good approximation of P ∗with high probability. Many traditional statistical methods have been designed with consistency in mind (Section 2.3).

The fact that in MDL, we do not assume a true distribution may suggest that we do not care about statistical consistency. But this is not the case: we would still like our statistical method to be such that in the idealized case where one of the distributions in one of the models under consideration actually generates the data, our method is able to identify this distribution, given enough data. If even in the idealized special case where a ‘truth’ exists within our models, the method fails to learn it, then we certainly cannot trust it to do something reasonable in the more general case, where there may not be a ‘true distribution’ underlying the data at all. So: consistency is important in the MDL philosophy, but it is used as a sanity check (for a method that has been developed without making distributional assumptions) rather than as a design principle.

In fact, mere consistency is not suﬃcient. We would like our method to converge to the imagined true P ∗fast, based on as small a sample as possible. Two-part code

16

---

[previous page](page-014.md) · [next page](page-016.md) · [all pages](index.md)
