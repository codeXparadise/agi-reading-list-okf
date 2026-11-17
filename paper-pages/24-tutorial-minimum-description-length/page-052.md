---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 52
pages: [52]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "In general, there is no need to use the ML estimator ˆθ(xi−1) in the definition (2.28). Instead, we may try some other estimator which asymptotically…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 52 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 52 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

In general, there is no need to use the ML estimator ˆθ(xi−1) in the definition (2.28). Instead, we may try some other estimator which asymptotically converges to the ML estimator – it turns out that some estimators considerably outperform the ML estimator in the sense that (2.29) becomes a much better approximation of −log ¯Pnml, see Example 2.19. Irrespective of whether we use the ML estimator or something else, we call model selection based on (2.29) the prequential form of MDL in honor of A.P. Dawid’s ‘prequential analysis’, Section 2.9. It is also known as ‘predictive MDL’. The validity of (2.30) was discovered independently by Rissanen \[1984\] and Dawid \[1984\].

The prequential view gives us a fourth interpretation of refined MDL model selection: given models M(1) and M(2), MDL tells us to pick the model that minimizes the accumulated prediction error resulting from sequentially predicting future outcomes given all the past outcomes.

Example 2.18 \[GLRT and Prequential Model Selection\] How does this diﬀer from the naive version of the generalized likelihood ratio test (GLRT) that we introduced in Example 2.15? In GLRT, we associate with each model the log-likelihood (minus log loss) that can be obtained by the ML estimator. This is the predictor within the model that minimizes log loss with hindsight, after having seen the data. In contrast, prequential model selection associates with each model the log-likelihood (minus log loss) that can be obtained by using a sequence of ML estimators ˆθ(xi−1) to predict data xi. Crucially, the data on which ML estimators are evaluated has not been used in constructing the ML estimators themselves. This makes the prediction scheme ‘honest’ (diﬀerent data are used for training and testing) and explains why it automatically protects us against overfitting.

Example 2.19 \[Laplace and Jeﬀreys\] Consider the prequential distribution for the Bernoulli model, Example 2.7, defined as in (2.28). We show that if we take ˆθ in (2.28) equal to the ML estimator n\[1\]/n, then the resulting ¯Pplug-in is not a universal model; but a slight modification of the ML estimator makes ¯Pplug-in a very good universal model. Suppose that n ≥3 and (x1, x2, x3) = (0, 0, 1) – a not-so-unlikely initial segment according to most θ. Then ¯Pplug-in(X3 = 1 | x1, x2) = P(X = 1 | ˆθ(x1, x2)) = 0, so that by (2.29),

−log ¯Pplug-in(xn) ≥−log ¯Pplug-in(x3 | x1, x2) = ∞,

whence ¯Pplug-in is not universal. Now let us consider the modified ML estimator

ˆθλ(xn):=n\[1\] + λ

n + 2λ . (2.31)

If we take λ = 0, we get the ordinary ML estimator. If we take λ = 1, then an exercise involving beta-integrals shows that, for all i, xi, P(Xi | ˆθ1(xi−1)) = ¯PBayes(Xi | xi−1), where ¯PBayes is defined relative to the uniform prior w(θ) ≡1. Thus ˆθ1(xi−1) corresponds to the Bayesian predictive distribution for the uniform prior. This prediction rule was advocated by the great probabilist P.S. de Laplace, co-originator of Bayesian

53

---

[previous page](page-051.md) · [next page](page-053.md) · [all pages](index.md)
