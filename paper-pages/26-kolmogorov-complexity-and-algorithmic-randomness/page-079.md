---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 79
pages: [79]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "80 3. MARTIN-L ¨OF RANDOMNESS Theorem 34. Any ML-random sequence with respect to Bernoulli measure with computable parameters 𝑞, 𝑝 has limit…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 79 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 79 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

80 3. MARTIN-L ¨OF RANDOMNESS
Theorem 34. Any ML-random sequence with respect to Bernoulli measure
with computable parameters 𝑞, 𝑝 has limit frequency 𝑝.
Proof. Indeed, the upper bound for the probability of large deviations (ob-
tained by comparing the given Bernoulli measure with the other one, with shifted
𝑝, see Problem 67, p. 72), gives an explicit bound and an explicit set of intervals,
so we get an effectively null set. 
There are several other properties of ML-randomness with respect to the uni-
form measure:
Theorem 35. Let 𝜔 be a ML-random sequnce with respect to the uniform
measure. Then any other sequence which is obtained from 𝜔 by a finite number of
insertions/deletions/changes, is also ML-random.
Proof. It is enough to show that adding a zero/one in the beginning of a
ML-random sequence or deleting the first term of a ML-random sequence gives a
ML-random sequence. Indeed, assume that sequence 𝜔 is not ML-random, i.e.,
forms an effectively null singleton: for each 𝜀 one can effective construct a covering
by intervals with total measure less than 𝜀. Let us add zero at the beginning of
all these intervals (i.e., the corresponding strings). We get a covering for 0𝜔 whose
measure is twice smaller. This argument shows that if 𝜔 is not ML-random, then
0𝜔 is not ML-random either. (Similar argument works for 1𝜔.)
On the other hand, if we delete the first bit of all strings that form a covering
for 𝜔, we get a family of intervals of twice larger measure that covers 𝜔′ (obtained
from 𝜔 by deleting the first bit). Therefore, 𝜔′ is not ML-random, too. 
81 Prove that by replacing all zeros by ones and vice versa in a ML-random
sequence (with respect to the uniform measure) we get a ML-random sequence.
The folllowing problem shows that a computable subsequence of a ML-random
sequence is ML-random.
82 Let 𝑛0, 𝑛1, 𝑛2, . . . be a computable sequence of different integers (𝑛𝑖̸ = 𝑛𝑗
if 𝑖̸ = 𝑗). Let 𝜔 = 𝜔0𝜔1𝜔2 . . . be a ML-random sequence. Then its subsequence
𝜔|𝑛 = 𝜔𝑛0 𝜔𝑛1 𝜔𝑛2 . . .
is ML-random. [Hint: any interval Ω𝑥 in a cover for 𝜔|𝑛 produces a finite family of
intervals whose union is the set of sequences whose (𝑛0, 𝑛1, . . . , 𝑛𝑖−1)-subsequence
coincides with 𝑥 (here 𝑖 is the length of the string 𝑥). The total measure of these
intervals equals 2−𝑖, the measure of Ω𝑥.]
More general selection rules are consider in Chapter 9 (p. 273) where the fre-
quency approach to the notion of randomness (von Mises’ approach) is considered.
83 Let 𝜔 be a ML-random sequence with respect to the uniform measure. Let
us split 𝜔 into two-bit blocks and then replace blocks 00 by zeros and blocks 01, 10
and 11 by ones. Prove that the resulting sequence is ML-random with respect to
Bernoulli measure with parameters 1/4, 3/4. [Hint. We described a transformation
𝐹 : Ω → Ω. The preimage of any open set 𝑈 is open, and the uniform measure of
that preimage equals the (1/4, 3/4)-measure of the set 𝑈 .]
84 (Continued.) Prove that every ML-random sequence with respect to the
nonuniform Bernoulli (1/4, 3/4)-measure can be obtained in this way from a se-
quence that is ML-random with respect to the uniform measure. [Hint: For any

---

[previous page](page-078.md) · [next page](page-080.md) · [all pages](index.md)
