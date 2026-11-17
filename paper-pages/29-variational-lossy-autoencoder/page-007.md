---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 7
pages: [7]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 Table 1: Statically Binarized MNIST Model NLL Test Normalizing flows (Rezende & Mohamed, 2015) 85.10…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 17 - Variational Lossy Autoencoder

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

Published as a conference paper at ICLR 2017

Table 1: Statically Binarized MNIST

Model NLL Test Normalizing flows (Rezende & Mohamed, 2015) 85.10 DRAW (Gregor et al., 2015) < 80.97 Discrete VAE (Rolfe, 2016) 81.01 PixelRNN (van den Oord et al., 2016a) 79.20 IAF VAE (Kingma et al., 2016) 79.88 AF VAE 79.30 VLAE 79.03

(2016) on statically binarized MNIST and make the single modification of replacing the original IAF posterior with an equivalent AF prior, removing the context. As seen in Table 1, VAE with AF prior is outperforming VAE with an equivalent IAF posterior, indicating that the deeper generative model from AF prior is beneficial. A similar gain carries over when an autoregressive decoder is used: on statically binarized MNIST, using AF prior instead of IAF posterior reduces train NLL by 0.8 nat and test NLL by 0.6 nat.

Next we evaluate whether using autoregressive decoding distribution can improve performance and we show in Table 1 that a VLAE model, with AF prior and PixelCNN conditional, is able to outperform a VAE with just AF prior and achieves new state-of-the-art results on statically binarized MNIST.

In addition, we hypothesize that the separation of different types of information, the modeling global structure in latent code and local statistics in PixelCNN, likely has some form of good inductive biases for 2D images. In order to evaluate if VLAE is an expressive density estimator with good inductive biases, we will test a single VLAE model, with the same network architecture, on all binary datasets. We choose hyperparameters manually on statically binarized MNIST and use the same hyperparameters to evaluate on dynamically binarized MNIST, OMNIGLOT and Caltech-101 Silhouettes. We also note that better performance can be obtained if we individually tune hyperparameters for each dataset. As a concrete demonstration, we report the performance of a fine-tuned VLAE on OMNIGLOT dataset in Table 3.

Table 2: Dynamically binarized MNIST

Model NLL Test Convolutional VAE + HVI (Salimans et al., 2014) 81.94 DLGM 2hl + IWAE (Burda et al., 2015a) 82.90 Discrete VAE (Rolfe, 2016) 80.04 LVAE (Kaae Sønderby et al., 2016) 81.74 DRAW + VGP (Tran et al., 2015) < 79.88 IAF VAE (Kingma et al., 2016) 79.10 Unconditional Decoder 87.55 VLAE 78.53

Table 3: OMNIGLOT. \[1\] (Burda et al., 2015a), \[2\] (Burda et al., 2015b), \[3\] (Gregor et al., 2015), \[4\] (Gregor et al., 2016),

Table 4: Caltech-101 Silhouettes. \[1\] (Bornschein & Bengio, 2014), \[2\] (Cho et al., 2011), \[3\] (Du et al., 2015), \[4\] (Rolfe, 2016), \[5\] (Goessling & Amit, 2015),

Model NLL Test VAE \[1\] 106.31 IWAE \[1\] 103.38 RBM (500 hidden) \[2\] 100.46 DRAW \[3\] < 96.50 Conv DRAW \[4\] < 91.00 Unconditional Decoder 95.02 VLAE 90.98 VLAE (fine-tuned) 89.83

Model NLL Test RWS SBN \[1\] 113.3 RBM \[2\] 107.8 NAIS NADE \[3\] 100.0 Discrete VAE \[4\] 97.6 SpARN \[5\] 88.48 Unconditional Decoder 89.26 VLAE 77.36

8

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
