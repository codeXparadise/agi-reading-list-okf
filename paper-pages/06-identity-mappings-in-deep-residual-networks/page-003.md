---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/06-identity-mappings-in-deep-residual-networks.md
source: ../../papers/06-identity-mappings-in-deep-residual-networks.md
paper_title: Identity Mappings in Deep Residual Networks
sequence: 6
page: 3
pages: [3]
page_of: 15
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "is unlikely for the gradient ∂E ∂xl to be canceled out for a mini-batch, because in general the term ∂ ∂xl PL−1 i=l F cannot be always -1 for all…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 15 - Identity Mappings in Deep Residual Networks

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md)

is unlikely for the gradient ∂E ∂xl to be canceled out for a mini-batch, because in general the term ∂ ∂xl

PL−1

i=l F cannot be always -1 for all samples in a mini-batch. This implies that the gradient of a layer does not vanish even when the weights are arbitrarily small.

## Discussions

Eqn.(4) and Eqn.(5) suggest that the signal can be directly propagated from any unit to another, both forward and backward. The foundation of Eqn.(4) is two identity mappings: (i) the identity skip connection h(xl) = xl, and (ii) the condition that f is an identity mapping.

These directly propagated information flows are represented by the grey arrows in Fig. 1, 2, and 4. And the above two conditions are true when these grey arrows cover no operations (expect addition) and thus are “clean”. In the following two sections we separately investigate the impacts of the two conditions.

## 3 On the Importance of Identity Skip Connections

Let’s consider a simple modification, h(xl) = λlxl, to break the identity shortcut:

xl+1 = λlxl + F(xl, Wl), (6)

where λl is a modulating scalar (for simplicity we still assume f is identity). Recursively applying this formulation we obtain an equation similar to Eqn. (4): xL = (QL−1

i=l λi)xl + PL−1

i=l (QL−1

j=i+1 λj)F(xi, Wi), or simply:

L−1 Y

L−1 X

ˆF(xi, Wi), (7)

xL = (

λi)xl +

i=l

i=l

where the notation ˆF absorbs the scalars into the residual functions. Similar to Eqn.(5), we have backpropagation of the following form:

L−1 Y

L−1 X

!

∂E ∂xl

= ∂E

λi) + ∂

ˆF(xi, Wi)

(

. (8)

∂xL

∂xl

i=l

i=l

Unlike Eqn.(5), in Eqn.(8) the first additive term is modulated by a factor QL−1

i=l λi. For an extremely deep network (L is large), if λi > 1 for all i, this factor can be exponentially large; if λi < 1 for all i, this factor can be exponentially small and vanish, which blocks the backpropagated signal from the shortcut and forces it to flow through the weight layers. This results in optimization diﬃculties as we show by experiments.

In the above analysis, the original identity skip connection in Eqn.(3) is replaced with a simple scaling h(xl) = λlxl. If the skip connection h(xl) represents more complicated transforms (such as gating and 1×1 convolutions), in Eqn.(8) the first term becomes QL−1

i where h′ is the derivative of h. This product may also impede information propagation and hamper the training procedure as witnessed in the following experiments.

i=l h′

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
