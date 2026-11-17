---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
page: 2
pages: [2]
page_of: 8
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "hl−1 hl−1 ❆❯ hl gate ❆❯ hl t−1 t−1 t t ✁✁☛ ✁✁☛ ✎☞ ✎☞ i Input o Output gate ✍✌ ✍✌ ❏ ❏❏❫ ❢ × Cell ✎☞ ✎☞ hl−1 ✘✘ ✿ ❳❳ ③ ❄ hl ✲ ✲ ✲ ✲ t ❢ × ct g ✍✌ ✍✌ t…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 8 - Recurrent Neural Network Regularization

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md)

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

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
