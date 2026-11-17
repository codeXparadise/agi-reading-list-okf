---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 7.1 Batch Dispatch
section_role: other
section_index: 31
pages: [19, 20, 21]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "In order to deploy our relatively large deep neural networks at low latency, we have paid special attention to efficiency during deployment. Most…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7.1 Batch Dispatch

> Section 31 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `other` · pages 19-21

In order to deploy our relatively large deep neural networks at low latency, we have paid special attention to efficiency during deployment. Most internet applications process requests individually as they arrive in the data center. This makes for a straightforward implementation where each request can be managed by one thread. However, processing requests individually is inefficient computationally, for two main reasons. Firstly, when processing requests individually, the processor must load all the weights of the network for each request. This lowers the arithmetic intensity of the workload, and tends to make the computation memory bandwidth bound, as it is difficult to effectively use on-chip caches when requests are presented individually. Secondly, the amount of parallelism that can be exploited to classify one request is limited, making it difficult to exploit SIMD or multicore parallelism. RNNs are especially challenging to deploy because evaluating RNNs sample by

![Figure, page 21](../../assets/15/fig-15-p21-4.png)

10 streams 20 streams 30 streams

0.4

0.3

Probability

0.2

0.1

0.0

0 1 2 3 4 5 6 7 8 9 10 11 Batch size

Figure 5: Probability that a request is processed in a batch of given size

sample relies on sequential matrix vector multiplications, which are bandwidth bound and difficult to parallelize.

To overcome these issues, we built a batching scheduler called Batch Dispatch that assembles streams of data from user requests into batches before performing forward propagation on these batches. In this case, there is a tradeoff between increased batch size, and consequently improved efficiency, and increased latency. The more we buffer user requests to assemble a large batch, the longer users must wait for their results. This places constraints on the amount of batching we can perform.

We use an eager batching scheme that processes each batch as soon as the previous batch is completed, regardless of how much work is ready by that point. This scheduling algorithm has proved to be the best at reducing end-user latency, despite the fact that it is less efficient computationally, since it does not attempt to maximize batch size.

Figure 5 shows the probability that a request is processed in a batch of given size for our production system running on a single NVIDIA Quadro K1200 GPU, with 10-30 concurrent user requests. As expected, batching works best when the server is heavily loaded: as load increases, the distribution shifts to favor processing requests in larger batches. However, even with a light load of only 10 concurrent user requests, our system performs more than half the work in batches with at least 2 samples.

![Figure, page 21](../../assets/15/fig-15-p21-5.png)

50%ile 98%ile

100

latency (ms)

50

0

0 10 20 30 40 Number of concurrent streams

Figure 6: Median and 98 percentile latencies as a function of server load

We see in Figure 6, that our system achieves a median latency of 44 ms, and a 98 percentile latency of 70 ms when loaded with 10 concurrent streams. As the load increases on the server, the batching scheduler shifts work to more efficient batches, which keeps latency low. This shows that Batch Dispatch makes it possible to deploy these large models at high throughput and low latency.

![Figure, page 22](../../assets/15/fig-15-p22-6.png)

0.5

nervana baidu

0.4

TeraFLOP/s

0.3

0.2

0.1

0.0

1 2 3 4 5 6 7 8 9 10 Batch size

Figure 7: Comparison of kernels that compute Ax = b where A is a matrix with dimension 2560 × 2560, and x is a matrix with dimension 2560 × Batch size, where Batch size ∈\[1, 10\]. All matrices are in half-precision format.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
