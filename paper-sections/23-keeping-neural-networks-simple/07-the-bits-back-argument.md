---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: "5.2 The “bits back” argument"
section_role: other
section_index: 7
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "To communicate a set of noisy weights, the sender first collapses the posterior probability distribution for each weight by using a source of random…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.2 The “bits back” argument

> Section 7 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

To communicate a set of noisy weights, the sender first collapses the posterior probability distribution for each weight by using a source of random bits to pick a precise value for the weight (to within some very fine tolerance $t$). The probability of picking each possible value is determined by the posterior probability distribution for the weight. The sender then communicates these precise weights by coding them using some prior Gaussian distribution, $P$, so that the communication cost of a precise weight, $w$, is:

$$C(w) = -\log t - \log P(w)$$

$t$ must be small compared with the variance of $P$ so $C(w)$ is big. However, as we shall see, we are due for a big refund at the end.

Having sent the precise weights, the sender then communicates the data-misfits achieved using those weights. Having received the weights and the misfits, the receiver can then produce the correct outputs. But he can also do something else. Once he has the correct outputs he can run whatever learning algorithm was used by the sender and recover the exact same posterior probability distribution, $Q$, that the sender collapsed in order to get the precise weights.3 Now, since the receiver knows the sender’s posterior distribution for each weight and he knows the precise value that was communicated, he can recover all the random bits that the sender used to collapse that distribution to that value. So these random bits have been successfully communicated and we must subtract them from the overall communication cost to get the true cost of communicating the model and the misfits. The number of random bits required to collapse the posterior distribution for a weight, $Q$, to a particular finely quantized value, $w$, is:

$$R(w) = -\log t - \log Q(w)$$

So the true expected description length for a noisy weight is determined by taking an expectation, under the distribution $Q$:

3If the sender used random initial weights these can be communicated at a net cost of 0 bits using the method that is being explained.

$$G(P, Q) = \langle C(w) - R(w) \rangle = \int Q(w) \log \frac{Q(w)}{P(w)} dw$$ (8)

For Gaussians with different means and variances, the asymmetric divergence is

$$G(P, Q) = \log \frac{\sigma_p}{\sigma_q} + \frac{1}{2\sigma_p^2} \left[ \sigma_q^2 - \sigma_p^2 + (\mu_p - \mu_q)^2 \right]$$ (9)

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
