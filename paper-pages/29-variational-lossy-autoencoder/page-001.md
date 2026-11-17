---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 1
pages: [1]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 well as the powerful recurrence of an autoregressive model. However, earlier attempts at combining these…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 17 - Variational Lossy Autoencoder

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

Published as a conference paper at ICLR 2017

well as the powerful recurrence of an autoregressive model. However, earlier attempts at combining these two kinds of models have run into the problem that the autoregressive part of the model ends up explaining all structure in the data, while the latent variables are not used (Fabius & van Amersfoort, 2014; Chung et al., 2015; Bowman et al., 2015; Serban et al., 2016; Fraccaro et al., 2016; Xu & Sun, 2016). Bowman et al. (2015) noted that weakening the autoregressive part of the model by, for example, dropout can encourage the latent variables to be used. We analyze why weakening is necessary, and we propose a principled solution that takes advantage of this property to control what kind of information goes into latent variables. The model we propose performs well as a density estimator, as evidenced by state-of-the-art log-likelihood results on MNIST, OMNIGLOT and Caltech-101, and also has a structure that is uniquely suited for learning interesting global representations of data.

## 2 VAES DO NOT AUTOENCODE IN GENERAL

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

---

first page · [next page](page-002.md) · [all pages](index.md)
