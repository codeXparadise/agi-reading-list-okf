---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
page: 12
pages: [12]
page_of: 18
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "A Further task details, analyses, and model configurations In the following sections we provide further details on the experiments and the model…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 12 of 18 - Relational Recurrent Neural Networks

> Page 12 of the source PDF, verbatim as extracted. Canonical document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md)

## A Further task details, analyses, and model configurations

In the following sections we provide further details on the experiments and the model configurations. We will sometimes refer to the following terms when describing the model:

• “total units”: The total number of elements in the memory matrix M. Equivalent to the size of each memory multiplied by the number of memories.

• “num heads”: The number of attention heads; i.e., the number of unique sets of queries, keys, and values produced for the memories.

• “memory slots” or “number of memories”: Equivalent to the number of rows in matrix M.

• “num blocks”: The number of iterations of attention performed at each time-step.

• “gate style”: Gating per unit or per memory slot

A.1 N th Farthest

Inputs consisted of sequences of eight randomly sampled, 16-dimensional vectors from a uniform distribution xt ∼U(−1, 1), and vector labels lt ∼{1, 2, ..., 8}, encoded as a one-hot vectors and sampled without replacement. Labels were sampled and hence did not correspond to the time-points at which the vectors were presented to the model. Appended to each vector-label input was the task specification (i.e., the values of n and m for that sequence), also encoded as one-hot vectors. Thus, an input for time-step t was a 40-dimensional vector (xt; lt; n; m).

For all models (RMC, LSTM, DNC) we used the Adam optimiser \[44\] with a batch size of 1600, learning rates tuned between 1e−5 and 1e−3, and trained using a softmax cross entropy loss function. All the models had an equivalent 4-layer MLP (256 units per layer with ReLu non-linearities) to process their outputs to produce logits for the softmax. Learning rate did not seem to influence performance, so we settled on 1e−4 for the final experiments.

For the LSTM and DNC, architecture parameters seemingly made no difference to model performance. For the LSTM we tried hidden sizes ranging from 64 up to 4096 units, and for the DNC we tried 1, 8, or 16 memories, 128, 512, or 1024 memory sizes (which we tied to the controller LSTM size), and 1, 2, or 4 memory reads & writes. The DNC used a 2-layer LSTM controller.

For the RMC we used 1, 8, or 16 memories with 2048 total units (so, the size of each memory was 2048 num\_mems), 1, 8, or 16 heads, 1 block of attention, and both the ‘unit’ and ‘memory’ gating methods. Figure 4 shows the results of a hyperparameter sweep scaled according to wall-clock time (models with more but smaller memories are faster to run than those with fewer but larger memories, and we chose to compare models with equivalent number of total units in the memory matrix M).

## A.2 Program Evaluation

To further study the effect of relational structure on working memory and symbolic representation we turned to a set of problems that provided insights into the RMC’s fitness as a generalized computational model. The Learning to Execute (LTE) dataset \[25\] provided a good starting point for assessing the power of our model over this class of problems. Sample problems are of the form of linear time, constant memory, mini-programs.

Training samples were generated in batches of 128 on-the-fly. Each model was trained for 200K iterations using an Adam optimiser and learning rate of 1e−3. The samples were parameterized by literal length and nesting depth which define the length of terminal values in the program snippets and the level of program operation nesting. Within each batch the literal length and nesting value was sampled uniformly up to the maximum value for each - this is consistent with the Mix curriculum strategy from \[25\]. We evaluated the model against a batch of 12800 samples using the maximum nesting and literal length values for all samples and report the top score. Examples of samples for each task can be found in figure 6 and figure 7. It also worth noting that the modulus operation was applied to addition, control, and full program samples so as to bound the output to the maximum literal length in case of longer for-loops.

The sequential model consists of an encoder and a decoder which each take the form of a recurrent neural network \[45, 25\]. Once the encoder has processed the input sequence the state of the encoder is used to initialize the decoder state and subsequently to generate the target sequence (program output). The output from all models is passed through a 4-layer MLP - all layers have size 256 with an output ReLU - to generate an output embedding at each step of the output sequence.

In \[25\] teacher forcing is used for both training and testing in the decode phase. For our experiments, we began by exploring teacher forcing during training but used model predictions from the previous step as input to the the decoder at the next step when evaluating the model \[45\]. We also considered the potential effect of limiting

---

[previous page](page-011.md) · [next page](page-013.md) · [all pages](index.md)
