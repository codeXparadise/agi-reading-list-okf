---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 5.3 The expected description length of the data misfits
section_role: other
section_index: 8
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "To compute the data-misfit cost given in equation 3 we need the expected value of $(dj^c - yj^c)^2$. This squared error is caused partly by the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.3 The expected description length of the data misfits

> Section 8 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

To compute the data-misfit cost given in equation 3 we need the expected value of $(d_j^c - y_j^c)^2$. This squared error is caused partly by the systematic errors of the network and partly by the noise in the weights. Unfortunately, for general feedforward networks with noisy weights, the expected squared errors are not easy to compute. Linear approximations are possible if the level of noise in the weights is sufficiently small compared with the smoothness of the non-linearities, but this defeats one of the main purposes of the idea which is to allow very noisy weights. Fortunately, if there is only one hidden layer and if the output units are linear, it is possible to compute the expected squared error exactly.

The weights are assumed to have independent Gaussian noise, so for any input vector we can compute the mean $\mu_{x_h}$, and variance, $V_{x_h}$, of the Gaussian-distributed total input, $x_h$, received by hidden unit $h$. Using a table, we can then compute the mean, $\mu_{y_h}$ and variance, $V_{y_h}$, of the output of the hidden unit, even though this output is not Gaussian distributed. A lot of computation is required to create this two-dimensional table since many different pairs of $\mu_{x_h}$ and $V_{x_h}$ must be used, and for each pair we must use Monte Carlo sampling or numerical integration to compute $\mu_{y_h}$ and $V_{y_h}$. Once the table is built, however, it is much more efficient than using Monte Carlo sampling at runtime.

Since the noise in the outputs of the hidden units is independent, they independently contribute variance to each linear output unit. The noisy weights, $w_{hj}$, also contribute variance to the output units. Since the output units are linear, their outputs, $y_j$, are equal to the total inputs they receive, $x_j$. On a particular training case, the output, $y_j$, of output unit $j$ is a random variable with the following mean and variance:

$$\mu_{y_j} = \sum_h \mu_{y_h} \mu_{w_{hj}}$$ (10)
$$V_{y_j} = \sum_h \left[ \mu_{w_{hj}}^2 V_{y_h} + \mu_{y_h}^2 V_{w_{hj}} + V_{y_h} V_{w_{hj}} \right]$$ (11)

The mean and the variance of the activity of output unit $j$ make independent contributions to the expected squared error $\langle E_j \rangle$. If the desired output of $j$ on a particular training case is $d_j$, $\langle E_j \rangle$ is given by:

$$\langle E_j \rangle = \langle (d_j - y_j)^2 \rangle = (d_j - \mu_{y_j})^2 + V_{y_j}$$ (12)

So, for each input vector, we can use the table and the equations above to compute the exact value of $\langle E_j \rangle$. We can also backpropagate the exact derivatives of $E = \sum_j \langle E_j \rangle$ provided we first build another table to allow derivatives to be backpropagated through the hidden units. As before, the table is indexed by $\mu_{x_h}$ and $V_{x_h}$ but for the backward pass each cell of the table contains the four partial derivatives that are needed to convert the output derivatives of $h$ into its input derivatives using the equations:

$$\frac{\partial E}{\partial \mu_{x_h}} = \frac{\partial E}{\partial \mu_{y_h}} \frac{\partial \mu_{y_h}}{\partial \mu_{x_h}} + \frac{\partial E}{\partial V_{y_h}} \frac{\partial V_{y_h}}{\partial \mu_{x_h}}$$ (13)
$$\frac{\partial E}{\partial V_{x_h}} = \frac{\partial E}{\partial \mu_{y_h}} \frac{\partial \mu_{y_h}}{\partial V_{x_h}} + \frac{\partial E}{\partial V_{y_h}} \frac{\partial V_{y_h}}{\partial V_{x_h}}$$ (14)

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
