---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 4.1 Data Augmentation
section_role: other
section_index: 12
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "The easiest and most common method to reduce overfitting on image data is to artificially enlarge the dataset using label-preserving transformations…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.1 Data Augmentation

> Section 12 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

The easiest and most common method to reduce overfitting on image data is to artificially enlarge
the dataset using label-preserving transformations (e.g., [25, 4, 5]). We employ two distinct forms
of data augmentation, both of which allow transformed images to be produced from the original
images with very little computation, so the transformed images do not need to be stored on disk.
In our implementation, the transformed images are generated in Python code on the CPU while the
GPU is training on the previous batch of images. So these data augmentation schemes are, in effect,
computationally free.

The first form of data augmentation consists of generating image translations and horizontal reflections. We do this by extracting random 224×224 patches (and their horizontal reflections) from the
256×256 images and training our network on these extracted patches4. This increases the size of our
training set by a factor of 2048, though the resulting training examples are, of course, highly interdependent. Without this scheme, our network suffers from substantial overfitting, which would have
forced us to use much smaller networks. At test time, the network makes a prediction by extracting
five 224 *×* 224 patches (the four corner patches and the center patch) as well as their horizontal
reflections (hence ten patches in all), and averaging the predictions made by the network’s softmax
layer on the ten patches.

$$
256\times256
$$

The second form of data augmentation consists of altering the intensities of the RGB channels in
training images. Specifically, we perform PCA on the set of RGB pixel values throughout the
ImageNet training set. To each training image, we add multiples of the found principal components,

4This is the reason why the input images in Figure 2 are 224 *×* 224 *×* 3-dimensional.

with magnitudes proportional to the corresponding eigenvalues times a random variable drawn from
a Gaussian with mean zero and standard deviation 0.1. Therefore to each RGB image pixel Ixy =
[IxyR,IxyG,IxyB]T we add the following quantity:

$$
I_{xy}=
[I_{x y}^{R},I_{x y}^{G},I_{x y}^{B}]^{T}
$$

$$
[\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}][\alpha_{1}\lambda_{1},\alpha_{2}\lambda_{2},\alpha_{3}\lambda_{3}]^{T}
$$

where pi and λi are ith eigenvector and eigenvalue of the 3 × 3 covariance matrix of RGB pixel
values, respectively, and αi is the aforementioned random variable. Each αi is drawn only once
for all the pixels of a particular training image until that image is used for training again, at which
point it is re-drawn. This scheme approximately captures an important property of natural images,
namely, that object identity is invariant to changes in the intensity and color of the illumination. This
scheme reduces the top-1 error rate by over 1%.

$$
\mathbf{p}_{i}
$$

$$
\lambda_{i}
$$

$$
3\times3
$$

$$
\alpha_{i}
$$

$$
\alpha_{i}
$$

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
