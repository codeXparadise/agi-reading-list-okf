---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 9. Conclusions and Future Work
section_role: conclusion
section_index: 15
pages: [7, 8]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Table 4. Towers vs Vanilla GG-NN (no explicit hydrogen) Model Average Error Ratio GG-NN + joint training 1.92 towers8 + joint training 1.75 GG-NN +…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 9. Conclusions and Future Work

> Section 15 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `conclusion` · pages 7-8

Table 4. Towers vs Vanilla GG-NN (no explicit hydrogen) Model Average Error Ratio GG-NN + joint training 1.92 towers8 + joint training 1.75 GG-NN + individual training 1.53 towers8 + individual training 1.37

Our results show that MPNNs with the appropriate message, update, and output functions have a useful inductive bias for predicting molecular properties, outperforming several strong baselines and eliminating the need for complicated feature engineering. Moreover, our results also reveal the importance of allowing long range interactions between nodes in the graph with either the master node or the set2set output. The towers variation makes these models more scalable, but additional improvements will be needed to scale to much larger graphs.

individual and joint target training. We believe the benefit of towers is that it resembles training an ensemble of models. Unfortunately, our attempts so far at combining the towers and edge network message function have failed to further improve performance, possibly because the combination makes training more difficult. Further training details, and error ratios on all targets can be found in the supplementary material.

An important future direction is to design MPNNs that can generalize effectively to larger graphs than those appearing in the training set or at least work with benchmarks designed to expose issues with generalization across graph sizes. Generalizing to larger molecule sizes seems particularly challenging when using spatial information. First of all, the pairwise distance distribution depends heavily on the number of atoms. Second, our most successful ways of using spatial information create a fully connected graph where the number of incoming messages also depends on the number of nodes. To address the second issue, we believe that adding an attention mechanism over the incoming message vectors could be an interesting direction to explore.

Additional Experiments: In preliminary experiments, we tried disabling weight tying across different time steps. However, we found that the most effective way to increase performance was to tie the weights and use a larger hidden dimension d. We also early on found the pair message function to perform worse than the edge network function. This included a toy pathfinding problem which was originally

2As reported in Sch¨utt et al. (2017). The model was trained on a different train/test split with 100k training samples vs 110k used in our experiments.

## Neural Message Passing for Quantum Chemistry

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
