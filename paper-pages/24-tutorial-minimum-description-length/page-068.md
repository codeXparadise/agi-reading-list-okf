---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 68
pages: [68]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "well it performs compared to such other methods. 2.10 Problems for MDL? Some authors have criticized MDL either on conceptual grounds (the idea makes…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 68 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 68 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

well it performs compared to such other methods.

## 2.10 Problems for MDL?

Some authors have criticized MDL either on conceptual grounds (the idea makes no sense) \[Webb 1996; Domingos 1999\] or on practical grounds (sometimes it does not work very well in practice) \[Kearns, Mansour, Ng, and Ron 1997; Pednault 2003\]. Are these criticisms justified? Let us consider them in turn.

2.10.1 Conceptual Problems: Occam’s Razor

The most-often heard conceptual criticisms are invariably related to Occam’s razor. We have already discussed in Section 1.5 of the previous chapter why we regard these criticisms as being entirely mistaken. Based on our newly acquired technical knowledge of MDL, let us discuss these criticisms a little bit further:

1. ‘Occam’s Razor (and MDL) is arbitrary’ (page 17) If we restrict ourselves to refined MDL for comparing a finite number of models for which the NML distribution is well-defined, then there is nothing arbitrary about MDL - it is exactly clear what codes we should use for our inferences. The NML distribution and its close cousins, the Jeﬀreys’ prior marginal likelihood ¯PBayes and the asymptotic expansion (2.21) are all invariant to continuous 1-to-1 reparameterizations of the model: parameterizing our model in a diﬀerent way (choosing a diﬀerent ‘description language’) does not change the inferred description lengths.

If we go beyond models for which the NML distribution is defined, and/or we compare an infinite set of models at the same time, then some ‘subjectivity’ is introduced – while there are still tough restrictions on the codes that we are allowed to use, all such codes prefer some hypotheses in the model over others. If one does not have an a priori preference over any of the hypotheses, one may interpret this as some arbitrariness being added to the procedure. But this ‘arbitrariness’ is of an infinitely milder sort than the arbitrariness that can be introduced if we allow completely arbitrary codes for the encoding of hypotheses as in crude two-part code MDL, Section 2.4.

Things get more subtle if we are interested not in model selection (find the best order Markov chain for the data) but in infinite-dimensional estimation (find the best Markov chain parameters for the data, among the set B of all Markov chains of each order). In the latter case, if we are to apply MDL, we somehow have to carve up B into subsets M(0) ⊆M(1) ⊆. . . ⊆B. Suppose that we have already chosen M(1) = B(1) as the set of 1-st order Markov chains. We normally take M(0) = B(0) , the set of 0-th order Markov chains (Bernoulli distributions). But we could also have defined M(0) as the set of all 1-st order Markov chains with P(Xi+1 = 1 | Xi = 1) = P(Xi+1 = 0 | Xi = 0). This defines a one-dimensional subset of B(1) that is not equal to B(0). While there are several good reasons21 for choosing B(0) rather than M(0), there may be no indication that B(0) is somehow

69

---

[previous page](page-067.md) · [next page](page-069.md) · [all pages](index.md)
