---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/01-attention-is-all-you-need.md
source: ../../papers/01-attention-is-all-you-need.md
paper_title: Attention Is All You Need
sequence: 1
section: 7 Conclusion
section_role: conclusion
section_index: 9
pages: [9]
topics: ["../../topics/attention.md", "../../topics/transformer-architecture.md", "../../topics/sequence-to-sequence.md", "../../topics/machine-translation.md"]
description: "In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7 Conclusion

> Section 9 of 11 from [01 - Attention Is All You Need](../../papers/01-attention-is-all-you-need.md) · `conclusion` · pages 9-9

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles.

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours.

The code we used to train and evaluate our models is available at https://github.com/ tensorflow/tensor2tensor.

Acknowledgements We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.

---

Full document: [01 - Attention Is All You Need](../../papers/01-attention-is-all-you-need.md) · Page-level evidence: [paper-pages/01-attention-is-all-you-need](../../paper-pages/01-attention-is-all-you-need/index.md)
