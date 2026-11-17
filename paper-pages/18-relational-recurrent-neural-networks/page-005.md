---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
page: 5
pages: [5]
page_of: 18
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "picked up. We also point the reader to the appendix for a description and results of another RL task called BoxWorld, which demands relational…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 18 - Relational Recurrent Neural Networks

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md)

picked up. We also point the reader to the appendix for a description and results of another RL task called BoxWorld, which demands relational reasoning in memory space.

## 4.3 Language Modeling

Finally, we investigate the task of word-based language modeling. We model the conditional probability p(wt|w<t) of a word wt given a sequence of observed words w<t = (wt−1, wt−2, . . . , w1). Language models can be directly applied to predictive keyboard and search-phrase completion, or they can be used as components within larger systems, e.g. machine translation \[27\], speech recognition \[28\], and information retrieval \[29\]. RNNs, and most notably LSTMs, have proven to be state-of-the-art on many competitive language modeling benchmarks such as Penn Treebank \[30, 31\], WikiText-103 \[32, 33\], and the One Billion Word Benchmark \[34, 35\]. As a sequential reasoning task, language modeling allows us to assess the RMC’s ability to process information over time on a large quantity of natural data, and compare it to well-tuned models.

We focus on datasets with contiguous sentences and a moderately large amount of data. WikiText-103 satisfies this set of requirements as it consists of Wikipedia articles shuffled at the article level with roughly 100M training tokens, as do two stylistically different sources of text data: books from Project Gutenberg3 and news articles from GigaWord v5 \[36\]. Using the same processing from \[32\] these datasets consist of 180M training tokens and 4B training tokens respectively, thus they cover a range of styles and corpus sizes. We choose a similar vocabulary size for all three datasets of approximately 250, 000, which is large enough to include rare words and numeric values.

## 5 Results

5.1 N th Farthest

This task revealed a stark difference between our LSTM and DNC baselines and RMC when training on 16-dimensional vector inputs. Both LSTM and DNC models failing to surpass 30% best batch accuracy and the RMC consistently achieving 91% at the end of training (see figure 5 in the appendix for training curves). The RMC achieved similar performance when the difficulty of the task was increased by using 32-dimensional vectors, placing a greater demand on high-fidelity memory storage. However, this performance was less robust with only a small number of seeds/model configurations demonstrating this performance, in contrast to the 16-dimensional vector case where most model configurations succeeded.

An attention analysis revealed some notable features of the RMC’s internal functions. Figure 3 shows attention weights in the RMC’s memory throughout a sequence: the first row contains a sequence where the reference vector m was observed last; in the second row it was observed first; and in the last row it was observed in the middle of the sequence. Before m is seen the model seems to shuttle input information into one or two memory slots, as shown by the high attention weights from these slots’ queries to the input key. After m is seen, most evident in row three of the figure, the model tends to change its attention behaviour, with all the memory slots preferentially focusing attention on those particular memories to which the m was written. Although this attention analysis provides some useful insights, the conclusions we can make are limited since even after a single round of attention the memory can become highly distributed, making any interpretations about information compartmentalisation potentially inaccurate.

## 5.2 Program Evaluation

Program evaluation performance was assessed via the Learning to Execute tasks \[25\]. We evaluated a number of baselines alongside the RMC including an LSTM \[3, 37\], DNC \[5\], and a bank of LSTMs resembling Recurrent Entity Networks \[38\] (EntNet) - the configurations for each of these is described in the appendix. Best test batch accuracy results are shown in Table 1. The RMC performs at least as well as all of the baselines on each task. It is marginally surpassed by a small fraction of performance on the double memorization task, but both models effectively solve this task. Further, the results of the RMC outperform all equivalent tasks from \[25\] which use teacher forcing even when evaluating model performance. It’s worth noting that we observed better results when we trained in a

3Project Gutenberg. (n.d.). Retrieved January 2, 2018, from www.gutenberg.org

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
