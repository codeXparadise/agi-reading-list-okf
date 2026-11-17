---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 10
pages: [10]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "selecting the degree. To apply MDL to polynomial or other types of hypothesis and model selection, we have to make precise the somewhat vague insight…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 10 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 10 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

selecting the degree.

To apply MDL to polynomial or other types of hypothesis and model selection, we have to make precise the somewhat vague insight ‘learning may be viewed as data compression’. This can be done in various ways. In this section, we concentrate on the earliest and simplest implementation of the idea. This is the so-called two-part code version of MDL:

Crude4, Two-part Version of MDL Principle (Informally Stated) Let H(1), H(2), . . . be a list of candidate models (e.g., H(k) is the set of k-th degree polynomials), each containing a set of point hypotheses (e.g., individual polynomials). The best point hypothesis H ∈H(1) ∪H(2) ∪. . . to explain the data D is the one which minimizes the sum L(H) + L(D|H), where

• L(H) is the length, in bits, of the description of the hypothesis; and

• L(D|H) is the length, in bits, of the description of the data when encoded with the help of the hypothesis.

The best model to explain D is the smallest model containing the selected H.

Example 1.3 \[Polynomials, cont.\] In our previous example, the candidate hypotheses were polynomials. We can describe a polynomial by describing its coeﬃcients in a certain precision (number of bits per parameter). Thus, the higher the degree of a polynomial or the precision, the more5 bits we need to describe it and the more ‘complex’ it becomes. A description of the data ‘with the help of’ a hypothesis means that the better the hypothesis fits the data, the shorter the description will be. A hypothesis that fits the data well gives us a lot of information about the data. Such information can always be used to compress the data (Section 2.2). Intuitively, this is because we only have to code the errors the hypothesis makes on the data rather than the full data. In our polynomial example, the better a polynomial H fits D, the fewer bits we need to encode the discrepancies between the actual y-values yi and the predicted y-values H(xi). We can typically find a very complex point hypothesis (large L(H)) with a very good fit (small L(D|H)). We can also typically find a very simple point hypothesis (small L(H)) with a rather bad fit (large L(D|H)). The sum of the two description lengths will be minimized at a hypothesis that is quite (but not too) ‘simple’, with a good (but not perfect) fit.

11

---

[previous page](page-009.md) · [next page](page-011.md) · [all pages](index.md)
