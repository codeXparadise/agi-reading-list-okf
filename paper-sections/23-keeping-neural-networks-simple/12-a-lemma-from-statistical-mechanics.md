---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 7.1 A lemma from statistical mechanics
section_role: other
section_index: 12
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "For a physical system at a temperature of 1, the Helmholtz free energy, $F$, is defined as the expected energy minus the entropy $$F = sumi ri Ei -…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7.1 A lemma from statistical mechanics

> Section 12 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

For a physical system at a temperature of 1, the Helmholtz free energy, $F$, is defined as the expected energy minus the entropy

$$F = \sum_i r_i E_i - \sum_i r_i \log \frac{1}{r_i}$$

where $i$ is an index over the alternative possible states of the system, $E_i$ is the energy of a state, and $r_i$ is the probability of a state. $F$ is a function of the probability distribution over states and the probability distribution which minimizes $F$ is the Boltzmann distribution in which probabilities are exponentially related to energies

$$r_i = \frac{e^{-E_i}}{\sum_j e^{-E_j}}$$

At the minimum given by the Boltzmann distribution, the free energy is equal to minus the log of the partition function:

$$F = -\log \sum_i e^{-E_i}$$

If we equate each Gaussian in the mixture with an alternative state of a physical system, we can equate $e^{-E_i}$ with $\pi_i e^{-G_i}$. So our method of picking a Gaussian from the mixture uses a Boltzmann distribution because it makes $r_i$ proportional to $e^{-E_i}$. The random bits that are successfully communicated when the receiver reconstructs the probabilities $r_i$ correspond exactly to the entropy of the Boltzmann distribution, so the total code cost (including the bits back) is equivalent to $F$ and is therefore equal to the expression given in equation 17.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
