---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
page: 5
pages: [5]
page_of: 11
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "5 OUTPUT SETS So far, we have considered the problem of encoding input sets; let us now turn our attention to output representations. The chain rule…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 11 - Order Matters: Sequence to Sequence for Sets

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md)

## 5 OUTPUT SETS

So far, we have considered the problem of encoding input sets; let us now turn our attention to output representations. The chain rule which describes joint probabilities over sets of random variables Y is, perhaps, the simplest decomposition of the joint probability which does not incur arbitrary restrictions (such as conditional independence). Thus, as long as a powerful model that is trainable exists (which can cope with long range correlations), any order should work without any prior order information of the underlying problem that generated Y . Despite this, and even when a very powerful model (in terms of modeling power, and resilience to vanishing long term gradients) like the LSTM is employed, output ordering still plays a key role in successfully training models.

In the next subsection, we describe how the order in which we apply the chain rule affects the performance on various tasks.

5.1 OUTPUT ORDER MATTERS

Let Y be a set (or a sequence). In this section, we will study the effect that ordering has on the performance of seq2seq models on several tasks. Namely, we will consider arbitrary (and non-arbitrary) orders over the variables in Y , and model the conditional probability distribution P(Y |X) following that order for all training examples. As we will see, order matters (even when considering that the formulation through the chain rule works regardless of the ordering of Y , at least in principle).

5.1.1 LANGUAGE MODELING

For this experiment, we use the PennTree Bank, which is a standard language modeling benchmark. This dataset is quite small for language modeling standards, so most models are data starved. We trained medium sized LSTMs with large amounts of regularization (see medium model from Zaremba et al. (2014)) to estimate probabilities over sequences of words. We consider three version of the dataset with three orderings: natural, reverse, and a fixed, 3-word reversal:

Natural: “This is a sentence .” Reverse: “. sentence a is This” 3-word: “a is This <pad> . sentence”

Note that the 3-word reversal destroys the underlying structure of the sentence, and makes modeling the joint probability much more difficult since many higher order n-grams are scrambled. For each ordering we trained a different model. The results for both natural and reverse matched each other at 86 perplexity on the development set (using the same setup as Zaremba et al. (2014)). Surprisingly, the 3-word reversal degraded only 10 perplexity points, still achieving an impressive result in this corpus at 96 perplexity. We note, however, that training perplexities were also 10 points higher, which indicates that the model had trouble handling the awkward ordering. Thus, even when considering that the chain rule still properly models the joint probability, some degradation was observed when a confounding ordering was chosen.

5.1.2 PARSING

The task of constituency parsing consists in producing a parse tree given a sentence. The model proposed by Vinyals et al. (2015b) is a sentence encoder LSTM followed by a decoder LSTM trained to generate a depth first traversal encoding of the parse tree, using an attention mechanism. This approach matched state-of-the-art results on this task.

Even though it seemed more sensible, depth first traversal is only one of the many ways one can uniquely encode a tree onto a sequence. We thus tried to train a small model using depth first traversal (which matches the baseline of Vinyals et al. (2015b)) and another one using breadth first traversal (note that these orderings are input dependent). See Figure 2 for an example on how the tree linearizes under both traversal schemes. The model trained to produce depth first traversal linearized trees obtained 89.5% F1 score (as reported by Vinyals et al. (2015b)), whereas the one producing breadth first traversal trees had a much lower F1 score at 81.5%,1 showing again the importance of picking the right output ordering.

1In fact, in many cases the decoder failed to produce a valid tree, so the real F1 score is likely lower.

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
