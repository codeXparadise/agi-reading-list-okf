---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 10.4. Additional Results
section_role: other
section_index: 21
pages: [11, 12, 13, 14]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "In Table 6 we compare the performance of the best architecture (edge network + set2set output) on different sized training sets. It is surprising how…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 10.4. Additional Results

> Section 21 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 11-14

In Table 6 we compare the performance of the best architecture (edge network + set2set output) on different sized training sets. It is surprising how data efficient this model is on some targets. For example, on both R2 and Omega our models are equal or better with 11k samples than the best baseline is with 110k samples.

• Electronic Spatial Extent ⟨R2⟩(Bohr2): The electronic spatial extent is the second moment of the charge distribution, ρ(r), or in other words ⟨R2⟩= R

drr2ρ(r).

• Norm of the dipole moment µ (Debye): The dipole moment, p(r) =

dr′p(r′)(r −r′), approximates the electric field far from a molecule. The norm of the dipole moment is related to how anisotropically

R

In Table 7 we compare the performance of several models trained without spatial information. The left 4 columns show the results of 4 experiments, one where we train the

## Neural Message Passing for Quantum Chemistry

Table 6. Results from training the edge network + set2set model on different sized training sets (N denotes the number of training samples)

Target N=11k N=35k N=58k N=82k N=110k mu 1.28 0.55 0.44 0.32 0.30 alpha 2.76 1.59 1.26 1.09 0.92 HOMO 2.33 1.50 1.34 1.19 0.99 LUMO 2.18 1.47 1.19 1.10 0.87 gap 3.53 2.34 2.07 1.84 1.60 R2 0.28 0.22 0.21 0.21 0.15 ZPVE 2.52 1.78 1.69 1.68 1.27 U0 1.24 0.69 0.58 0.62 0.45 U 1.05 0.69 0.60 0.52 0.45 H 1.14 0.64 0.65 0.53 0.39 G 1.23 0.62 0.64 0.49 0.44 Cv 1.99 1.24 0.93 0.87 0.80 Omega 0.28 0.25 0.24 0.15 0.19

GG-NN model on the sparse graph, one where we add virtual edges (ve), one where we add a master node (mn), and one where we change the graph level output to a set2set output (s2s). In general, we find that it’s important to allow the model to capture long range interactions in these graphs.

Table 7. Comparison of models when distance information is excluded

Target GG-NN ve mn s2s mu 3.94 3.76 4.02 3.81 alpha 2.43 2.07 2.01 2.04 HOMO 1.80 1.60 1.67 1.71 LUMO 1.73 1.48 1.48 1.41 gap 2.48 2.33 2.23 2.26 R2 14.74 17.11 13.16 13.67 ZPVE 5.93 3.21 3.26 3.02 U0 1.98 0.89 0.90 0.72 U 2.48 0.93 0.99 0.79 H 2.19 0.86 0.95 0.80 G 2.13 0.85 1.02 0.74 Cv 1.96 1.61 1.63 1.71 Omega 1.28 1.05 0.78 0.78 Average 3.47 2.90 2.62 2.57

In Table 8 we compare GG-NN + towers + set2set output (tow8) vs a baseline GG-NN + set2set output (GG-NN) when distance bins are used. We do this comparison in both the joint training regime (j) and when training one model per target (i). For joint training of the baseline we used 100 trials with d = 200 as well as 200 trials where d was chosen randomly in the set {43, 73, 113, 153}, we report the minimum test error across all 300 trials. For individual training of the baseline we used 100 trials where d was chosen uniformly in the range \[43, 200\]. The towers model was always trained with d = 200 and k = 8, with 100 tuning trials for joint training and 50 trials for individual training. The towers model outperforms the baseline model on 12 out of 13 targets in both individual and joint target training.

Table 8. Towers vs Vanilla Model (no explicit hydrogen) Target GG-NN-j tow8-j GG-NN-i tow8-i mu 2.73 2.47 2.16 2.23 alpha 1.66 1.50 1.47 1.34 HOMO 1.33 1.19 1.27 1.20 LUMO 1.28 1.12 1.24 1.11 gap 1.73 1.55 1.78 1.68 R2 6.07 6.16 4.78 4.11 ZPVE 4.07 3.43 2.70 2.54 U0 1.00 0.86 0.71 0.55 U 1.01 0.88 0.65 0.52 H 1.01 0.88 0.68 0.50 G 0.99 0.85 0.66 0.50 Cv 1.40 1.27 1.27 1.09 Omega 0.66 0.62 0.57 0.50 Average 1.92 1.75 1.53 1.37

In Table 9 right 2 columns compare the edge network (enn) with the pair message network (pm) in the joint training regime (j). The edge network consistently outperforms the pair message function across most targets.

In Table 10 we compare our MPNNs with different input featurizations. All models use the Set2Set output and GRU update functions. The no distance model uses the matrix multiply message function, the distance models use the edge neural network message function.

## Neural Message Passing for Quantum Chemistry

Table 9. Pair Message vs Edge Network in joint training

Target pm-j enn-j mu 2.10 2.24 alpha 2.30 1.48 HOMO 1.20 1.30 LUMO 1.46 1.20 gap 1.80 1.75 R2 10.87 2.41 ZPVE 16.53 3.85 U0 3.16 0.92 U 3.18 0.93 H 3.20 0.93 G 2.97 0.92 Cv 2.17 1.28 Omega 0.83 0.74 Average 3.98 1.53

Table 10. Performance With Different Input Information Target no distance distance dist + exp hydrogen mu 3.81 0.95 0.30 alpha 2.04 1.18 0.92 HOMO 1.71 1.10 0.99 LUMO 1.41 1.06 0.87 gap 2.26 1.74 1.60 R2 13.67 0.57 0.15 ZPVE 3.02 2.57 1.27 U0 0.72 0.55 0.45 U 0.79 0.55 0.45 H 0.80 0.59 0.39 G 0.74 0.55 0.44 Cv 1.71 0.99 0.80 Omega 0.78 0.41 0.19 Average 2.57 0.98 0.68

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
