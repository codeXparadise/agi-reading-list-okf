---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
section: 4.3 Language Modeling
section_role: other
section_index: 13
pages: [5]
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "Finally, we investigate the task of word-based language modeling. We model the conditional probability p(wt|w<t) of a word wt given a sequence of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.3 Language Modeling

> Section 13 of 25 from [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · `other` · pages 5-5

Finally, we investigate the task of word-based language modeling. We model the conditional probability p(wt|w<t) of a word wt given a sequence of observed words w<t = (wt−1, wt−2, . . . , w1). Language models can be directly applied to predictive keyboard and search-phrase completion, or they can be used as components within larger systems, e.g. machine translation \[27\], speech recognition \[28\], and information retrieval \[29\]. RNNs, and most notably LSTMs, have proven to be state-of-the-art on many competitive language modeling benchmarks such as Penn Treebank \[30, 31\], WikiText-103 \[32, 33\], and the One Billion Word Benchmark \[34, 35\]. As a sequential reasoning task, language modeling allows us to assess the RMC’s ability to process information over time on a large quantity of natural data, and compare it to well-tuned models.

We focus on datasets with contiguous sentences and a moderately large amount of data. WikiText-103 satisfies this set of requirements as it consists of Wikipedia articles shuffled at the article level with roughly 100M training tokens, as do two stylistically different sources of text data: books from Project Gutenberg3 and news articles from GigaWord v5 \[36\]. Using the same processing from \[32\] these datasets consist of 180M training tokens and 4B training tokens respectively, thus they cover a range of styles and corpus sizes. We choose a similar vocabulary size for all three datasets of approximately 250, 000, which is large enough to include rare words and numeric values.

---

Full document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/18-relational-recurrent-neural-networks](../../paper-pages/18-relational-recurrent-neural-networks/index.md)
