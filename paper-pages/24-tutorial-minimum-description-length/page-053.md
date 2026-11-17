---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 53
pages: [53]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "statistics. It may be interpreted as ML estimation based on an extended sample, containing some ‘virtual’ data: an extra 0 and an extra 1. Even…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 53 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 53 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

statistics. It may be interpreted as ML estimation based on an extended sample, containing some ‘virtual’ data: an extra 0 and an extra 1.

Even better, a similar calculation shows that if we take λ = 1/2, the resulting estimator is equal to ¯PBayes(Xi | xi−1) defined relative to Jeﬀreys’ prior. Asymptotically,

¯PBayes with Jeﬀreys’ prior achieves the same codelengths as ¯Pnml (Section 2.6.3). It follows that ¯Pplug-in with the slightly modified ML estimator is asymptotically indistinguishable from the optimal universal model ¯Pnml!

For more general models M, such simple modifications of the ML estimator usually do not correspond to a Bayesian predictive distribution; for example, if M is not convex (closed under taking mixtures) then a point estimator (an element of M) typically does not correspond to the Bayesian predictive distribution (a mixture of elements of M). Nevertheless, modifying the ML estimator by adding some virtual data y1, . . . , ym and replacing P(Xi | ˆθ(xi−1)) by P(Xi | ˆθ(xi−1, ym)) in the definition (2.28) may still lead to good universal models. This is of great practical importance, since, using (2.29), −log ¯Pplug-in(xn) is often much easier to compute than −log ¯PBayes(xn).

Summary We introduced the refined MDL Principle for model selection in a restricted setting. Refined MDL amounts to selecting the model under which the data achieve the smallest stochastic complexity, which is the codelength according to the minimax optimal universal model. We gave an asymptotic expansion of stochastic and parametric complexity, and interpreted these concepts in four diﬀerent ways.

## 2.7 General Refined MDL: Gluing it All Together

In the previous section we introduced a ‘refined’ MDL principle based on minimax regret. Unfortunately, this principle can be applied only in very restricted settings. We now show how to extend refined MDL, leading to a general MDL Principle, applicable to a wide variety of model selection problems. In doing so we glue all our previous insights (including ‘crude MDL’) together, thereby uncovering a single general, underlying principle, formulated in Figure 2.4. Therefore, if one understands the material in this section, then one understands the Minimum Description Length Principle.

First, Section 2.7.1, we show how to compare infinitely many models. Then, Section 2.7.2, we show how to proceed for models M for which the parametric complexity is undefined. Remarkably, a single, general idea resides behind our solution of both problems, and this leads us to formulate, in Section 2.7.3, a single, general refined MDL Principle.

2.7.1 Model Selection with Infinitely Many Models

Suppose we want to compare more than two models for the same data. If the number to be compared is finite, we can proceed as before and pick the model M(k) with smallest −log ¯Pnml(xn | M(k)). If the number of models is infinite, we have to be more careful. Say we compare models M(1), M(2), . . . for data xn. We may be tempted to

54

---

[previous page](page-052.md) · [next page](page-054.md) · [all pages](index.md)
