---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 13
pages: [13]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "GPU OpenMPI Our Performance all-reduce all-reduce Gain 4 55359.1 2587.4 21.4 8 48881.6 2470.9 19.8 16 21562.6 1393.7 15.5 32 8191.8 1339.6 6.1 64…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 13 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 13 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

GPU OpenMPI Our Performance all-reduce all-reduce Gain

4 55359.1 2587.4 21.4 8 48881.6 2470.9 19.8 16 21562.6 1393.7 15.5 32 8191.8 1339.6 6.1 64 1395.2 611.0 2.3 128 1602.1 422.6 3.8

Table 7: Comparison of two different all-reduce implementations. All times are in seconds. Performance gain is the ratio of OpenMPI all-reduce time to our all-reduce time.

Language Architecture CPU CTC Time GPU CTC Time Speedup

English 5-layer, 3 RNN 5888.12 203.56 28.9 Mandarin 5-layer, 3 RNN 1688.01 135.05 12.5

Table 8: Comparison of time spent in seconds in computing the CTC loss function and gradient in one epoch for two different implementations. Speedup is the ratio of CPU CTC time to GPU CTC time.

## 4.2 GPU implementation of CTC loss function

Calculating the CTC loss function is more complicated than performing forward and back propagation on our RNN architectures. Originally, we transferred activations from the GPUs to the CPU, where we calculated the loss function using an OpenMP parallelized implementation of CTC. However, this implementation limited our scalability rather significantly, for two reasons. Firstly, it became computationally more significant as we improved efficiency and scalability of the RNN itself. Secondly, transferring large activation matrices between CPU and GPU required us to spend interconnect bandwidth for CTC, rather than on transferring gradient matrices to allow us to scale using data parallelism to more processors.

To overcome this, we wrote a GPU implementation of the CTC loss function. Our parallel implementation relies on a slight refactoring to simplify the dependences in the CTC calculation, as well as the use of optimized parallel sort implementations from ModernGPU \[5\]. We give more details of this parallelization in the Appendix.

Table 8 compares the performance of two CTC implementations. The GPU implementation saves us 95 minutes per epoch in English, and 25 minutes in Mandarin. This reduces overall training time by 10-20%, which is also an important productivity benefit for our experiments.

## 4.3 Memory allocation

Our system makes frequent use of dynamic memory allocations to GPU and CPU memory, mainly to store activation data for variable length utterances, and for intermediate results. Individual allocations can be very large; over 1 GB for the longest utterances. For these very large allocations we found that CUDA’s memory allocator and even std::malloc introduced significant overhead into our application—over a 2x slowdown from using std::malloc in some cases. This is because both cudaMalloc and std::malloc forward very large allocations to the operating system or GPU driver to update the system page tables. This is a good optimization for systems running multiple applications, all sharing memory resources, but editing page tables is pure overhead for our system where nodes are dedicated entirely to running a single model. To get around this limitation, we wrote our own memory allocator for both CPU and GPU allocations. Our implementation follows the approach of the last level shared allocator in jemalloc: all allocations are carved out of contiguous memory blocks using the buddy algorithm \[34\]. To avoid fragmentation, we preallocate all of GPU memory at the start of training and subdivide individual allocations from this block. Similarly, we set the CPU memory block size that we forward to mmap to be substantially larger than std::malloc, at 12GB.

---

[previous page](page-012.md) · [next page](page-014.md) · [all pages](index.md)
