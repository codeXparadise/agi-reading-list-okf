---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: 3 VARIATIONAL LOSSY AUTOENCODER
section_role: other
section_index: 5
pages: [3, 4, 5]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "The discussion in Section 2.2 suggests that autoregressive models cannot be combined with VAE since information will be preferred to be modeled by…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 VARIATIONAL LOSSY AUTOENCODER

> Section 5 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `other` · pages 3-5

The discussion in Section 2.2 suggests that autoregressive models cannot be combined with VAE since information will be preferred to be modeled by autoregressive models. Nevertheless, in this section, we present two complementary classes of improvements to VAE that utilize autoregressive models fruitfully to explicitly control representation learning and improve density estimation.

3.1 LOSSY CODE VIA EXPLICIT INFORMATION PLACEMENT

Even though the information preference property of VAE might suggest that one should always use the full autoregressive models to achieve a better code length/log-likelihood, especially when slow data generation is not a concern, we argue that this information preference property can be exploited to turn the VAE into a powerful representation learning method that gives us fine-grained control over the kind of information that gets included in the learned representation.

When we try to learn a lossy compression/representation of data, we can simply construct a decoding distribution that’s capable of modeling the part of information that we don’t want the lossy representation to capture, but, critically, that’s incapable of modelling the information that we do want the lossy representation to capture.

For instance, if we are interested in learning a global representation for 2D images that doesn’t encode information about detailed texture, we can construct a specific factorization of the autoregressive distribution such that it has a small local receptive field as decoding distribution, e.g., plocal(x|z) = Q

i p(xi|z, xWindowAround(i)). Notice that, as long as xWindowAround(i) is smaller than x<i, plocal(x|z) won’t be able to represent arbitrarily complex distribution over x without dependence on z since the receptive field is limited such that not all distributions over x admit such factorizations. In particular, the receptive field window can be a small rectangle adjacent to a pixel xi and in this case long-range dependency will be encoded in the latent code z. On the other hand, if the true data distribution admits such factorization for a given datum x and dimension i, i.e.

4

Published as a conference paper at ICLR 2017

pdata(xi|xWindowAround(i)) = pdata(xi|x<i), then the information preference property discussed in Section 2.2 will apply here, which means that all the information will be encoded in local autoregressive distribution for xi. Local statistics of 2D images like texture will likely be modeled completely by a small local window, whereas global structural information of an images like shapes of objects is long-range dependency that can only be communicated through latent code z. Therefore we have given an example VAE that will produce a lossy compression of 2D images carrying exclusively global information that can’t be modeled locally.

Notice that a global representation is only one of many possible lossy representations that we can construct using this information preference property. For instance, the conditional of an autoregressive distribution might depend on a heavily down-sampled receptive field so that it can only model long-range pattern whereas local high-frequency statistics need to be encoded into the latent code. Hence we have demonstrated that we can achieve explicit placement of information by constraining the receptive field/factorization of an autoregressive distribution that’s used as decoding distribution.

We want to additionally emphasize the information preference property is an asymptotic view in a sense that it only holds when the variational lowerbound can be optimized well. Thus, we are not proposing an alternative to techniques like free bits Kingma et al. (2016) or KL annealing, and indeed they are still useful methods to smooth the optimization problem and used in this paper’s experiments.

3.2 LEARNED PRIOR WITH AUTOREGRESSIVE FLOW

Inefficiency in Bits-Back Coding, i.e., the mismatch between approximate posterior and true posterior, can be exploited to construct a lossy code but it’s still important to minimize such inefficiency to improve overall modeling performance/coding efficiency. We propose to parametrize the prior distribution p(z; θ) with an autoregressive model and show that a type of autoregressive latent code can in theory reduce inefficiency in Bits-Back coding.

It is well-known that limited approximate posteriors impede learning and therefore various expressive posterior approximations have been proposed to improve VAE’s density estimation performance (Turner et al., 2008; Mnih & Gregor, 2014; Salimans et al., 2014; Rezende & Mohamed, 2015; Kingma et al., 2016). One such class of approximate posteriors that has been shown to attain good empirical performance is based on the idea of Normalizing Flow, which is to apply an invertible mapping to a simple random variable, for example a factorized Gaussian as commonly used for q(z|x), in order to obtain a complicated random variable. For an invertible transformation between a simple distribution y and a more flexible z, we know from the change-of-variable technique that log q(z|x) = log q(y|x) −log det dz

dy and using q(z|x) as approximate posterior will decrease the coding efficiency gap DKL(q(z|x)||p(z|x)) provided the transformation is sufficiently expressive.

Kingma et al. (2016) introduced Inverse Autoregressive Flow, which is a powerful class of such invertible mappings that have simple determinant: zi = yi−µi(y1:i−1)

σi(y1:i−1) , where µi(.) ∈R, σi(.) ∈R+

are general functions that can be parametrized by expressive neural networks, such as MADE and PixelCNN variants (Germain et al., 2015; van den Oord et al., 2016a). Inverse autoregressive flow is the inverse/whitening of autoregressive flow: yi = ziσi(y1:i−1) + µi(y1:i−1). We refer interested readers to (Rezende & Mohamed, 2015; Kingma et al., 2016) for in-depth discussions on related topics.

In this paper, we propose to parametrize our learnable prior as an autoregressive flow from some simple noise source like spherical Gaussian. Next, we show that using latent code transformed by autoregressive flow (AF) is equivalent to using inverse autoregressive flow (IAF) approximate posterior, which explains why it can similarly improve Bits-Back Coding efficiency. Moreover, compared with an IAF posterior, an AF prior has a more expressive generative model that essentially “comes for free”.

For an autoregressive flow f, some continuous noise source ϵ is transformed into latent code z: z = f(ϵ). Assuming the density function for noise source is u(ϵ), we similarly know that log p(z) = log u(ϵ) + log det dϵ

dz.

5

Published as a conference paper at ICLR 2017

Simply re-arranging the variational lowerbound for using AF prior reveals that having an AF latent code z is equivalent to using an IAF posterior for ϵ that we can interpret as the new latent code:

L(x; θ) = Ez∼q(z|x) \[log p(x|z) + log p(z) −log q(z|x)\] (12)

log p(x|f(ϵ)) + log u(ϵ) + log det dϵ

= Ez∼q(z|x),ϵ=f −1(z)

(13)

dz −log q(z|x)





log p(x|f(ϵ)) + log u(ϵ) −(log q(z|x) −log det dϵ

 (14)

= Ez∼q(z|x),ϵ=f −1(z)

dz) | {z } IAF Posterior

AF prior is the same as IAF posterior along the encoder path, f −1(q(z|x)), but differs along the decoder/generator path: IAF posterior has a shorter decoder path p(x|z) whereas AF prior has a deeper decoder path p(x|f(ϵ)). The crucial observation is that AF prior and IAF posterior have the same computation cost under the expectation of z ∼q(z|x), so using AF prior makes the model more expressive at no training time cost.

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
