---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/06-identity-mappings-in-deep-residual-networks.md
source: ../../papers/06-identity-mappings-in-deep-residual-networks.md
paper_title: Identity Mappings in Deep Residual Networks
sequence: 6
section: 5 Results
section_role: results
section_index: 11
pages: [11, 12, 13]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "Comparisons on CIFAR-10/100. Table 4 compares the state-of-the-art methods on CIFAR-10/100, where we achieve competitive results. We note that we do…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5 Results

> Section 11 of 12 from [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md) · `results` · pages 11-13

Comparisons on CIFAR-10/100. Table 4 compares the state-of-the-art methods on CIFAR-10/100, where we achieve competitive results. We note that we do not specially tailor the network width or filter sizes, nor use regularization techniques (such as dropout) which are very eﬀective for these small datasets. We obtain these results via a simple but essential concept — going deeper. These results demonstrate the potential of pushing the limits of depth.

Comparisons on ImageNet. Next we report experimental results on the 1000class ImageNet dataset \[3\]. We have done preliminary experiments using the skip connections studied in Fig. 2 & 3 on ImageNet with ResNet-101 \[1\], and observed similar optimization diﬃculties. The training error of these non-identity shortcut networks is obviously higher than the original ResNet at the first learning rate

Table 5. Comparisons of single-crop error on the ILSVRC 2012 validation set. All ResNets are trained using the same hyper-parameters and implementations as \[1\]). Our Residual Units are the full pre-activation version (Fig. 4(e)). †: code/model available at https://github.com/facebook/fb.resnet.torch/tree/master/pretrained, using scale and aspect ratio augmentation in \[20\].

method augmentation train crop test crop top-1 top-5 ResNet-152, original Residual Unit \[1\] scale 224×224 224×224 23.0 6.7 ResNet-152, original Residual Unit \[1\] scale 224×224 320×320 21.3 5.5 ResNet-152, pre-act Residual Unit scale 224×224 320×320 21.1 5.5 ResNet-200, original Residual Unit \[1\] scale 224×224 320×320 21.8 6.0 ResNet-200, pre-act Residual Unit scale 224×224 320×320 20.7 5.3 ResNet-200, pre-act Residual Unit scale+asp ratio 224×224 320×320 20.1† 4.8†

Inception v3 \[19\] scale+asp ratio 299×299 299×299 21.2 5.6

(similar to Fig. 3), and we decided to halt training due to limited resources. But we did finish a “BN after addition” version (Fig. 4(b)) of ResNet-101 on ImageNet and observed higher training loss and validation error. This model’s single-crop (224×224) validation error is 24.6%/7.5%, vs. the original ResNet101’s 23.6%/7.1%. This is in line with the results on CIFAR in Fig. 6 (left). Table 5 shows the results of ResNet-152 \[1\] and ResNet-2003, all trained from scratch. We notice that the original ResNet paper \[1\] trained the models using scale jittering with shorter side s ∈\[256, 480\], and so the test of a 224×224 crop on s = 256 (as did in \[1\]) is negatively biased. Instead, we test a single 320×320 crop from s = 320, for all original and our ResNets. Even though the ResNets are trained on smaller crops, they can be easily tested on larger crops because the ResNets are fully convolutional by design. This size is also close to 299×299 used by Inception v3 \[19\], allowing a fairer comparison.

The original ResNet-152 \[1\] has top-1 error of 21.3% on a 320×320 crop, and our pre-activation counterpart has 21.1%. The gain is not big on ResNet-152 because this model has not shown severe generalization diﬃculties. However, the original ResNet-200 has an error rate of 21.8%, higher than the baseline ResNet-152. But we find that the original ResNet-200 has lower training error than ResNet-152, suggesting that it suﬀers from overfitting.

Our pre-activation ResNet-200 has an error rate of 20.7%, which is 1.1% lower than the baseline ResNet-200 and also lower than the two versions of ResNet-152. When using the scale and aspect ratio augmentation of \[20,19\], our ResNet-200 has a result better than Inception v3 \[19\] (Table 5). Concurrent with our work, an Inception-ResNet-v2 model \[21\] achieves a single-crop result of 19.9%/4.9%. We expect our observations and the proposed Residual Unit will help this type and generally other types of ResNets.

Computational Cost. Our models’ computational complexity is linear on

3 The ResNet-200 has 16 more 3-layer bottleneck Residual Units than ResNet-152, which are added on the feature map of 28×28.

depth (so a 1001-layer net is ∼10× complex of a 100-layer net). On CIFAR, ResNet-1001 takes about 27 hours to train on 2 GPUs; on ImageNet, ResNet200 takes about 3 weeks to train on 8 GPUs (on par with VGG nets \[22\]).

---

Full document: [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md) · Page-level evidence: [paper-pages/06-identity-mappings-in-deep-residual-networks](../../paper-pages/06-identity-mappings-in-deep-residual-networks/index.md)
