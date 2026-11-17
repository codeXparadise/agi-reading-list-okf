---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 3.3 SortaGrad
section_role: other
section_index: 8
pages: [6, 7]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Training on examples of varying length pose some algorithmic challenges. One possible solution is truncating backpropagation through time [68], so…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3 SortaGrad

> Section 8 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `other` · pages 6-7

Training on examples of varying length pose some algorithmic challenges. One possible solution is truncating backpropagation through time \[68\], so that all examples have the same sequence length during training \[52\]. However, this can inhibit the ability to learn longer term dependencies. Other works have found that presenting examples in order of difficulty can accelerate online learning \[6, 70\]. A common theme in many sequence learning problems including machine translation and speech recognition is that longer examples tend to be more challenging \[11\].

The CTC cost function that we use implicitly depends on the length of the utterance,

T Y

X

L(x, y; θ) = −log

pctc(ℓt|x; θ). (9)

t

ℓ∈Align(x,y)

where Align(x, y) is the set of all possible alignments of the characters of the transcription y to frames of input x under the CTC operator. In equation 9, the inner term is a product over time-steps of the sequence, which shrinks with the length of the sequence since pctc(ℓt|x; θ) < 1. This motivates a curriculum learning strategy we title SortaGrad. SortaGrad uses the length of the utterance as a heuristic for difficulty, since long utterances have higher cost than short utterances.

Architecture Simple RNN GRU

5 layers, 1 Recurrent 14.40 10.53 5 layers, 3 Recurrent 10.56 8.00 7 layers, 5 Recurrent 9.78 7.79 9 layers, 7 Recurrent 9.52 8.19

Table 3: Comparison of development set WER for networks with either simple RNN or GRU, for various depths. All models have batch normalization, one layer of 1D-invariant convolution, and approximately 38 million parameters.

In the first training epoch, we iterate through the training set in increasing order of the length of the longest utterance in the minibatch. After the first epoch, training reverts back to a random order over minibatches. Table 2 shows a comparison of training cost with and without SortaGrad on the 9 layer model with 7 recurrent layers. This effect is particularly pronounced for networks without BatchNorm, since they are numerically less stable. In some sense the two techniques substitute for one another, though we still find gains when applying SortaGrad and BatchNorm together. Even with BatchNorm we find that this curriculum improves numerical stability and sensitivity to small changes in training. Numerical instability can arise from different transcendental function implementations in the CPU and the GPU, especially when computing the CTC cost. This curriculum gives comparable results for both implementations.

We suspect that these benefits occur primarily because long utterances tend to have larger gradients, yet we use a fixed learning rate independent of utterance length. Furthermore, longer utterances are more likely to cause the internal state of the RNNs to explode at an early stage in training.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
