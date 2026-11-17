---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 8
pages: [8]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 As seen in Table 2,3,4, with the same set of hyperparameters tuned on statically binarized MNIST, VLAE…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 8 of 17 - Variational Lossy Autoencoder

> Page 8 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

Published as a conference paper at ICLR 2017

As seen in Table 2,3,4, with the same set of hyperparameters tuned on statically binarized MNIST, VLAE is able to perform well on the rest of datasets, significantly exceeding previous state-ofthe-art results on dynamically binarized MNIST and Caltech-101 Silhouettes and tying statistically with best previous result on OMNIGLOT. In order to isolate the effect of expressive PixelCNN as decoder, we also report performance of the same PixelCNN trained without VAE part under the name “Unconditional Decoder”.

4.3 NATURAL IMAGES: CIFAR10

In addition to binary image datasets, we have applied VLAE to the CIFAR10 dataset of natural images. Density estimation of CIFAR10 images has been a challenging benchmark problem used by many recent generative models and hence is great task to position VLAE among existing methods.

We investigated using ResNet (He et al., 2016) and DenseNet (Huang et al., 2016) as building blocks for VAE networks and observed that DenseNet reduces overfitting. We also propose a new optimization technique that blends the advantages of KL annealing (Serban et al., 2016) and ”free bits” (Kingma et al., 2016) to stabilize learning on this challenging dataset. Detailed experimental setup is described in Appendix.

VLAE is compared to other methods on CIFAR10 in Table 5. We show that VLAE models attain new state-of-the-art performance among other variationally trained latent-variable models. DenseNet VLAE model also outperforms most other tractable likelihood models including Gated PixelCNN and PixelRNN and has results only slightly worse than currently unarchived state-of-the-art PixelCNN++.

Table 5: CIFAR10. Likelihood for VLAE is approximated with 512 importance samples. \[1\] (van den Oord et al., 2016a), \[2\] (Dinh et al., 2014), \[3\] (van den Oord & Schrauwen, 2014), \[4\] (Dinh et al., 2016), \[5\] (van den Oord et al., 2016b), \[6\] (Salimans et al., 2017), \[7\] (Sohl-Dickstein et al., 2015), \[8\] (Gregor et al., 2016), \[9\] (Kingma et al., 2016)

Method bits/dim ≤ Results with tractable likelihood models: Uniform distribution \[1\] 8.00 Multivariate Gaussian \[1\] 4.70 NICE \[2\] 4.48 Deep GMMs \[3\] 4.00 Real NVP \[4\] 3.49 PixelCNN \[1\] 3.14 Gated PixelCNN \[5\] 3.03 PixelRNN \[1\] 3.00 PixelCNN++ \[6\] 2.92 Results with variationally trained latent-variable models: Deep Diffusion \[7\] 5.40 Convolutional DRAW \[8\] 3.58 ResNet VAE with IAF \[9\] 3.11 ResNet VLAE 3.04 DenseNet VLAE 2.95

We also investigate learning lossy codes on CIFAR10 images. To illustrate how does the receptive field size of PixelCNN decoder influence properties of learned latent codes, we show visualizations of similar VLAE models with receptive fields of different sizes. Specifically we say a receptive field, xWindowAround(i), has size AxB when a pixel xi can depend on the rectangle block of size AxB immediately on top of xi as well as the

 A−1

2 

pixels immediately to the left of xi. We use this notation to refer to different types of PixelCNN decoders in Figure 3.

From (a)-(c) in Figure 3, we can see that larger receptive fields progressively make autoregressive decoders capture more structural information. In (a), a smaller receptive field tends to preserve rather detailed shape information in the lossy code whereas the latent code only retains rough shape in (c) with a larger receptive field.

9

---

[previous page](page-007.md) · [next page](page-009.md) · [all pages](index.md)
