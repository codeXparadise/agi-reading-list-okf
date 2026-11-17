---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
page: 4
pages: [4]
page_of: 9
topics: ["../../topics/generative-models.md"]
description: "Theorem 1. The global minimum of the virtual training criterion C(G) is achieved if and only if pg = pdata. At that point, C(G) achieves the value…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 9 - Generative Adversarial Nets

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md)

Theorem 1. The global minimum of the virtual training criterion C(G) is achieved if and only if pg = pdata. At that point, C(G) achieves the value −log 4.

G(x) = 1

2, (consider Eq. 2). Hence, by inspecting Eq. 4 at D∗ G(x) = 1

Proof. For pg = pdata, D∗

2, we find C(G) = log 1

2 + log 1 2 = −log 4. To see that this is the best possible value of C(G), reached only for pg = pdata, observe that

Ex∼pdata \[−log 2\] + Ex∼pg \[−log 2\] = −log 4

and that by subtracting this expression from C(G) = V (D∗

G, G), we obtain:

pdata + pg

pdata + pg

C(G) = −log(4) + KL

pdata

+ KL

pg

(5)

2

2

where KL is the Kullback–Leibler divergence. We recognize in the previous expression the Jensen– Shannon divergence between the model’s distribution and the data generating process:

C(G) = −log(4) + 2 · JSD (pdata ∥pg ) (6)

Since the Jensen–Shannon divergence between two distributions is always non-negative and zero only when they are equal, we have shown that C∗= −log(4) is the global minimum of C(G) and that the only solution is pg = pdata, i.e., the generative model perfectly replicating the data generating process.

## 4.2 Convergence of Algorithm 1

Proposition 2. If G and D have enough capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum given G, and pg is updated so as to improve the criterion

Ex∼pdata\[log D∗

G(x)\] + Ex∼pg\[log(1 −D∗

G(x))\]

then pg converges to pdata

Proof. Consider V (G, D) = U(pg, D) as a function of pg as done in the above criterion. Note that U(pg, D) is convex in pg. The subderivatives of a supremum of convex functions include the derivative of the function at the point where the maximum is attained. In other words, if f(x) = supα∈A fα(x) and fα(x) is convex in x for every α, then ∂fβ(x) ∈∂f if β = arg supα∈A fα(x). This is equivalent to computing a gradient descent update for pg at the optimal D given the corresponding G. supD U(pg, D) is convex in pg with a unique global optima as proven in Thm 1, therefore with sufficiently small updates of pg, pg converges to px, concluding the proof.

In practice, adversarial nets represent a limited family of pg distributions via the function G(z; θg), and we optimize θg rather than pg itself. Using a multilayer perceptron to define G introduces multiple critical points in parameter space. However, the excellent performance of multilayer perceptrons in practice suggests that they are a reasonable model to use despite their lack of theoretical guarantees.

## 5 Experiments

We trained adversarial nets an a range of datasets including MNIST\[23\], the Toronto Face Database (TFD) \[28\], and CIFAR-10 \[21\]. The generator nets used a mixture of rectifier linear activations \[19, 9\] and sigmoid activations, while the discriminator net used maxout \[10\] activations. Dropout \[17\] was applied in training the discriminator net. While our theoretical framework permits the use of dropout and other noise at intermediate layers of the generator, we used noise as the input to only the bottommost layer of the generator network.

We estimate probability of the test set data under pg by fitting a Gaussian Parzen window to the samples generated with G and reporting the log-likelihood under this distribution. The σ parameter

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
