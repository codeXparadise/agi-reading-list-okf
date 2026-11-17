---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
section: 3 NEURAL NETWORKS FOR SEQUENCES AND SETS
section_role: method
section_index: 5
pages: [1, 2]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "Let us consider a generic supervised task with a given training set of n pairs (Xi, Y i)n i=1 where (Xi, Y i) is the ith pair of an input and its…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 NEURAL NETWORKS FOR SEQUENCES AND SETS

> Section 5 of 9 from [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md) · `method` · pages 1-2

Let us consider a generic supervised task with a given training set of n pairs (Xi, Y i)n

i=1 where (Xi, Y i) is the ith pair of an input and its corresponding target. The sequence-to-sequence paradigm corresponds to tasks where both Xi and Y i are represented by sequences, of possibly different lengths: Xi = {xi

1, xi 2, . . . , xi si} and Y i = {yi

1, yi 2, . . . , yi ti}. In this case, it is reasonable to model each example using the conditional probability P(Y |X) and to use the chain rule to decompose it as follows (we drop the example index i in the rest of this section for readability):

T Y

P(Y |X) =

P(yt|y1, y2, . . . , yt−1, X)

t=1

and implement it as an encoder recurrent neural network (RNN) to read sequentially each xs ∈X as follows:

hs = fenc(hs−1, xs) (1) where hs is the state of the encoder at time s, followed by a decoder RNN to produce each yt ∈Y one at a time, given the current state gt and the previous yt−1 symbol:

g1 = hs gt = fdec(gt−1, yt−1)

P(yt|y1, y2, . . . , yt−1, X) = softmax(affine(gt)) . (2)

The use of the chain rule makes this approach assumption free, so when the input X corresponds to a sequence (like a sentence), it is reasonable to read it sequentially into an RNN, as in eq. (1). However, how should we encode X if it does not correspond naturally to a sequence? For instance, what if it corresponds to an unordered set of elements?

Similarly, when the target Y corresponds to a sequence, it is reasonable to produce it sequentially with an RNN, as in eq. (2), but how should we produce Y if it does not correspond naturally to a sequence?

Note that sequences can be encoded as sets. Indeed, if we associate to each element of a sequence the index it occupies in it, forming a tuple, we effectively convert this sequence to a set. For example, the

sequence “I like cats” becomes the set {(I,1), (like,2), (cats,3)} (note that we can permute elements in the set but still recover the original sequence). Although this may be unnecessary in some cases, we argue that, even for sequences, inputting and/or outputting them in a different order could be beneficial. For example, in sorting we may want to employ a divide-and-conquer strategy which finds the median element first (i.e., we may output the solution in neither increasing nor decreasing sequential order).

In the following two sections we discuss how to extend seq2seq to handle input sets (Section 4) and output sets (Section 5). We also show the importance of ordering in a variety of tasks in which seq2seq has successfully been applied, and include experimental results to support our claims and extensions to the existing models.

---

Full document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md) · Page-level evidence: [paper-pages/13-order-matters-sequence-to-sequence-for-sets](../../paper-pages/13-order-matters-sequence-to-sequence-for-sets/index.md)
