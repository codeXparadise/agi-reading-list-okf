---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
source: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
paper_title: The Unreasonable Effectiveness of Recurrent Neural Networks
sequence: 8
section: "Source Code\\"
section_role: other
section_index: 8
pages: []
topics: ["../../topics/recurrent-neural-networks.md"]
description: "I hope I’ve convinced you that training character-level language models is a very fun exercise. You can train your own models using the [char-rnn…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Source Code\

> Section 8 of 10 from [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · `other` · pages n/a

\
I hope I’ve convinced you that training character-level language models is a very fun exercise. You can train your own models using the [char-rnn code](https://github.com/karpathy/char-rnn) I released on Github (under MIT license). It takes one large text file and trains a character-level model that you can then sample from. Also, it helps if you have a GPU or otherwise training on CPU will be about a factor of 10x slower. In any case, if you end up training on some data and getting fun results let me know! And if you get lost in the Torch/Lua codebase remember that all it is is just a more fancy version of this [100-line gist](https://gist.github.com/karpathy/d4dee566867f8291f086).\
\
_Brief digression._ The code is written in [Torch 7](http://torch.ch/), which has recently become my favorite deep learning framework. I’ve only started working with Torch/LUA over the last few months and it hasn’t been easy (I spent a good amount of time digging through the raw Torch code on Github and asking questions on their _gitter_ to get things done), but once you get a hang of things it offers a lot of flexibility and speed. I’ve also worked with Caffe and Theano in the past and I believe Torch, while not perfect, gets its levels of abstraction and philosophy right better than others. In my view the desirable features of an effective framework are:\
\
1. CPU/GPU transparent Tensor library with a lot of functionality (slicing, array/matrix operations, etc. )\
2. An entirely separate code base in a scripting language (ideally Python) that operates over Tensors and implements all Deep Learning stuff (forward/backward, computation graphs, etc)\
3. It should be possible to easily share pretrained models (Caffe does this well, others don’t), and crucially\
4. NO compilation step (or at least not as currently done in Theano). The trend in Deep Learning is towards larger, more complex networks that are are time-unrolled in complex graphs. It is critical that these do not compile for a long time or development time greatly suffers. Second, by compiling one gives up interpretability and the ability to log/debug effectively. If there is an _option_ to compile the graph once it has been developed for efficiency in prod that’s fine.\
\

---

Full document: [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks](../../paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks/index.md)
