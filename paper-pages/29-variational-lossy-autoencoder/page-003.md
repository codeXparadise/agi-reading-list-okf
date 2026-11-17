---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 3
pages: [3]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 Since Kullback Leibler divergence is always non-negative, we know that using the two-part code derived…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 17 - Variational Lossy Autoencoder

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

Published as a conference paper at ICLR 2017

Since Kullback Leibler divergence is always non-negative, we know that using the two-part code derived from VAE suffers at least an extra code length of DKL(q(z|x)||p(z|x)) nats for using a posterior that’s not precise. Many previous works in Variational Inference have designed flexible approximate posteriors to better approximate true posterior (Salimans et al., 2014; Rezende & Mohamed, 2015; Tran et al., 2015; Kingma et al., 2016). Improved posterior approximations have shown to be effective in improving variational inference but none of the existing methods are able to completely close the gap between approximate posterior and true posterior. This leads us to believe that for most practical models, at least in the near future, the extra coding cost DKL(q(z|x)||p(z|x)) will exist and will not be negligible.

Once we understand the inefficiency of the Bits-Back Coding mechanism, it’s simple to realize why sometimes the latent code z is not used: if the p(x|z) could model pdata(x) without using information from z, then it will not use z, in which case the true posterior p(z|x) is simply the prior p(z) and it’s usually easy to set q(z|x) to be p(z) to avoid incurring an extra cost DKL(q(z|x)||p(z|x)). And it’s exactly the case when a powerful decoding distribution is used like an RNN autoregressive distribution, which given enough capacity is able to model arbitrarily complex distributions. Hence there exists a preference of information when a VAE is optimized: information that can be modeled locally by decoding distribution p(x|z) without access to z will be encoded locally and only the remainder will be encoded in z.

We note that one common way to encourage putting information into the code is to use a factorized decoder p(x|z) = Q

i p(xi|z) but so long as there is one dimension xj that’s independent of all other dimensions for true data distribution, pdata(x) = pdata(xj)pdata(x̸=j), then the latent code doesn’t contain all the information about x since at least xj will be modeled locally by factorized p(x|z). This kind of independence structure rarely exists in images so common VAEs that have factorized decoder autoencode almost exactly. Other techniques to encourage the usage of the latent code include annealing the relative weight of of DKL(q(z|x)||p(z)) in the variational lower bound (Bowman et al., 2015; Kaae Sønderby et al., 2016) or the use of free bits (Kingma et al., 2016), which can serve the dual purpose of smoothing the optimization landscape and canceling out part of the Bits-Back Code inefficiency DKL(q(z|x)||p(z|x)).

## 3 VARIATIONAL LOSSY AUTOENCODER

The discussion in Section 2.2 suggests that autoregressive models cannot be combined with VAE since information will be preferred to be modeled by autoregressive models. Nevertheless, in this section, we present two complementary classes of improvements to VAE that utilize autoregressive models fruitfully to explicitly control representation learning and improve density estimation.

3.1 LOSSY CODE VIA EXPLICIT INFORMATION PLACEMENT

Even though the information preference property of VAE might suggest that one should always use the full autoregressive models to achieve a better code length/log-likelihood, especially when slow data generation is not a concern, we argue that this information preference property can be exploited to turn the VAE into a powerful representation learning method that gives us fine-grained control over the kind of information that gets included in the learned representation.

When we try to learn a lossy compression/representation of data, we can simply construct a decoding distribution that’s capable of modeling the part of information that we don’t want the lossy representation to capture, but, critically, that’s incapable of modelling the information that we do want the lossy representation to capture.

For instance, if we are interested in learning a global representation for 2D images that doesn’t encode information about detailed texture, we can construct a specific factorization of the autoregressive distribution such that it has a small local receptive field as decoding distribution, e.g., plocal(x|z) = Q

i p(xi|z, xWindowAround(i)). Notice that, as long as xWindowAround(i) is smaller than x<i, plocal(x|z) won’t be able to represent arbitrarily complex distribution over x without dependence on z since the receptive field is limited such that not all distributions over x admit such factorizations. In particular, the receptive field window can be a small rectangle adjacent to a pixel xi and in this case long-range dependency will be encoded in the latent code z. On the other hand, if the true data distribution admits such factorization for a given datum x and dimension i, i.e.

4

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
