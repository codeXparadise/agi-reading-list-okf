---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 38
pages: [38]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "1.2. ALGORITHMIC PROPERTIES 39 Let us prove the second inequality of the theorem showing that every 𝑡 BB (𝑛) has complexity at least 𝑛 − 𝑂(1). Assume…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 38 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 38 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

1.2. ALGORITHMIC PROPERTIES 39
Let us prove the second inequality of the theorem showing that every 𝑡 > BB (𝑛)
has complexity at least 𝑛 − 𝑂(1). Assume that 𝑡 has a description 𝑢 of length 𝑘; we
need to show that 𝑘 > 𝑛−𝑂(1). Knowing 𝑢 and 𝑛, one can effectively obtain a string
of complexity greater than 𝑛. Indeed, we reconstruct 𝑡 (from 𝑢) and wait 𝑡 steps for
every description of size at most 𝑛. This gives us all strings of complexity at most
𝑛, and we can take some other string. By definition of B (𝑛) we conclude that the
pair (𝑢, 𝑛) has complexity at least 𝑛 − 𝑂(1). On the other hand, this pair can be
described using 𝑘+𝑂(log(𝑛−𝑘)) bits if we join the self-delimited description of 𝑛−𝑘
and 𝑢. Therefore, 𝑘 +𝑂(log(𝑛−𝑘)) > 𝑛−𝑂(1), and (𝑛−𝑘)−𝑂(log(𝑛−𝑘)) 6 𝑂(1),
therefore 𝑛 − 𝑘 6 𝑂(1). (We assumed that 𝑛 > 𝑘, otherwise there is nothing to
prove.) 
This theorem shows that, within to an additive constant in the argument, B (𝑛)
is the maximal running time of the optimal decompressor on descriptions of length
at most 𝑛. A similar function appeared in the literature under the name of “busy
beaver function”. It was introduced by T. Rad´o [149] and is defined usually as the
maximal number of 1s on the tape of Turing machine with 𝑛 states and binary tape
alphabet (1 and blank) after it terminates (starting with blank tape).
More generally, given 𝑛 and any object from the following list we can find any
other object from the list for a little bit smaller value of 𝑛:
(a): the list of all strings of Kolmogorov complexity at most 𝑛 with their
Kolmogorov complexities;
(b): the number of such strings;
(c): B (𝑛);
(d): BB (𝑛);
(e): the list of all strings of length at most 𝑛 in the domain of the optimal
decompressor (the halting problem for the optimal decompressor restricted
to inputs of length at most 𝑛);
(f ): the number of such strings;
(g): the most time-consuming input of length at most 𝑛 for the optimal
decompressor;
(h): the graph 𝑇𝑛 of the function 𝐶(𝑥) on strings 𝑥 of length 𝑛;
(i): the lexicographically first string 𝛾𝑛 of length 𝑛 with Kolmogorov com-
plexity at least 𝑛 (it exists since the number of strings of complexity less
than 𝑛 is less than 2𝑛).
More specifically, the following statement holds.
Theorem 15. The complexity of every object in (a)–(i) is equal to 𝑛 + 𝑂(1).
These objects are equivalent to each other in the following sense: Let 𝑋𝑛 and 𝑌𝑛
are objects described in two items among (a)–(i). Then there is a constant 𝑐 and
an algorithm that given 𝑛 and 𝑋𝑛 finds 𝑌𝑛−𝑐.
Proof. The equivalence of (d), (e), (f) and (g) is easy. Each of the objects (d),
(e), (f) and (g) together with 𝑛 determines the list of all terminating computations
of the optimal decompressor 𝐷 on strings of length at most 𝑛. Indeed, knowing
BB (𝑛) we can run 𝐷 on all inputs of length at most 𝑛 for BB (𝑛) steps. Knowing
(e), that is, the list of strings of length at most 𝑛 in the domain of 𝐷, we can run
𝐷 on all those strings until all the computations terminate (and we know that this
happens). Knowing (f), the number of strings of length at most 𝑛 on which 𝐷
terminates, we run 𝐷 on all strings of length at most 𝑛 until the desired number

---

[previous page](page-037.md) · [next page](page-039.md) · [all pages](index.md)
