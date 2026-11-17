---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 10 Discussion
section_role: results
section_index: 15
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "There is a correct, but intractable, Bayesian method of determining the weights in a feedforward neural network. We start with a prior distribution…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 10 Discussion

> Section 15 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `results` · pages n/a

There is a correct, but intractable, Bayesian method of determining the weights in a feedforward neural network. We start with a prior distribution over all possible points in weight space. We then construct the correct posterior distribution at each point in weight space by multiplying the prior by the probability of getting the outputs in the training set given those weights.4 Finally we normalize to get the full posterior distribution. Then we use this distribution of weight values to make predictions for new input vectors.

In practice, the closest we can get to the ideal Bayesian method is to use a Monte Carlo method to sample from the posterior distribution. This could be done by considering random moves in weight space and accepting a move with a probability that depends on how well the resulting network fits the desired outputs. Neal (1993) shows how the gradient information provided by backpropagation can be used to get a much more efficient method of obtaining samples from the posterior distribution. The major advantage of Monte Carlo methods is that they do not impose unrealistically simple assumptions about the shape of the posterior distribution in weight space.

If we are willing to make simplifying assumptions about the posterior distribution, time-consuming Monte Carlo simulations can be avoided. MacKay (1992) finds a single locally optimal point in weight space and constructs a full covariance Gaussian approximation to the posterior distribution around that point. The alternative method proposed in this paper is to use a simpler Gaussian approximation (with no off-diagonal terms in the covariance matrix) but to take this distribution into account during the learning. With one layer of non-linear hidden units, the integration over the Gaussian distribution can be performed exactly and the exact weight derivatives can be computed efficiently.

It is not clear how much is lost by ignoring the off-diagonal terms in the covariance matrix. David Mackay (personal communication) has shown that if standard backpropagation is used to find a single, locally optimal point in weight space and a Gaussian approximation to the posterior weight distribution is then constructed around this point, the covariances between different weights are significant. However, this does not mean that the covariances are significant when the learning algorithm is explicitly manipulating the Gaussian distribution because in this case the learning will try to force the noise in the weights to be independent. The pressure for independence comes from the fact that the cost function will overestimate the information in the weights if they have correlated noise. We are currently performing simulations to see if this pressure does indeed suppress the covariances.

When using the standard backpropagation algorithm, it is essential that the output of a hidden unit is a smooth function of its input. This is why the hidden units use a smooth sigmoid function instead of a linear threshold function. With noisy weights, however, it is possible to use a version of the backpropagation algorithm described above in networks that have one layer of linear threshold units. The noise in the weights ensures that the probability of a threshold unit being active is a smooth function of its inputs. As a result, it is easier to optimize a whole Gaussian distribution over weight vectors than it is to optimize a single weight vector.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
