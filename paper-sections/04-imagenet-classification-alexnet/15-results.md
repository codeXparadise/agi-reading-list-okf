---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 6 Results
section_role: results
section_index: 15
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "Our results on ILSVRC-2010 are summarized in Table 1. Our network achieves top-1 and top-5 test set error rates of 37.5% and 17.0%5. The best…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6 Results

> Section 15 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `results` · pages n/a

```
Our results on ILSVRC-2010 are summarized in Table 1. Our network achieves top-1 and top-5
test set error rates of 37.5% and 17.0%5. The best performance achieved during the ILSVRC-
2010 competition was 47.1% and 28.2% with an approach that averages the predictions produced
from six sparse-coding models trained on different features [2], and since then the best pub-
lished results are 45.7% and 25.7% with an approach that averages the predictions of two classi-
fiers trained on Fisher Vectors (FVs) computed from two types of densely-sampled features [24].
```

We also entered our model in the ILSVRC-2012 competition and report our results in Table 2. Since the
ILSVRC-2012 test set labels are not publicly available,
we cannot report test error rates for all the models that
we tried. In the remainder of this paragraph, we use
validation and test error rates interchangeably because
in our experience they do not differ by more than 0.1%
(see Table 2). The CNN described in this paper achieves
a top-5 error rate of 18.2%. Averaging the predictions

| Model | Top-1 | Top-5 |
| --- | --- | --- |
| Sparse coding [2] | 47.1% | 28.2% |
| SIFT + FVs [24] | 45.7% | 25.7% |
| CNN | 37.5% | 17.0% |

of five similar CNNs gives an error rate of 16.4%. Training one CNN, with an extra sixth convolutional layer over the last pooling layer, to classify the entire ImageNet Fall 2011 release
(15M images, 22K categories), and then “fine-tuning” it on ILSVRC-2012 gives an error rate of
16.6%. Averaging the predictions of two CNNs that were pre-trained on the entire Fall 2011 release with the aforementioned five CNNs gives an error rate of **15.3%.** The second-best contest entry achieved an error rate of 26.2% with an approach that averages the predictions of several classifiers trained on FVs computed from different types of densely-sampled features [7].

Table 1: Comparison of results on ILSVRC-
2010 test set. In *italics* are best results
achieved by others.

Finally, we also report our error
rates on the Fall 2009 version of
ImageNet with 10,184 categories
and 8.9 million images. On this
dataset we follow the convention
in the literature of using half of
the images for training and half
for testing. Since there is no established test set, our split necessarily differs from the splits used
by previous authors, but this does
not affect the results appreciably.
Our top-1 and top-5 error rates
on this dataset are **67.4%** and

| Model | Top-1 (val) | Top-5 (val) | Top-5 (test) |
| --- | --- | --- | --- |
| SIFT + FVs [7] | — | — | 26.2% |
| 1 CNN | 40.7% | 18.2% | — |
| 5 CNNs | 38.1% | 16.4% | 16.4% |
| 1 CNN* | 39.0% | 16.6% | — |
| 7 CNNs* | 36.7% | 15.4% | 15.3% |

Table 2: Comparison of error rates on ILSVRC-2012 validation and
test sets. In *italics* are best results achieved by others. Models with an
asterisk* were “pre-trained” to classify the entire ImageNet 2011 Fall
release. See Section 6 for details.

**40.9%,** attained by the net described above but with an additional, sixth convolutional layer over the
last pooling layer. The best published results on this dataset are 78.1% and 60.9% [19].

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
