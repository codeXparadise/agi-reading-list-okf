---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
page: 9
pages: [9]
page_of: 11
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "6 CONCLUSION LSTMs have shown to be powerful models to represent variable length sequential data thanks to their ability to handle reasonably long…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 9 of 11 - Order Matters: Sequence to Sequence for Sets

> Page 9 of the source PDF, verbatim as extracted. Canonical document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md)

## 6 CONCLUSION

LSTMs have shown to be powerful models to represent variable length sequential data thanks to their ability to handle reasonably long term dependencies and the use of the chain rule to efficiently decompose joint distributions. On the other hand, some problems are expressed in terms of an unordered set of elements, either as input or as outputs; in some other cases, the data is represented by some structure that needs to be linearized to be fed to the LSTM, and there might be more than one way to do so. The first goal of this paper was to shed some light on these problems: indeed, we show that order matters to obtain the best performance. We then considered the case of unordered input data, for which we proposed the Read-Process-and-Write architecture, and the case of unordered output data, for which we proposed an efficient training algorithm that includes a search over possible orders during training and inference. We illustrated our proposed approaches for input and output sets through various experiments such as sorting, graphical models, language modeling, and parsing.

ACKNOWLEDGMENTS

We would like to thank Ilya Sutskever, Navdeep Jaitly, Rafal Jozefowicz, Quoc Le, Lukasz Kaiser, Geoffrey Hinton, Jeff Dean, Shane Gu and the Google Brain Team for useful discussions on this topic. We also thank the anonymous reviewers which helped improving our paper.

## REFERENCES

Bahdanau, D., Cho, K., and Bengio, Y. Neural machine translation by jointly learning to align and translate. In

Proc. ICLR, 2015a.

Bahdanau, D., Chorowski, J., Serdyuk, D., Brakel, P., and Bengio, Y. End-to-end attention-based large vocab-

ulary speech recognition. arXiv preprint arXiv:1508.04395, 2015b.

Bakir, G., Hofmann, T., Scholkopf, B., Smola, A. J., Taskar, B., and Vishwanathan, S.V.N. (eds.). Predicting

Structured Data. MIT Press, 2007.

Chan, W., Jaitly, N., Le, Q. V., and Vinyals, O. Listen, attend and spell. arXiv, abs/1508.01211, 2015. URL

http://arxiv.org/abs/1508.01211.

Cho, K., van Merrienboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., and Bengio, Y. Learning

phrase representations using RNN encoder-decoder for statistical machine translation. In Proc. EMNLP, 2014.

Donahue, J., Hendricks, L. A., Guadarrama, S., Rohrbach, M., Venugopalan, S., Saenko, K., and Darrell, T.

Long-term recurrent convolutional networks for visual recognition and description. In Proc. CVPR, 2015.

Graves, A. Supervised Sequence Labelling with Recurrent Neural Networks. Springer, 2012.

Graves, A., Wayne, G., and Danihelka, I. Neural turing machines. In arXiv preprint arXiv:1410.5401, 2014.

Hinton, G., Deng, L., Yu, D., Dahl, G., Mohamed, A., Jaitly, N., Senior, A., Vanhoucke, V., Nguyen, P., Sainath,

T. N., and Kingsbury, B. Deep neural networks for acoustic modeling in speech recognition. IEEE Signal Processing Magazine, 29:82–97, 2012.

Hochreiter, S. and Schmidhuber, J. Long short-term memory. Neural Computation, 9(8), 1997.

Ioffe, S. and Szegedy, C. Batch normalization: Accelerating deep network training by reducing internal covari-

ate shift. In Proceedings of the 32nd International Conference on Machine Learning, ICML, 2015.

Kalchbrenner, N. and Blunsom, P. Recurrent continuous translation models. In Proc. EMNLP, 2013.

Maas, A. L., Miller, S. D., O’Neil, T. M., and Ng, A. Y. Word-level acoustic modeling with convolutional

vector regression. In ICML 2012 Workshop on Representation Learning, 2012.

Mao, J., Xu, W., Yang, Y., Wang, J., Huang, Z., and Yuille, A. L. Deep captioning with multimodal recurrent

neural networks (m-RNN). In International Conference on Learning Representations, 2015.

Socher, R., Manning, C. D., and Ng, A. Y. Learning continuous phrase representations and syntactic parsing

with recursive neural networks. In Advances in Neural Information Processing Systems, 2010.

---

[previous page](page-008.md) · [next page](page-010.md) · [all pages](index.md)
