---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
source: ../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md
paper_title: Multi-Scale Context Aggregation by Dilated Convolutions
sequence: 7
page: 10
pages: [10]
page_of: 13
topics: ["../../topics/convolutional-networks.md"]
description: "APPENDIX A URBAN SCENE UNDERSTANDING In this appendix, we report experiments on three datasets for urban scene understanding: the CamVid dataset…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 10 of 13 - Multi-Scale Context Aggregation by Dilated Convolutions

> Page 10 of the source PDF, verbatim as extracted. Canonical document: [07 - Multi-Scale Context Aggregation by Dilated Convolutions](../../papers/07-multi-scale-context-aggregation-dilated-convolutions.md)

## APPENDIX A URBAN SCENE UNDERSTANDING

In this appendix, we report experiments on three datasets for urban scene understanding: the CamVid dataset (Brostow et al., 2009), the KITTI dataset (Geiger et al., 2013), and the new Cityscapes dataset (Cordts et al., 2016). As the accuracy measure we use the mean IoU (Everingham et al., 2010). We only train our model on the training set, even when a validation set is available. The results reported in this section do not use conditional random fields or other forms of structured prediction. They were obtained with convolutional networks that combine a front-end module and a context module, akin to the “Front + Basic” network evaluated in Table 3. The trained models can be found at https://github.com/fyu/dilation.

We now summarize the training procedure used for training the front-end module. This procedure applies to all datasets. Training is performed with stochastic gradient descent. Each mini-batch contains 8 crops from randomly sampled images. Each crop is of size 628×628 and is randomly sampled from a padded image. Images are padded using reflection padding. No padding is used in the intermediate layers. The learning rate is 10−4 and momentum is set to 0.99. The number of iterations depends on the number of images in the dataset and is reported for each dataset below.

The context modules used for these datasets are all derived from the “Basic” network, using the terminology of Table 1. The number of channels in each layer is the number of predicted classes C. (For example, C = 19 for the Cityscapes dataset.) Each layer in the context module is padded such that the input and response maps have the same size. The number of layers in the context module depends on the resolution of the images in the dataset. Joint training of the complete model, composed of the front-end and the context module, is summarized below for each dataset.

A.1 CAMVID

We use the split of Sturgess et al. (2009), which partitions the dataset into 367 training images, 100 validation images, and 233 test images. 11 semantic classes are used. The images are downsampled to 640×480.

The context module has 8 layers, akin to the model used for the Pascal VOC dataset in the main body of the paper. The overall training procedure is as follows. First, the front-end module is trained for 20K iterations. Then the complete model (front-end + context) is jointly trained by sampling crops of size 852 × 852 with batch size 1. The learning rate for joint training is set to 10−5 and the momentum is set to 0.9.

Results on the CamVid test set are reported in Table 5. We refer to our complete convolutional network (front-end + context) as Dilation8, since the context module has 8 layers. Our model outperforms the prior work. This model was used as the unary classifier in the recent work of Kundu et al. (2016).

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

ALE 73.4 70.2 91.1 64.2 24.4 91.1 29.1 31.0 13.6 72.4 28.6 53.6 SuperParsing 70.4 54.8 83.5 43.3 25.4 83.4 11.6 18.3 5.2 57.4 8.9 42.0 Liu and He 66.8 66.6 90.1 62.9 21.4 85.8 28.0 17.8 8.3 63.5 8.5 47.2 SegNet 68.7 52.0 87.0 58.5 13.4 86.2 25.3 17.9 16.0 60.5 24.8 46.4 DeepLab-LFOV 81.5 74.6 89.0 82.2 42.3 92.2 48.4 27.2 14.3 75.4 50.1 61.6 Dilation8 82.6 76.2 89.9 84.0 46.9 92.2 56.3 35.8 23.4 75.3 55.5 65.3

Table 5: Semantic segmentation results on the CamVid dataset. Our model (Dilation8) is compared to ALE (Ladicky et al., 2009), SuperParsing (Tighe & Lazebnik, 2013), Liu and He (Liu & He, 2015), SegNet (Badrinarayanan et al., 2015), and the DeepLab-LargeFOV model (Chen et al., 2015a). Our model outperforms the prior work.

---

[previous page](page-009.md) · [next page](page-011.md) · [all pages](index.md)
