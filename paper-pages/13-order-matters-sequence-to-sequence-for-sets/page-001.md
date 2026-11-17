---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
page: 1
pages: [1]
page_of: 11
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "2 RELATED WORK Since sequence-to-sequence models were proposed for machine translation (Sutskever et al., 2014; Cho et al., 2014; Kalchbrenner &…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 11 - Order Matters: Sequence to Sequence for Sets

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md)

## 2 RELATED WORK

Since sequence-to-sequence models were proposed for machine translation (Sutskever et al., 2014; Cho et al., 2014; Kalchbrenner & Blunsom, 2013), the research community has proposed several applications in which these models can perform mappings from and/or to sequences. For example, image captioning maps from an image to a sentence (Vinyals et al., 2015c; Mao et al., 2015; Donahue et al., 2015), parsing maps from a sentence to a (linearized) parse tree (Vinyals et al., 2015b), and models for computation map from problem statements (e.g. a python program or a set of points on the plane) to their solutions (the answer to the program (Zaremba & Sutskever, 2014), or the traveling salesman problem tour for the set of points (Vinyals et al., 2015a)). It is out of the scope of this paper to review all successful applications of seq2seq, but the list above already includes some non-trivial examples of mapping to/from objects that are not necessarily sequences.

More recently, many related models and key contributions have been proposed, that utilize the concept of external memories, including RNNSearch (Bahdanau et al., 2015a), Memory Networks (Weston et al., 2015) and Neural Turing Machines (Graves et al., 2014). The key element that these models utilize is a reading (or attention) mechanism to read these external memories in a fully differentiable way (though there has also been work with discrete reading mechanism, most notably RL-NTM (Zaremba & Sutskever, 2015)).

Unlike traditional structured prediction algorithms (Bakir et al., 2007), our approach relies on the chain rule to serialize output random variables through the strong capabilities of LSTM networks to model long-term correlation. Similarly, we do not want to assume a known structured input, as is done for instance with recursive neural networks (Socher et al., 2010) which encode sentences recursively as (given) trees.

## 3 NEURAL NETWORKS FOR SEQUENCES AND SETS

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

---

first page · [next page](page-002.md) · [all pages](index.md)
