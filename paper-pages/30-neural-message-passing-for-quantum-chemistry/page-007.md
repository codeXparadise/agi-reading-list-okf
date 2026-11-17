---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
page: 7
pages: [7]
page_of: 14
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Neural Message Passing for Quantum Chemistry Table 2. Comparison of Previous Approaches (left) with MPNN baselines (middle) and our methods (right)…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 14 - Neural Message Passing for Quantum Chemistry

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md)

## Neural Message Passing for Quantum Chemistry

Table 2. Comparison of Previous Approaches (left) with MPNN baselines (middle) and our methods (right) Target BAML BOB CM ECFP4 HDAD GC GG-NN DTNN enn-s2s enn-s2s-ens5

mu 4.34 4.23 4.49 4.82 3.34 0.70 1.22 0.30 0.20 alpha 3.01 2.98 4.33 34.54 1.75 2.27 1.55 0.92 0.68 HOMO 2.20 2.20 3.09 2.89 1.54 1.18 1.17 0.99 0.74 LUMO 2.76 2.74 4.26 3.10 1.96 1.10 1.08 0.87 0.65 gap 3.28 3.41 5.32 3.86 2.49 1.78 1.70 1.60 1.23 R2 3.25 0.80 2.83 90.68 1.35 4.73 3.99 0.15 0.14 ZPVE 3.31 3.40 4.80 241.58 1.91 9.75 2.52 1.27 1.10 U0 1.21 1.43 2.98 85.01 0.58 3.02 0.83 0.45 0.33 U 1.22 1.44 2.99 85.59 0.59 3.16 0.86 0.45 0.34 H 1.22 1.44 2.99 86.21 0.59 3.19 0.81 0.39 0.30 G 1.20 1.42 2.97 78.36 0.59 2.95 0.78 .842 0.44 0.34 Cv 1.64 1.83 2.36 30.29 0.88 1.45 1.19 0.80 0.62 Omega 0.27 0.35 1.32 1.47 0.34 0.32 0.53 0.19 0.15 Average 2.17 2.08 3.37 53.97 1.35 2.59 1.36 0.68 0.52

designed to benefit from using pair messages. Also, when trained jointly on the 13 targets the edge network function outperforms pair message on 11 out of 13 targets, and has an average error ratio of 1.53 compared to 3.98 for pair message. Given the difficulties with training this function we did not pursue it further. For performance on smaller sized training sets, consult the supplementary material.

Table 3. Models Trained Without Spatial Information Model Average Error Ratio GG-NN 3.47 GG-NN + Virtual Edge 2.90 GG-NN + Master Node 2.62 GG-NN + set2set 2.57

## 9. Conclusions and Future Work

Table 4. Towers vs Vanilla GG-NN (no explicit hydrogen) Model Average Error Ratio GG-NN + joint training 1.92 towers8 + joint training 1.75 GG-NN + individual training 1.53 towers8 + individual training 1.37

Our results show that MPNNs with the appropriate message, update, and output functions have a useful inductive bias for predicting molecular properties, outperforming several strong baselines and eliminating the need for complicated feature engineering. Moreover, our results also reveal the importance of allowing long range interactions between nodes in the graph with either the master node or the set2set output. The towers variation makes these models more scalable, but additional improvements will be needed to scale to much larger graphs.

individual and joint target training. We believe the benefit of towers is that it resembles training an ensemble of models. Unfortunately, our attempts so far at combining the towers and edge network message function have failed to further improve performance, possibly because the combination makes training more difficult. Further training details, and error ratios on all targets can be found in the supplementary material.

An important future direction is to design MPNNs that can generalize effectively to larger graphs than those appearing in the training set or at least work with benchmarks designed to expose issues with generalization across graph sizes. Generalizing to larger molecule sizes seems particularly challenging when using spatial information. First of all, the pairwise distance distribution depends heavily on the number of atoms. Second, our most successful ways of using spatial information create a fully connected graph where the number of incoming messages also depends on the number of nodes. To address the second issue, we believe that adding an attention mechanism over the incoming message vectors could be an interesting direction to explore.

Additional Experiments: In preliminary experiments, we tried disabling weight tying across different time steps. However, we found that the most effective way to increase performance was to tie the weights and use a larger hidden dimension d. We also early on found the pair message function to perform worse than the edge network function. This included a toy pathfinding problem which was originally

2As reported in Sch¨utt et al. (2017). The model was trained on a different train/test split with 100k training samples vs 110k used in our experiments.

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
