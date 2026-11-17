---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 25
pages: [25]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "26 BASIC NOTIONS AND NOTATIONS are called intervals. The concatenation 𝑥𝜔 of a finite sequence 𝑥 and an infinite sequence 𝜔 is defined in a natural…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 25 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 25 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

26 BASIC NOTIONS AND NOTATIONS
are called intervals. The concatenation 𝑥𝜔 of a finite sequence 𝑥 and an infinite
sequence 𝜔 is defined in a natural way.
In some contexts it is convenient to consider finite and infinite sequences to-
gether. We use the notation Σ for the set of all finite and infinite sequences of zeros
and ones, i.e., Σ = Ξ ∪ Ω, and Σ𝑥 denotes the set of all finite and infinite extensions
of a string 𝑥.
We consider computable functions whose arguments and values are binary
strings. Unless it is stated otherwise functions are partial (not necessarily total).
A function 𝑓 is called computable if there is a machine (a program, an algorithm)
that for all 𝑥 such that 𝑓 (𝑥) is defined halts on input 𝑥 and outputs the result 𝑓 (𝑥)
and does not halt on all inputs 𝑥 outside the domain of 𝑓 . We also consider com-
putable functions whose arguments and values are finite objects of different type,
like natural numbers, integer numbers, finite graphs etc. We assume that finite
objects are encoded by binary strings. The choice of an encoding is not important
provided different encodings can be translated to each other. The latter means that
we can algorithmically decide whether a string is an encoding of an object and, if
this is the case, we can find an encoding of the same object with respect to the
other encoding.
Sometimes we consider computable functions of infinite objects, like real num-
bers or measures. Such considerations require rigorous definitions of the notion of
computability, which are provided when needed (see below).
A set of finite objects (binary strings, natural numbers etc.) is called computably
enumerable, or just enumerable, if there is a machine (a program, an algorithm)
without input that prints all elements from the set (and no other elements) with
arbitrary delays between printing consecutive elements. The algorithm is not re-
quired to halt even when the set is finite. The order in which the elements are
printed can be arbitrary.
A real number 𝛼 is computable if there exists an algorithm that computes 𝛼
with any given precision: for any given rational 𝜀 > 0 the algorithm must produce a
rational number at distance at most 𝜀 from 𝛼 (in this case we say that the algorithm
computes the number). A real number 𝛼 is lower semicomputable if it can be
represented as a limit of a non-decreasing computable sequence of rational numbers.
An equivalent definition: 𝛼 is lower semicomputable if the set of rational numbers
that are less than 𝛼 is enumerable. A sequence of real numbers is computable if
all its terms are computable, and given any 𝑛 we are able to find an algorithm
computing the 𝑛th number in the sequence. The notion of a lower semicomputable
sequence of reals is defined in an entirely similar way (for any given 𝑛 we have to
find an algorithm that lower semicomputes the 𝑛th number).
We consider measures (more specifically, probability measures, or probability
distributions) on Ω. Every measure can be identified by its values on intervals Ω𝑥.
So measures are identified with non-negative functions 𝑝 on strings which satisfy
the following two conditions: 𝑝(Λ) = 1 and 𝑝(𝑥) = 𝑝(𝑥0) + 𝑝(𝑥1) for all 𝑥. Such
measures are called measures on the binary tree. We consider also semimeasures
on the binary tree, which are probability measures on the space Σ of all finite and
infinite binary sequences. They correspond to functions 𝑝 such that 𝑝(Λ) = 1 and
𝑝(𝑥) > 𝑝(𝑥0)+𝑝(𝑥1). We consider also semimeasures on natural numbers, which are
defined as sequences {𝑝𝑖} of non-negative reals with∑︀ 𝑖∈N 𝑝𝑖 6 1. It is natural to

---

[previous page](page-024.md) · [next page](page-026.md) · [all pages](index.md)
