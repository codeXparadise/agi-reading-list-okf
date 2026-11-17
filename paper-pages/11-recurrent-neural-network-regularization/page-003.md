---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
page: 3
pages: [3]
page_of: 8
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "yt−2 yt−1 yt yt+1 yt+2 ✻ ✻ ✻ ✻ ✻ ✲ ✲ ✲ ✲ ✲ ✲ ✻ ✻ ✻ ✻ ✻ ✲ ✲ ✲ ✲ ✲ ✲ ✻ ✻ ✻ ✻ ✻ xt−2 xt−1 xt xt+1 xt+2 Figure 3: The thick line shows a typical path of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 8 - Recurrent Neural Network Regularization

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md)

yt−2 yt−1 yt yt+1 yt+2

✻

✻

✻

✻

✻

✲

✲

✲

✲

✲

✲

✻

✻

✻

✻

✻

✲

✲

✲

✲

✲

✲

✻

✻

✻

✻

✻

xt−2 xt−1 xt xt+1 xt+2

Figure 3: The thick line shows a typical path of information flow in the LSTM. The information is affected by dropout L + 1 times, where L is depth of network.

the meaning of life is that only if an end would be of the whole supplier. widespread rules are regarded as the companies of refuses to deliver. in balance of the nation ’s information and loan growth associated with the carrier thrifts are in the process of slowing the seed and commercial paper.

the meaning of life is nearly in the first several months before the government was addressing such a move as president and chief executive of the nation past from a national commitment to curb grounds. meanwhile the government invests overcapacity that criticism and in the outer reversal of small-town america.

Figure 4: Some interesting samples drawn from a large regularized model conditioned on “The meaning of life is”. We have removed “unk”, “N”, “$” from the set of permissible words.

and this number is independent of the number of timesteps traversed by the information. Standard dropout perturbs the recurrent connections, which makes it difficult for the LSTM to learn to store information for long periods of time. By not using dropout on the recurrent connections, the LSTM can benefit from dropout regularization without sacrificing its valuable memorization ability.

## 4 EXPERIMENTS

We present results in three domains: language modeling (Section 4.1), speech recognition (Section 4.2), machine translation (Section 4.3), and image caption generation (Section 4.4).

4.1 LANGUAGE MODELING

We conducted word-level prediction experiments on the Penn Tree Bank (PTB) dataset Marcus et al. (1993), which consists of 929k training words, 73k validation words, and 82k test words. It has 10k words in its vocabulary. We downloaded it from Tomas Mikolov’s webpage†. We trained regularized LSTMs of two sizes; these are denoted the medium LSTM and large LSTM. Both LSTMs have two layers and are unrolled for 35 steps. We initialize the hidden states to zero. We then use the final hidden states of the current minibatch as the initial hidden state of the subsequent minibatch (successive minibatches sequentially traverse the training set). The size of each minibatch is 20.

†http://www.fit.vutbr.cz/˜imikolov/rnnlm/simple-examples.tgz

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
