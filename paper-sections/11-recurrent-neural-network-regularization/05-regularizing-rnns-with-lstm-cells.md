---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
section: 3 REGULARIZING RNNS WITH LSTM CELLS
section_role: other
section_index: 5
pages: [1, 2, 3]
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "In this section we describe the deep LSTM (Section 3.1). Next, we show how to regularize them (Section 3.2), and explain why our regularization…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 REGULARIZING RNNS WITH LSTM CELLS

> Section 5 of 9 from [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · `other` · pages 1-3

In this section we describe the deep LSTM (Section 3.1). Next, we show how to regularize them (Section 3.2), and explain why our regularization scheme works.

We let subscripts denote timesteps and superscripts denote layers. All our states are n-dimensional. Let hl

t ∈Rn be a hidden state in layer l in timestep t. Moreover, let Tn,m : Rn →Rm be an affine transform (Wx + b for some W and b). Let ⊙be element-wise multiplication and let h0

t be an input word vector at timestep k. We use the activations hL

t to predict yt, since L is the number of layers in our deep LSTM.

3.1 LONG-SHORT TERM MEMORY UNITS

The RNN dynamics can be described using deterministic transitions from previous to current hidden states. The deterministic state transition is a function

RNN : hl−1

t , hl

t−1 →hl

t

For classical RNNs, this function is given by

t−1), where f ∈{sigm, tanh}

t = f(Tn,nhl−1

hl

t + Tn,nhl

The LSTM has complicated dynamics that allow it to easily “memorize” information for an extended number of timesteps. The “long term” memory is stored in a vector of memory cells cl

t ∈Rn. Although many LSTM architectures that differ in their connectivity structure and activation functions, all LSTM architectures have explicit memory cells for storing information for long periods of time. The LSTM can decide to overwrite the memory cell, retrieve it, or keep it for the next time step. The LSTM architecture used in our experiments is given by the following equations Graves et al. (2013):

LSTM : hl−1

t , hl

t−1, cl

t−1 →hl

t, cl

t 

i f o g

sigm sigm sigm tanh







hl−1

t hl

 T2n,4n

 =

 

 

t−1

cl

t = f ⊙cl

t−1 + i ⊙g

hl

t = o ⊙tanh(cl

t)

In these equations, sigm and tanh are applied element-wise. Figure 1 illustrates the LSTM equations.

3.2 REGULARIZATION WITH DROPOUT

The main contribution of this paper is a recipe for applying dropout to LSTMs in a way that successfully reduces overfitting. The main idea is to apply the dropout operator only to the non-recurrent

hl−1

hl−1

❆❯ hl

gate ❆❯ hl

t−1

t−1

t

t

✁✁☛

✁✁☛

✎☞

✎☞

i Input

o Output

gate

✍✌

✍✌

❏

❏❏❫ ❢ ×

Cell

✎☞

✎☞

hl−1

✘✘ ✿ ❳❳ ③

❄ hl

✲

✲

✲

✲

t

❢ ×

ct

g

✍✌

✍✌

t hl

t−1

✣

Input modulation

✠

❢ ×

✎☞

✻

gate

f Forget gate

✍✌

✁✁✕ hl

t−1 ❆❆❑hl−1

t

Figure 1: A graphical representation of LSTM memory cells used in this paper (there are minor differences in comparison to Graves (2013)).

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

Figure 2: Regularized multilayer RNN. The dashed arrows indicate connections where dropout is applied, and the solid lines indicate connections where dropout is not applied.

connections (Figure 2). The following equation describes it more precisely, where D is the dropout operator that sets a random subset of its argument to zero:

i f o g

sigm sigm sigm tanh









D(hl−1

t ) hl

 T2n,4n

 =

 

 

t−1

cl

t = f ⊙cl

t−1 + i ⊙g

hl

t = o ⊙tanh(cl

t)

Our method works as follows. The dropout operator corrupts the information carried by the units, forcing them to perform their intermediate computations more robustly. At the same time, we do not want to erase all the information from the units. It is especially important that the units remember events that occurred many timesteps in the past. Figure 3 shows how information could flow from an event that occurred at timestep t −2 to the prediction in timestep t + 2 in our implementation of dropout. We can see that the information is corrupted by the dropout operator exactly L + 1 times,

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

---

Full document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · Page-level evidence: [paper-pages/11-recurrent-neural-network-regularization](../../paper-pages/11-recurrent-neural-network-regularization/index.md)
