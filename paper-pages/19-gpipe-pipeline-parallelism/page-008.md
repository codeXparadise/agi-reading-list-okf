---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
page: 8
pages: [8]
page_of: 11
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "computations across the batch (for example, BatchNorm uses statistics over the micro-batch during training, but accumulates mini-batch statistics for…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 8 of 11 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism

> Page 8 of the source PDF, verbatim as extracted. Canonical document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md)

computations across the batch (for example, BatchNorm uses statistics over the micro-batch during training, but accumulates mini-batch statistics for evaluation).

## 7 Conclusion

In this work, we introduce GPipe, a scalable model-parallelism library for training giant neural networks. We propose and implement a novel batch-splitting pipeline-parallelism algorithm that uses synchronous gradient updates, allowing model parallelism with high hardware utilization and training stability. We leverage GPipe to train large-scale convolutional and transformer-based models and demonstrate strong empirical results on both image classification and multilingual machine translation. We highlight three key attributes of the GPipe library: 1) Efficiency: Using a novel batch-splitting pipelining algorithm, GPipe achieves almost linear speedup with the number of devices. 2) Flexibility: GPipe supports any deep network that can be represented as a sequence of layers. 3) Reliability: GPipe utilizes synchronous gradient descent and guarantees consistent training regardless of the number of partitions.

## References

\[1\] Bryan McCann, James Bradbury, Caiming Xiong, and Richard Socher. Learned in translation:

Contextualized word vectors. CoRR, abs/1708.00107, 2017. \[2\] Matthew Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee,

and Luke Zettlemoyer. Deep contextualized word representations. In ACL, 2018. \[3\] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of

deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018. \[4\] Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language

models are unsupervised multitask learners. 2019. \[5\] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale

hierarchical image database. In CVPR. IEEE, 2009. \[6\] Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, and et al. Going deeper with

convolutions. In CVPR, pages 1–9, 2015. \[7\] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. Re-

thinking the inception architecture for computer vision. In CVPR, pages 2818–2826, 2016. \[8\] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Identity mappings in deep residual

networks. In European conference on computer vision, pages 630–645. Springer, 2016. \[9\] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and Kaiming He. Aggregated residual

transformations for deep neural networks. In CVPR, 2017. \[10\] Jie Hu, Li Shen, and Gang Sun. Squeeze-and-excitation networks. CVPR, 2018. \[11\] Barret Zoph, Vijay Vasudevan, Jonathon Shlens, and Quoc V Le. Learning transferable architectures for scalable image recognition. CVPR, 2018. \[12\] Esteban Real, Alok Aggarwal, Yanping Huang, and Quoc V Le. Regularized evolution for

image classifier architecture search. arXiv preprint arXiv:1802.01548, 2018. \[13\] Andreas Griewank and Andrea Walther. Algorithm 799: revolve: an implementation of check-

pointing for the reverse or adjoint mode of computational differentiation. ACM Transactions on Mathematical Software (TOMS), 26(1):19–45, 2000. \[14\] Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. Training deep nets with sublinear

memory cost. arXiv preprint arXiv:1604.06174, 2016. \[15\] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,

Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Neurips, pages 5998–6008, 2017. \[16\] Jonathan Shen, Patrick Nguyen, Yonghui Wu, Zhifeng Chen, Mia Xu Chen, Ye Jia, Anjuli

Kannan, Tara Sainath, Yuan Cao, Chung-Cheng Chiu, et al. Lingvo: a modular and scalable framework for sequence-to-sequence modeling. arXiv preprint arXiv:1902.08295, 2019.

---

[previous page](page-007.md) · [next page](page-009.md) · [all pages](index.md)
