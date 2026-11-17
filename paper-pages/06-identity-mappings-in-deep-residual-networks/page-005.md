---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/06-identity-mappings-in-deep-residual-networks.md
source: ../../papers/06-identity-mappings-in-deep-residual-networks.md
paper_title: Identity Mappings in Deep Residual Networks
sequence: 6
page: 5
pages: [5]
page_of: 15
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "Table 1. Classification error on the CIFAR-10 test set using ResNet-110 [1], with diﬀerent types of shortcut connections applied to all Residual…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 15 - Identity Mappings in Deep Residual Networks

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md)

Table 1. Classification error on the CIFAR-10 test set using ResNet-110 \[1\], with diﬀerent types of shortcut connections applied to all Residual Units. We report “fail” when the test error is higher than 20%.

case Fig. on shortcut on F error (%) remark

original \[1\] Fig. 2(a) 1 1 6.61

0 1 fail This is a plain net

constant

scaling Fig. 2(b)

0.5 1 fail

0.5 0.5 12.35 frozen gating

1 −g(x) g(x) fail init bg=0 to −5

exclusive

gating Fig. 2(c)

1 −g(x) g(x) 8.70 init bg=-6

1 −g(x) g(x) 9.81 init bg=-7

gating Fig. 2(d) 1 −g(x) 1 12.86 init bg=0

shortcut-only

1 −g(x) 1 6.91 init bg=-6

1×1 conv shortcut Fig. 2(e) 1×1 conv 1 12.22

dropout shortcut Fig. 2(f) dropout 0.5 1 fail

Exclusive gating. Following the Highway Networks \[6,7\] that adopt a gating mechanism \[5\], we consider a gating function g(x) = σ(Wgx + bg) where a transform is represented by weights Wg and biases bg followed by the sigmoid function σ(x) = 1 1+e−x . In a convolutional network g(x) is realized by a 1×1 convolutional layer. The gating function modulates the signal by element-wise multiplication.

We investigate the “exclusive” gates as used in \[6,7\] — the F path is scaled by g(x) and the shortcut path is scaled by 1−g(x). See Fig 2(c). We find that the initialization of the biases bg is critical for training gated models, and following the guidelines2 in \[6,7\], we conduct hyper-parameter search on the initial value of bg in the range of 0 to -10 with a decrement step of -1 on the training set by crossvalidation. The best value (−6 here) is then used for training on the training set, leading to a test result of 8.70% (Table 1), which still lags far behind the ResNet-110 baseline. Fig 3(b) shows the training curves. Table 1 also reports the results of using other initialized values, noting that the exclusive gating network does not converge to a good solution when bg is not appropriately initialized.

The impact of the exclusive gating mechanism is two-fold. When 1 −g(x) approaches 1, the gated shortcut connections are closer to identity which helps information propagation; but in this case g(x) approaches 0 and suppresses the function F. To isolate the eﬀects of the gating functions on the shortcut path alone, we investigate a non-exclusive gating mechanism in the next.

Shortcut-only gating. In this case the function F is not scaled; only the shortcut path is gated by 1−g(x). See Fig 2(d). The initialized value of bg is still essential in this case. When the initialized bg is 0 (so initially the expectation of 1 −g(x) is 0.5), the network converges to a poor result of 12.86% (Table 1). This is also caused by higher training error (Fig 3(c)).

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
