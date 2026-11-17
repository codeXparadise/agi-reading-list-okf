---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
page: 5
pages: [5]
page_of: 9
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "4 Empirical Results 4.1 Architecture and Hyperparameters No extensive architecture or hyperparameter search of the Ptr-Net was done in the work…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 9 - Pointer Networks

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [12 - Pointer Networks](../../papers/12-pointer-networks.md)

## 4 Empirical Results

## 4.1 Architecture and Hyperparameters

No extensive architecture or hyperparameter search of the Ptr-Net was done in the work presented here, and we used virtually the same architecture throughout all the experiments and datasets. Even though there are likely some gains to be obtained by tuning the model, we felt that having the same model hyperparameters operate on all the problems would make the main message of the paper stronger.

As a result, all our models used a single layer LSTM with either 256 or 512 hidden units, trained with stochastic gradient descent with a learning rate of 1.0, batch size of 128, random uniform weight initialization from -0.08 to 0.08, and L2 gradient clipping of 2.0. We generated 1M training example pairs, and we did observe overfitting in some cases where the task was simpler (i.e., for small n).

## 4.2 Convex Hull

We used the convex hull as the guiding task which allowed us to understand the deficiencies of standard models such as the sequence-to-sequence approach, and also setting up our expectations on what a purely data driven model would be able to achieve with respect to an exact solution.

We reported two metrics: accuracy, and area covered of the true convex hull (note that any simple polygon will have full intersection with the true convex hull). To compute the accuracy, we considered two output sequences C1 and C2 to be the same if they represent the same polygon. For simplicity, we only computed the area coverage for the test examples in which the output represents a simple polygon (i.e., without self-intersections). If an algorithm fails to produce a simple polygon in more than 1% of the cases, we simply reported FAIL.

The results are presented in Table 1. We note that the area coverage achieved with the Ptr-Net is close to 100%. Looking at examples of mistakes, we see that most problems come from points that are aligned (see Figure 3 (d) for a mistake for n = 500) – this is a common source of errors in most algorithms to solve the convex hull.

It was seen that the order in which the inputs are presented to the encoder during inference affects its performance. When the points on the true convex hull are seen “late” in the input sequence, the accuracy is lower. This is possibly the network does not have enough processing steps to “update” the convex hull it computed until the latest points were seen. In order to overcome this problem, we used the attention mechanism described in Section 2.2, which allows the decoder to look at the whole input at any time. This modification boosted the model performance significantly. We inspected what attention was focusing on, and we observed that it was “pointing” at the correct answer on the input side. This inspired us to create the Ptr-Net model described in Section 2.3.

More than outperforming both the LSTM and the LSTM with attention, our model has the key advantage of being inherently variable length. The bottom half of Table 1 shows that, when training our model on a variety of lengths ranging from 5 to 50 (uniformly sampled, as we found other forms of curriculum learning to not be effective), a single model is able to perform quite well on all lengths it has been trained on (but some degradation for n = 50 can be observed w.r.t. the model trained only on length 50 instances). More impressive is the fact that the model does extrapolate to lengths that it has never seen during training. Even for n = 500, our results are satisfactory and indirectly indicate that the model has learned more than a simple lookup. Neither LSTM or LSTM with attention can be used for any given n′̸ = n without training a new model on n′.

## 4.3 Delaunay Triangulation

The Delaunay Triangulation test case is connected to our first problem of finding the convex hull. In fact, the Delaunay Triangulation for a given set of points triangulates the convex hull of these points.

We reported two metrics: accuracy and triangle coverage in percentage (the percentage of triangles the model predicted correctly). Note that, in this case, for an input point set P, the output sequence C(P) is, in fact, a set. As a consequence, any permutation of its elements will represent the same triangulation.

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
