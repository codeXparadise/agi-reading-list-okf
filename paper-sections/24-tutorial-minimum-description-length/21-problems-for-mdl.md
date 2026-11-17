---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: "2.10 Problems for MDL?"
section_role: other
section_index: 21
pages: [68, 69, 70]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Some authors have criticized MDL either on conceptual grounds (the idea makes no sense) [Webb 1996; Domingos 1999] or on practical grounds (sometimes…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.10 Problems for MDL?

> Section 21 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 68-70

Some authors have criticized MDL either on conceptual grounds (the idea makes no sense) \[Webb 1996; Domingos 1999\] or on practical grounds (sometimes it does not work very well in practice) \[Kearns, Mansour, Ng, and Ron 1997; Pednault 2003\]. Are these criticisms justified? Let us consider them in turn.

2.10.1 Conceptual Problems: Occam’s Razor

The most-often heard conceptual criticisms are invariably related to Occam’s razor. We have already discussed in Section 1.5 of the previous chapter why we regard these criticisms as being entirely mistaken. Based on our newly acquired technical knowledge of MDL, let us discuss these criticisms a little bit further:

1. ‘Occam’s Razor (and MDL) is arbitrary’ (page 17) If we restrict ourselves to refined MDL for comparing a finite number of models for which the NML distribution is well-defined, then there is nothing arbitrary about MDL - it is exactly clear what codes we should use for our inferences. The NML distribution and its close cousins, the Jeﬀreys’ prior marginal likelihood ¯PBayes and the asymptotic expansion (2.21) are all invariant to continuous 1-to-1 reparameterizations of the model: parameterizing our model in a diﬀerent way (choosing a diﬀerent ‘description language’) does not change the inferred description lengths.

If we go beyond models for which the NML distribution is defined, and/or we compare an infinite set of models at the same time, then some ‘subjectivity’ is introduced – while there are still tough restrictions on the codes that we are allowed to use, all such codes prefer some hypotheses in the model over others. If one does not have an a priori preference over any of the hypotheses, one may interpret this as some arbitrariness being added to the procedure. But this ‘arbitrariness’ is of an infinitely milder sort than the arbitrariness that can be introduced if we allow completely arbitrary codes for the encoding of hypotheses as in crude two-part code MDL, Section 2.4.

Things get more subtle if we are interested not in model selection (find the best order Markov chain for the data) but in infinite-dimensional estimation (find the best Markov chain parameters for the data, among the set B of all Markov chains of each order). In the latter case, if we are to apply MDL, we somehow have to carve up B into subsets M(0) ⊆M(1) ⊆. . . ⊆B. Suppose that we have already chosen M(1) = B(1) as the set of 1-st order Markov chains. We normally take M(0) = B(0) , the set of 0-th order Markov chains (Bernoulli distributions). But we could also have defined M(0) as the set of all 1-st order Markov chains with P(Xi+1 = 1 | Xi = 1) = P(Xi+1 = 0 | Xi = 0). This defines a one-dimensional subset of B(1) that is not equal to B(0). While there are several good reasons21 for choosing B(0) rather than M(0), there may be no indication that B(0) is somehow

69

a priori more likely than M(0). While MDL tells us that we somehow have to carve up the full set B, it does not give us precise guidelines on how to do this – diﬀerent carvings may be equally justified and lead to diﬀerent inferences for small samples. In this sense, there is indeed some form of arbitrariness in this type of MDL applications. But this is unavoidable: we stress that this type of arbitrariness is enforced by all combined model/parameter selection methods - whether they be of the Structural Risk Minimization type \[Vapnik 1998\], AIC-type \[Burnham and Anderson 2002\], cross-validation or any other type. The only alternative is treating all hypotheses in the huge class B on the same footing, which amounts to maximum likelihood estimation and extreme overfitting.

2. ‘Occam’s razor is false’ (page 17) We often try to model real-world situations that can be arbitrarily complex, so why should we favor simple models? We gave in informal answer on page 17 where we claimed that even if the true data generating machinery is very complex, it may be a good strategy to prefer simple models for small sample sizes.

We are now in a position to give one formalization of this informal claim: it is simply the fact that MDL procedures, with their built-in preference for ‘simple’ models with small parametric complexity, are typically statistically consistent achieving good rates of convergence (page 16), whereas methods such as maximum likelihood which do not take model complexity into account are typically in-consistent whenever they are applied to complex enough models such as the set of polynomials of each degree or the set of Markov chains of all orders. This has implications for the quality of predictions: with complex enough models, no matter how many training data we observe, if we use the maximum likelihood distribution to predict future data from the same source, the prediction error we make will not converge to the prediction error that could be obtained if the true distribution were known; if we use an MDL submodel/parameter estimate (Section 2.8), the prediction error will converge to this optimal achieveable error.

Of course, consistency is not the only desirable property of a learning method, and it may be that in some particular settings, and under some particular performance measures, some alternatives to MDL outperform MDL. Indeed this can happen – see below. Yet it remains the case that all methods the author knows of that successfully deal with models of arbitrary complexity have a built-in preference for selecting simpler models at small sample sizes – methods such as Vapnik’s \[1998\] Structural Risk Minimization, penalized minimum error estimators \[Barron 1990\] and the Akaike criterion \[Burnham and Anderson 2002\] all trade-oﬀcomplexity with error on the data, the result invariably being that in this way, good convergence properties can be obtained. While these approaches measure ‘complexity’ in a manner diﬀerent from MDL, and attach diﬀerent relative weights to error on the data and complexity, the fundamental idea of finding a trade-oﬀbetween ‘error’ and ‘complexity’ remains.

70

2.10.2 Practical Problems with MDL

We just described some perceived problems about MDL. Unfortunately, there are also some real ones: MDL is not a perfect method. While in many cases, the methods described here perform very well22 there are also cases where they perform suboptimally compared to other state-of-the-art methods. Often this is due to one of two reasons:

1. An asymptotic formula like (2.21) was used and the sample size was not large enough to justify this \[Navarro 2004\].

2. ¯Pnml was undefined for the models under consideration, and this was solved by cutting oﬀthe parameter ranges at ad hoc values \[Lanterman 2004\].

In these cases the problem probably lies with the use of invalid approximations rather than with the MDL idea itself. More research is needed to find out when the asymptotics and other approximations can be trusted, and what is the ‘best’ way to deal with undefined ¯Pnml. For the time being, we suggest to avoid using (2.21) whenever possible, and to never cut oﬀthe parameter ranges at arbitrary values – instead, if COMPn(M) becomes infinite, then some of the methods described in Section 2.7.2 should be used. Given these restrictions, ¯Pnml and Bayesian inference with Jeﬀreys’ prior are the preferred methods, since they both achieve the minimax regret. If they are either ill-defined or computationally prohibitive for the models under consideration, one can use a prequential method or a sophisticated two-part code such as described by Barron and Cover \[1991\].

MDL and Misspecification However, there is a class of problems where MDL is problematic in a more fundamental sense. Namely, if none of the distributions under consideration represents the data generating machinery very well, then both MDL and Bayesian inference may sometimes do a bad job in finding the ‘best’ approximation within this class of not-so-good hypotheses. This has been observed in practice23

\[Kearns, Mansour, Ng, and Ron 1997; Clarke 2002; Pednault 2003\]. Gr¨unwald and Langford \[2004\] show that MDL can behave quite unreasonably for some classification problems in which the true distribution is not in M. This is closely related to the problematic behavior of MDL for classification tasks as mentioned in Section 2.8. All this is a bit ironic, since MDL was explicitly designed not to depend on the untenable assumption that some P ∗∈M generates the data. But empirically we find that while it generally works quite well if some P ∗∈M generates the data, it may sometimes fail if this is not the case.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
