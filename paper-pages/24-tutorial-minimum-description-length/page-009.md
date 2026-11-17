---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 9
pages: [9]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Figure 1.1: A simple, a complex and a trade-oﬀ(3rd degree) polynomial. This intuition is confirmed by numerous experiments on real-world data from a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 9 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 9 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Figure 1.1: A simple, a complex and a trade-oﬀ(3rd degree) polynomial.

This intuition is confirmed by numerous experiments on real-world data from a broad variety of sources \[Rissanen 1989; Vapnik 1998; Ripley 1996\]: if one naively fits a highdegree polynomial to a small sample (set of data points), then one obtains a very good fit to the data. Yet if one tests the inferred polynomial on a second set of data coming from the same source, it typically fits this test data very badly in the sense that there is a large distance between the polynomial and the new data points. We say that the polynomial overfits the data. Indeed, all model selection methods that are used in practice either implicitly or explicitly choose a trade-oﬀbetween goodness-of-fit and complexity of the models involved. In practice, such trade-oﬀs lead to much better predictions of test data than one would get by adopting the ‘simplest’ (one degree) or most ‘complex3’ (n −1-degree) polynomial. MDL provides one particular means of achieving such a trade-oﬀ.

It will be useful to make a precise distinction between ‘model’ and ‘hypothesis’:

Models vs. Hypotheses We use the phrase point hypothesis to refer to a single probability distribution or function. An example is the polynomial 5x2 + 4x + 3. A point hypothesis is also known as a ‘simple hypothesis’ in the statistical literature. We use the word model to refer to a family (set) of probability distributions or functions with the same functional form. An example is the set of all seconddegree polynomials. A model is also known as a ‘composite hypothesis’ in the statistical literature. We use hypothesis as a generic term, referring to both point hypotheses and models.

In our terminology, the problem described in Example 1.2 is a ‘hypothesis selection problem’ if we are interested in selecting both the degree of a polynomial and the corresponding parameters; it is a ‘model selection problem’ if we are mainly interested in

10

---

[previous page](page-008.md) · [next page](page-010.md) · [all pages](index.md)
