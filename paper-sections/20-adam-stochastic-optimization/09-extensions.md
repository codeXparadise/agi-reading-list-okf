---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
section: 7 EXTENSIONS
section_role: other
section_index: 9
pages: [7, 8]
topics: ["../../topics/optimization.md"]
description: "7.1 ADAMAX In Adam, the update rule for individual weights is to scale their gradients inversely proportional to a (scaled) L2 norm of their…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7 EXTENSIONS

> Section 9 of 13 from [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · `other` · pages 7-8

7.1 ADAMAX

In Adam, the update rule for individual weights is to scale their gradients inversely proportional to a (scaled) L2 norm of their individual current and past gradients. We can generalize the L2 norm based update rule to a Lp norm based update rule. Such variants become numerically unstable for large p. However, in the special case where we let p →∞, a surprisingly simple and stable algorithm emerges; see algorithm 2. We’ll now derive the algorithm. Let, in case of the Lp norm, the stepsize at time t be inversely proportional to v1/p

t , where:

vt = βp

2vt−1 + (1 −βp 2)|gt|p (6)

t X

βp(t−i)

= (1 −βp

2 · |gi|p (7)

2)

i=1

8

Published as a conference paper at ICLR 2015

Algorithm 2: AdaMax, a variant of Adam based on the infinity norm. See section 7.1 for details. Good default settings for the tested machine learning problems are α = 0.002, β1 = 0.9 and β2 = 0.999. With βt

1 we denote β1 to the power t. Here, (α/(1 −βt 1)) is the learning rate with the bias-correction term for the first moment. All operations on vectors are element-wise. Require: α: Stepsize Require: β1, β2 ∈\[0, 1): Exponential decay rates Require: f(θ): Stochastic objective function with parameters θ Require: θ0: Initial parameter vector

m0 ←0 (Initialize 1st moment vector) u0 ←0 (Initialize the exponentially weighted infinity norm) t ←0 (Initialize timestep) while θt not converged do

t ←t + 1 gt ←∇θft(θt−1) (Get gradients w.r.t. stochastic objective at timestep t) mt ←β1 · mt−1 + (1 −β1) · gt (Update biased first moment estimate) ut ←max(β2 · ut−1, |gt|) (Update the exponentially weighted infinity norm) θt ←θt−1 −(α/(1 −βt

1)) · mt/ut (Update parameters) end while return θt (Resulting parameters)

Note that the decay term is here equivalently parameterised as βp

2 instead of β2. Now let p →∞, and define ut = limp→∞(vt)1/p, then:

2 · |gi|p !1/p

t X

p→∞(vt)1/p = lim

βp(t−i)

(1 −βp

(8)

ut = lim

2)

p→∞

i=1

2)1/p t X

2 · |gi|p !1/p

βp(t−i)

p→∞(1 −βp

(9)

= lim

i=1

t X

!1/p

2 · |gi| p

β(t−i)

(10)

= lim

p→∞

i=1

βt−1

2 |g1|, βt−2

(11)

2 |g2|, . . . , β2|gt−1|, |gt|

= max

Which corresponds to the remarkably simple recursive formula:

ut = max(β2 · ut−1, |gt|) (12)

with initial value u0 = 0. Note that, conveniently enough, we don’t need to correct for initialization bias in this case. Also note that the magnitude of parameter updates has a simpler bound with AdaMax than Adam, namely: |∆t| ≤α.

7.2 TEMPORAL AVERAGING

Since the last iterate is noisy due to stochastic approximation, better generalization performance is often achieved by averaging. Previously in Moulines & Bach (2011), Polyak-Ruppert averaging (Polyak & Juditsky, 1992; Ruppert, 1988) has been shown to improve the convergence of standard SGD, where ¯θt = 1

Pn

k=1 θk. Alternatively, an exponential moving average over the parameters can be used, giving higher weight to more recent parameter values. This can be trivially implemented by adding one line to the inner loop of algorithms 1 and 2: ¯θt ←β2 · ¯θt−1 +(1−β2)θt, with ¯θ0 = 0. Initalization bias can again be corrected by the estimator bθt = ¯θt/(1 −βt

t

2).

---

Full document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · Page-level evidence: [paper-pages/20-adam-stochastic-optimization](../../paper-pages/20-adam-stochastic-optimization/index.md)
