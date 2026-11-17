---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: D AUTOREGRESSIVE DECODER WITHOUT AUTOREGRESSIVE PRIOR
section_role: other
section_index: 13
pages: [15]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "In this section, we investigate the scenario of just using an autoregressive decoder without using an autoregressive prior. We compare the exact same…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# D AUTOREGRESSIVE DECODER WITHOUT AUTOREGRESSIVE PRIOR

> Section 13 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `other` · pages 15-15

In this section, we investigate the scenario of just using an autoregressive decoder without using an autoregressive prior. We compare the exact same model in three configurations: 1) using smallreceptive-field PixelCNN as an unconditional density estimator; 2) using small-receptive-field as a decoder in a VAE with Gaussian latent variables; 3) replacing Gaussian latent variables with autoregressive flow latent variables in 2).

Table 1: Ablation on Dynamically binarized MNIST

Model NLL Test KL Unconditional PixelCNN 87.55 0 PixelCNN Decoder + Gaussian Prior 79.48 10.60 PixelCNN Decoder + AF Prior 78.94 11.73

In Table 1, we can observe that each step of modification improves density estimation performance. In addition, using an autoregressive latent code makes the latent code transmit more information as shown in the difference of E\[DKL(q(z|x)||p(z))\].

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
