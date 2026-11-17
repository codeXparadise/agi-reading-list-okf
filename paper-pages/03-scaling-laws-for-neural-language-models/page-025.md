---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 25
pages: [25]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "3.90 0.0010 3.85 0.0008 Learning Rate 0.0006 3.80 Loss 0.0004 3.75 0.0002 3.70 0.0000 3.65 0 50000 100000 150000 200000 250000 Step 50 100 150 200…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 25 of 30 - Scaling Laws for Neural Language Models

> Page 25 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

![Figure, page 26](../../assets/03/fig-03-p26-20.png)

3.90

0.0010

3.85

0.0008

Learning Rate

0.0006

3.80

Loss

0.0004

3.75

0.0002

3.70

0.0000

3.65

0 50000 100000 150000 200000 250000 Step

50 100 150 200 250 LR Summed Over Steps

Figure 22 We test a variety of learning rate schedules including cosine decay, linear decay, as well as other faster/slower decays schedules on a 3 million parameter model, shown on the left. For these experiments we do not decay to zero, since we find that this tends to give a fixed improvement close to the end of training. We find that, as long as the learning rate is not too small and does not decay too quickly, performance does not depend strongly on learning rate. Run-to-run variation is at the level of 0.05 in the loss, so averaging multiple runs is necessary to validate performance changes smaller than this level.

![Figure, page 26](../../assets/03/fig-03-p26-21.png)

6

L = (N/8.8 1013) 0.076

Test Loss (at convergence)

L = 0.25log(N/7.1 1012)

5

4

3

2

104 105 106 107 108 109

Parameters (non-embedding)

Figure 23 The trend for performance as a function of parameter count, L(N), is fit better by a power law than by other functions such as a logarithm at a qualitative level.

schedules appear to be statistical noise, and provide a rough gauge for the scale of variation between different training runs. Experiments on larger models suggest that the variation in the final test loss between different random seeds is roughly constant in magnitude for different model sizes.

We found that larger models require a smaller learning rate to prevent divergence, while smaller models can tolerate a larger learning rate. To implement this, the following rule of thumb was used for most runs:

LR(N) ≈0.003239 + −0.0001395 log(N) (D.1)

We expect that this formula could be improved. There may be a dependence on network width, likely set by the initialization scale. The formula also breaks down for N > 1010 parameters. Nevertheless, we found that it works sufficiently well for the models we considered.

## D.7 Fit Details and Power Law Quality

We experimented with a number of functional forms for the fits to L(N), L(C), and L(D); the power-law fits were qualitatively much more accurate than other functions such as logarithms (see Figure 23).

For L(C), we do not include small models with only 1 layer in the fit, as the transition from 1 to 2 layers causes a noticable lump in the data. For L(N) we also do not include very small models with only 1 layer in the fit, and we exclude the largest models that have not trained fully to convergence. Fit parameters change marginally if we do include them, and the trend extrapolates well in both directions regardless.

## D.8 Generalization and Architecture

In figure 24 we show that generalization to other data distributions does not depend on network depth when we hold the total parameter count fixed. It seems to depend only on the performance on the training distribution.

---

[previous page](page-024.md) · [next page](page-026.md) · [all pages](index.md)
