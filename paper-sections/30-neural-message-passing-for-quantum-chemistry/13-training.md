---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 7. Training
section_role: experiments
section_index: 13
pages: [6]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Each model and target combination was trained using a uniform random hyper parameter search with 50 trials. T was constrained to be in the range 3 ≤T…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7. Training

> Section 13 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `experiments` · pages 6-6

Each model and target combination was trained using a uniform random hyper parameter search with 50 trials. T was constrained to be in the range 3 ≤T ≤8 (in practice, any T ≥3 works). The number of set2set computations M was chosen from the range 1 ≤M ≤12. All models were trained using SGD with the ADAM optimizer (Kingma & Ba (2014)), with batch size 20 for 3 million steps ( 540 epochs). The initial learning rate was chosen uniformly between 1e−5 and 5e−4. We used a linear learning rate decay that began between 10% and 90% of the way through training and the initial learning rate l decayed to a final learning rate l ∗F, using a decay factor F in the range \[.01, 1\].

The QM-9 dataset has 130462 molecules in it. We randomly chose 10000 samples for validation, 10000 samples for testing, and used the rest for training. We use the validation set to do early stopping and model selection and we report scores on the test set. All targets were normalized to have mean 0 and variance 1. We minimize the mean squared error between the model output and the target, although we evaluate mean absolute error.

Training Without Spatial Information: We also experimented in the setting where spatial information is not included in the input. In general, we find that augmenting the MPNN with some means of capturing long range interactions between nodes in the graph greatly improves performance in this setting. To demonstrate this we performed 4 experiments, one where we train the GG-NN model on the sparse graph, one where we add virtual edges, one where we add a master node, and one where we change the graph level output to a set2set output. The error ratios averaged across the 13 targets are shown in table 3. Overall, these three modifications help on all 13 targets, and the Set2Set output achieves chemical accuracy on 5 out of 13 targets. For more details, consult the supplementary material. The experiments shown tables 3 and 4 were run with a partial charge feature as a node input. This feature is an output of the DFT calculation and thus could not be used in an applied setting. The state of art numbers we report in table 2 do not use this feature.

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
