---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/05-deep-residual-learning-resnet.md
source: ../../papers/05-deep-residual-learning-resnet.md
paper_title: Deep Residual Learning for Image Recognition
sequence: 5
section: 3.4. Implementation
section_role: experiments
section_index: 9
pages: [3]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "3x3 conv, 64 3x3 conv, 64 Our implementation for ImageNet follows the practice in [21, 41]. The image is resized with its shorter side randomly…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.4. Implementation

> Section 9 of 21 from [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · `experiments` · pages 3-3

3x3 conv, 64

3x3 conv, 64

Our implementation for ImageNet follows the practice in \[21, 41\]. The image is resized with its shorter side randomly sampled in \[256, 480\] for scale augmentation \[41\]. A 224×224 crop is randomly sampled from an image or its horizontal flip, with the per-pixel mean subtracted \[21\]. The standard color augmentation in \[21\] is used. We adopt batch normalization (BN) \[16\] right after each convolution and before activation, following \[16\]. We initialize the weights as in \[13\] and train all plain/residual nets from scratch. We use SGD with a mini-batch size of 256. The learning rate starts from 0.1 and is divided by 10 when the error plateaus, and the models are trained for up to 60 × 104 iterations. We use a weight decay of 0.0001 and a momentum of 0.9. We do not use dropout \[14\], following the practice in \[16\].

pool, /2

3x3 conv, 128, /2

3x3 conv, 128, /2

output size: 28

3x3 conv, 512

3x3 conv, 128

3x3 conv, 128

3x3 conv, 512

3x3 conv, 128

3x3 conv, 128

3x3 conv, 512

3x3 conv, 128

3x3 conv, 128

3x3 conv, 512

3x3 conv, 128

3x3 conv, 128

3x3 conv, 128

3x3 conv, 128

3x3 conv, 128

3x3 conv, 128

3x3 conv, 128

3x3 conv, 128

output size: 14

pool, /2

3x3 conv, 256, /2

3x3 conv, 256, /2

3x3 conv, 512

3x3 conv, 256

3x3 conv, 256

3x3 conv, 512

3x3 conv, 256

3x3 conv, 256

3x3 conv, 512

3x3 conv, 256

3x3 conv, 256

3x3 conv, 512

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

In testing, for comparison studies we adopt the standard 10-crop testing \[21\]. For best results, we adopt the fullyconvolutional form as in \[41, 13\], and average the scores at multiple scales (images are resized such that the shorter side is in {224, 256, 384, 480, 640}).

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

3x3 conv, 256

---

Full document: [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · Page-level evidence: [paper-pages/05-deep-residual-learning-resnet](../../paper-pages/05-deep-residual-learning-resnet/index.md)
