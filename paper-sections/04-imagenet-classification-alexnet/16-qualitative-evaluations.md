---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 6.1 Qualitative Evaluations
section_role: other
section_index: 16
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "Figure 3 shows the convolutional kernels learned by the network’s two data-connected layers. The network has learned a variety of frequency- and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.1 Qualitative Evaluations

> Section 16 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

Figure 3 shows the convolutional kernels learned by the network’s two data-connected layers. The
network has learned a variety of frequency- and orientation-selective kernels, as well as various colored blobs. Notice the specialization exhibited by the two GPUs, a result of the restricted connectivity described in Section 3.5. The kernels on GPU 1 are largely color-agnostic, while the kernels
on on GPU 2 are largely color-specific. This kind of specialization occurs during every run and is
independent of any particular random weight initialization (modulo a renumbering of the GPUs).

5The error rates without averaging predictions over ten patches as described in Section 4.1 are 39.0% and
18.3%.

mite container ship motor scooter leopard mite black widow container ship motor scooter leopard lifeboat go-kart jaguar cockroach amphibian moped cheetah tick fireboat bumper car snow leopard starfish drilling platform golfcart Egyptian cat grille mushroom cherry Madagascar cat convertible agaric dalmatian squirrel monkey grille mushroom grape spider monkey pickup elderberry titi beach wagon jelly fungus ffordshire bullterrier indri fire engine dead-man's-fingers currant howler monkey

Figure 4: **(Left)** Eight ILSVRC-2010 test images and the five labels considered most probable by our model.
The correct label is written under each image, and the probability assigned to the correct label is also shown
with a red bar (if it happens to be in the top 5). **(Right)** Five ILSVRC-2010 test images in the first column. The
remaining columns show the six training images that produce feature vectors in the last hidden layer with the
smallest Euclidean distance from the feature vector for the test image.

In the left panel of Figure 4 we qualitatively assess what the network has learned by computing its
top-5 predictions on eight test images. Notice that even off-center objects, such as the mite in the
top-left, can be recognized by the net. Most of the top-5 labels appear reasonable. For example,
only other types of cat are considered plausible labels for the leopard. In some cases (grille, cherry)
there is genuine ambiguity about the intended focus of the photograph.

Another way to probe the network’s visual knowledge is to consider the feature activations induced
by an image at the last, 4096-dimensional hidden layer. If two images produce feature activation
vectors with a small Euclidean separation, we can say that the higher levels of the neural network
consider them to be similar. Figure 4 shows five images from the test set and the six images from
the training set that are most similar to each of them according to this measure. Notice that at the
pixel level, the retrieved training images are generally not close in L2 to the query images in the first
column. For example, the retrieved dogs and elephants appear in a variety of poses. We present the
results for many more test images in the supplementary material.

Computing similarity by using Euclidean distance between two 4096-dimensional, real-valued vectors is inefficient, but it could be made efficient by training an auto-encoder to compress these vectors
to short binary codes. This should produce a much better image retrieval method than applying autoencoders to the raw pixels [14], which does not make use of image labels and hence has a tendency
to retrieve images with similar patterns of edges, whether or not they are semantically similar.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
