---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
page: 1
pages: [1]
page_of: 15
topics: ["../../topics/optimization.md"]
description: "Published as a conference paper at ICLR 2015 Algorithm 1: Adam, our proposed algorithm for stochastic optimization. See section 2 for details, and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 15 - Adam: A Method for Stochastic Optimization

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md)

Published as a conference paper at ICLR 2015

Algorithm 1: Adam, our proposed algorithm for stochastic optimization. See section 2 for details, and for a slightly more efficient (but less clear) order of computation. g2

t indicates the elementwise square gt ⊙gt. Good default settings for the tested machine learning problems are α = 0.001, β1 = 0.9, β2 = 0.999 and ϵ = 10−8. All operations on vectors are element-wise. With βt

1 and βt 2 we denote β1 and β2 to the power t. Require: α: Stepsize Require: β1, β2 ∈\[0, 1): Exponential decay rates for the moment estimates Require: f(θ): Stochastic objective function with parameters θ Require: θ0: Initial parameter vector

m0 ←0 (Initialize 1st moment vector) v0 ←0 (Initialize 2nd moment vector) t ←0 (Initialize timestep) while θt not converged do

t ←t + 1 gt ←∇θft(θt−1) (Get gradients w.r.t. stochastic objective at timestep t) mt ←β1 · mt−1 + (1 −β1) · gt (Update biased first moment estimate) vt ←β2 · vt−1 + (1 −β2) · g2

t (Update biased second raw moment estimate) bmt ←mt/(1 −βt

1) (Compute bias-corrected first moment estimate) bvt ←vt/(1 −βt

2) (Compute bias-corrected second raw moment estimate) θt ←θt−1 −α · bmt/(√bvt + ϵ) (Update parameters) end while return θt (Resulting parameters)

In section 2 we describe the algorithm and the properties of its update rule. Section 3 explains our initialization bias correction technique, and section 4 provides a theoretical analysis of Adam’s convergence in online convex programming. Empirically, our method consistently outperforms other methods for a variety of models and datasets, as shown in section 6. Overall, we show that Adam is a versatile algorithm that scales to large-scale high-dimensional machine learning problems.

## 2 ALGORITHM

See algorithm 1 for pseudo-code of our proposed algorithm Adam. Let f(θ) be a noisy objective function: a stochastic scalar function that is differentiable w.r.t. parameters θ. We are interested in minimizing the expected value of this function, E\[f(θ)\] w.r.t. its parameters θ. With f1(θ), ..., , fT (θ) we denote the realisations of the stochastic function at subsequent timesteps 1, ..., T. The stochasticity might come from the evaluation at random subsamples (minibatches) of datapoints, or arise from inherent function noise. With gt = ∇θft(θ) we denote the gradient, i.e. the vector of partial derivatives of ft, w.r.t θ evaluated at timestep t.

The algorithm updates exponential moving averages of the gradient (mt) and the squared gradient (vt) where the hyper-parameters β1, β2 ∈\[0, 1) control the exponential decay rates of these moving averages. The moving averages themselves are estimates of the 1st moment (the mean) and the 2nd raw moment (the uncentered variance) of the gradient. However, these moving averages are initialized as (vectors of) 0’s, leading to moment estimates that are biased towards zero, especially during the initial timesteps, and especially when the decay rates are small (i.e. the βs are close to 1). The good news is that this initialization bias can be easily counteracted, resulting in bias-corrected estimates bmt and bvt. See section 3 for more details.

Note that the efficiency of algorithm 1 can, at the expense of clarity, be improved upon by changing the order of computation, e.g. by replacing the last three lines in the loop with the following lines: αt = α ·

p

1 −βt 2/(1 −βt 1) and θt ←θt−1 −αt · mt/(√vt + ˆϵ).

2.1 ADAM’S UPDATE RULE

An important property of Adam’s update rule is its careful choice of stepsizes. Assuming ϵ = 0, the effective step taken in parameter space at timestep t is ∆t = α · bmt/√bvt. The effective stepsize has two upper bounds: |∆t| ≤α · (1 −β1)/√1 −β2 in the case (1 −β1) > √1 −β2, and |∆t| ≤α

2

---

first page · [next page](page-002.md) · [all pages](index.md)
