---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
page: 6
pages: [6]
page_of: 9
topics: ["../../topics/generative-models.md"]
description: "Figure 3: Digits obtained by linearly interpolating between coordinates in z space of the full model. Deep directed graphical models Deep undirected…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 6 of 9 - Generative Adversarial Nets

> Page 6 of the source PDF, verbatim as extracted. Canonical document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md)

Figure 3: Digits obtained by linearly interpolating between coordinates in z space of the full model.

Deep directed graphical models

Deep undirected graphical models

Generative autoencoders Adversarial models

Inference needed during training. MCMC needed to approximate partition function gradient.

Enforced tradeoff between mixing and power of reconstruction generation

Synchronizing the discriminator with the generator. Helvetica.

Training Inference needed during training.

Learned approximate inference

Learned approximate inference

Variational inference

MCMC-based inference

Inference

Sampling No difficulties Requires Markov chain

Requires Markov chain No difficulties

Not explicitly represented, may be approximated with Parzen density estimation

Not explicitly represented, may be approximated with Parzen density estimation

Intractable, may be approximated with AIS

Intractable, may be approximated with AIS

Evaluating p(x)

Any differentiable function is theoretically permitted

Any differentiable function is theoretically permitted

Nearly all models incur extreme difficulty

Careful design needed to ensure multiple properties

Model design

Table 2: Challenges in generative modeling: a summary of the difficulties encountered by different approaches to deep generative modeling for each of the major operations involving a model.

## 6 Advantages and disadvantages

This new framework comes with advantages and disadvantages relative to previous modeling frameworks. The disadvantages are primarily that there is no explicit representation of pg(x), and that D must be synchronized well with G during training (in particular, G must not be trained too much without updating D, in order to avoid “the Helvetica scenario” in which G collapses too many values of z to the same value of x to have enough diversity to model pdata), much as the negative chains of a Boltzmann machine must be kept up to date between learning steps. The advantages are that Markov chains are never needed, only backprop is used to obtain gradients, no inference is needed during learning, and a wide variety of functions can be incorporated into the model. Table 2 summarizes the comparison of generative adversarial nets with other generative modeling approaches.

The aforementioned advantages are primarily computational. Adversarial models may also gain some statistical advantage from the generator network not being updated directly with data examples, but only with gradients flowing through the discriminator. This means that components of the input are not copied directly into the generator’s parameters. Another advantage of adversarial networks is that they can represent very sharp, even degenerate distributions, while methods based on Markov chains require that the distribution be somewhat blurry in order for the chains to be able to mix between modes.

## 7 Conclusions and future work

This framework admits many straightforward extensions:

1. A conditional generative model p(x | c) can be obtained by adding c as input to both G and D. 2. Learned approximate inference can be performed by training an auxiliary network to predict z given x. This is similar to the inference net trained by the wake-sleep algorithm \[15\] but with the advantage that the inference net may be trained for a fixed generator net after the generator net has finished training.

---

[previous page](page-005.md) · [next page](page-007.md) · [all pages](index.md)
