---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
section: 7 Conclusions and future work
section_role: conclusion
section_index: 10
pages: [6, 7]
topics: ["../../topics/generative-models.md"]
description: "This framework admits many straightforward extensions: 1. A conditional generative model p(x | c) can be obtained by adding c as input to both G and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7 Conclusions and future work

> Section 10 of 12 from [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · `conclusion` · pages 6-7

This framework admits many straightforward extensions:

1. A conditional generative model p(x | c) can be obtained by adding c as input to both G and D. 2. Learned approximate inference can be performed by training an auxiliary network to predict z given x. This is similar to the inference net trained by the wake-sleep algorithm \[15\] but with the advantage that the inference net may be trained for a fixed generator net after the generator net has finished training.

3. One can approximately model all conditionals p(xS | x̸S) where S is a subset of the indices of x by training a family of conditional models that share parameters. Essentially, one can use adversarial nets to implement a stochastic extension of the deterministic MP-DBM \[11\]. 4. Semi-supervised learning: features from the discriminator or inference net could improve performance of classifiers when limited labeled data is available. 5. Efficiency improvements: training could be accelerated greatly by divising better methods for coordinating G and D or determining better distributions to sample z from during training.

This paper has demonstrated the viability of the adversarial modeling framework, suggesting that these research directions could prove useful.

---

Full document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · Page-level evidence: [paper-pages/28-generative-adversarial-nets](../../paper-pages/28-generative-adversarial-nets/index.md)
