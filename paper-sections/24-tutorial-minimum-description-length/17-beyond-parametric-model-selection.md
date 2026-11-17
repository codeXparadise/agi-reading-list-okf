---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 2.8 Beyond Parametric Model Selection
section_role: other
section_index: 17
pages: [59, 60, 61, 62, 63]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "The general principle as given in Figure 2.4 only applies to model selection. It can be extended in several directions. These range over many…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.8 Beyond Parametric Model Selection

> Section 17 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 59-63

The general principle as given in Figure 2.4 only applies to model selection. It can be extended in several directions. These range over many diﬀerent tasks of inductive inference – we mention prediction, transduction (as defined in \[Vapnik 1998\]), clustering \[Kontkanen, Myllym¨aki, Buntine, Rissanen, and Tirri 2004\] and similarity detection \[Li, Chen, Li, Ma, and Vit´anyi 2003\]. In these areas there has been less research and a ‘definite’ MDL approach has not yet been formulated.

MDL has been developed in some detail for some other inductive tasks: nonparametric inference, parameter estimation and regression and classification problems.

60

We give a very brief overview of these - for details we refer to \[Barron, Rissanen, and Yu 1998; Hansen and Yu 2001\] and, for the classification case, \[Gr¨unwald and Langford 2004\].

Non-Parametric Inference Sometimes the model class M is so large that it cannot be finitely parameterized. For example, let X = \[0, 1\] be the unit interval and let M be the i.i.d. model consisting of all distributions on X with densities f such that −log f(x) is a continuous function on X. M is clearly ‘non-parametric’: it cannot be meaningfully parameterized by a connected finite-dimensional parameter set Θ(k) ⊆Rk. We may still try to learn a distribution from M in various ways, for example by histogram density estimation \[Rissanen, Speed, and Yu 1992\] or kernel density estimation \[Rissanen 1989\]. MDL is quite suitable for such applications, in which we typically select a density f from a class M(n) ⊂M, where M(n) grows with n, and every P ∗∈M can be arbitrarily well approximated by members of M(n), M(n+1), . . . in the sense that limn→∞infP ∈M(n) D(P ∗∥P) = 0 \[Barron, Rissanen, and Yu 1998\]. Here D is the Kullback-Leibler divergence \[Cover and Thomas 1991\] between P ∗and P.

MDL Parameter Estimation: Three Approaches The ‘crude’ MDL method (Section 2.4) was a means of doing model selection and parameter estimation at the same time. ‘Refined’ MDL only dealt with selection of models. If instead, or at the same time, parameter estimates are needed, they may be obtained in three diﬀerent ways. Historically the first way \[Rissanen 1989; Hansen and Yu 2001\] was to simply use the refined MDL Principle to pick a parametric model M(k), and then, within M(k), pick the ML estimator ˆθ(k). After all, we associate with M(k) the distribution ¯Pnml with codelengths ‘as close as possible’ to those achieved by the ML estimator. This suggests that within M(k), we should prefer the ML estimator. But upon closer inspection, Figure 2.4 suggests to use a two-part code also to select θ within M(k); namely, we should discretize the parameter space in such a way that the resulting 2-part code achieves the minimax regret among all two-part codes; we then pick the (quantized) θ minimizing the two-part code length. Essentially this approach has been worked out in detail by Barron and Cover \[1991\]. The resulting estimators may be called two-part code MDL estimators. A third possibility is to define predictive MDL estimators such as the Laplace and Jeﬀreys estimators of Example 2.19; once again, these can be understood as an extension of Figure 2.4 \[Barron, Rissanen, and Yu 1998\]. These second and third possibilities are more sophisticated than the first. However, if the model M is finitedimensional parametric and n is large, then both the two-part and the predictive MDL estimators will become indistinguishable from the maximum likelihood estimators. For this reason, it has sometimes been claimed that MDL parameter estimation is just ML parameter estimation. Since for small samples, the estimates can be quite diﬀerent, this statement is misleading.

61

Regression In regression problems we are interested in learning how the values y1, . . . , yn of a regression variable Y depend on the values x1, . . . , xn of the regressor variable X. We assume or hope that there exists some function h : X →Y so that h(X) predicts the value Y reasonably well, and we want to learn such an h from data. To this end, we assume a set of candidate predictors (functions) H. In Example 1.2, we took H to be the set of all polynomials. In the standard formulation of this problem, we take h to express that

Yi = h(Xi) + Zi, (2.38)

where the Zi are i.i.d. Gaussian random variables with mean 0 and some variance σ2, independent of Xi. That is, we assume Gaussian noise: (2.38) implies that the conditional density of y1, . . . , yn, given x1, . . . , xn, is equal to the product of n Gaussian densities:

