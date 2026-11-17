---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
section: 2 Related work
section_role: background
section_index: 4
pages: [1]
topics: ["../../topics/generative-models.md"]
description: "An alternative to directed graphical models with latent variables are undirected graphical models with latent variables, such as restricted Boltzmann…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 Related work

> Section 4 of 12 from [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · `background` · pages 1-1

An alternative to directed graphical models with latent variables are undirected graphical models with latent variables, such as restricted Boltzmann machines (RBMs) \[27, 16\], deep Boltzmann machines (DBMs) \[26\] and their numerous variants. The interactions within such models are represented as the product of unnormalized potential functions, normalized by a global summation/integration over all states of the random variables. This quantity (the partition function) and its gradient are intractable for all but the most trivial instances, although they can be estimated by Markov chain Monte Carlo (MCMC) methods. Mixing poses a significant problem for learning algorithms that rely on MCMC \[3, 5\].

Deep belief networks (DBNs) \[16\] are hybrid models containing a single undirected layer and several directed layers. While a fast approximate layer-wise training criterion exists, DBNs incur the computational difficulties associated with both undirected and directed models.

Alternative criteria that do not approximate or bound the log-likelihood have also been proposed, such as score matching \[18\] and noise-contrastive estimation (NCE) \[13\]. Both of these require the learned probability density to be analytically specified up to a normalization constant. Note that in many interesting generative models with several layers of latent variables (such as DBNs and DBMs), it is not even possible to derive a tractable unnormalized probability density. Some models such as denoising auto-encoders \[30\] and contractive autoencoders have learning rules very similar to score matching applied to RBMs. In NCE, as in this work, a discriminative training criterion is employed to fit a generative model. However, rather than fitting a separate discriminative model, the generative model itself is used to discriminate generated data from samples a fixed noise distribution. Because NCE uses a fixed noise distribution, learning slows dramatically after the model has learned even an approximately correct distribution over a small subset of the observed variables.

Finally, some techniques do not involve defining a probability distribution explicitly, but rather train a generative machine to draw samples from the desired distribution. This approach has the advantage that such machines can be designed to be trained by back-propagation. Prominent recent work in this area includes the generative stochastic network (GSN) framework \[5\], which extends generalized denoising auto-encoders \[4\]: both can be seen as defining a parameterized Markov chain, i.e., one learns the parameters of a machine that performs one step of a generative Markov chain. Compared to GSNs, the adversarial nets framework does not require a Markov chain for sampling. Because adversarial nets do not require feedback loops during generation, they are better able to leverage piecewise linear units \[19, 9, 10\], which improve the performance of backpropagation but have problems with unbounded activation when used ina feedback loop. More recent examples of training a generative machine by back-propagating into it include recent work on auto-encoding variational Bayes \[20\] and stochastic backpropagation \[24\].

---

Full document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · Page-level evidence: [paper-pages/28-generative-adversarial-nets](../../paper-pages/28-generative-adversarial-nets/index.md)
