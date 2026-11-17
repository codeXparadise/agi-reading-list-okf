---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 62
pages: [62]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 63 We return to the inequality of Theorem 26 and to its geometric consequences in Chapter 10. We can…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 62 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 62 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 63
We return to the inequality of Theorem 26 and to its geometric consequences
in Chapter 10.
We can provide a more systematic treatment of the different complexity quan-
tities related to three strings as follows. There are seven basic quantities: three
of them are complexities of individual strings, another three are complexities of
pairs and one more is the complexity of the entire triple. Other quantities such as
conditional complexity and mutual information can be expressed in terms of these
seven complexities. To understand better what requirements these seven quantities
should satisfy, let us make a linear transformation in the 7-dimensional space and
switch to new coordinates. Consider seven variables 𝑎1, 𝑎2, . . . , 𝑎7 that correspond
to 7 regions shown in Fig. 4.
𝑥 𝑦
𝑧
1 2 3
4 5 6
7
Figure 4. New coordinates 𝑎1, 𝑎2, . . . , 𝑎7.
Formally, the coordinate transformation is given by the following equations:
𝐶(𝑥) = 𝑎1 + 𝑎2 + 𝑎4 + 𝑎5,
𝐶(𝑦) = 𝑎2 + 𝑎3 + 𝑎5 + 𝑎6,
𝐶(𝑧) = 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑥, 𝑦) = 𝑎1 + 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6,
𝐶(𝑥, 𝑧) = 𝑎1 + 𝑎2 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑦, 𝑧) = 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑥, 𝑦, 𝑧) = 𝑎1 + 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7.
Indeed, it is easy to see that these equations determine an invertible linear transfor-
mation of R7: each 7-tuple of complexities corresponds to unique value of variables
𝑎1, . . . , 𝑎7.
Conditional complexities and mutual informations could be expressed in terms
of complexities and therefore could be rewritten in new coordinates. For example,
𝐼(𝑥 : 𝑦) = 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦) = 𝑎2 + 𝑎5 and 𝐶(𝑥 | 𝑦) = 𝐶(𝑥, 𝑦) − 𝐶(𝑦) = 𝑎1 + 𝑎4.
What is the intuitive meaning of these new coordinates? It is easy to see that
𝑎1 = 𝐶(𝑥 | 𝑦, 𝑧) (with logarithmic precision). The meaning of 𝑎3 (and 𝑎7) is similar.
The coordinate 𝑎2 is (with the same precision) 𝐼(𝑥 : 𝑦 | 𝑧); coordinates 𝑎4 and 𝑎6
have similar meaning (see Fig. 5). In particular, we conclude that for any strings
𝑥, 𝑦, 𝑧 the corresponding values of coordinates 𝑎1, 𝑎2, 𝑎3, 𝑎4, 𝑎6, 𝑎7 are non-negative
(up to 𝑂(log 𝑛) for strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛).
The coordinate 𝑎5 is more delicate. Informally, we would like to understand
it as the “amount of mutual information in three strings 𝑥, 𝑦, 𝑧”. Sometimes the

---

[previous page](page-061.md) · [next page](page-063.md) · [all pages](index.md)
