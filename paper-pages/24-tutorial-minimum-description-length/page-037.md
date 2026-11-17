---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 37
pages: [37]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "sequence most. Two-part codes are universal (Section 2.5.1), but there exist other universal codes such as the Bayesian mixture code (Section 2.5.2)…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 37 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 37 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

sequence most. Two-part codes are universal (Section 2.5.1), but there exist other universal codes such as the Bayesian mixture code (Section 2.5.2) and the Normalized Maximum Likelihood (NML) code (Section 2.5.3). We also discuss universal models, which are just the probability distributions corresponding to universal codes. In this section, we are not concerned with learning from data; we only care about compressing data as much as possible. We reconnect our findings with learning in Section 2.6.

Coding as Communication Like many other topics in coding, ‘universal coding’ can best be explained if we think of descriptions as messages: we can always view a description as a message that some sender or encoder, say Mr. A, sends to some receiver or decoder, say Mr. B. Before sending any messages, Mr. A and Mr. B meet in person. They agree on the set of messages that A may send to B. Typically, this will be the set X n of sequences x1, . . . , xn, where each xi is an outcome in the space X . They also agree upon a (prefix) code that will be used by A to send his messages to B. Once this has been done, A and B go back to their respective homes and A sends his messages to B in the form of binary strings. The unique decodability property of prefix codes implies that, when B receives a message, he should always be able to decode it in a unique manner.

Universal Coding Suppose our encoder/sender is about to observe a sequence xn ∈ X n which he plans to compress as much as possible. Equivalently, he wants to send an encoded version of xn to the receiver using as few bits as possible. Sender and receiver have a set of candidate codes L for X n available14. They believe or hope that one of these codes will allow for substantial compression of xn. However, they must decide on a code for X n before sender observes the actual xn, and they do not know which code in L will lead to good compression of the actual xn. What is the best thing they can do? They may be tempted to try the following: upon seeing xn, sender simply encodes/sends xn using the L ∈L that minimizes L(xn) among all L ∈L. But this naive scheme will not work: since decoder/receiver does not know what xn

has been sent before decoding the message, he does not know which of the codes in L has been used by sender/encoder. Therefore, decoder cannot decode the message: the resulting protocol does not constitute a uniquely decodable, let alone a prefix code. Indeed, as we show below, in general no code ¯L exists such that for all xn ∈X n,

¯L(xn) ≤minL∈L L(xn): in words, there exists no code which, no matter what xn is, always mimics the best code for xn.

Example 2.9 Suppose we think that our sequence can be reasonably well-compressed by a code corresponding to some biased coin model. For simplicity, we restrict ourselves to a finite number of such models. Thus, let L = {L1, . . . , L9} where L1 is the code length function corresponding to the Bernoulli model P(· | θ) with parameter θ = 0.1, L2 corresponds to θ = 0.2 and so on. From (2.7) we see that, for example,

L8(xn) = −log P(xn|0.8) = −n\[0\] log 0.2 −n\[1\] log 0.8 L9(xn) = −log P(xn|0.9) = −n\[0\] log 0.1 −n\[1\] log 0.9.

38

---

[previous page](page-036.md) · [next page](page-038.md) · [all pages](index.md)
