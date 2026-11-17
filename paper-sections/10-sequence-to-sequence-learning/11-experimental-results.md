---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/10-sequence-to-sequence-learning.md
source: ../../papers/10-sequence-to-sequence-learning.md
paper_title: Sequence to Sequence Learning with Neural Networks
sequence: 10
section: 3.6 Experimental Results
section_role: experiments
section_index: 11
pages: [4, 5]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/machine-translation.md", "../../topics/recurrent-neural-networks.md"]
description: "We used the cased BLEU score [24] to evaluate the quality of our translations. We computed our BLEU scores using multi-bleu.pl1 on the tokenized…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.6 Experimental Results

> Section 11 of 20 from [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md) · `experiments` · pages 4-5

We used the cased BLEU score \[24\] to evaluate the quality of our translations. We computed our BLEU scores using multi-bleu.pl1 on the tokenized predictions and ground truth. This way of evaluating the BELU score is consistent with \[5\] and \[2\], and reproduces the 33.3 score of \[29\]. However, if we evaluate the best WMT’14 system \[9\] (whose predictions can be downloaded from statmt.org\\matrix) in this manner, we get 37.0, which is greater than the 35.8 reported by statmt.org\\matrix.

The results are presented in tables 1 and 2. Our best results are obtained with an ensemble of LSTMs that differ in their random initializations and in the random order of minibatches. While the decoded translations of the LSTM ensemble do not outperform the best WMT’14 system, it is the first time that a pure neural translation system outperforms a phrase-based SMT baseline on a large scale MT

1There several variants of the BLEU score, and each variant is defined with a perl script.

---

Full document: [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md) · Page-level evidence: [paper-pages/10-sequence-to-sequence-learning](../../paper-pages/10-sequence-to-sequence-learning/index.md)
