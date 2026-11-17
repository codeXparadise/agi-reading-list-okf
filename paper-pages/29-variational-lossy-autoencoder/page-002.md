---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/29-variational-lossy-autoencoder.md
source: ../../papers/29-variational-lossy-autoencoder.md
paper_title: Variational Lossy Autoencoder
sequence: 29
page: 2
pages: [2]
page_of: 17
topics: ["../../topics/generative-models.md", "../../topics/minimum-description-length.md"]
description: "Published as a conference paper at ICLR 2017 in previous work applying VAE to sequence modeling (Fabius & van Amersfoort, 2014; Chung et al., 2015;…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 17 - Variational Lossy Autoencoder

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [29 - Variational Lossy Autoencoder](../../papers/29-variational-lossy-autoencoder.md)

Published as a conference paper at ICLR 2017

in previous work applying VAE to sequence modeling (Fabius & van Amersfoort, 2014; Chung et al., 2015; Bowman et al., 2015; Serban et al., 2016; Fraccaro et al., 2016; Xu & Sun, 2016), where the decoding distribution is a powerful RNN with autoregressive dependency, i.e., p(x|z) = Q

i p(xi|z, x<i). Since RNNs are universal function approximators and any joint distribution over x admits an autoregressive factorization, the RNN autoregressive decoding distribution can in theory represent any probability distribution even without dependence on z.

However, previous attempts have found it hard to benefit from VAE when using an expressive decoding distribution p(x|z). Indeed it’s documented in detail by Bowman et al. (2015) that in most cases when an RNN autoregressive decoding distribution is used, the latent code z is completely ignored and the model regresses to be a standard unconditional RNN autoregressive distribution that doesn’t depend on the latent code. This phenomenon is commonly attributed to “optimization challenges” of VAE in the literature (Bowman et al., 2015; Serban et al., 2016; Kaae Sønderby et al., 2016) because early in the training the approximate posterior q(z|x) carries little information about datapoint x and hence it’s easy for the model to just set the approximate posterior to be the prior to avoid paying any regularization cost DKL(q(z|x)||p(z)).

Here we present a simple but often-neglected observation that this phenomenon arises not just due to optimization challenges and instead even if we can solve the optimization problems exactly, the latent code should still be ignored at optimum for most practical instances of VAE that have intractable true posterior distributions and sufficiently powerful decoders. It is easiest to understand this observation from a Bits-Back Coding perspective of VAE.

It is well-known that Bits-Back Coding is an information-theoretic view of Variational Inference (Hinton & Van Camp, 1993; Honkela & Valpola, 2004) and specific links have been established between Bits-Back Coding and the Helmholtz Machine/VAE (Hinton & Zemel, 1994; Gregor et al., 2013). Here we briefly relate VAE to Bits-Back Coding for self-containedness:

First recall that the goal of designing an efficient coding protocol is to minimize the expected code length of communicating x. To explain Bits-Back Coding, let’s first consider a more naive coding scheme. VAE can be seen as a way to encode data in a two-part code: p(z) and p(x|z), where z can be seen as the essence/structure of a datum and is encoded first and then the modeling error (deviation from z’s structure) is encoded next. The expected code length under this naive coding scheme for a given data distribution is hence:

Cnaive(x) = Ex∼data,z∼q(z|x) \[−log p(z) −log p(x|z)\] (5)

This coding scheme is, however, inefficient. Bits-Back Coding improves on it by noticing that the encoder distribution q(z|x) can be used to transmit additional information, up to H(q(z|x)) expected nats, as long as the receiver also has access to q(z|x). The decoding scheme works as follows: a receiver first decodes z from p(z), then decodes x from p(x|z) and, by running the same approximate posterior that the sender is using, decodes a secondary message from q(z|x). Hence, to properly measure the code length of VAE’s two-part code, we need to subtract the extra information from q(z|x). Using Bit-Back Coding, the expected code length equates to the negative variational lower bound or the so-called Helmholtz variational free energy, which means minimizing code length is equivalent to maximizing the variational lower bound:

CBitsBack(x) = Ex∼data,z∼q(z|x) \[log q(z|x) −log p(z) −log p(x|z)\] (6)

= Ex∼data \[−L(x)\] (7)

Casting the problem of optimizing VAE into designing an efficient coding scheme easily allows us to reason when the latent code z will be used: the latent code z will be used when the two-part code is an efficient code. Recalling that the lower-bound of expected code length for data is given by the Shannon entropy of data generation distribution: H(data) = Ex∼data \[−log pdata(x)\], we can analyze VAE’s coding efficiency:

CBitsBack(x) = Ex∼data,z∼q(z|x) \[log q(z|x) −log p(z) −log p(x|z)\] (8)

= Ex∼data \[−log p(x) + DKL(q(z|x)||p(z|x))\] (9) ≥Ex∼data \[−log pdata(x) + DKL(q(z|x)||p(z|x))\] (10) = H(data) + Ex∼data \[DKL(q(z|x)||p(z|x))\] (11)

3

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