n

Pn

i=1(yi −h(xi))2

 1

P(yn | xn, σ, h) =

√

exp

−

. (2.39)

2σ2

2πσ

With this choice, the log-likelihood becomes a linear function of the squared error:

n X

−log P(yn | xn, σ, h) = 1

(yi −h(xi))2 + n

2 log 2πσ2. (2.40)

2σ2

i=1

Let us now assume that H = ∪k≥1H(k) where for each k, H(k) is a set of functions h : X →Y. For example, H(k) may be the set of k-th degree polynomials.

With each model H(k) we can associate a set of densities (2.39), one for each (h, σ2) with h ∈H(k) and σ2 ∈R+. Let M(k) be the resulting set of conditional distributions. Each P(· | h, σ2) ∈M(k) is identified by the parameter vector (α0, . . . , αk, σ2) so that h(x):= Pk

j=0 αjxj. By Section 2.7.1, (2.8) MDL tells us to select the model minimizing

−log ¯P(yn | M(k), xn) + L(k) (2.41)

where we may take L(k) = 2 log k + 1, and ¯P(· | M(k), ·) is now a conditional universal model with small minimax regret. (2.41) ignores the codelength of x1, . . . , xn. Intuitively, this is because we are only interested in learning how y depends on x; therefore, we do not care how many bits are needed to encode x. Formally, this may be understood as follows: we really are encoding the x-values as well, but we do so using a fixed code that does not depend on the hypothesis h under consideration. Thus, we are really trying to find the model M(k) minimizing

−log ¯P(yn | M(k), xn) + L(k) + L′(xn)

where L′ represents some code for X n. Since this codelength does not involve k, it can be dropped from the minimization; see Figure 2.5. We will not go into the precise definition of ¯P(yn | M(k), xn). Ideally, it should be an NML distribution, but just as in Example 2.20, this NML distribution is not well-defined. We can get reasonable alternative universal models after all using any of the methods described in Section 2.7.2; see \[Barron, Rissanen, and Yu 1998\] and \[Rissanen 2000\] for details.

62

When the Codelength for xn Can Be Ignored If all models under consideration represent conditional densities or probability mass functions P(Y | X), then the codelength for X1, . . . , Xn can be ignored in model and parameter selection. Examples are applications of MDL in classification and regression.

Figure 2.5: Ignoring codelengths.

‘Non-probabilistic’ Regression and Classification In the approach we just described, we modeled the noise as being normally distributed. Alternatively, it has been tried to directly try to learn functions h ∈H from the data, without making any probabilistic assumptions about the noise \[Rissanen 1989; Barron 1990; Yamanishi 1998; Gr¨unwald 1998; Gr¨unwald 1999\]. The idea is to learn a function h that leads to good predictions of future data from the same source in the spirit of Vapnik’s \[1998\] statistical learning theory. Here prediction quality is measured by some fixed loss function; different loss functions lead to diﬀerent instantiations of the procedure. Such a version of MDL is meant to be more robust, leading to inference of a ‘good’ h ∈H irrespective of the details of the noise distribution. This loss-based approach has also been the method of choice in applying MDL to classification problems. Here Y takes on values in a finite set, and the goal is to match each feature X (for example, a bit map of a handwritten digit) with its corresponding label or class (e.g., a digit). While several versions of MDL for classification have been proposed \[Quinlan and Rivest 1989; Rissanen 1989; Kearns, Mansour, Ng, and Ron 1997\], most of these can be reduced to the same approach based on a 0/1-valued loss function \[Gr¨unwald 1998\]. In recent work \[Gr¨unwald and Langford 2004\] we show that this MDL approach to classification without making assumptions about the noise may behave suboptimally: we exhibit situations where no matter how large n, MDL keeps overfitting, selecting an overly complex model with suboptimal predictive behavior. Modifications of MDL suggested by Barron \[1990\] and Yamanishi \[1998\] do not suﬀer from this defect, but they do not admit a natural coding interpretation any longer. All in all, current versions of MDL that avoid probabilistic assumptions are still in their infancy, and more research is needed to find out whether they can be modified to perform well in more general and realistic settings.

Summary In the previous sections, we have covered basic refined MDL (Section 2.6), general refined MDL (Section 2.7), and several extensions of refined MDL (this section). This concludes our technical description of refined MDL. It only remains to place MDL in its proper context: what does it do compared to other methods of inductive inference? And how well does it perform, compared to other methods? The next two sections are devoted to these questions.

63

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
