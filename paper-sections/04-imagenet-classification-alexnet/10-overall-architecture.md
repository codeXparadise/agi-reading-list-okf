---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 3.5 Overall Architecture
section_role: other
section_index: 10
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "Now we are ready to describe the overall architecture of our CNN. As depicted in Figure 2, the net contains eight layers with weights; the first five…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.5 Overall Architecture

> Section 10 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

Now we are ready to describe the overall architecture of our CNN. As depicted in Figure 2, the net
contains eight layers with weights; the first five are convolutional and the remaining three are fullyconnected. The output of the last fully-connected layer is fed to a 1000-way softmax which produces
a distribution over the 1000 class labels. Our network maximizes the multinomial logistic regression
objective, which is equivalent to maximizing the average across training cases of the log-probability
of the correct label under the prediction distribution.

The kernels of the second, fourth, and fifth convolutional layers are connected only to those kernel
maps in the previous layer which reside on the same GPU (see Figure 2). The kernels of the third
convolutional layer are connected to all kernel maps in the second layer. The neurons in the fullyconnected layers are connected to all neurons in the previous layer. Response-normalization layers
follow the first and second convolutional layers. Max-pooling layers, of the kind described in Section
3.4, follow both response-normalization layers as well as the fifth convolutional layer. The ReLU
non-linearity is applied to the output of every convolutional and fully-connected layer.

The first convolutional layer filters the 224×224×3 input image with 96 kernels of size 11×11× 3
with a stride of 4 pixels (this is the distance between the receptive field centers of neighboring

$$
224\times224\times3
$$

$$
11\times11\times3
$$

3We cannot describe this network in detail due to space constraints, but it is specified precisely by the code
and parameter files provided here: http://code.google.com/p/cuda-convnet/.

Stride of 4 Max pooling Max pooling dense dense dense 1000 2048 2048 2048

Figure 2: An illustration of the architecture of our CNN, explicitly showing the delineation of responsibilities
between the two GPUs. One GPU runs the layer-parts at the top of the figure while the other runs the layer-parts
at the bottom. The GPUs communicate only at certain layers. The network’s input is 150,528-dimensional, and
the number of neurons in the network’s remaining layers is given by 253,440–186,624–64,896–64,896–43,264–
4096–4096–1000.

neurons in a kernel map). The second convolutional layer takes as input the (response-normalized
and pooled) output of the first convolutional layer and filters it with 256 kernels of size 5 *×* 5 *×* 48.
The third, fourth, and fifth convolutional layers are connected to one another without any intervening
pooling or normalization layers. The third convolutional layer has 384 kernels of size 3 *×* 3 *×*
256 connected to the (normalized, pooled) outputs of the second convolutional layer. The fourth
convolutional layer has 384 kernels of size 3 *×* 3 *×* 192 , and the fifth convolutional layer has 256
kernels of size 3 *×* 3 *×* 192. The fully-connected layers have 4096 neurons each.

$$
5\times5\times48.
$$

$$
3\times3\times
3\times3\times192
$$

$$
3\times3\times192
$$

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
