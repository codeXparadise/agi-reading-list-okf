---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/10-sequence-to-sequence-learning.md
source: ../../papers/10-sequence-to-sequence-learning.md
paper_title: Sequence to Sequence Learning with Neural Networks
sequence: 10
section: Method
section_role: method
section_index: 12
pages: [5]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/machine-translation.md", "../../topics/recurrent-neural-networks.md"]
description: "test BLEU score (ntst14) Bahdanau et al. [2] 28.45 Baseline System [29] 33.30 Single forward LSTM, beam size 12 26.17 Single reversed LSTM, beam size…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Method

> Section 12 of 20 from [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md) · `method` · pages 5-5

## test BLEU score (ntst14)

Bahdanau et al. \[2\]

28.45

Baseline System \[29\]

33.30

Single forward LSTM, beam size 12

26.17

Single reversed LSTM, beam size 12

30.59

Ensemble of 5 reversed LSTMs, beam size 1

33.00

Ensemble of 2 reversed LSTMs, beam size 12

33.27

Ensemble of 5 reversed LSTMs, beam size 2

34.50

Ensemble of 5 reversed LSTMs, beam size 12

## 34.81

Table 1: The performance of the LSTM on WMT’14 English to French test set (ntst14). Note that an ensemble of 5 LSTMs with a beam of size 2 is cheaper than of a single LSTM with a beam of size 12.

---

Full document: [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md) · Page-level evidence: [paper-pages/10-sequence-to-sequence-learning](../../paper-pages/10-sequence-to-sequence-learning/index.md)
