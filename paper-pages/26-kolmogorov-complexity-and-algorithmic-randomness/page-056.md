---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 56
pages: [56]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.2. CONDITIONAL COMPLEXITY 57 (with the same precision). 50 Prove that there exists a computable bit sequence 𝑥 such that 𝐶∞(𝑥) is much less than 𝑀…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 56 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 56 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.2. CONDITIONAL COMPLEXITY 57
(with the same precision).
50 Prove that there exists a computable bit sequence 𝑥 such that 𝐶∞(𝑥) is
much less than 𝑀 (𝑥) (and, therefore, much less than 𝐶(𝑥)). More precisely, there
exists a sequence 𝑥𝑚 of computable sequences such that 𝐶∞(𝑥𝑚) = 𝑂(log 𝑚) and
𝑀 (𝑥𝑚) > 𝑚. [Hint: Consider the sequence 𝑥𝑚 = 𝑦𝑚000 . . . , where 𝑦𝑚 is the
lexicographically first string of length 𝑚 that has conditional complexity (given 𝑚)
at least 𝑚.]
51 Prove that for some computable sequence 𝑥 the value of 𝑀 (𝑥) is much
less than 𝐶(𝑥). More precisely, there exist a sequence 𝑥𝑚 of computable sequences
such that 𝑀 (𝑥𝑚) = 𝑂(log 𝑚) and 𝐶(𝑥𝑚) > 𝑚. [Hint: Consider the sequence
𝑥𝑚 = (1BB (𝑚)000 . . . ), where the number of 1s before trailing zeros equals BB (𝑚),
defined on p. 38.]
52 Prove that 𝐶∞(𝑥) 6 2𝑀∞(𝑥) + 𝑂(1). [Hint: Use the same argument as
in Problem 48.]
In fact, the constant 2 in the preceding problem is optimal, as shown in [52].
53 Consider strings of length 𝑛 that have complexity at least 𝑛 (incompressible
strings).
(a) Prove that the number of incompressible strings of length 𝑛 is between 2𝑛−𝑐
and 2𝑛 − 2𝑛−𝑐 (for some 𝑐 and for all 𝑛)
(b) Prove that the cardinality of the set of incompressible strings of length 𝑛
has complexity 𝑛 − 𝑂(1) (note that this implies the statement (a));
(c) Prove that if the string 𝑥 of length 2𝑛 is incompressible, then its halves 𝑥1
and 𝑥2 (of length 𝑛) have complexity 𝑛 − 𝑂(1).
(d) Prove that if a string 𝑥 of length 𝑛 is incompressible, then each its substring
of length 𝑘 has complexity at least 𝑘 − 𝑂(log 𝑛).
(e) Prove that for any constant 𝑐 < 1 all incompressible strings of sufficiently
large length 𝑛 contain a substring of ⌊𝑐 log2 𝑛⌋ zeros.
[Hints: (a) There is at most 2𝑛 − 1 descritions of length less than 𝑛. and part
of them is used for shorter strings: any string of length 𝑛 − 𝑑 (for some 𝑑) has
complexity less than 𝑛. This gives a lower bound for the number of uncompressible
strings. To prove the upper bound, note that strings of length 𝑛 that have prefix
of 𝑘 zeros, could be described by 2 log 𝑘 + (𝑛 − 𝑘) bits.
(b) Let 𝑡 be the shortest description of the number of incompressible strings. If
𝑡 has 𝑛 − 𝑘 bits, then knowing 𝑡 and log 𝑘 additional bits, we can reconstruct first 𝑛
and then the list of all incompressible strings of length 𝑛, so the first incompressible
string has complexity less than 𝑛, a contradiction.
(c) If one part of the string is has a short description, the entire string has a
short description that starts with prefix-free encoding of the difference between the
length and complexity of the compressible part.
(d) If a string has a simple substring, then the entire string can be compressed
(we need to specify the substring, its position and the rest of the string).
(e) Let us count the number of strings of length 𝑛 that do not contain 𝑘 zeros in
a row; a recurrent relation shows that this number grows like a geometric sequence
whose base is the maximal real root of the equation 𝑥 = 2 − (1/𝑥𝑘), and we can
get a bound for complexity of strings that do not have 𝑘 zeros in a row.]

---

[previous page](page-055.md) · [next page](page-057.md) · [all pages](index.md)
