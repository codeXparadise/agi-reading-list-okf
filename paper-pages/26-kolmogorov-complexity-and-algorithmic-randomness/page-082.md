---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 82
pages: [82]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 83 This problem is related to the definition of randomness suggested by C. Schnorr in [165]. He gave a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 82 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 82 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 83
This problem is related to the definition of randomness suggested by C. Schnorr
in [165]. He gave a more restrictive definition of an effectively null set than Martin-
L¨of. The additional requirement: for every (rational) 𝜀 > 0 the total measure of
corresponding intervals is not only less than 𝜀 but also is a computable real (and the
approximation algorithm computably depends on 𝜀). This requirement is equivalent
to the following one: for every 𝜀 > 0 and 𝛿 > 0 one can effectively find out how
many terms in the series∑︀ 𝑖 𝑝(𝑥(𝜀, 𝑖)) are needed to make the tail less than 𝛿.
(For a series with non-negative terms the computability of sum is equivalent to
computable convergence.)
By Schnorr effectively null sets we mean the effectively null sets according
to this modified definition. (Schnorr calls them total rekursive Nullmenge, see
Definition 8.1 in [165]; effectively null sets (as in the Martin-L¨of defintion) are
called rekursive Nullmenge, see Definition 4.1.)
88 Let us change the definition of an effectively null set in another way: now
we require that the total measure of all intervals in the covering is exactly 𝜀. Show
that this definition is equivalent to the definition of Schnorr effectively null set.
(One can also consider the measure of the union of all intervals instead of the sum
of measures.)
Problem 87 shows that for every Schorr effectively null set there exists a com-
putable sequence outside this set. (For simplicity let us consider the case of uniform
measure.) On the other hand, every computable sequence (i.e., the singleton made
of it) is a Schnorr effectively null set. Therefore, none of the Schnorr effectively
null sets is the largest one in the class (in other words, the union of all Schnorr
effectively null sets is not a Schnorr effectively null set). Nevertheless we can call a
sequence which does not belong to any Schnorr null set a Schnorr random sequence
(or “Schnorr typical” sequence).
Since now we have less effectively null sets, we may get the broader class of
random sequences, and it is indeed the case. The following problem (together with
the results of Chapter 5) guarantees that there exist Schnorr random sequences
that are not Martin-L¨of random.
89 Prove that there exists a Schnorr random sequence 𝜔 = 𝜔0𝜔1𝜔2 . . . whose
prefixes have logarithmic complexity, i.e., 𝐶(𝜔0 . . . 𝜔𝑛−1) = 𝑂(log 𝑛).
[Hint: Problem 87 shows how one can construct a computable sequence that
does not belong to a given Schnorr effectively null set. At some point of this
construction we can take into account another Schnorr effectively null set and get
a computable sequence that does not belong to both. (Indeed, we need to take a
sufficiently small cover for the second set that does not go out of the safety margin
in the construction for the first set.) Moreover, we can consider infinitely many
Schnorr effectively null sets in this way (adding them one after another). This will
not give us a computable Schnorr random sequnce (it does not exist at all), because
we need additional information that says us which algorithms correspond to Schnorr
effectively null sets and which do not. But if we postpone the introduction of a new
algorithm until the moment when the constructed prefix of our sequence is rather
long, this additional information is logarithmic compared to the prefix length.]
We return to Schnorr’s definition of randomness in Section 9.8 where it is
reformulated in terms of computable martingales.

---

[previous page](page-081.md) · [next page](page-083.md) · [all pages](index.md)
