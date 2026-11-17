---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 15
pages: [15]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 images into gray-scale images via this specific transformation: (0.299∗R)+(0.587G)+(0.114B). Best…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 15 of 17 - Variational Lossy Autoencoder

> Page 15 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

Published as a conference paper at ICLR 2017

images into gray-scale images via this specific transformation: (0.299∗R)+(0.587G)+(0.114B). Best density estimation result is obtained with 7x4 receptive field experiments.

## C SOFT FREE BITS

”Free bits” was a technique proposed in (Kingma et al., 2016) where K groups of stochastic units are encouraged to be used through the following surrogate objective:

K X

eLλ = Ex∼M

Eq(z|x) \[log p(x|z)\]

maximum(λ, Ex∼M \[DKL(q(zj|x)||p(zj))\])

−

j=1

This technique is easy to use since it’s usually easy to determine the minimum number of bits/nats, λ, stochastic units need to encode. Choosing λ is hence easier than setting a fixed KL annealing schedule (Serban et al., 2016).

On the other hand, Kl annealing has the benefit of the surrogate objective will smoothly become the true objective, the variational lower bound where as ”free bits” has a sharp transition at the boundary. Therefore, we propose to still use λ as hyperparameter to specify at least λ nats should be used but try to change the optimization objective as slowly as possible:

LSoftFreeBits(x; θ) =Eq(z|x) \[log p(x|z)\] −γDKL(q(z|x)||p(z))

where 0 < γ ≤1.

And we make the optimization smoother by changing γ slowly online to make sure at least λ nats are used: when Kl is too much higher than λ (we experimented wide range of thresholds from 3% to 30%, all of which yield improved results, and we tend to use 5% us a threshold), γ is increased, and when Kl lower than λ, γ is decreased to encourage information flow.

We found it sufficient to increase/decrease at 10% increment and didn’t further tune this parameter.

## D AUTOREGRESSIVE DECODER WITHOUT AUTOREGRESSIVE PRIOR

In this section, we investigate the scenario of just using an autoregressive decoder without using an autoregressive prior. We compare the exact same model in three configurations: 1) using smallreceptive-field PixelCNN as an unconditional density estimator; 2) using small-receptive-field as a decoder in a VAE with Gaussian latent variables; 3) replacing Gaussian latent variables with autoregressive flow latent variables in 2).

Table 1: Ablation on Dynamically binarized MNIST

Model NLL Test KL Unconditional PixelCNN 87.55 0 PixelCNN Decoder + Gaussian Prior 79.48 10.60 PixelCNN Decoder + AF Prior 78.94 11.73

In Table 1, we can observe that each step of modification improves density estimation performance. In addition, using an autoregressive latent code makes the latent code transmit more information as shown in the difference of E\[DKL(q(z|x)||p(z))\].

## E CIFAR10 GENERATED SAMPLES

## REFERENCES

Martın Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo, Zhifeng Chen, Craig Citro, Greg S

Corrado, Andy Davis, Jeffrey Dean, Matthieu Devin, et al. Tensorflow: Large-scale machine learning on heterogeneous distributed systems. arXiv preprint arXiv:1603.04467, 2016.

16

---

[previous page](page-014.md) · [next page](page-016.md) · [all pages](index.md)
