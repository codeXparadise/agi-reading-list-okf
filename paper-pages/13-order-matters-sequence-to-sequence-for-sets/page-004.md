---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
page: 4
pages: [4]
page_of: 11
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "• A write block, which is an LSTM pointer network (Vinyals et al., 2015a) that takes in q∗ T (as the context it needs from which to produce the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 11 - Order Matters: Sequence to Sequence for Sets

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md)

• A write block, which is an LSTM pointer network (Vinyals et al., 2015a) that takes in q∗ T (as the context it needs from which to produce the output from the input set), and points at elements of mi (implicitly, xi), one step at a time. The original work in Vinyals et al. (2015a) used a pointer mechanism which, instead of issuing a readout of memory by a weighted sum with a soft pointer (see eq. 6), it uses the pointer as part of the loss. We extended this by adding an extra attention step before the pointer (we called this glimpse). This is related to the process block described above, but with the difference that the attention reads happen interleaved between each pointer output. As described later in the results, we found these two mechanisms to complement each other.

The architecture is depicted in Figure 1 and can be seen as a special case of a Neural Turing Machine or Memory Network. It satisfies the key property of being invariant to the order of the elements in X, thus effectively processing the inputs as a set. Also note that the write component could simply be an LSTM if the outputs were from a fixed dictionary. For this model, though, we study combinatorial problems where the outputs are pointers to the inputs, so we use a pointer network.

4.4 SORTING EXPERIMENT

In order to verify if our model handles sets more efficiently than the vanilla seq2seq approach, we ran the following experiment on artificial data for the task of sorting numbers: given N unordered random floating point numbers between 0 and 1, we return them in a sorted order. Note that this problem is an instance of set2seq. We used the architecture defined in Figure 1, where the Read module is a small multilayer perceptron for each number, the Process module is an attention mechanism over the read numbers, implemented as T steps over an LSTM with no input nor output, but attending the input embeddings, followed by an LSTM to produce indices in the input numbers with a pointer network (Vinyals et al., 2015a), in the proper sorted order. We also compared this architecture with a vanilla seq2seq architecture made of an input LSTM connected to an output LSTM which produces indices in the input numbers with a pointer network (Ptr-Net). Note that the only difference between these two models is the encoding of the set using either an LSTM (as in previous work), or with the architecture proposed in the previous section. We ran multiple experiments, varying the number N of numbers to sort, as well as the number T of processing steps of the Read, Process, Write model.

The out-of-sample accuracies (whether we succeeded in sorting all numbers or not) of these experiments are summarized in Table 1. We can see that the baseline pointer network LSTM input model is better than the Read-Process-and-Write model when no processing steps (P = 0 step) are used, but as soon as at least one processing step is allowed, the performance of the Read-Process-and-Write model gets better, increasing with the number of processing steps. We can also see that, as the size of the task (expressed in the number of elements to sort N) grows, the performance gets worse, as expected. Also note that with 0 processing steps and 0 glimpses, the writing module is effectively unconditioned on X and has to “blindly” point at the elements of X. Thus, it is unsurprising to see it performing worse than any other model considered in Table 1. Lastly, equipping the writing module with glimpses (i.e., adding an attention mechanism prior to “pointing”) improves both the baseline model (Ptr-Net), and our proposed modification quite significantly (in the most challenging cases, it more than doubles accuracy).

Table 1: The sorting experiment: out-of-sample sorting accuracy for various problem sizes and processing steps, with or without glimpses. All the reported accuracies are shown after reaching 10000 training iterations, at which point all models had converged but none overfitted. Higher is better.

Length N Ptr-Net P = 0 step P = 1 step P = 5 steps P = 10 steps glimpses 0 1 0 1 0 1 0 1 0 1 N = 5 81% 90% 65% 84% 84% 92% 88% 94% 90% 94% N = 10 8% 28% 7% 30% 14% 44% 17% 57% 19% 50% N = 15 0% 4% 1% 2% 0% 5% 2% 4% 0% 10%

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
