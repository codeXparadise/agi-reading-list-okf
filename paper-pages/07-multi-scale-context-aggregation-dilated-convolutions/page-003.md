---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
source: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
paper_title: Multi-Scale Context Aggregation by Dilated Convolutions
sequence: 7
page: 3
pages: [3]
page_of: 13
topics: ["../../topics/convolutional-networks.md"]
description: "Layer 1 2 3 4 5 6 7 8 Convolution 3×3 3×3 3×3 3×3 3×3 3×3 3×3 1×1 Dilation 1 1 2 4 8 16 1 1 Truncation Yes Yes Yes Yes Yes Yes Yes No Receptive field…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 13 - Multi-Scale Context Aggregation by Dilated Convolutions

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [07 - Multi-Scale Context Aggregation by Dilated Convolutions](../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md)

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

## 4 FRONT END

We implemented and trained a front-end prediction module that takes a color image as input and produces C = 21 feature maps as output. The front-end module follows the work of Long et al. (2015) and Chen et al. (2015a), but was implemented separately. We adapted the VGG-16 network (Simonyan & Zisserman, 2015) for dense prediction and removed the last two pooling and striding layers. Specifically, each of these pooling and striding layers was removed and convolutions in all subsequent layers were dilated by a factor of 2 for each pooling layer that was ablated. Thus convolutions in the final layers, which follow both ablated pooling layers, are dilated by a factor of 4. This enables initialization with the parameters of the original classification network, but produces higher-resolution output. The front-end module takes padded images as input and produces feature maps at resolution 64×64. We use reflection padding: the buffer zone is filled by reflecting the image about each edge.

Our front-end module is obtained by removing vestiges of the classification network that are counterproductive for dense prediction. Most significantly, we remove the last two pooling and striding layers entirely, whereas Long et al. kept them and Chen et al. replaced striding by dilation but kept the pooling layers. We found that simplifying the network by removing the pooling layers made it more accurate. We also remove the padding of the intermediate feature maps. Intermediate padding was used in the original classification network, but is neither necessary nor justified in dense prediction.

This simplified prediction module was trained on the Pascal VOC 2012 training set, augmented by the annotations created by Hariharan et al. (2011). We did not use images from the VOC-2012 validation set for training and therefore only used a subset of the annotations of Hariharan et al. (2011). Training was performed by stochastic gradient descent (SGD) with mini-batch size 14, learning rate 10−3, and momentum 0.9. The network was trained for 60K iterations.

We now compare the accuracy of our front-end module to the FCN-8s design of Long et al. (2015) and the DeepLab network of Chen et al. (2015a). For FCN-8s and DeepLab, we evaluate the public

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
