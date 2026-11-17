---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/06-identity-mappings-in-deep-residual-networks.md
source: ../../papers/06-identity-mappings-in-deep-residual-networks.md
paper_title: Identity Mappings in Deep Residual Networks
sequence: 6
section: 2 Analysis of Deep Residual Networks
section_role: results
section_index: 3
pages: [1, 2, 3]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "The ResNets developed in [1] are modularized architectures that stack building blocks of the same connecting shape. In this paper we call these…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 Analysis of Deep Residual Networks

> Section 3 of 12 from [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md) · `results` · pages 1-3

The ResNets developed in \[1\] are modularized architectures that stack building blocks of the same connecting shape. In this paper we call these blocks “Residual

yl = h(xl) + F(xl, Wl), (1)

xl+1 = f(yl). (2)

Here xl is the input feature to the l-th Residual Unit. Wl = {Wl,k|1≤k≤K} is a set of weights (and biases) associated with the l-th Residual Unit, and K is the number of layers in a Residual Unit (K is 2 or 3 in \[1\]). F denotes the residual function, e.g., a stack of two 3×3 convolutional layers in \[1\]. The function f is the operation after element-wise addition, and in \[1\] f is ReLU. The function h is set as an identity mapping: h(xl) = xl.1

If f is also an identity mapping: xl+1 ≡yl, we can put Eqn.(2) into Eqn.(1) and obtain:

xl+1 = xl + F(xl, Wl). (3)

Recursively (xl+2 = xl+1 + F(xl+1, Wl+1) = xl + F(xl, Wl) + F(xl+1, Wl+1), etc.) we will have:

L−1 X

F(xi, Wi), (4)

xL = xl +

i=l

for any deeper unit L and any shallower unit l. Eqn.(4) exhibits some nice properties. (i) The feature xL of any deeper unit L can be represented as the feature xl of any shallower unit l plus a residual function in a form of PL−1

i=l F, indicating that the model is in a residual fashion between any units L and l. (ii) The feature xL = x0 + PL−1

i=0 F(xi, Wi), of any deep unit L, is the summation of the outputs of all preceding residual functions (plus x0). This is in contrast to a “plain network” where a feature xL is a series of matrix-vector products, say, QL−1

i=0 Wix0 (ignoring BN and ReLU).

Eqn.(4) also leads to nice backward propagation properties. Denoting the loss function as E, from the chain rule of backpropagation \[9\] we have:

L−1 X

!

∂E ∂xl

= ∂E

= ∂E

∂xL

1 + ∂ ∂xl

F(xi, Wi)

. (5)

∂xL

∂xl

∂xL

i=l

Eqn.(5) indicates that the gradient ∂E ∂xl can be decomposed into two additive terms: a term of ∂E ∂xL that propagates information directly without concerning any weight layers, and another term of ∂E ∂xL

PL−1

∂ ∂xl

that propagates through the weight layers. The additive term of ∂E ∂xL ensures that information is directly propagated back to any shallower unit l. Eqn.(5) also suggests that it

i=l F

1 It is noteworthy that there are Residual Units for increasing dimensions and reducing feature map sizes \[1\] in which h is not identity. In this case the following derivations do not hold strictly. But as there are only a very few such units (two on CIFAR and three on ImageNet, depending on image sizes \[1\]), we expect that they do not have the exponential impact as we present in Sec. 3. One may also think of our derivations as applied to all Residual Units within the same feature map size.

is unlikely for the gradient ∂E ∂xl to be canceled out for a mini-batch, because in general the term ∂ ∂xl

PL−1

i=l F cannot be always -1 for all samples in a mini-batch. This implies that the gradient of a layer does not vanish even when the weights are arbitrarily small.

---

Full document: [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md) · Page-level evidence: [paper-pages/06-identity-mappings-in-deep-residual-networks](../../paper-pages/06-identity-mappings-in-deep-residual-networks/index.md)
