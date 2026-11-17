---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 12
pages: [12]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "the sense that L(D | H) is small, then the codelength ¯L(D|H) will also be small. Codes with this property are called universal codes in the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 12 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 12 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

the sense that L(D | H) is small, then the codelength ¯L(D|H) will also be small. Codes with this property are called universal codes in the information-theoretic literature \[Barron, Rissanen, and Yu 1998\]. Among all such universal codes, we pick the one that is minimax optimal in a sense made precise in Section 2.5. For example, the set H(3) of third-degree polynomials is associated with a code with lengths ¯L(· | H(3)) such that, the better the data D are fit by the best-fitting third-degree polynomial, the shorter the codelength ¯L(D | H). ¯L(D | H) is called the stochastic complexity of the data given the model.

Parametric Complexity The second fundamental concept of refined MDL is the parametric complexity of a parametric model H which we denote by COMP(H). This is a measure of the ‘richness’ of model H, indicating its ability to fit random data. This complexity is related to the degrees-of-freedom in H, but also to the geometrical structure of H; see Example 1.4. To see how it relates to stochastic complexity, let, for given data D, ˆH denote the distribution in H which maximizes the probability, and hence minimizes the codelength L(D | ˆH) of D. It turns out that

stochastic complexity of D given H = L(D | ˆH) + COMP(H).

Refined MDL model selection between two parametric models (such as the models of first and second degree polynomials) now proceeds by selecting the model such that the stochastic complexity of the given data D is smallest. Although we used a one-part code to encode data, refined MDL model selection still involves a trade-oﬀbetween two terms: a goodness-of-fit term L(D | ˆH) and a complexity term COMP(H). However, because we do not explicitly encode hypotheses H any more, there is no arbitrariness any more. The resulting procedure can be interpreted in several diﬀerent ways, some of which provide us with rationales for MDL beyond the pure coding interpretation (Sections 2.6.1–2.6.4):

1. Counting/diﬀerential geometric interpretation The parametric complexity of a model is the logarithm of the number of essentially diﬀerent, distinguishable point hypotheses within the model.

2. Two-part code interpretation For large samples, the stochastic complexity can be interpreted as a two-part codelength of the data after all, where hypotheses H are encoded with a special code that works by first discretizing the model space H into a set of ‘maximally distinguishable hypotheses’, and then assigning equal codelength to each of these.

3. Bayesian interpretation In many cases, refined MDL model selection coincides with Bayes factor model selection based on a non-informative prior such as Jeffreys’ prior \[Bernardo and Smith 1994\].

4. Prequential interpretation Refined MDL model selection can be interpreted as selecting the model with the best predictive performance when sequentially predicting unseen test data, in the sense described in Section 2.6.4. This makes it

13

---

[previous page](page-011.md) · [next page](page-013.md) · [all pages](index.md)
