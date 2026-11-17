---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
page: 3
pages: [3]
page_of: 9
topics: ["../../topics/generative-models.md"]
description: "Algorithm 1 Minibatch stochastic gradient descent training of generative adversarial nets. The number of steps to apply to the discriminator, k, is a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 9 - Generative Adversarial Nets

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md)

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

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
