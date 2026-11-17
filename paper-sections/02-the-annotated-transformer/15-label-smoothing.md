---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Label Smoothing
section_role: other
section_index: 15
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "During training, we employed label smoothing of value ϵls=0.1ϵls=0.1 [(cite)](https://arxiv.org/abs/1512.00567). This hurts perplexity, as the model…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Label Smoothing

> Section 15 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `other` · pages n/a

During training, we employed label smoothing of value ϵls=0.1ϵls=0.1 [(cite)](https://arxiv.org/abs/1512.00567). This hurts perplexity, as the model
learns to be more unsure, but improves accuracy and BLEU score.

> We implement label smoothing using the KL div loss. Instead of using a one-hot
> target distribution, we create a distribution that has `confidence` of the
> correct word and the rest of the `smoothing` mass distributed throughout the
> vocabulary.

```python
class LabelSmoothing(nn.Module):
    "Implement label smoothing."
    def __init__(self, size, padding_idx, smoothing=0.0):
        super(LabelSmoothing, self).__init__()
        self.criterion = nn.KLDivLoss(size_average=False)
        self.padding_idx = padding_idx
        self.confidence = 1.0 - smoothing
        self.smoothing = smoothing
        self.size = size
        self.true_dist = None

    def forward(self, x, target):
        assert x.size(1) == self.size
        true_dist = x.data.clone()
        true_dist.fill_(self.smoothing / (self.size - 2))
        true_dist.scatter_(1, target.data.unsqueeze(1), self.confidence)
        true_dist[:, self.padding_idx] = 0
        mask = torch.nonzero(target.data == self.padding_idx)
        if mask.dim() > 0:
            true_dist.index_fill_(0, mask.squeeze(), 0.0)
        self.true_dist = true_dist
        return self.criterion(x, Variable(true_dist, requires_grad=False))
```

> Here we can see an example of how the mass is distributed to the words based
> on confidence.

```python
## Example of label smoothing.
crit = LabelSmoothing(5, 0, 0.4)
predict = torch.FloatTensor([[0, 0.2, 0.7, 0.1, 0],\
                             [0, 0.2, 0.7, 0.1, 0],\
                             [0, 0.2, 0.7, 0.1, 0]])
v = crit(Variable(predict.log()),
         Variable(torch.LongTensor([2, 1, 0])))

## Show the target distributions expected by the system.
plt.imshow(crit.true_dist)
None
```

![png](https://nlp.seas.harvard.edu/images/the-annotated-transformer_74_0.png)

> Label smoothing actually starts to penalize the model if it gets very
> confident about a given choice.

```python
crit = LabelSmoothing(5, 0, 0.1)
def loss(x):
    d = x + 3 * 1
    predict = torch.FloatTensor([[0, x / d, 1 / d, 1 / d, 1 / d],\
                                 ])
    #print(predict)
    return crit(Variable(predict.log()),
                 Variable(torch.LongTensor([1]))).data[0]
plt.plot(np.arange(1, 100), [loss(x) for x in range(1, 100)])
None
```

![png](https://nlp.seas.harvard.edu/images/the-annotated-transformer_76_0.png)

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
