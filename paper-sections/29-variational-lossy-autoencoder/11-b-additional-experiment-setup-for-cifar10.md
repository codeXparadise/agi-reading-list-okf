---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: B ADDITIONAL EXPERIMENT SETUP FOR CIFAR10
section_role: other
section_index: 11
pages: [14, 15]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Latent codes are represented by 16 feature maps of size 8x8, and this choice of spatial stochastic units are inspired by ResNet IAF VAE (Kingma et…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# B ADDITIONAL EXPERIMENT SETUP FOR CIFAR10

> Section 11 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `other` · pages 14-15

Latent codes are represented by 16 feature maps of size 8x8, and this choice of spatial stochastic units are inspired by ResNet IAF VAE (Kingma et al., 2016). Prior distribution is factorized Gaussian noise transformed by 6 autoregressive flows, each of which is implemented by a PixelCNN (van den Oord et al., 2016a) with 2 hidden layers and 128 feature maps. Between every other autoregressive flow, the ordering of stochastic units is reversed.

ResNet VLAE has the following structure for encoder: 2 ResNet blocks, Conv w/ stride=2, 2 ResNet blocks, Conv w/ stride=2, 3 ResNet blocks, 1x1 convolution and has a symmetric decoder. Channel size = 48 for 32x32 feature maps and 96 for other feature maps. DenseNet VLAE follows a similar structure: replacing 2 ResNet blocks with one DenseNet block of 3 steps and each step produces a certain number of feature maps such that at the end of a block, the concatenated feature maps is slightly more than the ResNet VLAE at the same stage.

Conditional PixelCNN++ (Salimans et al., 2017) is used as the decoder. Specifically the channelautoregressive variant is used to ensure there is sufficient capacity even when the receptive field is small. Specifically, the decoder PixelCNN has 4 blocks of 64 feature maps where each block is conditioned on previous blocks with Gated ResNet connections and hence the PixelCNN decoders we use are shallow but very wide. For 4x2 receptive field experiment, we use 1 layer of vertical stack convolutions and 2 layers of horizontal stack convolutions; for 5x3 receptive field experiment, we use 2 layers of vertical stack convolutions and 2 layers of horizontal stack convolutions; For 5x3 receptive field experiment, we use 2 layers of vertical stack convolutions and 2 layers of horizontal stack convolutions; For 7x4 receptive field experiment, we use 3 layers of vertical stack convolutions and 3 layers of horizontal stack convolutions; for 7x4 Grayscale experiment, we transform RGB

15

Published as a conference paper at ICLR 2017

images into gray-scale images via this specific transformation: (0.299∗R)+(0.587G)+(0.114B). Best density estimation result is obtained with 7x4 receptive field experiments.

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
