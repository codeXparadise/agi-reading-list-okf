---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: "2.7 General Refined MDL: Gluing it All Together"
section_role: other
section_index: 16
pages: [53, 54, 55, 56, 57, 58, 59]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "In the previous section we introduced a ‘refined’ MDL principle based on minimax regret. Unfortunately, this principle can be applied only in very…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.7 General Refined MDL: Gluing it All Together

> Section 16 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 53-59

In the previous section we introduced a ‘refined’ MDL principle based on minimax regret. Unfortunately, this principle can be applied only in very restricted settings. We now show how to extend refined MDL, leading to a general MDL Principle, applicable to a wide variety of model selection problems. In doing so we glue all our previous insights (including ‘crude MDL’) together, thereby uncovering a single general, underlying principle, formulated in Figure 2.4. Therefore, if one understands the material in this section, then one understands the Minimum Description Length Principle.

First, Section 2.7.1, we show how to compare infinitely many models. Then, Section 2.7.2, we show how to proceed for models M for which the parametric complexity is undefined. Remarkably, a single, general idea resides behind our solution of both problems, and this leads us to formulate, in Section 2.7.3, a single, general refined MDL Principle.

2.7.1 Model Selection with Infinitely Many Models

Suppose we want to compare more than two models for the same data. If the number to be compared is finite, we can proceed as before and pick the model M(k) with smallest −log ¯Pnml(xn | M(k)). If the number of models is infinite, we have to be more careful. Say we compare models M(1), M(2), . . . for data xn. We may be tempted to

54

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

extended to sequences x1, . . . , xn by taking product densities. As is well-known \[Casella and Berger 1990\], the ML estimator ˆµ(xn) is equal to the sample mean: ˆµ(xn) = n−1 Pn

i=1 xi. An easy calculation shows that

Z

xn P(xn | ˆµ(xn))dxn = ∞,

COMPn(M) =

where we abbreviated dx1 . . . dxn to dxn. Therefore, we cannot use basic MDL model selection. It also turns out that I(µ) = σ−2 so that

Z

Z

p

p

|I(θ)|dθ =

|I(µ)|dµ = ∞.

µ∈R

Θ

Thus, the Bayesian universal model approach with Jeﬀreys’ prior cannot be applied either. Does this mean that our MDL model selection and complexity definitions break down even in such a simple case? Luckily, it turns out that they can be repaired, as we now show. Barron, Rissanen, and Yu \[1998\] and Foster and Stine \[2001\] show that, for all intervals \[a, b\],

2πσ · √

P(xn | ˆµ(xn))dxn = b −a

Z

√

n. (2.33)

xn:ˆµ(xn)∈\[a,b\]

Suppose for the moment that it is known that ˆµ lies in some set \[−K, K\] for some fixed K. Let MK be the set of conditional distributions thus obtained: MK = {P ′(· | µ) | µ ∈R}, where P ′(xn | µ) is the density of xn according to the normal distribution with mean µ, conditioned on |n−1 P xi| ≤K. By (2.33), the ‘conditional’ minimax regret distribution ¯Pnml(· | MK) is well-defined for all K > 0. That is, for all xn with |ˆµ(xn)| ≤K,

¯Pnml(xn | MK) = P ′(xn | ˆµ(xn))

xn : |ˆµ(xn)|<K P ′(xn | ˆµ(xn))dxn,

R

with regret (or ‘conditional’ complexity),

P ′(xn | ˆµ(xn))dxn = log K + 1

2 log n

Z

COMPn(MK) = log

2π −log σ + 1.

|ˆµ(xn)|<K

This suggests to redefine the complexity of the full model M so that its regret depends on the area in which ˆµ falls. The most straightforward way of achieving this is to define a meta-universal model for M, combining the NML with a two-part code: we encode data by first encoding some value for K. We then encode the actual data xn using the code ¯Pnml(·|MK). The resulting code ¯Pmeta is a universal code for M with lengths

−log ¯Pmeta(xn | MK) + L(K)

−log ¯Pmeta(xn|M):= min

. (2.34)

K

The idea is now to base MDL model selection on ¯Pmeta(·|M) as in (2.34) rather than on the (undefined) ¯Pnml(·|M). To make this work, we need to choose L in a clever

56

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

GENERAL ‘REFINED’ MDL PRINCIPLE for Model Selection Suppose we plan to select between models M(1), M(2), . . . for data D = (x1, . . . , xn). MDL tells us to design a universal code ¯P for X n, in which the index k of M(k) is encoded explicitly. The resulting code has two parts, the two sub-codes being defined such that

1. All models M(k) are treated on the same footing, as far as possible: we assign a uniform prior to these models, or, if that is not a possible, a prior ‘close to’ uniform.

2. All distributions within each M(k) are treated on the same footing, as far as possible: we use the minimax regret universal model ¯Pnml(xn | M(k)). If this model is undefined or too hard to compute, we instead use a diﬀerent universal model that achieves regret ‘close to’ the minimax regret for each submodel of M(k) in the sense of (2.35).

In the end, we encode data D using a hybrid two-part/one-part universal model, explicitly encoding the models we want to select between and implicitly encoding any distributions contained in those models.

Figure 2.4: The Refined MDL Principle.

59

possible. The general idea is summarized in Figure 2.4, which provides an (informal) definition of MDL, but only in a restricted context. If we go beyond that context, these prescriptions cannot be used literally – but extensions in the same spirit suggest themselves. Here is a first example of such an extension:

Example 2.21 \[MDL and Local Maxima in the Likelihood\] In practice we often work with models for which the ML estimator cannot be calculated eﬃciently; or at least, no algorithm for eﬃcient calculation of the ML estimator is known. Examples are finite and Gaussian mixtures and Hidden Markov models. In such cases one typically resorts to methods such as EM or gradient descent, which find a local maximum of the likelihood surface (function) P(xn | θ), leading to a local maximum likelihood estimator (LML) ˙θ(xn). Suppose we need to select between a finite number of such models. We may be tempted to pick the model M maximizing the normalized likelihood

¯Pnml(xn | M). However, if we then plan to use the local estimator ˙θ(xn) for predicting future data, this is not the right thing to do. To see this, note that, if suboptimal estimators ˙θ are to be used, the ability of model M to fit arbitrary data patterns may be severely diminished! Rather than using ¯Pnml, we should redefine it to take into account the fact that ˙θ is not the global ML estimator:

nml(xn):= P(xn | ˙θ(xn))

¯P ′

,

xn∈X n P(xn | ˙θ(xn))

P

leading to an adjusted parametric complexity

P(xn | ˙θ(xn)), (2.37)

X

COMP′

n(M):= log

xn∈X n

which, for every estimator ˙θ diﬀerent from ˆθ must be strictly smaller than COMPn(M).

Summary We have shown how to extend refined MDL beyond the restricted settings of Section 2.6. This uncovered the general principle behind refined MDL for model selection, given in Figure 2.4. General as it may be, it only applies to model selection – in the next section we briefly discuss extensions to other applications.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
