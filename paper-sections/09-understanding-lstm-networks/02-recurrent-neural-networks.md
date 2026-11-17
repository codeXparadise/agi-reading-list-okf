---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/09-understanding-lstm-networks.md
source: ../../papers/09-understanding-lstm-networks.md
paper_title: Understanding LSTM Networks
sequence: 9
section: Recurrent Neural Networks
section_role: other
section_index: 2
pages: []
topics: ["../../topics/long-short-term-memory.md", "../../topics/recurrent-neural-networks.md"]
description: "Humans don’t start their thinking from scratch every second. As you read this essay, you understand each word based on your understanding of previous…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Recurrent Neural Networks

> Section 2 of 10 from [09 - Understanding LSTM Networks](../../papers/09-understanding-lstm-networks.md) · `other` · pages n/a

Humans don’t start their thinking from scratch every second. As you read this essay, you understand each word based on your understanding of previous words. You don’t throw everything away and start thinking from scratch again. Your thoughts have persistence.

Traditional neural networks can’t do this, and it seems like a major shortcoming. For example, imagine you want to classify what kind of event is happening at every point in a movie. It’s unclear how a traditional neural network could use its reasoning about previous events in the film to inform later ones.

Recurrent neural networks address this issue. They are networks with loops in them, allowing information to persist.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-rolled.png)

**Recurrent Neural Networks have loops.**

In the above diagram, a chunk of neural network, AA, looks at some input xtxt and outputs a value htht. A loop allows information to be passed from one step of the network to the next.

These loops make recurrent neural networks seem kind of mysterious. However, if you think a bit more, it turns out that they aren’t all that different than a normal neural network. A recurrent neural network can be thought of as multiple copies of the same network, each passing a message to a successor. Consider what happens if we unroll the loop:

![An unrolled recurrent neural network.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png)

**An unrolled recurrent neural network.**

This chain-like nature reveals that recurrent neural networks are intimately related to sequences and lists. They’re the natural architecture of neural network to use for such data.

And they certainly are used! In the last few years, there have been incredible success applying RNNs to a variety of problems: speech recognition, language modeling, translation, image captioning… The list goes on. I’ll leave discussion of the amazing feats one can achieve with RNNs to Andrej Karpathy’s excellent blog post, [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). But they really are pretty amazing.

Essential to these successes is the use of “LSTMs,” a very special kind of recurrent neural network which works, for many tasks, much much better than the standard version. Almost all exciting results based on recurrent neural networks are achieved with them. It’s these LSTMs that this essay will explore.

---

Full document: [09 - Understanding LSTM Networks](../../papers/09-understanding-lstm-networks.md) · Page-level evidence: [paper-pages/09-understanding-lstm-networks](../../paper-pages/09-understanding-lstm-networks/index.md)
