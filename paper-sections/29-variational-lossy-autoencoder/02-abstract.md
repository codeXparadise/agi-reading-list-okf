---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: ABSTRACT
section_role: abstract
section_index: 2
pages: [1]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Representation learning seeks to expose certain aspects of observed data in a learned representation that’s amenable to downstream tasks like…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# ABSTRACT

> Section 2 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `abstract` · pages 1-1

Representation learning seeks to expose certain aspects of observed data in a learned representation that’s amenable to downstream tasks like classification. For instance, a good representation for 2D images might be one that describes only global structure and discards information about detailed texture. In this paper, we present a simple but principled method to learn such global representations by combining Variational Autoencoder (VAE) with neural autoregressive models such as RNN, MADE and PixelRNN/CNN. Our proposed VAE model allows us to have control over what the global latent code can learn and by designing the architecture accordingly, we can force the global latent code to discard irrelevant information such as texture in 2D images, and hence the VAE only “autoencodes” data in a lossy fashion. In addition, by leveraging autoregressive models as both prior distribution p(z) and decoding distribution p(x|z), we can greatly improve generative modeling performance of VAEs, achieving new state-of-the-art results on MNIST, OMNIGLOT and Caltech-101 Silhouettes density estimation tasks as well as competitive results on CIFAR10.

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
