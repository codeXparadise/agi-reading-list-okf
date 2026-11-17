---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
section: A.4 Language Modeling
section_role: other
section_index: 25
pages: [16, 17, 18]
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "We trained the Recurrent Memory Core with Adam, using a learning rate of 0.001 and gradients were clipped to have a maximum L2 norm of 0.1.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# A.4 Language Modeling

> Section 25 of 25 from [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · `other` · pages 16-18

We trained the Recurrent Memory Core with Adam, using a learning rate of 0.001 and gradients were clipped to have a maximum L2 norm of 0.1. Backpropagation-through-time was truncated to a window-length of 100. The model was trained with 6 Nvidia Tesla P100 GPUs synchronously. Each GPU trained with a batch of 64 and so the total batch size was 384. We used 512 (with 0.5 dropout) as the word embedding sizes, and tied the word embedding matrix parameters to the output softmax.

We swept over the following model architecture parameters:

• Total units in memory {1000, 1500, 2000, 2500, 3000}

• Attention heads {1, 2, 3, 4, 5}

• Number of memories {1, 2}

• MLP layers {1, 2, 3, 4, 5}

• Attention blocks {1, 2, 3, 4}

and chose 2500 total units, 4 heads, 1 memory, a 5-layer MLP, and 1 attention block based upon validation error on WikiText-103. We used these same parameters for GigaWord and Project Gutenberg without additional sweeps, due to the expense of training.

![Figure, page 18](../../assets/18/fig-18-p18-13.png)

60

RMC LSTM

55

50

Perplexity

45

40

35

30

0 1 2 3 4 5 6 7 8 Steps (B)

Figure 11: Validation perplexity on WikiText-103. LSTM comparison from \[32\]. Visual display of data may not match numbers from table 2 because of curve smoothing.

![Figure, page 18](../../assets/18/fig-18-p18-14.png)

25

RMC LSTM

Perplexity increase

20

15

10

5

0

0 100 200 300 400 500 Test unroll length

Figure 12: Perplexity as a function of test unroll length. Increase in perplexity when models are unrolled for shorter sequence lengths at test time without state transfer between unrolls. Perplexities are compared against the ‘best’ perplexity where the model is unrolled continuously over the full test set. We see that both models incorporate little information beyond 500 words. Furthermore, the RMC has a smaller gain in perplexity (drop in performance) when unrolled over shorter time steps in comparison to the LSTM, e.g. a regression of 1 perplexity for the RMC vs 5 for the LSTM at 100 time steps. This suggests it is focusing on more recent words in the text.

Table 3: Test perplexity split by word frequency on GigaWord v5. Words are bucketed by the number of times they occur in training set, > 10K contains the most frequent words.

> 10K 10K-1K < 1K All

LSTM \[32\] 39.4 6.5e3 3.7e4 53.5 LSTM + Hebbian Softmax \[32\] 33.2 3.2e3 1.6e4 43.7 RMC 28.3 3.1e3 6.9e4 38.3

---

Full document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/18-relational-recurrent-neural-networks](../../paper-pages/18-relational-recurrent-neural-networks/index.md)
