---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/10-sequence-to-sequence-learning.md
source: ../../papers/10-sequence-to-sequence-learning.md
paper_title: Sequence to Sequence Learning with Neural Networks
sequence: 10
section: Method
section_role: method
section_index: 13
pages: [5]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/machine-translation.md", "../../topics/recurrent-neural-networks.md"]
description: "test BLEU score (ntst14) Baseline System [29] 33.30 Cho et al. [5] 34.54 Best WMT’14 result [9] 37.0 Rescoring the baseline 1000-best with a single…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Method

> Section 13 of 20 from [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md) · `method` · pages 5-5

## test BLEU score (ntst14)

Baseline System \[29\]

33.30

Cho et al. \[5\]

34.54

Best WMT’14 result \[9\]

## 37.0

Rescoring the baseline 1000-best with a single forward LSTM

35.61

Rescoring the baseline 1000-best with a single reversed LSTM

35.85

Rescoring the baseline 1000-best with an ensemble of 5 reversed LSTMs

## 36.5

Oracle Rescoring of the Baseline 1000-best lists

∼45

Table 2: Methods that use neural networks together with an SMT system on the WMT’14 English to French test set (ntst14).

task by a sizeable margin, despite its inability to handle out-of-vocabulary words. The LSTM is within 0.5 BLEU points of the best WMT’14 result if it is used to rescore the 1000-best list of the baseline system.

---

Full document: [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md) · Page-level evidence: [paper-pages/10-sequence-to-sequence-learning](../../paper-pages/10-sequence-to-sequence-learning/index.md)
