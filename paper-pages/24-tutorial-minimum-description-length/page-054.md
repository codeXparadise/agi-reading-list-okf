---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 54
pages: [54]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "pick the model minimizing −log ¯Pnml(xn | M(k)) over all k ∈{1, 2, . . . }, but in some cases this gives unintended results. To illustrate, consider…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 54 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 54 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

pick the model minimizing −log ¯Pnml(xn | M(k)) over all k ∈{1, 2, . . . }, but in some cases this gives unintended results. To illustrate, consider the extreme case that every M(k) contains just one distribution. For example, let M(1) = {P1}, M(2) = {P2}, . . . where {P1, P2, . . . } is the set of all Markov chains with rational-valued parameters. In that case, COMPn(M(k)) = 0 for all k, and we would always select the maximum likelihood Markov chain that assigns probability 1 to data xn. Typically this will be a chain of very high order, severely overfitting the data. This cannot be right! A better idea is to pick the model minimizing

−log ¯Pnml(xn | M(k)) + L(k), (2.32)

where L is the codelength function of some code for encoding model indices k. We would typically choose the standard prior for the integers, L(k) = 2 log k+1, Example 2.4. By using (2.32) we avoid the overfitting problem mentioned above: if M(1) = {P1}, M(2) = {P2}, . . . where P1, P2, . . . is a list of all the rational-parameter Markov chains, (2.32) would reduce to two-part code MDL (Section 2.4) which is asymptotically consistent. On the other hand, if M(k) represents the set of k-th order Markov chains, the term L(k) is typically negligible compared to COMPn(M(k)), the complexity term associated with M(k) that is hidden in −log ¯Pnml(M(k)): thus, the complexity of M(k) comes from the fact that for large k, M(k) contains many distinguishable distributions; not from the much smaller term L(k) ≈2 log k.

To make our previous approach for a finite set of models compatible with (2.32), we can reinterpret it as follows: we assign uniform codelengths (a uniform prior) to the M(1), . . . , M(M) under consideration, so that for k = 1, . . . , M, L(k) = log M. We then pick the model minimizing (2.32). Since L(k) is constant over k, it plays no role in the minimization and can be dropped from the equation, so that our procedure reduces to our original refined MDL model selection method. We shall henceforth assume that we always encode the model index, either implicitly (if the number of models is finite) or explicitly. The general principle behind this is explained in Section 2.7.3.

2.7.2 The Infinity Problem

For some of the most commonly used models, the parametric complexity COMP(M) is undefined. A prime example is the Gaussian location model, which we discuss below. As we will see, we can ‘repair’ the situation using the same general idea as in the previous subsection.

Example 2.20 Parametric Complexity of the Normal Distributions Let M be the family of Normal distributions with fixed variance σ2 and varying mean µ, identified by their densities

2πσe−(x−µ)2

P(x|µ) = 1

2σ2 ,

√

55

---

[previous page](page-053.md) · [next page](page-055.md) · [all pages](index.md)
