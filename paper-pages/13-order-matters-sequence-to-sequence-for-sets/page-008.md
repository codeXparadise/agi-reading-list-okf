---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
page: 8
pages: [8]
page_of: 11
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "• We pretrain the model with a uniform prior over π(X) for 1000 steps, which amounts to replacing the maxπ(Xi) in eq. (9) by a P π(Xi). • We then…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 8 of 11 - Order Matters: Sequence to Sequence for Sets

> Page 8 of the source PDF, verbatim as extracted. Canonical document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md)

• We pretrain the model with a uniform prior over π(X) for 1000 steps, which amounts to replacing the maxπ(Xi) in eq. (9) by a P

π(Xi).

• We then pick an ordering by sampling π(X) according to a distribution proportional to p(Yπ(X)|X). This costs O(1) model evaluations (vs. naive search which would be O(n!)).

Crucially, sampling p(Yπ(X)|X) can be done very efficiently as we can use ancestral sampling (leftto-right) which requires to evaluate p(.) only once instead of n!.

5.2.1 5-GRAM MODELING

In our initial attempt to solve (9), we considered a simplified version of the language modeling task described in Section 5.1.1. The simplified task consists of modeling the joint probability of 5grams without any further context (i.e., there is no input X). This choice allowed us to have a small enough n as initially we were trying to exactly find the best ordering out of the n! possible ones. Thus, we disregarded possible effects of inexact search, and focused on the essential of the training dynamics where the model being optimized picks the best ordering π which maximizes p(Yπ) under its current parameters, and reinforces that ordering by applying updates on the gradient of log p(Yπ) w.r.t. the parameters. Eventually, as noted in Section 5.2, we found sampling to be superior in terms of convergence, whilst simplifying the complexity from O(n!) down to O(1), and is the preferred solution which we used in the rest of this section.

To test this framework, we converted 5-grams (i.e., sequences of words) to a set in the following way:

5-gram (sequence): y1=This, y2=is, y3=a, y4=five, y5=gram 5-gram (set): y1=(This,1), y2=(is,2), y3=(a,3), y4=(five,4), y5=(gram,5)

Note that adding the original position alongside the words makes Y a set. Thus, we can shuffle Y in arbitrarily without losing the original structure of the sequence. The first experiment, which reinforces our result in Section 5.1.1, tests the hypothesis once again that order matters. Training a model which follows the natural order (i.e., produces (This,1), followed by (is,2) conditioned on (This,1), etc.), achieves a validation perplexity of 225.2 If, instead of picking (1, 2, 3, 4, 5), we use (5, 1, 3, 4, 2), perplexity drops to 280.

We then test optimization of eq. (9) in two setups:

Easy: The training set contains examples from (1, 2, 3, 4, 5) and (5, 1, 3, 4, 2), uniformly sampled. Hard: The training set contains examples from the 5! possible orderings, uniformly sampled.

Our results are shown in Table 2. Note that, in the easy case, we restrict the search space over orderings to only 2, where one order is clearly better than the other. We note that, after the pretraining phase, we decide which of the two orderings is better to represent the data under the model being trained. Very quickly, the model settles on the natural (1, 2, 3, 4, 5) ordering, yielding a perplexity of 225. In the most difficult case, where any order is possible, the model settles to orders such as (1, 2, 3, 4, 5), (5, 4, 3, 2, 1), and small variations of them. In all cases, the final perplexity is 225. Thus, the framework we propose is able to find good orderings without any prior knowledge. We plan to not only recover optimal orderings, but find ones that were unknown to us when applying the seq2seq framework naively.

Table 2: Experiments in which the model finds the optimal ordering of a set for the 5-gram language modeling task. Perplexities are reported on the validation set (lower is better).

Task Orders considered Perplexity (1, 2, 3, 4, 5) 1 225 (5, 1, 3, 4, 2) 1 280 Easy 2 225 Hard 5! 225

2This is much worse than the results reported in Section 5.1.1 since modeling 5-grams without context is much harder than standard language modeling.

---

[previous page](page-007.md) · [next page](page-009.md) · [all pages](index.md)
