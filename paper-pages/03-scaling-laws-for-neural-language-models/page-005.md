---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 5
pages: [5]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "be maximally compute-efficient because of hardware constraints. Optimal performance depends on total compute as a power law (see Equation (1.3)). We…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 30 - Scaling Laws for Neural Language Models

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

be maximally compute-efficient because of hardware constraints. Optimal performance depends on total compute as a power law (see Equation (1.3)).

We provide some basic theoretical motivation for Equation (1.5), an analysis of learning curve fits and their implications for training time, and a breakdown of our results per token. We also make some brief comparisons to LSTMs and recurrent Transformers \[DGV+18\].

## 1.3 Notation

We use the following notation:

• L – the cross entropy loss in nats. Typically it will be averaged over the tokens in a context, but in some cases we report the loss for specific tokens within the context. • N – the number of model parameters, excluding all vocabulary and positional embeddings • C ≈6NBS – an estimate of the total non-embedding training compute, where B is the batch size, and S is the number of training steps (ie parameter updates). We quote numerical values in PF-days, where one PF-day = 1015 × 24 × 3600 = 8.64 × 1019 floating point operations. • D – the dataset size in tokens • Bcrit – the critical batch size \[MKAT18\], defined and discussed in Section 5.1. Training at the critical batch size provides a roughly optimal compromise between time and compute efficiency. • Cmin – an estimate of the minimum amount of non-embedding compute to reach a given value of the loss. This is the training compute that would be used if the model were trained at a batch size much less than the critical batch size. • Smin – an estimate of the minimal number of training steps needed to reach a given value of the loss. This is also the number of training steps that would be used if the model were trained at a batch size much greater than the critical batch size. • αX – power-law exponents for the scaling of the loss as L(X) ∝1/XαX where X can be any of N, D, C, S, B, Cmin.

## 2 Background and Methods

We train language models on WebText2, an extended version of the WebText \[RWC+19\] dataset, tokenized using byte-pair encoding \[SHB15\] with a vocabulary size nvocab = 50257. We optimize the autoregressive log-likelihood (i.e. cross-entropy loss) averaged over a 1024-token context, which is also our principal performance metric. We record the loss on the WebText2 test distribution and on a selection of other text distributions. We primarily train decoder-only \[LSP+18, RNSS18\] Transformer \[VSP+17\] models, though we also train LSTM models and Universal Transformers \[DGV+18\] for comparison.

## 2.1 Parameter and Compute Scaling of Transformers

We parameterize the Transformer architecture using hyperparameters nlayer (number of layers), dmodel (dimension of the residual stream), dﬀ(dimension of the intermediate feed-forward layer), dattn (dimension of the attention output), and nheads (number of attention heads per layer). We include nctx tokens in the input context, with nctx = 1024 except where otherwise noted.

We use N to denote the model size, which we define as the number of non-embedding parameters

N ≈2dmodelnlayer (2dattn + dﬀ)

= 12nlayerd2

model with the standard dattn = dﬀ/4 = dmodel (2.1)

where we have excluded biases and other sub-leading terms. Our models also have nvocabdmodel parameters in an embedding matrix, and use nctxdmodel parameters for positional embeddings, but we do not include these when discussing the ‘model size’ N; we will see that this produces significantly cleaner scaling laws.

Evaluating a forward pass of the Transformer involves roughly

Cforward ≈2N + 2nlayernctxdmodel (2.2)

add-multiply operations, where the factor of two comes from the multiply-accumulate operation used in matrix multiplication. A more detailed per-operation parameter and compute count is included in Table 1.

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
