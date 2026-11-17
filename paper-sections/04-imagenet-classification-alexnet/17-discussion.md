---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 7 Discussion
section_role: results
section_index: 17
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "Our results show that a large, deep convolutional neural network is capable of achieving recordbreaking results on a highly challenging dataset using…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7 Discussion

> Section 17 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `results` · pages n/a

Our results show that a large, deep convolutional neural network is capable of achieving recordbreaking results on a highly challenging dataset using purely supervised learning. It is notable
that our network’s performance degrades if a single convolutional layer is removed. For example,
removing any of the middle layers results in a loss of about 2% for the top-1 performance of the
network. So the depth really is important for achieving our results.

To simplify our experiments, we did not use any unsupervised pre-training even though we expect
that it will help, especially if we obtain enough computational power to significantly increase the
size of the network without obtaining a corresponding increase in the amount of labeled data. Thus
far, our results have improved as we have made our network larger and trained it longer but we still
have many orders of magnitude to go in order to match the infero-temporal pathway of the human
visual system. Ultimately we would like to use very large and deep convolutional nets on video
sequences where the temporal structure provides very helpful information that is missing or far less
obvious in static images.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
