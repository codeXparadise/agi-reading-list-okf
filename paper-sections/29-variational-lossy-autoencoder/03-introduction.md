---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: 1 INTRODUCTION
section_role: introduction
section_index: 3
pages: [1]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "A key goal of representation learning is to identify and disentangle the underlying causal factors of the data, so that it becomes easier to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1 INTRODUCTION

> Section 3 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `introduction` · pages 1-1

A key goal of representation learning is to identify and disentangle the underlying causal factors of the data, so that it becomes easier to understand the data, to classify it, or to perform other tasks (Bengio et al., 2013). For image data this often means that we are interested in uncovering the “global structure” that captures the content of an image (for example, the identity of objects present in the image) and its “style”, but that we are typically less interested in the local and high frequency sources of variation such as the specific textures or white noise patterns.

A popular approach for learning representations is to fit a probabilistic latent variable model, an approach also known as analysis-by-synthesis (Yuille & Kersten, 2006; Nair et al., 2008). By learning a generative model of the data with the appropriate hierarchical structure of latent variables, it is hoped that the model will somehow uncover and untangle those causal sources of variations that we happen to be interested in. However, without further assumptions, representation learning via generative modeling is ill-posed: there are many different possible generative models with different (or no) kinds of latent variables that all encode the same probability density function on our observed data. Thus, the results we empirically get using this approach are highly dependent on the specific architectural and modeling choices that are made. Moreover, the objective that we optimize is often completely disconnected from the goal of learning a good representation: An autoregressive model of the data may achieve the same log-likelihood as a variational autoencoder (VAE) (Kingma & Welling, 2013), but the structure learned by the two models is completely different: the latter typically has a clear hierarchy of latent variables, while the autoregressive model has no stochastic latent variables at all (although it is conceivable that the deterministic hidden units of the autoregressive models will have meaningful and useful representations). For this reason, autoregressive models have thus far not been popular for the purpose of learning representations, even though they are extremely powerful as generative models (see e.g. van den Oord et al., 2016a).

A natural question becomes: is it possible to have a model that is a powerful density estimator and at the same time has the right hierarchical structure for representation learning? A potential solution would be to use a hybrid model that has both the latent variable structure of a VAE, as

1

Published as a conference paper at ICLR 2017

well as the powerful recurrence of an autoregressive model. However, earlier attempts at combining these two kinds of models have run into the problem that the autoregressive part of the model ends up explaining all structure in the data, while the latent variables are not used (Fabius & van Amersfoort, 2014; Chung et al., 2015; Bowman et al., 2015; Serban et al., 2016; Fraccaro et al., 2016; Xu & Sun, 2016). Bowman et al. (2015) noted that weakening the autoregressive part of the model by, for example, dropout can encourage the latent variables to be used. We analyze why weakening is necessary, and we propose a principled solution that takes advantage of this property to control what kind of information goes into latent variables. The model we propose performs well as a density estimator, as evidenced by state-of-the-art log-likelihood results on MNIST, OMNIGLOT and Caltech-101, and also has a structure that is uniquely suited for learning interesting global representations of data.

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
