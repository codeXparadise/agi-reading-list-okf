---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 80
pages: [80]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 81 open set 𝐵 ⊂ Ω consider the set 𝐵′ of all sequences 𝜔 such that 𝐹 −1({𝜔}) ⊂ 𝐵 (the set of sequences…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 80 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 80 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 81
open set 𝐵 ⊂ Ω consider the set 𝐵′ of all sequences 𝜔 such that 𝐹 −1({𝜔}) ⊂ 𝐵
(the set of sequences that do not have a preimage outside 𝐵, i.e., the complement
to the image of the complement of 𝐵). The image of a compact set is a compact
set, therefore 𝐵′ is open. Show that if 𝐵 is a union of an enumerable family of
intervals, then 𝐵′ is also a union of enumerable family of intervals, and Bernoulli
measure of 𝐵′ does not exceed the uniform measure of 𝐵. See also the proof of a
more general statement (Theorem 123, p. 195).]
What can be said about the “complexity” of a ML-random sequence (with
respect to the uniform measure) from the viewpoint of the recursion theory? We
know already that ML-random sequence is not computable. It also cannot be
a characteristic function of an enumerable (recursively enumerable, computably
enumerable) set.
Theorem 36. Let 𝐴 be an enumerable set of natural numbers. Consider its
characteristic sequence 𝑎0𝑎1𝑎2 . . . (𝑎𝑖 = 0 for 𝑖 /∈ 𝐴 and 𝑎𝑖 = 1 for 𝑖 ∈ 𝐴). This
sequence is not ML-random.
Proof. Let 𝑘 be an arbitrary natural number. Let us enumerate the set 𝐴
and see what happens with 𝑘 first bits of its characteristic sequences. As (the
current version of) 𝐴 increases, we get more and more ones in this 𝑘-bit prefix. In
this way we get at most 𝑘 + 1 candidates; at some point we come to a final (true)
one, but we never know that this happened already. Anyway, the set of candidates
is enumerable and the number of candidates does not exceed 𝑘 + 1 (since 𝑘-bit
prefix can have 0 . . . 𝑘 ones). The total measure of these intervals is (𝑘 + 1)/2𝑘 and
therefore can be made arbitrarily small. (Note that the definition of the effectively
null set allows us to enumerate the intervals that form a covering, and this is exactly
what we can do in our case.) 
A natural question arises: in what sense one can provide explicitly a ML-
random sequence? As we have seen, neither computable sequences nor character-
istic sequences of enumerable sets are random. If you are familiar with the basics
of the recursion theory (see, e.g., [182]), you may appreciate the following result:
there exist a ML-random sequence that belongs to the class Σ2 ∩ Π2 of the arith-
metic hierarchy (this class can be also described as the class of all 0′-computable
sequences).
Theorem 37. There exists a 0′-computable sequence that is ML-random with
respect to the uniform measure.
Proof. It is enough to show that for any enumerable set of strings {𝑥0, 𝑥1, . . .}
such that∑︀ 2−𝑙(𝑥𝑖) < 1/2 there exists a 0′-computable sequence that does not have
any of 𝑥𝑖 as a prefix. (Indeed, the largest effective null set has such a covering with
total measure less than 1/2, and any sequence that is not covered is ML-random.)
The intervals Ω𝑥𝑖 are divided into two groups: some of them belong to the left
half of Ω (i.e., 𝑥𝑖 starts with 0) and some belong to the right half. Total measure of
both groups at most 1/2. Therefore, at least one of the groups has total measure
at most 1/4. However, looking at the sequence 𝑥𝑖, we cannot find out which half
has this property (since at any moment new large interval can arrive).
However, 0′-oracle allows us to make this choice, since the event “measure
exceeds 1/4” is enumerable. Then we divide this half into two parts of size 1/4

---

[previous page](page-079.md) · [next page](page-081.md) · [all pages](index.md)
