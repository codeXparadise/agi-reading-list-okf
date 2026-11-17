---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
page: 7
pages: [7]
page_of: 9
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "Table 2: Tour length of the Ptr-Net and a collection of algorithms on a small scale TSP problem. n OPTIMAL A1 A2 A3 PTR-NET 5 2.12 2.18 2.12 2.12…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 9 - Pointer Networks

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [12 - Pointer Networks](../../papers/12-pointer-networks.md)

Table 2: Tour length of the Ptr-Net and a collection of algorithms on a small scale TSP problem.

n OPTIMAL A1 A2 A3 PTR-NET

5 2.12 2.18 2.12 2.12 2.12 10 2.87 3.07 2.87 2.87 2.88 50 (A1 TRAINED) N/A 6.46 5.84 5.79 6.42 50 (A3 TRAINED) N/A 6.46 5.84 5.79 6.09 5 (5-20 TRAINED) 2.12 2.18 2.12 2.12 2.12 10 (5-20 TRAINED) 2.87 3.07 2.87 2.87 2.87 20 (5-20 TRAINED) 3.83 4.24 3.86 3.85 3.88 25 (5-20 TRAINED) N/A 4.71 4.27 4.24 4.30 30 (5-20 TRAINED) N/A 5.11 4.63 4.60 4.72 40 (5-20 TRAINED) N/A 5.82 5.27 5.23 5.91 50 (5-20 TRAINED) N/A 6.46 5.84 5.79 7.66

this example we set the beam search procedure to only consider valid tours. Otherwise, the Ptr-Net model would sometimes output an invalid tour – for instance, it would repeat two cities or decided to ignore a destination. This procedure was relevant for n > 20, where at least 10% of instances would not produce any valid tour.

The first group of rows in the table show the Ptr-Net trained on optimal data, except for n = 50, since that is not feasible computationally (we trained a separate model for each n). Interestingly, when using the worst algorithm (A1) data to train the Ptr-Net, our model outperforms the algorithm that is trying to imitate.

The second group of rows in the table show how the Ptr-Net trained on optimal data with 5 to 20 cities can generalize beyond that. The results are virtually perfect for n = 25, and good for n = 30, but it seems to break for 40 and beyond (still, the results are far better than chance). This contrasts with the convex hull case, where we were able to generalize by a factor of 10. However, the underlying algorithms are of far greater complexity than O(n log n), which could explain this phenomenon.

## 5 Conclusions

In this paper we described Ptr-Net, a new architecture that allows us to learn a conditional probability of one sequence CP given another sequence P, where CP is a sequence of discrete tokens corresponding to positions in P. We show that Ptr-Nets can be used to learn solutions to three different combinatorial optimization problems. Our method works on variable sized inputs (yielding variable sized output dictionaries), something the baseline models (sequence-to-sequence with or without attention) cannot do directly. Even more impressively, they outperform the baselines on fixed input size problems - to which both the models can be applied.

Previous methods such as RNNSearch, Memory Networks and Neural Turing Machines \[5, 6, 2\] have used attention mechanisms to process inputs. However these methods do not directly address problems that arise with variable output dictionaries. We have shown that an attention mechanism can be applied to the output to solve such problems. In so doing, we have opened up a new class of problems to which neural networks can be applied without artificial assumptions. In this paper, we have applied this extension to RNNSearch, but the methods are equally applicable to Memory Networks and Neural Turing Machines.

Future work will try and show its applicability to other problems such as sorting where the outputs are chosen from the inputs. We are also excited about the possibility of using this approach to other combinatorial optimization problems.

## Acknowledgments

We would like to thank Rafal Jozefowicz, Ilya Sutskever, Quoc Le and Samy Bengio for useful discussions on this topic. We would also like to thank Daniel Gillick for his help with the final manuscript.

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
