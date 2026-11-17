---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/06-identity-mappings-in-deep-residual-networks.md
source: ../../papers/06-identity-mappings-in-deep-residual-networks.md
paper_title: Identity Mappings in Deep Residual Networks
sequence: 6
page: 13
pages: [13]
page_of: 15
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "depth (so a 1001-layer net is ∼10× complex of a 100-layer net). On CIFAR, ResNet-1001 takes about 27 hours to train on 2 GPUs; on ImageNet, ResNet200…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 13 of 15 - Identity Mappings in Deep Residual Networks

> Page 13 of the source PDF, verbatim as extracted. Canonical document: [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md)

depth (so a 1001-layer net is ∼10× complex of a 100-layer net). On CIFAR, ResNet-1001 takes about 27 hours to train on 2 GPUs; on ImageNet, ResNet200 takes about 3 weeks to train on 8 GPUs (on par with VGG nets \[22\]).

## 6 Conclusions

This paper investigates the propagation formulations behind the connection mechanisms of deep residual networks. Our derivations imply that identity shortcut connections and identity after-addition activation are essential for making information propagation smooth. Ablation experiments demonstrate phenomena that are consistent with our derivations. We also present 1000-layer deep networks that can be easily trained and achieve improved accuracy.

Appendix: Implementation Details The implementation details and hyperparameters are the same as those in \[1\]. On CIFAR we use only the translation and flipping augmentation in \[1\] for training. The learning rate starts from 0.1, and is divided by 10 at 32k and 48k iterations. Following \[1\], for all CIFAR experiments we warm up the training by using a smaller learning rate of 0.01 at the beginning 400 iterations and go back to 0.1 after that, although we remark that this is not necessary for our proposed Residual Unit. The mini-batch size is 128 on 2 GPUs (64 each), the weight decay is 0.0001, the momentum is 0.9, and the weights are initialized as in \[23\].

On ImageNet, we train the models using the same data augmentation as in \[1\]. The learning rate starts from 0.1 (no warming up), and is divided by 10 at 30 and 60 epochs. The mini-batch size is 256 on 8 GPUs (32 each). The weight decay, momentum, and weight initialization are the same as above.

When using the pre-activation Residual Units (Fig. 4(d)(e) and Fig. 5), we pay special attention to the first and the last Residual Units of the entire network. For the first Residual Unit (that follows a stand-alone convolutional layer, conv1), we adopt the first activation right after conv1 and before splitting into two paths; for the last Residual Unit (followed by average pooling and a fullyconnected classifier), we adopt an extra activation right after its element-wise addition. These two special cases are the natural outcome when we obtain the pre-activation network via the modification procedure as shown in Fig. 5.

The bottleneck Residual Units (for ResNet-164/1001 on CIFAR) are constructed following \[1\]. For example, a

"

#

unit in ResNet-110 is replaced

3×3, 16 3×3, 16





1×1, 16 3×3, 16 1×1, 64

with a

unit in ResNet-164, both of which have roughly the same num-



ber of parameters. For the bottleneck ResNets, when reducing the feature map size we use projection shortcuts \[1\] for increasing dimensions, and when preactivation is used, these projection shortcuts are also with pre-activation.

---

[previous page](page-012.md) · [next page](page-014.md) · [all pages](index.md)
