---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 6.1 A more flexible prior distribution for the weights
section_role: other
section_index: 10
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "If we use a single Gaussian prior for communicating the noisy weights, we get a relatively simple penalty term, the asymmetric divergence, for the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.1 A more flexible prior distribution for the weights

> Section 10 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

If we use a single Gaussian prior for communicating the noisy weights, we get a relatively simple penalty term, the asymmetric divergence, for the posterior distribution of each noisy weight. Unfortunately, this coding scheme is not flexible enough to capture certain kinds of common structure in the weights. Suppose, for example, that we want a few of the weights to have values near 1 and the rest to have values very close to 0. If the posterior distribution for each weight has low variance (to avoid the extra squared error caused by noise in the weights) we inevitably pay a high code cost for weights because no single Gaussian prior can provide a good model of a spike around 0 and a spike around 1.

If we know in advance that different subsets of the weights are likely to have different distributions, we can use different coding-priors for the different subsets. As MacKay (1992) has demonstrated, it makes sense to use different coding-priors for the input-to-hidden weights and the hidden-to-output weights since the input and output values may have quite different scales. If we do not know in advance which weights should be similar, we can model the weight distribution by an adaptive mixture of Gaussians as proposed by Nowlan and Hinton (1992). During the optimization, the means, variances and mixing proportions in the mixture adapt to model the clusters in the weight values. Simultaneously, the weights adapt to fit the current mixture model so weights get pulled towards the centers of nearby clusters. Suppose, for eaxample, that there are two Gaussians in the mixture. If one gaussian has mean 1 and low variance and the other gaussian has mean 0 and low variance it is very cheap to encode low-variance weights with values near 1 or 0.

Nowlan and Hinton (1992) implicitly assumed that the posterior distribution for each weight has a fixed and negligible variance so they focussed on maximizing the probability density of the mean of the weight under the coding-prior mixture distribution. We now show how their technique can be extended to take into account the variance of the posterior distributions for the weights, assuming that the posterior distributions are still constrained to be single Gaussians. As before, we ignore the cost of communicating the mixture distribution that is to be used for coding the weights.

The mixture prior has the form:

$$P(w) = \sum_i \pi_i P_i(w)$$

where $\pi_i$ is the mixing proportion of Gaussian $P_i$. The asymmetric divergence between the mixture prior and the single Gaussian posterior, $Q$, for a noisy weight is

$$G(P, Q) = \int Q(w) \log \frac{Q(w)}{\sum_i \pi_i P_i(w)} dw$$

The sum inside the log makes this hard to integrate analytically. This is unfortunate since the optimization process requires that we repeatedly evaluate both $G(P, Q)$ and its derivatives with respect to the parameters of $P$ and $Q$. Fortunately, there is a much more tractable expression which is an upper bound on $G$ and can therefore be used in its place. This expression is in terms of the $G_i(P_i, Q)$ the asymmetric divergences between the posterior distribution, $Q$, and each of the Gaussians, $P_i$, in the mixture prior.

$$\hat{G}(P_1, P_2, \ldots, Q) = -\log \sum_i \pi_i e^{-G_i}$$

The way in which $\hat{G}$ depends on the $G_i$ in equation 17 is precisely analogous to the way in which the free energy of a system depends on the energies of the various alternative configurations of the system. Indeed, one way to derive equation 17 is to define a coding scheme in which the code cost resembles a free energy and to then use a lemma from statistical mechanics.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
