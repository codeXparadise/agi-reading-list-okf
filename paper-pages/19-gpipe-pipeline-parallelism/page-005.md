---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
page: 5
pages: [5]
page_of: 11
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "Table 4: Image classification accuracy using AmoebaNet-B (18, 512) first trained on ImageNet 2012 then fine-tuned on others. Please refer to the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 11 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md)

Table 4: Image classification accuracy using AmoebaNet-B (18, 512) first trained on ImageNet 2012 then fine-tuned on others. Please refer to the supplementary material for a detailed description of our training setup. Our fine-tuned results were averaged across 5 fine-tuning runs. Baseline results from Real et al. \[12\] and Cubuk et al. \[26\] were directly trained from scratch. \*Mahajan et al.’s model \[27\] achieved 85.4% top-1 accuracy but it was pretrained on non-public Instagram data. Ngiam et al. \[28\] achieved better results by pre-training with data from a private dataset (JFT-300M).

Dataset # Train # Test # Classes Accuracy (%) Previous Best (%)

ImageNet-2012 1,281,167 50,000 1000 84.4 83.9 \[12\] (85.4∗\[27\]) CIFAR-10 50,000 10,000 10 99.0 98.5 \[26\] CIFAR-100 50,000 10,000 100 91.3 89.3 \[26\] Stanford Cars 8,144 8,041 196 94.6 94.8∗\[26\] Oxford Pets 3,680 3,369 37 95.9 93.8∗\[29\] Food-101 75,750 25,250 101 93.0 90.4∗\[30\] FGVC Aircraft 6,667 3,333 100 92.7 92.9∗\[31\] Birdsnap 47,386 2,443 500 83.6 80.2∗\[32\]

ImageNet pre-training. Input images to the network during training were resized to 480 × 480, horizontally flipped randomly and augmented using cutout \[24\]. Training hyper-parameters were the same as those used for ImageNet (a detailed description of our training setup is provided in supplementary material). In Table 4, we report the average single-crop test accuracy over 5 fine-tuning runs for each dataset. Our giant models obtain competitive results on all target datasets. For example, CIFAR-10 error rate is reduced to 1% and CIFAR-100 error rate to 8.7%. These results corroborate the findings by Kornblith et al. \[25\], i.e., better ImageNet models transfer better.

## 5 Massive Massively Multilingual Machine Translation

Next, we demonstrate the flexibility of GPipe by scaling up models used for Natural Language Processing (NLP). Due to an abundance of available parallel corpora, neural machine translation (NMT) has become a benchmark task for any architecture used for NLP \[33, 15, 34, 35, 36\]. For this reason, we continue our GPipe experiments on a large-scale multilingual NMT task. We use a corpus of parallel documents over 102 languages and English, containing a total of 25 billion training examples, ranging from 104 to 109 per language \[37\]. This dataset creates a realistic test bed for experiments on scalability by spanning a diverse set of languages from data-scarce (low-resource) to data-rich (high-resource). For the first time in machine translation, we show that a large enough NMT model can learn the mapping between more than 100 language pairs simultaneously, while achieving better than bilingual model performance for all languages. This further brings out the importance of having efficient and flexible model-parallelism tools.

Our comparison is based on the performance of a single Transformer \[15\] trained on all language pairs in this corpus. We scale the architecture along two dimensions to stress the flexibility of GPipe: (i) along the depth by increasing the number of layers in the model and (ii) along the width by increasing the hidden dimension in the feed-forward layers and the number of attention heads (as well as # attention channels) in multi-head attention layers similar to Shazeer et al. \[34\]. Please refer to the supplementary material for a detailed description of our dataset, baselines, training configuration and optimization hyper-parameters.

We start with a standard 400M-parameter Transformer Big model, T(6, 8192, 16)1, as described in Chen et al. \[35\], with a vocabulary size of 64k. In Figure 3, we compare its performance against a 1.3B-parameter deep model, T(24, 8192, 16), a 1.3B-parameter wide model, T(12, 16384, 32), a 3Bparameter model, T(32, 16384, 32) and a 6B-parameter model, T(64, 16384, 32). All of the models are trained on all language pairs simultaneously, using temperature-based sampling as employed for multilingual BERT2 \[3\]. T(12, 16384, 32), T(24, 8192, 32), T(32, 16384, 32) and T(64, 16384, 32) are partitioned over 2, 4, 8 and 16 accelerators respectively.

1T(L, H, A) is a Transformer model with L encoder layers and L decoder layers, a feed-forward hidden dimension of H and A attention heads. The model dimension is fixed to 1024.

2https://github.com/google-research/bert/blob/master/multilingual.md

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
