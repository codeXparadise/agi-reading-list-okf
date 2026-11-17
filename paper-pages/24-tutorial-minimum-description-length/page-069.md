---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 69
pages: [69]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "a priori more likely than M(0). While MDL tells us that we somehow have to carve up the full set B, it does not give us precise guidelines on how to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 69 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 69 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

a priori more likely than M(0). While MDL tells us that we somehow have to carve up the full set B, it does not give us precise guidelines on how to do this – diﬀerent carvings may be equally justified and lead to diﬀerent inferences for small samples. In this sense, there is indeed some form of arbitrariness in this type of MDL applications. But this is unavoidable: we stress that this type of arbitrariness is enforced by all combined model/parameter selection methods - whether they be of the Structural Risk Minimization type \[Vapnik 1998\], AIC-type \[Burnham and Anderson 2002\], cross-validation or any other type. The only alternative is treating all hypotheses in the huge class B on the same footing, which amounts to maximum likelihood estimation and extreme overfitting.

2. ‘Occam’s razor is false’ (page 17) We often try to model real-world situations that can be arbitrarily complex, so why should we favor simple models? We gave in informal answer on page 17 where we claimed that even if the true data generating machinery is very complex, it may be a good strategy to prefer simple models for small sample sizes.

We are now in a position to give one formalization of this informal claim: it is simply the fact that MDL procedures, with their built-in preference for ‘simple’ models with small parametric complexity, are typically statistically consistent achieving good rates of convergence (page 16), whereas methods such as maximum likelihood which do not take model complexity into account are typically in-consistent whenever they are applied to complex enough models such as the set of polynomials of each degree or the set of Markov chains of all orders. This has implications for the quality of predictions: with complex enough models, no matter how many training data we observe, if we use the maximum likelihood distribution to predict future data from the same source, the prediction error we make will not converge to the prediction error that could be obtained if the true distribution were known; if we use an MDL submodel/parameter estimate (Section 2.8), the prediction error will converge to this optimal achieveable error.

Of course, consistency is not the only desirable property of a learning method, and it may be that in some particular settings, and under some particular performance measures, some alternatives to MDL outperform MDL. Indeed this can happen – see below. Yet it remains the case that all methods the author knows of that successfully deal with models of arbitrary complexity have a built-in preference for selecting simpler models at small sample sizes – methods such as Vapnik’s \[1998\] Structural Risk Minimization, penalized minimum error estimators \[Barron 1990\] and the Akaike criterion \[Burnham and Anderson 2002\] all trade-oﬀcomplexity with error on the data, the result invariably being that in this way, good convergence properties can be obtained. While these approaches measure ‘complexity’ in a manner diﬀerent from MDL, and attach diﬀerent relative weights to error on the data and complexity, the fundamental idea of finding a trade-oﬀbetween ‘error’ and ‘complexity’ remains.

70

---

[previous page](page-068.md) · [next page](page-070.md) · [all pages](index.md)
