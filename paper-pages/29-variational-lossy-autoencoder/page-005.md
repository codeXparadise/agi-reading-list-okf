---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 5
pages: [5]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 Simply re-arranging the variational lowerbound for using AF prior reveals that having an AF latent code…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 17 - Variational Lossy Autoencoder

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

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

## 4 EXPERIMENTS

In this paper, we evaluate VLAE on 2D images and leave extensions to other forms of data to future work. For the rest of the section, we define a VLAE model as a VAE that uses AF prior and autoregressive decoder. We choose to implement conditional distribution p(x|z) with a smallreceptive-field PixelCNN (van den Oord et al., 2016a), which has been proved to be a scalable autoregressive model.

For evaluation, we use binary image datasets that are commonly used for density estimation tasks: MNIST (LeCun et al., 1998) (both statically binarized 1 and dynamically binarized version (Burda et al., 2015a)), OMNIGLOT (Lake et al., 2013; Burda et al., 2015a) and Caltech-101 Silhouettes (Marlin et al., 2010). All datasets uniformly consist of 28x28 binary images, which allow us to use a unified architecture. VAE networks used in binary image datasets are simple variants of ResNet VAEs described in (Salimans et al., 2014; Kingma et al., 2016). For the decoder, we use a variant of PixelCNN that has 6 layers of masked convolution with filter size 3, which means the window of dependency, xWindowAround(i), is limited to a small local patch. During training, ”free bits” (Kingma et al., 2016) is used improve optimization stability. Experimental setup and hyperparameters are detailed in the appendix. Reported marginal NLL is estimated using Importance Sampling with 4096 samples.

We designed experiments to answer the following questions:

• Can VLAE learn lossy codes that encode global statistics?

• Does using AF priors improves upon using IAF posteriors as predicted by theory?

• Does using autoregressive decoding distributions improve density estimation performance?

4.1 LOSSY COMPRESSION

First we are interested in whether VLAE can learn a lossy representation/compression of data by using the PixelCNN decoder to model local statistics. We trained VLAE model on Statically Binarized MNIST and the converged model has E\[DKL(q(z|x)||p(z))\] = 13.3 nats = 19.2 bits, which is the number of bits it uses on average to encode/compress one MNIST image. By comparison, an identical VAE model with factorized decoding distribution will uses on average 37.3 bits in latent code, and this thus indicates that VLAE can learn a lossier compression than a VAE with regular factorized conditional distribution.

The next question is whether VLAE’s lossy compression encodes global statistics and discards local statistics. In Fig 1a, we visualize original images xdata and one random “decompression” xdecompressed from VLAE: z ∼q(z|xdata), xdecompressed ∼p(x|z). We observe that none of the

1We use the version provided by Hugo Larochelle.

6

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
