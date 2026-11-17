---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 59
pages: [59]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "possible. The general idea is summarized in Figure 2.4, which provides an (informal) definition of MDL, but only in a restricted context. If we go…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 59 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 59 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

possible. The general idea is summarized in Figure 2.4, which provides an (informal) definition of MDL, but only in a restricted context. If we go beyond that context, these prescriptions cannot be used literally – but extensions in the same spirit suggest themselves. Here is a first example of such an extension:

Example 2.21 \[MDL and Local Maxima in the Likelihood\] In practice we often work with models for which the ML estimator cannot be calculated eﬃciently; or at least, no algorithm for eﬃcient calculation of the ML estimator is known. Examples are finite and Gaussian mixtures and Hidden Markov models. In such cases one typically resorts to methods such as EM or gradient descent, which find a local maximum of the likelihood surface (function) P(xn | θ), leading to a local maximum likelihood estimator (LML) ˙θ(xn). Suppose we need to select between a finite number of such models. We may be tempted to pick the model M maximizing the normalized likelihood

¯Pnml(xn | M). However, if we then plan to use the local estimator ˙θ(xn) for predicting future data, this is not the right thing to do. To see this, note that, if suboptimal estimators ˙θ are to be used, the ability of model M to fit arbitrary data patterns may be severely diminished! Rather than using ¯Pnml, we should redefine it to take into account the fact that ˙θ is not the global ML estimator:

nml(xn):= P(xn | ˙θ(xn))

¯P ′

,

xn∈X n P(xn | ˙θ(xn))

P

leading to an adjusted parametric complexity

P(xn | ˙θ(xn)), (2.37)

X

COMP′

n(M):= log

xn∈X n

which, for every estimator ˙θ diﬀerent from ˆθ must be strictly smaller than COMPn(M).

Summary We have shown how to extend refined MDL beyond the restricted settings of Section 2.6. This uncovered the general principle behind refined MDL for model selection, given in Figure 2.4. General as it may be, it only applies to model selection – in the next section we briefly discuss extensions to other applications.

## 2.8 Beyond Parametric Model Selection

The general principle as given in Figure 2.4 only applies to model selection. It can be extended in several directions. These range over many diﬀerent tasks of inductive inference – we mention prediction, transduction (as defined in \[Vapnik 1998\]), clustering \[Kontkanen, Myllym¨aki, Buntine, Rissanen, and Tirri 2004\] and similarity detection \[Li, Chen, Li, Ma, and Vit´anyi 2003\]. In these areas there has been less research and a ‘definite’ MDL approach has not yet been formulated.

MDL has been developed in some detail for some other inductive tasks: nonparametric inference, parameter estimation and regression and classification problems.

60

---

[previous page](page-058.md) · [next page](page-060.md) · [all pages](index.md)
