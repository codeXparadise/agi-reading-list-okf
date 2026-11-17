---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/05-deep-residual-learning-resnet.md
source: ../../papers/05-deep-residual-learning-resnet.md
paper_title: Deep Residual Learning for Image Recognition
sequence: 5
page: 1
pages: [1]
page_of: 12
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "ImageNet test set, and won the 1st place in the ILSVRC 2015 classification competition. The extremely deep representations also have excellent…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 12 - Deep Residual Learning for Image Recognition

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md)

ImageNet test set, and won the 1st place in the ILSVRC 2015 classification competition. The extremely deep representations also have excellent generalization performance on other recognition tasks, and lead us to further win the 1st places on: ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation in ILSVRC & COCO 2015 competitions. This strong evidence shows that the residual learning principle is generic, and we expect that it is applicable in other vision and non-vision problems.

## x

weight layer

relu

F(x) x

weight layer

identity

relu F(x)+x

Figure 2. Residual learning: a building block.

are comparably good or better than the constructed solution (or unable to do so in feasible time).

## 2. Related Work

In this paper, we address the degradation problem by introducing a deep residual learning framework. Instead of hoping each few stacked layers directly fit a desired underlying mapping, we explicitly let these layers fit a residual mapping. Formally, denoting the desired underlying mapping as H(x), we let the stacked nonlinear layers fit another mapping of F(x) := H(x)−x. The original mapping is recast into F(x)+x. We hypothesize that it is easier to optimize the residual mapping than to optimize the original, unreferenced mapping. To the extreme, if an identity mapping were optimal, it would be easier to push the residual to zero than to fit an identity mapping by a stack of nonlinear layers.

Residual Representations. In image recognition, VLAD \[18\] is a representation that encodes by the residual vectors with respect to a dictionary, and Fisher Vector \[30\] can be formulated as a probabilistic version \[18\] of VLAD. Both of them are powerful shallow representations for image retrieval and classification \[4, 48\]. For vector quantization, encoding residual vectors \[17\] is shown to be more effective than encoding original vectors.

In low-level vision and computer graphics, for solving Partial Differential Equations (PDEs), the widely used Multigrid method \[3\] reformulates the system as subproblems at multiple scales, where each subproblem is responsible for the residual solution between a coarser and a finer scale. An alternative to Multigrid is hierarchical basis preconditioning \[45, 46\], which relies on variables that represent residual vectors between two scales. It has been shown \[3, 45, 46\] that these solvers converge much faster than standard solvers that are unaware of the residual nature of the solutions. These methods suggest that a good reformulation or preconditioning can simplify the optimization.

The formulation of F(x)+x can be realized by feedforward neural networks with “shortcut connections” (Fig. 2). Shortcut connections \[2, 34, 49\] are those skipping one or more layers. In our case, the shortcut connections simply perform identity mapping, and their outputs are added to the outputs of the stacked layers (Fig. 2). Identity shortcut connections add neither extra parameter nor computational complexity. The entire network can still be trained end-to-end by SGD with backpropagation, and can be easily implemented using common libraries (e.g., Caffe \[19\]) without modifying the solvers.

Shortcut Connections. Practices and theories that lead to shortcut connections \[2, 34, 49\] have been studied for a long time. An early practice of training multi-layer perceptrons (MLPs) is to add a linear layer connected from the network input to the output \[34, 49\]. In \[44, 24\], a few intermediate layers are directly connected to auxiliary classifiers for addressing vanishing/exploding gradients. The papers of \[39, 38, 31, 47\] propose methods for centering layer responses, gradients, and propagated errors, implemented by shortcut connections. In \[44\], an “inception” layer is composed of a shortcut branch and a few deeper branches.

We present comprehensive experiments on ImageNet \[36\] to show the degradation problem and evaluate our method. We show that: 1) Our extremely deep residual nets are easy to optimize, but the counterpart “plain” nets (that simply stack layers) exhibit higher training error when the depth increases; 2) Our deep residual nets can easily enjoy accuracy gains from greatly increased depth, producing results substantially better than previous networks.

Similar phenomena are also shown on the CIFAR-10 set \[20\], suggesting that the optimization difficulties and the effects of our method are not just akin to a particular dataset. We present successfully trained models on this dataset with over 100 layers, and explore models with over 1000 layers.

Concurrent with our work, “highway networks” \[42, 43\] present shortcut connections with gating functions \[15\]. These gates are data-dependent and have parameters, in contrast to our identity shortcuts that are parameter-free. When a gated shortcut is “closed” (approaching zero), the layers in highway networks represent non-residual functions. On the contrary, our formulation always learns residual functions; our identity shortcuts are never closed, and all information is always passed through, with additional residual functions to be learned. In addition, high-

On the ImageNet classification dataset \[36\], we obtain excellent results by extremely deep residual nets. Our 152layer residual net is the deepest network ever presented on ImageNet, while still having lower complexity than VGG nets \[41\]. Our ensemble has 3.57% top-5 error on the

2

---

first page · [next page](page-002.md) · [all pages](index.md)
