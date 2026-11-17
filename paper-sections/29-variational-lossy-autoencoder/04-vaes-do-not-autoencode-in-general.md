---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: 2 VAES DO NOT AUTOENCODE IN GENERAL
section_role: other
section_index: 4
pages: [1, 2, 3]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "A VAE is frequently interpreted as a regularized autoencoder (Kingma & Welling, 2013; Zhang et al., 2016), but the conditions under which it is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 VAES DO NOT AUTOENCODE IN GENERAL

> Section 4 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `other` · pages 1-3

A VAE is frequently interpreted as a regularized autoencoder (Kingma & Welling, 2013; Zhang et al., 2016), but the conditions under which it is guaranteed to autoencode (reconstruction being close to original datapoint) are not discussed. In this section, we discuss the often-neglected fact that VAEs do not always autoencode and give explicit reasons why previous attempts to apply VAE in sequence modeling found that the latent code is generally not used unless the decoder is weakened (Bowman et al., 2015; Serban et al., 2016; Fraccaro et al., 2016). The understanding of when VAE does autoencode will be an essential building piece for VLAE.

2.1 TECHNICAL BACKGROUND

Let x be observed variables, z latent variables and let p(x, z) be the parametric model of their joint distribution, called the generative model defined over the variables. Given a dataset X = {x1, ..., xN} we wish to perform maximum likelihood learning of its parameters:

N X

log p(x(i)), (1)

log p(X) =

i=1

but in general this marginal likelihood is intractable to compute or differentiate directly for flexible generative models that have high-dimensional latent variables and flexible priors and likelihoods. A solution is to introduce q(z|x), a parametric inference model defined over the latent variables, and optimize the variational lower bound on the marginal log-likelihood of each observation x:

log p(x) ≥Eq(z|x) \[log p(x, z) −log q(z|x)\] = L(x; θ) (2)

where θ indicates the parameters of p and q models.

There are various ways to optimize the lower bound L(x; θ); for continuous z it can be done efficiently through a re-parameterization of q(z|x) (Kingma & Welling, 2013; Rezende et al., 2014).

This way of optimizing the variational lower bound with a parametric inference network and reparameterization of continuous latent variables is usually called VAE. The “autoencoding” terminology comes from the fact that the lower bound L(x; θ) can be re-arranged:

L(x; θ) = Eq(z|x) \[log p(x, z) −log q(z|x)\] (3)

= Eq(z|x) \[log p(x|z)\] −DKL(q(z|x)||p(z)) (4)

where the first term can be seen as the expectation of negative reconstruction error and the KL divergence term can be seen as a regularizer, which as a whole could be seen as a regularized autoencoder loss with q(z|x) being the encoder and p(x|z) being the decoder. In the context of 2D images modeling, the decoding distribution p(x|z) is usually chosen to be a simple factorized distribution, i.e. p(x|z) = Q

i p(xi|z), and this setup often yields a sharp decoding distribution p(x|z) that tends to reconstruct original datapoint x exactly.

2.2 BITS-BACK CODING AND INFORMATION PREFERENCE

It’s straightforward to see that having a more powerful p(x|z) will make VAE’s marginal generative distribution p(x) =

R

z p(z)p(x|z)dz more expressive. This idea has been explored extensively

2

Published as a conference paper at ICLR 2017

in previous work applying VAE to sequence modeling (Fabius & van Amersfoort, 2014; Chung et al., 2015; Bowman et al., 2015; Serban et al., 2016; Fraccaro et al., 2016; Xu & Sun, 2016), where the decoding distribution is a powerful RNN with autoregressive dependency, i.e., p(x|z) = Q

i p(xi|z, x<i). Since RNNs are universal function approximators and any joint distribution over x admits an autoregressive factorization, the RNN autoregressive decoding distribution can in theory represent any probability distribution even without dependence on z.

However, previous attempts have found it hard to benefit from VAE when using an expressive decoding distribution p(x|z). Indeed it’s documented in detail by Bowman et al. (2015) that in most cases when an RNN autoregressive decoding distribution is used, the latent code z is completely ignored and the model regresses to be a standard unconditional RNN autoregressive distribution that doesn’t depend on the latent code. This phenomenon is commonly attributed to “optimization challenges” of VAE in the literature (Bowman et al., 2015; Serban et al., 2016; Kaae Sønderby et al., 2016) because early in the training the approximate posterior q(z|x) carries little information about datapoint x and hence it’s easy for the model to just set the approximate posterior to be the prior to avoid paying any regularization cost DKL(q(z|x)||p(z)).

Here we present a simple but often-neglected observation that this phenomenon arises not just due to optimization challenges and instead even if we can solve the optimization problems exactly, the latent code should still be ignored at optimum for most practical instances of VAE that have intractable true posterior distributions and sufficiently powerful decoders. It is easiest to understand this observation from a Bits-Back Coding perspective of VAE.

