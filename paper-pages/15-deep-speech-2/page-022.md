---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 22
pages: [22]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "the deployed system. In order to accomplish this, we employ a neural network architecture with low deployment latency, reduce the precision of our…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 22 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 22 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

the deployed system. In order to accomplish this, we employ a neural network architecture with low deployment latency, reduce the precision of our network to 16-bit, built a batching scheduler to more efficiently evaluate RNNs, and find a simple heuristic to reduce beam search cost. The model has five forward-only recurrent layers with 2560 hidden units, one row convolution layer (Section 3.7) with τ = 19, and one fully-connected layer with 2560 hidden units. These techniques allow us to deploy Deep Speech at low cost to interactive applications.

## 8 Conclusion

End-to-end deep learning presents the exciting opportunity to improve speech recognition systems continually with increases in data and computation. Indeed, our results show that, compared to the previous incarnation, Deep Speech has significantly closed the gap in transcription performance with human workers by leveraging more data and larger models. Further, since the approach is highly generic, we’ve shown that it can quickly be applied to new languages. Creating high-performing recognizers for two very different languages, English and Mandarin, required essentially no expert knowledge of the languages. Finally, we have also shown that this approach can be efficiently deployed by batching user requests together on a GPU server, paving the way to deliver end-to-end Deep Learning technologies to users.

To achieve these results, we have explored various network architectures, finding several effective techniques: enhancements to numerical optimization through SortaGrad and Batch Normalization, evaluation of RNNs with larger strides with bigram outputs for English, searching through both bidirectional and unidirectional models. This exploration was powered by a well optimized, High Performance Computing inspired training system that allows us to train new, full-scale models on our large datasets in just a few days.

Overall, we believe our results confirm and exemplify the value of end-to-end Deep Learning methods for speech recognition in several settings. In those cases where our system is not already comparable to humans, the difference has fallen rapidly, largely because of application-agnostic Deep Learning techniques. We believe these techniques will continue to scale, and thus conclude that the vision of a single speech system that outperforms humans in most scenarios is imminently achievable.

## Acknowledgments

We are grateful to Baidu’s speech technology group for help with data preparation and useful conversations. We would like to thank Scott Gray, Amir Khosrowshahi and all of Nervana Systems for their excellent matrix multiply routines and useful discussions. We would also like to thank Natalia Gimelshein of NVIDIA for useful discussions and thoughts on implementing our fast deployment matrix multiply.

## References

\[1\] O. Abdel-Hamid, A.-r. Mohamed, H. Jang, and G. Penn. Applying convolutional neural networks con-

cepts to hybrid nn-hmm model for speech recognition. In ICASSP, 2012.

\[2\] D. Bahdanau, K. Cho, and Y. Bengio. Neural machine translation by jointly learning to align and translate.

In ICLR, 2015.

\[3\] D. Bahdanau, J. Chorowski, D. Serdyuk, P. Brakel, and Y. Bengio. End-to-end attention-based large

vocabulary speech recognition. abs/1508.04395, 2015. http://arxiv.org/abs/1508.04395.

\[4\] J. Barker, E. Marxer, Ricard Vincent, and S. Watanabe. The third ’CHiME’ speech separation and recogni-

tion challenge: Dataset, task and baselines. 2015. Submitted to IEEE 2015 Automatic Speech Recognition and Understanding Workshop (ASRU).

\[5\] S. Baxter. Modern GPU. https://nvlabs.github.io/moderngpu/.

\[6\] Y. Bengio, J. Louradour, R. Collobert, and J. Weston. Curriculum learning. In International Conference

on Machine Learning, 2009.

\[7\] H. Bourlard and N. Morgan. Connectionist Speech Recognition: A Hybrid Approach. Kluwer Academic

Publishers, Norwell, MA, 1993.

---

[previous page](page-021.md) · [next page](page-023.md) · [all pages](index.md)
