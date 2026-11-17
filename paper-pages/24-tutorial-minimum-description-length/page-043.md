---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 43
pages: [43]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "✷ ¯Pnml is quite literally a ‘normalized maximum likelihood’ distribution: it tries to assign to each xn the probability of xn according to the ML…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 43 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 43 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

✷

¯Pnml is quite literally a ‘normalized maximum likelihood’ distribution: it tries to assign to each xn the probability of xn according to the ML distribution for xn. By (2.10), this is not possible: the resulting ‘probabilities’ add to something larger than 1. But we can normalize these ‘probabilities’ by dividing by their sum P

yn∈X n P(yn | ˆθ(yn)), and then we obtain a probability distribution on X n after all.

Whenever X is finite, the sum COMPn(M) is finite so that the NML distribution is well-defined. If X is countably infinite or continuous-valued, the sum COMPn(M) may be infinite and then the NML distribution may be undefined. In that case, there exists no universal model achieving constant regret as in (2.19). If M is parametric, then ¯Pnml is typically well-defined as long as we suitably restrict the parameter space. The parametric case forms the basis of ‘refined MDL’ and will be discussed at length in the next section.

Summary: Universal Codes and Models Let M be a family of probabilistic sources. A universal model in an individual sequence sense16 relative to M, in this text simply called a ‘universal model for M’, is a sequence of distributions ¯P (1), ¯P (2), . . . on X 1, X 2, . . . respectively, such that for all P ∈M, for all ǫ > 0,

1

−log ¯P (n)(xn) −\[−log P(xn)\]

max xn∈X n

≤ǫ as n →∞.

n

Multiplying both sides with n we see that ¯P is universal if for every P ∈M, the codelength diﬀerence −log ¯P(xn) + log P(xn) increases sublinearly in n. If M is finite, then the two-part, Bayes and NML distributions are universal in a very strong sense: rather than just increasing sublinearly, the codelength diﬀerence is bounded by a constant. We already discussed two-part, Bayesian and minimax optimal (NML) universal models, but there several other types. We mention prequential universal models (Section 2.6.4), the Kolmogorov universal model, conditionalized two-part codes \[Rissanen 2001\] and Cesaro-average codes \[Barron, Rissanen, and Yu 1998\].

## 2.6 Simple Refined MDL and its Four Interpretations

In Section 2.4, we indicated that ‘crude’ MDL needs to be refined. In Section 2.5 we introduced universal models. We now show how universal models, in particular the minimax optimal universal model ¯Pnml, can be used to define a refined version of MDL model selection. Here we only discuss the simplest case: suppose we are given

44

---

[previous page](page-042.md) · [next page](page-044.md) · [all pages](index.md)
