---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 4
pages: [4]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 pdata(xi|xWindowAround(i)) = pdata(xi|x<i), then the information preference property discussed in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 17 - Variational Lossy Autoencoder

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

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

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
