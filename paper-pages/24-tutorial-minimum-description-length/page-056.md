---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 56
pages: [56]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "manner. A good choice is to encode K′ = log K as an integer, using the standard code for the integers. To see why, note that the regret of ¯Pmeta now…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 56 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 56 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

manner. A good choice is to encode K′ = log K as an integer, using the standard code for the integers. To see why, note that the regret of ¯Pmeta now becomes:

−log ¯Pmeta(xn | M) −\[−log P(xn | ˆµ(xn))\] =

log K + 1

2 log n

2π −log σ + 1 + 2 log⌈log K⌉

min K:log K∈{1,2,... }

+ 1 ≤

log |ˆµ(xn)| + 2 log log |ˆµ(xn)| + 1

2 log n

2π −log σ + 4 ≤

COMPn(M|ˆµ|) + 2 log COMPn(M|ˆµ|) + 3. (2.35)

If we had known a good bound K on |ˆµ| a priori, we could have used the NML model

¯Pnml(· | MK). With ‘maximal’ a priori knowledge, we would have used the model ¯Pnml(· | M|ˆµ|), leading to regret COMPn(M|ˆµ|). The regret achieved by ¯Pmeta is almost as good as this ‘smallest possible regret-with-hindsight’ COMPn(M|ˆµ|): the diﬀerence is much smaller than, in fact logarithmic in, COMPn(M|ˆµ|) itself, no matter what xn we observe. This is the underlying reason why we choose to encode K with log-precision: the basic idea in refined MDL was to minimize worst-case regret, or additional code-length compared to the code that achieves the minimal code-length with hindsight. Here, we use this basic idea on a meta-level: we design a code such that the additional regret is minimized, compared to the code that achieves the minimal regret with hindsight.

This meta-two-part coding idea was introduced by Rissanen \[1996\]. It can be extended to a wide range of models with COMPn(M) = ∞; for example, if the Xi represent outcomes of a Poisson or geometric distribution, one can encode a bound on µ just like in Example 2.20. If M is the full Gaussian model with both µ and σ2 allowed to vary, one has to encode a bound on ˆµ and a bound on ˆσ2. Essentially the same holds for linear regression problems, Section 2.8.

Renormalized Maximum Likelihood Meta-two-part coding is just one possible solution to the problem of undefined COMPn(M). It is suboptimal, the main reason being the use of 2-part codes. Indeed, these 2-part codes are not complete (Section 2.2): they reserve several codewords for the same data D = (x1, . . . , xn) (one for each integer value of log K); therefore, there must exist more eﬃcient (one-part) codes ¯P ′

meta such that for all xn ∈X n, ¯P ′

meta(xn) > ¯Pmeta(xn); in keeping with the idea that we should minimize description length, such alternative codes are preferable. This realization has led to a search for more eﬃcient and intrinsic solutions to the problem. Foster and Stine \[2001\] consider the possibility of restricting the parameter values rather than the data, and develop a general framework for comparing universal codes for models with undefined COMP(M). Rissanen \[2001\] suggests the following elegant solution. He defines the Renormalized Maximum Likelihood (RNML) distribution ¯Prnml. In our Gaussian example, this universal model would be defined as follows. Let ˆK(xn) be the bound on ˆµ(xn) that maximizes ¯Pnml(xn | MK) for the actually given K. That is,

57

---

[previous page](page-055.md) · [next page](page-057.md) · [all pages](index.md)
