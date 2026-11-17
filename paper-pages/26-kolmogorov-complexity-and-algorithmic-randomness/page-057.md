---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 57
pages: [57]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "58 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY 54 Prove that (for some constant 𝑐) for every infinite sequence 𝑥0𝑥1𝑥2 . . . of zeros and ones…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 57 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 57 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

58 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
54 Prove that (for some constant 𝑐) for every infinite sequence 𝑥0𝑥1𝑥2 . . . of
zeros and ones there exist infinitely many 𝑛 such that
𝐶(𝑥0𝑥1 . . . 𝑥𝑛−1) 6 𝑛 − log 𝑛 + 𝑐.
Prove that there is a constant 𝑐 and the sequence 𝑥0𝑥1𝑥2 . . . such that
𝐶(𝑥0𝑥1 . . . 𝑥𝑛−1) > 𝑛 − 2 log 𝑛 − 𝑐
for all 𝑛. [Hint: The series∑︀ 1/𝑛 diverges while the series∑︀ (1/𝑛2) converges. For
details see Theorem 95 and 99.]
This result was published by Martin-L¨of [116] for conditional complexity (and
a reference to an earlier unpiblished work in Russian was given for unconditional
complexity; see also [223, Theorem 2.6]).
55 For a string 𝑥 of length 𝑛 let us define 𝑑(𝑥) and 𝑑𝑐(𝑥) as follows:
𝑑(𝑥) = 𝑛 − 𝐶(𝑥) and 𝑑𝑐(𝑥) = 𝑛 − 𝐶(𝑥 | 𝑛).
Show that they are rather close to each other:
𝑑𝑐(𝑥) − 2 log 𝑑𝑐(𝑥) − 𝑂(1) 6 𝑑(𝑥) 6 𝑑𝑐(𝑥) + 𝑂(1).
[Hint: We need to show that 𝐶(𝑥 | 𝑛) = 𝑛−𝑑 implies 𝐶(𝑥) 6 𝑛−𝑑+2 log 𝑑+𝑂(1).
Indeed, let us take the conditional description of 𝑥 of length 𝑛 − 𝑑 and put it after
the self-delimiting description of 𝑑 that has size 2 log 𝑑 + 𝑂(1). Knowing this string,
we can reconstruct 𝑑, then 𝑛 and finally 𝑥.]
56 Prove that 𝑑(𝑥𝑦) = 𝑑(𝑥)+𝑑(𝑦 | 𝑥)+𝑂(log 𝑑(𝑥𝑦)) for every two 𝑛-bit strings
𝑥 and 𝑦. (Here 𝑑(𝑢) = 𝑙(𝑢) − 𝐶(𝑢).) [Hint: use Problem 36.]
The intuitive meaning of the difference between length and complexity as a
kind of “randomness deficiency” is discussed (for different complexity versions) in
## Chapter 5 and Chapter 14.)
57 Prove that for sufficiently large values of a constant 𝑐 the enumerable set
of pairs (𝑥, 𝑦) such that 𝐶(𝑥 | 𝑦) < 𝑐, is Turing complete (one can solve halting
problem using an oracle for such a set). [Hint: Use Problem 15 and the fact that
the output of a program has 𝑂(1) conditional complexity given the program.]
### 2.3. Complexity as the amount of information
As we know (Theorem 18), the conditional complexity 𝐶(𝑦|𝑥) does not exceed
the unconditional one 𝐶(𝑦) (up to a constant). The difference 𝐶(𝑦) − 𝐶(𝑦|𝑥) tells
us how much the knowledge of 𝑦 makes 𝑥 easier to describe. So this difference can
be called the amount of information in 𝑥 about 𝑦. Notation: 𝐼(𝑥 : 𝑦).
Theorem 18 says that 𝐼(𝑥 : 𝑦) is non-negative (up to a constant): there exists
some 𝑐 such that 𝐼(𝑥 : 𝑦) > 𝑐 for all 𝑥 and 𝑦.
58 Let 𝑓 be a computable function. Prove that 𝐼(𝑓 (𝑥) : 𝑦) 6 𝐼(𝑥 : 𝑦) + 𝑐 for
some 𝑐 and for all 𝑥, 𝑦 such that 𝑓 (𝑥) is defined.
A generalization of this statement to probabilistic algorithms is possible.
59 Let 𝑓 (𝑥, 𝑟) be a computable function of two arguments, and 𝑟 is chosen at
random uniformly among 𝑛-bit strings for some 𝑛. Then for each 𝑙 the probability
of the event
𝐼(𝑓 (𝑥, 𝑟) : 𝑦) > 𝐼(𝑥 : 𝑦) + 𝑙
does not exceed 2−𝑙+𝑂(𝐶(𝑛)+𝐶(𝑙)). [Hint: Use the conditional version of Problem 41.]

---

[previous page](page-056.md) · [next page](page-058.md) · [all pages](index.md)
