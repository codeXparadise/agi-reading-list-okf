---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
source: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
paper_title: Multi-Scale Context Aggregation by Dilated Convolutions
sequence: 7
page: 11
pages: [11]
page_of: 13
topics: ["../../topics/convolutional-networks.md"]
description: "A.2 KITTI We use the training and validation split of Ros et al. (2015): 100 training images and 46 test images. The images were all collected from…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 11 of 13 - Multi-Scale Context Aggregation by Dilated Convolutions

> Page 11 of the source PDF, verbatim as extracted. Canonical document: [07 - Multi-Scale Context Aggregation by Dilated Convolutions](../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md)

A.2 KITTI

We use the training and validation split of Ros et al. (2015): 100 training images and 46 test images. The images were all collected from the KITTI visual odometry/SLAM dataset. The image resolution is 1226×370. Since the vertical resolution is small compared to the other datasets, we remove Layer 6 in Table 1. The resulting context module has 7 layers. The complete network (front-end + context) is referred to as Dilation7.

The front-end is trained for 10K iterations. Next, the front-end and the context module are trained jointly. For joint training, the crop size is 900×900 and momentum is set to 0.99, while the other parameters are the same as the ones used for the CamVid dataset. Joint training is performed for 20K iterations.

The results are shown in Table 6. As the table demonstrates, our model outperforms the prior work.

Pedestrian

mean IoU

Sidewalk

Bicyclist

Building

Fence

Road

Tree

Pole

Sign

Car

Sky

Ros et al. 71.8 69.5 84.4 51.2 4.2 72.4 1.7 32.4 2.6 45.3 3.2 39.9 DeepLab-LFOV 82.8 78.6 82.4 78.0 28.8 91.3 0.0 39.4 29.9 72.4 12.9 54.2 Dilation7 84.6 81.1 83 81.4 41.8 92.9 4.6 47.1 35.2 73.1 26.4 59.2

Table 6: Semantic segmentation results on the KITTI dataset. We compare our results to Ros et al. (2015) and to the DeepLab-LargeFOV model (Chen et al., 2015a). Our network (Dilation7) yields higher accuracy than the prior work.

A.3 CITYSCAPES

The Cityscapes dataset contains 2975 training images, 500 validation images, and 1525 test images (Cordts et al., 2016). Due to the high image resolution (2048×1024), we add two layers to the context network after Layer 6 in Table 1. These two layers have dilation 32 and 64, respectively. The total number of layers in the context module is 10 and we refer to the complete model (front-end + context) as Dilation10.

The Dilation10 network was trained in three stages. First, the front-end prediction module was trained for 40K iterations. Second, the context module was trained for 24K iterations on whole (uncropped) images, with learning rate 10−4, momentum 0.99, and batch size 100. Third, the complete model (front-end + context) was jointly trained for 60K iterations on halves of images (input size 1396×1396, including padding), with learning rate 10−5, momentum 0.99, and batch size 1.

Figure 5 visualizes the effect of the training stages on the performance of the model. Quantitative results are given in Tables 7 and 8.

The performance of Dilation10 was compared to prior work on the Cityscapes dataset by Cordts et al. (2016). In their evaluation, Dilation10 outperformed all prior models (Cordts et al., 2016). Dilation10 was also used as the unary classifier in the recent work of Kundu et al. (2016), which used structured prediction to increase accuracy further.

---

[previous page](page-010.md) · [next page](page-012.md) · [all pages](index.md)
