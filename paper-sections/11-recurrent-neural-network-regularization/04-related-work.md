---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
section: 2 RELATED WORK
section_role: background
section_index: 4
pages: [1]
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "Dropout Srivastava (2013) is a recently introduced regularization method that has been very successful with feed-forward neural networks. While much…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 RELATED WORK

> Section 4 of 9 from [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · `background` · pages 1-1

Dropout Srivastava (2013) is a recently introduced regularization method that has been very successful with feed-forward neural networks. While much work has extended dropout in various ways Wang & Manning (2013); Wan et al. (2013), there has been relatively little research in applying it to RNNs. The only paper on this topic is by Bayer et al. (2013), who focuses on “marginalized dropout” Wang & Manning (2013), a noiseless deterministic approximation to standard dropout. Bayer et al. (2013) claim that conventional dropout does not work well with RNNs because the recurrence amplifies noise, which in turn hurts learning. In this work, we show that this problem can be fixed by applying dropout to a certain subset of the RNNs’ connections. As a result, RNNs can now also benefit from dropout.

Independently of our work, Pham et al. (2013) developed the very same RNN regularization method and applied it to handwriting recognition. We rediscovered this method and demonstrated strong empirical results over a wide range of problems. Other work that applied dropout to LSTMs is Pachitariu & Sahani (2013).

∗Work done while the author was in Google Brain.

There have been a number of architectural variants of the RNN that perform better on problems with long term dependencies Hochreiter & Schmidhuber (1997); Graves et al. (2009); Cho et al. (2014); Jaeger et al. (2007); Koutn´ık et al. (2014); Sundermeyer et al. (2012). In this work, we show how to correctly apply dropout to LSTMs, the most commonly-used RNN variant; this way of applying dropout is likely to work well with other RNN architectures as well.

In this paper, we consider the following tasks: language modeling, speech recognition, and machine translation. Language modeling is the first task where RNNs have achieved substantial success Mikolov et al. (2010; 2011); Pascanu et al. (2013). RNNs have also been successfully used for speech recognition Robinson et al. (1996); Graves et al. (2013) and have recently been applied to machine translation, where they are used for language modeling, re-ranking, or phrase modeling Devlin et al. (2014); Kalchbrenner & Blunsom (2013); Cho et al. (2014); Chow et al. (1987); Mikolov et al. (2013).

---

Full document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · Page-level evidence: [paper-pages/11-recurrent-neural-network-regularization](../../paper-pages/11-recurrent-neural-network-regularization/index.md)
