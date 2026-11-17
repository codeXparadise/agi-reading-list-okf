---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 66
pages: [66]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "CHAPTER 3 Martin-L¨ of randomness Here we interrupt the exposition of Kolmogorov complexity and its properties and define another basic notion of the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 66 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 66 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

CHAPTER 3
Martin-L¨	of randomness
Here we interrupt the exposition of Kolmogorov complexity and its properties
and define another basic notion of the algorithmic information theory, the notion
of Martin-L¨of random (or “typical”) sequence. This chapter does not refer to the
preceding one and is not used until Chapter 5 where we characterize randomness
in terms of Kolmogorov complexity.
Let us recall some basic facts of measure theory for the case of the Cantor space
of infinite sequences of zeros and ones.
### 3.1. Measures on Ω
Consider the set Ω = BN whose elements are infinite sequences of zeros and
ones. This set is called Cantor space. For a binary string 𝑥 we consider a set Ω𝑥 of
all infinite sequences that have initial segment 𝑥. For example, Ω00 is the set of all
sequences that start with two zeros, and ΩΛ = Ω (where Λ is the empty string).
The sets Ω𝑥 are called intervals. All intervals and all unions of arbitrary families
of intervals are called open subsets of Ω. In this way we get a topology on Ω, and
this topology corresponds to a standard distance function on Ω defined as follows:
the longer common prefix two sequences 𝜔 = 𝜔0𝜔1 . . . and 𝜔′ = 𝜔′
0𝜔′
1 . . . have, the
smaller the distance between them is:
𝑑(𝜔, 𝜔′) = 2−𝑛,
where 𝑛 is the smallest index such that 𝜔𝑛̸ = 𝜔′
𝑛.
66 Prove that topological space Ω is homeomorphic to the Cantor set on the
real line. (This set is obtained from [0, 1] by deleting the middle third, then the
middle thirds of two remaining segments and so on.)
However, we are interested in measure theory rather than topology. A family
of subsets of Ω is called a 𝜎-algebra if it is closed under finite or countable unions
and intersections, and under negation (taking the complement).
A minimal 𝜎-algebra that contains all intervals Ω𝑥 (and therefore all open sets)
is called the algebra of Borel sets.
Consider an arbitrary 𝜎-algebra that contains all intervals. Let 𝜇 be a function
that maps every set in this 𝜎-algebra into a non-negative real number, and has the
following property (called 𝜎-additivity):
if a set 𝐴 is a union of a countable or finite family of disjoint
sets 𝐴0, 𝐴1, 𝐴2, . . . that belong to the 𝜎-algebra on which 𝜇 is
defined, then
𝜇(𝐴) = 𝜇(𝐴0) + 𝜇(𝐴1) + 𝜇(𝐴2) + . . .
(the right-hand side is a finite sum or a converging series with
non-negative terms).
67

---

[previous page](page-065.md) · [next page](page-067.md) · [all pages](index.md)
