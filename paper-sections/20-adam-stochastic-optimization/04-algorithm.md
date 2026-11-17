---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
section: 2 ALGORITHM
section_role: method
section_index: 4
pages: [1, 2]
topics: ["../../topics/optimization.md"]
description: "See algorithm 1 for pseudo-code of our proposed algorithm Adam. Let f(θ) be a noisy objective function: a stochastic scalar function that is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 ALGORITHM

> Section 4 of 13 from [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · `method` · pages 1-2

See algorithm 1 for pseudo-code of our proposed algorithm Adam. Let f(θ) be a noisy objective function: a stochastic scalar function that is differentiable w.r.t. parameters θ. We are interested in minimizing the expected value of this function, E\[f(θ)\] w.r.t. its parameters θ. With f1(θ), ..., , fT (θ) we denote the realisations of the stochastic function at subsequent timesteps 1, ..., T. The stochasticity might come from the evaluation at random subsamples (minibatches) of datapoints, or arise from inherent function noise. With gt = ∇θft(θ) we denote the gradient, i.e. the vector of partial derivatives of ft, w.r.t θ evaluated at timestep t.

The algorithm updates exponential moving averages of the gradient (mt) and the squared gradient (vt) where the hyper-parameters β1, β2 ∈\[0, 1) control the exponential decay rates of these moving averages. The moving averages themselves are estimates of the 1st moment (the mean) and the 2nd raw moment (the uncentered variance) of the gradient. However, these moving averages are initialized as (vectors of) 0’s, leading to moment estimates that are biased towards zero, especially during the initial timesteps, and especially when the decay rates are small (i.e. the βs are close to 1). The good news is that this initialization bias can be easily counteracted, resulting in bias-corrected estimates bmt and bvt. See section 3 for more details.

Note that the efficiency of algorithm 1 can, at the expense of clarity, be improved upon by changing the order of computation, e.g. by replacing the last three lines in the loop with the following lines: αt = α ·

p

1 −βt 2/(1 −βt 1) and θt ←θt−1 −αt · mt/(√vt + ˆϵ).

2.1 ADAM’S UPDATE RULE

An important property of Adam’s update rule is its careful choice of stepsizes. Assuming ϵ = 0, the effective step taken in parameter space at timestep t is ∆t = α · bmt/√bvt. The effective stepsize has two upper bounds: |∆t| ≤α · (1 −β1)/√1 −β2 in the case (1 −β1) > √1 −β2, and |∆t| ≤α

2

Published as a conference paper at ICLR 2015

otherwise. The first case only happens in the most severe case of sparsity: when a gradient has been zero at all timesteps except at the current timestep. For less sparse cases, the effective stepsize will be smaller. When (1 −β1) = √1 −β2 we have that | bmt/√bvt| < 1 therefore |∆t| < α. In more common scenarios, we will have that bmt/√bvt ≈±1 since |E\[g\]/

p

E\[g2\]| ≤1. The effective magnitude of the steps taken in parameter space at each timestep are approximately bounded by the stepsize setting α, i.e., |∆t| ⪅α. This can be understood as establishing a trust region around the current parameter value, beyond which the current gradient estimate does not provide sufficient information. This typically makes it relatively easy to know the right scale of α in advance. For many machine learning models, for instance, we often know in advance that good optima are with high probability within some set region in parameter space; it is not uncommon, for example, to have a prior distribution over the parameters. Since α sets (an upper bound of) the magnitude of steps in parameter space, we can often deduce the right order of magnitude of α such that optima can be reached from θ0 within some number of iterations. With a slight abuse of terminology, we will call the ratio bmt/√bvt the signal-to-noise ratio (SNR). With a smaller SNR the effective stepsize ∆t will be closer to zero. This is a desirable property, since a smaller SNR means that there is greater uncertainty about whether the direction of bmt corresponds to the direction of the true gradient. For example, the SNR value typically becomes closer to 0 towards an optimum, leading to smaller effective steps in parameter space: a form of automatic annealing. The effective stepsize ∆t is also invariant to the scale of the gradients; rescaling the gradients g with factor c will scale bmt with a factor c and bvt with a factor c2, which cancel out: (c · bmt)/(√

c2 · bvt) = bmt/√bvt.

---

Full document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · Page-level evidence: [paper-pages/20-adam-stochastic-optimization](../../paper-pages/20-adam-stochastic-optimization/index.md)
