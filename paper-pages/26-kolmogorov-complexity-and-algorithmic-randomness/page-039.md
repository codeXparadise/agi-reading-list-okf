---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 39
pages: [39]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "40 1. PLAIN KOLMOGOROV COMPLEXITY of computations do terminate. Knowing the string (g), we run 𝐷 on that string, count the number of steps 𝑡 and then…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 39 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 39 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

40 1. PLAIN KOLMOGOROV COMPLEXITY
of computations do terminate. Knowing the string (g), we run 𝐷 on that string,
count the number of steps 𝑡 and then run 𝐷 on all other strings of length at most
𝑛 for 𝑡 steps.
Conversely, the list of all halting computations of the optimal decompressor 𝐷
on strings of length at most 𝑛 together with 𝑛 identifies each of the objects (d)–(g),
as well as the objects (a)–(c). Therefore, by transitivity (which is easy to check)
all the objects (d)–(g) are equivalent.
Let us prove now that (a)–(c) are equivalent to each other and equivalent to
(d)–(g). Given the list of strings of complexity at most 𝑛 we can find the number of
them (so (a)→(b)) and the largest number of complexity at most 𝑛 (so (a)→(c)).
It is not that easy to find (a) given (b) and 𝑛. Given 𝑛 and the number of strings
of complexity at most 𝑛 we can reconstruct the list of these strings (generating them
until we obtain the desired number of strings), and find a maximal number among
them ((b)→(c)). But we still do not know Kolmogorov complexity of the generated
strings. We will prove the implication (c)→(a) indirectly, by showing (c)→(d);
we know already that (d) implies (a). This will prove that all objects (a)–(g) are
equivalent.
The implication (c)→(d) follows from Theorem 14. We know that B (𝑛) is an
upper bound for BB (𝑛 − 𝑐) (for appropriate 𝑐). Thus, given 𝑛 and B (𝑛), we can
find BB (𝑛 − 𝑐) as follows: run 𝐷 on all inputs of length at most 𝑛 − 𝑐 within B (𝑛)
steps. Then find BB (𝑛 − 𝑐) as the number of steps in the longest run.
It remains to consider the objects (h) and (i). The implication (a)→(h) is easy.
Indeed, for some constant 𝑐 the complexity of every string of length 𝑛 − 𝑐 does not
exceed 𝑛. If we know the list (a) and 𝑛, then removing all the strings of length
different from 𝑛 − 𝑐 from the list, we get (h) for 𝑛 − 𝑐.
The conversion (h)→(i) is straightforward.
Thus it remains to prove (i)→(a). It is enough to show that given the lex-
icographically first string 𝛾𝑛 of length 𝑛 and complexity at least 𝑛 we can find
BB (𝑛 − 𝑂(1)) or a number greater than BB (𝑛 − 𝑂(1)). This can be done as
follows.
Given 𝛾𝑛 find 𝑛 and for each string 𝑥 of length 𝑛 preceding 𝛾𝑛 in the lexicograph-
ical order find a description 𝑝𝑥 of 𝑥 that has length 𝑛 or less, and find out the running
time 𝑡𝑥 of 𝐷 on 𝑝𝑥. (Note that 𝑝𝑥 may be not the shortest description of 𝑥.) Let 𝑇
be the maximum of 𝑡𝑥 for those 𝑥. We claim that 𝑇 > BB (𝑛 − 𝑐) for some 𝑐 that
does not depend on 𝑛. Assume that this inequality is false, that is, 𝑇 6 BB (𝑛 − 𝑐).
We will prove that then 𝑐 is small. Consider the most time-consuming description
𝛼𝑛−𝑐 of length at most 𝑛 − 𝑐; let 𝑛 − 𝑐 − 𝑑 be its length. Given 𝛼𝑛−𝑐 and 𝑐 + 𝑑 we
can find 𝑛 and BB (𝑛 − 𝑐). From this we can find 𝛾𝑛: run 𝐷 on all strings of length
at most 𝑛 within BB (𝑛 − 𝑐) steps. Consider all the strings of length 𝑛 for which
we have found descriptions of length 𝑛 or less. Then 𝛾𝑛 is the lexicographically
first remaining string (since 𝑇 6 BB (𝑛 − 𝑐) according to our assumption). As the
complexity of 𝛾𝑛 is at least 𝑛 we have 𝑛 6 𝐶(𝛾𝑛) 6 (𝑛 − 𝑐 − 𝑑) + 2 log(𝑐 + 𝑑) + 𝑂(1),
hence (𝑐 + 𝑑) = 𝑂(1).
We have thus proven the equivalence of objects (a)–(h). It remains to prove
that complexity of each of them is 𝑛 + 𝑂(1).
Let 𝑋𝑛 be one of objects (a)–(h). We have just proven that 𝑋𝑛 can be obtained
from 𝛾𝑛+𝑐 and 𝑛 (actually, we do not need 𝑛, as 𝑛 = 𝑙(𝛾𝑛+𝑐) − 𝑐). Therefore,
𝐶(𝑋𝑛) 6 𝐶(𝛾𝑛+𝑐) + 𝑂(1) 6 𝑛 + 𝑂(1).

---

[previous page](page-038.md) · [next page](page-040.md) · [all pages](index.md)
