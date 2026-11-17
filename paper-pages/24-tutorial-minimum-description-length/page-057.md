---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 57
pages: [57]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "ˆK(xn) = |ˆµ(xn)|. Then ¯Prnml is defined as, for all xn ∈X n, ¯Pnml(xn|M ˆ K(xn)) ¯Prnml(xn|M) = xn∈Rn ¯Pnml(xn | M ˆ K(xn))dxn . (2.36) R Model…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 57 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 57 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

ˆK(xn) = |ˆµ(xn)|. Then ¯Prnml is defined as, for all xn ∈X n,

¯Pnml(xn|M ˆ K(xn))

¯Prnml(xn|M) =

xn∈Rn ¯Pnml(xn | M ˆ K(xn))dxn . (2.36)

R

Model selection between a finite set of models now proceeds by selecting the model maximizing the re-normalized likelihood (2.36).

Region Indiﬀerence All the approaches considered thus far slightly prefer some regions of the parameter space over others. In spite of its elegance, even the Rissanen renormalization is slightly ‘arbitrary’ in this way: had we chosen the origin of the real line diﬀerently, the same sequence xn would have achieved a diﬀerent codelength −log ¯Prnml(xn | M). In recent work, Liang and Barron \[2004a, 2004b\] consider a novel and quite diﬀerent approach for dealing with infinite COMPn(M) that partially addresses this problem. They make use of the fact that, while Jeﬀreys’ prior is improper (

R p

|I(θ)|dθ is infinite), using Bayes’ rule we can still compute Jeﬀreys’ posterior based on the first few observations, and this posterior turns out to be a proper probability measure after all. Liang and Barron use universal models of a somewhat diﬀerent type than ¯Pnml, so it remains to be investigated whether their approach can be adapted to the form of MDL discussed here.

2.7.3 The General Picture

Section 2.7.1 illustrates that, in all applications of MDL, we first define a single universal model that allows us to code all sequences with length equal to the given sample size. If the set of models is finite, we use the uniform prior. We do this in order to be as ‘honest’ as possible, treating all models under consideration on the same footing. But if the set of models becomes infinite, there exists no uniform prior any more. Therefore, we must choose a non-uniform prior/non-fixed length code to encode the model index. In order to treat all models still ‘as equally as possible’, we should use some code which is ‘close’ to uniform, in the sense that the codelength increases only very slowly with k. We choose the standard prior for the integers (Example 2.4), but we could also have chosen diﬀerent priors, for example, a prior P(k) which is uniform on k = 1..M for some large M, and P(k) ∝k−2 for k > M. Whatever prior we choose, we are forced to encode a slight preference of some models over others; see Section 2.10.1.

Section 2.7.2 applies the same idea, but implemented at a meta-level: we try to associate with M(k) a code for encoding outcomes in X n that achieves uniform (= minimax) regret for every sequence xn. If this is not possible, we still try to assign regret as ‘uniformly’ as we can, by carving up the parameter space in regions with larger and larger minimax regret, and devising a universal code that achieves regret not much larger than the minimax regret achievable within the smallest region containing the ML estimator. Again, the codes we used encoded a slight preference of some regions of the parameter space over others, but our aim was to keep this preference as small as

58

---

[previous page](page-056.md) · [next page](page-058.md) · [all pages](index.md)
