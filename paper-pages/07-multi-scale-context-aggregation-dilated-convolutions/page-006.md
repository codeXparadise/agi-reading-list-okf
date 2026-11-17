---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
source: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
paper_title: Multi-Scale Context Aggregation by Dilated Convolutions
sequence: 7
page: 6
pages: [6]
page_of: 13
topics: ["../../topics/convolutional-networks.md"]
description: "(a) Image (b) Front end (c) + Context (d) + CRF-RNN (e) Ground truth Figure 3: Semantic segmentations produced by different models. From left to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 6 of 13 - Multi-Scale Context Aggregation by Dilated Convolutions

> Page 6 of the source PDF, verbatim as extracted. Canonical document: [07 - Multi-Scale Context Aggregation by Dilated Convolutions](../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md)

![Figure, page 7](../../assets/07/fig-07-p07-27.jpg)

![Figure, page 7](../../assets/07/fig-07-p07-28.png)

![Figure, page 7](../../assets/07/fig-07-p07-29.png)

![Figure, page 7](../../assets/07/fig-07-p07-30.png)

![Figure, page 7](../../assets/07/fig-07-p07-31.png)

![Figure, page 7](../../assets/07/fig-07-p07-32.jpg)

![Figure, page 7](../../assets/07/fig-07-p07-33.png)

![Figure, page 7](../../assets/07/fig-07-p07-34.png)

![Figure, page 7](../../assets/07/fig-07-p07-35.png)

![Figure, page 7](../../assets/07/fig-07-p07-36.png)

![Figure, page 7](../../assets/07/fig-07-p07-37.jpg)

![Figure, page 7](../../assets/07/fig-07-p07-38.png)

![Figure, page 7](../../assets/07/fig-07-p07-39.png)

![Figure, page 7](../../assets/07/fig-07-p07-40.png)

![Figure, page 7](../../assets/07/fig-07-p07-41.png)

![Figure, page 7](../../assets/07/fig-07-p07-42.jpg)

![Figure, page 7](../../assets/07/fig-07-p07-43.png)

![Figure, page 7](../../assets/07/fig-07-p07-44.png)

![Figure, page 7](../../assets/07/fig-07-p07-45.png)

![Figure, page 7](../../assets/07/fig-07-p07-46.png)

![Figure, page 7](../../assets/07/fig-07-p07-47.jpg)

![Figure, page 7](../../assets/07/fig-07-p07-48.png)

![Figure, page 7](../../assets/07/fig-07-p07-49.png)

![Figure, page 7](../../assets/07/fig-07-p07-50.png)

![Figure, page 7](../../assets/07/fig-07-p07-51.png)

(a) Image

(b) Front end

(c) + Context

(d) + CRF-RNN

(e) Ground truth

Figure 3: Semantic segmentations produced by different models. From left to right: (a) input image, (b) prediction by the front-end module, (c) prediction by the large context network plugged into the front end, (d) prediction by the front end + context module + CRF-RNN, (e) ground truth.

mean IoU

mbike

bottle

person

horse

sheep

chair

table

train

plant

boat

bike

sofa

bird

aero

cow

bus

dog

cat

car

tv

Front end 86.3 38.2 76.8 66.8 63.2 87.3 78.7 82 33.7 76.7 53.5 73.7 76 76.6 83 51.9 77.8 44 79.9 66.3 69.8 Front + Basic 86.4 37.6 78.5 66.3 64.1 89.9 79.9 84.9 36.1 79.4 55.8 77.6 81.6 79 83.1 51.2 81.3 43.7 82.3 65.7 71.3 Front + Large 87.3 39.2 80.3 65.6 66.4 90.2 82.6 85.8 34.8 81.9 51.7 79 84.1 80.9 83.2 51.2 83.2 44.7 83.4 65.6 72.1 Front end + CRF 89.2 38.8 80 69.8 63.2 88.8 80 85.2 33.8 80.6 55.5 77.1 80.8 77.3 84.3 53.1 80.4 45 80.7 67.9 71.6 Front + Basic + CRF 89.1 38.7 81.4 67.4 65 91 81 86.7 37.5 81 57 79.6 83.6 79.9 84.6 52.7 83.3 44.3 82.6 67.2 72.7 Front + Large + CRF 89.6 39.9 82.7 66.7 67.5 91.1 83.3 87.4 36 83.3 52.5 80.7 85.7 81.8 84.4 52.6 84.4 45.3 83.7 66.7 73.3 Front end + RNN 88.8 38.1 80.8 69.1 65.6 89.9 79.6 85.7 36.3 83.6 57.3 77.9 83.2 77 84.6 54.7 82.1 46.9 80.9 66.7 72.5 Front + Basic + RNN 89 38.4 82.3 67.9 65.2 91.5 80.4 87.2 38.4 82.1 57.7 79.9 85 79.6 84.5 53.5 84 45 82.8 66.2 73.1 Front + Large + RNN 89.3 39.2 83.6 67.2 69 92.1 83.1 88 38.4 84.8 55.3 81.2 86.7 81.3 84.3 53.6 84.4 45.8 83.8 67 73.9

Table 3: Controlled evaluation of the effect of the context module on the accuracy of three different architectures for semantic segmentation. Experiments performed on the VOC-2012 validation set. Validation images were not used for training. Top: adding the context module to a semantic segmentation front end with no structured prediction (Long et al., 2015). The basic context module increases accuracy, the large module increases it by a larger margin. Middle: the context module increases accuracy when plugged into a front-end + dense CRF configuration (Chen et al., 2015a). Bottom: the context module increases accuracy when plugged into a front-end + CRF-RNN configuration (Zheng et al., 2015).

is both feasible and desirable. Our work shows that the dilated convolution operator is particularly suited to dense prediction due to its ability to expand the receptive field without losing resolution or coverage. We have utilized dilated convolutions to design a new network structure that reliably increases accuracy when plugged into existing semantic segmentation systems. As part of this work, we have also shown that the accuracy of existing convolutional networks for semantic segmentation can be increased by removing vestigial components that had been developed for image classification.

---

[previous page](page-005.md) · [next page](page-007.md) · [all pages](index.md)