It is well-known that Bits-Back Coding is an information-theoretic view of Variational Inference (Hinton & Van Camp, 1993; Honkela & Valpola, 2004) and specific links have been established between Bits-Back Coding and the Helmholtz Machine/VAE (Hinton & Zemel, 1994; Gregor et al., 2013). Here we briefly relate VAE to Bits-Back Coding for self-containedness:

First recall that the goal of designing an efficient coding protocol is to minimize the expected code length of communicating x. To explain Bits-Back Coding, let’s first consider a more naive coding scheme. VAE can be seen as a way to encode data in a two-part code: p(z) and p(x|z), where z can be seen as the essence/structure of a datum and is encoded first and then the modeling error (deviation from z’s structure) is encoded next. The expected code length under this naive coding scheme for a given data distribution is hence:

Cnaive(x) = Ex∼data,z∼q(z|x) \[−log p(z) −log p(x|z)\] (5)

This coding scheme is, however, inefficient. Bits-Back Coding improves on it by noticing that the encoder distribution q(z|x) can be used to transmit additional information, up to H(q(z|x)) expected nats, as long as the receiver also has access to q(z|x). The decoding scheme works as follows: a receiver first decodes z from p(z), then decodes x from p(x|z) and, by running the same approximate posterior that the sender is using, decodes a secondary message from q(z|x). Hence, to properly measure the code length of VAE’s two-part code, we need to subtract the extra information from q(z|x). Using Bit-Back Coding, the expected code length equates to the negative variational lower bound or the so-called Helmholtz variational free energy, which means minimizing code length is equivalent to maximizing the variational lower bound:

CBitsBack(x) = Ex∼data,z∼q(z|x) \[log q(z|x) −log p(z) −log p(x|z)\] (6)

= Ex∼data \[−L(x)\] (7)

Casting the problem of optimizing VAE into designing an efficient coding scheme easily allows us to reason when the latent code z will be used: the latent code z will be used when the two-part code is an efficient code. Recalling that the lower-bound of expected code length for data is given by the Shannon entropy of data generation distribution: H(data) = Ex∼data \[−log pdata(x)\], we can analyze VAE’s coding efficiency:

CBitsBack(x) = Ex∼data,z∼q(z|x) \[log q(z|x) −log p(z) −log p(x|z)\] (8)

= Ex∼data \[−log p(x) + DKL(q(z|x)||p(z|x))\] (9) ≥Ex∼data \[−log pdata(x) + DKL(q(z|x)||p(z|x))\] (10) = H(data) + Ex∼data \[DKL(q(z|x)||p(z|x))\] (11)

3

Published as a conference paper at ICLR 2017

Since Kullback Leibler divergence is always non-negative, we know that using the two-part code derived from VAE suffers at least an extra code length of DKL(q(z|x)||p(z|x)) nats for using a posterior that’s not precise. Many previous works in Variational Inference have designed flexible approximate posteriors to better approximate true posterior (Salimans et al., 2014; Rezende & Mohamed, 2015; Tran et al., 2015; Kingma et al., 2016). Improved posterior approximations have shown to be effective in improving variational inference but none of the existing methods are able to completely close the gap between approximate posterior and true posterior. This leads us to believe that for most practical models, at least in the near future, the extra coding cost DKL(q(z|x)||p(z|x)) will exist and will not be negligible.

Once we understand the inefficiency of the Bits-Back Coding mechanism, it’s simple to realize why sometimes the latent code z is not used: if the p(x|z) could model pdata(x) without using information from z, then it will not use z, in which case the true posterior p(z|x) is simply the prior p(z) and it’s usually easy to set q(z|x) to be p(z) to avoid incurring an extra cost DKL(q(z|x)||p(z|x)). And it’s exactly the case when a powerful decoding distribution is used like an RNN autoregressive distribution, which given enough capacity is able to model arbitrarily complex distributions. Hence there exists a preference of information when a VAE is optimized: information that can be modeled locally by decoding distribution p(x|z) without access to z will be encoded locally and only the remainder will be encoded in z.

We note that one common way to encourage putting information into the code is to use a factorized decoder p(x|z) = Q

i p(xi|z) but so long as there is one dimension xj that’s independent of all other dimensions for true data distribution, pdata(x) = pdata(xj)pdata(x̸=j), then the latent code doesn’t contain all the information about x since at least xj will be modeled locally by factorized p(x|z). This kind of independence structure rarely exists in images so common VAEs that have factorized decoder autoencode almost exactly. Other techniques to encourage the usage of the latent code include annealing the relative weight of of DKL(q(z|x)||p(z)) in the variational lower bound (Bowman et al., 2015; Kaae Sønderby et al., 2016) or the use of free bits (Kingma et al., 2016), which can serve the dual purpose of smoothing the optimization landscape and canceling out part of the Bits-Back Code inefficiency DKL(q(z|x)||p(z|x)).

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
