---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
page: 2
pages: [2]
page_of: 11
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "sequence “I like cats” becomes the set {(I,1), (like,2), (cats,3)} (note that we can permute elements in the set but still recover the original…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 11 - Order Matters: Sequence to Sequence for Sets

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md)

sequence “I like cats” becomes the set {(I,1), (like,2), (cats,3)} (note that we can permute elements in the set but still recover the original sequence). Although this may be unnecessary in some cases, we argue that, even for sequences, inputting and/or outputting them in a different order could be beneficial. For example, in sorting we may want to employ a divide-and-conquer strategy which finds the median element first (i.e., we may output the solution in neither increasing nor decreasing sequential order).

In the following two sections we discuss how to extend seq2seq to handle input sets (Section 4) and output sets (Section 5). We also show the importance of ordering in a variety of tasks in which seq2seq has successfully been applied, and include experimental results to support our claims and extensions to the existing models.

## 4 INPUT SETS

We first study extensions to encoding (reading) sets. As we discussed in the previous section, sequences can be read with a recurrent neural network which can compress its contents into a vector. An important invariance property that must be satisfied when the input is a set (i.e., the order does not matter) is that swapping two elements xi and xj in the set X should not alter its encoding.

A simple approach which satisfies this, and which in fact has been commonly used for encoding sentences, is the bag-of-words approach. In this case, the representation is simply a reduction (e.g., addition) of counts, word embeddings, or similar embedding functions, and is naturally permutation invariant. For language and other domains which are naturally sequential, this is replaced with more complex encoders such as recurrent neural networks that take order into account and model higher order statistics of the data.

An unsatisfying property of using a reduction operation (such as addition) is that it makes the representation quite inefficient: the model operates over a fixed dimensional embedding regardless of the length of the set. It is unlikely that such representation will succeed, as the amount of memory required to encode a length T set (or sequence, for that matter) should increase as a function of T. Thus, we argue that even deep convolutional architectures will suffer from this limitation – though some modifications exist (Maas et al., 2012).

In our work, we largely rely on attention mechanisms to integrate information from a variable length structure, which we describe in Section 4.2.

4.1 INPUT ORDER MATTERS

In this section, we highlight prior work where we observed that the order of inputs impacted the performance of seq2seq models taking sequences as input. In principle, order should not matter when using a complex encoder such as a recurrent neural network, as these are universal approximators that can encode complex features from the input sequence (e.g., n-grams of any order). We believe that the reason order seems to matter is due to the underlying non-convex optimization and more suitable prior.

The first example which we experimented with was altering the order of sequences in the context of machine translation. In machine translation, the mapping function encodes a sentence in a source language (e.g., English), and decodes it to its translation in a target language (e.g., French). By reversing the order of the input English sentence, Sutskever et al. (2014) got a 5.0 BLEU score improvement which allowed them to close the gap between their model – a fully end-to-end model for machine translation – and state-of-the-art models which were highly engineered. Similarly, for constituency parsing, in which the mapping is from an English sentence to a flattened version of its constituency parse tree, a 0.5% absolute increase in F1 score was observed when reversing the English sentence (Vinyals et al., 2015b).

Furthermore, if we preprocess the data for, e.g., convex hull computation that was presented in Vinyals et al. (2015a) by sorting the points by angle, the task becomes simpler (from O(n log n) to O(n)), and as a result the models obtained are much faster to train and better (increasing accuracy by up to 10% absolute in the most challenging cases).

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
