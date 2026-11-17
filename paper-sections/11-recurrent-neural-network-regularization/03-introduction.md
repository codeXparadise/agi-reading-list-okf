---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
section: 1 INTRODUCTION
section_role: introduction
section_index: 3
pages: [1]
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "The Recurrent Neural Network (RNN) is neural sequence model that achieves state of the art performance on important tasks that include language…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1 INTRODUCTION

> Section 3 of 9 from [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · `introduction` · pages 1-1

The Recurrent Neural Network (RNN) is neural sequence model that achieves state of the art performance on important tasks that include language modeling Mikolov (2012), speech recognition Graves et al. (2013), and machine translation Kalchbrenner & Blunsom (2013). It is known that successful applications of neural networks require good regularization. Unfortunately, dropout Srivastava (2013), the most powerful regularization method for feedforward neural networks, does not work well with RNNs. As a result, practical applications of RNNs often use models that are too small because large RNNs tend to overfit. Existing regularization methods give relatively small improvements for RNNs Graves (2013). In this work, we show that dropout, when correctly used, greatly reduces overfitting in LSTMs, and evaluate it on three different problems.

The code for this work can be found in https://github.com/wojzaremba/lstm.

---

Full document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · Page-level evidence: [paper-pages/11-recurrent-neural-network-regularization](../../paper-pages/11-recurrent-neural-network-regularization/index.md)
