---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 14
pages: [14]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Smaller models require more steps to train, while larger models require fewer Models between 0.6x and 2.2x the optimal size can be trained with a 20%…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 14 of 30 - Scaling Laws for Neural Language Models

> Page 14 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

![Figure, page 15](../../assets/03/fig-03-p15-10.png)

Smaller models require more steps to train, while larger models require fewer

Models between 0.6x and 2.2x the

optimal size can be trained with a

20% larger compute budget

Our framework does not capture early training dynamics

Figure 12 Left: Given a fixed compute budget, a particular model size is optimal, though somewhat larger or smaller models can be trained with minimal additional compute. Right: Models larger than the computeefficient size require fewer steps to train, allowing for potentially faster training if sufficient additional parallelism is possible. Note that this equation should not be trusted for very large models, as it is only valid in the power-law region of the learning curve, after initial transient effects.

![Figure, page 15](../../assets/03/fig-03-p15-11.png)

7

L = (Cmin/2.3 108) 0.050

6

L = (C/2.0 107) 0.057

5

Test Loss

4

3

2

10 8 10 6 10 4 10 2 100

Compute (PF-days), non-embedding

Figure 13 When adjusting performance to simulate training far below the critical batch size, we find a somewhat altered power law for L(Cmin) when compared with the fully empirical results. The conspicuous lump at 10−5 PF-days marks the transition from 1-layer to 2-layer networks; we exclude 1-layer networks in the power-law fits. It is the L(Cmin) trend that we expect to provide a reliable extrapolation for larger compute.

that in fact we could train more efficiently6 by training at the batch size Bcrit discussed in Section 5.1. Large and small values of the loss could have been achieved with fewer samples or fewer steps, respectively, and correcting for this inefficiency by standardizing to the critical batch size results in cleaner and more predictable trends.

In this section we will adjust for this oversight. More importantly, we will use the results of Section 5 to determine the optimal allocation of compute between model size N and the quantity of data processed during training, namely 2BcritSmin. We will determine this allocation both empirically and theoretically, by using the equation for L(N, Smin), and we will demonstrate that these methods agree.

## 6.1 Optimal Performance and Allocations

Let us first study the loss as a function of the optimally allocated compute from Equation (5.5). The result is plotted in Figure 13, along with a power-law fit. We see that as compared to the compute plot of Figure 1, the new fit with Cmin is somewhat improved.

Given L(Cmin), it is natural to ask for the optimal model size N(Cmin) that provides the minimal loss with a given quantity of training compute. The optimal model size is shown in Figure 14. We observe that N(Cmin)

6One might ask why we did not simply train at Bcrit in the first place. The reason is that it depends not only on the model but also on the target value of the loss we wish to achieve, and so is a moving target.

---

[previous page](page-013.md) · [next page](page-015.md) · [all pages](index.md)
