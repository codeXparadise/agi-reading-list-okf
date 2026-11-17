---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: 7 Related Work
section_role: background
section_index: 24
pages: [17]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Power laws can arise from a wide variety of sources [THK18]. Power-law scalings with model and dataset size in density estimation [Was06] and in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7 Related Work

> Section 24 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `background` · pages 17-17

Power laws can arise from a wide variety of sources \[THK18\]. Power-law scalings with model and dataset size in density estimation \[Was06\] and in random forest models \[Bia12\] may be connected with our results. These models suggest that power-law exponents may have a very rough interpretation as the inverse of the number of relevant features in the data.

Some early \[BB01, Goo01\] work found power-law scalings between performance and dataset size. More recent work \[HNA+17, HAD19\] also investigated scaling between model size and data size; their work is perhaps the closest to ours in the literature8. Note, however, that \[HNA+17\] found super-linear scaling of dataset size with model size, whereas we find a sub-linear scaling. There are some parallels between our findings on optimal allocation of compute and \[Kom19\], including power-law learning curves. EfficientNets \[TL19\] also appear to obey an approximate power-law relation between accuracy and model size. Very recent work \[RRBS19b\] studies scaling with both dataset size and model size for a variety of datasets, and fits an ansatz similar to ours.

EfficientNet \[TL19\] advocates scaling depth and width exponentially (with different coefficients) for optimal performance of image models, resulting in a power-law scaling of width as a function of depth. We find that for language models this power should be roughly one when scaling up (as width/depth should remain fixed). But more importantly, we find that the precise architectural hyperparameters are unimportant compared to the overall scale of the language model. In \[VWB16\] it was argued that deep models can function as ensembles of shallower models, which could potentially explain this finding. Earlier work \[ZK16\] has compared width and depth, and found that wide ResNets can outperform deep ResNets on image classification. Some studies fix computation per data example, which tends to scale in proportion to the number of model parameters, whereas we investigate scaling with both model size and the quantity of training computation.

Various works \[AS17, BHMM18\] have investigated generalization in highly overparameterized models, finding a “jamming transition” \[GJS+19\] when the model size reaches the dataset size (this may require training many orders of magnitude beyond typical practice, and in particular does not use early stopping). We do not observe such a transition, and find that the necessary training data scales sublinearly in the model size. Expansions in the model size, particularly at large width \[JGH18, LXS+19\], may provide a useful framework for thinking about some of our scaling relations. Our results on optimization, such as the shape of learning curves, can likely be explained using a noisy quadratic model, which can provide quite accurate predictions \[ZLN+19\] in realistic settings. Making this connection quantitative will require a characterization of the Hessian spectrum \[Pap18, GKX19, GARD18\].

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
