---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 2.6 Simple Refined MDL and its Four Interpretations
section_role: other
section_index: 15
pages: [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "In Section 2.4, we indicated that ‘crude’ MDL needs to be refined. In Section 2.5 we introduced universal models. We now show how universal models,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.6 Simple Refined MDL and its Four Interpretations

> Section 15 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 43-53

In Section 2.4, we indicated that ‘crude’ MDL needs to be refined. In Section 2.5 we introduced universal models. We now show how universal models, in particular the minimax optimal universal model ¯Pnml, can be used to define a refined version of MDL model selection. Here we only discuss the simplest case: suppose we are given

44

data D = (x1, . . . , xn) and two models M(1) and M(2) such that COMPn(M(1)) and COMPn(M(2)) (Equation 2.17) are both finite. For example, we could have some binary data and M(1) and M(2) are the first- and second-order Markov models (Example 2.7), both considered possible explanations for the data. We show how to deal with an infinite number of models and/or models with infinite COMPn in Section 2.7.

Denote by ¯Pnml(· | M(j)) the NML distribution on X n corresponding to model M(j). Refined MDL tells us to pick the model M(j) maximizing the normalized maximum likelihood ¯Pnml(D | M(j)), or, by (2.18), equivalently, minimizing

−log ¯Pnml(D | M(j)) = −log P(D | ˆθ(j)(D)) + COMPn(M(j)) (2.20)

From a coding theoretic point of view, we associate with each M(j) a code with lengths

¯Pnml(· | M(j)), and we pick the model minimizing the codelength of the data. The codelength −log ¯Pnml(D | M(j)) has been called the stochastic complexity of the data D relative to model M(j) \[Rissanen 1987\], whereas COMPn(M(j)) is called the parametric complexity or model cost of M(j) (in this survey we simply call it ‘complexity’). We have already indicated in the previous section that COMPn(M(j)) measures something like the ‘complexity’ of model M(j). On the other hand, −log P(D | ˆθ(j)(D)) is minus the maximized log-likelihood of the data, so it measures something like (minus) fit or error – in the linear regression case, it can be directly related to the mean squared error, Section 2.8. Thus, (2.20) embodies a trade-oﬀbetween lack of fit (measured by minus log-likelihood) and complexity (measured by COMPn(M(j))). The confidence in the decision is given by the codelength diﬀerence

−log ¯Pnml(D | M(1)) −\[−log ¯Pnml(D | M(2))\]

.

In general, −log ¯Pnml(D | M) can only be evaluated numerically – the only exception this author is aware of is when M is the Gaussian family, Example 2.20. In many cases even numerical evaluation is computationally problematic. But the re-interpretations of ¯Pnml we provide below also indicate that in many cases, −log ¯P(D | M) is relatively easy to approximate.

Example 2.15 \[Refined MDL and GLRT\] Generalized likelihood ratio testing \[Casella and Berger 1990\] tells us to pick the M(j) maximizing log P(D | ˆθ(j)(D)) + c where c is determined by the desired type-I and type-II errors. In practice one often applies a naive variation17, simply picking the model M(j) maximizing log P(D |

ˆθ(j)(D)). This amounts to ignoring the complexity terms COMPn(M(j)) in (2.20): MDL tries to avoid overfitting by picking the model maximizing the normalized rather than the ordinary likelihood. The more distributions in M that fit the data well, the larger the normalization term.

The hope is that the normalization term COMPn(M(j)) strikes the right balance between complexity and fit. Whether it really does depends on whether COMPn is

45

a ‘good’ measure of complexity. In the remainder of this section we shall argue that it is, by giving four diﬀerent interpretations of COMPn and of the resulting trade-oﬀ (2.20):

1. Compression interpretation.

2. Counting interpretation.

3. Bayesian interpretation.

4. Prequential (predictive) interpretation.

2.6.1 Compression Interpretation

Rissanen’s original goal was to select the model that detects the most regularity in the data; he identified this with the ‘model that allows for the most compression of data xn’. To make this precise, a code is associated with each model. The NML code with lengths −log ¯Pnml(· | M(j)) seems to be a very reasonable choice for such a code because of the following two properties:

1. The better the best-fitting distribution in M(j) fits the data, the shorter the codelength −log ¯Pnml(D | M(j)).

2. No distribution in M(j) is given a prior preference over any other distribution, since the regret of ¯Pnml(· | M(j)) is the same for all D ∈X n (Equation (2.19)).

¯Pnml is the only complete prefix code with this property, which may be restated as: ¯Pnml treats all distributions within each M(j) on the same footing!

Therefore, if one is willing to accept the basic ideas underlying MDL as first principles, then the use of NML in model selection is now justified to some extent. Below we give additional justifications that are not directly based on data compression; but we first provide some further interpretation of −log ¯Pnml.

Compression and Separating Structure from Noise We present the following ideas in an imprecise fashion – Rissanen and Tabus \[2004\] recently showed how to make them precise. The stochastic complexity of data D relative to M, given by (2.20) can be interpreted as the amount of information in the data relative to M, measured in bits. Although a one-part codelength, it still consists of two terms: a term COMPn(M) measuring the amount of structure or meaningful information in the data (as ‘seen through M’), and a term −log P(D | ˆθ(D)) measuring the amount of noise or accidental information in the data. To see that this second term measures noise, consider the regression example, Example 1.2, again. As will be seen in Section 2.8, Equation (2.40), in that case −log P(D | ˆθ(D)) becomes equal to a linear function of the mean squared error of the best-fitting polynomial in the set of k-th degree polynomials. To see that the first term measures structure, we reinterpret it below as the number of bits needed to specify a ‘distinguishable’ distribution in M, using a uniform code on all ‘distinguishable’ distributions.

46

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

Asymptotic Expansion of ¯Pnml and COMPn Let M be a k-dimensional parametric model. Under regularity conditions on M and the parameterization Θ →M, to be detailed below, we obtain the following asymptotic expansion of COMPn \[Rissanen 1996; Takeuchi and Barron 1997; Takeuchi and Barron 1998; Takeuchi 2000\]:

COMPn(M) = k

2 log n

2π + log Z

p

|I(θ)|dθ + o(1). (2.21)

θ∈Θ

Here k is the number of parameters (degrees of freedom) in model M, n is the sample size, and o(1) →0 as n →∞. |I(θ)| is the determinant of the k × k Fisher information matrix18 I evaluated at θ. In case M is an i.i.d. model, I is given by

− ∂2

Iij(θ∗):=Eθ∗

log P(X|θ)

θ=θ∗.

∂θi∂θj

This is generalized to non-i.i.d. models as follows:

− ∂2

1

log P(Xn|θ)

Iij(θ∗):= lim

nEθ∗

θ=θ∗.

∂θi∂θj

n→∞

(2.21) only holds if the model M, its parameterization Θ and the sequence x1, x2, . . . all satisfy certain conditions. Specifically, we require:

1. COMPn(M) < ∞and R p

|I(θ)|dθ < ∞;

2. ˆθ(xn) does not come arbitrarily close to the boundary of Θ: for some ǫ > 0, for all large n, ˆθ(xn) remains farther than ǫ from the boundary of Θ.

3. M and Θ satisfy certain further conditions. A simple suﬃcient condition is that M be an exponential family \[Casella and Berger 1990\]. Roughly, this is a family that can be parameterized so that for all x, P(x | β) = exp(βt(x))f(x)g(β), where t : X →R is a function of X. The Bernoulli model is an exponential family, as can be seen by setting β := ln(1 −θ) −ln θ and t(x) = x. Also the multinomial, Gaussian, Poisson, Gamma, exponential, Zipf and many other models are exponential families; but, for example, mixture models are not.

More general conditions are given by Takeuchi and Barron \[1997, 1998, 2000\]. Essentially, if M behaves ‘asymptotically’ like an exponential family, then (2.21) still holds. For example, (2.21) holds for the Markov models and for AR and ARMA processes.

Example 2.17 \[Complexity of the Bernoulli Model\] The Bernoulli model B(0)

can be parameterized in a 1-1 way by the unit interval (Example 2.7). Thus, k = 1. An easy calculation shows that the Fisher information is given by θ(1 −θ). Plugging this into (2.21) and calculating

R p

|θ(1 −θ)|dθ gives

COMPn(B(0)) = 1

2 log n + 1

2 log π

2 −3 + o(1) = 1

2 log n −2.674251935 + o(1).

Computing the integral of the Fisher determinant is not easy in general. Hanson and Fu \[2004\] compute it for several practically relevant models.

48

Whereas for finite M, COMPn(M) remains finite, for parametric models it generally grows logarithmically in n. Since typically −log P(xn | ˆθ(xn)) grows linearly in n, it is still the case that for fixed dimensionality k (i.e. for a fixed M that is k-dimensional) and large n, the part of the codelength −log ¯Pnml(xn | M) due to the complexity of M is very small compared to the part needed to encode data xn with ˆθ(xn). The term R

p

|I(θ)|dθ may be interpreted as the contribution of the functional form of M to the model complexity \[Balasubramanian 2004\]. It does not grow with n so that, when selecting between two models, it becomes irrelevant and can be ignored for very large n. But for small n, it can be important, as can be seen from Example 1.4, Fechner’s and Stevens’ model. Both models have two parameters, yet the

Θ

p

R

|I(θ)|dθ-term is much larger for Fechner’s than for Stevens’ model. In the experiments of Myung, Balasubramanian, and Pitt \[2000\], the parameter set was restricted to 0 < a < ∞, 0 < b < 3 for Stevens’ model and 0 < a < ∞, 0 < b < ∞for Fechner’s model. The variance of the error Z was set to 1 in both models. With these values, the diﬀerence in

Θ

p

R

|I(θ)|dθ is 3.804, which is non-negligible for small samples. Thus, Stevens’ model contains more distinguishable distributions than Fechner’s, and is better able to capture random noise in the data – as Townsend \[1975\] already speculated almost 30 years ago. Experiments suggest that for regression models such as Stevens’ and Fechner’s’, as well as for Markov models and general exponential families, the approximation (2.21) is reasonably accurate already for small samples. But this is certainly not true for general models:

Θ

The Asymptotic Expansion of COMPn Should Be Used with Care! (2.21) does not hold for all parametric models; and for some models for which it does hold, the o(1) term may only converge to 0 only for quite large sample sizes. Foster and Stine \[1999, 2004\] show that the approximation (2.21) is, in general, only valid if k is much smaller than n.

Two-part codes and COMPn(M) We now have a clear guiding principle (minimax regret) which we can use to construct ‘optimal’ two-part codes, that achieve the minimax regret among all two-part codes. How do such optimal two-part codes compare to the NML codelength? Let M be a k-dimensional model. By slightly adjusting the arguments of \[Barron and Cover 1991, Appendix\], one can show that, under regularity conditions, the minimax optimal two-part code ¯P2-p achieves regret

−log ¯P2-p(xn | M) + log P(xn | ˆθ(xn)) = k

2 log n

2π + log Z

p

|I(θ)|dθ + f(k) + o(1),

θ∈Θ

where f : N →R is a bounded positive function satisfying limk→∞f(k) = 0. Thus, for large k, optimally designed two-part codes are about as good as NML. The problem with two-part code MDL is that in practice, people often use much cruder codes with much larger minimax regret.

49

2.6.3 Bayesian Interpretation

The Bayesian method of statistical inference provides several alternative approaches to model selection. The most popular of these is based on Bayes factors \[Kass and Raftery 1995\]. The Bayes factor method is very closely related to the refined MDL approach. Assuming uniform priors on models M(1) and M(2), it tells us to select the model with largest marginal likelihood ¯PBayes(xn | M(j)), where ¯PBayes is as in (2.12), with the sum replaced by an integral, and w(j) is the density of the prior distribution on M(j):

Z

¯PBayes(xn | M(j)) =

P(xn | θ)w(j)(θ)dθ. (2.22)

M is Exponential Family Let now ¯PBayes = ¯PBayes(· | M) for some fixed model M. Under regularity conditions on M, we can perform a Laplace approximation of the integral in (2.12). For the special case that M is an exponential family, we obtain the following expression for the regret \[Jeﬀreys 1961; Schwarz 1978; Kass and Raftery 1995; Balasubramanian 1997\]:

−log ¯PBayes(xn) −\[−log P(xn | ˆθ(xn))\] = k

2 log n

2π −log w(ˆθ) + log q

|I(ˆθ)| + o(1).

(2.23)

Let us compare this with (2.21). Under the regularity conditions needed for (2.21), the quantity on the right of (2.23) is within O(1) of COMPn(M). Thus, the code length achieved with ¯PBayes is within a constant of the minimax optimal −log ¯Pnml(xn). Since −log P(xn | ˆθ(xn)) increases linearly in n, this means that if we compare two models M(1) and M(2), then for large enough n, Bayes and refined MDL select the same model. If we equip the Bayesian universal model with a special prior known as the Jeﬀreys-Bernardo prior \[Jeﬀreys 1946; Bernardo and Smith 1994\],

p

|I(θ)|

wJeﬀreys(θ) =

, (2.24)

p

R

|I(θ)|dθ

θ∈Θ

then Bayes and refined NML become even more closely related: plugging in (2.24) into (2.23), we find that the right-hand side of (2.23) now simply coincides with (2.21). A concrete example of Jeﬀreys’ prior is given in Example 2.19. Jeﬀreys introduced his prior as a ‘least informative prior’, to be used when no useful prior knowledge about the parameters is available \[Jeﬀreys 1946\]. As one may expect from such a prior, it is invariant under continuous 1-to-1 reparameterizations of the parameter space. The present analysis shows that, when M is an exponential family, then it also leads to asymptotically minimax codelength regret: for large n, refined NML model selection becomes indistinguishable from Bayes factor model selection with Jeﬀreys’ prior.

50

M is not an Exponential Family Under weak conditions on M, Θ and the sequence xn, we get the following generalization of (2.23):

−log ¯PBayes(xn | M) =

−log P(xn | ˆθ(xn)) + k

2 log n

2π −log w(ˆθ) + log q

ˆI(xn)

+ o(1). (2.25)

Here ˆI(xn) is the so-called observed information, sometimes also called observed Fisher information; see \[Kass and Voss 1997\] for a definition. If M is an exponential family, then the observed Fisher information at xn coincides with the Fisher information at

ˆθ(xn), leading to (2.23). If M is not exponential, then if data are distributed according to one of the distributions in M, the observed Fisher information still converges with probability 1 to the expected Fisher information. If M is neither exponential, nor are the data actually generated by a distribution in M, then there may be O(1)discrepancies between −log ¯Pnml and −log ¯PBayes even for large n.

2.6.4 Prequential Interpretation

Distributions as Prediction Strategies Let P be a distribution on X n. Applying the definition of conditional probability, we can write for every xn:

n Y

n Y

P(xi)

P(xn) =

P(xi | xi−1), (2.26)

P(xi−1) =

i=1

i=1

so that also

n X

−log P(xn) =

−log P(xi | xi−1) (2.27)

i=1

Let us abbreviate P(Xi = · | Xi−1 = xi−1) to P(Xi | xi−1). P(Xi | xi−1) (capital Xi) is the distribution (not a single number) of Xi given xi−1; P(xi | xi−1) (lower case xi) is the probability (a single number) of actual outcome xi given xi−1. We can think of −log P(xi | xi−1) as the loss incurred when predicting Xi based on the conditional distribution P(Xi | xi−1), and the actual outcome turned out to be xi. Here ‘loss’ is measured using the so-called logarithmic score, also known simply as ‘log loss’. Note that the more likely x is judged to be, the smaller the loss incurred when x actually obtains. The log loss has a natural interpretation in terms of sequential gambling \[Cover and Thomas 1991\], but its main interpretation is still in terms of coding: by (2.27), the codelength needed to encode xn based on distribution P is just the accumulated log loss incurred when P is used to sequentially predict the i-th outcome based on the past (i −1)-st outcomes.

(2.26) gives a fundamental re-interpretation of probability distributions as prediction strategies, mapping each individual sequence of past observations x1, . . . , xi−1 to a probabilistic prediction of the next outcome P(Xi | xi−1). Conversely, (2.26) also shows

51

that every probabilistic prediction strategy for sequential prediction of n outcomes may be thought of as a probability distribution on X n: a strategy is identified with a function mapping all potential initial segments xi−1 to the prediction that is made for the next outcome Xi, after having seen xi−1. Thus, it is a function S : ∪0≤i<nX i →PX , where PX is the set of distributions on X. We can now define, for each i < n, all xi ∈X i, P(Xi | xi−1):=S(xi−1). We can turn these partial distributions into a distribution on X n by sequentially plugging them into (2.26).

Log Loss for Universal Models Let M be some parametric model and let ¯P be some universal model/code relative to M. What do the individual predictions ¯P(Xi | xi−1) look like? Readers familiar with Bayesian statistics will realize that for i.i.d. models, the Bayesian predictive distribution ¯PBayes(Xi | xi−1) converges to the ML distribution P(· | ˆθ(xi−1)); Example 2.19 provides a concrete case. It seems reasonable to assume that something similar holds not just for ¯PBayes but for universal models in general. This in turn suggests that we may approximate the conditional distributions ¯P(Xi | xi−1) of any ‘good’ universal model by the maximum likelihood predictions P(· | ˆθ(xi−1)). Indeed, we can recursively define the ‘maximum likelihood plug-in’ distribution ¯Pplug-in by setting, for i = 1 to n,

¯Pplug-in(Xi = · | xi−1):=P(X = · | ˆθ(xi−1)). (2.28)

Then

n X

−log P(xi | ˆθ(xi−1)). (2.29)

−log ¯Pplug-in(xn):=

i=1

Indeed, it turns out that under regularity conditions on M and xn,

−log ¯Pplug-in(xn) = −log P(xn | ˆθ(xn)) + k

2 log n + O(1), (2.30)

showing that ¯Pplug-in acts as a universal model relative to M, its performance being within a constant of the minimax optimal ¯Pnml. The construction of ¯Pplug-in can be easily extended to non-i.i.d. models, and then, under regularity conditions, (2.30) still holds; we omit the details.

We note that all general proofs of (2.30) that we are aware of show that (2.30) holds with probability 1 or in expectation for sequences generated by some distribution in M \[Rissanen 1984; Rissanen 1986; Rissanen 1989\]. Note that the expressions (2.21) and (2.25) for the regret of ¯Pnml and ¯PBayes hold for a much wider class of sequences; they also hold with probability 1 for i.i.d. sequences generated by suﬃciently regular distributions outside M. Not much is known about the regret obtained by ¯Pplug-in for such sequences, except for some special cases such as if M is the Gaussian model.

52

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

statistics. It may be interpreted as ML estimation based on an extended sample, containing some ‘virtual’ data: an extra 0 and an extra 1.

Even better, a similar calculation shows that if we take λ = 1/2, the resulting estimator is equal to ¯PBayes(Xi | xi−1) defined relative to Jeﬀreys’ prior. Asymptotically,

¯PBayes with Jeﬀreys’ prior achieves the same codelengths as ¯Pnml (Section 2.6.3). It follows that ¯Pplug-in with the slightly modified ML estimator is asymptotically indistinguishable from the optimal universal model ¯Pnml!

For more general models M, such simple modifications of the ML estimator usually do not correspond to a Bayesian predictive distribution; for example, if M is not convex (closed under taking mixtures) then a point estimator (an element of M) typically does not correspond to the Bayesian predictive distribution (a mixture of elements of M). Nevertheless, modifying the ML estimator by adding some virtual data y1, . . . , ym and replacing P(Xi | ˆθ(xi−1)) by P(Xi | ˆθ(xi−1, ym)) in the definition (2.28) may still lead to good universal models. This is of great practical importance, since, using (2.29), −log ¯Pplug-in(xn) is often much easier to compute than −log ¯PBayes(xn).

Summary We introduced the refined MDL Principle for model selection in a restricted setting. Refined MDL amounts to selecting the model under which the data achieve the smallest stochastic complexity, which is the codelength according to the minimax optimal universal model. We gave an asymptotic expansion of stochastic and parametric complexity, and interpreted these concepts in four diﬀerent ways.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
