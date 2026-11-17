---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
source: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
paper_title: Multi-Scale Context Aggregation by Dilated Convolutions
sequence: 7
section: 3 MULTI-SCALE CONTEXT AGGREGATION
section_role: other
section_index: 5
pages: [2, 3]
topics: ["../../topics/convolutional-networks.md"]
description: "The context module is designed to increase the performance of dense prediction architectures by aggregating multi-scale contextual information. The…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 MULTI-SCALE CONTEXT AGGREGATION

> Section 5 of 11 from [07 - Multi-Scale Context Aggregation by Dilated Convolutions](../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md) · `other` · pages 2-3

The context module is designed to increase the performance of dense prediction architectures by aggregating multi-scale contextual information. The module takes C feature maps as input and produces C feature maps as output. The input and output have the same form, thus the module can be plugged into existing dense prediction architectures.

We begin by describing a basic form of the context module. In this basic form, each layer has C channels. The representation in each layer is the same and could be used to directly obtain a dense per-class prediction, although the feature maps are not normalized and no loss is defined inside the module. Intuitively, the module can increase the accuracy of the feature maps by passing them through multiple layers that expose contextual information.

The basic context module has 7 layers that apply 3×3 convolutions with different dilation factors. The dilations are 1, 1, 2, 4, 8, 16, and 1. Each convolution operates on all layers: strictly speaking, these are 3×3×C convolutions with dilation in the first two dimensions. Each of these convolutions is followed by a pointwise truncation max(·, 0). A final layer performs 1×1×C convolutions and produces the output of the module. The architecture is summarized in Table 1. Note that the frontend module that provides the input to the context network in our experiments produces feature maps at 64×64 resolution. We therefore stop the exponential expansion of the receptive field after layer 6.

Our initial attempts to train the context module failed to yield an improvement in prediction accuracy. Experiments revealed that standard initialization procedures do not readily support the training of the module. Convolutional networks are commonly initialized using samples from random distributions (Glorot & Bengio, 2010; Krizhevsky et al., 2012; Simonyan & Zisserman, 2015). However, we found that random initialization schemes were not effective for the context module. We found an alternative initialization with clear semantics to be much more effective:

kb(t, a) = 1\[t=0\]1\[a=b\], (4)

where a is the index of the input feature map and b is the index of the output map. This is a form of identity initialization, which has recently been advocated for recurrent networks (Le et al., 2015). This initialization sets all filters such that each layer simply passes the input directly to the next. A natural concern is that this initialization could put the network in a mode where backpropagation cannot significantly improve the default behavior of simply passing information through. However, experiments indicate that this is not the case. Backpropagation reliably harvests the contextual information provided by the network to increase the accuracy of the processed maps.

Layer 1 2 3 4 5 6 7 8 Convolution 3×3 3×3 3×3 3×3 3×3 3×3 3×3 1×1 Dilation 1 1 2 4 8 16 1 1 Truncation Yes Yes Yes Yes Yes Yes Yes No Receptive field 3×3 5×5 9×9 17×17 33×33 65×65 67×67 67×67 Output channels Basic C C C C C C C C Large 2C 2C 4C 8C 16C 32C 32C C

Table 1: Context network architecture. The network processes C feature maps by aggregating contextual information at progressively increasing scales without losing resolution.

This completes the presentation of the basic context network. Our experiments show that even this basic module can increase dense prediction accuracy both quantitatively and qualitatively. This is particularly notable given the small number of parameters in the network: ≈64C2 parameters in total.

We have also trained a larger context network that uses a larger number of feature maps in the deeper layers. The number of maps in the large network is summarized in Table 1. We generalize the initialization scheme to account for the difference in the number of feature maps in different layers. Let ci and ci+1 be the number of feature maps in two consecutive layers. Assume that C divides both ci and ci+1. The initialization is

 bC

  

aC

C ci+1

t = 0 and

=

ci

ci+1

kb(t, a) =

(5)

 

ε otherwise

Here ε ∼N(0, σ2) and σ ≪C/ci+1. The use of random noise breaks ties among feature maps with a common predecessor.

---

Full document: [07 - Multi-Scale Context Aggregation by Dilated Convolutions](../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md) · Page-level evidence: [paper-pages/07-multi-scale-context-aggregation-dilated-convolutions](../../paper-pages/07-multi-scale-context-aggregation-dilated-convolutions/index.md)
