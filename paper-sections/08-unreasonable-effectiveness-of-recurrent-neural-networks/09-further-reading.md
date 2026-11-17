---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
source: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
paper_title: The Unreasonable Effectiveness of Recurrent Neural Networks
sequence: 8
section: "Further Reading\\"
section_role: other
section_index: 9
pages: []
topics: ["../../topics/recurrent-neural-networks.md"]
description: "Before the end of the post I also wanted to position RNNs in a wider context and provide a sketch of the current research directions. RNNs have…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Further Reading\

> Section 9 of 10 from [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · `other` · pages n/a

\
Before the end of the post I also wanted to position RNNs in a wider context and provide a sketch of the current research directions. RNNs have recently generated a significant amount of buzz and excitement in the field of Deep Learning. Similar to Convolutional Networks they have been around for decades but their full potential has only recently started to get widely recognized, in large part due to our growing computational resources. Here’s a brief sketch of a few recent developments (definitely not complete list, and a lot of this work draws from research back to 1990s, see related work sections):\
\
In the domain of **NLP/Speech**, RNNs [transcribe speech to text](http://www.jmlr.org/proceedings/papers/v32/graves14.pdf), perform [machine translation](http://arxiv.org/abs/1409.3215), [generate handwritten text](http://www.cs.toronto.edu/~graves/handwriting.html), and of course, they have been used as powerful language models [(Sutskever et al.)](http://www.cs.utoronto.ca/~ilya/pubs/2011/LANG-RNN.pdf) [(Graves)](http://arxiv.org/abs/1308.0850) [(Mikolov et al.)](http://www.rnnlm.org/) (both on the level of characters and words). Currently it seems that word-level models work better than character-level models, but this is surely a temporary thing.\
\
**Computer Vision.** RNNs are also quickly becoming pervasive in Computer Vision. For example, we’re seeing RNNs in frame-level [video classification](http://arxiv.org/abs/1411.4389), [image captioning](http://arxiv.org/abs/1411.4555) (also including my own work and many others), [video captioning](http://arxiv.org/abs/1505.00487) and very recently [visual question answering](http://arxiv.org/abs/1505.02074). My personal favorite RNNs in Computer Vision paper is [Recurrent Models of Visual Attention](http://arxiv.org/abs/1406.6247), both due to its high-level direction (sequential processing of images with glances) and the low-level modeling (REINFORCE learning rule that is a special case of policy gradient methods in Reinforcement Learning, which allows one to train models that perform non-differentiable computation (taking glances around the image in this case)). I’m confident that this type of hybrid model that consists of a blend of CNN for raw perception coupled with an RNN glance policy on top will become pervasive in perception, especially for more complex tasks that go beyond classifying some objects in plain view.\
\
**Inductive Reasoning, Memories and Attention.** Another extremely exciting direction of research is oriented towards addressing the limitations of vanilla recurrent networks. One problem is that RNNs are not inductive: They memorize sequences extremely well, but they don’t necessarily always show convincing signs of generalizing in the _correct_ way (I’ll provide pointers in a bit that make this more concrete). A second issue is they unnecessarily couple their representation size to the amount of computation per step. For instance, if you double the size of the hidden state vector you’d quadruple the amount of FLOPS at each step due to the matrix multiplication. Ideally, we’d like to maintain a huge representation/memory (e.g. containing all of Wikipedia or many intermediate state variables), while maintaining the ability to keep computation per time step fixed.\
\
The first convincing example of moving towards these directions was developed in DeepMind’s [Neural Turing Machines](http://arxiv.org/abs/1410.5401) paper. This paper sketched a path towards models that can perform read/write operations between large, external memory arrays and a smaller set of memory registers (think of these as our working memory) where the computation happens. Crucially, the NTM paper also featured very interesting memory addressing mechanisms that were implemented with a (soft, and fully-differentiable) attention model. The concept of **soft attention** has turned out to be a powerful modeling feature and was also featured in [Neural Machine Translation by Jointly Learning to Align and Translate](http://arxiv.org/abs/1409.0473) for Machine Translation and [Memory Networks](http://arxiv.org/abs/1503.08895) for (toy) Question Answering. In fact, I’d go as far as to say that\
\
> The concept of **attention** is the most interesting recent architectural innovation in neural networks.\
\
Now, I don’t want to dive into too many details but a soft attention scheme for memory addressing is convenient because it keeps the model fully-differentiable, but unfortunately one sacrifices efficiency because everything that can be attended to is attended to (but softly). Think of this as declaring a pointer in C that doesn’t point to a specific address but instead defines an entire distribution over all addresses in the entire memory, and dereferencing the pointer returns a weighted sum of the pointed content (that would be an expensive operation!). This has motivated multiple authors to swap soft attention models for **hard attention** where one samples a particular chunk of memory to attend to (e.g. a read/write action for some memory cell instead of reading/writing from all cells to some degree). This model is significantly more philosophically appealing, scalable and efficient, but unfortunately it is also non-differentiable. This then calls for use of techniques from the Reinforcement Learning literature (e.g. REINFORCE) where people are perfectly used to the concept of non-differentiable interactions. This is very much ongoing work but these hard attention models have been explored, for example, in [Inferring Algorithmic Patterns with Stack-Augmented Recurrent Nets](http://arxiv.org/abs/1503.01007), [Reinforcement Learning Neural Turing Machines](http://arxiv.org/abs/1505.00521), and [Show Attend and Tell](http://arxiv.org/abs/1502.03044).\
\
**People**. If you’d like to read up on RNNs I recommend theses from [Alex Graves](http://www.cs.toronto.edu/~graves/), [Ilya Sutskever](http://www.cs.toronto.edu/~ilya/) and [Tomas Mikolov](http://www.rnnlm.org/). For more about REINFORCE and more generally Reinforcement Learning and policy gradient methods (which REINFORCE is a special case of) [David Silver](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Home.html)’s class, or one of [Pieter Abbeel](http://www.cs.berkeley.edu/~pabbeel/)’s classes.\
\
**Code**. If you’d like to play with training RNNs I hear good things about [keras](https://github.com/fchollet/keras) or [passage](https://github.com/IndicoDataSolutions/Passage) for Theano, the [code](https://github.com/karpathy/char-rnn) released with this post for Torch, or [this gist](https://gist.github.com/karpathy/587454dc0146a6ae21fc) for raw numpy code I wrote a while ago that implements an efficient, batched LSTM forward and backward pass. You can also have a look at my numpy-based [NeuralTalk](https://github.com/karpathy/neuraltalk) which uses an RNN/LSTM to caption images, or maybe this [Caffe](http://jeffdonahue.com/lrcn/) implementation by Jeff Donahue.\
\

---

Full document: [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks](../../paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks/index.md)
