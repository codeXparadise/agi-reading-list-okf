---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 45
pages: [45]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "a ‘good’ measure of complexity. In the remainder of this section we shall argue that it is, by giving four diﬀerent interpretations of COMPn and of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 45 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 45 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

a ‘good’ measure of complexity. In the remainder of this section we shall argue that it is, by giving four diﬀerent interpretations of COMPn and of the resulting trade-oﬀ (2.20):

1. Compression interpretation.

2. Counting interpretation.

3. Bayesian interpretation.

4. Prequential (predictive) interpretation.

2.6.1 Compression Interpretation

Rissanen’s original goal was to select the model that detects the most regularity in the data; he identified this with the ‘model that allows for the most compression of data xn’. To make this precise, a code is associated with each model. The NML code with lengths −log ¯Pnml(· | M(j)) seems to be a very reasonable choice for such a code because of the following two properties:

1. The better the best-fitting distribution in M(j) fits the data, the shorter the codelength −log ¯Pnml(D | M(j)).

2. No distribution in M(j) is given a prior preference over any other distribution, since the regret of ¯Pnml(· | M(j)) is the same for all D ∈X n (Equation (2.19)).

¯Pnml is the only complete prefix code with this property, which may be restated as: ¯Pnml treats all distributions within each M(j) on the same footing!

Therefore, if one is willing to accept the basic ideas underlying MDL as first principles, then the use of NML in model selection is now justified to some extent. Below we give additional justifications that are not directly based on data compression; but we first provide some further interpretation of −log ¯Pnml.

Compression and Separating Structure from Noise We present the following ideas in an imprecise fashion – Rissanen and Tabus \[2004\] recently showed how to make them precise. The stochastic complexity of data D relative to M, given by (2.20) can be interpreted as the amount of information in the data relative to M, measured in bits. Although a one-part codelength, it still consists of two terms: a term COMPn(M) measuring the amount of structure or meaningful information in the data (as ‘seen through M’), and a term −log P(D | ˆθ(D)) measuring the amount of noise or accidental information in the data. To see that this second term measures noise, consider the regression example, Example 1.2, again. As will be seen in Section 2.8, Equation (2.40), in that case −log P(D | ˆθ(D)) becomes equal to a linear function of the mean squared error of the best-fitting polynomial in the set of k-th degree polynomials. To see that the first term measures structure, we reinterpret it below as the number of bits needed to specify a ‘distinguishable’ distribution in M, using a uniform code on all ‘distinguishable’ distributions.

46

---

[previous page](page-044.md) · [next page](page-046.md) · [all pages](index.md)
