---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 2 Applying the Minimum Description Length Principle
section_role: other
section_index: 4
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "When fitting models to data, it is always possible to fit the training data better by using a more complex model, but this may make the model worse…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 Applying the Minimum Description Length Principle

> Section 4 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

When fitting models to data, it is always possible to fit the training data better by using a more complex model, but this may make the model worse at fitting new data. So we need some way of deciding when extra complexity in the model is not worth the improvement in the data-fit. The Minimum Description Length Principle (Rissanen, 1986) asserts that the best model of some data is the one that minimizes the combined cost of describing the model and describing the misfit between the model and the data. For supervised neural networks with a predetermined architecture, the model cost is the number of bits it takes to describe the weights, and the data-misfit cost is the number of bits it takes to describe the discrepancy between the correct output and the output of the neural network on each training case. We can think in terms of a sender who can see both the input vector and the correct output and a receiver who can only see the input vector. The sender first fits a neural network, of pre-arranged architecture, to the complete set of training cases, then sends the weights to the receiver. For each training case the sender also sends the discrepancy between the net’s output and the correct output. By adding this discrepancy to the output of the net, the receiver can generate exactly the correct output.

t
0 v

Figure This shows the probability mass asso
ciated with a quantized value vusing a quan
tization width tIft is much narrower than the
Gaussian distribution the probability mass is well
approximated by the product of the height and the
width so the log probability is a sum of two terms
The log t term is a constant and if the distribu
tion is a zeromean Gaussian the log of the height
is proportional to v2

$$
v^{2}
$$

## Coding the data mists

To apply the MDL principle we need to decide on a
coding scheme for the data mists and for the weights
Clearlyif the data mists are real numbers an innite
amount of information is needed to convey them So we
shall assume that they are very nely quantized using
intervals of xed width tWe shall also assume that
the data mists are encoded separately for each of the
output units

The coding theorem tells us that if a sender and a re
ceiver have agreed on a probability distribution that as
signs a probability mass p yto each possible quan
tized data mist ythen we can code the mist using
log2p ybits If wewant to minimize the expected
number of bits the best probability distribution to use
is the correct one but any other agreed distribution can
also be used For convenience we shall assume that for
output unit j the data mists are encoded by assuming
that they are drawn from a zeromean Gaussian distri
bution with standard deviation jProvided thatjis
large compared with the quantization width tthe as
sumed probability of a particular data mist between
the desired output dcj on training case c and the actual
output yjc is then well approximated by the probability
mass shown in gure

$$
p(\Delta y)
$$

$$
\left[\Delta y\right.
j
$$

$$
-\log_{2}p(\Delta y)
$$

$$
\sigma_{j}
$$

$$
\sigma_{j}
$$

$$
d_{j}^{c}
$$

$$
y_{j}^{c}
$$

$$
p(d_{j}^{c}-y_{j}^{c})=t\frac{1}{\sqrt{2\pi}\sigma_{j}}\exp\left[\frac{-(d_{j}^{c}-y_{j}^{c})^{2}}{2\sigma_{j}^{2}}\right]
$$

(1)

Using an optimal code the description length of a data
mist dcj yjcin units of log2 ebits called nats is

$$
d_{j}^{c}-y_{j}^{c}
$$

$$
\log_{2}(e)
$$

$$
-\log p(d_{j}^{c}-y_{j}^{c})=-\log t+\log\sqrt{2\pi}+\log\sigma_{j}+\frac{(d_{j}^{c}-y_{j}^{c})^{2}}{2\sigma_{j}^{2}}
$$

(2)

$$
\sigma_{j}
$$

square deviation of the mists from zero1 Using this
value ofjand summing over all training cases the last
term of equation becomes a constant and the data
mist cost is
X

To minimize this description length summed over all N
training cases the optimal value ofjis the root mean

$$
\sigma_{j}
$$

$$
C_{\mathrm{d a t a-m i s f i t}}=k N\quad+\quad\frac{N}{2}\log\left[\frac{1}{N}\sum_{c}(d_{j}^{c}-y_{j}^{c})^{2}\right]
$$

(3)

where k is a constant that depends only on t

$$
k
$$

Independently of whether we use the optimal value or
a predetermined value for jit is apparent that the
description length is minimized by minimizing the usual
squared error function so the Gaussian assumptions we
have made about coding can be viewed as the MDL
justication of this error function

$$
\sigma_{j},
$$

## A simple method of coding the weights

We could code the weights in just the same way aswe
code the data mists We assume that the weights of
the trained network are nely quantized and come from
a zeromean Gaussian distribution If the standard de
viation wof this distribution is xed in advance the
description length of the weights is simply proportional
to the sum of their squares So assuming we use a Gaus
sian with standard deviationjfor encoding the output
errors we can minimize the total description length of
the data mists and the weights by minimizing the sum
of two terms
X X X

$$
\sigma_{w},
$$

$$
\sigma_{j}
$$

$$
C=\sum_{j}\frac{1}{2\sigma_{j}^{2}}\sum_{c}(d_{j}^{c}-y_{j}^{c})^{2}+\frac{1}{2\sigma_{w}^{2}}\sum_{ij}w_{ij}^{2}
$$

(4)

where c is an index over training cases

This is just the standard weightdecay method The
fact that weightdecay improves generalization Hinton
can therefore be viewed as a vindication of this
crude MDL approach in which the standard deviations
of the gaussians used for coding the data mists and the
weights are both xed in advance2

An elaboration of standard weightdecay is to assume
that the distribution of weights in the trained network
can be modelled more accurately by using a mixture
of several Gaussians whose means variances and mix
ing proportions are adapted as the network is trained

1If the optimal value of j is to b e used it must b e com
municated b efore the data mists are sent so it to o must b e
co ded However since it is only one numb er we are probably
safe in ignoring this asp ect of the total description length

$$
\sigma_{j}
$$

2It is clear from equation that it is only the ratio of
the variances of the two Gaussians that matters Rather
than guessing this ratio it is usually b etter to estimate it by
seeing which ratio gives optimal p erformance on a validation
set

(Nowlan and Hinton, 1992). For some tasks this more elaborate way of coding the weights gives considerably better generalization. This is especially true when only a small number of different weight values are required.

However, this more elaborate scheme still suffers from a serious weakness: It assumes that all the weights are quantized to the same tolerance, and that this tolerance is small compared with the standard deviations of the Gaussians used for modelling the weight distribution. Thus it takes into account the probability density of a weight (the height in figure 1) but it ignores the precision (the width). This is a terrible waste of bits. A network is clearly much more economical to describe if some of the weight values can be described very imprecisely without significantly affecting the predictions of the network.

MacKay (1992) has considered the effects of small changes in the weights on the outputs of the network after the network has been trained. The next section describes a method of taking the precision of the weights into account during training so that the precision of a weight can be traded against both its probability density and the excess data misfit caused by imprecision in the weight.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
