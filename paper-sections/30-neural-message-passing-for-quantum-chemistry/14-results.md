---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 8. Results
section_role: results
section_index: 14
pages: [6, 7]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "In all of our tables we report the ratio of the mean absolute error (MAE) of our models with the provided estimate of chemical accuracy for that…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 8. Results

> Section 14 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `results` · pages 6-7

In all of our tables we report the ratio of the mean absolute error (MAE) of our models with the provided estimate of chemical accuracy for that target. Thus any model with error ratio less than 1 has achieved chemical accuracy for that target. In the supplementary material we list the chemical accuracy estimates for each target, these are the same estimates that were given in Faber et al. (2017). In this way, the MAE of our models can be calculated as (Error Ratio) × (Chemical Accuracy). Note, unless otherwise indicated, all tables display result of models trained individually on each target (as opposed to training one model to predict all 13).

We performed numerous experiments in order to find the best possible MPNN on this dataset as well as the proper input representation. In our experiments, we found that including the complete edge feature vector (bond type, spatial distance) and treating hydrogen atoms as explicit nodes in the graph to be very important for a number of targets. We also found that training one model per target consistently outperformed jointly training on all 13 targets. In some cases the improvement was up to 40%. Our best MPNN variant used the edge network message function, set2set output, and operated on graphs with explicit hydrogens. We were able to further improve performance on the test set by ensembling the predictions of the five models with lowest validation error.

Towers: Our original intent in developing the towers variant was to improve training time, as well as to allow the model to be trained on larger graphs. However, we also found some evidence that the multi-tower structure improves generalization performance. In table 4 we compare GG-NN + towers + set2set output vs a baseline GGNN + set2set output when distance bins are used. We do this comparison in both the joint training regime and when training one model per target. The towers model outperforms the baseline model on 12 out of 13 targets in both

## Neural Message Passing for Quantum Chemistry

Table 2. Comparison of Previous Approaches (left) with MPNN baselines (middle) and our methods (right) Target BAML BOB CM ECFP4 HDAD GC GG-NN DTNN enn-s2s enn-s2s-ens5

mu 4.34 4.23 4.49 4.82 3.34 0.70 1.22 0.30 0.20 alpha 3.01 2.98 4.33 34.54 1.75 2.27 1.55 0.92 0.68 HOMO 2.20 2.20 3.09 2.89 1.54 1.18 1.17 0.99 0.74 LUMO 2.76 2.74 4.26 3.10 1.96 1.10 1.08 0.87 0.65 gap 3.28 3.41 5.32 3.86 2.49 1.78 1.70 1.60 1.23 R2 3.25 0.80 2.83 90.68 1.35 4.73 3.99 0.15 0.14 ZPVE 3.31 3.40 4.80 241.58 1.91 9.75 2.52 1.27 1.10 U0 1.21 1.43 2.98 85.01 0.58 3.02 0.83 0.45 0.33 U 1.22 1.44 2.99 85.59 0.59 3.16 0.86 0.45 0.34 H 1.22 1.44 2.99 86.21 0.59 3.19 0.81 0.39 0.30 G 1.20 1.42 2.97 78.36 0.59 2.95 0.78 .842 0.44 0.34 Cv 1.64 1.83 2.36 30.29 0.88 1.45 1.19 0.80 0.62 Omega 0.27 0.35 1.32 1.47 0.34 0.32 0.53 0.19 0.15 Average 2.17 2.08 3.37 53.97 1.35 2.59 1.36 0.68 0.52

designed to benefit from using pair messages. Also, when trained jointly on the 13 targets the edge network function outperforms pair message on 11 out of 13 targets, and has an average error ratio of 1.53 compared to 3.98 for pair message. Given the difficulties with training this function we did not pursue it further. For performance on smaller sized training sets, consult the supplementary material.

Table 3. Models Trained Without Spatial Information Model Average Error Ratio GG-NN 3.47 GG-NN + Virtual Edge 2.90 GG-NN + Master Node 2.62 GG-NN + set2set 2.57

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
