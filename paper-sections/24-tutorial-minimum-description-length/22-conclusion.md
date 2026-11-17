---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 2.11 Conclusion
section_role: conclusion
section_index: 22
pages: [70, 71, 72, 73, 74]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "MDL is a versatile method for inductive inference: it can be interpreted in at least four diﬀerent ways, all of which indicate that it does something…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.11 Conclusion

> Section 22 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `conclusion` · pages 70-74

MDL is a versatile method for inductive inference: it can be interpreted in at least four diﬀerent ways, all of which indicate that it does something reasonable. It is typically asymptotically consistent, achieving good rates of convergence. It achieves all

71

this without having been designed for consistency, being based on a philosophy which makes no metaphysical assumptions about the existence of ‘true’ distributions. All this strongly suggests that it is a good method to use in practice. Practical evidence shows that in many contexts it is, in other contexts its behavior can be problematic. In the author’s view, the main challenge for the future is to improve MDL for such cases, by somehow extending and further refining MDL procedures in a non ad-hoc manner. I am confident that this can be done, and that MDL will continue to play an important role in the development of statistical, and more generally, inductive inference.

Further Reading MDL can be found on the web at www.mdl-research.org. Good places to start further exploration of MDL are \[Barron, Rissanen, and Yu 1998\] and \[Hansen and Yu 2001\]. Both papers provide excellent introductions, but they are geared towards a more specialized audience of information theorists and statisticians, respectively. Also worth reading is Rissanen’s \[1989\] monograph. While outdated as an introduction to MDL methods, this famous ‘little green book’ still serves as a great introduction to Rissanen’s radical but appealing philosophy, which is described very eloquently.

Acknowledgments The author would like to thank Jay Myung, Mark Pitt, Steven de Rooij and Teemu Roos, who read a preliminary version of this chapter and suggested several improvements.

## Notes

1. But see Section 2.9.4. 2. Working directly with distributions on infinite sequences is more elegant, but it requires measure theory, which we want to avoid here.

3. Also known as instantaneous codes and called, perhaps more justifiably, ‘prefix-free’ codes in \[Li and Vit´anyi 1997\].

4. For example, with non-integer codelengths the notion of ‘code’ becomes invariant to the size of the alphabet in which we describe data.

5. As understood in elementary probability, i.e. with respect to Lebesgue measure. 6. Even if one adopts a Bayesian stance and postulates that an agent can come up with a (subjective) distribution for every conceivable domain, this problem remains: in practice, the adopted distribution may be so complicated that we cannot design the optimal code corresponding to it, and have to use some ad hoc-instead.

7. Henceforth, we simply use ‘model’ to denote probabilistic models; we typically use H to denote sets of hypotheses such as polynomials, and reserve M for probabilistic models.

8. The terminology ‘crude MDL’ is not standard. It is introduced here for pedagogical reasons, to make clear the importance of having a single, unified principle for designing codes. It should be noted that Rissanen’s and Barron’s early theoretical papers on MDL already contain such principles, albeit in a slightly diﬀerent form than in their recent papers. Early practical applications \[Quinlan and Rivest 1989; Gr¨unwald 1996\] often do use ad hoc two-part codes which really are ‘crude’ in the sense defined here.

9. See the previous endnote. 10. but see \[Gr¨unwald 1998\], Chapter 5 for more discussion.

72

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

74

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
