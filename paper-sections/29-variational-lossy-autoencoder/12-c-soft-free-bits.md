---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: C SOFT FREE BITS
section_role: other
section_index: 12
pages: [15]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "”Free bits” was a technique proposed in (Kingma et al., 2016) where K groups of stochastic units are encouraged to be used through the following…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# C SOFT FREE BITS

> Section 12 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `other` · pages 15-15

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

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
