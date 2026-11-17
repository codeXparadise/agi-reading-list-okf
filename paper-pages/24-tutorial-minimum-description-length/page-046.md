---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 46
pages: [46]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "2.6.2 Counting Interpretation The parametric complexity can be interpreted as measuring (the log of) the number of distinguishable distributions in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 46 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 46 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

2.6.2 Counting Interpretation

The parametric complexity can be interpreted as measuring (the log of) the number of distinguishable distributions in the model. Intuitively, the more distributions a model contains, the more patterns it can fit well so the larger the risk of overfitting. However, if two distributions are very ‘close’ in the sense that they assign high likelihood to the same patterns, they do not contribute so much to the complexity of the overall model. It seems that we should measure complexity of a model in terms of the number of distributions it contains that are ‘essentially diﬀerent’ (distinguishable), and we now show that COMPn measures something like this. Consider a finite model M with parameter set Θ = {θ1, . . . , θM}. Note that

P(xn|ˆθ(xn)) =

X

X

X

P(xn|θj) =

xn∈X n

j=1..M

xn:ˆθ(xn)=θj

P(ˆθ(xn)̸ = θj|θj).

X

1 − X

X

P(xn|θj)

= M −

j

j=1..M

xn:ˆθ(xn)̸=θj

We may think of P(ˆθ(xn)̸ = θj|θj) as the probability, according to θj, that the data look as if they come from some θ̸ = θj. Thus, it is the probability that θj is mistaken for another distribution in Θ. Therefore, for finite M, Rissanen’s model complexity is the logarithm of the number of distributions minus the summed probability that some θj is ‘mistaken’ for some θ̸ = θj. Now suppose M is i.i.d. By the law of large numbers \[Feller 1968\], we immediately see that the ‘sum of mistake probabilities’ P j P(ˆθ(xn)̸ = θj|θj) tends to 0 as n grows. It follows that for large n, the model complexity converges to log M. For large n, the distributions in M are ‘perfectly distinguishable’ (the probability that a sample coming from one is more representative of another is negligible), and then the parametric complexity COMPn(M) of M is simply the log of the number of distributions in M.

Example 2.16 \[NML vs. Two-part Codes\] Incidentally, this shows that for finite i.i.d. M, the two-part code with uniform prior W on M is asymptotically minimax optimal: for all n, the regret of the 2-part code is log M (Equation 2.11), whereas we just showed that for n →∞, R( ¯Pnml) = COMPn(M) →log M. However, for small n, some distributions in M may be mistaken for one another; the number of distinguishable distributions in M is then smaller than the actual number of distributions, and this is reflected in COMPn(M) being (sometimes much) smaller than log M.

For the more interesting case of parametric models, containing infinitely many distributions, Balasubramanian \[1997, 2004\] has a somewhat diﬀerent counting interpretation of COMPn(M) as a ratio between two volumes. Rissanen and Tabus \[2004\] give a more direct counting interpretation of COMPn(M). These extensions are both based on the asymptotic expansion of ¯Pnml, which we now discuss.

47

---

[previous page](page-045.md) · [next page](page-047.md) · [all pages](index.md)
