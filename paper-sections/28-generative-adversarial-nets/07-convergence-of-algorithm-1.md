---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
section: 4.2 Convergence of Algorithm 1
section_role: other
section_index: 7
pages: [4]
topics: ["../../topics/generative-models.md"]
description: "Proposition 2. If G and D have enough capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum given G, and pg is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.2 Convergence of Algorithm 1

> Section 7 of 12 from [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · `other` · pages 4-4

Proposition 2. If G and D have enough capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum given G, and pg is updated so as to improve the criterion

Ex∼pdata\[log D∗

G(x)\] + Ex∼pg\[log(1 −D∗

G(x))\]

then pg converges to pdata

Proof. Consider V (G, D) = U(pg, D) as a function of pg as done in the above criterion. Note that U(pg, D) is convex in pg. The subderivatives of a supremum of convex functions include the derivative of the function at the point where the maximum is attained. In other words, if f(x) = supα∈A fα(x) and fα(x) is convex in x for every α, then ∂fβ(x) ∈∂f if β = arg supα∈A fα(x). This is equivalent to computing a gradient descent update for pg at the optimal D given the corresponding G. supD U(pg, D) is convex in pg with a unique global optima as proven in Thm 1, therefore with sufficiently small updates of pg, pg converges to px, concluding the proof.

In practice, adversarial nets represent a limited family of pg distributions via the function G(z; θg), and we optimize θg rather than pg itself. Using a multilayer perceptron to define G introduces multiple critical points in parameter space. However, the excellent performance of multilayer perceptrons in practice suggests that they are a reasonable model to use despite their lack of theoretical guarantees.

---

Full document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · Page-level evidence: [paper-pages/28-generative-adversarial-nets](../../paper-pages/28-generative-adversarial-nets/index.md)
