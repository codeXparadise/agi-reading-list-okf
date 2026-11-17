---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
section: 4 Theoretical Results
section_role: other
section_index: 6
pages: [2, 3, 4]
topics: ["../../topics/generative-models.md"]
description: "The generator G implicitly defines a probability distribution pg as the distribution of the samples G(z) obtained when z ∼pz. Therefore, we would…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4 Theoretical Results

> Section 6 of 12 from [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · `other` · pages 2-4

The generator G implicitly defines a probability distribution pg as the distribution of the samples G(z) obtained when z ∼pz. Therefore, we would like Algorithm 1 to converge to a good estimator of pdata, if given enough capacity and training time. The results of this section are done in a nonparametric setting, e.g. we represent a model with infinite capacity by studying convergence in the space of probability density functions.

We will show in section 4.1 that this minimax game has a global optimum for pg = pdata. We will then show in section 4.2 that Algorithm 1 optimizes Eq 1, thus obtaining the desired result.

Algorithm 1 Minibatch stochastic gradient descent training of generative adversarial nets. The number of steps to apply to the discriminator, k, is a hyperparameter. We used k = 1, the least expensive option, in our experiments.

for number of training iterations do

for k steps do

• Sample minibatch of m noise samples {z(1), . . . , z(m)} from noise prior pg(z). • Sample minibatch of m examples {x(1), . . . , x(m)} from data generating distribution pdata(x). • Update the discriminator by ascending its stochastic gradient:

m X

1 m

h

x(i)

1 −D 

z(i)i

∇θd

log D

+ log

G

.

i=1

end for • Sample minibatch of m noise samples {z(1), . . . , z(m)} from noise prior pg(z). • Update the generator by descending its stochastic gradient:

m X

1 m

1 −D 

z(i)

∇θg

log

G

.

i=1

end for The gradient-based updates can use any standard gradient-based learning rule. We used momentum in our experiments.

4.1 Global Optimality of pg = pdata

We first consider the optimal discriminator D for any given generator G.

Proposition 1. For G fixed, the optimal discriminator D is

G(x) = pdata(x) pdata(x) + pg(x) (2)

D∗

Proof. The training criterion for the discriminator D, given any generator G, is to maximize the quantity V (G, D)

Z

Z

pz(z) log(1 −D(g(z)))dz

V (G, D) =

pdata(x) log(D(x))dx +

## x

z

Z

pdata(x) log(D(x)) + pg(x) log(1 −D(x))dx (3)

=

## x

For any (a, b) ∈R2 \\ {0, 0}, the function y →a log(y) + b log(1 −y) achieves its maximum in \[0, 1\] at a a+b. The discriminator does not need to be defined outside of Supp(pdata) ∪Supp(pg), concluding the proof.

Note that the training objective for D can be interpreted as maximizing the log-likelihood for estimating the conditional probability P(Y = y|x), where Y indicates whether x comes from pdata (with y = 1) or from pg (with y = 0). The minimax game in Eq. 1 can now be reformulated as:

C(G) = max

D V (G, D)

=Ex∼pdata\[log D∗

G(x)\] + Ez∼pz\[log(1 −D∗

G(G(z)))\] (4) =Ex∼pdata\[log D∗

G(x)\] + Ex∼pg\[log(1 −D∗

G(x))\]

log pdata(x) Pdata(x) + pg(x)

log pg(x) pdata(x) + pg(x)

=Ex∼pdata

+ Ex∼pg

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

---

Full document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · Page-level evidence: [paper-pages/28-generative-adversarial-nets](../../paper-pages/28-generative-adversarial-nets/index.md)
