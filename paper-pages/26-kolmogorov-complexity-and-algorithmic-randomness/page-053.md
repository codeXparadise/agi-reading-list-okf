---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 53
pages: [53]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "54 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY at most 𝑛. The number of these strings does not exceed 2𝑛−𝑘, and we can apply Theorem 19, p.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 53 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 53 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

54 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
at most 𝑛. The number of these strings does not exceed 2𝑛−𝑘, and we can apply
Theorem 19, p. 50.]
Using this problem, we can prove the following statement about unconditional
complexity (see [102, Exercises 4.3.9, 4.3.10]):
40 Let 𝐷 be some optimal unconditional decompressor. Then there exists
some constant 𝑐 such that for any string 𝑥 the number of shortest 𝐷-descriptions
of 𝑥 does not exceed 𝑐.
[Hint: The previous problems show that 𝐶(𝑥) 6 𝑛 − 𝑘 + 2 log 𝑘 + 𝑂(1), so for
𝐶(𝑥) = 𝑛 we get an upper bound for 𝑘.]
41 Prove that there exists a constant 𝑐 with the following property: if for
some 𝑥 and 𝑛 the probability of the event 𝐶(𝑥 | 𝑦) 6 𝑘 (all strings 𝑦 of lengths 𝑛 are
considered as equiprobable here) is at least 2−𝑙, then 𝐶(𝑥 | 𝑛, 𝑙) 6 𝑘 + 𝑙 + 𝑐. [Hint:
Connect each string 𝑦 of length 𝑛 to all strings 𝑥 such that 𝐶(𝑥 | 𝑦) 6 𝑘. We get
a bipartite graph that has 𝑂(2𝑛+𝑘) edges. In this graph the number of vertices 𝑥
that have degree at least 2𝑛−𝑙 does not exceed 𝑂(2𝑘+𝑙). Note that 𝐶(𝑥 | 𝑛, 𝑙) does
not include 𝑘—this is not a typo!]
This problem could help us to find the average value of 𝐶(𝑥 | 𝑦) for given 𝑥 and
all string 𝑦 of some length 𝑛. It is evident that 𝐶(𝑥 | 𝑦) 6 𝐶(𝑥 | 𝑛) + 𝑂(1) since
𝑛 = 𝑙(𝑦) is determined by 𝑦. It turns out that for most strings 𝑦 (of given length)
this inequality is close to an equality:
42 Prove that there exists some constant 𝑐 such that for each string 𝑥 and for
all natural numbers 𝑛 and 𝑑 the fraction of strings 𝑦 such that 𝐶(𝑥 | 𝑦) < 𝐶(𝑥 | 𝑛)−𝑑
(among all strings of length 𝑛) does not exceed 𝑐𝑑2/2𝑑. Using this statement, prove
that the average value of 𝐶(𝑥 | 𝑦) taken over all strings 𝑦 of a given length 𝑛 equals
𝐶(𝑥 | 𝑛) + 𝑂(1) (the constant in 𝑂(1) does not depend on 𝑥 and 𝑛).
43 Prove that 𝐶(𝑥 | 𝑘) 6 𝑘 implies 𝐶(𝑥) 6 𝑘 + 𝑂(1). [Hint: See Theorem 7.
One can also note that if a conditional description of 𝑥 given 𝑘 has length 𝑘, then 𝑘
is known anyway, and if this description is shorter, we have enough space to specify
the difference between 𝑘 and the description length.]
A similar (though not identical) statement:
44 Prove that 𝐶(𝑥) = 𝐶(𝑥 | 𝐶(𝑥)) + 𝑂(1). [Hint: Assume that 𝑥 has a condi-
tional description 𝑞 with condition 𝐶(𝑥) that is shorter than 𝐶(𝑥). Then one can
specify 𝑥 by providing 𝑞 and the difference 𝐶(𝑥) − 𝑙(𝑞), and we get a description of
𝑥 that is shorter than 𝐶(𝑥)—a contradiction.]
45 Prove that for every 𝑛 there exists a 𝑛-bit string 𝑥 such that
𝐶(𝐶(𝑥) | 𝑥) = log 𝑛 − 𝑂(1).
(This is a maximal possible value, since 𝐶(𝑥) 6 𝑛 for 𝑛-bit string 𝑥.)
This result (in a bit weaker form) was proven long ago by P. G´acs [55]. Re-
cently E. Kalinina and B. Bauwens suggested a simple game-theoretic proof of this
statement. Here is a sketch is this argument (see [6] for details). Consider a rectan-
gular game board of width 2𝑛 and height 𝑛. Two players, White and Black, make
alternating moves and place pawns of their respective colors into the board cells.
Unlike chess, each cell may contain both white and black pawns (at most one of
each color). At each move player may place several pawns into different cells (or no

---

[previous page](page-052.md) · [next page](page-054.md) · [all pages](index.md)
