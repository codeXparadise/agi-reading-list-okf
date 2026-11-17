---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
source: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
paper_title: Multi-Scale Context Aggregation by Dilated Convolutions
sequence: 7
page: 1
pages: [1]
page_of: 13
topics: ["../../topics/convolutional-networks.md"]
description: "In this work, we develop a convolutional network module that aggregates multi-scale contextual information without losing resolution or analyzing…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 13 - Multi-Scale Context Aggregation by Dilated Convolutions

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [07 - Multi-Scale Context Aggregation by Dilated Convolutions](../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md)

In this work, we develop a convolutional network module that aggregates multi-scale contextual information without losing resolution or analyzing rescaled images. The module can be plugged into existing architectures at any resolution. Unlike pyramid-shaped architectures carried over from image classification, the presented context module is designed specifically for dense prediction. It is a rectangular prism of convolutional layers, with no pooling or subsampling. The module is based on dilated convolutions, which support exponential expansion of the receptive field without loss of resolution or coverage.

As part of this work, we also re-examine the performance of repurposed image classification networks on semantic segmentation. The performance of the core prediction modules can be unintentionally obscured by increasingly elaborate systems that involve structured prediction, multi-column architectures, multiple training datasets, and other augmentations. We therefore examine the leading adaptations of deep image classification networks in a controlled setting and remove vestigial components that hinder dense prediction performance. The result is an initial prediction module that is both simpler and more accurate than prior adaptations.

Using the simplified prediction module, we evaluate the presented context network through controlled experiments on the Pascal VOC 2012 dataset (Everingham et al., 2010). The experiments demonstrate that plugging the context module into existing semantic segmentation architectures reliably increases their accuracy.

## 2 DILATED CONVOLUTIONS

Let F : Z2 →R be a discrete function. Let Ωr = \[−r, r\]2 ∩Z2 and let k : Ωr →R be a discrete filter of size (2r + 1)2. The discrete convolution operator ∗can be defined as

X

(F ∗k)(p) =

F(s) k(t). (1)

s+t=p

We now generalize this operator. Let l be a dilation factor and let ∗l be defined as

X

(F ∗l k)(p) =

F(s) k(t). (2)

s+lt=p

We will refer to ∗l as a dilated convolution or an l-dilated convolution. The familiar discrete convolution ∗is simply the 1-dilated convolution.

The dilated convolution operator has been referred to in the past as “convolution with a dilated filter”. It plays a key role in the algorithme \`a trous, an algorithm for wavelet decomposition (Holschneider et al., 1987; Shensa, 1992).1 We use the term “dilated convolution” instead of “convolution with a dilated filter” to clarify that no “dilated filter” is constructed or represented. The convolution operator itself is modified to use the filter parameters in a different way. The dilated convolution operator can apply the same filter at different ranges using different dilation factors. Our definition reflects the proper implementation of the dilated convolution operator, which does not involve construction of dilated filters.

In recent work on convolutional networks for semantic segmentation, Long et al. (2015) analyzed filter dilation but chose not to use it. Chen et al. (2015a) used dilation to simplify the architecture of Long et al. (2015). In contrast, we develop a new convolutional network architecture that systematically uses dilated convolutions for multi-scale context aggregation.

Our architecture is motivated by the fact that dilated convolutions support exponentially expanding receptive fields without losing resolution or coverage. Let F0, F1, . . . , Fn−1 : Z2 →R be discrete functions and let k0, k1, . . . , kn−2 : Ω1 →R be discrete 3×3 filters. Consider applying the filters with exponentially increasing dilation:

Fi+1 = Fi ∗2i ki for i = 0, 1, . . . , n −2. (3)

Define the receptive field of an element p in Fi+1 as the set of elements in F0 that modify the value of Fi+1(p). Let the size of the receptive field of p in Fi+1 be the number of these elements. It is

1Some recent work mistakenly referred to the dilated convolution operator itself as the algorithme \`a trous. This is incorrect. The algorithme \`a trous applies a filter at multiple scales to produce a signal decomposition. The algorithm uses dilated convolutions, but is not equivalent to the dilated convolution operator itself.

---

first page · [next page](page-002.md) · [all pages](index.md)
