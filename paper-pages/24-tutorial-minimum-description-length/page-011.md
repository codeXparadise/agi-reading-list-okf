---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 11
pages: [11]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "1.4 Crude and Refined MDL Crude MDL picks the H minimizing the sum L(H)+L(D|H). To make this procedure well-defined, we need to agree on precise…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 11 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 11 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

## 1.4 Crude and Refined MDL

Crude MDL picks the H minimizing the sum L(H)+L(D|H). To make this procedure well-defined, we need to agree on precise definitions for the codes (description methods) giving rise to lengths L(D|H) and L(H). We now discuss these codes in more detail. We will see that the definition of L(H) is problematic, indicating that we somehow need to ‘refine’ our crude MDL Principle.

Definition of L(D|H) Consider a two-part code as described above, and assume for the time being that all H under consideration define probability distributions. If H is a polynomial, we can turn it into a distribution by making the additional assumption that the Y -values are given by Y = H(X)+Z, where Z is a normally distributed noise term.

For each H we need to define a code with length L(· | H) such that L(D|H) can be interpreted as ‘the codelength of D when encoded with the help of H’. It turns out that for probabilistic hypotheses, there is only one reasonable choice for this code. It is the so-called Shannon-Fano code, satisfying, for all data sequences D, L(D|H) = −log P(D|H), where P(D|H) is the probability mass or density of D according to H – such a code always exists, Section 2.2.

Definition of L(H): A Problem for Crude MDL It is more problematic to find a good code for hypotheses H. Some authors have simply used ‘intuitively reasonable’ codes in the past, but this is not satisfactory: since the description length L(H) of any fixed point hypothesis H can be very large under one code, but quite short under another, our procedure is in danger of becoming arbitrary. Instead, we need some additional principle for designing a code for H. In the first publications on MDL \[Rissanen 1978; Rissanen 1983\], it was advocated to choose some sort of minimax code for H, minimizing, in some precisely defined sense, the shortest worst-case total description length L(H) + L(D|H), where the worst-case is over all possible data sequences. Thus, the MDL Principle is employed at a ‘meta-level’ to choose a code for H. However, this code requires a cumbersome discretization of the model space H, which is not always feasible in practice. Alternatively, Barron \[1985\] encoded H by the shortest computer program that, when input D, computes P(D|H). While it can be shown that this leads to similar codelengths, it is computationally problematic. Later, Rissanen \[1984\] realized that these problems could be side-stepped by using a one-part rather than a two-part code. This development culminated in 1996 in a completely precise prescription of MDL for many, but certainly not all practical situations \[Rissanen 1996\]. We call this modern version of MDL refined MDL:

Refined MDL In refined MDL, we associate a code for encoding D not with a single H ∈H, but with the full model H. Thus, given model H, we encode data not in two parts but we design a single one-part code with lengths ¯L(D|H). This code is designed such that whenever there is a member of (parameter in) H that fits the data well, in

12

---

[previous page](page-010.md) · [next page](page-012.md) · [all pages](index.md)
