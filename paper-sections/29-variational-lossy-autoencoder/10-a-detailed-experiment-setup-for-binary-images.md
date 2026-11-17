---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: A DETAILED EXPERIMENT SETUP FOR BINARY IMAGES
section_role: other
section_index: 10
pages: [14]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "For VAE’s encoder and decoder, we use the same ResNet (He et al., 2015) VAE architecture as the one used in IAF MNIST experiment (Kingma et al.,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# A DETAILED EXPERIMENT SETUP FOR BINARY IMAGES

> Section 10 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `other` · pages 14-14

For VAE’s encoder and decoder, we use the same ResNet (He et al., 2015) VAE architecture as the one used in IAF MNIST experiment (Kingma et al., 2016). The only difference is that the decoder network now, instead of outputing a 28x28x1 spatial feature map to specify the mean of a factorized bernoulli distribution, outputs a 28x28x4 spatial feature map that’s concatenated with the original binary image channel-wise, forming a 28x28x5 feature map that’s then fed through a typical masked PixelCNN (van den Oord et al., 2016a). As such even though the PixelCNN conditions on the latent code, we don’t call it a Conditional PixelCNN because it doesn’t use the specific architecture that was proposed in van den Oord et al. (2016b). For the PixelCNN, it has 6 masked convolution layers with 12 3x3 filters organized in ResNet blocks, and it has 4 additional 1x1 convolution ResNet block between every other masked convolution layer to increase processing capacity since it employs fewer masked convolutions than usual. All the masked convolution layer have their weights tied to reduce overfitting on statically binarized MNIST, and untying the weights will increase performance for other datasets. Experiments are tuned on the validation set and then final experiment was run with train and validation set, with performance evaluated with test set. Exponential Linear Units (Clevert et al., 2015) are used as activation functions in both VAE network and PixelCNN network. Weight normalization is everywhere with data-dependent initialization (Salimans & Kingma, 2016).

A latent code of dimension 64 was used. For AF prior, it’s implemented with MADE (Germain et al., 2015) as detailed in Kingma et al. (2016). We used 4 steps of autoregressive flow and each flow is implemented by a 3-layer MADE that has 640 hidden units and uses Relu (Nair & Hinton, 2010) as activation functions. Differing from the practice of Kingma et al. (2016), we use mean-only autoregressive flow, which we found to be more numerically stable.

In terms of training, Adamax (Kingma & Ba, 2014) was used with a learning rate of 0.002. 0.01 nats/data-dim free bits (Kingma et al., 2016) was found to be effective in dealing with the problem of all the latent code being ignored early in training. Polyak averaging (Polyak & Juditsky, 1992) was used to compute the final parameters, with α = 0.998.

All experiments are implemented using TensorFlow (Abadi et al., 2016).

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
