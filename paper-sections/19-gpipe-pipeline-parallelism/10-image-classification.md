---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
section: 4 Image Classification
section_role: other
section_index: 10
pages: [4, 5]
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "As a proof of concept, we first used GPipe to scale AmoebaNet. We increased the number of channels in an AmoebaNet and scaled the input image size to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4 Image Classification

> Section 10 of 14 from [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · `other` · pages 4-5

As a proof of concept, we first used GPipe to scale AmoebaNet. We increased the number of channels in an AmoebaNet and scaled the input image size to 480 × 480. We trained this 557-millionparameter AmoebaNet-B(18, 512) on the ImageNet 2012 dataset, using the same hyper-parameters as described in \[12\]. The network was divided into 4 partitions. This single model achieves 84.4% top-1 and 97% top-5 validation accuracy with single-crop.

We further demonstrate the effectiveness of giant convolution networks on other image datasets through transfer learning \[22, 23\]. Specifically, we used the pre-trained ImageNet model to fine-tune on a variety of target datasets ranging from general to fine-grained classification. We changed the number of output units in the last softmax classification layer to the number of classes in the target dataset and initialized the new softmax layer randomly. All the other layers were initialized from

Table 4: Image classification accuracy using AmoebaNet-B (18, 512) first trained on ImageNet 2012 then fine-tuned on others. Please refer to the supplementary material for a detailed description of our training setup. Our fine-tuned results were averaged across 5 fine-tuning runs. Baseline results from Real et al. \[12\] and Cubuk et al. \[26\] were directly trained from scratch. \*Mahajan et al.’s model \[27\] achieved 85.4% top-1 accuracy but it was pretrained on non-public Instagram data. Ngiam et al. \[28\] achieved better results by pre-training with data from a private dataset (JFT-300M).

Dataset # Train # Test # Classes Accuracy (%) Previous Best (%)

ImageNet-2012 1,281,167 50,000 1000 84.4 83.9 \[12\] (85.4∗\[27\]) CIFAR-10 50,000 10,000 10 99.0 98.5 \[26\] CIFAR-100 50,000 10,000 100 91.3 89.3 \[26\] Stanford Cars 8,144 8,041 196 94.6 94.8∗\[26\] Oxford Pets 3,680 3,369 37 95.9 93.8∗\[29\] Food-101 75,750 25,250 101 93.0 90.4∗\[30\] FGVC Aircraft 6,667 3,333 100 92.7 92.9∗\[31\] Birdsnap 47,386 2,443 500 83.6 80.2∗\[32\]

ImageNet pre-training. Input images to the network during training were resized to 480 × 480, horizontally flipped randomly and augmented using cutout \[24\]. Training hyper-parameters were the same as those used for ImageNet (a detailed description of our training setup is provided in supplementary material). In Table 4, we report the average single-crop test accuracy over 5 fine-tuning runs for each dataset. Our giant models obtain competitive results on all target datasets. For example, CIFAR-10 error rate is reduced to 1% and CIFAR-100 error rate to 8.7%. These results corroborate the findings by Kornblith et al. \[25\], i.e., better ImageNet models transfer better.

---

Full document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · Page-level evidence: [paper-pages/19-gpipe-pipeline-parallelism](../../paper-pages/19-gpipe-pipeline-parallelism/index.md)
