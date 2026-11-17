---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/06-identity-mappings-in-deep-residual-networks.md
source: ../../papers/06-identity-mappings-in-deep-residual-networks.md
paper_title: Identity Mappings in Deep Residual Networks
sequence: 6
page: 8
pages: [8]
page_of: 15
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "is the identity mapping. But in the above experiments f is ReLU as designed in [1], so Eqn.(5) and (8) are approximate in the above experiments. Next…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 8 of 15 - Identity Mappings in Deep Residual Networks

> Page 8 of the source PDF, verbatim as extracted. Canonical document: [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md)

is the identity mapping. But in the above experiments f is ReLU as designed in \[1\], so Eqn.(5) and (8) are approximate in the above experiments. Next we investigate the impact of f.

We want to make f an identity mapping, which is done by re-arranging the activation functions (ReLU and/or BN). The original Residual Unit in \[1\] has a shape in Fig. 4(a) — BN is used after each weight layer, and ReLU is adopted after BN except that the last ReLU in a Residual Unit is after elementwise addition (f = ReLU). Fig. 4(b-e) show the alternatives we investigated, explained as following.

## 4.1 Experiments on Activation

In this section we experiment with ResNet-110 and a 164-layer Bottleneck \[1\] architecture (denoted as ResNet-164). A bottleneck Residual Unit consist of a 1×1 layer for reducing dimension, a 3×3 layer, and a 1×1 layer for restoring dimension. As designed in \[1\], its computational complexity is similar to the two-3×3 Residual Unit. More details are in the appendix. The baseline ResNet164 has a competitive result of 5.93% on CIFAR-10 (Table 2). BN after addition. Before turning f into an identity mapping, we go the opposite way by adopting BN after addition (Fig. 4(b)). In this case f involves BN and ReLU. The results become considerably worse than the baseline (Table 2). Unlike the original design, now the BN layer alters the signal that passes through the shortcut and impedes information propagation, as reflected by the diﬃculties on reducing training loss at the beginning of training (Fib. 6 left).

ReLU before addition. A na¨ıve choice of making f into an identity mapping is to move the ReLU before addition (Fig. 4(c)). However, this leads to a non-negative output from the transform F, while intuitively a “residual” function should take values in (−∞, +∞). As a result, the forward propagated signal is monotonically increasing. This may impact the representational ability, and the result is worse (7.84%, Table 2) than the baseline. We expect to have a residual function taking values in (−∞, +∞). This condition is satisfied by other Residual Units including the following ones.

Post-activation or pre-activation? In the original design (Eqn.(1) and Eqn.(2)), the activation xl+1 = f(yl) aﬀects both paths in the next Residual Unit: yl+1 = f(yl) + F(f(yl), Wl+1). Next we develop an asymmetric form where an activation ˆf only aﬀects the F path: yl+1 = yl + F( ˆf(yl), Wl+1), for any l (Fig. 5 (a) to (b)). By renaming the notations, we have the following form:

xl+1 = xl + F( ˆf(xl), Wl), . (9)

It is easy to see that Eqn.(9) is similar to Eqn.(4), and can enable a backward formulation similar to Eqn.(5). For this new Residual Unit as in Eqn.(9), the new after-addition activation becomes an identity mapping. This design means that if a new after-addition activation ˆf is asymmetrically adopted, it is equivalent to recasting ˆf as the pre-activation of the next Residual Unit. This is illustrated in Fig. 5.

---

[previous page](page-007.md) · [next page](page-009.md) · [all pages](index.md)
