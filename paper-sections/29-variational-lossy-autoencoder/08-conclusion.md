---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
section: 6 CONCLUSION
section_role: conclusion
section_index: 8
pages: [10]
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "In this paper, we analyze the condition under which the latent code in VAE should be used, i.e. when does VAE autoencode, and use this observation to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6 CONCLUSION

> Section 8 of 14 from [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · `conclusion` · pages 10-10

In this paper, we analyze the condition under which the latent code in VAE should be used, i.e. when does VAE autoencode, and use this observation to design a VAE model that’s a lossy compressor of observed data. At modeling level, we propose two complementary improvements to VAE that are shown to have good empirical performance.

VLAE has the appealing properties of controllable representation learning and improved density estimation performance but these properties come at a cost: compared with VAE models that have simple prior and decoder, VLAE is slower at generation due to the sequential nature of autoregressive model.

Moving forward, we believe it’s exciting to extend this principle of learning lossy codes to other forms of data, in particular those that have a temporal aspect like audio and video. Another promising direction is to design representations that contain only information for downstream tasks and utilize those representations to improve semi-supervised learning.

---

Full document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md) · Page-level evidence: [paper-pages/29-variational-lossy-autoencoder](../../paper-pages/29-variational-lossy-autoencoder/index.md)
