---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 72
pages: [72]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "11. See Section 1.5 of Chapter 1 for a discussion on the role of consistency in MDL. 12. See, for example [Barron and Cover 1991], [Barron 1985] 13.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 72 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 72 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

11. See Section 1.5 of Chapter 1 for a discussion on the role of consistency in MDL. 12. See, for example \[Barron and Cover 1991\], \[Barron 1985\] 13. Strictly speaking, the assumption that n is given in advance (i.e., both encoder and decoder know n) contradicts the earlier requirement that the code to be used for encoding hypotheses is not allowed to depend on n. Thus, strictly speaking, we should first encode some n explicitly, using 2 log n + 1 bits (Example 2.4), and then pick the n (typically, but not necessarily equal to the actual sample size) that allows for the shortest three-part codelength of the data (first encode n, then (k, θ), then the data). In practice this will not significantly alter the chosen hypothesis, unless for some quite special data sequences.

14. As explained in Figure 2.2, we identify these codes with their length functions, which is the only aspect we are interested in.

15. The reason is that, in the full Bernoulli model with parameter θ ∈\[0, 1\], the maximum likelihood estimator is given by n1/n, see Example 2.7. Since the likelihood log P(xn | θ) is a continuous function of θ, this implies that if the frequency n1/n in xn is approximately (but not precisely) j/10, then the ML estimator in the restricted model {0.1, . . . , 0.9} is still given by ˆθ = j/10. Then log P(xn|θ) is maximized by ˆθ = j/10, so that the L ∈L that minimizes codelength corresponds to θ = j/10.

16. What we call ‘universal model’ in this text is known in the literature as a ‘universal model in the individual sequence sense’ – there also exist universal models in an ‘expected sense’, see Section 2.9.1. These lead to slightly diﬀerent versions of MDL.

17. To be fair, we should add that this naive version of GLRT is introduced here for educational purposes only. It is not recommended by any serious statistician!

18. The standard definition of Fisher information \[Kass and Voss 1997\] is in terms of first derivatives of the log-likelihood; for most parametric models of interest, the present definition coincides with the standard one.

19. The author has heard many people say this at many conferences. The reasons are probably historical: while the underlying philosophy has always been diﬀerent, until Rissanen introduced the use of ¯Pnml, most actual implementations of MDL ‘looked’ quite Bayesian.

20. The reason is that the Bayesian and plug-in models can be interpreted as probabilistic sources. The NML and the two-part code models are no probabilistic sources, since ¯P (n) and ¯P (n+1) are not compatible in the sense of Section 2.2.

21. For example, B(0) is better interpretable. 22. We mention \[Hansen and Yu 2000; Hansen and Yu 2001\] reporting excellent behavior of MDL in regression contexts; and \[Allen, Madani, and Greiner 2003; Kontkanen, Myllym¨aki, Silander, and Tirri 1999; Modha and Masry 1998\] reporting excellent behavior of predictive (prequential) coding in Bayesian network model selection and regression. Also, ‘objective Bayesian’ model selection methods are frequently and successfully used in practice \[Kass and Wasserman 1996\]. Since these are based on non-informative priors such as Jeﬀreys’, they often coincide with a version of refined MDL and thus indicate successful performance of MDL.

23. But see Viswanathan., Wallace, Dowe, and Korb \[1999\] who point out that the problem of \[Kearns, Mansour, Ng, and Ron 1997\] disappears if a more reasonable coding scheme is used.

73

---

[previous page](page-071.md) · [next page](page-073.md) · [all pages](index.md)
