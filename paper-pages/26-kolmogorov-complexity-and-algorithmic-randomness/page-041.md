---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 41
pages: [41]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "42 1. PLAIN KOLMOGOROV COMPLEXITY (c) Prove that there is an enumerable set that is not 𝑟-separable (such set does not 𝑚-reduce to the upper graph of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 41 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 41 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

42 1. PLAIN KOLMOGOROV COMPLEXITY
(c) Prove that there is an enumerable set that is not 𝑟-separable (such set does
not 𝑚-reduce to the upper graph of 𝐶). [Hint: there is a pair of disjoint enumerable
inseparable sets.]
13 Following [73], prove that the problems “for a given integer 𝑛 find some
string of complexity at least 𝑛” and “for a given algorithm without input find some
string that is different from its output” (if the algorithm does not terminate, any
string is OK) are equivalent: an oracle that fulfills one of the tasks can be used to
(effectively) fulfill the other. [Hint: given an algorithm, we can provide an upper
bound for the complexity of its output: it is bounded by complexity (and therefore
the length) of the algorithm itself. On the other hand, to provide a string of high
complexity means to provide a string which is guaranteed to be different from the
outputs of finitely many algorithms. At first, this looks like a more difficult task
than for one algorithm (as the oracle does). However, the following trick helps: we
may assume that the outputs are tuples and construct a tuple that differs from the
output of 𝑖-th algorithm in 𝑖-th position.]
14 (Continued.) Prove that both these problems are equivalent to the problem
of computing a fixed-point free function: “for every algorithm construct another
algorithm that computes a different function” (not the same as the first one).
15 (Continued.) Prove that an enumerable oracle can solve these problems if
and only if it solves the halting problem (M. Arslanov proved this result without
using Kolmogorov complexity). [Hint: Assume that an enumerable oracle 𝐴 allows
us to compute strings of arbitrarily high complexity. Then let us compute a string
of complexity at least 𝑛 using this oracle, and look at all elements of 𝐴 that were
questioned during this computation. How many steps are needed to enumerate all
this elements? This is a big number: any 𝑇 greater than this number, has the
Kolmogorov complexity at least 𝑛, since 𝑇 -approximation of 𝐴 can be used instead
of 𝐴. On the other hand, having an oracle for 𝐴, we can find 𝑇 for a given 𝑛.]
Kolmogorov complexity and functions 𝐵 and BB turn out to be useful to study
the the so-called “generic” and “coarse” algorithms that solve the halting problem
for most inputs (the fraction of errors converges to zero), see [11]. The versions
of these functions based on prefix complexity were introduced by G´acs [57], see
also [4] for recent results related to the busy beaver functions for different versions
of Kolmogorov complexity.
We have shown only several (simple) example that show how Kolmogorov com-
plexity is related to computability theory (also called “recursion theory”). This area
now actively grows, so we refer the interested reader to two recent monographs [146]
(by A. Nies) and [49] (by R. Downey and D. Hirschfeldt).
Theorem 15 selects some very special objects among all objects of complexity 𝑛
(in fact, one object up to equivalence described above). At first glance, this seems
strange: our intuition says that all “random” (incompressible) strings of length 𝑛
should be indistinguishable, and any special property of a string could be used to
compress it. However, we have found a very special random string 𝛾𝑛 of length 𝑛.
This paradox can be explained as follows: the individual properties of 𝛾𝑛 does allow
us to find a short description for 𝛾𝑛, but we need the oracle for 0′ to decompress
that description.
We will come back to this question in Section 5.7 discussing “the number of
wisdom” Ω and in Section 14.3 studying two-part descriptions.

---

[previous page](page-040.md) · [next page](page-042.md) · [all pages](index.md)
