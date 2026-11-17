---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 9 Preliminary Results
section_role: other
section_index: 14
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "We have not yet performed a thorough comparison between this algorithm and alternative methods and it may well turn out that further refinements are…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 9 Preliminary Results

> Section 14 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

We have not yet performed a thorough comparison between this algorithm and alternative methods and it may well turn out that further refinements are required to make it competitive. We have, however, tried the algorithm on one very high dimensional task with very scarce training data. The task is to predict the effectiveness of a class of peptide molecules. Each molecule is described by 128 parameters (the input vector) and has an effectiveness that is a single scalar (the output value). All inputs and outputs were normalized to have zero mean and unit variance so that the weights could be expected to have similar scales. The training set consisted of 105 cases and the test set was the remaining 420 cases. We deliberately chose a very small training set since these are the circumstances in which it should be most helpful to control the amount of information in the weights. We tried a network with 4 hidden units. This network contains 521 adaptive weights (including the biases of the output and hidden units) so it overfits the 105 training cases very badly if we do not limit the information in the weights.

We used an adaptive mixture of 5 Gaussians as our coding-prior for the weights. The Gaussians were initialized with means uniformly spaced between $-0.24$ and $+0.24$ and separated by 2 standard deviations from their neighbors. The initial means for the posterior distributions of each weight were chosen from a Gaussian with mean 0 and standard deviation 0.15. The standard deviations of the posteriors for the weights were all initialized at 0.1.

We optimize all of the parameters simultaneously using a conjugate gradient method. For the variances we optimize the log variance so that it cannot go negative and cannot collapse to zero. To ensure that the mixing proportions of the Gaussians in the coding-prior lie between 0 and 1 and add to 1 we optimize the $x_i$ where

$$\pi_i = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

If we penalize the weights by the full cost of describing them, the optimization quickly makes all of the weights equal and negative and uses the bias of the output unit to fix the output at the mean of the desired values in the training set. It seems that it is initially very easy to reduce the combined cost function by using weights that contain almost no information, and it is very hard to escape from this poor solution. To avoid this trap, we multiply the cost of the weights by a coefficient that starts at .05 and gradually increases to 1 according to the schedule .05, .1, .15, .2, .3, .4, .5, .6, .7, .8, .9, 1.0. At each value of the coefficient we do 100 conjugate gradient updates of the weights and at the final value of 1.0 we do not terminate the optimization until the cost function changes by less than $10^{-6}$ nats (a nat is $\log_2(e)$ bits). Figure 2 shows all the incoming and outgoing weights of the four hidden units after one run of the optimization. It

Figure 2: The final weights of the network. Each large block represents one hidden unit.The small black or white rectangles represent negative or positive weights with the area of a rectangle representing the magnitude of the weight. The bottom 12 rows in each block represent the incoming weights of the hidden unit. The central weight at the top of each block is the weight from the hidden unit to the linear output unit. The weight at the top-right of a block is the bias of the hidden unit.

| Category | Probability distribution |
| --- | --- |
| -2 | 0 |
| 2 | 0 |

Figure 3: The final probability distribution that is used for coding the weights. This distribution is implemented by adapting the means, variances and mixing proportions of five gaussians.

is clear that the weights form three fairly sharp clusters. Figure 3 shows that the mixture of 5 Gaussians has adapted to implement the appropriate coding-prior for this weight distribution.

The performance of the network can be measured by comparing the squared error it achieves on the test data with the error that would be achieved by simply guessing the mean of the correct answers for the test data:

$$
Relative Error=\frac{\sum_{c}(d_{c}-y_{c})^{2}}{\sum_{c}(d_{c}-\bar{d})^{2}}
$$

(27)

We ran the optimization five times using different randomly chosen values for the initial means of the noisy weights. For the network that achieved the lowest value of the overall cost function, the relative error was 0.286. This compares with a relative error of 0.967 for the same network when we used noise-free weights and did not penalize their information content. The best relative error obtained using simple weight-decay with four nonlinear hidden units was .317. This required a carefully chosen penalty coefficient for the squared weights that corresponds to $ \sigma_{j}^{2} /\sigma_{w}^{2} $ in equation 4. To set this weightdecay coefficient appropriately it was necessary to try many different values on a portion of the training set and to use the remainder of the training set to decide which coefficient gave the best generalization. Once the best coefficient had been determined the whole of the training set was used with this coefficient. A lower error of 0.291 can be achieved using weight-decay if we gradually increase the weight-decay coefficient and pick the value that gives optimal performance on the test data. But this is cheating. Linear regression gave a huge relative error of 35.6 (gross overfitting) but this fell to 0.291 when we penalized the sum of the squares of the regression coefficients by an amount that was chosen to optimize performance on the test data. This is almost identical to the performance with 4 hidden units and optimal weight-decay probably because, with small weights, the hidden units operate in their central linear range, so the whole network is effectively linear.

$$
\sigma_{j}^{2}/\sigma_{w}^{2}
$$

These preliminary results demonstrate that our new method allows us to fit quite complicated non-linear models even when the number of training cases is less than the number of dimensions in the input vector. The results also show that the new method is slightly better than simple weight-decay on at least one task. Much more experimental work is required to decide whether the method is competitive with other statistical techniques for handling non-linear tasks in which the amount of training data is very small compared with the dimensionality of the input. It is also worth mentioning that the solution with the lowest value of the total description length was the solution in which all the weights except the output bias are equal and negative. This solution has a relative error of approximately 1.0 so it is a serious embarrassment for the Minimum Description Length Principle or for our method of describing the weights.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
